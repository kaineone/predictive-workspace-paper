#!/usr/bin/env bash
# Build the arXiv source bundle from paper.md; nothing is installed on the host (Docker only).
#
# Usage: arxiv/build-arxiv.sh [git-ref [out-dir]]
#   git-ref   branch, tag or commit to build (default HEAD); sources come from `git archive`,
#             so the working tree is never read or written
#   out-dir   default arxiv/out/<short-sha>; receives:
#       kaine-arxiv-<sha>.tar.gz        the file to upload to arXiv
#       kaine-arxiv-<sha>-proof.pdf     the PDF produced by compiling that tarball, as arXiv will
#       abstract.txt, comments.txt      the abstract and Comments fields in arXiv's metadata form
#       compile.log, MANIFEST.txt, VERIFY.txt
# ARXIV_VECTOR_FIGURES=1 ships each figure as a vector PDF built from its TikZ source instead of the PNG.
#
# Stage 1 (pandoc, pinned image, no network): paper.md -> standalone paper.tex.
# Stage 2 (official texlive/texlive image pinned by digest, no network): xelatex under TeX Live 2025,
#         arXiv's default TeX Live; arXiv has offered the xelatex processor since 2025-11.
# The tarball is unpacked into a fresh directory and compiled from there, so the proof PDF is a
# compile of exactly what is uploaded. No margin note is added: arXiv does not allow margin notes.
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(cd "$HERE/.." && pwd)
REF=${1:-HEAD}
PANDOC_IMAGE=pandoc/extra:3.11-debian@sha256:fa8ccae75418449568f10f1842706aee1885ab24fba54f5aec08516260fc0166
# TeX Live 2025 final state (Docker Hub tag TL2025-historic), pinned by manifest-list digest, 2026-10-31.
TEXLIVE_IMAGE=texlive/texlive@sha256:7056390eac37715fd3e01875037ceb4016cb17d44c611f7bbbfa7a012007979f
for img in "$PANDOC_IMAGE" "$TEXLIVE_IMAGE"; do
  docker image inspect "$img" >/dev/null 2>&1 || docker pull -q "$img" >/dev/null
done

SHA=$(git -C "$REPO" rev-parse --short=8 "$REF^{commit}")
OUT=$(realpath -m "${2:-$HERE/out/$SHA}")
CTIME=$(git -C "$REPO" show -s --format=%ct "$REF^{commit}")
NAME=kaine-arxiv-$SHA
WORK=$(mktemp -d "$HERE/work.XXXXXX"); trap 'rm -rf "$WORK"' EXIT
mkdir -p "$WORK/src" "$WORK/bundle/figures" "$WORK/compile" "$OUT"
git -C "$REPO" archive "$REF" | tar -x -C "$WORK/src"
[ -f "$WORK/src/paper.md" ] || { echo "no paper.md at $REF" >&2; exit 2; }

# --- stage 1: markdown -> tex
python3 -I "$HERE/tools/mk_arxiv_md.py" "$WORK/src/paper.md" "$WORK/src/paper-arxiv.md" "$OUT/abstract.txt"
drun() { docker run --rm --network none --user "$(id -u):$(id -g)" -e HOME=/tmp -e TEXMFVAR=/tmp/texmf-var "$@"; }
drun -v "$WORK/src:/data:Z" -w /data --entrypoint pandoc "$PANDOC_IMAGE" -f markdown+autolink_bare_uris paper-arxiv.md -s -t latex -o paper.tex \
  -V fontsize=11pt -V geometry:margin=1in -V colorlinks=true -V linkcolor=blue \
  -V mainfont=NotoSerif-Regular.ttf \
  -V 'mainfontoptions=BoldFont=NotoSerif-Bold.ttf,ItalicFont=NotoSerif-Italic.ttf,BoldItalicFont=NotoSerif-BoldItalic.ttf'

# --- assemble the bundle: only figures the .tex references
cp "$WORK/src/paper.tex" "$WORK/bundle/paper.tex"
grep -o 'includegraphics\[[^]]*\]{[^}]*}' "$WORK/bundle/paper.tex" | sed 's/.*{\(.*\)}/\1/' | sort -u > "$WORK/figs.txt"
[ -s "$WORK/figs.txt" ] || { echo "no figures found in paper.tex" >&2; exit 1; }
if [ "${ARXIV_VECTOR_FIGURES:-0}" = 1 ]; then
  # Optional: rebuild each figure from its committed TikZ source to a vector PDF (smaller, sharper, searchable
  # text) instead of shipping the committed PNG. Needs figures/<name>.tex next to each <name>.png.
  NAME=$NAME-vec
  while read -r f; do
    b=${f%.png}; [ -f "$WORK/src/$b.tex" ] || { echo "no TikZ source for $f" >&2; exit 1; }
    drun -v "$WORK/src/figures:/data:Z" -w /data "$TEXLIVE_IMAGE" xelatex -interaction=nonstopmode -halt-on-error "$(basename "$b").tex" >/dev/null
    cp "$WORK/src/$b.pdf" "$WORK/bundle/$b.pdf"
    sed -i "s|{$f}|{$b.pdf}|" "$WORK/bundle/paper.tex"
  done < "$WORK/figs.txt"
else
  while read -r f; do cp "$WORK/src/$f" "$WORK/bundle/$f"; done < "$WORK/figs.txt"
fi
cat > "$WORK/bundle/00README.json" <<'J'
{
  "spec_version": 1,
  "process": { "compiler": "xelatex" },
  "sources": [ { "filename": "paper.tex", "usage": "toplevel" } ],
  "texlive_version": 2025,
  "stamp": true
}
J
# reproducible tarball
(cd "$WORK/bundle" && find . -type f | sed 's|^\./||' | LC_ALL=C sort > ../files.txt \
  && tar --owner=0 --group=0 --numeric-owner --mtime="@$CTIME" -cf - -T ../files.txt | gzip -n -9 > "$OUT/$NAME.tar.gz")

# --- stage 2: compile the tarball as arXiv will (fresh dir, TeX Live 2025, xelatex, no network)
tar -xzf "$OUT/$NAME.tar.gz" -C "$WORK/compile"
drun -v "$WORK/compile:/data:Z" -w /data "$TEXLIVE_IMAGE" \
  latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error paper.tex > "$WORK/latexmk.out" 2>&1 \
  || { tail -40 "$WORK/latexmk.out" >&2; cp "$WORK/compile/paper.log" "$OUT/compile.log" 2>/dev/null; echo "xelatex FAILED (log in $OUT/compile.log)" >&2; exit 1; }
cp "$WORK/compile/paper.pdf" "$OUT/$NAME-proof.pdf"
cp "$WORK/compile/paper.log" "$OUT/compile.log"
# arXiv Comments field: pages, figures, status (ASCII; a space after any URL)
PAGES=$(pdfinfo "$OUT/$NAME-proof.pdf" 2>/dev/null | awk '/^Pages:/{print $2}'); NFIG=$(wc -l < "$WORK/figs.txt")
echo "${PAGES:-?} pages, $NFIG figures. Preprint, not peer-reviewed. Includes a disclosure of generative AI use. Code: https://github.com/kaineone/kaine ." > "$OUT/comments.txt"

# --- verify + manifest
python3 -I "$HERE/tools/verify_bundle.py" "$OUT/$NAME.tar.gz" "$OUT/compile.log" "$OUT/abstract.txt" "$OUT/$NAME-proof.pdf" > "$OUT/VERIFY.txt" || { cat "$OUT/VERIFY.txt"; exit 1; }
cat "$OUT/VERIFY.txt"
(cd "$OUT" && tar -tzvf "$NAME.tar.gz" > MANIFEST.txt && sha256sum "$NAME.tar.gz" "$NAME-proof.pdf" >> MANIFEST.txt)
echo "wrote $OUT/$NAME.tar.gz and $OUT/$NAME-proof.pdf"

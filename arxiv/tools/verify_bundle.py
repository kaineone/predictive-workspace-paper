#!/usr/bin/env python3
"""Verify an arXiv source bundle (.tar.gz) and its compile log against arXiv's rules.

Usage: verify_bundle.py <bundle.tar.gz> <compile.log> <abstract.txt> [proof.pdf]
Prints a PASS/WARN/FAIL table; exit 1 on any FAIL.
Rules and sources: the arXiv help pages cited in the README section "Building the arXiv source bundle".
"""
import json
import re
import shutil
import struct
import subprocess
import sys
import tarfile
from pathlib import Path

NAME_OK = re.compile(r"^[A-Za-z0-9_+\-.,=/]+$")  # info.arxiv.org/help/submit/index.html (file names)
AUX_EXT = {".aux", ".log", ".toc", ".lof", ".lot", ".dvi", ".ps", ".out", ".fls", ".fdb_latexmk", ".blg", ".xdv"}
FIG_EXT = {".png", ".jpg", ".jpeg", ".pdf"}
ABSTRACT_LIMIT = 1920
SIZE_FAIL = 30 * 1024 * 1024  # current arXiv pages state no number; 2020 annual report says 50 MB
SIZE_WARN = 10 * 1024 * 1024
MEGAPIXEL_WARN = 34e6
COMPILERS = {"tex", "etex+dvips_ps2pdf", "pdftex", "pdfetex", "latex", "latex+dvips_ps2pdf", "pdflatex", "xelatex"}

rows = []


def add(status, rule, detail=""):
    rows.append((status, rule, detail))


def png_info(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    w, h, _bd, ct, _cm, _fm, il = struct.unpack(">IIBBBBB", data[16:29])
    chunks, i = [], 8
    while i < len(data):
        (n,) = struct.unpack(">I", data[i : i + 4])
        chunks.append(data[i + 4 : i + 8].decode("latin1"))
        i += 12 + n
    return w, h, ct, il, chunks


def check_pdf(proof):
    out = subprocess.run(["pdffonts", str(proof)], capture_output=True, text=True).stdout.splitlines()[2:]
    fonts = [l for l in out if l.strip()]
    t3 = [l.split()[0] for l in fonts if re.search(r"\sType 3\s", l)]
    # columns: name type encoding emb sub uni object-id; emb is the 4th from the right group of yes/no
    noemb = []
    for l in fonts:
        m = re.search(r"\s(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", l)
        if m and m.group(1) == "no":
            noemb.append(l.split()[0])
    add("FAIL" if t3 else "PASS", "PDF: no Type 3 fonts", ", ".join(t3))
    add("FAIL" if noemb else "PASS", "PDF: all fonts embedded", ", ".join(noemb) or f"{len(fonts)} fonts")
    info = subprocess.run(["pdfinfo", str(proof)], capture_output=True, text=True).stdout
    pages = re.search(r"Pages:\s+(\d+)", info).group(1)
    psz = re.search(r"Page size:\s+(.*)", info).group(1)
    add("PASS", "PDF: pages and page size", f"{pages} pages, {psz}")
    txt = subprocess.run(["pdftotext", "-l", "3", str(proof), "-"], capture_output=True, text=True).stdout
    add("PASS" if "KAINE" in txt else "FAIL", "PDF: text extractable", f"{len(txt)} chars in first 3 pages")
    lig = re.search(r"\b(dierent|rst|eect|ofcial|ffi|fi)\b", txt)
    add("WARN" if lig and lig.group(1) not in {"fi"} else "PASS", "PDF: ligatures extract as text", "")


def main():
    bundle, log, abstract = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    proof = Path(sys.argv[4]) if len(sys.argv) > 4 else None
    tf = tarfile.open(bundle, "r:gz")
    members = [m for m in tf.getmembers() if m.isfile()]
    names = [m.name for m in members]
    data = {m.name: tf.extractfile(m).read() for m in members}

    bad = [n for n in names if not NAME_OK.match(n)]
    add("FAIL" if bad else "PASS", "file names", f"bad: {bad}" if bad else f"{len(names)} files, only a-zA-Z0-9_+-.,= characters")
    hidden = [n for n in names if any(p.startswith(".") for p in n.split("/"))]
    add("FAIL" if hidden else "PASS", "no hidden files", str(hidden) if hidden else "none")
    odd = [m.name for m in tf.getmembers() if not (m.isfile() or m.isdir())]
    add("FAIL" if odd else "PASS", "no links or special files", str(odd) if odd else "regular files only")
    aux = [n for n in names if Path(n).suffix.lower() in AUX_EXT]
    add("FAIL" if aux else "PASS", "no aux/output files", str(aux) if aux else "none")
    total = sum(len(v) for v in data.values())
    st = "FAIL" if total > SIZE_FAIL else "WARN" if total > SIZE_WARN else "PASS"
    add(st, "size", f"{total/1e6:.2f} MB uncompressed, {bundle.stat().st_size/1e6:.2f} MB compressed")

    tex = [n for n in names if n.endswith(".tex")]
    tops = [n for n in tex if b"\\documentclass" in data[n]]
    add("PASS" if len(tops) == 1 else "FAIL", "one top-level .tex", f"{tops}")
    src = data[tops[0]].decode("utf-8") if tops else ""
    src_nc = re.sub(r"(?<!\\)%.*", "", src)

    refs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", src_nc)
    missing = [r for r in refs if r not in data]
    badext = [r for r in refs if Path(r).suffix.lower() not in FIG_EXT]
    absol = [r for r in refs if r.startswith("/") or ".." in r]
    unused = [n for n in names if Path(n).suffix.lower() in FIG_EXT and n not in refs]
    problem = missing or badext or absol
    add("FAIL" if problem else "PASS", "figures present, PDF/PNG/JPG, relative, case-exact",
        f"missing={missing} ext={badext} abs={absol}" if problem else f"{len(set(refs))} referenced figures")
    add("FAIL" if unused else "PASS", "no unused figures", str(unused) if unused else "none")
    for r in sorted(set(refs)):
        if r.lower().endswith(".png") and r in data:
            info = png_info(data[r])
            if not info:
                add("FAIL", f"png {r}", "not a PNG")
                continue
            w, h, ct, il, chunks = info
            problems = []
            if ct in (3, 4, 6):
                problems.append("palette/alpha")
            if il:
                problems.append("interlaced")
            problems += [c for c in chunks if c in {"gAMA", "sRGB", "cHRM", "iCCP", "sBIT", "bKGD", "hIST", "tRNS", "sPLT"}]
            if w * h > MEGAPIXEL_WARN:
                problems.append(f"{w*h/1e6:.0f} MP")
            add("WARN" if problems else "PASS", f"png {r}",
                f"{w}x{h}; " + (", ".join(problems) + " (slow or oversize warning)" if problems else "embeds without re-encoding"))

    forbid = {
        r"\\usepackage(\[[^\]]*\])?\{[^}]*eso-pic[^}]*\}": "margin note or watermark (eso-pic)",
        r"\\AddToShipout": "page overlay (margin note or watermark)",
        r"\\usepackage(\[[^\]]*\])?\{[^}]*\blineno\b[^}]*\}": "line numbers",
        r"\\doublespacing|\\linespread\{(1\.[6-9]|[2-9])": "double spacing",
        r"\\pdfoutput": "\\pdfoutput",
        r"\\usepackage(\[[^\]]*\])?\{psfig\}": "psfig",
        r"\\today": "\\today",
        r"\\write18|\\immediate\\write|shell-escape": "shell escape",
        r"\\usepackage(\[[^\]]*\])?\{minted\}": "minted",
        r"\\usepackage(\[[^\]]*\])?\{cleveref\}": "cleveref (broken in TeX Live 2025)",
        r"\\documentclass\[[^\]]*\breferee\b": "referee mode",
    }
    hits = [why for pat, why in forbid.items() if re.search(pat, src_nc)]
    add("FAIL" if hits else "PASS", "no forbidden constructs", ", ".join(hits) if hits else "none")
    m = re.search(r"\\documentclass\[([^\]]*)\]", src_nc)
    sz = re.search(r"\b(\d+)pt\b", m.group(1)) if m else None
    size = sz.group(1) if sz else "10"
    add("PASS" if 10 <= int(size) <= 14 else "FAIL", "type size 10-14 pt", f"{size}pt")
    geo = re.search(r"\\usepackage\[([^\]]*)\]\{geometry\}", src_nc)
    mg = re.search(r"margin=([\d.]+)(in|cm|mm)", geo.group(1)) if geo else None
    inch = {"in": 1.0, "cm": 1 / 2.54, "mm": 1 / 25.4}
    ok_margin = bool(mg) and float(mg.group(1)) * inch[mg.group(2)] >= 0.999
    add("PASS" if ok_margin else "FAIL", "page margin >= 1 inch", geo.group(1) if geo else "no geometry setting")
    for pat, label in ((r"\\title\{", "\\title"), (r"\\author\{", "\\author"),
                       (r"\\begin\{abstract\}", "abstract environment"), (r"\\maketitle", "\\maketitle")):
        add("PASS" if re.search(pat, src_nc) else "FAIL", f"has {label}")
    if "bibliography{" in src_nc or "\\addbibresource" in src_nc:
        add("PASS" if any(n.endswith(".bbl") for n in names) else "FAIL", ".bbl present for bibliography")
    else:
        add("PASS", "bibliography", "references typeset in the text; no BibTeX or Biber, so no .bbl needed")
    fl = re.findall(r"\\(?:setmainfont|setsansfont|setmonofont|newfontfamily\\\w+)\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}", src_nc)
    nonfile = [f for f in fl if not re.search(r"\.(ttf|otf)$", f.strip())]
    add("FAIL" if nonfile else "PASS", "fontspec by file name (arXiv has no fontconfig)",
        f"name lookups: {nonfile}" if nonfile else f"{fl or 'no custom fonts'}")

    readme = json.loads(data["00README.json"]) if "00README.json" in data else None
    if readme:
        try:
            comp = readme["process"]["compiler"]
            tl = [s["filename"] for s in readme["sources"] if s.get("usage", "toplevel") == "toplevel"]
            ok = (comp in COMPILERS and readme.get("spec_version") == 1 and readme.get("texlive_version") in (2023, 2025)
                  and tl == tops)
            add("PASS" if ok else "FAIL", "00README.json", f"compiler={comp} texlive={readme.get('texlive_version')} toplevel={tl}")
        except (KeyError, TypeError) as e:
            add("FAIL", "00README.json", f"invalid: {e!r}")
    else:
        add("WARN", "00README.json", "absent: pick xelatex and TeX Live 2025 in the upload UI")
    if re.search(r"\\setmainfont|fontspec|unicode-math", src_nc):
        ok = bool(readme) and readme.get("process", {}).get("compiler") == "xelatex"
        add("PASS" if ok else "FAIL", "fontspec or unicode-math requires xelatex to be declared")

    lg = log.read_text(errors="replace")
    errs = re.findall(r"^! .*$", lg, re.M)
    add("FAIL" if errs else "PASS", "log: no TeX errors", "; ".join(errs[:3]))
    miss = sorted(set(re.findall(r"Missing character: There is no (.*?) in font (.*?)!", lg)))
    add("FAIL" if miss else "PASS", "log: no missing glyphs", "; ".join(f"{a} in {b}" for a, b in miss[:6]))
    undef = re.findall(r"(?:Reference|Citation) `([^']*)' .*undefined", lg)
    add("FAIL" if undef else "PASS", "log: no undefined references", ", ".join(undef[:5]))
    tail = lg.split("Output written")[-1]
    add("FAIL" if ("Rerun to get" in tail or "Label(s) may have changed" in tail) else "PASS", "log: labels stable after the last run")
    fw = re.findall(r"^(?:Package|Class) (\w+) Warning: (.*)$", lg, re.M)
    fw = [f"{p}: {t}" for p, t in fw if p in {"fontspec", "unicode-math", "hyperref", "microtype", "xetex"}]
    add("WARN" if fw else "PASS", "log: package warnings", f"{len(fw)}; first: {fw[0]}" if fw else "none")
    ov = [float(x) for x in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)", lg)]
    big = [x for x in ov if x > 10]
    add("WARN" if big else "PASS", "log: overfull boxes > 10pt", f"{len(big)} of {len(ov)}" + (f", max {max(big)}pt" if big else ""))

    a = abstract.read_text().rstrip("\n")
    add("PASS" if len(a) <= ABSTRACT_LIMIT else "FAIL", "abstract <= 1920 chars (as pasted, newlines counted)",
        f"{len(a)} chars, headroom {ABSTRACT_LIMIT - len(a)}")
    nonascii = [c for c in a if ord(c) > 127]
    add("FAIL" if nonascii else "PASS", "abstract ASCII", str(nonascii[:5]))
    add("FAIL" if re.match(r"\s*abstract\b", a, re.I) else "PASS", "abstract has no 'Abstract' heading")
    add("FAIL" if re.search(r"[\\$^~`*]", a) else "PASS", "abstract has no TeX or Markdown markup")
    add("FAIL" if re.search(r"\n\s*\n", a) else "PASS", "abstract has no blank lines")

    if proof and proof.exists() and shutil.which("pdffonts"):
        check_pdf(proof)

    w = max(len(r[1]) for r in rows)
    for s, r, d in rows:
        print(f"{s:5} {r.ljust(w)}  {d}".rstrip())
    f = sum(1 for r in rows if r[0] == "FAIL")
    wn = sum(1 for r in rows if r[0] == "WARN")
    print(f"{len(rows)} checks, {f} FAIL, {wn} WARN")
    sys.exit(1 if f else 0)


if __name__ == "__main__":
    main()

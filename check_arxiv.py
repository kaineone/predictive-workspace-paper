#!/usr/bin/env python3
"""Check a paper repository against common arXiv submission requirements.

Reads paper.md and header-preprint.tex from the repository root and reports
compliance with rules drawn from https://info.arxiv.org/help/prep.html and
https://info.arxiv.org/help/submit_tex.html. The script also enforces house
word budgets for the main text and Appendix A.
"""

import argparse
import re
import struct
import sys
import urllib.request
from pathlib import Path

ABSTRACT_LIMIT = 1920
ACCEPTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".pdf"}
# arXiv file-name alphabet (https://info.arxiv.org/help/submit/index.html), case sensitive.
ARXIV_FILENAME = re.compile(r"^[A-Za-z0-9_+\-.,=/]+$")
# arXiv warns above 34 megapixels (https://info.arxiv.org/help/sizes.html).
MEGAPIXEL_LIMIT = 34_000_000
# PNG features that stop pdfTeX/XeTeX embedding the file without re-encoding.
PNG_SLOW_CHUNKS = {"gAMA", "sRGB", "cHRM", "iCCP", "sBIT", "bKGD", "hIST", "tRNS", "sPLT"}
# Body characters must lie in Latin-1/Latin Extended (U+0000-U+024F) so that both pdflatex
# (T1/utf8) and xelatex with Noto Serif set them; plus section sign and degree already in range.
BODY_CHAR_LIMIT = 0x0250

# House limits, not arXiv rules; raising one should be a deliberate edit.
MAIN_TEXT_WORD_BUDGET = 12600
APPENDIX_WORD_BUDGET = 10950


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check arXiv submission compliance."
    )
    parser.add_argument(
        "--root",
        default=None,
        help="Repository root directory (default: directory containing this script).",
    )
    parser.add_argument(
        "--check-links",
        action="store_true",
        help="Also fetch the repository links (needs network).",
    )
    return parser.parse_args()


def load_paper(root):
    """Return (text, error_message) for paper.md."""
    path = root / "paper.md"
    if not path.is_file():
        return None, "paper.md not found"
    try:
        return path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError:
        return None, "paper.md not valid UTF-8"


def strip_markdown(text):
    """Remove simple Markdown formatting and return the plain text."""
    text = re.sub(r"\[(.*?)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"__(.+?)__", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"(?<![A-Za-z0-9])_(.+?)_(?![A-Za-z0-9])", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return text


def counted_abstract(raw_abstract):
    """Return the abstract as it is pasted into arXiv's form, and so as it is counted.

    Paragraphs stay on their own lines, and each continuation line starts with one space,
    because arXiv strips a carriage return unless whitespace follows it
    (https://info.arxiv.org/help/prep.html). That costs two characters per paragraph break
    where the old single-space join cost one.
    """
    plain = strip_markdown(raw_abstract)
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", plain) if p.strip()]
    return "\n ".join(paras)


def non_ascii_detail(text):
    """Return a description of the first non-ASCII characters, or None."""
    bad = [c for c in text if ord(c) >= 128]
    if not bad:
        return None
    return ", ".join(f"U+{ord(c):04X} '{c}'" for c in bad)


def extract_title(paper_text):
    for line in paper_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def extract_author_line(paper_text):
    title_seen = False
    for line in paper_text.splitlines():
        if title_seen:
            if line.strip():
                return line.strip()
        elif line.startswith("# "):
            title_seen = True
    return None


def extract_raw_abstract(paper_text):
    lines = paper_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Abstract":
            start = i
            break
    if start is None:
        return None, "## Abstract marker missing"

    end = None
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("**Keywords"):
            end = j
            break
    if end is None:
        return None, "**Keywords marker missing"

    raw = "\n".join(lines[start + 1 : end])
    if not raw.strip():
        return None, "abstract is empty"
    return raw, None


def extract_main_text(paper_text):
    lines = paper_text.splitlines()
    end = None
    for i, line in enumerate(lines):
        if line.strip() == "## Disclosure of generative AI use":
            end = i
            break
    if end is None:
        return None, "## Disclosure of generative AI use marker missing"
    return "\n".join(lines[:end]), None


def extract_appendix(paper_text):
    lines = paper_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("## Appendix A"):
            start = i
            break
    if start is None:
        return None, "## Appendix A marker missing"
    return "\n".join(lines[start:]), None


def figure_paths(paper_text):
    """Return a list of figure paths referenced in the paper."""
    refs = []
    for m in re.finditer(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)", paper_text):
        refs.append(m.group(1))
    for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", paper_text):
        refs.append(m.group(1))
    return refs


def rule_abstract_length(count, headroom):
    ok = count <= ABSTRACT_LIMIT
    detail = f"{count} / {ABSTRACT_LIMIT} chars, headroom {headroom}"
    return ok, detail


def rule_title_ascii(title):
    if title is None:
        return False, "title not found"
    bad = non_ascii_detail(title)
    if bad:
        return False, bad
    return True, "all ASCII"


def rule_title_not_all_caps(title):
    if title is None:
        return False, "title not found"
    letters = [c for c in title if c.isalpha()]
    if letters and all(c.isupper() for c in letters):
        return False, "title is all uppercase"
    return True, "not all caps"


def rule_author_ascii(author_line):
    if author_line is None:
        return False, "author line not found"
    author = strip_markdown(author_line).strip()
    bad = non_ascii_detail(author)
    if bad:
        return False, bad
    return True, author


def rule_abstract_ascii(raw_abstract):
    if raw_abstract is None:
        return False, "abstract not found"
    bad = non_ascii_detail(raw_abstract)
    if bad:
        return False, bad
    return True, "all ASCII"


def rule_abstract_no_markup(raw_abstract):
    if raw_abstract is None:
        return False, "abstract not found"

    found = []
    if "*" in raw_abstract:
        found.append("asterisk")
    if "`" in raw_abstract:
        found.append("backtick")
    if re.search(r"\[.*?\]\([^)]*\)", raw_abstract):
        found.append("markdown link")
    if "$" in raw_abstract:
        found.append("dollar sign")
    if "\\" in raw_abstract:
        found.append("backslash")
    if "^" in raw_abstract:
        found.append("caret")
    if "~" in raw_abstract:
        found.append("tilde")
    if (
        re.search(r"(?<![A-Za-z0-9])_", raw_abstract)
        or re.search(r"_(?![A-Za-z0-9])", raw_abstract)
    ):
        found.append("underscore emphasis")

    if found:
        return False, ", ".join(found) + " found"
    return True, "no Markdown or math markup found"


def rule_no_referee_lineno(root, paper_text):
    header_path = root / "header-preprint.tex"
    if not header_path.is_file():
        return False, "header-preprint.tex not found"

    try:
        header_text = header_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, "header-preprint.tex not valid UTF-8"

    header_text = re.sub(r"(?<!\\)%.*", "", header_text)

    patterns = [
        r"\\usepackage\s*(\[[^\]]*\])?\s*\{[^}]*\blineno\b[^}]*\}",
        r"\\linenumbers\b",
        r"\\doublespacing\b",
        r"\\usepackage\s*\[[^\]]*\bdoublespacing\b[^\]]*\]\s*\{setspace\}",
        r"\\documentclass\s*\[[^\]]*\breferee\b[^\]]*\]",
        r"\\linespread\s*\{\s*(1\.[6-9]|[2-9])",
        r"\\setstretch\s*\{\s*(1\.[6-9]|[2-9])",
    ]
    yaml_patterns = [
        (r"^\s*classoption\s*:.*\breferee\b", "paper.md"),
        (r"^\s*linestretch\s*:\s*(1\.[6-9]|[2-9])", "paper.md"),
    ]

    hits = []
    for pat in patterns:
        rgx = re.compile(pat)
        for m in rgx.finditer(header_text):
            hits.append(f"header-preprint.tex: {m.group(0)}")
        for m in rgx.finditer(paper_text):
            hits.append(f"paper.md: {m.group(0)}")

    for pat, filename in yaml_patterns:
        rgx = re.compile(pat, re.MULTILINE)
        for m in rgx.finditer(paper_text):
            hits.append(f"{filename}: {m.group(0)}")

    if hits:
        return False, "; ".join(hits)
    return True, "no referee format, line numbers or double spacing found"


def rule_figures(root, paper_text):
    refs = figure_paths(paper_text)
    if not refs:
        return True, "no figures referenced"

    bad = []
    root_resolved = root.resolve()
    seen = set()

    for path_str in refs:
        if path_str in seen:
            continue
        seen.add(path_str)

        lowered = path_str.lower()
        if lowered.startswith("http://") or lowered.startswith("https://"):
            bad.append(f"{path_str}: remote")
            continue

        try:
            p = Path(path_str)
        except Exception:
            bad.append(f"{path_str}: outside repository")
            continue

        if p.is_absolute() or path_str.startswith("/"):
            bad.append(f"{path_str}: outside repository")
            continue

        try:
            full = (root / path_str).resolve()
        except Exception:
            bad.append(f"{path_str}: outside repository")
            continue

        try:
            if not full.is_relative_to(root_resolved):
                bad.append(f"{path_str}: outside repository")
                continue
        except Exception:
            bad.append(f"{path_str}: outside repository")
            continue

        ext = Path(path_str).suffix.lower()
        if ext not in ACCEPTED_IMAGE_EXTENSIONS:
            if not ext:
                ext = "(none)"
            bad.append(f"{path_str}: unsupported type {ext}")
            continue

        if not full.is_file():
            bad.append(f"{path_str}: missing")
            continue

    if bad:
        return False, "; ".join(bad)
    return True, f"{len(refs)} figures, all present (PNG/JPG/PDF)"


def rule_main_text_length(count, headroom):
    ok = count <= MAIN_TEXT_WORD_BUDGET
    detail = f"{count} / {MAIN_TEXT_WORD_BUDGET} words, headroom {headroom}"
    return ok, detail


def rule_appendix_length(count, headroom):
    ok = count <= APPENDIX_WORD_BUDGET
    detail = f"{count} / {APPENDIX_WORD_BUDGET} words, headroom {headroom}"
    return ok, detail


def rule_author_format(author_line):
    """arXiv: 'Firstname Lastname', no honorifics, degrees, commas or the word 'and' inside a name."""
    if author_line is None:
        return False, "author line not found"
    name = strip_markdown(author_line).strip()
    bad = []
    if re.search(r"\b(Dr|Prof|Professor|Mr|Mrs|Ms|PhD|MD|MSc|BSc)\b\.?", name):
        bad.append("honorific or degree")
    if "," in name or re.search(r"\band\b", name):
        bad.append("comma or 'and' inside a single name")
    if not re.fullmatch(r"[A-Z][A-Za-z.'-]+( [A-Za-z][A-Za-z.'-]*)+", name):
        bad.append("not 'Firstname Lastname'")
    if name.isupper():
        bad.append("all caps")
    if bad:
        return False, f"{name!r}: " + ", ".join(bad)
    return True, name


def rule_body_characters(paper_text):
    """Every non-ASCII body character must be one both TeX engines can set."""
    odd = sorted({c for c in paper_text if ord(c) >= BODY_CHAR_LIMIT})
    ctrl = sorted({c for c in paper_text if c in "\u00a0\u00ad\u200b\u200c\u200d\ufeff\u2028\u2029"})
    if odd or ctrl:
        parts = [f"U+{ord(c):04X}" for c in odd + ctrl]
        return False, "characters needing a font check or removal: " + ", ".join(parts)
    kinds = sorted({c for c in paper_text if ord(c) >= 128})
    return True, f"{len(kinds)} distinct non-ASCII characters, all in U+0080-U+024F, no NBSP/soft hyphen/zero-width"


def rule_ai_disclosure(paper_text, author_line):
    """arXiv requires reporting significant generative AI use, and no AI tool as an author."""
    m = re.search(r"^## Disclosure of generative AI use\s*\n(.*?)(?=^## |\Z)", paper_text, re.S | re.M)
    if not m or len(m.group(1).split()) < 20:
        return False, "no substantive '## Disclosure of generative AI use' section"
    if author_line and re.search(r"\b(Claude|GPT|ChatGPT|Gemini|LLM|AI)\b", author_line):
        return False, "an AI tool appears in the author line"
    return True, f"disclosure section present ({len(m.group(1).split())} words); no AI tool listed as author"


def rule_content_type(paper_text, raw_abstract):
    """CS moderation (2025-10-31) refuses position papers and review articles without peer review;
    arXiv content-type policy lists 'proposals for future research' as typically not accepted."""
    head = (raw_abstract or "") + "\n" + paper_text[:6000]
    hits = sorted(set(re.findall(r"\b(position paper|review article|survey article|literature review|perspective article|research proposal)\b", head, re.I)))
    if hits:
        return False, "self-described as: " + ", ".join(hits)
    return True, "abstract and introduction do not self-describe as a position paper, review or proposal"


def rule_tex_hazards(paper_text):
    """Raw TeX in paper.md that arXiv rejects or that breaks under TeX Live 2025."""
    pats = {
        r"\\today": "\\today",
        r"\\pdfoutput": "\\pdfoutput",
        r"\\write18|\\immediate\\write|shell-escape": "shell escape",
        r"\\usepackage": "\\usepackage in the body",
        r"\\usepackage(\[[^\]]*\])?\{(cleveref|minted|psfig|eso-pic|lineno)\}": "package unsuitable for arXiv",
        r"\\AddToShipout": "page overlay (margin note or watermark)",
        r"<script|\\href\{javascript:": "embedded script",
    }
    hits = [why for pat, why in pats.items() if re.search(pat, paper_text)]
    if hits:
        return False, "; ".join(hits)
    return True, "none found"


def png_problems(path):
    """Return (width, height, [problems]) for a PNG, or None if it is not a PNG."""
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    w, h, _bd, ct, _cm, _fm, il = struct.unpack(">IIBBBBB", data[16:29])
    chunks, i = [], 8
    while i < len(data):
        (n,) = struct.unpack(">I", data[i : i + 4])
        chunks.append(data[i + 4 : i + 8].decode("latin1"))
        i += 12 + n
    problems = []
    if ct in (3, 4, 6):
        problems.append("palette or alpha")
    if il:
        problems.append("interlaced")
    problems += sorted(PNG_SLOW_CHUNKS.intersection(chunks))
    if w * h > MEGAPIXEL_LIMIT:
        problems.append(f"{w * h / 1e6:.0f} megapixels")
    return w, h, problems


def rule_figure_files(root, paper_text):
    """File-name alphabet, exact case, and PNG features, for every local figure."""
    refs = sorted({r for r in figure_paths(paper_text) if not r.lower().startswith("http")})
    bad = []
    for ref in refs:
        if not ARXIV_FILENAME.match(ref):
            bad.append(f"{ref}: characters outside a-zA-Z0-9_+-.,=")
            continue
        p = root / ref
        if p.is_file() and p.name not in {q.name for q in p.parent.iterdir()}:
            bad.append(f"{ref}: case differs on disk")
        if p.suffix.lower() == ".png" and p.is_file():
            info = png_problems(p)
            if info is None:
                bad.append(f"{ref}: not a PNG")
            elif info[2]:
                bad.append(f"{ref}: " + ", ".join(info[2]))
    if bad:
        return False, "; ".join(bad)
    return True, f"{len(refs)} figure files: arXiv file-name alphabet, exact case, PNGs embed without re-encoding"


def rule_margin_note_excluded(root):
    """arXiv's format policy forbids margin notes and puts text within 1 inch of the edge off limits;
    header-preprint.tex draws a margin note, so the arXiv build must not use it."""
    header = root / "header-preprint.tex"
    if not header.is_file():
        return True, "no header-preprint.tex"
    text = re.sub(r"(?<!\\)%.*", "", header.read_text(encoding="utf-8"))
    if not re.search(r"AddToShipoutPicture|eso-pic", text):
        return True, "header-preprint.tex has no page overlay"
    build = root / "arxiv" / "build-arxiv.sh"
    if not build.is_file():
        return False, "header-preprint.tex draws a margin note and there is no arxiv/build-arxiv.sh that leaves it out"
    if "header-preprint" in build.read_text(encoding="utf-8"):
        return False, "arxiv/build-arxiv.sh uses header-preprint.tex (margin note)"
    return True, "margin note is confined to the pandoc PDF; the arXiv build excludes it"


def rule_links_public(paper_text, enabled):
    """arXiv: links to code or data must resolve to a publicly available repository."""
    urls = sorted(set(re.findall(r"https://github\.com/kaineone/[A-Za-z0-9_-]+", paper_text)))
    if not enabled:
        return True, f"{len(urls)} repository links (not fetched; pass --check-links)"
    dead = []
    for u in urls:
        try:
            req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "check_arxiv"})
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status != 200:
                    dead.append(f"{u}: {r.status}")
        except Exception as exc:  # noqa: BLE001
            dead.append(f"{u}: {exc}")
    if dead:
        return False, "; ".join(dead)
    return True, f"{len(urls)} repository links resolve publicly"


def add_rule(rows, name, func, *args):
    """Call a rule function and append a (status, name, detail) row."""
    try:
        ok, detail = func(*args)
    except Exception as exc:
        ok, detail = False, f"check error: {exc}"
    status = "PASS" if ok else "FAIL"
    rows.append((status, name, detail))


def print_table(rows):
    w_status = max(len("STATUS"), max(len(r[0]) for r in rows))
    w_name = max(len("RULE"), max(len(r[1]) for r in rows))
    w_detail = max(len("DETAIL"), max(len(r[2]) for r in rows))

    line = (
        f"{'STATUS'.ljust(w_status)}  "
        f"{'RULE'.ljust(w_name)}  "
        f"{'DETAIL'.ljust(w_detail)}"
    )
    print(line.rstrip())
    line = f"{'-' * w_status}--{'-' * w_name}--{'-' * w_detail}"
    print(line.rstrip())
    for status, name, detail in rows:
        line = (
            f"{status.ljust(w_status)}  "
            f"{name.ljust(w_name)}  "
            f"{detail.ljust(w_detail)}"
        )
        print(line.rstrip())


def main():
    args = parse_args()
    if args.root:
        root = Path(args.root).resolve()
    else:
        root = Path(__file__).resolve().parent

    print(f"arXiv compliance check: {root}")

    paper_text, paper_err = load_paper(root)
    if paper_err:
        rows = [("FAIL", "paper.md", paper_err)]
        print_table(rows)
        print("1 of 1 checks FAILED.")
        return 1

    title = extract_title(paper_text)
    author_line = extract_author_line(paper_text)
    raw_abstract, abstract_err = extract_raw_abstract(paper_text)
    main_text, main_text_err = extract_main_text(paper_text)
    appendix, appendix_err = extract_appendix(paper_text)

    rows = []

    if raw_abstract is not None:
        count = len(counted_abstract(raw_abstract))
        headroom = ABSTRACT_LIMIT - count
        add_rule(
            rows,
            "abstract length",
            rule_abstract_length,
            count,
            headroom,
        )
        print(
            f"Abstract: {count} characters "
            f"(limit {ABSTRACT_LIMIT}, headroom {headroom})"
        )
    else:
        rows.append(("FAIL", "abstract length", abstract_err))

    if main_text is not None:
        m_count = len(main_text.split())
        m_headroom = MAIN_TEXT_WORD_BUDGET - m_count
    else:
        m_count = None
        m_headroom = None

    if appendix is not None:
        a_count = len(appendix.split())
        a_headroom = APPENDIX_WORD_BUDGET - a_count
    else:
        a_count = None
        a_headroom = None

    main_summary = (
        f"main text {m_count} words "
        f"(budget {MAIN_TEXT_WORD_BUDGET}, headroom {m_headroom})"
        if m_count is not None
        else "main text missing"
    )
    appendix_summary = (
        f"Appendix A {a_count} words "
        f"(budget {APPENDIX_WORD_BUDGET}, headroom {a_headroom})"
        if a_count is not None
        else "Appendix A missing"
    )
    print(f"Length: {main_summary}; {appendix_summary}")

    add_rule(rows, "title ASCII", rule_title_ascii, title)
    add_rule(rows, "title not all caps", rule_title_not_all_caps, title)
    add_rule(rows, "author ASCII", rule_author_ascii, author_line)
    add_rule(rows, "abstract ASCII", rule_abstract_ascii, raw_abstract)
    add_rule(rows, "abstract no Markdown or math", rule_abstract_no_markup, raw_abstract)
    add_rule(
        rows,
        "no referee format, line numbers or double spacing",
        rule_no_referee_lineno,
        root,
        paper_text,
    )
    add_rule(rows, "figures", rule_figures, root, paper_text)
    add_rule(rows, "figure files (names, case, PNG features)", rule_figure_files, root, paper_text)
    add_rule(rows, "author name format", rule_author_format, author_line)
    add_rule(rows, "body characters", rule_body_characters, paper_text)
    add_rule(rows, "generative AI disclosure", rule_ai_disclosure, paper_text, author_line)
    add_rule(rows, "content type (CS moderation)", rule_content_type, paper_text, raw_abstract)
    add_rule(rows, "no arXiv-hostile raw TeX", rule_tex_hazards, paper_text)
    add_rule(rows, "margin note excluded from arXiv build", rule_margin_note_excluded, root)
    add_rule(rows, "repository links public", rule_links_public, paper_text, args.check_links)

    if main_text is not None:
        add_rule(
            rows,
            "main-text length",
            rule_main_text_length,
            m_count,
            m_headroom,
        )
    else:
        rows.append(("FAIL", "main-text length", main_text_err))

    if appendix is not None:
        add_rule(
            rows,
            "appendix length",
            rule_appendix_length,
            a_count,
            a_headroom,
        )
    else:
        rows.append(("FAIL", "appendix length", appendix_err))

    print_table(rows)

    failed = sum(1 for status, _, _ in rows if status == "FAIL")
    total = len(rows)
    if failed == 0:
        print(f"All {total} checks passed.")
    else:
        print(f"{failed} of {total} checks FAILED.")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

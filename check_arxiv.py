#!/usr/bin/env python3
"""Check a paper repository against common arXiv submission requirements.

Reads paper.md and header-preprint.tex from the repository root and reports
compliance with rules drawn from https://info.arxiv.org/help/prep.html and
https://info.arxiv.org/help/submit_tex.html.
"""

import argparse
import re
import sys
from pathlib import Path

ABSTRACT_LIMIT = 1920
ACCEPTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".pdf"}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check arXiv submission compliance."
    )
    parser.add_argument(
        "--root",
        default=None,
        help="Repository root directory (default: directory containing this script).",
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
    """Return the abstract the way arXiv's form would count it."""
    plain = strip_markdown(raw_abstract)
    collapsed = re.sub(r"\s+", " ", plain).strip()
    return collapsed


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

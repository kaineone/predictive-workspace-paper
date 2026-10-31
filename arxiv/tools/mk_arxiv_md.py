#!/usr/bin/env python3
"""Turn paper.md into paper-arxiv.md: the front matter becomes pandoc YAML
metadata (title, author, abstract) so the .tex has \\title/\\author/\\maketitle
and an abstract environment; the body is unchanged.

Fails closed: if the front matter no longer has the expected shape, exit 1.
Usage: mk_arxiv_md.py <paper.md> <out.md> <abstract.txt>
"""
import json
import re
import sys
from pathlib import Path


def die(msg):
    print(f"mk_arxiv_md: {msg}", file=sys.stderr)
    sys.exit(1)


def strip_md(text):
    text = re.sub(r"\[(.*?)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return text


def main():
    src, out, abs_out = (Path(a) for a in sys.argv[1:4])
    lines = src.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# "):
        die("line 1 is not the '# Title' heading")
    title = lines[0][2:].strip()

    # Front matter is lines[1:abstract_marker]: author, affiliation, contact, preprint, rule.
    try:
        a_idx = lines.index("## Abstract")
    except ValueError:
        die("'## Abstract' marker missing")
    front = [l.strip() for l in lines[1:a_idx] if l.strip() and not re.fullmatch(r"-{3,}", l.strip())]
    if len(front) != 4:
        die(f"front matter should be author/affiliation/contact/preprint (4 lines), got {front!r}")
    m = re.fullmatch(r"\*\*(.+)\*\*", front[0])
    if not m:
        die("author line is not bold")
    author = m.group(1)
    affiliation = front[1]
    m = re.fullmatch(r"Contact: \[(.+?)\]\(mailto:(.+?)\)", front[2])
    if not m or m.group(1) != m.group(2):
        die("contact line is not 'Contact: [addr](mailto:addr)'")
    email = m.group(1)
    m = re.fullmatch(r"\*(Preprint\.?)\*", front[3])
    if not m:
        die("preprint line is not '*Preprint.*'")

    # Abstract is a_idx+1 .. the line before '**Keywords'.
    try:
        k_idx = next(i for i in range(a_idx + 1, len(lines)) if lines[i].startswith("**Keywords"))
    except StopIteration:
        die("'**Keywords' marker missing")
    abstract_md = "\n".join(lines[a_idx + 1 : k_idx]).strip()
    mk = re.fullmatch(r"\*\*Keywords:\*\*\s*(.+)", lines[k_idx].strip())
    if not mk:
        die("keywords line is not '**Keywords:** a; b; c'")
    keywords = [k.strip() for k in mk.group(1).split(";") if k.strip()]
    if not abstract_md:
        die("abstract empty")

    yaml_lines = [
        "---",
        f"title: {json.dumps(title)}",
        # one author string with line breaks so \author{} carries affiliation and contact
        "author: |",
        f"  {author}\\",
        f"  {affiliation}\\",
        f"  {email}",
        f"author-meta: {json.dumps(author)}",
        'date: "Preprint. Not peer-reviewed."',
        f"keywords: {json.dumps(keywords)}",
        "abstract: |",
    ]
    yaml_lines += [("  " + l) if l.strip() else "" for l in abstract_md.splitlines()]
    yaml_lines += ["---", ""]
    body = "\n".join(lines[k_idx:]) + "\n"
    out.write_text("\n".join(yaml_lines) + "\n" + body, encoding="utf-8")

    # arXiv abstract field text: plain ASCII, paragraphs separated by a newline
    # followed by a one-space indent (arXiv strips bare carriage returns).
    paras = [re.sub(r"\s+", " ", strip_md(p)).strip() for p in re.split(r"\n\s*\n", abstract_md)]
    abs_out.write_text("\n ".join(paras) + "\n", encoding="utf-8")
    print(f"title={title!r} author={author!r} abstract_paragraphs={len(paras)}")


if __name__ == "__main__":
    main()

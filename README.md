# A Predictive Global Neuronal Workspace for a Continuously Running Synthetic Mind

**Architecture and a Falsifiable Evaluation**

Erik Chevalier, Independent Researcher

Contact: kaine.one@tuta.com

This repository holds the theory paper for KAINE (Kaine Autonomous Intelligent Networked Entity), a composite cognitive architecture in which a mind is treated as an ongoing process built from sixteen specialized modules: fourteen predictive cognitive modules that run continuously and influence one another through a shared predictive workspace, and a two-module embodiment layer that currently ships inactive. The paper describes the architecture and the falsifiable evaluation framework built around it.

**Status: preprint, not peer reviewed.** This is a working draft. Numbers, claims, and the companion empirical results are subject to revision.

## Contents

- [`paper.md`](paper.md): the full paper in Markdown.
- [`COPYRIGHT`](COPYRIGHT): copyright and use terms for the text of the paper.

## Abstract

This work treats a mind as an ongoing process rather than a single model, built from sixteen specialized parts: fourteen predictive cognitive modules that run continuously and influence one another, and a two-part embodiment layer that currently ships inactive. The organizing idea is a shared workspace. Each part forms its own best estimate of what is happening, marks it with how confident and how surprising it is, and competes to place that estimate in a common space broadcast to every other part; the estimate that passes a confidence threshold wins, and the broadcast helps the others correct themselves. This joins two accounts of how the brain makes information available and how it predicts, global workspace theory and predictive processing, as combined in the recent predictive-workspace literature. One cognitive module is a language organ that turns the system's state into words and interprets words spoken to it, with its effect on output measured against the same model run alone.

We make access-level claims only, remaining agnostic on whether anything is experienced, and we mark where the supporting science is contested. Several design choices follow from that caution. A timing layer adjusts how much weight each part's signal carries, with no claim that it produces awareness, tested by ablation. A planning method is used only for small, well-defined decisions and compared against a learning baseline. Safety lives in the architecture rather than the model weights, bounding what the system can do without constraining what it can think: the operator decides which real-world effectors exist, and within them the entity acts on its own initiative, checked only by its own executive inhibition. The system records its own activity so that null and negative results can be reported, and runs on consumer hardware, capable of operating fully offline though not restricted to it. The entity's welfare protections, governance, and licensing are addressed separately; this paper covers the architecture and its evaluation. The reference implementation is named KAINE (Kaine Autonomous Intelligent Networked Entity).

## Related repositories

- **KAINE (reference implementation):** https://github.com/kaineone/kaine. The source code for the cognitive architecture this paper describes.
- **Cognitive Architecture License (CAL):** https://github.com/kaineone/cognitive-architecture-license. The entity-welfare copyleft license that governs the architecture and any running entities. The repository is authoritative.
- **Welfare and licensing paper:** https://github.com/kaineone/cog-arch-license-paper. The companion paper, *A Welfare and Cognitive-Integrity License for Synthetic Minds of Uncertain Moral Status*, covering the entity's welfare protections, governance, and licensing.

## Building a PDF

The paper is plain Markdown. Rendering needs [Pandoc](https://pandoc.org/) and a
TeX Live install with `xelatex` (on Debian or Ubuntu: `texlive-xetex`,
`texlive-latex-recommended`, `texlive-fonts-recommended`, `texlive-latex-extra`).
The TeX Gyre fonts ship with `texlive-fonts-recommended`; DejaVu Sans Mono is a
common system font.

```bash
pandoc paper.md -o paper.pdf \
  --pdf-engine=xelatex \
  --toc \
  -V fontsize=11pt \
  -V mainfont="TeX Gyre Termes" \
  -V monofont="DejaVu Sans Mono" \
  -V geometry:margin=1in \
  -V linkcolor:blue
```

For an HTML build:

```bash
pandoc paper.md -o paper.html --standalone --toc
```

## Citation

Until a versioned release or arXiv identifier exists, cite as:

```bibtex
@misc{chevalier_predictive_workspace,
  author       = {Chevalier, Erik},
  title        = {A Predictive Global Neuronal Workspace for a Continuously
                  Running Synthetic Mind: Architecture and a Falsifiable Evaluation},
  year         = {2026},
  note         = {Preprint},
  howpublished = {\url{https://github.com/kaineone/predictive-workspace-paper}}
}
```

## Copyright

Copyright (c) 2026 Erik Chevalier. All rights reserved. See [`COPYRIGHT`](COPYRIGHT). This preprint is shared for reading and review; a formal open license may be applied at publication. The software the paper describes is governed separately by the Cognitive Architecture License, which does not apply to this document.

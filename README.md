# KAINE: A Continuously Running Predictive Global Workspace for Synthetic Minds

Part of the Kaine project — **[kaine.one](https://kaine.one)**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21203505.svg)](https://doi.org/10.5281/zenodo.21203505)

**A falsifiability-first architecture paper, centered on a single losable test.**

Erik Chevalier, Independent Researcher

Contact: kaine.one@tuta.com

This repository holds the theory paper for KAINE (Kaine Autonomous Intelligent Networked Entity), a continuously running predictive global neuronal workspace in which a mind is treated as the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. The paper presents the architecture in its base-thesis form — four externally-grounded predictive processors, an affective precision core, and an output-only language organ — together with a falsifiability-first evaluation built around a single losable test. The experimental verdicts are reported in a separate empirical paper.

**Status: preprint, not peer reviewed.** This is a working draft. Numbers, claims, and the companion empirical results are subject to revision.

## About this version

This is the base-thesis form of the paper. It narrows the architecture to the minimal configuration that can test the claim on which everything else depends: that routing diverse predictive processors through a competitive workspace produces behavior that concatenating the same processors' outputs does not. Eight of the sixteen modules are active; the rest are built and held for future experiments that only matter if the base thesis survives. The centerpiece is the workspace-mediation ablation (Section 6.3), a pre-registered test the architecture can genuinely lose.

## Contents

- [`paper.md`](paper.md): the full paper in Markdown.
- [`paper.pdf`](paper.pdf): the rendered paper, including the figures and module table.
- [`figures/`](figures): the TikZ sources and rendered PNGs for the seven figures.
- [`LICENSE`](LICENSE): the Creative Commons Attribution 4.0 International license for the text.
- [`COPYRIGHT`](COPYRIGHT): copyright and licensing summary for the text of the paper.
- [`CITATION.cff`](CITATION.cff): machine-readable citation metadata.

## Abstract

A synthetic mind, if one can be built, may be the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. This paper presents a continuously running predictive global neuronal workspace built on that thesis. The workspace selects the most salient coalition above a confidence threshold and broadcasts it. The broadcast becomes shared state that shapes every module's prediction environment on the next tick, and the changed errors feed back into the next round. Coherence, where it arises, comes from competition over shared state.

The base-thesis form activates four predictive processors (foveated vision, raw hearing, interoceptive prediction, and temporal prediction) together with an affective core whose arousal sets the precision on their competition and is itself driven by perceptual surprise, and an output-only language organ that verbalizes the entity's conscious state. The entity is observed, not conversed with: sound, including speech, enters only as prediction error, and the language organ receives no transcript. Keeping text out is a precondition for the falsification test, since any route from input to the model would let it answer as a chatbot and confound the ablation.

The primary experiment is a workspace-mediation ablation with pre-registered directional criteria on cross-module error structure and coalition dynamics: does routing processors through the competitive workspace produce structured behavior that the same processors, concatenated into a flat prompt, do not? If the workspace adds nothing, the two conditions will be indistinguishable, falsifying the thesis and demoting the architecture to a scored prompt-assembler. The system runs locally on consumer hardware. The reference implementation is named KAINE (Kaine Autonomous Intelligent Networked Entity).

## Related repositories

- **KAINE (reference implementation):** https://github.com/kaineone/kaine. The source code for the cognitive architecture this paper describes.
- **Cognitive Architecture License (CAL):** https://github.com/kaineone/cognitive-architecture-license. The entity-welfare copyleft license that governs the architecture and any running entities. The repository is authoritative.
- **Welfare and licensing paper:** https://github.com/kaineone/cog-arch-license-paper. The companion paper, *A Welfare and Cognitive-Integrity License for Synthetic Minds of Uncertain Moral Status*, covering the entity's welfare protections, governance, and licensing.

## Building the PDF

A pre-built [`paper.pdf`](paper.pdf) is included and is the canonical rendered version. To rebuild it you need [Pandoc](https://pandoc.org/) and a TeX Live install with `xelatex` (on Debian or Ubuntu: `texlive-xetex`, `texlive-latex-recommended`, `texlive-fonts-recommended`, `texlive-latex-extra`). The figures live in `figures/` and are referenced by relative path, so build from the repository root. [`header-preprint.tex`](header-preprint.tex) draws the rotated "Preprint. Not peer-reviewed." note in the page margin.

```bash
pandoc paper.md -o paper.pdf \
  --pdf-engine=xelatex \
  -V fontsize=11pt \
  -V mainfont="Noto Serif" \
  -V geometry:margin=1in \
  -V colorlinks=true -V linkcolor=blue \
  --include-in-header=header-preprint.tex
```

## Citation

Archived on Zenodo. The **all-versions (concept) DOI**, which always resolves to
the latest version, is
[10.5281/zenodo.21203505](https://doi.org/10.5281/zenodo.21203505). Cite as:

```bibtex
@misc{chevalier_kaine_workspace,
  author       = {Chevalier, Erik},
  title        = {{KAINE}: A Continuously Running Predictive Global Workspace
                  for Synthetic Minds},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21203505},
  url          = {https://doi.org/10.5281/zenodo.21203505}
}
```

## License

The text of this preprint is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/); see [`LICENSE`](LICENSE). You are free to share and adapt it, including commercially, with attribution. The software the paper describes is governed separately by the Cognitive Architecture License, which does not apply to this document.

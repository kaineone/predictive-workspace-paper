# KAINE: A Continuously Running Predictive Global Workspace for Synthetic Minds

Part of the Kaine project — **[kaine.one](https://kaine.one)**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21203505.svg)](https://doi.org/10.5281/zenodo.21203505)

**A modular predictive-workspace architecture for synthetic minds, with the instruments that test it.**

Erik Chevalier, Independent Researcher

Contact: kaine.one@tuta.com

This repository holds the theory paper for KAINE (Kaine Autonomous Intelligent Networked Entity), a continuously running predictive global neuronal workspace in which a mind is treated as the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. The paper presents the architecture in its base-thesis form: four externally grounded predictive processors, an affective core that sets the gain on their competition, fatigue-triggered sleep, and an output-only language organ, together with the instruments built to test it: an offline workspace-mediation ablation, an eight-experiment offline suite, and a module-ignition study protocol that adds the held modules one at a time.

**Status: preprint, not peer reviewed.** This is a working draft. Numbers, claims, and the companion empirical results are subject to revision.

## About this version

This is the base-thesis form of the paper. It describes the architecture and its instruments as built: nine components are active (seven modules plus the workspace and the action layer), and the remaining seven cognitive modules and the embodiment layer are built and held, each joining the competition one at a time through the module-ignition study. The workspace-mediation ablation (Section 6.3) asks whether routing the processors through the competitive workspace produces behavior that concatenating their outputs does not.

## Contents

- [`paper.md`](paper.md): the full paper in Markdown.
- [`paper.pdf`](paper.pdf): the rendered paper, including the figures and module table.
- [`figures/`](figures): the TikZ sources and rendered PNGs for the seven figures.
- [`EMPIRICAL-NOTES.md`](EMPIRICAL-NOTES.md): implementation history that bears on interpreting data from runs, kept for the empirical paper.
- [`LICENSE`](LICENSE): the Creative Commons Attribution 4.0 International license for the text.
- [`COPYRIGHT`](COPYRIGHT): copyright and licensing summary for the text of the paper.
- [`CITATION.cff`](CITATION.cff): machine-readable citation metadata.

## Abstract

A synthetic mind, if one can be built, may be the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. This paper presents a continuously running predictive global workspace built on that thesis. The workspace selects the most salient coalition above a confidence threshold and broadcasts it; the broadcast becomes shared state that shapes every module's prediction environment on the next tick. Coherence, where it arises, comes from competition over shared state.

The base-thesis form activates four predictive processors (foveated vision, raw hearing, interoceptive prediction, and temporal prediction), an affective core whose arousal sets the gain on their competition and is itself driven by perceptual surprise, a fatigue-triggered sleep system that returns affect to baseline, and an output-only language organ that verbalizes the entity's state. The entity is observed but not conversed with: sound enters as auditory prediction error and a classified tone of voice, not as words, and the language organ receives no transcript. That exclusion is a precondition for the falsification test: any input route to the model would let it answer as a chatbot and confound the ablation.

The primary experiment is a built, offline, seeded workspace-mediation ablation that compares competitive selection with a flat fan-in of the same candidates. Its decision rule, with a fixed minimum effect and an explicit UNDERPOWERED outcome, is fixed in the released code. A module-ignition study protocol grows the architecture by adding the held modules one at a time. A null falsifies the thesis, demoting the architecture to a scored prompt-assembler. The system runs locally on consumer hardware, and the reference implementation is named KAINE (Kaine Autonomous Intelligent Networked Entity).

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

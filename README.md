# KAINE: A Modular Cognitive Architecture with a Predictive Global Workspace

Part of the Kaine project: **[kaine.one](https://kaine.one)**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21203505.svg)](https://doi.org/10.5281/zenodo.21203505)

**A modular predictive-workspace architecture for synthetic minds, with the instruments that test it.**

Erik Chevalier, Independent Researcher

Contact: kaine.one@tuta.com

This repository holds the paper for KAINE (Kaine Autonomous Intelligent Networked Entity), source-available software that implements existing theories of consciousness as a running program, so that they can be tested and compared. It proposes no new theory. Its first instantiation implements the predictive global neuronal workspace, which joins global workspace theory with predictive processing. The paper presents the architecture in its first configuration, four predictive processors (two externally grounded, two internal), an affective core that sets the gain on their competition, fatigue-triggered sleep, and an output-only language organ, together with its instruments and the research program they serve: an offline suite of experiments, a module-addition study that adds the held modules one at a time, and a planned test of whether competition does work that pooling does not.

**Status: preprint, not peer reviewed.** This is a working draft. Numbers, claims, and the companion empirical results are subject to revision.

## About this version

This version describes the architecture as designed and built, its instruments, and the planned experiments. In the first configuration nine components are active (seven modules plus the workspace and the action layer), and the remaining seven cognitive modules and the two embodiment modules are built and held, each joining the competition one at a time through the module-addition study. The planned test (Section 6.3) compares competitive selection with a score-blind coalition of the same size and with a pool of every candidate, by cross-module broadcast information gain. The live experiments have not yet been run; their results will be reported in a revised version of this preprint.

## Contents

- [`paper.md`](paper.md): the full paper in Markdown.
- [`paper.pdf`](paper.pdf): the rendered paper, including the figures and module table.
- [`figures/`](figures): the TikZ sources and rendered PNGs for the nine figures, with theme-matched light and dark web versions of all nine in `figures/web`.
- [`EMPIRICAL-NOTES.md`](EMPIRICAL-NOTES.md): implementation history that bears on interpreting data from runs, kept for the empirical paper.
- [`LICENSE`](LICENSE): the Creative Commons Attribution 4.0 International license for the text.
- [`COPYRIGHT`](COPYRIGHT): copyright and licensing summary for the text of the paper.
- [`CITATION.cff`](CITATION.cff): machine-readable citation metadata.

## Abstract

KAINE is source-available software, a cognitive architecture for synthetic minds. It proposes no new theory of consciousness: it implements existing theories as a running program so that they can be tested and compared. Each faculty is a replaceable module behind a fixed interface. Its first instantiation implements the predictive global workspace, which joins global workspace theory with predictive processing. Predictive processors, each minimizing its own error, are coupled only through a competitive workspace with no central executive. Each processor scales its prediction error by an estimate of its precision drawn from its own recent errors, and the reports compete for access. A summary of which modules' reports gained access, and how strongly, becomes the context for the processors' next predictions. Arousal, raised by perceptual surprise and interoceptive alarm, is the global gain on that competition and sizes the sensory apertures. The system runs continuously whether or not anyone interacts with it.

The first configuration activates four predictive processors (foveated vision, raw hearing, interoception of the compute substrate, and temporal prediction), an affective core, a fatigue-triggered sleep analog, and an output-only language organ. Nine further modules are built and held. A module-addition study seeds an entity through a developmental phase, in which a self-generated rhythm must entrain to a simulated maternal heartbeat by a marker validated offline, and then adds the held modules one at a time.

A planned test asks whether competition does work that pooling does not. It compares competitive selection with a score-blind coalition of the same size and with a pool of every candidate, by cross-module broadcast information gain. No live experiment has been run, and the only result reported is the offline validation of the entrainment marker.

## Related repositories

- **KAINE (reference implementation):** https://github.com/kaineone/kaine. The source code for the cognitive architecture this paper describes.
- **Cognitive Architecture License (CAL):** https://github.com/kaineone/cognitive-architecture-license. The entity-welfare copyleft license that governs the architecture and any running entities. The repository is authoritative.
- **Welfare and licensing paper:** https://github.com/kaineone/cog-arch-license-paper. The companion paper, *A Welfare and Cognitive-Integrity License for Synthetic Minds of Uncertain Moral Status*, covering the entity's welfare protections, governance, and licensing.

## arXiv requirements

This paper is kept within arXiv's submission requirements at all times, even though it is not being submitted now. This keeps a future submission from starting with cleanup.

`check_arxiv.py` enforces the rules. It checks that the abstract stays within arXiv's 1,920-character limit, that the title, authors, and abstract use plain ASCII, that the title avoids all capitals, that the abstract carries no Markdown emphasis, links, or math markup, that the source avoids double-spaced referee formatting and line numbers, and that every figure referenced in `paper.md` exists as a PNG, JPG, or PDF. The rules come from [arXiv's metadata help](https://info.arxiv.org/help/prep.html) and [arXiv's TeX submission help](https://info.arxiv.org/help/submit_tex.html).

The same script also holds the paper to two length budgets: the main text, from the title through the line before "Disclosure of generative AI use", stays within `MAIN_TEXT_WORD_BUDGET` words, and Appendix A stays within `APPENDIX_WORD_BUDGET` words, counting whitespace-separated words with LaTeX and captions included. These budgets are house rules, not arXiv rules, so raising one should be a deliberate edit to its constant at the top of `check_arxiv.py`, never a side effect of a content change.

The `arXiv check` GitHub Actions workflow runs `check_arxiv.py` on every push and pull request to `main`, and it fails when any rule fails. To run the same check locally:

```bash
python3 check_arxiv.py
```

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
  title        = {{KAINE}: A Modular Cognitive Architecture with a Predictive
                  Global Workspace},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21203505},
  url          = {https://doi.org/10.5281/zenodo.21203505}
}
```

## License

The text of this preprint is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/); see [`LICENSE`](LICENSE). You are free to share and adapt it, including commercially, with attribution. The software the paper describes is governed separately by the Cognitive Architecture License, which does not apply to this document.

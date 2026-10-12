# KAINE: A Modular Cognitive Architecture with a Predictive Global Workspace

Part of the Kaine project — **[kaine.one](https://kaine.one)**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21203505.svg)](https://doi.org/10.5281/zenodo.21203505)

**A modular predictive-workspace architecture for synthetic minds, with the instruments that test it.**

Erik Chevalier, Independent Researcher

Contact: kaine.one@tuta.com

This repository holds the theory paper for KAINE (Kaine Autonomous Intelligent Networked Entity), a continuously running predictive global neuronal workspace in which a mind is treated as the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. The paper presents the architecture in its base-thesis form, four predictive processors (two externally grounded, two internal), an affective core that sets the gain on their competition, fatigue-triggered sleep, and an output-only language organ, together with its instruments and the research program they serve: an offline suite of eight experiments, a module-ignition study protocol that adds the held modules one at a time, and a planned workspace-mediation ablation that tests whether the competition does work at all.

**Status: preprint, not peer reviewed.** This is a working draft. Numbers, claims, and the companion empirical results are subject to revision.

## About this version

This is the base-thesis form of the paper. It describes the architecture as designed and built, its instruments, and the planned experiments: nine components are active (seven modules plus the workspace and the action layer), and the remaining seven cognitive modules and the two embodiment modules are built and held, each joining the competition one at a time through the module-ignition study. The planned workspace-mediation ablation (Section 6.3) asks whether routing the processors through the competitive workspace produces behavior that concatenating their outputs does not. The live experiments have not yet been run; their results will be reported in a revised version of this preprint.

## Contents

- [`paper.md`](paper.md): the full paper in Markdown.
- [`paper.pdf`](paper.pdf): the rendered paper, including the figures and module table.
- [`figures/`](figures): the TikZ sources and rendered PNGs for the nine figures, with theme-matched light and dark web versions of all nine in `figures/web`.
- [`EMPIRICAL-NOTES.md`](EMPIRICAL-NOTES.md): implementation history that bears on interpreting data from runs, kept for the empirical paper.
- [`LICENSE`](LICENSE): the Creative Commons Attribution 4.0 International license for the text.
- [`COPYRIGHT`](COPYRIGHT): copyright and licensing summary for the text of the paper.
- [`CITATION.cff`](CITATION.cff): machine-readable citation metadata.

## Abstract

A synthetic mind, if one can be built, may be the coherent global behavior that emerges when specialized predictive modules, each minimizing its own error, compete for a shared workspace with no central executive. This paper presents a continuously running predictive global workspace built on that thesis. The workspace selects the most salient coalition above a confidence threshold and broadcasts it; the broadcast becomes shared state that shapes every module's prediction environment on the next tick. Coherence, where it arises, comes from competition over shared state.

The base-thesis form activates four predictive processors (foveated vision, raw hearing, and interoceptive and temporal prediction), an affective core whose arousal sets the gain on their competition and is itself driven by perceptual surprise, a fatigue-triggered sleep system that returns affect to baseline, and an output-only language organ that verbalizes the entity's state. During the tests the entity is observed, not conversed with: sound enters as auditory prediction error and a classified tone of voice, not as words, and the language organ receives no transcript. That exclusion is a precondition for the test, since any input route to the model would let it answer as a chatbot and confound the ablation; its conversation path with people is built but held off during the tests.

A module-ignition study protocol grows the architecture by adding the held modules one at a time to an entity seeded through a developmental phase. Before any module joins, a workspace-mediation ablation will test the base form against a flat fan-in of the same candidates, under a decision rule fixed before the runs, and a null would demote the architecture to a scored prompt-assembler. Results will follow in a revised version. The reference implementation, KAINE (Kaine Autonomous Intelligent Networked Entity), runs locally on consumer hardware.

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

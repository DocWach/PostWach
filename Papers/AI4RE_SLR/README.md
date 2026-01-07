# AI4RE Systematic Literature Review

## Overview

This is a systematic literature review on **Artificial Intelligence for Requirements Engineering (AI4RE)**, with particular focus on Large Language Models for requirements quality evaluation.

## Files

- `main.tex` - Main LaTeX document
- `references.bib` - BibTeX bibliography with 45+ references
- `README.md` - This file

## Compilation

### Using pdflatex

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Using latexmk (recommended)

```bash
latexmk -pdf main.tex
```

### Using Overleaf

1. Upload all files to a new Overleaf project
2. Set `main.tex` as the main document
3. Compile with pdfLaTeX

## Required Packages

The document uses standard LaTeX packages:
- `natbib` for citations
- `tikz` for diagrams
- `booktabs` for tables
- `hyperref` for links
- `pgfplots` for charts (via tikz)

## Structure

1. **Introduction** - Motivation, research questions, contributions
2. **Background** - RE tasks, NLP history, transformer models
3. **Methodology** - PRISMA search, selection, extraction
4. **Results** - Five thematic areas with evidence synthesis
5. **Discussion** - RQ answers, implications, threats
6. **Research Agenda** - Prioritized future work
7. **Conclusion** - Summary and recommendations

## Key References

The review synthesizes 74 primary studies including:

- Hou et al. (2024) - LLM4SE systematic review
- Hey et al. (2020) - NoRBERT for requirements classification
- Ezzini et al. (2022) - Anaphoric ambiguity handling
- Wach et al. (2024) - "Broken Clock" LLM evaluation study
- Ferrari & Esuli (2019) - Cross-domain ambiguity detection

## Citation

```bibtex
@article{author2026ai4re_slr,
  title={Artificial Intelligence for Requirements Engineering: A Systematic Literature Review of Large Language Models for Requirements Quality Evaluation},
  author={[Author]},
  journal={[Venue]},
  year={2026}
}
```

## License

[To be determined]

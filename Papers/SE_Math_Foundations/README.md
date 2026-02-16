# Mathematical Foundations of Systems Engineering

A research program investigating the minimum set of mathematical tools needed to underpin the systems engineering discipline, with a focus on cross-domain isomorphisms and homomorphisms.

## Overview

This project bridges classical engineering analogies (mechanical-electrical, thermal-hydraulic, etc.) with the systems-theoretic morphism framework established by Wach (2022) using T3SD (Wymorian) and DEVS (Zeigerian) formalisms. The work is organized as a multi-paper research program, each paper addressing one focused idea.

**Current paper (Idea 5):** *A Systematic Catalog of Cross-Domain Isomorphisms and Homomorphisms for Systems Engineering*

## Project Structure

```
Papers/SE_Math_Foundations/
├── library/
│   ├── catalog.json       # 19-entry isomorphism catalog (Tier 1-3)
│   └── schema.json        # JSON Schema for catalog validation
├── src/
│   ├── models/            # System models (MSD, RLC, thermal, rotational)
│   ├── morphisms/         # Morphism distance metrics (planned)
│   ├── simulation/        # ODE integration, discretization, comparison
│   └── visualization/     # Trajectory overlays, degradation plots
├── tests/                 # 38 tests (pytest)
├── notebooks/             # Jupyter demonstrations
├── paper/sections/        # Paper outline stubs (IEEE style)
├── references.bib         # BibTeX references
├── requirements.txt       # Python dependencies
└── effort_report.md       # Session tracking
```

## Isomorphism Catalog

19 cross-domain isomorphism/homomorphism entries organized in three tiers:

| Tier | Entries | Description |
|------|---------|-------------|
| 1 (I-1 to I-7) | Classical physical-domain | MSD/RLC, translational/rotational, electrical/hydraulic, electrical/thermal, electrical/acoustic |
| 2 (I-8 to I-13) | Less common cross-domain | Magnetic, compressible fluid, chemical, population dynamics, s/z-domain, queuing |
| 3 (I-14 to I-19) | Emerging / under-investigated | Neural/electrical, economic/hydraulic, thermodynamic/information, software/control, epidemic/circuit |

## Key Result

Under the force-voltage (Maxwell) analogy, a mass-spring-damper and series RLC circuit produce **identical** continuous-time responses (D = 0 at machine precision). Exact discretization (matrix exponential) preserves this isomorphism; Euler introduces O(dt) error; RK4 introduces O(dt^4) error.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Run tests
python -m pytest tests/ -v

# Launch notebook
jupyter notebook notebooks/01_classical_analogies.ipynb
```

## Research Program

This project is part of a 19-idea research program. See `Papers/Dissertation_Journal/future_research_ideas.md` for the full catalog. Key papers in sequence:

1. **Idea 5** (current): Library of cross-domain isomorphisms
2. **Idea 6**: Degrees of homomorphism metric
3. **Idea 11**: DEVS/T3SD sufficiency analysis
4. **Idea 16**: Category-theoretic framework for SE
5. **Idea 19**: Minimum mathematical toolkit for SE (capstone)

## References

- Wach, P.F. (2022). *Morphic Equivalence Between Discrete System Models for Verification Model Definition*. PhD dissertation, University of Arizona.
- Olson, H.F. (1943). *Dynamical Analogies*. Van Nostrand.
- Karnopp, D.C. et al. (2012). *System Dynamics*. 5th ed. Wiley.
- van der Schaft, A. (2006). Port-Hamiltonian systems: an introductory survey.
- Girard, A. & Pappas, G.J. (2007). Approximation metrics for discrete and continuous systems. IEEE TAC.

See `references.bib` for the full bibliography.

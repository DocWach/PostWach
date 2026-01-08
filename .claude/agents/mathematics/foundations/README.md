# Mathematical Foundations Agents (MSC 03)

Phase 1 of the MSC2020 Mathematics Architecture covering Mathematical Logic and Foundations.

## Overview

This module provides comprehensive coverage of MSC category 03 (Mathematical logic and foundations), implementing 6 specialized agents and 3 skills for foundational mathematics work.

## MSC Coverage

| MSC Code | Subcategory | Agent | Status |
|----------|-------------|-------|--------|
| 03B | General logic | general-logician | Complete |
| 03C | Model theory | model-theorist | Complete |
| 03D | Computability and recursion theory | computability-theorist | Complete |
| 03E | Set theory | set-theorist | Complete |
| 03F | Proof theory and constructive mathematics | (shared by general-logician) | Partial |
| 03G | Algebraic logic | algebraic-logician | Complete |
| 03H | Nonstandard models | nonstandard-analyst | Complete |

## Agents

### set-theorist.md
Primary agent for axiomatic set theory (MSC 03E).

**Capabilities:**
- ZFC axioms and extensions
- Cardinal and ordinal arithmetic
- Transfinite induction and recursion
- Forcing and independence proofs
- Large cardinals
- Descriptive set theory
- Combinatorial set theory

**Key Methods:**
- Cumulative hierarchy (V_α)
- Constructible universe (L)
- Forcing extensions M[G]
- Ultrapower constructions

### model-theorist.md
Primary agent for model theory (MSC 03C).

**Capabilities:**
- First-order structures and satisfaction
- Compactness and Löwenheim-Skolem theorems
- Types and saturation
- Elementary equivalence and embeddings
- Quantifier elimination
- Stability and classification theory
- Ultraproducts

**Key Methods:**
- Back-and-forth arguments
- Type-counting for stability
- Forking independence
- Morley rank analysis

### computability-theorist.md
Primary agent for computability theory (MSC 03D).

**Capabilities:**
- Turing machines and equivalents
- Decidability and undecidability
- Many-one and Turing reductions
- Turing degrees and jump operator
- Arithmetical hierarchy
- Rice's theorem applications
- Recursive function theory

**Key Methods:**
- Diagonalization arguments
- Reduction constructions
- Oracle computations
- Hierarchy classifications

### general-logician.md
Primary agent for general and mathematical logic (MSC 03B).

**Capabilities:**
- Propositional and predicate logic
- Natural deduction and sequent calculus
- Modal and temporal logics
- Intuitionistic logic
- Many-valued logics
- Proof theory
- Gödel's theorems

**Key Methods:**
- Inference rule application
- Proof system analysis
- Completeness and soundness proofs
- Kripke semantics

### algebraic-logician.md
Primary agent for algebraic logic (MSC 03G).

**Capabilities:**
- Boolean algebras and Stone duality
- Heyting algebras
- Cylindric and polyadic algebras
- Modal algebras
- Residuated lattices
- MV-algebras
- Algebraic semantics

**Key Methods:**
- Variety theory
- Stone-type dualities
- Algebraic completeness proofs
- Categorical semantics

### nonstandard-analyst.md
Primary agent for nonstandard models (MSC 03H).

**Capabilities:**
- Ultrapower construction of hyperreals
- Transfer principle
- Infinitesimal calculus
- Internal vs external sets
- Saturation principles
- Loeb measure theory
- Internal Set Theory (IST)

**Key Methods:**
- Standard part calculations
- Hyperfinite sums for integrals
- Nonstandard characterizations
- Transfer arguments

## Skills

### set-theory
Methodologies for axiomatic set theory, cardinal/ordinal arithmetic, forcing, and the cumulative hierarchy.

**Location:** `.claude/skills/set-theory/SKILL.md`

### model-theory
Methodologies for structures, satisfaction, types, stability, quantifier elimination, and ultraproducts.

**Location:** `.claude/skills/model-theory/SKILL.md`

### computability-theory
Methodologies for Turing machines, decidability, reductions, degrees, and the arithmetical hierarchy.

**Location:** `.claude/skills/computability-theory/SKILL.md`

## Hive Integration

### Worker: foundations-specialist
Defined in `.hive-mind/config/workers.json`

Combines all foundation agents for comprehensive logic and set theory work.

### Swarm: foundational-mathematics
Defined in `.hive-mind/config/swarms.json`

6-stage workflow:
1. Problem analysis
2. Framework selection
3. Construction development
4. Proof construction
5. Verification
6. Meta-analysis

## Usage Examples

### Set-Theoretic Problem
```
Task: Prove that 2^ℵ₀ > ℵ₀ (Cantor's theorem)

Agents: set-theorist (primary)
Skills: set-theory, formal-proof
Workflow: Direct proof via diagonal argument
```

### Model-Theoretic Problem
```
Task: Show DLO has quantifier elimination

Agents: model-theorist (primary), general-logician (support)
Skills: model-theory, formal-proof
Workflow: Back-and-forth argument, QE test
```

### Undecidability Proof
```
Task: Prove the halting problem is undecidable

Agents: computability-theorist (primary)
Skills: computability-theory, formal-proof
Workflow: Diagonalization, reduction
```

### Cross-Domain Problem
```
Task: Analyze Gödel's incompleteness via forcing

Agents: set-theorist, computability-theorist, general-logician
Skills: set-theory, computability-theory, formal-proof
Workflow: Use foundational-mathematics swarm
```

## Dependencies

- Integrates with existing mathematics agents (proof-constructor, axiom-architect)
- Philosophy agents (foundationalist-validator, rationalist-synthesizer)
- Research agents (math-research-connector)

## References

### Set Theory
- Kunen, K. (2011). Set Theory
- Jech, T. (2003). Set Theory (3rd millennium ed.)
- Kanamori, A. (2009). The Higher Infinite

### Model Theory
- Marker, D. (2002). Model Theory: An Introduction
- Hodges, W. (1993). Model Theory
- Tent, K. & Ziegler, M. (2012). A Course in Model Theory

### Computability Theory
- Sipser, M. (2012). Introduction to the Theory of Computation
- Rogers, H. (1987). Theory of Recursive Functions
- Soare, R.I. (2016). Turing Computability

### Logic
- Enderton, H.B. (2001). A Mathematical Introduction to Logic
- van Dalen, D. (2013). Logic and Structure
- Troelstra, A.S. & van Dalen, D. (1988). Constructivism in Mathematics

## Next Steps

Phase 2 will add:
- Order, lattice, and general algebraic systems (MSC 06)
- Combinatorics (MSC 05)
- General algebraic systems (MSC 08)

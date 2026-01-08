# Phase 8: Lie Theory & Global Analysis

## Overview

Phase 8 implements the MSC2020 coverage for Lie theory and global analysis, spanning MSC categories 17, 22, and 58. This phase provides comprehensive agents for Lie algebras, Lie groups, and analysis on manifolds.

## MSC Categories Covered

| MSC | Category | Agent(s) |
|-----|----------|----------|
| 17 | Nonassociative rings and algebras | `lie-algebraist` |
| 22 | Topological groups, Lie groups | `lie-group-theorist` |
| 58 | Global analysis, analysis on manifolds | `global-analyst` |

## Agents (3)

### `lie-algebraist` (MSC 17)
Lie algebra specialist covering structure theory, classification, and representation theory.

**Capabilities:**
- Lie brackets and structure constants
- Killing form and Cartan's criteria
- Root systems and Cartan subalgebras
- Semisimple classification (Dynkin diagrams)
- Highest weight representation theory
- Jordan algebras and other nonassociative structures

**Key Theorems:**
- Cartan's Criteria (solvability, semisimplicity)
- Levi Decomposition
- Classification of Simple Lie Algebras
- Weyl Character Formula

### `lie-group-theorist` (MSC 22)
Lie group specialist covering topology, structure, and representation theory.

**Capabilities:**
- Exponential map and Lie correspondence
- Maximal tori and Cartan subgroups
- Structural decompositions (Cartan, Iwasawa, Bruhat)
- Peter-Weyl theorem and harmonic analysis
- Unitary representations
- Classical groups (GL, SL, O, U, Sp)

**Key Theorems:**
- Lie Correspondence
- Peter-Weyl Theorem
- Cartan Decomposition
- Iwasawa Decomposition

### `global-analyst` (MSC 58)
Global analysis specialist covering differential operators, index theory, and spectral geometry.

**Capabilities:**
- Elliptic operators and Fredholm theory
- Atiyah-Singer index theorem
- Heat kernel methods
- Hodge theory
- Spectral geometry and Weyl's law
- Variational methods on manifolds

**Key Theorems:**
- Atiyah-Singer Index Theorem
- Hodge Decomposition
- Weyl's Law
- Bochner-Weitzenböck Formula

## Skills (3)

### `lie-algebras`
Methodology for Lie algebra analysis.

**Subcommands:**
- `/lie-algebras structure <algebra>` - Structure analysis
- `/lie-algebras roots <algebra>` - Root system computation
- `/lie-algebras classify <algebra>` - Classification
- `/lie-algebras representation <algebra> <weight>` - Representation theory
- `/lie-algebras decompose <algebra>` - Levi decomposition
- `/lie-algebras bracket <elements>` - Bracket computation

### `lie-groups`
Methodology for Lie group analysis.

**Subcommands:**
- `/lie-groups structure <group>` - Structure analysis
- `/lie-groups exponential <element>` - Exponential map
- `/lie-groups representation <group> <weight>` - Representation theory
- `/lie-groups decomposition <group>` - Structural decompositions
- `/lie-groups subgroup <group> <subalgebra>` - Subgroup analysis
- `/lie-groups character <representation>` - Character formula

### `global-analysis`
Methodology for global analysis on manifolds.

**Subcommands:**
- `/global-analysis operator <operator>` - Operator analysis
- `/global-analysis index <operator>` - Index computation
- `/global-analysis spectrum <operator>` - Spectral analysis
- `/global-analysis heat-kernel <operator>` - Heat kernel expansion
- `/global-analysis hodge <manifold>` - Hodge theory
- `/global-analysis variational <functional>` - Variational problems

## Worker Type

### `lie-theory-specialist`
Expert worker coordinating all Phase 8 agents.

**Capabilities:**
- Lie algebra structure and classification
- Lie group topology and representations
- Elliptic operators and index theory
- Spectral geometry

## Swarm

### `lie-theory-global-analysis`
Comprehensive swarm for Lie theory and global analysis problems.

**Workflow Stages:**
1. **problem-classification** - Identify problem domain
2. **structure-analysis** - Analyze algebraic/geometric structures
3. **technique-selection** - Choose methods
4. **computation** - Compute invariants
5. **proof-development** - Develop proofs
6. **verification** - Verify results

## Directory Structure

```
.claude/
├── agents/
│   └── mathematics/
│       └── lie-theory/
│           ├── lie-algebraist.md
│           ├── lie-group-theorist.md
│           ├── global-analyst.md
│           └── README.md (this file)
├── skills/
│   ├── lie-algebras/
│   │   └── SKILL.md
│   ├── lie-groups/
│   │   └── SKILL.md
│   └── global-analysis/
│       └── SKILL.md
└── ...

.hive-mind/
└── config/
    ├── workers.json   (lie-theory-specialist added)
    └── swarms.json    (lie-theory-global-analysis added)
```

## Usage Examples

### Lie Algebra Classification
```
User: Classify the Lie algebra with brackets [e,f]=h, [h,e]=2e, [h,f]=-2f

Response flow:
1. lie-algebraist identifies as 3-dimensional
2. Computes Killing form (non-degenerate)
3. Finds root system: type A₁
4. Classifies as 𝔰𝔩(2, ℂ)
```

### Representation Theory
```
User: Find irreducible representations of SU(3)

Response flow:
1. lie-group-theorist identifies maximal torus
2. Determines weight lattice (A₂ type)
3. Classifies by dominant weights (m,n)
4. Computes dimensions via Weyl formula
```

### Index Computation
```
User: Compute index of Dirac operator on 4-manifold

Response flow:
1. global-analyst sets up spin structure
2. Applies Atiyah-Singer theorem
3. Computes Â-genus from curvature
4. Relates to signature and Euler characteristic
```

## Cross-Domain Integration

Phase 8 agents integrate with:
- **Phase 3 (Algebra)**: Representation theory connections
- **Phase 5 (Topology/Geometry)**: Manifold structures
- **Phase 6 (Applied)**: Mathematical physics applications
- **Phase 7 (Algebraic Geometry)**: K-theory and characteristic classes

## Key Concepts

### Lie Theory
- Root systems and Dynkin diagrams
- Weyl group and chambers
- Highest weight modules
- Characters and multiplicities

### Global Analysis
- Elliptic regularity
- Fredholm index
- Heat kernel asymptotics
- Spectral invariants

## References

- Humphreys, J.E. (1972). Introduction to Lie Algebras and Representation Theory
- Knapp, A.W. (2002). Lie Groups Beyond an Introduction
- Hall, B.C. (2015). Lie Groups, Lie Algebras, and Representations
- Berline, Getzler, Vergne (1992). Heat Kernels and Dirac Operators
- Gilkey, P. (1995). Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem

# Phase 7: Algebraic Geometry & K-Theory

## Overview

Phase 7 implements the MSC2020 coverage for algebraic geometry and K-theory, spanning MSC categories 14 and 19. This phase provides comprehensive agents for varieties, schemes, sheaves, cohomology, and K-theoretic methods.

## MSC Categories Covered

| MSC | Category | Agent(s) |
|-----|----------|----------|
| 14 | Algebraic geometry | `algebraic-geometer` |
| 19 | K-theory | `k-theorist` |

## Agents (2)

### `algebraic-geometer` (MSC 14)
Algebraic geometry specialist covering varieties, schemes, sheaves, and cohomology.

**Capabilities:**
- Affine and projective varieties
- Scheme theory (Spec, Proj, gluing)
- Sheaf theory and cohomology
- Divisors and line bundles
- Intersection theory
- Algebraic curves (Riemann-Roch, Jacobian)
- Algebraic surfaces (classification, blow-ups)

**Key Theorems:**
- Hilbert's Nullstellensatz
- Riemann-Roch Theorem
- Serre Duality
- GAGA Principle
- Kodaira Vanishing

### `k-theorist` (MSC 19)
K-theory specialist covering topological and algebraic K-theory.

**Capabilities:**
- Topological K-theory (vector bundles, Bott periodicity)
- Algebraic K-theory (K₀, K₁, higher K-groups)
- Chern character and Chern classes
- Adams operations
- Grothendieck-Riemann-Roch
- K-theory of rings and schemes

**Key Theorems:**
- Bott Periodicity
- Grothendieck-Riemann-Roch
- Quillen's Localization
- Fundamental Theorem of K-theory

## Skills (2)

### `algebraic-geometry`
Methodology for algebraic geometry analysis.

**Subcommands:**
- `/algebraic-geometry variety <equations>` - Analyze varieties
- `/algebraic-geometry scheme <spec>` - Analyze schemes
- `/algebraic-geometry sheaf <sheaf>` - Compute cohomology
- `/algebraic-geometry divisor <divisor>` - Analyze divisors
- `/algebraic-geometry morphism <map>` - Analyze morphisms
- `/algebraic-geometry intersection <cycles>` - Intersection theory

### `k-theory`
Methodology for K-theory computations.

**Subcommands:**
- `/k-theory topological <space>` - Topological K-theory
- `/k-theory algebraic <ring>` - Algebraic K-groups
- `/k-theory chern <bundle>` - Chern character
- `/k-theory adams <element>` - Adams operations
- `/k-theory index <operator>` - Index theorem
- `/k-theory grothendieck <morphism>` - Grothendieck-Riemann-Roch

## Worker Type

### `algebraic-geometry-specialist`
Expert worker coordinating both Phase 7 agents for comprehensive algebraic geometry and K-theory problems.

**Capabilities:**
- Variety and scheme analysis
- Sheaf cohomology
- K-theoretic computations
- Intersection theory
- Riemann-Roch applications

## Swarm

### `algebraic-geometry-k-theory`
Comprehensive swarm for algebraic geometry and K-theory problems.

**Workflow Stages:**
1. **problem-classification** - Identify problem domain
2. **structure-analysis** - Analyze geometric structures
3. **technique-selection** - Choose methods
4. **computation** - Compute invariants
5. **proof-development** - Develop proofs
6. **verification** - Verify results

## Directory Structure

```
.claude/
├── agents/
│   └── mathematics/
│       └── algebraic-geometry/
│           ├── algebraic-geometer.md
│           ├── k-theorist.md
│           └── README.md (this file)
├── skills/
│   ├── algebraic-geometry/
│   │   └── SKILL.md
│   └── k-theory/
│       └── SKILL.md
└── ...

.hive-mind/
└── config/
    ├── workers.json   (algebraic-geometry-specialist added)
    └── swarms.json    (algebraic-geometry-k-theory added)
```

## Usage Examples

### Variety Analysis
```
User: Analyze the cubic surface x³ + y³ + z³ + w³ = 0 in ℙ³

Response flow:
1. algebraic-geometer identifies as degree 3 surface
2. Checks smoothness via Jacobian
3. Computes invariants: Pic = ℤ⁷, 27 lines
4. Classifies as del Pezzo surface
```

### K-theory Computation
```
User: Compute K(ℂℙⁿ)

Response flow:
1. k-theorist applies Bott periodicity
2. Identifies generator [O(1)] - 1
3. Computes ring structure K⁰ = ℤ[H]/(H^{n+1})
4. Relates to cohomology via Chern character
```

### Riemann-Roch Application
```
User: Find h⁰(C, O(D)) for degree 5 divisor on genus 3 curve

Response flow:
1. algebraic-geometer applies Riemann-Roch
2. Computes ℓ(D) - ℓ(K-D) = 5 + 1 - 3 = 3
3. Analyzes whether D is special
4. Provides geometric interpretation
```

## Cross-Domain Integration

Phase 7 agents integrate with:
- **Phase 3 (Algebra)**: Commutative algebra for local rings
- **Phase 4 (Analysis)**: Complex analysis for GAGA
- **Phase 5 (Topology)**: Algebraic topology for K-theory
- **Phase 6 (Applied)**: Intersection theory applications

## Key Concepts

### Algebraic Geometry
- Varieties and schemes
- Sheaves and cohomology
- Divisors and Picard group
- Intersection theory
- Classification of curves/surfaces

### K-Theory
- Grothendieck groups
- Vector bundles
- Bott periodicity
- Chern classes
- Index theorems

## References

- Hartshorne, R. (1977). Algebraic Geometry
- Griffiths & Harris (1978). Principles of Algebraic Geometry
- Atiyah, M.F. (1967). K-Theory
- Weibel, C. (2013). The K-book
- Vakil, R. The Rising Sea (online notes)

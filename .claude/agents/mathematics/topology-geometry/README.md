# Phase 5: Topology & Geometry

## Overview

Phase 5 implements the MSC2020 coverage for topology and geometry, spanning MSC categories 51, 52, 53, 54, 55, and 57. This phase provides comprehensive agents for studying topological spaces, algebraic invariants, differential structures, and classical geometry.

## MSC Categories Covered

| MSC | Category | Agent(s) |
|-----|----------|----------|
| 51 | Geometry | `geometer` |
| 52 | Convex and discrete geometry | `geometer` |
| 53 | Differential geometry | `differential-geometer` |
| 54 | General topology | `general-topologist` |
| 55 | Algebraic topology | `algebraic-topologist` |
| 57 | Manifolds and cell complexes | `algebraic-topologist` |

## Agents (4)

### `general-topologist` (MSC 54)
General topology specialist covering topological spaces, continuity, compactness, connectedness, and separation axioms.

**Capabilities:**
- Topological spaces and bases
- Continuity and homeomorphisms
- Compactness (Heine-Borel, Tychonoff)
- Connectedness and path connectedness
- Separation axioms (T₀-T₄)
- Product and quotient topologies
- Metric spaces
- Convergence and nets

**Key Theorems:**
- Heine-Borel Theorem
- Tychonoff's Theorem
- Urysohn's Lemma
- Tietze Extension Theorem
- Extreme Value Theorem

### `algebraic-topologist` (MSC 55, 57)
Algebraic topology specialist covering homotopy, fundamental group, homology, cohomology, and covering spaces.

**Capabilities:**
- Homotopy and homotopy equivalence
- Fundamental group computation
- Van Kampen theorem
- Covering spaces and lifting
- Singular homology
- Cohomology and cup product
- Exact sequences (pair, Mayer-Vietoris)
- CW complexes

**Key Theorems:**
- Van Kampen Theorem
- Covering Space Classification
- Excision Theorem
- Universal Coefficient Theorem
- Poincaré Duality
- de Rham Theorem

### `differential-geometer` (MSC 53)
Differential geometry specialist covering manifolds, tangent bundles, Riemannian geometry, curvature, and connections.

**Capabilities:**
- Smooth manifolds and atlases
- Tangent and cotangent bundles
- Vector fields and flows
- Differential forms
- Riemannian metrics
- Levi-Civita connection
- Curvature (Riemann, Ricci, scalar)
- Geodesics

**Key Theorems:**
- Inverse Function Theorem
- Frobenius Theorem
- Stokes' Theorem
- Gauss-Bonnet Theorem
- Hopf-Rinow Theorem
- Cartan-Hadamard Theorem

### `geometer` (MSC 51, 52)
Geometry specialist covering Euclidean, projective, affine, and convex geometry.

**Capabilities:**
- Euclidean geometry and isometries
- Triangle and circle theorems
- Projective geometry and duality
- Cross-ratio invariants
- Affine geometry and barycentric coordinates
- Convex sets and polytopes
- Separation theorems
- Geometric transformations

**Key Theorems:**
- Euler Line Theorem
- Pascal's Theorem
- Desargues' Theorem
- Carathéodory's Theorem
- Krein-Milman Theorem
- Euler's Polyhedron Formula

## Skills (4)

### `general-topology`
Methodology for rigorous general topology including topological space analysis and compactness/connectedness arguments.

**Subcommands:**
- `/general-topology space <specification>` - Analyze topological spaces
- `/general-topology continuous <function>` - Verify continuity
- `/general-topology compact <space>` - Analyze compactness
- `/general-topology connected <space>` - Analyze connectedness
- `/general-topology homeomorphism <spaces>` - Determine homeomorphisms
- `/general-topology product <spaces>` - Analyze product/quotient topologies

### `algebraic-topology`
Methodology for algebraic topology including fundamental group computation and homology analysis.

**Subcommands:**
- `/algebraic-topology fundamental-group <space>` - Compute π₁
- `/algebraic-topology covering <space>` - Analyze covering spaces
- `/algebraic-topology homology <space>` - Compute homology groups
- `/algebraic-topology cohomology <space>` - Compute cohomology
- `/algebraic-topology exact-sequence <diagram>` - Apply exact sequences
- `/algebraic-topology homotopy <maps>` - Analyze homotopy equivalences

### `differential-geometry`
Methodology for differential geometry including manifold analysis and curvature computation.

**Subcommands:**
- `/differential-geometry manifold <specification>` - Analyze manifold structure
- `/differential-geometry tangent <manifold>` - Analyze tangent bundles
- `/differential-geometry forms <manifold>` - Work with differential forms
- `/differential-geometry metric <manifold>` - Analyze Riemannian metrics
- `/differential-geometry curvature <metric>` - Compute curvature tensors
- `/differential-geometry connection <bundle>` - Analyze connections

### `geometry`
Methodology for classical geometry including Euclidean, projective, affine, and convex geometry.

**Subcommands:**
- `/geometry euclidean <figure>` - Analyze Euclidean geometry
- `/geometry projective <figure>` - Analyze projective geometry
- `/geometry affine <figure>` - Analyze affine geometry
- `/geometry convex <set>` - Analyze convex geometry
- `/geometry transformation <type>` - Analyze transformations
- `/geometry construction <goal>` - Compass and straightedge

## Worker Type

### `topology-geometry-specialist`
Expert worker coordinating all Phase 5 agents for comprehensive topology and geometry problems.

**Capabilities:**
- General topology (spaces, continuity, compactness)
- Algebraic topology (π₁, homology, cohomology)
- Differential geometry (manifolds, curvature)
- Classical geometry (Euclidean, projective, convex)

## Swarm

### `topology-geometry`
Comprehensive swarm for topology and geometry problems across all four agents.

**Workflow Stages:**
1. **problem-classification** - Identify topology/geometry domain
2. **space-analysis** - Analyze spaces, manifolds, structures
3. **technique-selection** - Choose appropriate methods
4. **computation** - Compute invariants and quantities
5. **proof-development** - Develop rigorous proofs
6. **verification** - Verify correctness

## Directory Structure

```
.claude/
├── agents/
│   └── mathematics/
│       ├── topology/
│       │   ├── general-topologist.md
│       │   └── algebraic-topologist.md
│       ├── geometry/
│       │   ├── differential-geometer.md
│       │   └── geometer.md
│       └── topology-geometry/
│           └── README.md (this file)
├── skills/
│   ├── general-topology/
│   │   └── SKILL.md
│   ├── algebraic-topology/
│   │   └── SKILL.md
│   ├── differential-geometry/
│   │   └── SKILL.md
│   └── geometry/
│       └── SKILL.md
└── ...

.hive-mind/
└── config/
    ├── workers.json   (topology-geometry-specialist added)
    └── swarms.json    (topology-geometry added)
```

## Usage Examples

### Fundamental Group Computation
```
User: Compute π₁(T²)

Response flow:
1. algebraic-topologist identifies T² = S¹ × S¹
2. Applies π₁ of product formula
3. Computes π₁(T²) ≅ ℤ × ℤ
4. Provides generators as loop classes
```

### Compactness Proof
```
User: Prove [0,1]² is compact

Response flow:
1. general-topologist notes [0,1] compact by Heine-Borel
2. Applies Tychonoff's theorem
3. Concludes [0,1]² = [0,1] × [0,1] is compact
4. Alternatively: direct argument via finite subcovers
```

### Curvature Computation
```
User: Find the Gaussian curvature of a sphere of radius R

Response flow:
1. differential-geometer sets up spherical coordinates
2. Computes metric gᵢⱼ
3. Computes Christoffel symbols
4. Calculates Riemann tensor
5. Extracts K = 1/R²
```

### Projective Geometry
```
User: Show that cross-ratio is projectively invariant

Response flow:
1. geometer sets up homogeneous coordinates
2. Defines cross-ratio formula
3. Shows invariance under PGL(2)
4. Provides explicit calculation
```

## Cross-Domain Integration

Phase 5 agents integrate with:
- **Phase 1 (Foundations)**: Logic for rigorous proofs
- **Phase 3 (Algebra)**: Group theory for symmetries, linear algebra for coordinates
- **Phase 4 (Analysis)**: Functional analysis for infinite-dimensional spaces, measure theory for integration on manifolds
- **Future phases**: PDEs on manifolds, algebraic geometry

## Key Concepts

### General Topology
- Topological spaces abstract "nearness" without distance
- Compactness generalizes closed+bounded
- Connectedness means cannot be split by open sets
- Separation axioms (Hausdorff, regular, normal)

### Algebraic Topology
- Fundamental group captures "holes" detectable by loops
- Homology assigns abelian groups to spaces
- Functorial: continuous maps induce homomorphisms
- Covering spaces correspond to subgroups of π₁

### Differential Geometry
- Manifolds are locally Euclidean smooth spaces
- Tangent bundles collect all tangent spaces
- Riemannian metrics enable length, angle, curvature
- Curvature measures deviation from flatness

### Classical Geometry
- Euclidean geometry: isometry invariants
- Projective geometry: cross-ratio invariant
- Affine geometry: parallelism preserved
- Convex geometry: polytopes, separation theorems

## References

- Munkres, J.R. (2000). Topology
- Hatcher, A. (2002). Algebraic Topology
- Lee, J.M. (2018). Introduction to Smooth Manifolds
- Lee, J.M. (2018). Introduction to Riemannian Manifolds
- do Carmo, M. (1992). Riemannian Geometry
- Coxeter, H.S.M. (1969). Introduction to Geometry
- Hartshorne, R. (2000). Geometry: Euclid and Beyond

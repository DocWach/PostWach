# Graph Theory Skill

## Overview

This skill provides methodologies for analyzing graphs as mathematical structures, covering connectivity, coloring, matchings, planarity, and spectral methods.

## When to Use

- Analyzing network structures
- Graph coloring problems
- Matching and covering problems
- Planarity testing and analysis
- Connectivity questions
- Extremal graph problems

---

## Graph Fundamentals

```
DEFINITIONS
═══════════════════════════════════════════════════════════════

GRAPH TYPES
─────────────────────────────────────────
Simple graph: G = (V, E), E ⊆ {{u,v} : u,v ∈ V, u≠v}
Directed graph: E ⊆ V × V
Multigraph: Multiple edges allowed
Weighted graph: w: E → ℝ

NOTATION
─────────────────────────────────────────
n = |V|, m = |E|
deg(v) = degree of v
δ(G) = min degree, Δ(G) = max degree
N(v) = neighbors of v

HANDSHAKING
─────────────────────────────────────────
∑deg(v) = 2m

SPECIAL GRAPHS
─────────────────────────────────────────
Kₙ: Complete graph, C(n,2) edges
Kₘ,ₙ: Complete bipartite
Cₙ: Cycle, Pₙ: Path
Qₙ: n-cube, 2ⁿ vertices
```

## Connectivity

```
PATHS AND CONNECTIVITY
═══════════════════════════════════════════════════════════════

PATH TYPES
─────────────────────────────────────────
Walk: vertices may repeat
Trail: edges don't repeat
Path: vertices don't repeat

CONNECTIVITY MEASURES
─────────────────────────────────────────
κ(G): vertex connectivity (min cut)
λ(G): edge connectivity
κ(G) ≤ λ(G) ≤ δ(G)

MENGER'S THEOREM
─────────────────────────────────────────
Max number of internally disjoint u-v paths = min u-v vertex cut.

EULERIAN
─────────────────────────────────────────
Eulerian circuit exists iff connected and all degrees even.

HAMILTONIAN
─────────────────────────────────────────
Dirac: δ(G) ≥ n/2 implies Hamiltonian (n ≥ 3).
```

## Trees

```
TREE PROPERTIES
═══════════════════════════════════════════════════════════════

EQUIVALENCES
─────────────────────────────────────────
For n-vertex graph:
  □ Connected and acyclic
  □ Connected with n-1 edges
  □ Acyclic with n-1 edges
  □ Unique path between any two vertices

COUNTING
─────────────────────────────────────────
Cayley: n^{n-2} labeled trees on n vertices.

SPANNING TREE ALGORITHMS
─────────────────────────────────────────
Kruskal: Sort edges, add if no cycle (O(m log n))
Prim: Grow from vertex (O(m log n))
```

## Coloring

```
VERTEX COLORING
═══════════════════════════════════════════════════════════════

χ(G) = chromatic number = min k for proper k-coloring

BOUNDS
─────────────────────────────────────────
χ(G) ≥ ω(G)        (clique number)
χ(G) ≤ Δ(G) + 1    (greedy)

Brooks: χ(G) ≤ Δ(G) unless complete or odd cycle.

SPECIAL CASES
─────────────────────────────────────────
Bipartite: χ = 2
Planar: χ ≤ 4 (Four Color Theorem)
Perfect: χ(H) = ω(H) for all induced H

EDGE COLORING
═══════════════════════════════════════════════════════════════

χ'(G) = edge chromatic number

Vizing: Δ(G) ≤ χ'(G) ≤ Δ(G) + 1
König: Bipartite implies χ'(G) = Δ(G).
```

## Matchings

```
MATCHING THEORY
═══════════════════════════════════════════════════════════════

DEFINITIONS
─────────────────────────────────────────
Matching: edges sharing no vertices
ν(G) = max matching size
Perfect: matches all vertices

KEY THEOREMS
─────────────────────────────────────────
Hall: Bipartite G=(X∪Y,E) has X-saturating matching iff
      |N(S)| ≥ |S| for all S ⊆ X.

König: In bipartite, ν(G) = τ(G) (min vertex cover).

Tutte: G has perfect matching iff o(G-S) ≤ |S| for all S.

ALGORITHMS
─────────────────────────────────────────
Augmenting path method: O(mn)
Hopcroft-Karp (bipartite): O(m√n)
```

## Planarity

```
PLANAR GRAPHS
═══════════════════════════════════════════════════════════════

EULER'S FORMULA
─────────────────────────────────────────
n - m + f = 2 (connected plane graph)

BOUNDS
─────────────────────────────────────────
m ≤ 3n - 6 (simple planar, n ≥ 3)
m ≤ 2n - 4 (triangle-free planar)

CHARACTERIZATIONS
─────────────────────────────────────────
Kuratowski: No K₅ or K₃,₃ subdivision.
Wagner: No K₅ or K₃,₃ minor.
```

## Spectral Methods

```
SPECTRAL GRAPH THEORY
═══════════════════════════════════════════════════════════════

ADJACENCY MATRIX
─────────────────────────────────────────
Aᵢⱼ = 1 if ij ∈ E, else 0
(A^k)ᵢⱼ = walks of length k from i to j

LAPLACIAN
─────────────────────────────────────────
L = D - A (D = degree matrix)
μ₂ > 0 iff G connected (algebraic connectivity)

APPLICATIONS
─────────────────────────────────────────
□ Expansion and mixing
□ Chromatic bounds
□ Spectral clustering
```

---

## Integration with Agents

- **graph-theorist**: Primary structural analysis
- **combinatorialist**: Graph enumeration
- **algorithm-designer**: Graph algorithms

---

## References

- Diestel, R. (2017). Graph Theory
- West, D.B. (2001). Introduction to Graph Theory
- Bollobás, B. (1998). Modern Graph Theory

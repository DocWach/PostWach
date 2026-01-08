# Discrete Mathematics Agents (MSC 05, 06, 08)

Phase 2 of the MSC2020 Mathematics Architecture covering Combinatorics, Order Theory, and Universal Algebra.

## Overview

This module provides comprehensive coverage of:
- MSC 05 (Combinatorics)
- MSC 06 (Order, lattices, ordered algebraic structures)
- MSC 08 (General algebraic systems)

Implementing 7 specialized agents and 4 skills for discrete mathematics work.

## MSC Coverage

| MSC Code | Subcategory | Agent | Status |
|----------|-------------|-------|--------|
| 05A | Enumerative combinatorics | combinatorialist | Complete |
| 05C | Graph theory | graph-theorist | Complete |
| 05D | Extremal combinatorics | extremal-combinatorialist | Complete |
| 05D40 | Probabilistic methods | probabilistic-combinatorialist | Complete |
| 06A | Ordered sets | order-theorist | Complete |
| 06B | Lattices | lattice-theorist | Complete |
| 08 | General algebraic systems | universal-algebraist | Complete |

## Agents

### Combinatorics (`.claude/agents/mathematics/combinatorics/`)

#### combinatorialist.md
Primary agent for enumeration and counting (MSC 05A).

**Capabilities:**
- Enumeration and counting
- Generating functions (OGF, EGF)
- Bijective proofs
- Recurrence relations
- Inclusion-exclusion
- Partition theory

#### graph-theorist.md
Primary agent for graph theory (MSC 05C).

**Capabilities:**
- Graph structure (paths, cycles, trees)
- Connectivity and Menger's theorem
- Graph coloring (vertex, edge, chromatic polynomial)
- Matchings (Hall, König, Tutte)
- Planarity (Euler, Kuratowski)
- Spectral graph theory

#### extremal-combinatorialist.md
Primary agent for extremal combinatorics (MSC 05D).

**Capabilities:**
- Ramsey theory
- Turán-type problems
- Extremal set theory (Sperner, EKR)
- Regularity lemma
- Supersaturation

#### probabilistic-combinatorialist.md
Primary agent for probabilistic methods (MSC 05D40).

**Capabilities:**
- First/second moment methods
- Lovász Local Lemma
- Concentration inequalities
- Random graphs (Erdős-Rényi)
- Threshold phenomena

### Order Theory (`.claude/agents/mathematics/order-theory/`)

#### order-theorist.md
Primary agent for ordered sets (MSC 06A).

**Capabilities:**
- Partial orders and posets
- Chains and antichains
- Fixed-point theorems (Knaster-Tarski, Kleene)
- Domain theory
- Order dimension

#### lattice-theorist.md
Primary agent for lattice theory (MSC 06B).

**Capabilities:**
- Lattice structure (joins, meets)
- Distributive and modular lattices
- Boolean algebras
- Congruence theory
- Stone representation

### Universal Algebra (`.claude/agents/mathematics/universal-algebra/`)

#### universal-algebraist.md
Primary agent for general algebraic systems (MSC 08).

**Capabilities:**
- Signatures and algebras
- HSP theorem (Birkhoff)
- Variety theory
- Clone theory
- Maltsev conditions
- Subdirect representation

## Skills

### combinatorics
Location: `.claude/skills/combinatorics/SKILL.md`

Methodologies for counting, generating functions, recurrences, and important sequences (Catalan, Stirling, Bell).

### graph-theory
Location: `.claude/skills/graph-theory/SKILL.md`

Methodologies for graph structure, connectivity, coloring, matchings, and planarity.

### order-theory
Location: `.claude/skills/order-theory/SKILL.md`

Methodologies for posets, lattices, fixed-point theorems, and domain theory.

### universal-algebra
Location: `.claude/skills/universal-algebra/SKILL.md`

Methodologies for abstract algebraic structures, varieties, clones, and Maltsev conditions.

## Hive Integration

### Worker: discrete-math-specialist
Defined in `.hive-mind/config/workers.json`

Combines all 7 discrete mathematics agents with capabilities across combinatorics, graph theory, order theory, and universal algebra.

### Swarm: discrete-mathematics
Defined in `.hive-mind/config/swarms.json`

6-stage workflow:
1. Problem classification
2. Technique selection
3. Pattern exploration
4. Proof development
5. Verification
6. Generalization

## Usage Examples

### Enumeration Problem
```
Task: Find number of ways to tile a 2×n board with dominoes

Agents: combinatorialist (primary)
Skills: combinatorics, formal-proof
Workflow: Recurrence → Generating function → Closed form
Result: Fibonacci numbers
```

### Graph Coloring Problem
```
Task: Prove Brooks' theorem (χ(G) ≤ Δ unless complete/odd cycle)

Agents: graph-theorist (primary), theorem-prover (support)
Skills: graph-theory, formal-proof
Workflow: Greedy argument with careful ordering
```

### Ramsey Theory Problem
```
Task: Show R(3,3) = 6

Agents: extremal-combinatorialist (primary)
Skills: combinatorics, formal-proof
Workflow: Upper bound (pigeonhole) + lower bound (K₅ construction)
```

### Lattice Theory Problem
```
Task: Prove finite distributive lattices are characterized by no N₅ or M₃

Agents: lattice-theorist (primary)
Skills: order-theory, formal-proof
Workflow: Birkhoff representation theorem
```

## Dependencies

- Integrates with Phase 1 foundations agents (set-theorist for infinite combinatorics)
- Philosophy agents (rationalist-synthesizer, empiricist-gatherer)
- Existing math workers (theorem-prover, pattern-analyst)

## Cross-Phase Connections

### Phase 1 → Phase 2
- Set theory → Infinite combinatorics, cardinal arithmetic
- Model theory → Ultraproducts in combinatorics
- Computability → Decidability of combinatorial problems

### Phase 2 → Future Phases
- Graph theory → Algebraic graph theory (Phase 3: Algebra)
- Order theory → Topology (Phase 5)
- Universal algebra → Category theory (Phase 3)

## References

### Combinatorics
- Stanley, R.P. (2011). Enumerative Combinatorics
- Wilf, H.S. (2005). generatingfunctionology
- Graham, Knuth, Patashnik (1994). Concrete Mathematics

### Graph Theory
- Diestel, R. (2017). Graph Theory
- Bollobás, B. (1998). Modern Graph Theory

### Extremal/Probabilistic
- Alon & Spencer (2016). The Probabilistic Method
- Jukna, S. (2011). Extremal Combinatorics

### Order/Lattice Theory
- Davey & Priestley (2002). Introduction to Lattices and Order
- Grätzer, G. (2011). Lattice Theory: Foundation

### Universal Algebra
- Burris & Sankappanavar (1981). A Course in Universal Algebra
- McKenzie, McNulty, Taylor (1987). Algebras, Lattices, Varieties

## Next Steps

Phase 3 will add:
- Number theory (MSC 11)
- Field theory and polynomials (MSC 12)
- Commutative algebra (MSC 13)
- Algebraic geometry (MSC 14)
- Linear and multilinear algebra (MSC 15)
- Associative/nonassociative/category theory (MSC 16-18)

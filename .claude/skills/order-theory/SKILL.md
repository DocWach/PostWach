# Order Theory Skill

## Overview

This skill provides methodologies for partially ordered sets, lattices, fixed-point theorems, and domain theory. It covers order-theoretic structures fundamental to algebra, logic, and computer science.

## When to Use

- Analyzing poset structure
- Working with lattices
- Applying fixed-point theorems
- Domain-theoretic semantics
- Order dimension questions

---

## Poset Fundamentals

```
PARTIAL ORDERS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Partial order ≤ on P:
  □ Reflexive: x ≤ x
  □ Antisymmetric: x ≤ y ∧ y ≤ x → x = y
  □ Transitive: x ≤ y ∧ y ≤ z → x ≤ z

SPECIAL ELEMENTS
─────────────────────────────────────────
Minimum: ⊥ ≤ x for all x
Maximum: x ≤ ⊤ for all x
Minimal: no y < x
Maximal: no y > x

CHAINS AND ANTICHAINS
─────────────────────────────────────────
Chain: totally ordered subset
Antichain: pairwise incomparable

Dilworth: width = min chain cover
Mirsky: height = min antichain cover
```

## Bounds and Completeness

```
BOUNDS
═══════════════════════════════════════════════════════════════

DEFINITIONS
─────────────────────────────────────────
Upper bound of S: u with s ≤ u for all s ∈ S
Supremum: least upper bound, sup(S) = ∨S
Infimum: greatest lower bound, inf(S) = ∧S

COMPLETENESS CONDITIONS
─────────────────────────────────────────
Complete lattice: Every S has sup and inf
DCPO: Every directed S has sup
Chain complete: Every chain has sup
ω-complete: Every ascending chain has sup

LATTICES
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Lattice: Every pair has sup (join ∨) and inf (meet ∧).

AXIOMS (algebraic)
─────────────────────────────────────────
Idempotent: x ∨ x = x, x ∧ x = x
Commutative: x ∨ y = y ∨ x, x ∧ y = y ∧ x
Associative: (x∨y)∨z = x∨(y∨z)
Absorption: x ∨ (x ∧ y) = x, x ∧ (x ∨ y) = x

SPECIAL LATTICES
─────────────────────────────────────────
Distributive: x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)
  No N₅ or M₃ sublattice

Modular: x ≤ z → x ∨ (y ∧ z) = (x ∨ y) ∧ z
  No N₅ sublattice

Boolean: Complemented distributive
```

## Fixed-Point Theorems

```
KNASTER-TARSKI
═══════════════════════════════════════════════════════════════

THEOREM
─────────────────────────────────────────
If L is complete lattice and f: L → L is monotone,
then Fix(f) is nonempty complete lattice.

lfp(f) = ∧{x : f(x) ≤ x}
gfp(f) = ∨{x : x ≤ f(x)}

KLEENE FIXED-POINT
═══════════════════════════════════════════════════════════════

THEOREM
─────────────────────────────────────────
If L is dcpo with ⊥ and f: L → L is Scott-continuous:
  lfp(f) = ∨{fⁿ(⊥) : n ∈ ω}

APPLICATIONS
─────────────────────────────────────────
□ Recursive definitions in semantics
□ Dataflow analysis
□ Abstract interpretation
```

## Domain Theory

```
DOMAINS
═══════════════════════════════════════════════════════════════

APPROXIMATION
─────────────────────────────────────────
x ≪ y (way below): For directed D with y ≤ ∨D, ∃d ∈ D: x ≤ d

Continuous: Every x = ∨{y : y ≪ x}
Algebraic: Every x = ∨{compact k : k ≤ x}

SCOTT TOPOLOGY
─────────────────────────────────────────
Open U: upward closed, inaccessible by directed sups
f continuous iff f preserves directed sups

FUNCTION SPACES
─────────────────────────────────────────
[D → E] = continuous functions with pointwise order
Forms domain, allows D ≅ [D → D].
```

---

## Integration with Agents

- **order-theorist**: Primary poset analysis
- **lattice-theorist**: Lattice-specific structure
- **set-theorist**: Well-orderings

---

## References

- Davey & Priestley (2002). Introduction to Lattices and Order
- Gierz et al. (2003). Continuous Lattices and Domains

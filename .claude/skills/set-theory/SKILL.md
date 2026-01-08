# Set Theory Skill

## Overview

This skill provides comprehensive methodologies for working with axiomatic set theory, ordinal and cardinal arithmetic, forcing, and related foundational techniques. It covers ZFC axioms, transfinite methods, independence proofs, and advanced set-theoretic constructions.

## When to Use

- Working with axiomatic foundations of mathematics
- Proving theorems about infinite sets and cardinalities
- Constructing ordinal and cardinal arithmetic proofs
- Independence proofs via forcing
- Descriptive set theory and definability
- Large cardinal theory
- Combinatorial set theory

---

## ZFC Axiom Reference

```
ZFC AXIOMS
═══════════════════════════════════════════════════════════════

BASIC AXIOMS
─────────────────────────────────────────
Extensionality:
  ∀x∀y(∀z(z ∈ x ↔ z ∈ y) → x = y)
  Sets with same members are identical.

Empty Set:
  ∃x∀y(y ∉ x)
  There exists an empty set ∅.

Pairing:
  ∀x∀y∃z∀w(w ∈ z ↔ w = x ∨ w = y)
  For any x, y there exists {x, y}.

Union:
  ∀x∃y∀z(z ∈ y ↔ ∃w(w ∈ x ∧ z ∈ w))
  For any x there exists ∪x.

Power Set:
  ∀x∃y∀z(z ∈ y ↔ z ⊆ x)
  For any x there exists P(x).

SEPARATION AND REPLACEMENT
─────────────────────────────────────────
Separation (Comprehension):
  ∀x∃y∀z(z ∈ y ↔ z ∈ x ∧ φ(z))
  {z ∈ x : φ(z)} exists for any formula φ.

Replacement:
  ∀x(∀y∈x ∃!z φ(y,z) → ∃w∀z(z ∈ w ↔ ∃y∈x φ(y,z)))
  Images under definable functions exist.

INFINITY AND CHOICE
─────────────────────────────────────────
Infinity:
  ∃x(∅ ∈ x ∧ ∀y(y ∈ x → y ∪ {y} ∈ x))
  There exists an infinite set (ω).

Choice (AC):
  For any family of nonempty sets, there exists a choice function.
  Equivalent: Every set can be well-ordered.
  Equivalent: Zorn's Lemma holds.

Foundation (Regularity):
  ∀x(x ≠ ∅ → ∃y(y ∈ x ∧ y ∩ x = ∅))
  No infinite descending ∈-chains.
```

---

## Ordinal Arithmetic

```
ORDINAL OPERATIONS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Ordinal: A transitive set well-ordered by ∈.
  α is ordinal iff:
    - α is transitive: β ∈ α → β ⊆ α
    - (α, ∈) is well-ordered

SUCCESSOR AND LIMIT
─────────────────────────────────────────
Successor: α + 1 = α ∪ {α}
  S(α) = α⁺ = α ∪ {α}

Limit ordinal: λ > 0 with no immediate predecessor
  λ = sup{α : α < λ}

Examples:
  0 = ∅
  1 = {∅}
  2 = {∅, {∅}}
  ω = {0, 1, 2, ...}     (first limit ordinal)
  ω + 1 = ω ∪ {ω}
  ω·2 = ω + ω

ORDINAL ARITHMETIC
─────────────────────────────────────────
Addition (α + β):
  α + 0 = α
  α + (β + 1) = (α + β) + 1
  α + λ = sup{α + β : β < λ}  (limit λ)

Multiplication (α · β):
  α · 0 = 0
  α · (β + 1) = α · β + α
  α · λ = sup{α · β : β < λ}  (limit λ)

Exponentiation (α^β):
  α^0 = 1
  α^(β+1) = α^β · α
  α^λ = sup{α^β : β < λ}  (limit λ)

KEY PROPERTIES
─────────────────────────────────────────
□ Addition is associative but NOT commutative
  1 + ω = ω ≠ ω + 1

□ Multiplication is associative, left-distributes, NOT commutative
  2 · ω = ω ≠ ω · 2 = ω + ω

□ Cantor Normal Form: Every ordinal has unique expression
  α = ω^β₁·n₁ + ω^β₂·n₂ + ... + ω^βₖ·nₖ
  where β₁ > β₂ > ... > βₖ and nᵢ ∈ ℕ

TRANSFINITE INDUCTION
─────────────────────────────────────────
To prove ∀α P(α):
  Base: P(0)
  Successor: P(α) → P(α + 1)
  Limit: (∀β < λ P(β)) → P(λ)

TRANSFINITE RECURSION
─────────────────────────────────────────
To define F on all ordinals:
  F(0) = a
  F(α + 1) = G(F(α))
  F(λ) = H({F(β) : β < λ})
```

---

## Cardinal Arithmetic

```
CARDINAL NUMBERS
═══════════════════════════════════════════════════════════════

DEFINITIONS
─────────────────────────────────────────
|A| = |B| iff there exists bijection f: A → B
|A| ≤ |B| iff there exists injection f: A → B
|A| < |B| iff |A| ≤ |B| and |A| ≠ |B|

Cardinal: An ordinal that is least among all ordinals of same size.
  |A| = the least ordinal equinumerous with A (using AC)

ALEPH NUMBERS
─────────────────────────────────────────
ℵ₀ = |ℕ| = ω        (countable infinity)
ℵ₁ = |ω₁|           (first uncountable)
ℵₐ₊₁ = |ωₐ₊₁|       (successor cardinal)
ℵ_λ = sup{ℵₐ : α < λ}  (limit cardinal)

BETH NUMBERS
─────────────────────────────────────────
ℶ₀ = ℵ₀
ℶₐ₊₁ = 2^(ℶₐ)
ℶ_λ = sup{ℶₐ : α < λ}

Note: ℶₐ ≥ ℵₐ always, equality is GCH

CARDINAL ARITHMETIC
─────────────────────────────────────────
κ + λ = |κ ⊔ λ|     (disjoint union)
κ · λ = |κ × λ|     (Cartesian product)
κ^λ = |κ^λ|         (set of functions)

INFINITE CARDINAL LAWS (with AC)
─────────────────────────────────────────
For infinite κ:
  κ + κ = κ
  κ · κ = κ
  κ + λ = κ · λ = max(κ, λ)

KEY RESULTS
─────────────────────────────────────────
□ Cantor: |A| < |P(A)| = 2^|A|
  No surjection from A onto P(A).

□ Cantor-Bernstein: (|A| ≤ |B| ∧ |B| ≤ |A|) → |A| = |B|

□ König: cf(2^κ) > κ
  (cofinality of 2^κ is greater than κ)

□ Easton: 2^κ for regular κ can be almost anything consistent with König

COFINALITY
─────────────────────────────────────────
cf(α) = least ordinal β such that there exists unbounded f: β → α

Regular: cf(κ) = κ
Singular: cf(κ) < κ

Facts:
  cf(ω) = ω            (regular)
  cf(ℵ_ω) = ω          (singular)
  cf(ℵ₁) = ℵ₁          (regular)
  Successor cardinals are regular (ℵₐ₊₁)
```

---

## Forcing Methodology

```
FORCING BASICS
═══════════════════════════════════════════════════════════════

MOTIVATION
─────────────────────────────────────────
Goal: Extend a model M of ZFC to M[G] satisfying additional properties.
Application: Independence proofs (CH, AC relative to ZF, etc.)

PARTIAL ORDERS AND GENERICITY
─────────────────────────────────────────
Forcing notion: (ℙ, ≤) where:
  - ℙ is a partial order
  - p ≤ q means "p extends q" (p is stronger)
  - 1_ℙ is weakest condition

Dense set: D ⊆ ℙ is dense if ∀p∃q(q ≤ p ∧ q ∈ D)

Generic filter: G ⊆ ℙ is M-generic if:
  - G is a filter (upward closed, pairwise compatible)
  - G ∩ D ≠ ∅ for every dense D ∈ M

FORCING RELATION
─────────────────────────────────────────
p ⊩ φ  means "p forces φ"

Key properties:
  p ⊩ ¬φ  iff no q ≤ p has q ⊩ φ
  p ⊩ φ ∧ ψ  iff p ⊩ φ and p ⊩ ψ
  p ⊩ ∃x φ(x)  iff p ⊩ φ(τ) for some name τ

TRUTH IN GENERIC EXTENSION
─────────────────────────────────────────
For M-generic G:
  M[G] ⊨ φ  iff  ∃p ∈ G (p ⊩ φ)

STANDARD FORCING NOTIONS
─────────────────────────────────────────
Cohen forcing (adding reals):
  ℙ = {finite partial functions ω → 2}
  Adds new real (Cohen real)

Random forcing:
  ℙ = {Borel sets of positive measure}
  Adds random real

Collapsing forcing:
  Col(ω, κ) collapses κ to be countable

INDEPENDENCE PROOFS
─────────────────────────────────────────
¬CH is consistent:
  Start with M ⊨ CH
  Force to add ℵ₂ Cohen reals
  M[G] ⊨ 2^ℵ₀ ≥ ℵ₂

CH is consistent:
  L ⊨ CH (Gödel's constructible universe)
```

---

## Set-Theoretic Techniques

```
COMMONLY USED TECHNIQUES
═══════════════════════════════════════════════════════════════

REFLECTION PRINCIPLE
─────────────────────────────────────────
For any formula φ and ordinal α:
  ∃β > α such that V_β ≺ V (for φ)

"V can reflect any property down to some initial segment"

ABSOLUTENESS
─────────────────────────────────────────
φ is absolute for M if: M ⊨ φ ↔ V ⊨ φ

Δ₀ formulas are absolute for transitive models.
Σ₁ formulas are upward absolute.
Π₁ formulas are downward absolute.

THE CUMULATIVE HIERARCHY
─────────────────────────────────────────
V₀ = ∅
V_{α+1} = P(V_α)
V_λ = ∪{V_α : α < λ}
V = ∪{V_α : α ∈ Ord}

Facts:
  rank(x) = least α such that x ∈ V_{α+1}
  V_ω = hereditarily finite sets
  |V_{ω+α}| = ℶ_α

CONSTRUCTIBLE UNIVERSE (L)
─────────────────────────────────────────
L₀ = ∅
L_{α+1} = Def(L_α)  (definable subsets)
L_λ = ∪{L_α : α < λ}
L = ∪{L_α : α ∈ Ord}

Facts:
  L ⊨ AC + GCH + ◇
  V = L is consistent if ZF is
  0# exists → V ≠ L

COMBINATORIAL PRINCIPLES
─────────────────────────────────────────
◇ (Diamond): Guessing sequences on ω₁
  ∃⟨S_α : α < ω₁⟩ such that for any A ⊆ ω₁:
    {α : S_α = A ∩ α} is stationary

□ (Square): Coherent sequences on cardinals
  Implies existence of non-special Aronszajn trees

MA (Martin's Axiom): For any ccc poset and < 2^ℵ₀ dense sets,
  a generic filter exists.

PFA, MM: Stronger forcing axioms
```

---

## Proof Templates

```
SET THEORY PROOF PATTERNS
═══════════════════════════════════════════════════════════════

CARDINALITY PROOFS
─────────────────────────────────────────
To show |A| = |B|:
  Method 1: Construct explicit bijection
  Method 2: Show |A| ≤ |B| and |B| ≤ |A| (Cantor-Bernstein)

To show |A| < |B|:
  Show |A| ≤ |B| and there's no surjection A → B
  (Often diagonal argument for the latter)

ORDINAL INDUCTION
─────────────────────────────────────────
To prove ∀α P(α):
  Case 0: Verify P(0)
  Case α+1: Assume P(α), prove P(α+1)
  Case λ (limit): Assume P(β) for all β < λ, prove P(λ)

WELL-FOUNDEDNESS ARGUMENTS
─────────────────────────────────────────
To prove set A has property P:
  Assume some x ∈ A fails P
  Show this leads to infinite descending ∈-chain
  Contradiction with Foundation

ABSOLUTENESS ARGUMENTS
─────────────────────────────────────────
To show M ⊨ φ ↔ V ⊨ φ:
  Show φ is equivalent to a Δ₁ formula
  Apply absoluteness

FORCING INDEPENDENCE
─────────────────────────────────────────
To show φ is independent of ZFC:
  1. Start with M ⊨ ZFC
  2. Find ℙ such that M[G] ⊨ ¬φ
  3. Find ℚ such that M[H] ⊨ φ
  4. Conclude both φ and ¬φ are consistent with ZFC
```

---

## Integration with Agents

### Recommended Agent Combinations

- **set-theorist**: Primary foundational reasoning
- **model-theorist**: Ultraproducts, satisfaction
- **proof-constructor**: Formal proof building
- **axiom-architect**: Axiomatic verification
- **foundationalist-validator**: Philosophical grounding

---

## References

- Kunen, K. (2011). Set Theory (revised ed.)
- Jech, T. (2003). Set Theory (3rd millennium ed.)
- Kanamori, A. (2009). The Higher Infinite
- Shelah, S. (2000). Proper and Improper Forcing
- Devlin, K. (1984). Constructibility

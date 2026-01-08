# Model Theory Skill

## Overview

This skill provides comprehensive methodologies for working with structures, theories, and the model-theoretic analysis of mathematical objects. It covers satisfaction relations, compactness and Löwenheim-Skolem theorems, types, stability theory, and classification theory.

## When to Use

- Analyzing mathematical structures through logical lenses
- Proving existence/non-existence of models with properties
- Working with elementary equivalence and embeddings
- Type-theoretic reasoning over structures
- Classification of theories (stable, simple, NIP, etc.)
- Quantifier elimination arguments
- Definability questions

---

## Structures and Languages

```
FIRST-ORDER STRUCTURES
═══════════════════════════════════════════════════════════════

LANGUAGE
─────────────────────────────────────────
A first-order language L consists of:
  - Constant symbols: c₁, c₂, ...
  - Function symbols: f₁, f₂, ... with arities
  - Relation symbols: R₁, R₂, ... with arities
  - Logical symbols: =, ¬, ∧, ∨, →, ∀, ∃

STRUCTURE
─────────────────────────────────────────
An L-structure M = (M, ...) consists of:
  - A nonempty set M (the domain/universe)
  - For each constant c: an element c^M ∈ M
  - For each n-ary function f: a function f^M: M^n → M
  - For each n-ary relation R: a subset R^M ⊆ M^n

EXAMPLES
─────────────────────────────────────────
L_ring = {0, 1, +, ·}
  - (ℤ, 0, 1, +, ·)  -- integers
  - (ℚ, 0, 1, +, ·)  -- rationals
  - (ℝ, 0, 1, +, ·)  -- reals

L_order = {<}
  - (ℚ, <)  -- rationals with ordering
  - (ℝ, <)  -- reals with ordering

L_graph = {E}  (binary edge relation)
  - Any graph (V, E)

TERMS AND FORMULAS
─────────────────────────────────────────
Terms: Built from constants, variables, function symbols
Atomic formulas: t₁ = t₂ or R(t₁,...,tₙ)
Formulas: Closed under ¬, ∧, ∨, →, ∀x, ∃x

Sentence: Formula with no free variables
Theory: Set of sentences
```

---

## Satisfaction and Truth

```
SATISFACTION RELATION
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
M ⊨ φ[a₁,...,aₙ] means "M satisfies φ with aᵢ for xᵢ"

Recursive definition:
  M ⊨ t₁ = t₂[ā]     iff  t₁^M[ā] = t₂^M[ā]
  M ⊨ R(t₁,...,tₖ)[ā] iff  (t₁^M[ā],...,tₖ^M[ā]) ∈ R^M
  M ⊨ ¬φ[ā]          iff  M ⊭ φ[ā]
  M ⊨ φ ∧ ψ[ā]       iff  M ⊨ φ[ā] and M ⊨ ψ[ā]
  M ⊨ ∀x φ[ā]        iff  for all b ∈ M: M ⊨ φ[b,ā]
  M ⊨ ∃x φ[ā]        iff  for some b ∈ M: M ⊨ φ[b,ā]

For sentence σ: M ⊨ σ means "M is a model of σ"

THEORY OF A STRUCTURE
─────────────────────────────────────────
Th(M) = {σ : M ⊨ σ}  (all sentences true in M)

Complete theory: T such that for all σ: T ⊢ σ or T ⊢ ¬σ

Model of T: M such that M ⊨ σ for all σ ∈ T

ELEMENTARY EQUIVALENCE
─────────────────────────────────────────
M ≡ N  iff  Th(M) = Th(N)
         iff  for all sentences σ: M ⊨ σ ↔ N ⊨ σ

Examples:
  (ℚ, <) ≡ (ℝ, <)    (both dense linear orders without endpoints)
  (ℤ, +) ≢ (ℚ, +)    (divisibility differs)

ELEMENTARY EMBEDDING
─────────────────────────────────────────
f: M → N is elementary  iff
  for all φ(x₁,...,xₙ) and a₁,...,aₙ ∈ M:
    M ⊨ φ[a₁,...,aₙ]  ↔  N ⊨ φ[f(a₁),...,f(aₙ)]

Notation: M ≺ N means M is an elementary substructure of N
```

---

## Fundamental Theorems

```
COMPACTNESS THEOREM
═══════════════════════════════════════════════════════════════

STATEMENT
─────────────────────────────────────────
T has a model  iff  every finite T₀ ⊆ T has a model.

Equivalently:
  If T ⊨ φ then T₀ ⊨ φ for some finite T₀ ⊆ T.

APPLICATIONS
─────────────────────────────────────────
Existence of nonstandard models:
  Let T = Th(ℕ) ∪ {c > n : n ∈ ℕ}
  Every finite subset has a model (interpret c as large n)
  By compactness, T has a model with "infinite" element

Non-finite-axiomatizability:
  To show theory T is not finitely axiomatizable:
  Find sequence of non-models M₁, M₂, ... approaching models

Transfer of finite character properties:
  P holds in all finite structures → P holds in some infinite structure
  (with appropriate formulation)

LÖWENHEIM-SKOLEM THEOREMS
═══════════════════════════════════════════════════════════════

DOWNWARD
─────────────────────────────────────────
If M ⊨ T and A ⊆ M with |A| ≤ κ ≥ |L|, then
  ∃N ≺ M with A ⊆ N and |N| = κ

Corollary: If T has infinite model, T has countable model.

UPWARD
─────────────────────────────────────────
If M ⊨ T and |M| ≥ |L| and κ > |M|, then
  ∃N ⪰ M with |N| = κ

Corollary: If T has infinite model, T has models of all infinite sizes.

IMPLICATIONS
─────────────────────────────────────────
□ No first-order theory characterizes exactly one infinite cardinality
□ Categoricity in one uncountable cardinal has strong implications
□ "There are exactly n elements" is expressible for finite n, not for ℵ₀
```

---

## Types and Saturation

```
TYPES
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
An n-type over A in M is a maximal consistent set of formulas φ(x₁,...,xₙ)
with parameters from A.

p(x̄) = {φ(x̄,ā) : M ⊨ φ(b̄,ā) for fixed b̄}  -- type realized by b̄

TYPE SPACE
─────────────────────────────────────────
Sₙ(T) = space of n-types over ∅ consistent with T
Sₙ(A) = space of n-types over A in a monster model

Topology: Stone topology (compact, Hausdorff, totally disconnected)
  Basic open: [φ] = {p : φ ∈ p}

REALIZED VS OMITTED TYPES
─────────────────────────────────────────
Type p is realized in M if some ā ∈ M^n satisfies all φ ∈ p.
Type p is omitted in M if p is not realized.

OMITTING TYPES THEOREM
─────────────────────────────────────────
If T is a countable complete theory and Γ = {pᵢ : i ∈ ω} are
non-isolated types, then T has a model omitting all pᵢ.

Isolation: p is isolated if there exists φ with [φ] = {p}.

SATURATION
═══════════════════════════════════════════════════════════════

DEFINITIONS
─────────────────────────────────────────
M is κ-saturated if:
  For all A ⊆ M with |A| < κ,
  every 1-type over A is realized in M.

M is saturated if M is |M|-saturated.

M is ω-saturated (countably saturated) if:
  Every type over a finite set is realized.

PROPERTIES
─────────────────────────────────────────
□ Saturated models are "universal" in their cardinality class
□ Saturated models of same cardinality are isomorphic
□ Existence of saturated models requires set-theoretic assumptions
  (GCH or κ^{<κ} = κ)

HOMOGENEITY
─────────────────────────────────────────
M is κ-homogeneous if:
  For all A ⊆ M with |A| < κ,
  any elementary map A → M extends to an automorphism.

Saturation implies homogeneity.
```

---

## Classification Theory

```
STABILITY THEORY
═══════════════════════════════════════════════════════════════

COUNTING TYPES
─────────────────────────────────────────
T is stable in κ if |S₁(A)| ≤ κ for all |A| ≤ κ.

T is stable if stable in some κ ≥ |T|.

T is superstable if stable in all κ ≥ 2^|T|.

T is ω-stable if |S₁(A)| ≤ |A| + ℵ₀ for all A.

STABILITY HIERARCHY
─────────────────────────────────────────
ω-stable ⊂ superstable ⊂ stable ⊂ simple ⊂ NIP

EXAMPLES
─────────────────────────────────────────
ω-stable:
  - Algebraically closed fields (ACF)
  - Vector spaces
  - Divisible abelian groups

Superstable but not ω-stable:
  - Differentially closed fields

Stable but not superstable:
  - Separably closed fields (imperfect case)

Unstable:
  - Dense linear orders (DLO)
  - Random graph
  - Arithmetic (with ×)

INDEPENDENCE AND FORKING
═══════════════════════════════════════════════════════════════

FORKING
─────────────────────────────────────────
In stable theories, p(x) forks over A if:
  p(x) implies a disjunction of formulas, each dividing over A.

φ(x,b) divides over A if there exist (bᵢ)_{i<ω} with:
  tp(bᵢ/A) = tp(b/A) and {φ(x,bᵢ)} is k-inconsistent.

INDEPENDENCE
─────────────────────────────────────────
a ⫝_A b  means "a is independent from b over A"
        means tp(a/Ab) does not fork over A

Properties in stable theories:
  - Symmetry: a ⫝_A b iff b ⫝_A a
  - Transitivity: a ⫝_A bc and a ⫝_{Ab} c implies a ⫝_A c
  - Extension: Any type has non-forking extension
  - Local character: tp(a/B) doesn't fork over some A ⊆ B, |A| ≤ |T|

MORLEY RANK
─────────────────────────────────────────
For definable set D:
  RM(D) ≥ 0 if D ≠ ∅
  RM(D) ≥ α+1 if infinitely many disjoint D_i ⊆ D with RM(D_i) ≥ α
  RM(D) ≥ λ if RM(D) ≥ α for all α < λ

Morley degree: Number of disjoint sets of maximal rank.

ω-stable iff every formula has ordinal Morley rank.
```

---

## Quantifier Elimination

```
QUANTIFIER ELIMINATION
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
T has QE if every formula is equivalent (mod T) to a quantifier-free formula.

CONSEQUENCES
─────────────────────────────────────────
□ Every definable set is a boolean combination of atomic sets
□ Substructure test for elementary embedding
□ Types determined by atomic formulas
□ Often implies model completeness

TEST FOR QE
─────────────────────────────────────────
T has QE iff:
  For any M, N ⊨ T with common substructure A,
  and a ∈ M, there exists b ∈ N such that
  (A, a) and (A, b) satisfy same quantifier-free formulas.

EXAMPLES WITH QE
─────────────────────────────────────────
□ DLO (dense linear orders without endpoints)
  Every formula ↔ boolean combination of x < y, x = y

□ ACF_p (algebraically closed fields of characteristic p)
  Every formula ↔ polynomial equations/inequations

□ RCF (real closed fields) with order
  Every formula ↔ polynomial inequalities

□ Presburger arithmetic (ℤ, +, <)
  Every formula ↔ linear inequalities + congruences

□ ACVF (algebraically closed valued fields)
  With valuation and residue field sorts

MODEL COMPLETENESS
─────────────────────────────────────────
T is model complete if:
  M ⊆ N with M, N ⊨ T implies M ≺ N

QE implies model completeness.
Model completeness + witness implies QE.
```

---

## Ultraproducts

```
ULTRAPRODUCT CONSTRUCTION
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Given:
  - Index set I
  - Structures {Mᵢ : i ∈ I}
  - Ultrafilter U on I

Ultraproduct: ∏_U Mᵢ = (∏ᵢ Mᵢ) / ~_U

where (aᵢ) ~_U (bᵢ) iff {i : aᵢ = bᵢ} ∈ U

ŁOSIOM THEOREM
─────────────────────────────────────────
∏_U Mᵢ ⊨ φ[(aᵢ)_U]  iff  {i : Mᵢ ⊨ φ[aᵢ]} ∈ U

APPLICATIONS
─────────────────────────────────────────
Compactness: Alternative proof via ultraproducts
  If every finite T₀ ⊆ T has model, use ultraproduct of finite models.

Existence of saturated models:
  Ultrapower ∏_U M for good ultrafilter gives saturation.

Nonstandard analysis:
  *ℝ = ∏_U ℝ (ultrapower of reals)

KEISLER-SHELAH THEOREM
─────────────────────────────────────────
M ≡ N  iff  ∏_U M ≅ ∏_U N for some ultrafilter U

Elementary equivalence = isomorphism of suitable ultrapowers.
```

---

## Proof Templates

```
MODEL THEORY PROOF PATTERNS
═══════════════════════════════════════════════════════════════

COMPACTNESS ARGUMENTS
─────────────────────────────────────────
To show property P is consistent with T:
  1. Add constants c₁, c₂, ... for witnesses
  2. Add sentences expressing P using constants
  3. Show every finite subset has a model
  4. Apply compactness

ELEMENTARY CHAIN ARGUMENTS
─────────────────────────────────────────
Elementary chain: M₀ ≺ M₁ ≺ M₂ ≺ ...
Union: ∪ᵢ Mᵢ is elementary extension of each Mᵢ

Use to: Build models with desired properties iteratively

BACK-AND-FORTH
─────────────────────────────────────────
To show M ≅ N (for countable ω-saturated structures):
  Build isomorphism f in ω steps
  At each step: extend domain then extend range
  Saturation ensures extensions exist

TYPE-COUNTING
─────────────────────────────────────────
To show T is unstable:
  Find A and 2^|A| many types over A
  (e.g., cuts in DLO)

FORKING CALCULATIONS
─────────────────────────────────────────
To show a ⫝_A b:
  Show tp(a/Ab) doesn't fork over A
  Typically: find non-forking extension, apply uniqueness
```

---

## Integration with Agents

### Recommended Agent Combinations

- **model-theorist**: Primary model-theoretic reasoning
- **set-theorist**: Ultrafilters, cardinality arguments
- **algebraic-logician**: Algebraic semantics connections
- **proof-constructor**: Formal proofs
- **general-logician**: Syntactic foundations

---

## References

- Marker, D. (2002). Model Theory: An Introduction
- Hodges, W. (1993). Model Theory
- Chang, C.C. & Keisler, H.J. (1990). Model Theory (3rd ed.)
- Tent, K. & Ziegler, M. (2012). A Course in Model Theory
- Pillay, A. (1996). Geometric Stability Theory

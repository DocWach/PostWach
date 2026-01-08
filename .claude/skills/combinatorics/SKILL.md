# Combinatorics Skill

## Overview

This skill provides comprehensive methodologies for counting, enumeration, generating functions, and combinatorial structures. It covers fundamental counting principles, advanced enumeration techniques, and asymptotic analysis.

## When to Use

- Counting permutations, combinations, partitions
- Solving recurrence relations
- Using generating functions
- Proving combinatorial identities
- Asymptotic enumeration
- Bijective proof construction

---

## Counting Principles

```
FUNDAMENTAL COUNTING
═══════════════════════════════════════════════════════════════

PRODUCT RULE
─────────────────────────────────────────
Sequential choices: If task A has m ways, task B has n ways,
then A followed by B has m·n ways.

|A × B| = |A| · |B|

SUM RULE
─────────────────────────────────────────
Disjoint choices: If A and B are disjoint,
|A ∪ B| = |A| + |B|

BIJECTION PRINCIPLE
─────────────────────────────────────────
If f: A → B is bijection, then |A| = |B|.
To count A, find easier B and bijection.

DOUBLE COUNTING
─────────────────────────────────────────
Count same set two ways to establish identity.
∑_{k=0}^n k·C(n,k) = n·2^{n-1}

INCLUSION-EXCLUSION
─────────────────────────────────────────
|A₁ ∪ ... ∪ Aₙ| = ∑|Aᵢ| - ∑|Aᵢ∩Aⱼ| + ... + (-1)^{n+1}|A₁∩...∩Aₙ|

Complement form: |Ā₁ ∩ ... ∩ Āₙ| = |U| - |A₁ ∪ ... ∪ Aₙ|
```

## Basic Counting Formulas

```
PERMUTATIONS AND COMBINATIONS
═══════════════════════════════════════════════════════════════

PERMUTATIONS
─────────────────────────────────────────
P(n,k) = n!/(n-k)! = n(n-1)···(n-k+1)

Special cases:
  n! = permutations of n items
  (n-1)! = circular permutations
  n!/∏kᵢ! = permutations with repetition

COMBINATIONS
─────────────────────────────────────────
C(n,k) = n!/(k!(n-k)!)

Properties:
  C(n,k) = C(n,n-k)                (symmetry)
  C(n,k) = C(n-1,k-1) + C(n-1,k)   (Pascal)
  ∑C(n,k) = 2^n                    (row sum)
  ∑(-1)^k C(n,k) = 0               (alternating)
  ∑C(n,k)² = C(2n,n)               (Vandermonde)

MULTISET COEFFICIENT
─────────────────────────────────────────
((n,k)) = C(n+k-1,k)

k selections from n types with repetition.
Stars and bars: k balls in n bins.

MULTINOMIAL COEFFICIENT
─────────────────────────────────────────
(n; k₁,k₂,...,kᵣ) = n!/(k₁!k₂!···kᵣ!)

where k₁ + k₂ + ··· + kᵣ = n.
```

## Generating Functions

```
ORDINARY GENERATING FUNCTIONS (OGF)
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
For sequence (aₙ): A(x) = ∑_{n≥0} aₙxⁿ

BASIC OGFs
─────────────────────────────────────────
1/(1-x) = 1 + x + x² + ...           (aₙ = 1)
1/(1-x)^k = ∑C(n+k-1,k-1)xⁿ          (multiset)
(1+x)^n = ∑C(n,k)x^k                 (binomial)
e^x = ∑xⁿ/n!                         (EGF for aₙ=1)

OPERATIONS
─────────────────────────────────────────
A(x) + B(x) ↔ (aₙ + bₙ)
A(x)·B(x) ↔ (∑_{k=0}^n aₖbₙ₋ₖ)       (convolution)
xA'(x) ↔ (n·aₙ)
∫A(x)dx ↔ (aₙ₋₁/n)

COEFFICIENT EXTRACTION
─────────────────────────────────────────
[xⁿ]A(x) = aₙ = (1/n!) · d^n/dx^n A(x)|_{x=0}

Partial fractions for rational A(x).

EXPONENTIAL GENERATING FUNCTIONS (EGF)
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Â(x) = ∑_{n≥0} aₙ xⁿ/n!

PRODUCT
─────────────────────────────────────────
Â(x)·B̂(x) ↔ (∑_{k=0}^n C(n,k) aₖbₙ₋ₖ)  (binomial convolution)

For labeled structures: product = labeled product.
```

## Recurrence Relations

```
SOLVING LINEAR RECURRENCES
═══════════════════════════════════════════════════════════════

CONSTANT COEFFICIENTS
─────────────────────────────────────────
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ··· + cₖaₙ₋ₖ

1. Characteristic polynomial: x^k - c₁x^{k-1} - ··· - cₖ = 0
2. Find roots r₁,...,rₖ
3. If distinct: aₙ = A₁r₁ⁿ + A₂r₂ⁿ + ··· + Aₖrₖⁿ
4. If repeated root r (mult m): contributes (A + Bn + ··· + Cn^{m-1})rⁿ
5. Solve for constants using initial conditions

GENERATING FUNCTION METHOD
─────────────────────────────────────────
1. Multiply recurrence by xⁿ, sum over n
2. Express in terms of A(x)
3. Solve for A(x)
4. Extract coefficients via partial fractions

EXAMPLE: FIBONACCI
─────────────────────────────────────────
Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀=0, F₁=1

Characteristic: x² - x - 1 = 0
Roots: φ = (1+√5)/2, ψ = (1-√5)/2
Solution: Fₙ = (φⁿ - ψⁿ)/√5
```

## Important Sequences

```
CATALAN NUMBERS
═══════════════════════════════════════════════════════════════

Cₙ = C(2n,n)/(n+1) = (2n)!/((n+1)!n!)

C₀=1, C₁=1, C₂=2, C₃=5, C₄=14, C₅=42

Counts:
  □ Balanced parentheses with n pairs
  □ Binary trees with n+1 leaves
  □ Dyck paths (0,0) to (2n,0)
  □ Triangulations of (n+2)-gon

Recurrence: Cₙ₊₁ = ∑_{k=0}^n CₖCₙ₋ₖ

STIRLING NUMBERS
═══════════════════════════════════════════════════════════════

SECOND KIND S(n,k)
─────────────────────────────────────────
Ways to partition [n] into k nonempty blocks.
S(n,k) = k·S(n-1,k) + S(n-1,k-1)

FIRST KIND |s(n,k)|
─────────────────────────────────────────
Permutations of [n] with exactly k cycles.

BELL NUMBERS
═══════════════════════════════════════════════════════════════

Bₙ = ∑_{k=0}^n S(n,k) = partitions of [n]

B₀=1, B₁=1, B₂=2, B₃=5, B₄=15, B₅=52

EGF: exp(e^x - 1)

PARTITION NUMBERS
═══════════════════════════════════════════════════════════════

p(n) = integer partitions of n

OGF: ∏_{k≥1} 1/(1-x^k)

Asymptotic: p(n) ~ exp(π√(2n/3))/(4n√3)
```

---

## Integration with Agents

- **combinatorialist**: Primary enumeration
- **graph-theorist**: Graph counting
- **probabilistic-combinatorialist**: Expected counts

---

## References

- Stanley, R.P. (2011). Enumerative Combinatorics
- Wilf, H.S. (2005). generatingfunctionology
- Graham, Knuth, Patashnik (1994). Concrete Mathematics

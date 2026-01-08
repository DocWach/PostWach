# Real Analysis Skill

## Overview

This skill provides methodology for rigorous real analysis including limits, continuity, differentiation, and integration. It coordinates with the real-analyst agent for epsilon-delta proofs and convergence analysis.

## Invocation

```
/real-analysis [subcommand] [arguments]
```

## Subcommands

### `/real-analysis limit <expression>`
Analyze limits using epsilon-delta methods.

### `/real-analysis continuity <function>`
Analyze continuity properties (pointwise, uniform).

### `/real-analysis derivative <function>`
Compute and analyze derivatives, mean value theorems.

### `/real-analysis integral <function>`
Evaluate integrals, analyze convergence of improper integrals.

### `/real-analysis series <expression>`
Analyze convergence of series and sequences.

### `/real-analysis uniform <sequence>`
Analyze uniform convergence of function sequences.

---

## Methodology

### Limit Analysis Pipeline

```
EPSILON-DELTA PROOF STRUCTURE
═══════════════════════════════════════════════════════════════

GOAL: Prove lim_{x→a} f(x) = L

TEMPLATE
─────────────────────────────────────────
1. Let ε > 0 be given.

2. [Work backwards to find δ]
   Need: |f(x) - L| < ε when 0 < |x - a| < δ

3. Choose δ = [expression in terms of ε]

4. Verify: If 0 < |x - a| < δ, then
   |f(x) - L| = [simplify]
              ≤ [bound]
              < ε

COMMON STRATEGIES
─────────────────────────────────────────
□ Factor: |f(x) - L| = |x - a| · |g(x)|, bound |g(x)|
□ Add/subtract: |f(x) - L| ≤ |f(x) - M| + |M - L|
□ Restrict δ initially: Take δ ≤ 1 to bound troublesome terms
```

### Continuity Analysis Pipeline

```
CONTINUITY VERIFICATION
═══════════════════════════════════════════════════════════════

POINTWISE CONTINUITY AT a
─────────────────────────────────────────
Check:
1. f(a) is defined
2. lim_{x→a} f(x) exists
3. lim_{x→a} f(x) = f(a)

Epsilon-delta: ∀ε > 0, ∃δ > 0: |x-a| < δ ⟹ |f(x)-f(a)| < ε

UNIFORM CONTINUITY
─────────────────────────────────────────
Check: ∀ε > 0, ∃δ > 0: ∀x,y: |x-y| < δ ⟹ |f(x)-f(y)| < ε

Key difference: δ independent of position.

TEST: f continuous on [a,b] ⟹ uniformly continuous

NOT UNIFORMLY CONTINUOUS TEST
─────────────────────────────────────────
Find sequences (xₙ), (yₙ) with:
  |xₙ - yₙ| → 0 but |f(xₙ) - f(yₙ)| ↛ 0

Example: f(x) = 1/x on (0,1): Take xₙ = 1/n, yₙ = 1/(n+1)
```

### Differentiation Pipeline

```
DERIVATIVE COMPUTATION
═══════════════════════════════════════════════════════════════

LIMIT DEFINITION
─────────────────────────────────────────
f'(a) = lim_{h→0} [f(a+h) - f(a)]/h

DIFFERENTIATION RULES
─────────────────────────────────────────
□ Sum: (f + g)' = f' + g'
□ Product: (fg)' = f'g + fg'
□ Quotient: (f/g)' = (f'g - fg')/g²
□ Chain: (f∘g)' = (f'∘g) · g'
□ Inverse: (f⁻¹)'(y) = 1/f'(f⁻¹(y))

MEAN VALUE THEOREM APPLICATION
═══════════════════════════════════════════════════════════════

STRATEGY
─────────────────────────────────────────
1. Verify hypotheses:
   □ f continuous on [a,b]
   □ f differentiable on (a,b)

2. Conclude: ∃c ∈ (a,b): f'(c) = [f(b)-f(a)]/(b-a)

3. Use for:
   □ Proving inequalities
   □ Establishing bounds
   □ Showing monotonicity

TAYLOR'S THEOREM APPLICATION
─────────────────────────────────────────
f(x) = Σ_{k=0}^n [f^(k)(a)/k!](x-a)^k + R_n(x)

Error bound: |R_n(x)| ≤ M|x-a|^{n+1}/(n+1)!
where M bounds |f^{(n+1)}|.
```

### Integration Pipeline

```
RIEMANN INTEGRAL EVALUATION
═══════════════════════════════════════════════════════════════

METHOD 1: FUNDAMENTAL THEOREM
─────────────────────────────────────────
∫_a^b f(x) dx = F(b) - F(a) where F' = f

METHOD 2: DIRECT (Riemann sums)
─────────────────────────────────────────
1. Partition [a,b]: P = {x₀, x₁, ..., xₙ}
2. Compute upper/lower sums
3. Show U(f,P) - L(f,P) → 0

IMPROPER INTEGRAL CONVERGENCE
═══════════════════════════════════════════════════════════════

TYPE I (Infinite interval)
─────────────────────────────────────────
∫_a^∞ f(x) dx = lim_{b→∞} ∫_a^b f(x) dx

Convergence tests:
□ Comparison: 0 ≤ f ≤ g, ∫g converges ⟹ ∫f converges
□ Limit comparison: f/g → L ∈ (0,∞), same behavior
□ p-test: ∫_1^∞ x^{-p} dx converges ⟺ p > 1

TYPE II (Unbounded function)
─────────────────────────────────────────
If f unbounded near b:
  ∫_a^b f(x) dx = lim_{c→b⁻} ∫_a^c f(x) dx

p-test: ∫_0^1 x^{-p} dx converges ⟺ p < 1
```

### Series Analysis Pipeline

```
SERIES CONVERGENCE ANALYSIS
═══════════════════════════════════════════════════════════════

STEP 1: DIVERGENCE TEST
─────────────────────────────────────────
If aₙ ↛ 0, series diverges.
(If aₙ → 0, inconclusive)

STEP 2: RECOGNIZE SPECIAL SERIES
─────────────────────────────────────────
□ Geometric: Σar^n converges ⟺ |r| < 1, sum = a/(1-r)
□ p-series: Σ1/n^p converges ⟺ p > 1
□ Alternating: Σ(-1)^n bₙ converges if bₙ ↓ 0

STEP 3: APPLY TESTS
─────────────────────────────────────────
Ratio test: L = lim |aₙ₊₁/aₙ|
  L < 1: converges absolutely
  L > 1: diverges
  L = 1: inconclusive

Root test: L = lim |aₙ|^{1/n}, same criteria

Comparison: If 0 ≤ aₙ ≤ bₙ and Σbₙ converges, so does Σaₙ

Integral test: If f positive, decreasing, Σf(n) and ∫f have same behavior

STEP 4: ABSOLUTE VS CONDITIONAL
─────────────────────────────────────────
Σ|aₙ| converges ⟹ Σaₙ converges absolutely
Σaₙ converges but Σ|aₙ| diverges ⟹ conditional convergence

POWER SERIES
═══════════════════════════════════════════════════════════════

RADIUS OF CONVERGENCE
─────────────────────────────────────────
R = 1/lim sup |aₙ|^{1/n} or R = lim |aₙ/aₙ₊₁|

□ Converges absolutely for |x-c| < R
□ Diverges for |x-c| > R
□ Test endpoints separately
```

### Uniform Convergence Pipeline

```
UNIFORM CONVERGENCE ANALYSIS
═══════════════════════════════════════════════════════════════

DEFINITION CHECK
─────────────────────────────────────────
fₙ → f uniformly on S:
  sup_{x∈S} |fₙ(x) - f(x)| → 0

Equivalently: ∀ε > 0, ∃N: ∀n > N, ∀x ∈ S: |fₙ(x) - f(x)| < ε

VERIFICATION METHODS
─────────────────────────────────────────
1. Direct: Compute sup |fₙ - f|, show → 0

2. Weierstrass M-test (for series):
   If |fₙ(x)| ≤ Mₙ and ΣMₙ converges,
   then Σfₙ converges uniformly and absolutely

DISPROVING UNIFORM CONVERGENCE
─────────────────────────────────────────
Find sequence xₙ (depending on n) with |fₙ(xₙ) - f(xₙ)| ↛ 0

Example: fₙ(x) = xⁿ on [0,1)
  f(x) = 0, but fₙ(1-1/n) = (1-1/n)ⁿ → 1/e ≠ 0

CONSEQUENCES
─────────────────────────────────────────
If fₙ → f uniformly on [a,b]:
□ fₙ continuous ⟹ f continuous
□ ∫fₙ → ∫f
□ (With extra condition) fₙ' → f' uniformly ⟹ (lim fₙ)' = lim fₙ'
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Notes |
|--------------|---------------|-------|
| Limits, continuity | real-analyst | Epsilon-delta |
| Derivatives | real-analyst | Mean value theorems |
| Riemann integrals | real-analyst | FTC |
| Measure theory | measure-theorist | Lebesgue |
| Function spaces | functional-analyst | L^p |

---

## Output Format

### Epsilon-Delta Proof
```
LIMIT PROOF
═══════════════════════════════════════════════════════════════

CLAIM: lim_{x→a} f(x) = L

PROOF
─────────────────────────────────────────
Let ε > 0 be given.

Choose δ = [value].

Suppose 0 < |x - a| < δ. Then:
  |f(x) - L| = [computation]
             ≤ [bound]
             < ε

Therefore lim_{x→a} f(x) = L.  □
```

### Convergence Analysis
```
SERIES ANALYSIS: Σaₙ
═══════════════════════════════════════════════════════════════

DIVERGENCE TEST
─────────────────────────────────────────
lim aₙ = [value] [→ or ↛ 0]

CONVERGENCE TEST
─────────────────────────────────────────
Test used: [name]
Computation: [details]
Result: [converges/diverges]

CONCLUSION
─────────────────────────────────────────
[Absolute/conditional convergence or divergence]
```

---

## Examples

### Example: Prove lim_{x→2} x² = 4

```
/real-analysis limit "x^2 as x→2"

LIMIT PROOF
═══════════════════════════════════════════════════════════════

CLAIM: lim_{x→2} x² = 4

SCRATCH WORK
─────────────────────────────────────────
Need |x² - 4| < ε when |x - 2| < δ.
|x² - 4| = |x - 2||x + 2|

If |x - 2| < 1, then |x| < 3, so |x + 2| < 5.
Thus |x² - 4| < 5|x - 2|.

Choose δ = min(1, ε/5).

PROOF
─────────────────────────────────────────
Let ε > 0. Choose δ = min(1, ε/5).

Suppose 0 < |x - 2| < δ.

Since δ ≤ 1: |x - 2| < 1 ⟹ |x + 2| < 5

Thus: |x² - 4| = |x - 2||x + 2|
              < δ · 5
              ≤ (ε/5) · 5
              = ε

Therefore lim_{x→2} x² = 4.  □
```

---

## References

- Rudin, W. - Principles of Mathematical Analysis
- Abbott, S. - Understanding Analysis
- Apostol, T. - Mathematical Analysis

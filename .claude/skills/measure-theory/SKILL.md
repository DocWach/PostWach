# Measure Theory Skill

## Overview

This skill provides methodology for measure-theoretic analysis including sigma-algebras, measures, Lebesgue integration, and convergence theorems. It coordinates with the measure-theorist agent for rigorous integration theory.

## Invocation

```
/measure-theory [subcommand] [arguments]
```

## Subcommands

### `/measure-theory measure <set>`
Compute or analyze Lebesgue measure of sets.

### `/measure-theory integral <function>`
Evaluate Lebesgue integrals.

### `/measure-theory convergence <sequence>`
Analyze convergence using MCT, DCT, Fatou.

### `/measure-theory lp <function>`
Analyze L^p properties and norms.

### `/measure-theory product <integral>`
Apply Fubini/Tonelli theorems.

### `/measure-theory radon-nikodym <measures>`
Compute Radon-Nikodym derivatives.

---

## Methodology

### Measurability Pipeline

```
CHECKING MEASURABILITY
═══════════════════════════════════════════════════════════════

FOR SETS
─────────────────────────────────────────
Check if A is Lebesgue measurable:

1. Is A a Borel set?
   □ Open, closed, Fσ, Gδ → Yes
   □ Countable unions/intersections of Borel → Yes

2. Is A a null set (m*(A) = 0)?
   □ Countable sets → Yes
   □ Cantor set → Yes (measure zero)

3. Can A be written as Borel ± null set?
   □ Yes → measurable

FOR FUNCTIONS
─────────────────────────────────────────
f: X → ℝ is measurable if f⁻¹((a,∞)) ∈ Σ for all a.

Sufficient conditions:
□ f continuous (Borel measurable)
□ f = lim fₙ where fₙ measurable
□ f = sup fₙ, inf fₙ, lim sup fₙ, lim inf fₙ
□ f = g + h, f = gh, f/g where g,h measurable
```

### Lebesgue Integration Pipeline

```
COMPUTING LEBESGUE INTEGRALS
═══════════════════════════════════════════════════════════════

STEP 1: CHECK INTEGRABILITY
─────────────────────────────────────────
f integrable ⟺ ∫|f| dm < ∞

For non-negative: Always well-defined (may be ∞)

STEP 2: COMPUTE INTEGRAL
─────────────────────────────────────────
Method A: Riemann integral
  If f Riemann integrable on [a,b], use FTC.
  Riemann = Lebesgue for such functions.

Method B: Simple function approximation
  f = lim sₙ where sₙ simple, sₙ ↑ f
  ∫f = lim ∫sₙ (by MCT)

Method C: Convergence theorems
  Use MCT, DCT, Fatou as appropriate.

Method D: Fubini
  ∫∫f d(m×m) = ∫(∫f(x,y)dy)dx

STEP 3: VERIFY
─────────────────────────────────────────
□ Check hypotheses of theorem used
□ Confirm convergence if limits involved
```

### Convergence Theorem Pipeline

```
APPLYING CONVERGENCE THEOREMS
═══════════════════════════════════════════════════════════════

DECISION TREE
─────────────────────────────────────────
Is fₙ → f pointwise?
  │
  ├─ Are fₙ ≥ 0 and increasing?
  │   └─ YES → Use MCT: ∫f = lim ∫fₙ
  │
  ├─ Is there g with |fₙ| ≤ g and ∫g < ∞?
  │   └─ YES → Use DCT: ∫f = lim ∫fₙ
  │
  └─ Only have fₙ ≥ 0?
      └─ Use Fatou: ∫lim inf fₙ ≤ lim inf ∫fₙ

MONOTONE CONVERGENCE THEOREM
─────────────────────────────────────────
Hypotheses:
  □ fₙ measurable
  □ 0 ≤ f₁ ≤ f₂ ≤ ... (increasing)
  □ fₙ → f pointwise

Conclusion: ∫f = lim ∫fₙ (including both = ∞)

DOMINATED CONVERGENCE THEOREM
─────────────────────────────────────────
Hypotheses:
  □ fₙ measurable
  □ fₙ → f pointwise
  □ |fₙ| ≤ g for some integrable g

Conclusions:
  □ f is integrable
  □ ∫f = lim ∫fₙ
  □ ∫|fₙ - f| → 0

FATOU'S LEMMA
─────────────────────────────────────────
Hypotheses:
  □ fₙ ≥ 0 measurable

Conclusion: ∫lim inf fₙ ≤ lim inf ∫fₙ

(Inequality can be strict!)
```

### L^p Analysis Pipeline

```
L^P SPACE ANALYSIS
═══════════════════════════════════════════════════════════════

NORM COMPUTATION
─────────────────────────────────────────
‖f‖_p = (∫|f|^p dm)^{1/p} for 1 ≤ p < ∞
‖f‖_∞ = ess sup |f|

MEMBERSHIP CHECK
─────────────────────────────────────────
f ∈ L^p ⟺ ‖f‖_p < ∞

RELATIONS BETWEEN L^P SPACES
─────────────────────────────────────────
For finite measure space (m(X) < ∞):
  p < q ⟹ L^q ⊆ L^p
  ‖f‖_p ≤ m(X)^{1/p - 1/q} ‖f‖_q

For ℝⁿ with Lebesgue measure:
  No general inclusion

HÖLDER'S INEQUALITY
─────────────────────────────────────────
1/p + 1/q = 1:
  ‖fg‖_1 ≤ ‖f‖_p ‖g‖_q

MINKOWSKI'S INEQUALITY
─────────────────────────────────────────
‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p

CONVERGENCE IN L^P
─────────────────────────────────────────
fₙ → f in L^p ⟺ ‖fₙ - f‖_p → 0

Dominated convergence in L^p:
  fₙ → f a.e., |fₙ| ≤ g ∈ L^p ⟹ fₙ → f in L^p
```

### Product Measure Pipeline

```
FUBINI/TONELLI APPLICATION
═══════════════════════════════════════════════════════════════

STEP 1: IDENTIFY INTEGRAL TYPE
─────────────────────────────────────────
∫∫ f(x,y) dμ(x) dν(y)

STEP 2: CHECK HYPOTHESES
─────────────────────────────────────────
For Tonelli (f ≥ 0):
  □ f measurable on product σ-algebra
  □ μ, ν are σ-finite

For Fubini (general f):
  □ f measurable on product σ-algebra
  □ μ, ν are σ-finite
  □ ∫|f| d(μ×ν) < ∞

STEP 3: APPLY THEOREM
─────────────────────────────────────────
∫∫ f d(μ×ν) = ∫_X (∫_Y f(x,y) dν(y)) dμ(x)
            = ∫_Y (∫_X f(x,y) dμ(x)) dν(y)

STEP 4: COMPUTE ITERATED INTEGRAL
─────────────────────────────────────────
Choose order that simplifies computation.
Inner integral first, then outer.

COMMON STRATEGY
─────────────────────────────────────────
1. Use Tonelli on |f| to verify integrability
2. Apply Fubini to compute ∫f
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Notes |
|--------------|---------------|-------|
| Measure computation | measure-theorist | Outer measure |
| Lebesgue integral | measure-theorist | Convergence thms |
| Riemann vs Lebesgue | real-analyst | Comparison |
| L^p analysis | measure-theorist + functional-analyst | Norms |
| Probability | measure-theorist | Foundation |

---

## Output Format

### Integral Computation
```
LEBESGUE INTEGRAL
═══════════════════════════════════════════════════════════════

FUNCTION: f(x) = [expression]
DOMAIN: [set]

INTEGRABILITY CHECK
─────────────────────────────────────────
[Verify ∫|f| < ∞ or explain why f ≥ 0]

METHOD
─────────────────────────────────────────
[Theorem/technique used]

COMPUTATION
─────────────────────────────────────────
[Step-by-step calculation]

RESULT
─────────────────────────────────────────
∫ f dm = [value]
```

### Convergence Theorem Application
```
CONVERGENCE ANALYSIS
═══════════════════════════════════════════════════════════════

SEQUENCE: fₙ(x) = [expression]
LIMIT: f(x) = [expression]

THEOREM: [MCT/DCT/Fatou]

HYPOTHESIS VERIFICATION
─────────────────────────────────────────
□ [Hypothesis 1]: [verification]
□ [Hypothesis 2]: [verification]
...

CONCLUSION
─────────────────────────────────────────
[Result]
```

---

## Examples

### Example: Interchange limit and integral

```
/measure-theory convergence "f_n(x) = n*x*e^(-nx^2) on [0,∞)"

CONVERGENCE ANALYSIS
═══════════════════════════════════════════════════════════════

SEQUENCE: fₙ(x) = nx·e^{-nx²} on [0,∞)

POINTWISE LIMIT
─────────────────────────────────────────
For x = 0: fₙ(0) = 0 → 0
For x > 0: fₙ(x) = nx·e^{-nx²} → 0 (exponential dominates)

So f(x) = 0.

CAN WE USE DCT?
─────────────────────────────────────────
Need dominating function g with |fₙ| ≤ g, ∫g < ∞.

fₙ(x) = nx·e^{-nx²}

Maximum of fₙ: Set derivative = 0
d/dx[nx·e^{-nx²}] = n·e^{-nx²}(1 - 2nx²) = 0
Maximum at x = 1/√(2n), value = √(n/(2e))

This maximum → ∞, so no uniform bound.

DCT DOES NOT APPLY DIRECTLY.

DIRECT COMPUTATION
─────────────────────────────────────────
∫_0^∞ nx·e^{-nx²} dx = [-e^{-nx²}/2]_0^∞ = 1/2

So ∫fₙ = 1/2 for all n, but ∫f = 0.

CONCLUSION
─────────────────────────────────────────
lim ∫fₙ = 1/2 ≠ 0 = ∫lim fₙ

Cannot interchange limit and integral here.
(No integrable dominator exists)
```

---

## References

- Royden & Fitzpatrick - Real Analysis
- Folland - Real Analysis
- Rudin - Real and Complex Analysis
- Cohn - Measure Theory

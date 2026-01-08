# Probability & Statistics Skill

## Overview

This skill provides methodology for probability theory and statistics, including distributions, limit theorems, stochastic processes, and statistical inference. It coordinates with the probabilist agent.

## Invocation

```
/probability-statistics [subcommand] [arguments]
```

## Subcommands

### `/probability-statistics distribution <specification>`
Analyze probability distributions.

### `/probability-statistics expectation <expression>`
Compute expectations and moments.

### `/probability-statistics limit-theorem <sequence>`
Apply LLN, CLT, or other limit theorems.

### `/probability-statistics markov <chain>`
Analyze Markov chains.

### `/probability-statistics inference <data> <model>`
Perform statistical inference (frequentist or Bayesian).

### `/probability-statistics test <hypothesis> <data>`
Conduct hypothesis test.

---

## Methodology

### Distribution Analysis

```
DISTRIBUTION ANALYSIS
═══════════════════════════════════════════════════════════════

STEP 1: IDENTIFY DISTRIBUTION
─────────────────────────────────────────
From description or PDF/PMF.

STEP 2: COMPUTE PARAMETERS
─────────────────────────────────────────
Mean: E[X] = ∫ x f(x) dx
Variance: Var(X) = E[X²] - (E[X])²

STEP 3: FIND RELEVANT PROBABILITIES
─────────────────────────────────────────
P(a < X < b) = ∫ₐᵇ f(x) dx = F(b) - F(a)

COMMON DISTRIBUTIONS
─────────────────────────────────────────
Binomial(n,p): E = np, Var = np(1-p)
Poisson(λ): E = Var = λ
Normal(μ,σ²): E = μ, Var = σ²
Exponential(λ): E = 1/λ, Var = 1/λ²
```

### Limit Theorems

```
LIMIT THEOREM APPLICATION
═══════════════════════════════════════════════════════════════

LAW OF LARGE NUMBERS
─────────────────────────────────────────
X₁,...,Xₙ iid with E[Xᵢ] = μ
S̄ₙ → μ as n → ∞ (a.s. or in probability)

CENTRAL LIMIT THEOREM
─────────────────────────────────────────
√n(S̄ₙ - μ)/σ →ᵈ N(0,1)

Application: P(a < S̄ₙ < b) ≈ Φ((b-μ)√n/σ) - Φ((a-μ)√n/σ)
```

### Statistical Inference

```
INFERENCE PIPELINE
═══════════════════════════════════════════════════════════════

POINT ESTIMATION
─────────────────────────────────────────
MLE: θ̂ = argmax Π f(xᵢ; θ)
Method of moments: Match sample to population moments

CONFIDENCE INTERVALS
─────────────────────────────────────────
Normal mean (σ known): X̄ ± z_{α/2} σ/√n
Normal mean (σ unknown): X̄ ± t_{α/2,n-1} s/√n

HYPOTHESIS TESTING
─────────────────────────────────────────
1. State H₀, H₁
2. Choose test statistic T
3. Compute p-value = P(T ≥ t_obs | H₀)
4. Reject H₀ if p < α

BAYESIAN INFERENCE
─────────────────────────────────────────
Posterior ∝ Likelihood × Prior
P(θ|X) ∝ P(X|θ) P(θ)
```

---

## Output Format

### Statistical Analysis
```
STATISTICAL ANALYSIS
═══════════════════════════════════════════════════════════════

DATA SUMMARY
─────────────────────────────────────────
n = [sample size]
x̄ = [sample mean]
s = [sample std dev]

MODEL
─────────────────────────────────────────
[Distribution/model assumption]

INFERENCE
─────────────────────────────────────────
[Point estimate, CI, or test result]

CONCLUSION
─────────────────────────────────────────
[Interpretation in context]
```

---

## Examples

### Example: Normal confidence interval

```
/probability-statistics inference "n=25, x̄=50, s=10, 95% CI for μ"

CONFIDENCE INTERVAL
═══════════════════════════════════════════════════════════════

DATA
─────────────────────────────────────────
n = 25, x̄ = 50, s = 10

ASSUMPTION: X ~ Normal(μ, σ²), σ unknown

METHOD: t-interval

COMPUTATION
─────────────────────────────────────────
df = n - 1 = 24
t_{0.025, 24} = 2.064

CI = x̄ ± t s/√n
   = 50 ± 2.064 × 10/5
   = 50 ± 4.13
   = (45.87, 54.13)

CONCLUSION
─────────────────────────────────────────
95% confidence interval for μ: (45.87, 54.13)
```

---

## References

- Durrett (2019). Probability: Theory and Examples
- Casella & Berger (2002). Statistical Inference
- Gelman et al. (2013). Bayesian Data Analysis

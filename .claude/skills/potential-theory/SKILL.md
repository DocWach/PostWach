# Potential Theory Skill

## Overview

This skill provides methodology for potential theory, including harmonic functions, capacity, and the Dirichlet problem. It coordinates with the potential-theorist agent.

## Invocation

```
/potential-theory [subcommand] [arguments]
```

## Subcommands

### `/potential-theory harmonic <domain>`
Analyze harmonic functions on a domain.

### `/potential-theory dirichlet <domain> <boundary-data>`
Solve the Dirichlet problem.

### `/potential-theory capacity <set>`
Compute capacity.

### `/potential-theory green <domain>`
Compute Green function.

### `/potential-theory subharmonic <function>`
Analyze subharmonic functions.

### `/potential-theory equilibrium <set>`
Compute equilibrium measure.

---

## Methodology

### Dirichlet Problem

```
DIRICHLET PROBLEM
═══════════════════════════════════════════════════════════════

PROBLEM: Find harmonic u with u|_∂Ω = f

STEP 1: REGULARITY CHECK
─────────────────────────────────────────
Apply Wiener criterion to boundary points
Smooth boundary ⟹ all points regular

STEP 2: SOLUTION METHOD
─────────────────────────────────────────
- Perron method (general domains)
- Poisson integral (ball, half-space)
- Green function representation

STEP 3: VERIFY
─────────────────────────────────────────
Check Δu = 0 and boundary conditions
```

### Capacity Computation

```
CAPACITY COMPUTATION
═══════════════════════════════════════════════════════════════

NEWTONIAN (n ≥ 3)
─────────────────────────────────────────
cap(K) = 1/inf{I(μ)} over probabilities on K
I(μ) = ∫∫ |x-y|^{2-n} dμ(x)dμ(y)

LOGARITHMIC (n = 2)
─────────────────────────────────────────
cap(K) = e^{-V(K)}
V(K) = inf ∫∫ log|z-w|^{-1} dμ(z)dμ(w)

POLAR SETS
─────────────────────────────────────────
cap(E) = 0 ⟺ E is polar
Polar sets are "negligible" for potential theory
```

---

## Output Format

### Potential Theory Report
```
POTENTIAL THEORY ANALYSIS
═══════════════════════════════════════════════════════════════

DOMAIN/SET
─────────────────────────────────────────
[Specification]

CAPACITY
─────────────────────────────────────────
[Value or estimate]

GREEN FUNCTION
─────────────────────────────────────────
[Formula if available]

DIRICHLET PROBLEM
─────────────────────────────────────────
[Solution method, regularity]
```

---

## Examples

### Example: Capacity of Ball

```
/potential-theory capacity "Ball B_r in ℝⁿ"

CAPACITY COMPUTATION: Ball B_r
═══════════════════════════════════════════════════════════════

SET
─────────────────────────────────────────
K = B_r(0) ⊂ ℝⁿ (closed ball of radius r)

NEWTONIAN CAPACITY (n ≥ 3)
─────────────────────────────────────────
cap(B_r) = r^{n-2}

Equilibrium measure: uniform on ∂B_r
μ = (1/|∂B_r|) · σ_{∂B_r}

LOGARITHMIC CAPACITY (n = 2)
─────────────────────────────────────────
cap(D_r) = r (disk of radius r)

Robin constant: V = -log r

VERIFICATION
─────────────────────────────────────────
The potential U^μ = ∫ |x-y|^{2-n} dμ(y)
equals r^{2-n} on K and decays outside.
```

### Example: Dirichlet on Half-Space

```
/potential-theory dirichlet "half-space" "f(x')"

DIRICHLET PROBLEM: Half-Space
═══════════════════════════════════════════════════════════════

DOMAIN
─────────────────────────────────────────
Ω = {x ∈ ℝⁿ : xₙ > 0} (upper half-space)

POISSON KERNEL
─────────────────────────────────────────
P(x, y') = (2xₙ)/(nωₙ) · 1/|(x', xₙ) - (y', 0)|ⁿ

for x = (x', xₙ) ∈ Ω, y' ∈ ℝⁿ⁻¹

SOLUTION
─────────────────────────────────────────
u(x', xₙ) = ∫_{ℝⁿ⁻¹} f(y') P((x', xₙ), y') dy'

PROPERTIES
─────────────────────────────────────────
- All boundary points regular
- Solution bounded if f bounded
- u → f as xₙ → 0 (in various senses)
```

---

## References

- Armitage, D.H. & Gardiner, S.J. (2001). Classical Potential Theory
- Helms, L.L. (2014). Potential Theory
- Ransford, T. (1995). Potential Theory in the Complex Plane

# PDE Methods Skill

## Overview

This skill provides methodology for partial differential equations, including classification, solution techniques, weak formulations, and well-posedness analysis. It coordinates with the pde-specialist agent.

## Invocation

```
/pde-methods [subcommand] [arguments]
```

## Subcommands

### `/pde-methods classify <equation>`
Classify PDE as elliptic, parabolic, or hyperbolic.

### `/pde-methods solve <equation> <conditions>`
Solve PDE using appropriate methods.

### `/pde-methods weak-form <equation>`
Derive weak formulation for variational methods.

### `/pde-methods separation <equation> <domain>`
Apply separation of variables.

### `/pde-methods characteristics <equation>`
Apply method of characteristics.

### `/pde-methods maximum-principle <equation>`
Apply maximum principle for bounds/uniqueness.

---

## Methodology

### PDE Classification Pipeline

```
PDE CLASSIFICATION
═══════════════════════════════════════════════════════════════

SECOND-ORDER LINEAR: Σ aᵢⱼ ∂²u/∂xᵢ∂xⱼ + lower = 0

STEP 1: FORM COEFFICIENT MATRIX
─────────────────────────────────────────
[aᵢⱼ] symmetric matrix of leading coefficients

STEP 2: FIND EIGENVALUES
─────────────────────────────────────────
All same sign → Elliptic
One zero → Parabolic
Mixed signs → Hyperbolic

TWO VARIABLES: au_xx + 2bu_xy + cu_yy
─────────────────────────────────────────
D = b² - ac
  D < 0: Elliptic
  D = 0: Parabolic
  D > 0: Hyperbolic
```

### Separation of Variables

```
SEPARATION OF VARIABLES
═══════════════════════════════════════════════════════════════

STEP 1: ASSUME PRODUCT FORM
─────────────────────────────────────────
u(x,t) = X(x)T(t) (or similar)

STEP 2: SUBSTITUTE AND SEPARATE
─────────────────────────────────────────
Each side depends on different variable → constant

STEP 3: SOLVE EIGENVALUE PROBLEM
─────────────────────────────────────────
Boundary conditions → eigenvalues λₙ, eigenfunctions Xₙ

STEP 4: SUPERPOSE
─────────────────────────────────────────
u = Σ cₙ Xₙ(x) Tₙ(t)
Determine cₙ from initial conditions (Fourier).
```

### Weak Formulation

```
WEAK FORMULATION
═══════════════════════════════════════════════════════════════

STEP 1: MULTIPLY BY TEST FUNCTION
─────────────────────────────────────────
∫ (Lu - f)v dx = 0 for all v in test space

STEP 2: INTEGRATE BY PARTS
─────────────────────────────────────────
Move derivatives to test function.
Incorporate boundary conditions.

STEP 3: STATE WEAK PROBLEM
─────────────────────────────────────────
Find u ∈ V: a(u,v) = F(v) for all v ∈ V

STEP 4: VERIFY LAX-MILGRAM
─────────────────────────────────────────
a(·,·) bounded and coercive → unique solution.
```

---

## Output Format

### PDE Solution
```
PDE SOLUTION
═══════════════════════════════════════════════════════════════

EQUATION
─────────────────────────────────────────
[PDE with boundary/initial conditions]

CLASSIFICATION
─────────────────────────────────────────
[Elliptic/Parabolic/Hyperbolic]

METHOD
─────────────────────────────────────────
[Separation/Characteristics/Transform/etc.]

SOLUTION
─────────────────────────────────────────
u(x,t) = [expression]

VERIFICATION
─────────────────────────────────────────
[Check PDE and conditions satisfied]
```

---

## Examples

### Example: Heat equation on [0,L]

```
/pde-methods solve "u_t = k u_xx, u(0,t)=u(L,t)=0, u(x,0)=f(x)"

HEAT EQUATION SOLUTION
═══════════════════════════════════════════════════════════════

EQUATION
─────────────────────────────────────────
uₜ = k uₓₓ, x ∈ (0,L), t > 0
u(0,t) = u(L,t) = 0
u(x,0) = f(x)

CLASSIFICATION: Parabolic

METHOD: Separation of Variables

STEP 1: u = X(x)T(t)
─────────────────────────────────────────
T'/T = k X''/X = -λ

STEP 2: Eigenvalue problem
─────────────────────────────────────────
X'' + λX = 0, X(0) = X(L) = 0
λₙ = (nπ/L)², Xₙ = sin(nπx/L)

STEP 3: Time equation
─────────────────────────────────────────
T' = -kλₙT → Tₙ = e^{-k(nπ/L)²t}

SOLUTION
─────────────────────────────────────────
u(x,t) = Σ bₙ sin(nπx/L) e^{-k(nπ/L)²t}

bₙ = (2/L) ∫₀ᴸ f(x) sin(nπx/L) dx
```

---

## References

- Evans, L.C. (2010). Partial Differential Equations
- John, F. (1982). Partial Differential Equations
- Strauss, W.A. (2008). Partial Differential Equations: An Introduction

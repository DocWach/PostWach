# Mathematical Modeling Skill

## Overview

This skill provides methodologies for constructing, analyzing, and validating mathematical models of real-world phenomena. It covers the complete modeling cycle from problem formulation through model validation, with techniques for abstraction, idealization, and model refinement.

## When to Use

- Translating real-world problems into mathematics
- Building predictive or explanatory models
- Analyzing complex systems mathematically
- Simplifying problems through appropriate abstractions
- Validating and refining existing models
- Communicating mathematical insights to stakeholders

---

## The Modeling Cycle

```
MATHEMATICAL MODELING PROCESS
═══════════════════════════════════════════════════════════════

                    ┌─────────────────────┐
                    │   REAL WORLD        │
                    │   PROBLEM           │
                    └──────────┬──────────┘
                               │
                               ▼ (1) Formulation
                    ┌─────────────────────┐
                    │   MATHEMATICAL      │
                    │   MODEL             │
                    └──────────┬──────────┘
                               │
                               ▼ (2) Analysis
                    ┌─────────────────────┐
                    │   MATHEMATICAL      │
                    │   CONCLUSIONS       │
                    └──────────┬──────────┘
                               │
                               ▼ (3) Interpretation
                    ┌─────────────────────┐
                    │   REAL WORLD        │
                    │   PREDICTIONS       │
                    └──────────┬──────────┘
                               │
                               ▼ (4) Validation
                    ┌─────────────────────┐
                    │   COMPARISON        │◄───┐
                    │   WITH DATA         │    │
                    └──────────┬──────────┘    │
                               │               │
              ┌────────────────┼───────────────┤
              │                │               │
              ▼                ▼               │
        ┌──────────┐    ┌──────────┐          │
        │ ACCEPT   │    │ REFINE   │──────────┘
        │ MODEL    │    │ MODEL    │
        └──────────┘    └──────────┘
```

---

## Phase 1: Problem Formulation

### Problem Understanding

```
PROBLEM ANALYSIS FRAMEWORK
═══════════════════════════════════════════════════════════════

STEP 1: IDENTIFY THE QUESTION
─────────────────────────────────────────
What exactly do we want to know?

Question types:
□ Prediction: What will happen?
□ Optimization: What's the best choice?
□ Explanation: Why does this occur?
□ Estimation: How much/many?
□ Classification: What type is this?
□ Control: How can we achieve X?

Question clarification checklist:
□ What is the output we seek?
□ What level of precision is needed?
□ What time scale is relevant?
□ What spatial scale is relevant?
□ Who will use the answer?

STEP 2: IDENTIFY KEY QUANTITIES
─────────────────────────────────────────
List all relevant variables:

Dependent variables (outputs):
  □ What do we want to predict/explain?
  □ What are we trying to optimize?

Independent variables (inputs):
  □ What can we control?
  □ What do we observe?

Parameters:
  □ What constants govern the system?
  □ What can we measure about the environment?

State variables:
  □ What describes the system's condition?
  □ How does the system evolve?

STEP 3: IDENTIFY RELATIONSHIPS
─────────────────────────────────────────
How do quantities relate?

□ Cause-effect relationships
□ Conservation laws
□ Proportionalities
□ Constraints
□ Rates of change
□ Equilibrium conditions

Document relationships:
┌─────────────────────────────────────────────────────────────┐
│ VARIABLE RELATIONSHIP TABLE                                 │
│                                                             │
│ Variable │ Type │ Units │ Related to │ How               │
│──────────┼──────┼───────┼────────────┼───────────────────│
│ x        │ ind  │ m     │ t          │ position vs time  │
│ v        │ dep  │ m/s   │ x, t       │ dx/dt             │
│ m        │ param│ kg    │ F, a       │ F = ma            │
└─────────────────────────────────────────────────────────────┘
```

### Abstraction and Idealization

```
ABSTRACTION STRATEGIES
═══════════════════════════════════════════════════════════════

WHAT TO INCLUDE vs EXCLUDE
─────────────────────────────────────────

Include if:
  ✓ Significantly affects outcome
  ✓ Is part of the main question
  ✓ Data is available
  ✓ Mathematical treatment is feasible

Exclude if:
  ✗ Effect is negligible (quantify!)
  ✗ Unrelated to main question
  ✗ Would make model intractable
  ✗ Adds complexity without insight

COMMON IDEALIZATIONS
─────────────────────────────────────────

Physical systems:
  □ Point masses (ignore size/shape)
  □ Rigid bodies (ignore deformation)
  □ Frictionless surfaces
  □ Perfect elasticity
  □ No air resistance
  □ Constant coefficients
  □ Small angle approximation (sin θ ≈ θ)

Biological systems:
  □ Well-mixed populations
  □ Constant environment
  □ No spatial variation
  □ Continuous populations (not discrete)
  □ No age structure
  □ Deterministic (no randomness)

Economic systems:
  □ Rational agents
  □ Perfect information
  □ No transaction costs
  □ Continuous quantities
  □ Equilibrium conditions

IDEALIZATION DOCUMENTATION
─────────────────────────────────────────
For each idealization:

┌─────────────────────────────────────────────────────────────┐
│ IDEALIZATION: [name]                                        │
│                                                             │
│ Reality: [what actually happens]                           │
│ Idealization: [what we assume instead]                     │
│ Justification: [why this is reasonable]                    │
│ When it fails: [conditions where idealization breaks]      │
│ Effect of failure: [what goes wrong]                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 2: Model Construction

### Model Types

```
MATHEMATICAL MODEL TAXONOMY
═══════════════════════════════════════════════════════════════

BY MATHEMATICAL STRUCTURE
─────────────────────────────────────────

Algebraic models:
  • Equations relating variables
  • Example: PV = nRT (ideal gas)
  • Use when: equilibrium, static relationships

Differential equation models:
  • ODEs: change over single variable (usually time)
  • PDEs: change over multiple variables (space, time)
  • Example: dP/dt = rP(1 - P/K) (logistic growth)
  • Use when: dynamics, rates of change

Difference equation models:
  • Discrete time steps
  • Example: xₙ₊₁ = rxₙ(1 - xₙ)
  • Use when: discrete generations, measurements

Integral equation models:
  • Accumulated effects, convolution
  • Example: delay equations, age-structured models
  • Use when: history dependence

Optimization models:
  • Objective function + constraints
  • Example: minimize cost subject to requirements
  • Use when: decision-making, design

Probabilistic/Stochastic models:
  • Random variables, distributions
  • Example: Markov chains, stochastic differential equations
  • Use when: inherent randomness, uncertainty

BY DETERMINISM
─────────────────────────────────────────

Deterministic:
  Same initial conditions → same outcome
  Appropriate when: large populations, controlled systems

Stochastic:
  Random elements, probability distributions
  Appropriate when: small populations, uncertain parameters

BY LINEARITY
─────────────────────────────────────────

Linear:
  Superposition principle holds
  f(ax + by) = af(x) + bf(y)
  Advantages: exact solutions, well-developed theory

Nonlinear:
  Superposition fails
  Advantages: more realistic, richer behavior
  Challenges: harder to solve, sensitive to conditions
```

### Building Specific Model Types

```
DIFFERENTIAL EQUATION MODELS
═══════════════════════════════════════════════════════════════

CONSTRUCTION PRINCIPLES
─────────────────────────────────────────

Conservation laws:
  Rate of change = Rate in - Rate out

  d[quantity]/dt = inflow - outflow

  Examples:
    Mass: dm/dt = ṁ_in - ṁ_out
    Energy: dE/dt = power in - power out
    Population: dN/dt = births - deaths

Constitutive relations:
  Relate flux to driving force

  Examples:
    Fourier: heat flux ∝ temperature gradient
    Fick: mass flux ∝ concentration gradient
    Ohm: current ∝ voltage

Force balance:
  ma = ΣF (Newton's second law)

  d²x/dt² = (1/m) Σ forces(x, dx/dt, t)

COMMON ODE FORMS
─────────────────────────────────────────

First-order linear:
  dy/dt + p(t)y = q(t)
  Solution: integrating factor method

Separable:
  dy/dt = f(t)g(y)
  Solution: ∫dy/g(y) = ∫f(t)dt

Autonomous:
  dy/dt = f(y)  [no explicit t dependence]
  Analysis: fixed points, stability

Systems:
  dx/dt = f(x, y)
  dy/dt = g(x, y)
  Analysis: phase plane, equilibria, Jacobian

EXAMPLE: Population Model
─────────────────────────────────────────

Problem: Model population growth with limited resources.

Variables:
  P(t) = population at time t
  K = carrying capacity (parameter)
  r = intrinsic growth rate (parameter)

Assumptions:
  1. Continuous population (large N)
  2. Closed population (no migration)
  3. Growth rate decreases linearly as P → K

Model (logistic equation):
  dP/dt = rP(1 - P/K)

Analysis:
  Fixed points: P = 0 (unstable), P = K (stable)
  Solution: P(t) = K / (1 + Ce^{-rt})
  Behavior: S-shaped growth, approaches K
```

### Optimization Models

```
OPTIMIZATION MODEL CONSTRUCTION
═══════════════════════════════════════════════════════════════

COMPONENTS
─────────────────────────────────────────

Decision variables:
  What can we choose/control?
  x = (x₁, x₂, ..., xₙ)

Objective function:
  What do we want to maximize/minimize?
  f(x) → min or max

Constraints:
  What restrictions apply?
  gᵢ(x) ≤ 0   (inequality constraints)
  hⱼ(x) = 0   (equality constraints)
  x ∈ X       (domain constraints)

STANDARD FORM
─────────────────────────────────────────

  minimize    f(x)
  subject to  gᵢ(x) ≤ 0,  i = 1,...,m
              hⱼ(x) = 0,  j = 1,...,p
              x ∈ X

CLASSIFICATION
─────────────────────────────────────────

By variable type:
  □ Continuous optimization
  □ Integer programming
  □ Mixed-integer programming

By function type:
  □ Linear programming (LP): f, g, h all linear
  □ Quadratic programming (QP): f quadratic, g, h linear
  □ Nonlinear programming (NLP): general functions
  □ Convex optimization: f, gᵢ convex, hⱼ affine

By structure:
  □ Unconstrained
  □ Box-constrained
  □ Network flow
  □ Combinatorial

EXAMPLE: Resource Allocation
─────────────────────────────────────────

Problem: Allocate budget across projects to maximize impact.

Decision variables:
  xᵢ = investment in project i

Objective:
  maximize Σᵢ bᵢ·log(1 + xᵢ)  (diminishing returns)

Constraints:
  Σᵢ xᵢ ≤ B           (budget constraint)
  xᵢ ≥ 0              (non-negativity)
  xᵢ ≤ cᵢ            (capacity constraints)
```

---

## Phase 3: Model Analysis

### Analytical Techniques

```
MODEL ANALYSIS METHODS
═══════════════════════════════════════════════════════════════

EXACT SOLUTIONS
─────────────────────────────────────────

When possible:
  □ Solve equations explicitly
  □ Find closed-form expressions
  □ Identify parameter dependence

Techniques:
  □ Standard ODE methods
  □ Separation of variables
  □ Fourier methods
  □ Laplace transforms
  □ Special functions

QUALITATIVE ANALYSIS
─────────────────────────────────────────

For ODEs:
  □ Find equilibrium points (fixed points)
  □ Determine stability (linearization)
  □ Sketch phase portraits
  □ Identify bifurcations
  □ Find invariant sets

Stability analysis:
  1. Find equilibria: f(x*) = 0
  2. Linearize: J = ∂f/∂x at x*
  3. Check eigenvalues of J:
     - All negative real parts → stable
     - Any positive real part → unstable
     - Pure imaginary → center (need higher order)

ASYMPTOTIC ANALYSIS
─────────────────────────────────────────

For limiting behavior:
  □ Long-time behavior (t → ∞)
  □ Large/small parameter limits
  □ Boundary layers
  □ Scaling analysis

Perturbation methods:
  □ Regular perturbation
  □ Singular perturbation
  □ Multiple scales
  □ WKB approximation

DIMENSIONAL ANALYSIS
─────────────────────────────────────────

Steps:
  1. List all variables and parameters
  2. Identify their dimensions
  3. Find dimensionless groups (Buckingham π theorem)
  4. Reduce parameter space
  5. Identify dominant balances

Example:
  Pendulum period T depends on: length L, mass m, gravity g
  Dimensions: [T] = T, [L] = L, [m] = M, [g] = LT⁻²
  Only one dimensionless group: T√(g/L)
  Therefore: T = C√(L/g) for some constant C
```

### Numerical Methods

```
NUMERICAL ANALYSIS TECHNIQUES
═══════════════════════════════════════════════════════════════

ODE SOLVERS
─────────────────────────────────────────

Euler's method (simple, first-order):
  yₙ₊₁ = yₙ + h·f(tₙ, yₙ)

Runge-Kutta methods (higher-order):
  RK4: Fourth-order, widely used
  k₁ = f(tₙ, yₙ)
  k₂ = f(tₙ + h/2, yₙ + h·k₁/2)
  k₃ = f(tₙ + h/2, yₙ + h·k₂/2)
  k₄ = f(tₙ + h, yₙ + h·k₃)
  yₙ₊₁ = yₙ + h(k₁ + 2k₂ + 2k₃ + k₄)/6

Adaptive methods:
  □ Adjust step size based on error estimate
  □ RK45 (Dormand-Prince)
  □ ode45 (MATLAB), solve_ivp (Python)

Stiff solvers:
  □ For problems with multiple timescales
  □ BDF methods, implicit methods
  □ ode15s (MATLAB), 'BDF' in solve_ivp

OPTIMIZATION SOLVERS
─────────────────────────────────────────

Unconstrained:
  □ Gradient descent
  □ Newton's method
  □ Quasi-Newton (BFGS)
  □ Conjugate gradient

Constrained:
  □ Simplex method (LP)
  □ Interior point methods
  □ Sequential quadratic programming
  □ Penalty/barrier methods

Global optimization:
  □ Simulated annealing
  □ Genetic algorithms
  □ Basin-hopping
  □ Branch and bound (discrete)

SENSITIVITY ANALYSIS
─────────────────────────────────────────

Local sensitivity:
  ∂output/∂parameter at nominal values

Global sensitivity:
  □ Sobol indices
  □ Morris method
  □ Monte Carlo sampling

Implementation:
  1. Define parameter ranges
  2. Sample parameter space
  3. Run model for each sample
  4. Compute sensitivity measures
```

---

## Phase 4: Validation and Refinement

### Model Validation

```
VALIDATION FRAMEWORK
═══════════════════════════════════════════════════════════════

VALIDATION TYPES
─────────────────────────────────────────

Face validation:
  □ Does the model make intuitive sense?
  □ Do experts find it reasonable?
  □ Are assumptions justified?

Internal validation:
  □ Is the mathematics correct?
  □ Are numerical solutions accurate?
  □ Is the code bug-free?

External validation:
  □ Does model match data?
  □ Does it predict out-of-sample?
  □ Does it generalize?

COMPARISON WITH DATA
─────────────────────────────────────────

Metrics:
  □ Mean squared error (MSE)
  □ Mean absolute error (MAE)
  □ R² (coefficient of determination)
  □ Residual analysis
  □ Confidence intervals

Visualization:
  □ Model vs data plots
  □ Residual plots
  □ Q-Q plots (for distributions)
  □ Time series comparisons

Statistical tests:
  □ Hypothesis tests for parameters
  □ Goodness-of-fit tests
  □ Cross-validation

VALIDATION CHECKLIST
─────────────────────────────────────────
□ Model reproduces known special cases
□ Model respects physical constraints
□ Predictions have correct dimensions
□ Behavior is reasonable at extremes
□ Sensitivity to parameters is understood
□ Comparison with data is documented
```

### Model Refinement

```
REFINEMENT STRATEGIES
═══════════════════════════════════════════════════════════════

WHEN MODEL FAILS
─────────────────────────────────────────

Systematic errors suggest:
  □ Missing phenomenon
  □ Wrong functional form
  □ Incorrect mechanism

Random errors suggest:
  □ Stochastic effects
  □ Measurement noise
  □ Parameter uncertainty

REFINEMENT OPTIONS
─────────────────────────────────────────

Add complexity:
  □ Include neglected effects
  □ Add spatial/temporal structure
  □ Remove linearizations
  □ Add stochastic terms

Reduce complexity:
  □ Aggregate variables
  □ Use quasi-steady approximations
  □ Simplify geometry
  □ Average over fast dynamics

Change structure:
  □ Different mechanisms
  □ Alternative formulations
  □ Hybrid models

REFINEMENT DOCUMENTATION
─────────────────────────────────────────
┌─────────────────────────────────────────────────────────────┐
│ MODEL VERSION: [v2.0]                                       │
│                                                             │
│ Changes from previous version:                              │
│   [list changes]                                            │
│                                                             │
│ Motivation:                                                 │
│   [why changes were made]                                   │
│                                                             │
│ Validation results:                                         │
│   Previous model: [metrics]                                 │
│   Current model: [metrics]                                  │
│                                                             │
│ Trade-offs:                                                 │
│   [what was gained/lost]                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Model Documentation Template

```
MODEL DOCUMENTATION
═══════════════════════════════════════════════════════════════

1. EXECUTIVE SUMMARY
─────────────────────────────────────────
Purpose: [what question does the model answer?]
Key finding: [main result/insight]
Limitations: [important caveats]

2. PROBLEM DESCRIPTION
─────────────────────────────────────────
Context: [background and motivation]
Question: [precise formulation]
Scope: [what's included and excluded]

3. MODEL FORMULATION
─────────────────────────────────────────
Variables:
  [list with units and descriptions]

Parameters:
  [list with values, units, sources]

Assumptions:
  [list with justifications]

Equations:
  [mathematical formulation]

4. ANALYSIS
─────────────────────────────────────────
Methods: [analytical and numerical]
Results: [key findings]
Sensitivity: [parameter dependence]

5. VALIDATION
─────────────────────────────────────────
Data sources: [what data was used]
Comparison: [model vs data]
Assessment: [quality of fit]

6. CONCLUSIONS
─────────────────────────────────────────
Findings: [what was learned]
Recommendations: [practical implications]
Future work: [extensions and improvements]

7. APPENDICES
─────────────────────────────────────────
Derivations: [mathematical details]
Code: [implementation]
Data: [datasets used]
```

---

## Integration with Agents

### Recommended Agent Combinations

- **proof-constructor**: Prove model properties
- **numerical-analyst**: Computational analysis
- **pattern-detector**: Identify model behaviors
- **experimentalist**: Validation methodology
- **cross-domain-translator**: Apply models across fields

---

## References

- Meerschaert, M.M. (2013). Mathematical Modeling (4th ed.)
- Fowler, A.C. (1997). Mathematical Models in the Applied Sciences
- Murray, J.D. (2002). Mathematical Biology I & II
- Edelstein-Keshet, L. (2005). Mathematical Models in Biology
- Gershenfeld, N. (1999). The Nature of Mathematical Modeling

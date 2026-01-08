# Complex Analysis Skill

## Overview

This skill provides methodology for complex analysis including holomorphic functions, contour integration, residue calculus, and conformal mappings. It coordinates with the complex-analyst agent for rigorous complex-variable techniques.

## Invocation

```
/complex-analysis [subcommand] [arguments]
```

## Subcommands

### `/complex-analysis holomorphic <function>`
Verify holomorphy, compute derivatives.

### `/complex-analysis integral <contour>`
Evaluate contour integrals using Cauchy or residues.

### `/complex-analysis residue <function> <point>`
Compute residues at singularities.

### `/complex-analysis series <function> <center>`
Find Taylor or Laurent series expansions.

### `/complex-analysis real-integral <integral>`
Evaluate real integrals using complex methods.

### `/complex-analysis conformal <domain>`
Find conformal mappings between domains.

---

## Methodology

### Holomorphy Verification Pipeline

```
CHECKING HOLOMORPHY
═══════════════════════════════════════════════════════════════

METHOD 1: CAUCHY-RIEMANN EQUATIONS
─────────────────────────────────────────
Write f(x + iy) = u(x,y) + iv(x,y)

Verify:
  □ ∂u/∂x = ∂v/∂y
  □ ∂u/∂y = -∂v/∂x
  □ Partial derivatives are continuous

Then f is holomorphic and f' = ∂u/∂x + i∂v/∂x

METHOD 2: DIRECT DEFINITION
─────────────────────────────────────────
Show lim_{h→0} [f(z₀+h) - f(z₀)]/h exists
(independent of how h → 0 in ℂ)

METHOD 3: COMPOSITION
─────────────────────────────────────────
□ Sums, products, quotients of holomorphic are holomorphic
□ Compositions of holomorphic are holomorphic
□ Power series are holomorphic inside radius of convergence

COMMON HOLOMORPHIC FUNCTIONS
─────────────────────────────────────────
□ Polynomials: everywhere
□ eᶻ, sin z, cos z: everywhere (entire)
□ Rational functions: except poles
□ log z: ℂ minus branch cut
□ zᵅ: ℂ minus branch cut (for non-integer α)
```

### Contour Integration Pipeline

```
CONTOUR INTEGRAL EVALUATION
═══════════════════════════════════════════════════════════════

STEP 1: IDENTIFY APPROACH
─────────────────────────────────────────
□ f holomorphic inside contour? → Cauchy's theorem (= 0)
□ Isolated singularities inside? → Residue theorem
□ Need Cauchy formula? → f(z₀) from integral

STEP 2: FOR RESIDUE THEOREM
─────────────────────────────────────────
∮_γ f(z) dz = 2πi × (sum of residues inside γ)

Find all singularities inside γ.
Compute residue at each.
Sum and multiply by 2πi.

STEP 3: VERIFY ORIENTATION
─────────────────────────────────────────
Standard (positive) orientation: counterclockwise
Negative orientation: clockwise (multiply result by -1)

PARAMETERIZATION METHOD
─────────────────────────────────────────
For direct computation:
∫_γ f(z) dz = ∫_a^b f(γ(t)) γ'(t) dt

Common parameterizations:
□ Circle |z - z₀| = r: γ(t) = z₀ + re^{it}, t ∈ [0, 2π]
□ Line segment: γ(t) = (1-t)z₁ + tz₂, t ∈ [0, 1]
```

### Residue Computation Pipeline

```
COMPUTING RESIDUES
═══════════════════════════════════════════════════════════════

STEP 1: CLASSIFY SINGULARITY
─────────────────────────────────────────
At z = z₀:
□ Removable: f bounded near z₀ (Res = 0)
□ Simple pole: lim(z-z₀)f(z) finite and nonzero
□ Pole of order m: lim(z-z₀)^m f(z) finite and nonzero
□ Essential: none of above

STEP 2: APPLY FORMULA
─────────────────────────────────────────
Simple pole:
  Res(f, z₀) = lim_{z→z₀} (z - z₀)f(z)

If f = g/h with h having simple zero at z₀:
  Res(f, z₀) = g(z₀)/h'(z₀)

Pole of order m:
  Res(f, z₀) = (1/(m-1)!) lim_{z→z₀} d^{m-1}/dz^{m-1}[(z-z₀)^m f(z)]

Laurent series:
  Res(f, z₀) = coefficient of (z-z₀)^{-1}

STEP 3: VERIFY
─────────────────────────────────────────
Check by alternative method or numerical approximation.
```

### Real Integral Evaluation Pipeline

```
EVALUATING REAL INTEGRALS
═══════════════════════════════════════════════════════════════

TYPE 1: ∫_{-∞}^∞ P(x)/Q(x) dx
─────────────────────────────────────────
Requirements:
  □ deg(Q) ≥ deg(P) + 2
  □ Q has no real zeros

Method:
1. Close contour with upper semicircle C_R
2. Show ∫_{C_R} → 0 as R → ∞
3. ∫_{-∞}^∞ = 2πi × (residues in upper half-plane)

TYPE 2: ∫_0^{2π} R(cos θ, sin θ) dθ
─────────────────────────────────────────
Substitution z = e^{iθ}:
  cos θ = (z + z⁻¹)/2
  sin θ = (z - z⁻¹)/(2i)
  dθ = dz/(iz)

∫_0^{2π} R dθ = ∮_{|z|=1} [rational in z] dz/iz

Use residue theorem on unit circle.

TYPE 3: ∫_{-∞}^∞ f(x)e^{iax} dx (a > 0)
─────────────────────────────────────────
Use Jordan's lemma:
If |f(z)| → 0 uniformly as |z| → ∞ in upper half-plane:
  ∫_{C_R} f(z)e^{iaz} dz → 0

For a < 0: Use lower half-plane.

TYPE 4: Integrals with branch cuts
─────────────────────────────────────────
∫_0^∞ x^{α-1}/(1+x) dx (0 < α < 1)

Use keyhole contour around branch cut [0,∞).
```

### Series Expansion Pipeline

```
SERIES EXPANSIONS
═══════════════════════════════════════════════════════════════

TAYLOR SERIES
─────────────────────────────────────────
f holomorphic at z₀:
  f(z) = Σ_{n=0}^∞ aₙ(z-z₀)^n

where aₙ = f^{(n)}(z₀)/n!

Radius of convergence = distance to nearest singularity.

LAURENT SERIES
─────────────────────────────────────────
f holomorphic in annulus r < |z-z₀| < R:
  f(z) = Σ_{n=-∞}^∞ aₙ(z-z₀)^n

where aₙ = (1/2πi) ∮ f(z)/(z-z₀)^{n+1} dz

Principal part: Σ_{n<0} aₙ(z-z₀)^n

STANDARD EXPANSIONS
─────────────────────────────────────────
eᶻ = Σ zⁿ/n!                    (R = ∞)
sin z = Σ (-1)^n z^{2n+1}/(2n+1)!   (R = ∞)
cos z = Σ (-1)^n z^{2n}/(2n)!       (R = ∞)
1/(1-z) = Σ zⁿ                  (R = 1)
log(1+z) = Σ (-1)^{n+1} zⁿ/n    (R = 1)

FINDING LAURENT SERIES
─────────────────────────────────────────
1. Partial fractions decomposition
2. Expand each term using geometric series
3. Combine, adjusting for different regions
```

### Conformal Mapping Pipeline

```
CONFORMAL MAPPING
═══════════════════════════════════════════════════════════════

STANDARD MAPPINGS
─────────────────────────────────────────
Upper half-plane ↔ Unit disk:
  w = (z - i)/(z + i)  (ℍ → 𝔻)
  z = i(1 + w)/(1 - w)  (𝔻 → ℍ)

Disk ↔ Disk (Möbius):
  w = e^{iθ}(z - a)/(1 - āz)  (maps a to 0)

Strip ↔ Half-plane:
  w = e^{πz/a}  ({0 < Im z < a} → upper half-plane)

Sector ↔ Half-plane:
  w = z^{π/α}  (sector of angle α → upper half-plane)

CONSTRUCTING MAPPINGS
─────────────────────────────────────────
Strategy: Chain standard mappings

Domain 1 → Standard → Domain 2

Common standard domains:
□ Upper half-plane ℍ
□ Unit disk 𝔻
□ Right half-plane
□ Strips, sectors

LINEAR FRACTIONAL TRANSFORMATIONS
─────────────────────────────────────────
w = (az + b)/(cz + d)

Properties:
□ Maps circles/lines to circles/lines
□ Determined by image of 3 points
□ Preserves cross-ratio

To find LFT mapping z₁, z₂, z₃ to w₁, w₂, w₃:
  (w - w₁)(w₂ - w₃)/((w - w₃)(w₂ - w₁)) = (z - z₁)(z₂ - z₃)/((z - z₃)(z₂ - z₁))

SCHWARZ-CHRISTOFFEL FORMULA
─────────────────────────────────────────
Maps upper half-plane to polygon:
  f(z) = A ∫ (z-x₁)^{α₁-1}...(z-xₙ)^{αₙ-1} dz + B

where xₖ are preimages of vertices, αₖπ are interior angles.
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Notes |
|--------------|---------------|-------|
| Holomorphy | complex-analyst | Cauchy-Riemann |
| Contour integrals | complex-analyst | Residues |
| Real integrals | complex-analyst | Contour choice |
| Series | complex-analyst | Laurent |
| Conformal maps | complex-analyst | Standard maps |
| Harmonic functions | real-analyst + complex-analyst | Connection |

---

## Output Format

### Residue Computation
```
RESIDUE CALCULATION
═══════════════════════════════════════════════════════════════

FUNCTION: f(z) = [expression]
POINT: z₀ = [value]

SINGULARITY TYPE
─────────────────────────────────────────
[Pole of order m / Essential / Removable]

COMPUTATION
─────────────────────────────────────────
[Method and calculation]

RESULT
─────────────────────────────────────────
Res(f, z₀) = [value]
```

### Real Integral Evaluation
```
REAL INTEGRAL VIA COMPLEX METHODS
═══════════════════════════════════════════════════════════════

INTEGRAL: ∫ [expression] dx

CONTOUR
─────────────────────────────────────────
[Description of contour]

SINGULARITIES INSIDE CONTOUR
─────────────────────────────────────────
[List with residues]

AUXILIARY INTEGRALS
─────────────────────────────────────────
[Show other parts → 0 or compute them]

RESULT
─────────────────────────────────────────
∫ = [value]
```

---

## Examples

### Example: Evaluate ∫_{-∞}^∞ dx/(1+x²)²

```
/complex-analysis real-integral "1/(1+x^2)^2 from -∞ to ∞"

REAL INTEGRAL VIA RESIDUES
═══════════════════════════════════════════════════════════════

INTEGRAL: ∫_{-∞}^∞ dx/(1+x²)²

STEP 1: CONTOUR
─────────────────────────────────────────
Use semicircle in upper half-plane:
  [-R, R] on real axis + semicircle C_R

STEP 2: CHECK CONDITIONS
─────────────────────────────────────────
|1/(1+z²)²| ~ 1/|z|⁴ for large |z|
deg(denominator) = 4 ≥ deg(numerator) + 2 ✓

So ∫_{C_R} → 0 as R → ∞.

STEP 3: SINGULARITIES
─────────────────────────────────────────
1 + z² = 0 ⟹ z = ±i

In upper half-plane: z = i (pole of order 2)

STEP 4: COMPUTE RESIDUE
─────────────────────────────────────────
f(z) = 1/(z+i)²(z-i)²

Res(f, i) = d/dz[1/(z+i)²]|_{z=i}
          = -2/(z+i)³|_{z=i}
          = -2/(2i)³
          = -2/(-8i)
          = 1/(4i)

STEP 5: APPLY RESIDUE THEOREM
─────────────────────────────────────────
∮ f(z) dz = 2πi · Res(f, i) = 2πi · 1/(4i) = π/2

As R → ∞:
∫_{-∞}^∞ dx/(1+x²)² = π/2
```

---

## References

- Ahlfors - Complex Analysis
- Conway - Functions of One Complex Variable
- Stein & Shakarchi - Complex Analysis
- Needham - Visual Complex Analysis

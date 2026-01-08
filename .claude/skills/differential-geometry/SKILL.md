# Differential Geometry Skill

## Overview

This skill provides methodology for differential geometry including smooth manifolds, tangent bundles, vector fields, differential forms, Riemannian metrics, and curvature. It coordinates with the differential-geometer agent for geometric analysis using calculus.

## Invocation

```
/differential-geometry [subcommand] [arguments]
```

## Subcommands

### `/differential-geometry manifold <specification>`
Analyze smooth manifold structure (charts, atlas, submanifolds).

### `/differential-geometry tangent <manifold>`
Analyze tangent bundle, vector fields, and flows.

### `/differential-geometry forms <manifold>`
Work with differential forms and exterior calculus.

### `/differential-geometry metric <manifold>`
Analyze Riemannian metrics and geodesics.

### `/differential-geometry curvature <metric>`
Compute curvature tensors (Riemann, Ricci, scalar).

### `/differential-geometry connection <bundle>`
Analyze connections and parallel transport.

---

## Methodology

### Smooth Manifold Analysis Pipeline

```
SMOOTH MANIFOLD VERIFICATION
═══════════════════════════════════════════════════════════════

STEP 1: TOPOLOGICAL PREREQUISITES
─────────────────────────────────────────
Verify M is:
□ Hausdorff
□ Second countable
□ Locally Euclidean (homeomorphic to ℝⁿ locally)

STEP 2: ATLAS CONSTRUCTION
─────────────────────────────────────────
Atlas {(Uα, φα)} where:
□ {Uα} covers M
□ φα: Uα → ℝⁿ homeomorphism onto open set
□ Transition maps φα ∘ φβ⁻¹: φβ(Uα ∩ Uβ) → φα(Uα ∩ Uβ) are C∞

STEP 3: DIMENSION VERIFICATION
─────────────────────────────────────────
All charts map to same ℝⁿ (n = dim M)
Invariance of domain ensures well-defined

COMMON EXAMPLES
─────────────────────────────────────────
□ ℝⁿ: Single chart (id)
□ Sⁿ: Stereographic projections from N and S
□ ℝPⁿ: n+1 charts from standard affine patches
□ Lie groups: Left translation charts
□ Level sets: Regular value theorem

SUBMANIFOLD CRITERION
═══════════════════════════════════════════════════════════════

REGULAR VALUE THEOREM
─────────────────────────────────────────
If f: M → N smooth, c ∈ N regular value (df surjective at f⁻¹(c)):
  f⁻¹(c) is smooth submanifold of codimension dim N

IMMERSION THEOREM
─────────────────────────────────────────
If f: M → N immersion (df injective everywhere):
  f is local embedding
  f(M) locally a submanifold
```

### Tangent Space and Vector Field Pipeline

```
TANGENT SPACE COMPUTATION
═══════════════════════════════════════════════════════════════

DERIVATION DEFINITION
─────────────────────────────────────────
TₚM = {v: C∞(M) → ℝ : v linear, v(fg) = v(f)g(p) + f(p)v(g)}

COORDINATE BASIS
─────────────────────────────────────────
In chart (U, x¹,...,xⁿ):
  ∂/∂xⁱ|ₚ: f ↦ ∂(f ∘ φ⁻¹)/∂xⁱ|_{φ(p)}

{∂/∂x¹|ₚ,..., ∂/∂xⁿ|ₚ} is basis for TₚM

General vector: v = Σ vⁱ ∂/∂xⁱ

TANGENT BUNDLE
─────────────────────────────────────────
TM = ∐_{p∈M} TₚM
dim(TM) = 2n
π: TM → M projection

VECTOR FIELDS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Vector field X: Smooth section X: M → TM
In coordinates: X = Σ Xⁱ(x) ∂/∂xⁱ

LIE BRACKET
─────────────────────────────────────────
[X, Y]f = X(Yf) - Y(Xf)

In coordinates: [X, Y]ⁱ = Σⱼ (Xʲ ∂Yⁱ/∂xʲ - Yʲ ∂Xⁱ/∂xʲ)

Properties:
□ Bilinear, antisymmetric
□ Jacobi identity
□ 𝔛(M) is Lie algebra

FLOWS
═══════════════════════════════════════════════════════════════

INTEGRAL CURVES
─────────────────────────────────────────
γ: I → M integral curve of X if γ'(t) = X(γ(t))

FLOW MAP
─────────────────────────────────────────
φ: ℝ × M → M (where defined)
φₜ(p) = integral curve through p at time t

Properties:
□ φ₀ = id
□ φₛ ∘ φₜ = φₛ₊ₜ (group property)
□ d/dt|₀ φₜ(p) = X(p)

LIE DERIVATIVE
─────────────────────────────────────────
ℒ_X Y = [X, Y]
ℒ_X f = X(f)
```

### Differential Forms Pipeline

```
DIFFERENTIAL FORMS
═══════════════════════════════════════════════════════════════

k-FORMS
─────────────────────────────────────────
Ωᵏ(M) = smooth sections of Λᵏ(T*M)

k-form ω assigns to each p:
  ωₚ: TₚM × ⋯ × TₚM → ℝ (k copies, alternating multilinear)

In coordinates: ω = Σ ωᵢ₁...ᵢₖ dxⁱ¹ ∧ ⋯ ∧ dxⁱᵏ

WEDGE PRODUCT
─────────────────────────────────────────
∧: Ωᵏ × Ωˡ → Ωᵏ⁺ˡ

Properties:
□ Associative
□ α ∧ β = (-1)^{kl} β ∧ α
□ dxⁱ ∧ dxʲ = -dxʲ ∧ dxⁱ

EXTERIOR DERIVATIVE
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
d: Ωᵏ(M) → Ωᵏ⁺¹(M)

For f: df = Σ (∂f/∂xⁱ) dxⁱ
For ω = Σ ωᵢ dx^I: dω = Σ dωᵢ ∧ dx^I

PROPERTIES
─────────────────────────────────────────
□ d² = 0 (fundamental!)
□ d(α ∧ β) = dα ∧ β + (-1)^{deg α} α ∧ dβ
□ Naturality: f*(dω) = d(f*ω)

CLOSED AND EXACT FORMS
─────────────────────────────────────────
ω closed: dω = 0
ω exact: ω = dη

Exact ⟹ Closed (d² = 0)
Poincaré lemma: On contractible domains, closed ⟹ exact

DE RHAM COHOMOLOGY
═══════════════════════════════════════════════════════════════

H^k_{dR}(M) = {closed k-forms} / {exact k-forms}
            = ker(d: Ωᵏ → Ωᵏ⁺¹) / im(d: Ωᵏ⁻¹ → Ωᵏ)

de Rham theorem: H^k_{dR}(M) ≅ H^k(M; ℝ)

COMPUTATION STRATEGY
─────────────────────────────────────────
1. Identify closed forms
2. Determine which are exact
3. Quotient gives cohomology
```

### Riemannian Geometry Pipeline

```
RIEMANNIAN METRIC
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
g: Smooth assignment p ↦ gₚ where
  gₚ: TₚM × TₚM → ℝ symmetric positive definite bilinear

In coordinates: g = Σ gᵢⱼ dxⁱ ⊗ dxʲ
  ⟨v, w⟩ = Σ gᵢⱼ vⁱ wʲ

LENGTH AND DISTANCE
─────────────────────────────────────────
Length: L(γ) = ∫ |γ'(t)| dt = ∫ √⟨γ'(t), γ'(t)⟩ dt
Distance: d(p,q) = inf{L(γ) : γ from p to q}

STANDARD METRICS
─────────────────────────────────────────
□ Euclidean: gᵢⱼ = δᵢⱼ
□ Sphere Sⁿ ⊂ ℝⁿ⁺¹: Induced metric
□ Hyperbolic: ds² = (dx₁² + ⋯ + dxₙ²)/xₙ²

LEVI-CIVITA CONNECTION
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Unique connection ∇ satisfying:
□ Torsion-free: ∇_X Y - ∇_Y X = [X, Y]
□ Metric-compatible: X⟨Y, Z⟩ = ⟨∇_X Y, Z⟩ + ⟨Y, ∇_X Z⟩

CHRISTOFFEL SYMBOLS
─────────────────────────────────────────
∇_{∂ᵢ} ∂ⱼ = Σₖ Γᵏᵢⱼ ∂ₖ

Γᵏᵢⱼ = ½ Σₗ gᵏˡ (∂ᵢgⱼˡ + ∂ⱼgᵢˡ - ∂ₗgᵢⱼ)

COVARIANT DERIVATIVE
─────────────────────────────────────────
Along curve: ∇_{γ'} Y = Σₖ (dYᵏ/dt + Σᵢⱼ Γᵏᵢⱼ γ'ⁱ Yʲ) ∂ₖ

GEODESICS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
γ geodesic: ∇_{γ'} γ' = 0 (parallel velocity)

GEODESIC EQUATION
─────────────────────────────────────────
d²γᵏ/dt² + Σᵢⱼ Γᵏᵢⱼ (dγⁱ/dt)(dγʲ/dt) = 0

PROPERTIES
─────────────────────────────────────────
□ Locally length minimizing
□ Constant speed
□ Determined by initial point and velocity

EXPONENTIAL MAP
─────────────────────────────────────────
exp_p: TₚM → M
exp_p(v) = γᵥ(1) where γᵥ geodesic with γᵥ(0) = p, γ'ᵥ(0) = v
```

### Curvature Computation Pipeline

```
RIEMANN CURVATURE TENSOR
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
R(X, Y)Z = ∇_X ∇_Y Z - ∇_Y ∇_X Z - ∇_{[X,Y]} Z

Measures failure of parallel transport to commute.

COMPONENTS
─────────────────────────────────────────
R^l_{ijk} = ⟨R(∂ᵢ, ∂ⱼ)∂ₖ, ∂ˡ⟩/gˡˡ
          = ∂ᵢΓˡⱼₖ - ∂ⱼΓˡᵢₖ + ΓˡᵢₘΓᵐⱼₖ - ΓˡⱼₘΓᵐᵢₖ

SYMMETRIES
─────────────────────────────────────────
□ R(X,Y) = -R(Y,X)
□ ⟨R(X,Y)Z, W⟩ = -⟨R(X,Y)W, Z⟩
□ Bianchi: R(X,Y)Z + R(Y,Z)X + R(Z,X)Y = 0
□ ⟨R(X,Y)Z, W⟩ = ⟨R(Z,W)X, Y⟩

SECTIONAL CURVATURE
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
For 2-plane σ = span{X, Y}:
  K(σ) = ⟨R(X,Y)Y, X⟩ / (⟨X,X⟩⟨Y,Y⟩ - ⟨X,Y⟩²)

Sectional curvature determines full Riemann tensor.

CONSTANT CURVATURE
─────────────────────────────────────────
K ≡ 0: Flat (locally Euclidean ℝⁿ)
K ≡ 1: Locally spherical (Sⁿ)
K ≡ -1: Locally hyperbolic (ℍⁿ)

RICCI AND SCALAR CURVATURE
═══════════════════════════════════════════════════════════════

RICCI CURVATURE
─────────────────────────────────────────
Ric(X, Y) = trace(Z ↦ R(Z, X)Y)
Ricᵢⱼ = Σₖ R^k_{ikj}

SCALAR CURVATURE
─────────────────────────────────────────
S = trace(Ric) = Σⁱʲ gⁱʲ Ricᵢⱼ

EINSTEIN CONDITION
─────────────────────────────────────────
Ric = λg (Einstein manifold)
Examples: Spheres, hyperbolic spaces, Kähler-Einstein
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Notes |
|--------------|---------------|-------|
| Manifold structure | differential-geometer | Charts, submanifolds |
| Vector fields/flows | differential-geometer | Lie brackets |
| Differential forms | differential-geometer | de Rham |
| Curvature | differential-geometer | Riemann tensor |
| Topology | algebraic-topologist | Homology, π₁ |
| Classical geometry | geometer | Euclidean, projective |

---

## Output Format

### Manifold Analysis
```
MANIFOLD ANALYSIS: M
═══════════════════════════════════════════════════════════════

DESCRIPTION
─────────────────────────────────────────
[Definition of M]

ATLAS
─────────────────────────────────────────
Charts: {(Uα, φα)}
Transition maps: [description]

DIMENSION: n = [value]

TANGENT SPACE
─────────────────────────────────────────
TₚM at typical point p = [description]
Basis: {∂/∂x¹,...,∂/∂xⁿ}

KEY PROPERTIES
─────────────────────────────────────────
□ Orientable: [Yes/No]
□ Compact: [Yes/No]
□ Connected: [Yes/No]
```

### Curvature Computation
```
CURVATURE ANALYSIS: (M, g)
═══════════════════════════════════════════════════════════════

METRIC
─────────────────────────────────────────
g = [expression in coordinates]

CHRISTOFFEL SYMBOLS
─────────────────────────────────────────
Γᵏᵢⱼ = [values]

RIEMANN TENSOR
─────────────────────────────────────────
R^l_{ijk} = [nonzero components]

SECTIONAL CURVATURE
─────────────────────────────────────────
K(∂ᵢ, ∂ⱼ) = [values]

RICCI TENSOR
─────────────────────────────────────────
Ric = [matrix form]

SCALAR CURVATURE
─────────────────────────────────────────
S = [value]
```

---

## Examples

### Example: Tangent space of S²

```
/differential-geometry tangent "S²"

TANGENT SPACE ANALYSIS: S²
═══════════════════════════════════════════════════════════════

DESCRIPTION
─────────────────────────────────────────
S² = {(x,y,z) ∈ ℝ³ : x² + y² + z² = 1}

EMBEDDING VIEW
─────────────────────────────────────────
S² ⊂ ℝ³ as level set of f(x,y,z) = x² + y² + z²

At p = (x₀, y₀, z₀):
  ∇f = (2x₀, 2y₀, 2z₀) (normal to sphere)

TₚS² = {v ∈ ℝ³ : v ⊥ p}
     = {v : x₀v₁ + y₀v₂ + z₀v₃ = 0}

COORDINATE DESCRIPTION
─────────────────────────────────────────
Using spherical coordinates (θ, φ):
  x = sin θ cos φ
  y = sin θ sin φ
  z = cos θ

Coordinate basis:
  ∂/∂θ = (cos θ cos φ, cos θ sin φ, -sin θ)
  ∂/∂φ = (-sin θ sin φ, sin θ cos φ, 0)

These span TₚS² (2-dimensional).

TANGENT BUNDLE
─────────────────────────────────────────
TS² = {(p, v) : p ∈ S², v ∈ TₚS²}
dim(TS²) = 4

Note: TS² is nontrivial bundle (S² has no nonvanishing vector field
by hairy ball theorem).
```

### Example: Curvature of S² with round metric

```
/differential-geometry curvature "S² round"

CURVATURE: S² with Round Metric
═══════════════════════════════════════════════════════════════

METRIC
─────────────────────────────────────────
Induced from ℝ³ in spherical coordinates (θ, φ):
  g = dθ² + sin²θ dφ²

gᵢⱼ = [1      0    ]
      [0   sin²θ   ]

CHRISTOFFEL SYMBOLS
─────────────────────────────────────────
Nonzero symbols:
  Γ^θ_{φφ} = -sin θ cos θ
  Γ^φ_{θφ} = Γ^φ_{φθ} = cot θ

RIEMANN TENSOR
─────────────────────────────────────────
R^θ_{φθφ} = sin²θ
R^φ_{θφθ} = 1

⟨R(∂_θ, ∂_φ)∂_φ, ∂_θ⟩ = sin²θ

SECTIONAL CURVATURE
─────────────────────────────────────────
K = ⟨R(∂_θ, ∂_φ)∂_φ, ∂_θ⟩ / (g_{θθ}g_{φφ} - g_{θφ}²)
  = sin²θ / (1 · sin²θ - 0)
  = 1

Constant sectional curvature K = 1.

RICCI AND SCALAR
─────────────────────────────────────────
Ric = g (Einstein with λ = 1)

Ricᵢⱼ = [1      0    ]
        [0   sin²θ   ]

S = 2 (for 2-sphere of radius 1)

CONCLUSION
─────────────────────────────────────────
S² with round metric has constant positive curvature K = 1.
It is the unique simply connected complete surface of constant
positive curvature (up to isometry).
```

---

## References

- Lee, J.M. (2018). Introduction to Smooth Manifolds
- Lee, J.M. (2018). Introduction to Riemannian Manifolds
- do Carmo, M. (1992). Riemannian Geometry
- Spivak, M. (1999). A Comprehensive Introduction to Differential Geometry

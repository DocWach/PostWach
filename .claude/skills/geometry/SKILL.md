# Geometry Skill

## Overview

This skill provides methodology for classical geometry including Euclidean, projective, affine, and convex geometry. It coordinates with the geometer agent for synthetic and analytic approaches to geometric problems.

## Invocation

```
/geometry [subcommand] [arguments]
```

## Subcommands

### `/geometry euclidean <figure>`
Analyze Euclidean geometry (triangles, circles, classical theorems).

### `/geometry projective <figure>`
Analyze projective geometry (cross-ratio, duality, conics).

### `/geometry affine <figure>`
Analyze affine geometry (barycentric coordinates, affine invariants).

### `/geometry convex <set>`
Analyze convex geometry (polytopes, separation theorems).

### `/geometry transformation <type>`
Analyze geometric transformations and invariants.

### `/geometry construction <goal>`
Compass and straightedge constructions.

---

## Methodology

### Euclidean Geometry Pipeline

```
EUCLIDEAN GEOMETRY ANALYSIS
═══════════════════════════════════════════════════════════════

FOUNDATIONS
─────────────────────────────────────────
Distance: d(x,y) = |x - y| = √(Σ(xᵢ - yᵢ)²)
Angle: cos θ = ⟨u,v⟩/(|u||v|)

Isometries preserve distance and angle.
Isom(ℝⁿ) = O(n) ⋊ ℝⁿ

TRIANGLE ANALYSIS
═══════════════════════════════════════════════════════════════

TRIANGLE CENTERS
─────────────────────────────────────────
□ Centroid G: (A + B + C)/3
  Intersection of medians
  Divides each median 2:1

□ Circumcenter O: Equidistant from vertices
  Intersection of perpendicular bisectors
  Center of circumscribed circle

□ Incenter I: Equidistant from sides
  Intersection of angle bisectors
  Center of inscribed circle

□ Orthocenter H: Intersection of altitudes

EULER LINE
─────────────────────────────────────────
G, O, H collinear with G dividing OH in ratio 1:2
  G = (O + 2H)/3

FUNDAMENTAL THEOREMS
═══════════════════════════════════════════════════════════════

PYTHAGOREAN THEOREM
─────────────────────────────────────────
Right triangle with legs a, b and hypotenuse c:
  a² + b² = c²

LAW OF COSINES
─────────────────────────────────────────
c² = a² + b² - 2ab cos C

LAW OF SINES
─────────────────────────────────────────
a/sin A = b/sin B = c/sin C = 2R
(R = circumradius)

STEWART'S THEOREM
─────────────────────────────────────────
Cevian AD with BD = m, DC = n, AD = d:
  b²m + c²n - a(d² + mn) = 0

CIRCLE THEOREMS
═══════════════════════════════════════════════════════════════

INSCRIBED ANGLE THEOREM
─────────────────────────────────────────
Inscribed angle = ½ central angle (same arc)
Angles in same arc are equal

POWER OF A POINT
─────────────────────────────────────────
For point P and circle with center O, radius r:
  Power(P) = |PO|² - r²

For secants through P:
  PA · PB = PC · PD

RADICAL AXIS
─────────────────────────────────────────
Locus of points with equal power to two circles.
Always a line perpendicular to line of centers.

Three circles: Radical axes concurrent at radical center.

PTOLEMY'S THEOREM
─────────────────────────────────────────
Cyclic quadrilateral ABCD:
  AC · BD = AB · CD + AD · BC

Equality characterizes cyclic quadrilaterals.
```

### Projective Geometry Pipeline

```
PROJECTIVE GEOMETRY
═══════════════════════════════════════════════════════════════

PROJECTIVE SPACE
─────────────────────────────────────────
ℙⁿ = (ℝⁿ⁺¹ \ {0}) / ~ where x ~ λx for λ ≠ 0

Points: Lines through origin in ℝⁿ⁺¹
Homogeneous coordinates: [x₀ : x₁ : ⋯ : xₙ]

ℙ¹ = ℝ ∪ {∞}
ℙ² = ℝ² plus "line at infinity"

INCIDENCE
─────────────────────────────────────────
Point P = [a : b : c], Line ℓ = [p : q : r]
P ∈ ℓ ⟺ ap + bq + cr = 0

DUALITY
─────────────────────────────────────────
In ℙ²: Points ↔ Lines
Every theorem has dual (interchange point/line).

FUNDAMENTAL PROPERTIES
─────────────────────────────────────────
□ Any two distinct points determine unique line
□ Any two distinct lines meet in unique point (no parallels!)
□ Desargues' theorem holds
□ Pappus' theorem holds

CROSS-RATIO
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
For four collinear points A, B, C, D:
  (A, B; C, D) = (AC/BC) / (AD/BD)

With coordinates: (a, b; c, d) = (c-a)(d-b) / (c-b)(d-a)

PROPERTIES
─────────────────────────────────────────
□ Projective invariant (fundamental!)
□ 24 values under permutation, related by:
  λ, 1/λ, 1-λ, 1/(1-λ), (λ-1)/λ, λ/(λ-1)
□ Harmonic division: (A,B;C,D) = -1

PROJECTIVE TRANSFORMATIONS
═══════════════════════════════════════════════════════════════

PGL(n+1) acts on ℙⁿ:
  [x] ↦ [Ax] for invertible A

In ℙ²: 8 parameters (3×3 matrix up to scale)
Determined uniquely by 4 points in general position.

CONICS
═══════════════════════════════════════════════════════════════

Conic: xᵀQx = 0 for symmetric 3×3 matrix Q

CLASSIFICATION
─────────────────────────────────────────
By rank of Q:
□ Rank 3: Nondegenerate (ellipse, hyperbola, parabola)
□ Rank 2: Pair of lines
□ Rank 1: Double line

5 points (no 3 collinear) determine unique conic.

PASCAL'S THEOREM
─────────────────────────────────────────
Hexagon inscribed in conic:
  Opposite sides meet on a line (Pascal line)

BRIANCHON'S THEOREM (Dual)
─────────────────────────────────────────
Hexagon circumscribed about conic:
  Diagonals are concurrent (Brianchon point)
```

### Affine Geometry Pipeline

```
AFFINE GEOMETRY
═══════════════════════════════════════════════════════════════

AFFINE SPACE
─────────────────────────────────────────
𝔸ⁿ = set with free transitive action of ℝⁿ

Points without preferred origin.
Vectors = differences of points.

AFFINE TRANSFORMATIONS
─────────────────────────────────────────
f(x) = Ax + b where A invertible

Aff(n) = GL(n) ⋊ ℝⁿ

PRESERVED PROPERTIES
─────────────────────────────────────────
□ Collinearity
□ Parallelism
□ Ratios of lengths on parallel lines
□ Barycentric combinations

NOT PRESERVED
─────────────────────────────────────────
□ Distances
□ Angles
□ Perpendicularity

BARYCENTRIC COORDINATES
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
For simplex with vertices P₀,...,Pₙ:
  P = Σλᵢ Pᵢ with Σλᵢ = 1

(λ₀,...,λₙ) are barycentric coordinates of P.

PROPERTIES
─────────────────────────────────────────
□ λᵢ ≥ 0 for all i ⟺ P inside simplex
□ λᵢ = 0 ⟺ P on face opposite Pᵢ
□ Affine invariant

TRIANGLE COORDINATES
─────────────────────────────────────────
For triangle ABC, P has coordinates (λ_A, λ_B, λ_C):
  P = λ_A · A + λ_B · B + λ_C · C
  λ_A + λ_B + λ_C = 1

Centroid: (1/3, 1/3, 1/3)
Incenter: (a, b, c)/(a+b+c) where a,b,c are side lengths

AFFINE INVARIANTS
═══════════════════════════════════════════════════════════════

□ Ratios of parallel segments
□ Area/volume ratios
□ Parallelism
□ Signed ratios (division ratio)
□ Barycentric coordinates
```

### Convex Geometry Pipeline

```
CONVEX SETS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
C ⊆ ℝⁿ convex: ∀x,y ∈ C, t ∈ [0,1]:
  tx + (1-t)y ∈ C

(Line segment stays inside)

CONVEX HULL
─────────────────────────────────────────
conv(S) = smallest convex set containing S
        = {Σλᵢxᵢ : xᵢ ∈ S, λᵢ ≥ 0, Σλᵢ = 1}

CARATHÉODORY'S THEOREM
─────────────────────────────────────────
In ℝⁿ: Every point in conv(S) is convex combination of ≤ n+1 points of S.

EXTREME POINTS
─────────────────────────────────────────
x extreme in C: Cannot write x = ty + (1-t)z with y ≠ z in C

KREIN-MILMAN THEOREM
─────────────────────────────────────────
Compact convex C = closed convex hull of extreme points.

SEPARATION THEOREMS
═══════════════════════════════════════════════════════════════

SEPARATING HYPERPLANE
─────────────────────────────────────────
Disjoint convex C, D (one compact, one closed):
  ∃ hyperplane H strictly separating C from D

SUPPORTING HYPERPLANE
─────────────────────────────────────────
For convex C and boundary point p:
  ∃ hyperplane H with p ∈ H and C on one side

HAHN-BANACH (Geometric Form)
─────────────────────────────────────────
Point p outside closed convex C:
  ∃ hyperplane strictly separating p from C

POLYTOPES
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Polytope = convex hull of finitely many points
         = bounded intersection of finitely many half-spaces

FACE LATTICE
─────────────────────────────────────────
□ Vertices (0-faces)
□ Edges (1-faces)
□ Facets (codimension 1 faces)

Face = intersection with supporting hyperplane

EULER'S FORMULA (3D)
─────────────────────────────────────────
V - E + F = 2 for convex polyhedron

PLATONIC SOLIDS
─────────────────────────────────────────
Regular convex polyhedra (all faces congruent regular polygons):
□ Tetrahedron: 4 triangles
□ Cube: 6 squares
□ Octahedron: 8 triangles
□ Dodecahedron: 12 pentagons
□ Icosahedron: 20 triangles

DUAL POLYTOPES
─────────────────────────────────────────
P* = {y : ⟨x,y⟩ ≤ 1 ∀x ∈ P}

Faces of P ↔ Faces of P* (reverse dimension)
Cube ↔ Octahedron, Dodecahedron ↔ Icosahedron
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Notes |
|--------------|---------------|-------|
| Classical theorems | geometer | Triangle, circle theorems |
| Projective/affine | geometer | Cross-ratio, duality |
| Convex analysis | geometer | Polytopes, separation |
| Manifolds | differential-geometer | Smooth structure |
| Topology | algebraic-topologist | Invariants |

---

## Output Format

### Euclidean Geometry Proof
```
EUCLIDEAN GEOMETRY PROBLEM
═══════════════════════════════════════════════════════════════

GIVEN
─────────────────────────────────────────
[Setup and given information]

TO PROVE
─────────────────────────────────────────
[Statement to prove]

PROOF
─────────────────────────────────────────
[Step-by-step reasoning]

□ [Conclusion]
```

### Projective Geometry Analysis
```
PROJECTIVE ANALYSIS
═══════════════════════════════════════════════════════════════

CONFIGURATION
─────────────────────────────────────────
[Points, lines, conics in homogeneous coordinates]

CROSS-RATIO COMPUTATION
─────────────────────────────────────────
(A, B; C, D) = [calculation]

PROJECTIVE TRANSFORMATION
─────────────────────────────────────────
[Matrix and its action]

INVARIANTS
─────────────────────────────────────────
[Preserved quantities]
```

---

## Examples

### Example: Prove the Euler Line Theorem

```
/geometry euclidean "Euler line"

EULER LINE THEOREM
═══════════════════════════════════════════════════════════════

STATEMENT
─────────────────────────────────────────
In any triangle, the centroid G, circumcenter O, and
orthocenter H are collinear, with G dividing OH in ratio 1:2.

PROOF
─────────────────────────────────────────
Let triangle ABC have vertices A, B, C (position vectors).

CENTROID:
  G = (A + B + C)/3

CIRCUMCENTER:
  O satisfies |O - A| = |O - B| = |O - C| = R

ORTHOCENTER:
  H satisfies (H - A) ⊥ (B - C), etc.

  Claim: H = A + B + C - 2O

  Verify: (H - A) · (B - C) = (B + C - 2O) · (B - C)
         = |B|² - |C|² - 2O·(B - C)
         = |B|² - |C|² - 2(O·B - O·C)

  Since |O - B|² = |O - C|²:
    |O|² - 2O·B + |B|² = |O|² - 2O·C + |C|²
    O·B - O·C = (|B|² - |C|²)/2

  So (H - A) · (B - C) = |B|² - |C|² - (|B|² - |C|²) = 0  ✓

COLLINEARITY:
  G = (A + B + C)/3
  H = A + B + C - 2O

  So G = (H + 2O)/3

  This shows G lies on segment OH with OG:GH = 1:2.  □

COROLLARY
─────────────────────────────────────────
O⃗G = G⃗H/2, so G divides OH in ratio 1:2.
```

### Example: Cross-ratio calculation

```
/geometry projective "cross-ratio"

CROSS-RATIO COMPUTATION
═══════════════════════════════════════════════════════════════

PROBLEM
─────────────────────────────────────────
Compute (0, 1; 2, ∞) on ℙ¹.

METHOD
─────────────────────────────────────────
Using formula: (a, b; c, d) = (c-a)(d-b) / (c-b)(d-a)

With d = ∞, interpret as limit:
  (a, b; c, ∞) = lim_{d→∞} (c-a)(d-b) / (c-b)(d-a)
               = (c-a)/(c-b)

CALCULATION
─────────────────────────────────────────
(0, 1; 2, ∞) = (2-0)/(2-1) = 2/1 = 2

VERIFICATION (Homogeneous coordinates)
─────────────────────────────────────────
A = [0:1], B = [1:1], C = [2:1], D = [1:0]

Using determinants:
  (A,B;C,D) = det[A,C]·det[B,D] / det[B,C]·det[A,D]
            = det[0 2; 1 1]·det[1 1; 1 0] / det[1 2; 1 1]·det[0 1; 1 0]
            = (-2)·(-1) / (-1)·(-1)
            = 2/1 = 2  ✓

HARMONIC CONJUGATE
─────────────────────────────────────────
Given A, B, C with (A, B; C, D) = -1:
  D is harmonic conjugate of C with respect to A, B.

For (0, 1; 2, D) = -1:
  (2-0)/(2-1) · (D-1)/(D-0) = -1
  2(D-1)/D = -1
  2D - 2 = -D
  D = 2/3

So D = 2/3 is harmonic conjugate of C = 2 w.r.t. A = 0, B = 1.
```

---

## References

- Coxeter, H.S.M. (1969). Introduction to Geometry
- Hartshorne, R. (2000). Geometry: Euclid and Beyond
- Berger, M. (2009). Geometry I, II
- Grünbaum, B. (2003). Convex Polytopes

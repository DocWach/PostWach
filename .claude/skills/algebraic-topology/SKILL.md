# Algebraic Topology Skill

## Overview

This skill provides methodology for algebraic topology including fundamental groups, covering spaces, homology, and cohomology. It coordinates with the algebraic-topologist agent for computing algebraic invariants of topological spaces.

## Invocation

```
/algebraic-topology [subcommand] [arguments]
```

## Subcommands

### `/algebraic-topology fundamental-group <space>`
Compute π₁ using Van Kampen or covering space theory.

### `/algebraic-topology covering <space>`
Analyze covering spaces and classify by subgroups.

### `/algebraic-topology homology <space>`
Compute singular homology groups.

### `/algebraic-topology cohomology <space>`
Compute cohomology and cup product structure.

### `/algebraic-topology exact-sequence <diagram>`
Apply long exact sequences (pair, Mayer-Vietoris).

### `/algebraic-topology homotopy <maps>`
Analyze homotopy equivalences and retracts.

---

## Methodology

### Fundamental Group Computation Pipeline

```
FUNDAMENTAL GROUP COMPUTATION
═══════════════════════════════════════════════════════════════

STEP 1: IDENTIFY SPACE TYPE
─────────────────────────────────────────
□ Simply connected → π₁ = 0
□ Known space → Use table
□ Decomposable → Van Kampen
□ Has nice cover → Covering space method

KNOWN π₁ VALUES
─────────────────────────────────────────
π₁(ℝⁿ) = 0
π₁(Sⁿ) = 0 for n ≥ 2
π₁(S¹) ≅ ℤ
π₁(T²) ≅ ℤ × ℤ
π₁(ℝPⁿ) ≅ ℤ/2ℤ
π₁(S¹ ∨ S¹) ≅ F₂ (free group)
π₁(Σ_g) = ⟨a₁,b₁,...,a_g,b_g | [a₁,b₁]⋯[a_g,b_g]⟩

VAN KAMPEN THEOREM
═══════════════════════════════════════════════════════════════

SETUP
─────────────────────────────────────────
X = U ∪ V with U, V, U ∩ V open, path connected, x₀ ∈ U ∩ V

STATEMENT
─────────────────────────────────────────
π₁(X, x₀) ≅ π₁(U) *_{π₁(U∩V)} π₁(V)

(Amalgamated free product)

SPECIAL CASES
─────────────────────────────────────────
□ U ∩ V simply connected:
  π₁(X) ≅ π₁(U) * π₁(V) (free product)

□ V simply connected:
  π₁(X) ≅ π₁(U) / N
  where N = normal closure of i_*(π₁(U ∩ V))

APPLICATION TEMPLATE
─────────────────────────────────────────
1. Decompose X = U ∪ V appropriately
2. Verify U, V, U ∩ V path connected
3. Compute π₁(U), π₁(V), π₁(U ∩ V)
4. Identify inclusion homomorphisms
5. Compute amalgamated product / quotient
```

### Covering Space Pipeline

```
COVERING SPACE ANALYSIS
═══════════════════════════════════════════════════════════════

DEFINITION VERIFICATION
─────────────────────────────────────────
p: E → B is covering map if:
  Every b ∈ B has evenly covered neighborhood U:
    p⁻¹(U) = ∐ Vᵢ with p|_{Vᵢ}: Vᵢ → U homeomorphism

STANDARD EXAMPLES
─────────────────────────────────────────
□ ℝ → S¹: t ↦ e^{2πit} (universal cover)
□ S¹ → S¹: z ↦ zⁿ (n-fold cyclic cover)
□ Sⁿ → ℝPⁿ: x ↦ [x] (2-fold cover)

LIFTING THEOREMS
═══════════════════════════════════════════════════════════════

PATH LIFTING
─────────────────────────────────────────
Given: p: E → B covering, γ: [0,1] → B path, e₀ ∈ p⁻¹(γ(0))
Conclusion: ∃! lift γ̃ with p ∘ γ̃ = γ, γ̃(0) = e₀

HOMOTOPY LIFTING
─────────────────────────────────────────
Given: H: Y × I → B homotopy, f̃₀ lift of H(·,0)
Conclusion: ∃! H̃ with p ∘ H̃ = H, H̃(·,0) = f̃₀

LIFTING CRITERION
─────────────────────────────────────────
f: (Y, y₀) → (B, b₀) lifts to E ⟺ f_*(π₁(Y)) ⊆ p_*(π₁(E))

CLASSIFICATION
═══════════════════════════════════════════════════════════════

For B "nice" (connected, locally path connected, semi-locally simply connected):

{Covering spaces of B} ↔ {Subgroups of π₁(B)}
        (E, p)         ↦     p_*(π₁(E))
     n-fold cover      ↔   index n subgroup

UNIVERSAL COVER
─────────────────────────────────────────
B̃ simply connected, covers all other covers.
π₁(B) acts on B̃ with B̃/π₁(B) ≅ B

DECK TRANSFORMATIONS
─────────────────────────────────────────
Deck(E/B) = {φ: E → E : p ∘ φ = p}

Normal cover: Deck(E/B) ≅ π₁(B)/p_*(π₁(E))
```

### Homology Computation Pipeline

```
SINGULAR HOMOLOGY COMPUTATION
═══════════════════════════════════════════════════════════════

CHAIN COMPLEX
─────────────────────────────────────────
Cₙ(X) = free abelian group on singular n-simplices
∂ₙ: Cₙ → Cₙ₋₁ boundary map
∂² = 0

Hₙ(X) = ker(∂ₙ)/im(∂ₙ₊₁) = Zₙ/Bₙ

BASIC COMPUTATIONS
─────────────────────────────────────────
H₀(X) = ℤ^{# path components}
H₁(X) ≅ π₁(X)^{ab} (abelianization)
Hₙ(pt) = 0 for n > 0
Hₙ(Sⁿ) = ℤ, Hₖ(Sⁿ) = 0 for k ≠ 0, n

COMPUTATIONAL TOOLS
═══════════════════════════════════════════════════════════════

LONG EXACT SEQUENCE OF PAIR
─────────────────────────────────────────
For pair (X, A):
  ⋯ → Hₙ(A) →^{i_*} Hₙ(X) →^{j_*} Hₙ(X,A) →^{∂} Hₙ₋₁(A) → ⋯

MAYER-VIETORIS
─────────────────────────────────────────
For X = U ∪ V:
  ⋯ → Hₙ(U∩V) → Hₙ(U) ⊕ Hₙ(V) → Hₙ(X) →^{∂} Hₙ₋₁(U∩V) → ⋯

EXCISION
─────────────────────────────────────────
If Z̄ ⊆ int(A):
  Hₙ(X \ Z, A \ Z) ≅ Hₙ(X, A)

EXACT SEQUENCE COMPUTATION
═══════════════════════════════════════════════════════════════

STRATEGY
─────────────────────────────────────────
1. Write out portion of sequence
2. Fill in known groups
3. Use exactness: im = ker at each position
4. Identify connecting homomorphisms
5. Solve for unknown groups

SPLITTING
─────────────────────────────────────────
0 → A → B → C → 0 exact and splits ⟹ B ≅ A ⊕ C

Splits if:
□ C free abelian
□ A injective (divisible)
□ Section exists
```

### Cohomology Pipeline

```
SINGULAR COHOMOLOGY
═══════════════════════════════════════════════════════════════

COCHAIN COMPLEX
─────────────────────────────────────────
Cⁿ(X; G) = Hom(Cₙ(X), G)
δⁿ: Cⁿ → Cⁿ⁺¹, (δφ)(σ) = φ(∂σ)
δ² = 0

Hⁿ(X; G) = ker(δⁿ)/im(δⁿ⁻¹)

UNIVERSAL COEFFICIENT THEOREM
─────────────────────────────────────────
0 → Ext(Hₙ₋₁(X), G) → Hⁿ(X; G) → Hom(Hₙ(X), G) → 0

For G = ℤ, free homology: Hⁿ(X) ≅ Hom(Hₙ(X), ℤ)

CUP PRODUCT
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
∪: Hᵖ(X) × Hᵍ(X) → Hᵖ⁺ᵍ(X)

H*(X) = ⊕Hⁿ(X) is graded ring

PROPERTIES
─────────────────────────────────────────
□ Associative
□ Graded commutative: α ∪ β = (-1)^{pq} β ∪ α
□ Natural: f*(α ∪ β) = f*α ∪ f*β

COHOMOLOGY RINGS
─────────────────────────────────────────
H*(Sⁿ) = ℤ[x]/(x²), |x| = n
H*(ℂPⁿ) = ℤ[x]/(x^{n+1}), |x| = 2
H*(ℝPⁿ; ℤ/2) = ℤ/2[x]/(x^{n+1}), |x| = 1
H*(T²) = ℤ[a,b]/(a², b², ab + ba), |a| = |b| = 1
```

### Homotopy Analysis Pipeline

```
HOMOTOPY EQUIVALENCE
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
f: X → Y homotopy equivalence if:
  ∃g: Y → X with g ∘ f ≃ id_X, f ∘ g ≃ id_Y

X ≃ Y (homotopy equivalent)

HOMOTOPY INVARIANCE
─────────────────────────────────────────
X ≃ Y ⟹ π_n(X) ≅ π_n(Y), H_n(X) ≅ H_n(Y)

RECOGNIZING HOMOTOPY EQUIVALENCES
─────────────────────────────────────────
□ Deformation retract: A ⊆ X deformation retract ⟹ A ≃ X
□ Contractible: X ≃ pt ⟺ id_X ≃ constant
□ CW approximation: Every space ≃ CW complex

DEFORMATION RETRACT
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
A ⊆ X is deformation retract if:
  ∃ H: X × I → X with H(x,0) = x, H(x,1) ∈ A, H(a,t) = a ∀a ∈ A

EXAMPLES
─────────────────────────────────────────
□ ℝⁿ \ {0} deformation retracts to Sⁿ⁻¹
□ Möbius band deformation retracts to S¹
□ Solid torus deformation retracts to S¹
□ Punctured plane ℝ² \ {0} ≃ S¹

VERIFICATION STRATEGY
─────────────────────────────────────────
Construct explicit homotopy H(x,t) with required properties.
Often: H(x,t) = (1-t)x + t·r(x) where r is retraction.
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Notes |
|--------------|---------------|-------|
| π₁ computation | algebraic-topologist | Van Kampen, covers |
| Homology | algebraic-topologist | Exact sequences |
| Cohomology ring | algebraic-topologist | Cup product |
| Point-set topology | general-topologist | Compactness, etc. |
| Manifold structure | differential-geometer | Smoothness |

---

## Output Format

### Fundamental Group Computation
```
FUNDAMENTAL GROUP: π₁(X)
═══════════════════════════════════════════════════════════════

SPACE DESCRIPTION
─────────────────────────────────────────
[Definition of X]

DECOMPOSITION
─────────────────────────────────────────
X = U ∪ V where:
  U = [description]
  V = [description]
  U ∩ V = [description]

COMPONENT π₁'S
─────────────────────────────────────────
π₁(U) = [group]
π₁(V) = [group]
π₁(U ∩ V) = [group]

VAN KAMPEN APPLICATION
─────────────────────────────────────────
[Amalgamated product computation]

RESULT
─────────────────────────────────────────
π₁(X) ≅ [group with presentation]
```

### Homology Computation
```
HOMOLOGY: H_*(X)
═══════════════════════════════════════════════════════════════

SPACE DESCRIPTION
─────────────────────────────────────────
[Definition of X]

METHOD
─────────────────────────────────────────
[Mayer-Vietoris / Exact sequence / Direct]

COMPUTATION
─────────────────────────────────────────
[Long exact sequence with computations]

RESULT
─────────────────────────────────────────
H₀(X) = [group]
H₁(X) = [group]
H₂(X) = [group]
⋮
Hₙ(X) = 0 for n > [dimension]
```

---

## Examples

### Example: Compute π₁(S¹ ∨ S¹)

```
/algebraic-topology fundamental-group "S¹ ∨ S¹"

FUNDAMENTAL GROUP: π₁(S¹ ∨ S¹)
═══════════════════════════════════════════════════════════════

SPACE DESCRIPTION
─────────────────────────────────────────
S¹ ∨ S¹ = figure eight (wedge of two circles at basepoint)

DECOMPOSITION (Van Kampen)
─────────────────────────────────────────
Let x₀ be wedge point.

U = S¹ ∨ S¹ \ {point on first circle}
  ≃ S¹ (second circle with whisker)

V = S¹ ∨ S¹ \ {point on second circle}
  ≃ S¹ (first circle with whisker)

U ∩ V ≃ ℝ (open arc around wedge point)

COMPONENT π₁'S
─────────────────────────────────────────
π₁(U) ≅ ℤ = ⟨b⟩
π₁(V) ≅ ℤ = ⟨a⟩
π₁(U ∩ V) = 0 (contractible)

VAN KAMPEN APPLICATION
─────────────────────────────────────────
Since U ∩ V simply connected:
  π₁(S¹ ∨ S¹) ≅ π₁(U) * π₁(V)
              ≅ ℤ * ℤ
              = F₂

RESULT
─────────────────────────────────────────
π₁(S¹ ∨ S¹) ≅ F₂ (free group on 2 generators)

Generators: [a] = loop around first circle
            [b] = loop around second circle

No relations between a and b.
```

### Example: Compute H_*(S²)

```
/algebraic-topology homology "S²"

HOMOLOGY: H_*(S²)
═══════════════════════════════════════════════════════════════

METHOD: Mayer-Vietoris

DECOMPOSITION
─────────────────────────────────────────
S² = U ∪ V where:
  U = S² \ {north pole} ≃ ℝ² ≃ pt
  V = S² \ {south pole} ≃ ℝ² ≃ pt
  U ∩ V = S² \ {N, S} ≃ S¹ × ℝ ≃ S¹

MAYER-VIETORIS SEQUENCE
─────────────────────────────────────────
⋯ → Hₙ(U∩V) → Hₙ(U) ⊕ Hₙ(V) → Hₙ(S²) → Hₙ₋₁(U∩V) → ⋯

For n = 2:
  H₂(S¹) → H₂(pt) ⊕ H₂(pt) → H₂(S²) → H₁(S¹) → H₁(pt) ⊕ H₁(pt)
     0    →       0         → H₂(S²) →    ℤ    →       0

Exactness: H₂(S²) →^{≅} ℤ

For n = 1:
  H₁(S¹) → H₁(pt) ⊕ H₁(pt) → H₁(S²) → H₀(S¹) → H₀(pt) ⊕ H₀(pt)
     ℤ    →       0         → H₁(S²) →    ℤ    →     ℤ ⊕ ℤ

Map ℤ → ℤ ⊕ ℤ is x ↦ (x, x), injective.
So H₁(S²) = 0.

RESULT
─────────────────────────────────────────
H₀(S²) = ℤ   (connected)
H₁(S²) = 0
H₂(S²) = ℤ   (generator: fundamental class)
Hₙ(S²) = 0   for n > 2
```

---

## References

- Hatcher, A. (2002). Algebraic Topology
- Munkres, J.R. (1984). Elements of Algebraic Topology
- Spanier, E. (1966). Algebraic Topology
- May, J.P. (1999). A Concise Course in Algebraic Topology

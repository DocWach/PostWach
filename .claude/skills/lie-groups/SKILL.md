# Lie Groups Skill

## Overview

This skill provides methodology for Lie group analysis, including structure theory, representation theory, and harmonic analysis. It coordinates with the lie-group-theorist agent.

## Invocation

```
/lie-groups [subcommand] [arguments]
```

## Subcommands

### `/lie-groups structure <group>`
Analyze Lie group structure (topology, Lie algebra).

### `/lie-groups exponential <algebra-element>`
Compute exponential map.

### `/lie-groups representation <group> <weight>`
Analyze representation.

### `/lie-groups decomposition <group>`
Compute structural decompositions (Cartan, Iwasawa).

### `/lie-groups subgroup <group> <subalgebra>`
Analyze connected Lie subgroup.

### `/lie-groups character <representation>`
Compute character formula.

---

## Methodology

### Lie Group Analysis

```
LIE GROUP ANALYSIS
═══════════════════════════════════════════════════════════════

STEP 1: TOPOLOGICAL PROPERTIES
─────────────────────────────────────────
- Dimension
- Connected components
- Simply connected?
- Compact?

STEP 2: LIE ALGEBRA
─────────────────────────────────────────
Compute 𝔤 = T_e G
Identify brackets, structure constants
Classify algebra type

STEP 3: EXPONENTIAL MAP
─────────────────────────────────────────
exp: 𝔤 → G
Determine: surjective? covering properties?

STEP 4: SUBGROUPS
─────────────────────────────────────────
- Maximal torus (compact case)
- Cartan subgroup
- Maximal compact (noncompact case)
```

### Representation Theory

```
REPRESENTATION THEORY
═══════════════════════════════════════════════════════════════

COMPACT GROUP
─────────────────────────────────────────
1. Find maximal torus T
2. Weight lattice Λ ⊂ 𝔱*
3. Dominant weights Λ⁺
4. Irreducibles ↔ Λ⁺

CHARACTER
─────────────────────────────────────────
χ_λ(t) = Σ_{w∈W} det(w) · e^{w(λ+ρ)} / Σ_{w∈W} det(w) · e^{w(ρ)}

DIMENSION
─────────────────────────────────────────
dim V_λ = ∏_{α>0} ⟨λ+ρ, α⟩ / ⟨ρ, α⟩
```

---

## Output Format

### Lie Group Report
```
LIE GROUP ANALYSIS
═══════════════════════════════════════════════════════════════

GROUP
─────────────────────────────────────────
[Definition]

TOPOLOGY
─────────────────────────────────────────
Dimension: [dim]
Connected: [yes/no]
Simply connected: [yes/no]
Compact: [yes/no]

LIE ALGEBRA
─────────────────────────────────────────
[Description and type]

STRUCTURE
─────────────────────────────────────────
[Decompositions, subgroups]

REPRESENTATIONS
─────────────────────────────────────────
[Classification]
```

---

## Examples

### Example: SO(3) Analysis

```
/lie-groups structure "SO(3)"

LIE GROUP ANALYSIS: SO(3)
═══════════════════════════════════════════════════════════════

GROUP
─────────────────────────────────────────
SO(3) = {A ∈ M₃(ℝ) : AᵀA = I, det(A) = 1}
= rotations of ℝ³

TOPOLOGY
─────────────────────────────────────────
Dimension: 3
Connected: Yes
Simply connected: No (π₁ = ℤ/2)
Compact: Yes
Homeomorphic to ℝP³

LIE ALGEBRA
─────────────────────────────────────────
𝔰𝔬(3) = {X ∈ M₃(ℝ) : Xᵀ = -X}
= skew-symmetric 3×3 matrices
Type: Simple (A₁ = B₁ = C₁)

EXPONENTIAL MAP
─────────────────────────────────────────
exp: 𝔰𝔬(3) → SO(3) is surjective
Rodrigues formula:
exp(θ n̂×) = I + sin(θ)(n̂×) + (1-cos θ)(n̂×)²

UNIVERSAL COVER
─────────────────────────────────────────
SU(2) → SO(3) is 2:1 cover
Spin(3) = SU(2)

REPRESENTATIONS
─────────────────────────────────────────
Irreducibles: V_ℓ for ℓ = 0, 1, 2, ...
dim V_ℓ = 2ℓ + 1
(integer spin only; half-integer spin lifts to SU(2))
```

### Example: Decomposition of SL(2,ℝ)

```
/lie-groups decomposition "SL(2,ℝ)"

DECOMPOSITION: SL(2,ℝ)
═══════════════════════════════════════════════════════════════

GROUP
─────────────────────────────────────────
SL(2,ℝ) = {A ∈ M₂(ℝ) : det(A) = 1}

CARTAN DECOMPOSITION
─────────────────────────────────────────
𝔤 = 𝔨 ⊕ 𝔭

𝔨 = 𝔰𝔬(2) = {(0  -θ)}  (compact part)
              {(θ   0)}

𝔭 = {(a   b)}  (noncompact part)
    {(b  -a)}

G = K · exp(𝔭) where K = SO(2)

IWASAWA DECOMPOSITION
─────────────────────────────────────────
G = KAN

K = SO(2) = {(cos θ  -sin θ)}
            {(sin θ   cos θ)}

A = {(a    0  )} for a > 0
    {(0   1/a)}

N = {(1  x)} for x ∈ ℝ
    {(0  1)}

Every g ∈ SL(2,ℝ) uniquely: g = kan
```

---

## References

- Knapp, A.W. (2002). Lie Groups Beyond an Introduction
- Hall, B.C. (2015). Lie Groups, Lie Algebras, and Representations
- Bröcker & tom Dieck (1985). Representations of Compact Lie Groups

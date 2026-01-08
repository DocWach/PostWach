# Abstract Algebra Skill

## Overview

This skill provides methodology for abstract algebraic investigations across group theory, ring theory, field theory, and module theory. It coordinates specialized algebra agents to solve problems about algebraic structures and their homomorphisms.

## Invocation

```
/abstract-algebra [subcommand] [arguments]
```

## Subcommands

### `/abstract-algebra group <specification>`
Analyze a group: structure, subgroups, quotients, representations.

### `/abstract-algebra ring <specification>`
Analyze a ring: ideals, quotients, properties.

### `/abstract-algebra field <specification>`
Analyze a field extension: degree, Galois group, splitting fields.

### `/abstract-algebra module <specification>`
Analyze a module: structure, decomposition, properties.

### `/abstract-algebra homomorphism <map>`
Analyze a homomorphism: kernel, image, isomorphism theorems.

### `/abstract-algebra classify <structure>`
Classify algebraic structures of given type.

---

## Methodology

### Group Analysis Pipeline

```
GROUP STRUCTURE ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: Group G (given by presentation, generators, or multiplication table)

STEP 1: BASIC PROPERTIES
─────────────────────────────────────────
□ Order |G| (finite or infinite)
□ Abelian? (check ab = ba)
□ Cyclic? (single generator)
□ Center Z(G) = {g : gx = xg ∀x}
□ Commutator subgroup G' = [G,G]

STEP 2: SUBGROUP STRUCTURE
─────────────────────────────────────────
□ Find all subgroups (for small groups)
□ Normal subgroups
□ Sylow p-subgroups (for finite groups)
□ Maximal subgroups

STEP 3: QUOTIENT STRUCTURE
─────────────────────────────────────────
For each normal N ⊴ G:
  □ Form G/N
  □ Identify isomorphism type
  □ Build composition series

STEP 4: CLASSIFICATION
─────────────────────────────────────────
□ Compare to known groups
□ Apply structure theorems
□ For abelian: fundamental theorem
□ For finite: use Sylow analysis
```

### Sylow Analysis Pipeline

```
SYLOW THEOREM APPLICATION
═══════════════════════════════════════════════════════════════

INPUT: Finite group G with |G| = p₁^{a₁} · p₂^{a₂} · ... · pₖ^{aₖ}

FOR EACH PRIME p DIVIDING |G|:
─────────────────────────────────────────
1. Sylow subgroups exist of order p^a

2. Count n_p = # of Sylow p-subgroups
   Constraints:
   □ n_p ≡ 1 (mod p)
   □ n_p | |G|/p^a

3. Determine possibilities for n_p

4. If n_p = 1:
   □ Unique Sylow p-subgroup P
   □ P is normal in G

5. Analyze structure implications

EXAMPLE: |G| = 12 = 2² · 3
─────────────────────────────────────────
n_3: divides 4, ≡ 1 (mod 3) → n_3 ∈ {1, 4}
n_2: divides 3, ≡ 1 (mod 2) → n_2 ∈ {1, 3}

If n_3 = 1: Normal subgroup of order 3
If n_2 = 1: Normal subgroup of order 4
```

### Ring Analysis Pipeline

```
RING STRUCTURE ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: Ring R

STEP 1: BASIC PROPERTIES
─────────────────────────────────────────
□ Commutative?
□ Has identity?
□ Characteristic
□ Zero divisors?
□ Units R*

STEP 2: CLASSIFY RING TYPE
─────────────────────────────────────────
Check hierarchy:
  Field ⊂ Division Ring ⊂ Domain ⊂ Ring

For domains:
  Field ⊂ Euclidean ⊂ PID ⊂ UFD ⊂ Domain

For noncommutative:
  Division ring? Simple? Semisimple?

STEP 3: IDEAL STRUCTURE
─────────────────────────────────────────
□ Find prime ideals
□ Find maximal ideals
□ Principal ideals?
□ Noetherian? Artinian?

STEP 4: SPECIAL ANALYSIS
─────────────────────────────────────────
Commutative:
  □ Spec(R), Max(R)
  □ Localization at primes
  □ Nilradical, Jacobson radical

Noncommutative:
  □ J(R) Jacobson radical
  □ Simple modules
  □ Wedderburn decomposition
```

### Field Extension Analysis Pipeline

```
FIELD EXTENSION ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: Extension K/F

STEP 1: DEGREE COMPUTATION
─────────────────────────────────────────
□ [K:F] = dim_F(K)
□ For K = F(α): [K:F] = deg(min_α)
□ Tower law: [L:F] = [L:K][K:F]

STEP 2: EXTENSION TYPE
─────────────────────────────────────────
□ Algebraic or transcendental?
□ Finite or infinite degree?
□ Simple extension? K = F(α)?
□ Normal? (splitting field)
□ Separable? (distinct roots)

STEP 3: GALOIS ANALYSIS
─────────────────────────────────────────
If K/F is Galois (normal + separable):

1. Compute Gal(K/F)
   □ Automorphisms fixing F
   □ |Gal(K/F)| = [K:F]

2. Subfield correspondence
   □ Subgroups H ≤ Gal(K/F) ↔ Intermediate fields
   □ K^H = fixed field of H
   □ [K:K^H] = |H|, [K^H:F] = [G:H]

3. Normal subgroups
   □ H ⊴ G iff K^H/F is Galois
   □ Gal(K^H/F) ≅ G/H

STEP 4: SPLITTING FIELD CONSTRUCTION
─────────────────────────────────────────
For f(x) ∈ F[x]:
  □ Factor f over F
  □ Adjoin roots iteratively
  □ K = F(α₁, ..., αₙ) where αᵢ are roots
  □ [K:F] divides n!
```

### Module Analysis Pipeline

```
MODULE STRUCTURE ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: R-module M

STEP 1: BASIC PROPERTIES
─────────────────────────────────────────
□ Finitely generated?
□ Free? (has basis)
□ Cyclic? M = Rm
□ Torsion elements?
□ Annihilator Ann(M)

STEP 2: SUBMODULE STRUCTURE
─────────────────────────────────────────
□ Find submodules
□ Simple submodules (no proper nonzero subs)
□ Maximal submodules
□ Socle (sum of simple submodules)

STEP 3: DECOMPOSITION
─────────────────────────────────────────
Direct sum decomposition:
  □ Indecomposable factors
  □ For semisimple: M = ⊕ simple modules
  □ For f.g. abelian groups: ℤ/n₁ ⊕ ... ⊕ ℤ/nₖ ⊕ ℤʳ

STEP 4: SPECIAL MODULE TYPES
─────────────────────────────────────────
□ Projective: direct summand of free
□ Injective: Ext¹(−, M) = 0
□ Flat: tensoring preserves exactness
□ Noetherian: ACC on submodules
□ Artinian: DCC on submodules
```

### Isomorphism Theorem Application

```
HOMOMORPHISM ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: Homomorphism φ: G → H (groups, rings, or modules)

STEP 1: COMPUTE KERNEL AND IMAGE
─────────────────────────────────────────
ker(φ) = {g ∈ G : φ(g) = e_H}
im(φ) = {φ(g) : g ∈ G}

STEP 2: FIRST ISOMORPHISM THEOREM
─────────────────────────────────────────
G/ker(φ) ≅ im(φ)

This identifies:
  □ Structure of quotient
  □ Structure of image

STEP 3: ADDITIONAL ISOMORPHISM THEOREMS
─────────────────────────────────────────
Second: For subgroups H, N with N normal:
  HN/N ≅ H/(H ∩ N)

Third: For N ⊆ H both normal in G:
  (G/N)/(H/N) ≅ G/H

Correspondence: Normal subgroups of G/N ↔
                Normal subgroups of G containing N
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Supporting Agents |
|--------------|---------------|-------------------|
| Group structure | group-theorist | - |
| Representations | group-theorist | linear-algebraist |
| Ring ideals | ring-theorist | commutative-algebraist |
| Modules | ring-theorist | linear-algebraist |
| Field extensions | field-theorist | group-theorist (Galois) |
| Commutative rings | commutative-algebraist | - |

### Workflow: Galois Theory Problem

```
1. field-theorist
   └─ Identify extension, check normality/separability

2. group-theorist
   └─ Analyze Galois group structure

3. field-theorist
   └─ Apply correspondence theorem

4. Synthesis
   └─ Complete solution with intermediate fields
```

### Workflow: Ring Classification

```
1. ring-theorist OR commutative-algebraist
   └─ Identify ring properties (commutativity, etc.)

2. Appropriate specialist
   └─ Detailed structure analysis

3. Classification
   └─ Place in hierarchy, identify isomorphism type
```

---

## Structure Theorems Reference

### Fundamental Theorem of Finite Abelian Groups
```
Every finite abelian group G decomposes uniquely:
  G ≅ ℤ/n₁ × ℤ/n₂ × ... × ℤ/nₖ
where n₁ | n₂ | ... | nₖ (invariant factors)

Equivalently:
  G ≅ ℤ/p₁^{a₁} × ℤ/p₂^{a₂} × ... × ℤ/pₘ^{aₘ}
(elementary divisors)
```

### Classification of Groups of Small Order
```
|G| = 1: {e}
|G| = 2: ℤ₂
|G| = 3: ℤ₃
|G| = 4: ℤ₄, ℤ₂ × ℤ₂
|G| = 5: ℤ₅
|G| = 6: ℤ₆, S₃
|G| = 7: ℤ₇
|G| = 8: ℤ₈, ℤ₄ × ℤ₂, ℤ₂³, D₄, Q₈
```

### Wedderburn-Artin Theorem
```
R is semisimple iff:
  R ≅ Mₙ₁(D₁) × Mₙ₂(D₂) × ... × Mₙₖ(Dₖ)
where Dᵢ are division rings.
```

### Fundamental Theorem of Galois Theory
```
For Galois extension K/F:
  { Intermediate fields E } ←→ { Subgroups H ≤ Gal(K/F) }

  E ↦ Gal(K/E)
  K^H ↤ H

  [K:E] = |Gal(K/E)|
  [E:F] = [G:Gal(K/E)]
```

---

## Output Format

### Structure Analysis
```
ALGEBRAIC STRUCTURE ANALYSIS
═══════════════════════════════════════════════════════════════

STRUCTURE: [Name/Description]

BASIC PROPERTIES
─────────────────────────────────────────
[List of properties]

SUBSTRUCTURE ANALYSIS
─────────────────────────────────────────
[Subgroups/ideals/submodules]

CLASSIFICATION
─────────────────────────────────────────
[Identification with known structures]
```

### Galois Analysis
```
GALOIS EXTENSION ANALYSIS
═══════════════════════════════════════════════════════════════

EXTENSION: K/F

DEGREE: [K:F] = n

GALOIS GROUP
─────────────────────────────────────────
Gal(K/F) ≅ [Group identification]

INTERMEDIATE FIELDS
─────────────────────────────────────────
[List with corresponding subgroups]

LATTICE DIAGRAM
─────────────────────────────────────────
[Visual representation]
```

---

## Examples

### Example 1: Classify groups of order 15

```
/abstract-algebra classify "groups of order 15"

CLASSIFICATION
═══════════════════════════════════════════════════════════════

ORDER: |G| = 15 = 3 · 5

SYLOW ANALYSIS
─────────────────────────────────────────
n₃: divides 5, ≡ 1 (mod 3) → n₃ = 1
n₅: divides 3, ≡ 1 (mod 5) → n₅ = 1

Both Sylow subgroups are unique, hence normal.

STRUCTURE
─────────────────────────────────────────
P₃ ⊴ G, |P₃| = 3, P₃ ≅ ℤ₃
P₅ ⊴ G, |P₅| = 5, P₅ ≅ ℤ₅

P₃ ∩ P₅ = {e}
G = P₃P₅ ≅ P₃ × P₅ ≅ ℤ₃ × ℤ₅ ≅ ℤ₁₅

CONCLUSION
─────────────────────────────────────────
There is exactly ONE group of order 15:
  G ≅ ℤ₁₅ (cyclic)
```

### Example 2: Galois group of x⁴ - 2 over ℚ

```
/abstract-algebra field "splitting field of x^4 - 2 over Q"

GALOIS ANALYSIS
═══════════════════════════════════════════════════════════════

POLYNOMIAL: f(x) = x⁴ - 2 ∈ ℚ[x]

ROOTS
─────────────────────────────────────────
α = ⁴√2 (real fourth root)
Roots: α, -α, iα, -iα
     = ⁴√2, -⁴√2, i⁴√2, -i⁴√2

SPLITTING FIELD
─────────────────────────────────────────
K = ℚ(⁴√2, i)
[K:ℚ] = [ℚ(⁴√2, i):ℚ(⁴√2)][ℚ(⁴√2):ℚ] = 2 · 4 = 8

GALOIS GROUP
─────────────────────────────────────────
|Gal(K/ℚ)| = 8

Generators:
  σ: ⁴√2 ↦ i⁴√2, i ↦ i  (order 4)
  τ: ⁴√2 ↦ ⁴√2, i ↦ -i  (order 2, complex conjugation)

Relations: τστ = σ³

Gal(K/ℚ) ≅ D₄ (dihedral group of order 8)

INTERMEDIATE FIELDS
─────────────────────────────────────────
ℚ ⊂ ℚ(√2) ⊂ ℚ(⁴√2) ⊂ K
ℚ ⊂ ℚ(i) ⊂ K
ℚ ⊂ ℚ(i√2) ⊂ K
```

---

## References

- Dummit, D.S. & Foote, R.M. - Abstract Algebra
- Lang, S. - Algebra
- Hungerford, T.W. - Algebra
- Jacobson, N. - Basic Algebra I & II

# Category Theory Skill

## Overview

This skill provides methodology for categorical reasoning and constructions. It covers categories, functors, natural transformations, limits, adjunctions, and universal properties. The skill coordinates with the category-theorist agent for comprehensive categorical analysis.

## Invocation

```
/category-theory [subcommand] [arguments]
```

## Subcommands

### `/category-theory category <specification>`
Analyze a category: objects, morphisms, composition, special properties.

### `/category-theory functor <specification>`
Analyze a functor: covariance, preservation properties.

### `/category-theory natural <transformation>`
Analyze a natural transformation: components, naturality.

### `/category-theory limit <diagram>`
Compute limits or colimits of diagrams.

### `/category-theory adjunction <pair>`
Analyze an adjunction: unit, counit, universal property.

### `/category-theory yoneda <application>`
Apply Yoneda lemma or embedding.

---

## Methodology

### Category Analysis Pipeline

```
CATEGORY ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: Category C

STEP 1: BASIC STRUCTURE
─────────────────────────────────────────
□ Objects: Ob(C) - what are the objects?
□ Morphisms: Hom(A,B) for each pair A,B
□ Composition: ∘ : Hom(B,C) × Hom(A,B) → Hom(A,C)
□ Identities: id_A ∈ Hom(A,A) for each A

STEP 2: VERIFY AXIOMS
─────────────────────────────────────────
□ Associativity: (h ∘ g) ∘ f = h ∘ (g ∘ f)
□ Identity: id_B ∘ f = f = f ∘ id_A for f: A → B

STEP 3: SPECIAL MORPHISMS
─────────────────────────────────────────
□ Isomorphisms: f with two-sided inverse
□ Monomorphisms: f ∘ g = f ∘ h ⟹ g = h
□ Epimorphisms: g ∘ f = h ∘ f ⟹ g = h
□ Sections/retractions

STEP 4: SPECIAL OBJECTS
─────────────────────────────────────────
□ Initial object: Unique morphism I → A for all A
□ Terminal object: Unique morphism A → T for all A
□ Zero object: Both initial and terminal
□ Group objects, ring objects (if applicable)

STEP 5: CATEGORY PROPERTIES
─────────────────────────────────────────
□ Small: Ob(C) is a set
□ Locally small: Each Hom(A,B) is a set
□ Has products/coproducts?
□ Complete/cocomplete?
□ Abelian? Topos?
```

### Functor Analysis Pipeline

```
FUNCTOR ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: Functor F: C → D

STEP 1: BASIC DATA
─────────────────────────────────────────
□ Domain category C
□ Codomain category D
□ Object map: A ↦ F(A)
□ Morphism map: (f: A → B) ↦ (F(f): F(A) → F(B))

STEP 2: VARIANCE CHECK
─────────────────────────────────────────
Covariant: F(f): F(A) → F(B) for f: A → B
Contravariant: F(f): F(B) → F(A) for f: A → B
  (Equivalently: F: C^op → D)

STEP 3: FUNCTOR AXIOMS
─────────────────────────────────────────
□ F(id_A) = id_{F(A)}
□ F(g ∘ f) = F(g) ∘ F(f) (covariant)
         or = F(f) ∘ F(g) (contravariant)

STEP 4: FUNCTOR PROPERTIES
─────────────────────────────────────────
□ Faithful: Hom(A,B) → Hom(FA,FB) injective
□ Full: Hom(A,B) → Hom(FA,FB) surjective
□ Fully faithful: Full and faithful (embedding)
□ Essentially surjective: Every D ∈ D iso to some F(C)

STEP 5: PRESERVATION
─────────────────────────────────────────
□ Preserves limits? (right adjoints do)
□ Preserves colimits? (left adjoints do)
□ Preserves monos/epis?
□ Preserves specific structures?

EQUIVALENCE CHECK
─────────────────────────────────────────
F is equivalence iff:
  □ Full and faithful
  □ Essentially surjective

C ≃ D (equivalent categories)
```

### Natural Transformation Pipeline

```
NATURAL TRANSFORMATION
═══════════════════════════════════════════════════════════════

INPUT: α: F ⟹ G where F, G: C → D

STEP 1: COMPONENT DATA
─────────────────────────────────────────
For each A ∈ Ob(C):
  α_A: F(A) → G(A) in D

STEP 2: NATURALITY CHECK
─────────────────────────────────────────
For each f: A → B in C, verify:

  F(A) --α_A--> G(A)
    |            |
  F(f)         G(f)
    ↓            ↓
  F(B) --α_B--> G(B)

commutes: G(f) ∘ α_A = α_B ∘ F(f)

STEP 3: SPECIAL PROPERTIES
─────────────────────────────────────────
□ Natural isomorphism: Each α_A is isomorphism
□ Component-wise: [Property] if each α_A has [property]

FUNCTOR CATEGORY
─────────────────────────────────────────
[C, D] = category where:
  Objects: Functors C → D
  Morphisms: Natural transformations
  Composition: (β ∘ α)_A = β_A ∘ α_A
```

### Limit/Colimit Pipeline

```
LIMITS AND COLIMITS
═══════════════════════════════════════════════════════════════

LIMIT OF DIAGRAM D: J → C
─────────────────────────────────────────
lim D is object L with cone (π_j: L → D(j))_{j∈J}

Universal property:
  For any cone (f_j: X → D(j))_{j∈J},
  exists unique u: X → L with π_j ∘ u = f_j for all j.

      X
     /|\
    / | \
   /  u  \
  ↙   ↓   ↘
D(j)← L →D(k)

COLIMIT OF DIAGRAM D: J → C
─────────────────────────────────────────
colim D is object C with cocone (ι_j: D(j) → C)_{j∈J}

Universal property:
  For any cocone (f_j: D(j) → X)_{j∈J},
  exists unique u: C → X with u ∘ ι_j = f_j for all j.

COMMON LIMITS
─────────────────────────────────────────
□ Terminal object: Limit of empty diagram
□ Product A × B: Limit of discrete {A, B}
□ Equalizer: Limit of A ⇉ B (parallel pair)
□ Pullback: Limit of A → C ← B

COMMON COLIMITS
─────────────────────────────────────────
□ Initial object: Colimit of empty diagram
□ Coproduct A ∐ B: Colimit of discrete {A, B}
□ Coequalizer: Colimit of A ⇉ B
□ Pushout: Colimit of A ← C → B

LIMIT PRESERVATION
─────────────────────────────────────────
Right adjoints preserve all limits.
Left adjoints preserve all colimits.
```

### Adjunction Pipeline

```
ADJUNCTION ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: Functors F: C → D and G: D → C

ADJUNCTION F ⊣ G
─────────────────────────────────────────
Natural bijection:
  Hom_D(F(A), B) ≅ Hom_C(A, G(B))

F is left adjoint, G is right adjoint.

UNIT AND COUNIT
─────────────────────────────────────────
Unit η: Id_C ⟹ G ∘ F
  η_A: A → G(F(A))

Counit ε: F ∘ G ⟹ Id_D
  ε_B: F(G(B)) → B

TRIANGLE IDENTITIES
─────────────────────────────────────────
(εF) ∘ (Fη) = id_F:

F(A) --F(η_A)--> F(G(F(A))) --ε_{F(A)}--> F(A) = id_{F(A)}

(Gε) ∘ (ηG) = id_G:

G(B) --η_{G(B)}--> G(F(G(B))) --G(ε_B)--> G(B) = id_{G(B)}

VERIFICATION CHECKLIST
─────────────────────────────────────────
□ Natural bijection exists
□ Unit natural transformation
□ Counit natural transformation
□ Triangle identities satisfied

UNIVERSAL PROPERTY FORM
─────────────────────────────────────────
F(A) → B corresponds to A → G(B):
  Given f: F(A) → B, get f̃ = G(f) ∘ η_A: A → G(B)
  Given g: A → G(B), get ĝ = ε_B ∘ F(g): F(A) → B
```

### Yoneda Pipeline

```
YONEDA LEMMA
═══════════════════════════════════════════════════════════════

REPRESENTABLE FUNCTORS
─────────────────────────────────────────
h^A = Hom_C(A, −): C → Set (covariant)
h_A = Hom_C(−, A): C^op → Set (contravariant)

YONEDA LEMMA STATEMENT
─────────────────────────────────────────
For F: C → Set and A ∈ C:

Nat(h^A, F) ≅ F(A)

The bijection:
  α: h^A ⟹ F  ↦  α_A(id_A) ∈ F(A)

Inverse:
  x ∈ F(A)  ↦  α where α_B(f) = F(f)(x)

YONEDA EMBEDDING
─────────────────────────────────────────
y: C → [C^op, Set]
y(A) = h_A = Hom(−, A)
y(f: A → B) = f ∘ − : Hom(−, A) ⟹ Hom(−, B)

PROPERTIES
─────────────────────────────────────────
□ y is full and faithful
□ C embeds into its presheaf category
□ h^A ≅ h^B ⟹ A ≅ B (objects determined by morphisms)

APPLICATIONS
─────────────────────────────────────────
□ Proving isomorphisms by showing representability
□ Universal properties via natural transformations
□ Density theorem constructions
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Supporting Agents |
|--------------|---------------|-------------------|
| Category structure | category-theorist | - |
| Abelian categories | category-theorist | commutative-algebraist |
| Topos theory | category-theorist | set-theorist |
| Module categories | ring-theorist | category-theorist |
| Galois connections | order-theorist | category-theorist |

### Workflow: Prove Universal Property

```
1. Identify the construction
   └─ What limit/colimit or adjunction?

2. State the universal property
   └─ Existence and uniqueness conditions

3. Verify universality
   └─ For any other candidate, unique morphism exists

4. Apply Yoneda if needed
   └─ Reduce to representability question
```

---

## Common Categories Reference

```
FUNDAMENTAL CATEGORIES
═══════════════════════════════════════════════════════════════

Set: Sets and functions
  □ Complete and cocomplete
  □ Cartesian closed
  □ Well-pointed

Grp: Groups and homomorphisms
  □ Has all limits and colimits
  □ Not abelian

Ab: Abelian groups and homomorphisms
  □ Abelian category
  □ Has tensor product ⊗

Vect_k: k-vector spaces and linear maps
  □ Abelian category
  □ Semisimple

Top: Topological spaces and continuous maps
  □ Complete and cocomplete
  □ Not Cartesian closed

Ring: Rings and ring homomorphisms
  □ Has all limits
  □ Coproduct = tensor product

Cat: Small categories and functors
  □ Complete and cocomplete
  □ Cartesian closed

IMPORTANT FUNCTORS
═══════════════════════════════════════════════════════════════

Forgetful functors: Grp → Set, Ring → Ab, Top → Set
Free functors: Set → Grp, Set → Vect_k

Hom functors: Hom(A, −), Hom(−, B)
Tensor functors: − ⊗ M

Nerve and realization: Cat ⇄ sSet
```

---

## Output Format

### Category Description
```
CATEGORY ANALYSIS
═══════════════════════════════════════════════════════════════

CATEGORY: [Name]

OBJECTS
─────────────────────────────────────────
[Description of objects]

MORPHISMS
─────────────────────────────────────────
[Description of morphisms]

COMPOSITION
─────────────────────────────────────────
[How composition works]

SPECIAL PROPERTIES
─────────────────────────────────────────
[Complete, abelian, etc.]
```

### Adjunction Analysis
```
ADJUNCTION
═══════════════════════════════════════════════════════════════

F ⊣ G
F: C → D (left adjoint)
G: D → C (right adjoint)

NATURAL BIJECTION
─────────────────────────────────────────
Hom_D(F(A), B) ≅ Hom_C(A, G(B))

UNIT
─────────────────────────────────────────
η_A: A → G(F(A))
[Description]

COUNIT
─────────────────────────────────────────
ε_B: F(G(B)) → B
[Description]
```

---

## Examples

### Example 1: Free-Forgetful Adjunction

```
/category-theory adjunction "Free ⊣ Forgetful for groups"

ADJUNCTION ANALYSIS
═══════════════════════════════════════════════════════════════

FUNCTORS
─────────────────────────────────────────
F: Set → Grp (Free group functor)
U: Grp → Set (Forgetful functor)

ADJUNCTION: F ⊣ U

NATURAL BIJECTION
─────────────────────────────────────────
Hom_Grp(F(S), G) ≅ Hom_Set(S, U(G))

Group homomorphisms from free group on S
correspond to
Set functions from S into underlying set of G.

UNIT
─────────────────────────────────────────
η_S: S → U(F(S))
Inclusion of generators into free group.

For s ∈ S, η_S(s) = s as element of F(S).

COUNIT
─────────────────────────────────────────
ε_G: F(U(G)) → G
Evaluation map: Send generators to themselves.

For g ∈ U(G), word in F(U(G)) evaluates to product in G.

UNIVERSAL PROPERTY
─────────────────────────────────────────
F(S) is the free group on S:
  For any function f: S → U(G),
  exists unique group homomorphism f̃: F(S) → G
  such that U(f̃) ∘ η_S = f.

      S ---η_S---> U(F(S))
       \           |
        f         U(f̃)
         \         |
          ↘        ↓
            U(G) = U(G)
```

### Example 2: Product as Limit

```
/category-theory limit "product of A and B"

PRODUCT AS LIMIT
═══════════════════════════════════════════════════════════════

DIAGRAM
─────────────────────────────────────────
J = {•, •} (discrete two-object category)
D: J → C with D(•₁) = A, D(•₂) = B

CONE OVER D
─────────────────────────────────────────
Cone from X: Pair of morphisms (f: X → A, g: X → B)

(No compatibility conditions since J is discrete)

LIMIT = PRODUCT
─────────────────────────────────────────
A × B with projections π₁: A × B → A, π₂: A × B → B

UNIVERSAL PROPERTY
─────────────────────────────────────────
For any (f: X → A, g: X → B),
exists unique ⟨f, g⟩: X → A × B
such that π₁ ∘ ⟨f, g⟩ = f and π₂ ∘ ⟨f, g⟩ = g.

         X
        /|\
       f | g
      /  |  \
     ↓   ↓   ↓
     A ← A×B → B
       π₁   π₂

IN Set
─────────────────────────────────────────
A × B = {(a, b) : a ∈ A, b ∈ B}
π₁(a, b) = a
π₂(a, b) = b
⟨f, g⟩(x) = (f(x), g(x))
```

---

## References

- Mac Lane, S. - Categories for the Working Mathematician
- Awodey, S. - Category Theory
- Riehl, E. - Category Theory in Context
- Leinster, T. - Basic Category Theory

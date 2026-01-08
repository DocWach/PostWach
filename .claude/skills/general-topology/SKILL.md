# General Topology Skill

## Overview

This skill provides methodology for rigorous general topology including topological spaces, continuity, compactness, connectedness, and separation axioms. It coordinates with the general-topologist agent for point-set topology analysis.

## Invocation

```
/general-topology [subcommand] [arguments]
```

## Subcommands

### `/general-topology space <specification>`
Analyze topological space properties (Hausdorff, compactness, connectedness).

### `/general-topology continuous <function>`
Verify continuity and analyze properties of maps.

### `/general-topology compact <space>`
Analyze compactness using open cover arguments.

### `/general-topology connected <space>`
Analyze connectedness and path connectedness.

### `/general-topology homeomorphism <spaces>`
Determine if spaces are homeomorphic.

### `/general-topology product <spaces>`
Analyze product and quotient topologies.

---

## Methodology

### Topological Space Analysis Pipeline

```
TOPOLOGICAL SPACE VERIFICATION
═══════════════════════════════════════════════════════════════

STEP 1: VERIFY TOPOLOGY AXIOMS
─────────────────────────────────────────
Check collection τ satisfies:
□ ∅, X ∈ τ
□ Arbitrary unions preserve openness
□ Finite intersections preserve openness

STEP 2: IDENTIFY BASE
─────────────────────────────────────────
Base B generates τ if:
□ B covers X
□ ∀B₁, B₂ ∈ B, ∀x ∈ B₁ ∩ B₂, ∃B₃ ∈ B: x ∈ B₃ ⊆ B₁ ∩ B₂

Common bases:
□ Open balls (metric spaces)
□ Open intervals (ℝ)
□ Products of open sets (product spaces)

STEP 3: COMPUTE INTERIOR/CLOSURE
─────────────────────────────────────────
int(A) = {x : ∃ open U, x ∈ U ⊆ A}
cl(A) = {x : every neighborhood of x meets A}
∂A = cl(A) \ int(A)

x ∈ cl(A) ⟺ ∀ open U ∋ x, U ∩ A ≠ ∅
```

### Continuity Verification Pipeline

```
CONTINUITY ANALYSIS
═══════════════════════════════════════════════════════════════

METHOD 1: PREIMAGE OF OPEN SETS
─────────────────────────────────────────
f: X → Y continuous ⟺ f⁻¹(V) open in X for all V open in Y

VERIFICATION STRATEGY
─────────────────────────────────────────
1. Take arbitrary open V ⊆ Y
2. Compute f⁻¹(V) = {x ∈ X : f(x) ∈ V}
3. Show f⁻¹(V) is union of basic open sets

METHOD 2: NEIGHBORHOOD CRITERION
─────────────────────────────────────────
f continuous at x₀ ⟺
  ∀ neighborhood V of f(x₀), f⁻¹(V) is neighborhood of x₀

METHOD 3: CLOSURE/INTERIOR
─────────────────────────────────────────
f continuous ⟺ f(cl(A)) ⊆ cl(f(A)) for all A
           ⟺ f⁻¹(int(B)) ⊆ int(f⁻¹(B)) for all B

HOMEOMORPHISM VERIFICATION
═══════════════════════════════════════════════════════════════

f: X → Y is homeomorphism if:
□ f is bijective
□ f is continuous
□ f⁻¹ is continuous (equivalently: f is open map)

STRATEGY
─────────────────────────────────────────
1. Construct explicit bijection
2. Verify continuity of f
3. Verify either:
   - f⁻¹ continuous, or
   - f maps open sets to open sets
```

### Compactness Analysis Pipeline

```
COMPACTNESS VERIFICATION
═══════════════════════════════════════════════════════════════

DEFINITION METHOD
─────────────────────────────────────────
X compact: Every open cover has finite subcover

PROOF STRUCTURE
─────────────────────────────────────────
1. Let {Uα} be open cover of X
2. [Construct finite subcover]
3. Conclude X compact

COMMON STRATEGIES
─────────────────────────────────────────
□ Heine-Borel (ℝⁿ): Compact ⟺ closed and bounded
□ Finite intersection property:
  Compact ⟺ every collection of closed sets with FIP has nonempty intersection
□ Sequential (metric): Compact ⟺ every sequence has convergent subsequence

COMPACTNESS PROPERTIES
─────────────────────────────────────────
□ Closed subset of compact → compact
□ Compact subset of Hausdorff → closed
□ Continuous image of compact → compact
□ Product of compact → compact (Tychonoff)

LOCAL COMPACTNESS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
X locally compact at x: ∃ compact K containing neighborhood of x
X locally compact: locally compact at every point

CHARACTERIZATION (Hausdorff)
─────────────────────────────────────────
Locally compact Hausdorff ⟺
  Every point has neighborhood base of compact sets

ONE-POINT COMPACTIFICATION
─────────────────────────────────────────
X* = X ∪ {∞} with:
□ Old open sets remain open
□ {∞} ∪ (X \ K) open for K compact

X* Hausdorff ⟺ X locally compact Hausdorff
```

### Connectedness Analysis Pipeline

```
CONNECTEDNESS VERIFICATION
═══════════════════════════════════════════════════════════════

DEFINITION METHOD
─────────────────────────────────────────
X connected: X ≠ U ∪ V for disjoint nonempty open U, V

EQUIVALENT CONDITIONS
─────────────────────────────────────────
□ Only clopen sets are ∅ and X
□ Every continuous f: X → {0,1} is constant
□ Not union of two disjoint nonempty closed sets

PROOF STRATEGIES
─────────────────────────────────────────
Method 1: Suppose X = U ∪ V (separation), derive contradiction
Method 2: Use f: X → {0,1} continuous, show constant
Method 3: Show every pair of points connected by chain

DISCONNECTION PROOF
─────────────────────────────────────────
To show X disconnected:
  Exhibit explicit separation X = U ∪ V

PATH CONNECTEDNESS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
X path connected: ∀x,y ∈ X, ∃ continuous γ: [0,1] → X
                  with γ(0) = x, γ(1) = y

RELATIONSHIPS
─────────────────────────────────────────
Path connected ⟹ connected
Converse: False in general (topologist's sine curve)
           True for open subsets of ℝⁿ

LOCAL CONNECTEDNESS
─────────────────────────────────────────
X locally connected: Has base of connected open sets
X locally path connected: Has base of path connected open sets

Locally path connected + connected ⟹ path connected
```

### Separation Axioms Pipeline

```
SEPARATION AXIOM VERIFICATION
═══════════════════════════════════════════════════════════════

T₀ (KOLMOGOROV)
─────────────────────────────────────────
∀ distinct x, y: ∃ open U containing exactly one

Verify: For each pair, find separating open set

T₁ (FRÉCHET)
─────────────────────────────────────────
∀ distinct x, y: ∃ open U with x ∈ U, y ∉ U

Equivalent: Points are closed

T₂ (HAUSDORFF)
─────────────────────────────────────────
∀ distinct x, y: ∃ disjoint open U, V with x ∈ U, y ∈ V

Consequences:
□ Limits unique
□ Compact sets closed
□ Diagonal closed in X × X

T₃ (REGULAR)
─────────────────────────────────────────
T₁ + ∀ closed F, x ∉ F: ∃ disjoint open U, V with x ∈ U, F ⊆ V

T₃½ (COMPLETELY REGULAR/TYCHONOFF)
─────────────────────────────────────────
T₁ + ∀ closed F, x ∉ F: ∃ continuous f: X → [0,1]
                        with f(x) = 0, f(F) = {1}

T₄ (NORMAL)
─────────────────────────────────────────
T₁ + ∀ disjoint closed E, F: ∃ disjoint open U, V
                              with E ⊆ U, F ⊆ V

KEY THEOREMS
═══════════════════════════════════════════════════════════════

URYSOHN'S LEMMA
─────────────────────────────────────────
X normal, E, F disjoint closed:
  ∃ continuous f: X → [0,1] with f(E) = 0, f(F) = 1

TIETZE EXTENSION
─────────────────────────────────────────
X normal, A closed, f: A → ℝ continuous:
  ∃ continuous F: X → ℝ extending f
```

### Product and Quotient Topology Pipeline

```
PRODUCT TOPOLOGY
═══════════════════════════════════════════════════════════════

FINITE PRODUCTS
─────────────────────────────────────────
X × Y has base: {U × V : U open in X, V open in Y}

Projections πₓ, πᵧ are continuous and open.

UNIVERSAL PROPERTY
─────────────────────────────────────────
f: Z → X × Y continuous ⟺ πₓ ∘ f and πᵧ ∘ f continuous

INFINITE PRODUCTS
─────────────────────────────────────────
∏Xᵢ has subbase: {πᵢ⁻¹(U) : U open in Xᵢ}

Basic open: Finitely many coordinates restricted

TYCHONOFF'S THEOREM
─────────────────────────────────────────
Arbitrary product of compact spaces is compact
(Product topology essential; fails for box topology)

QUOTIENT TOPOLOGY
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
For surjection q: X → Y:
  V ⊆ Y open ⟺ q⁻¹(V) open in X

q is quotient map (continuous, surjective, saturated open sets map to open)

CONSTRUCTION
─────────────────────────────────────────
Given equivalence relation ~ on X:
  X/~ = {[x] : x ∈ X}
  q: X → X/~, q(x) = [x]

EXAMPLES
─────────────────────────────────────────
□ [0,1]/{0,1} ≅ S¹ (circle)
□ ℝ/ℤ ≅ S¹
□ S²/(x ~ -x) = ℝP²
□ D²/S¹ ≅ S² (collapse boundary)
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Notes |
|--------------|---------------|-------|
| Point-set topology | general-topologist | Spaces, continuity |
| Fundamental group | algebraic-topologist | π₁, covering spaces |
| Homology | algebraic-topologist | Chain complexes |
| Manifold topology | differential-geometer | Charts, smoothness |

---

## Output Format

### Topological Property Verification
```
TOPOLOGICAL ANALYSIS: X
═══════════════════════════════════════════════════════════════

SPACE DESCRIPTION
─────────────────────────────────────────
[Definition of X]

COMPACTNESS
─────────────────────────────────────────
[Analysis and conclusion]

CONNECTEDNESS
─────────────────────────────────────────
[Analysis and conclusion]

SEPARATION AXIOMS
─────────────────────────────────────────
T₀: [Yes/No]
T₁: [Yes/No]
T₂ (Hausdorff): [Yes/No]
T₃ (Regular): [Yes/No]
T₄ (Normal): [Yes/No]

SUMMARY
─────────────────────────────────────────
[Key properties]
```

### Homeomorphism Proof
```
HOMEOMORPHISM: X ≅ Y
═══════════════════════════════════════════════════════════════

MAP DEFINITION
─────────────────────────────────────────
f: X → Y, f(x) = [formula]

BIJECTIVITY
─────────────────────────────────────────
[Injective and surjective verification]

CONTINUITY OF f
─────────────────────────────────────────
[Preimage argument]

CONTINUITY OF f⁻¹
─────────────────────────────────────────
[Preimage argument or open map]

CONCLUSION
─────────────────────────────────────────
X ≅ Y via f.  □
```

---

## Examples

### Example: Show [0,1] is compact

```
/general-topology compact "[0,1]"

COMPACTNESS PROOF: [0,1]
═══════════════════════════════════════════════════════════════

CLAIM: [0,1] is compact.

METHOD: Heine-Borel

PROOF
─────────────────────────────────────────
[0,1] ⊆ ℝ is:
□ Closed: Contains all limit points
□ Bounded: Contained in [-1, 2]

By Heine-Borel theorem, closed and bounded subsets of ℝ are compact.

Therefore [0,1] is compact.  □

ALTERNATIVE (Direct)
─────────────────────────────────────────
Let {Uα} be open cover of [0,1].

Let S = {x ∈ [0,1] : [0,x] covered by finitely many Uα}.

S nonempty: 0 ∈ some Uα, so Uα contains [0,ε) for some ε.

Let s = sup S.

Claim: s = 1 and s ∈ S.

s ∈ some Uβ. Since Uβ open, (s-δ, s+δ) ⊆ Uβ for some δ.
By def of sup, ∃x ∈ S with x > s - δ.
[0,x] has finite subcover, so [0, min(1, s+δ)] has finite subcover.
Thus s = 1 and 1 ∈ S.

Therefore [0,1] compact.  □
```

### Example: Prove ℝ is connected

```
/general-topology connected "ℝ"

CONNECTEDNESS PROOF: ℝ
═══════════════════════════════════════════════════════════════

CLAIM: ℝ is connected.

PROOF
─────────────────────────────────────────
Suppose ℝ = U ∪ V where U, V disjoint, nonempty, open.

Choose a ∈ U, b ∈ V with a < b (WLOG).

Let c = sup(U ∩ [a,b]).

Since U open: c ∉ U (else (c-ε, c+ε) ⊆ U, contradicting supremum)
Since V open: c ∉ V (else (c-ε, c) ∩ U = ∅, contradicting supremum)

Contradiction: c ∈ ℝ = U ∪ V but c ∉ U and c ∉ V.

Therefore ℝ is connected.  □

COROLLARY
─────────────────────────────────────────
Connected subsets of ℝ are exactly the intervals.
```

---

## References

- Munkres, J.R. (2000). Topology
- Willard, S. (2004). General Topology
- Engelking, R. (1989). General Topology
- Kelley, J.L. (1955). General Topology

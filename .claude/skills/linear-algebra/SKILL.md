# Linear Algebra Skill

## Overview

This skill provides methodology for linear algebraic computations and theory. It covers vector spaces, linear transformations, matrices, eigentheory, inner product spaces, and canonical forms. The skill coordinates with the linear-algebraist agent for comprehensive analysis.

## Invocation

```
/linear-algebra [subcommand] [arguments]
```

## Subcommands

### `/linear-algebra matrix <operation> <matrix>`
Perform matrix operations: determinant, inverse, rank, etc.

### `/linear-algebra eigen <matrix>`
Compute eigenvalues, eigenvectors, and analyze diagonalizability.

### `/linear-algebra decompose <type> <matrix>`
Compute matrix decompositions: LU, QR, SVD, Jordan, etc.

### `/linear-algebra solve <system>`
Solve systems of linear equations.

### `/linear-algebra space <specification>`
Analyze vector space: basis, dimension, subspaces.

### `/linear-algebra transform <specification>`
Analyze linear transformation: kernel, image, matrix representation.

---

## Methodology

### Matrix Analysis Pipeline

```
MATRIX ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: m × n matrix A over field F

STEP 1: BASIC PROPERTIES
─────────────────────────────────────────
□ Size: m × n
□ Rank: dim(col space) = dim(row space)
□ Nullity: dim(ker A)
□ Rank + Nullity = n (number of columns)

STEP 2: SQUARE MATRIX PROPERTIES (if m = n)
─────────────────────────────────────────
□ Determinant
□ Invertibility (det ≠ 0)
□ Trace: tr(A) = Σaᵢᵢ
□ Characteristic polynomial: det(tI - A)

STEP 3: SPECIAL STRUCTURE
─────────────────────────────────────────
□ Symmetric: A = Aᵀ
□ Hermitian: A = A*
□ Orthogonal: AAᵀ = I
□ Unitary: AA* = I
□ Normal: AA* = A*A
□ Nilpotent: Aᵏ = 0 for some k
□ Idempotent: A² = A
```

### Row Reduction Pipeline

```
GAUSSIAN ELIMINATION
═══════════════════════════════════════════════════════════════

INPUT: Augmented matrix [A|b] for system Ax = b

ALGORITHM
─────────────────────────────────────────
1. Forward elimination (to row echelon form)
   FOR each column c from left to right:
     □ Find pivot (first nonzero entry in column below current row)
     □ Swap rows to bring pivot to current row
     □ Scale pivot row to make pivot = 1
     □ Eliminate entries below pivot

2. Back substitution (to reduced row echelon form)
   FOR each pivot from bottom to top:
     □ Eliminate entries above pivot

OUTPUT
─────────────────────────────────────────
□ RREF (Reduced Row Echelon Form)
□ Pivot positions → basic variables
□ Non-pivot columns → free variables
□ Solution set parametrization
```

### Eigenvalue Pipeline

```
EIGENVALUE ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: n × n matrix A

STEP 1: CHARACTERISTIC POLYNOMIAL
─────────────────────────────────────────
p(t) = det(tI - A)

Compute by cofactor expansion or other methods.

p(t) = tⁿ - tr(A)tⁿ⁻¹ + ... + (-1)ⁿdet(A)

STEP 2: FIND EIGENVALUES
─────────────────────────────────────────
Eigenvalues = roots of p(t)

For each eigenvalue λ:
  □ Algebraic multiplicity = multiplicity as root of p(t)

STEP 3: FIND EIGENVECTORS
─────────────────────────────────────────
For each eigenvalue λ:
  □ Solve (A - λI)x = 0
  □ E_λ = ker(A - λI) = eigenspace
  □ Geometric multiplicity = dim(E_λ)

STEP 4: DIAGONALIZABILITY CHECK
─────────────────────────────────────────
A is diagonalizable iff:
  □ Sum of geometric multiplicities = n
  □ Equivalently: geometric mult = algebraic mult for all λ

If diagonalizable:
  A = PDP⁻¹
  P = [eigenvector columns]
  D = diag(λ₁, ..., λₙ)

SPECIAL CASES
─────────────────────────────────────────
□ n distinct eigenvalues ⟹ diagonalizable
□ Symmetric real ⟹ diagonalizable (orthogonally)
□ Normal ⟹ unitarily diagonalizable
```

### Jordan Form Pipeline

```
JORDAN CANONICAL FORM
═══════════════════════════════════════════════════════════════

INPUT: n × n matrix A over algebraically closed field

SETUP
─────────────────────────────────────────
For each eigenvalue λ:
  □ Algebraic multiplicity = aₗ
  □ Compute null spaces: ker(A - λI)ᵏ for k = 1, 2, ...

GENERALIZED EIGENSPACE
─────────────────────────────────────────
Vₗ = ker(A - λI)^{aₗ} = generalized eigenspace
dim(Vₗ) = aₗ

JORDAN BLOCK STRUCTURE
─────────────────────────────────────────
For eigenvalue λ:
  dₖ = dim ker(A - λI)ᵏ - dim ker(A - λI)^{k-1}

Number of Jordan blocks of size ≥ k = dₖ - d_{k+1}
Number of Jordan blocks total = d₁ = geometric multiplicity

JORDAN CHAIN CONSTRUCTION
─────────────────────────────────────────
For each Jordan block of size m:
  □ Find v with (A - λI)^m v = 0, (A - λI)^{m-1} v ≠ 0
  □ Chain: v, (A-λI)v, ..., (A-λI)^{m-1}v

OUTPUT
─────────────────────────────────────────
A = PJP⁻¹ where J = diag(J_{n₁}(λ₁), ..., J_{nₖ}(λₖ))

Jordan block: J_m(λ) = [λ 1 0 ··· 0]
                       [0 λ 1 ··· 0]
                       [⋮     ⋱    ]
                       [0 0 ··· λ 1]
                       [0 0 ··· 0 λ]
```

### Inner Product Space Pipeline

```
INNER PRODUCT ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT: Inner product space (V, ⟨·,·⟩)

ORTHOGONALIZATION (GRAM-SCHMIDT)
─────────────────────────────────────────
Input: Basis {v₁, v₂, ..., vₙ}
Output: Orthonormal basis {e₁, e₂, ..., eₙ}

Algorithm:
  u₁ = v₁
  uₖ = vₖ - Σᵢ<ₖ proj_{uᵢ}(vₖ)
     = vₖ - Σᵢ<ₖ (⟨vₖ,uᵢ⟩/⟨uᵢ,uᵢ⟩)uᵢ

  eₖ = uₖ/‖uₖ‖

ORTHOGONAL COMPLEMENT
─────────────────────────────────────────
For subspace W ⊆ V:
  W⊥ = {v ∈ V : ⟨v,w⟩ = 0 ∀w ∈ W}

V = W ⊕ W⊥ (orthogonal direct sum)
dim(W) + dim(W⊥) = dim(V)

PROJECTION
─────────────────────────────────────────
Orthogonal projection onto W:
  proj_W(v) = Σᵢ ⟨v,eᵢ⟩eᵢ
where {e₁,...,eₖ} is orthonormal basis for W.

Matrix form: P = A(AᵀA)⁻¹Aᵀ where columns of A span W.
```

### Spectral Theorem Pipeline

```
SPECTRAL THEOREM APPLICATION
═══════════════════════════════════════════════════════════════

FOR REAL SYMMETRIC MATRIX A = Aᵀ
─────────────────────────────────────────
1. All eigenvalues are real
2. Eigenvectors for distinct eigenvalues are orthogonal
3. A = QDQᵀ where:
   □ Q orthogonal (QQᵀ = I)
   □ D diagonal with eigenvalues
   □ Columns of Q = orthonormal eigenvectors

FOR HERMITIAN MATRIX A = A*
─────────────────────────────────────────
Same as above with:
  □ Q unitary (QQ* = I)
  □ All eigenvalues real

FOR NORMAL MATRIX (AA* = A*A)
─────────────────────────────────────────
A = UDU* where:
  □ U unitary
  □ D diagonal (possibly complex)
  □ Eigenvalues may be complex

APPLICATIONS
─────────────────────────────────────────
□ Positive definite: All eigenvalues > 0
□ Positive semidefinite: All eigenvalues ≥ 0
□ Quadratic forms: xᵀAx classification
```

### Singular Value Decomposition Pipeline

```
SINGULAR VALUE DECOMPOSITION
═══════════════════════════════════════════════════════════════

INPUT: m × n matrix A (real or complex)

CONSTRUCTION
─────────────────────────────────────────
1. Form A*A (n × n, positive semidefinite)
2. Find eigenvalues λ₁ ≥ λ₂ ≥ ... ≥ λₙ ≥ 0
3. Singular values: σᵢ = √λᵢ
4. Right singular vectors: vᵢ = eigenvectors of A*A
5. Left singular vectors: uᵢ = (1/σᵢ)Avᵢ (for σᵢ ≠ 0)
6. Complete to orthonormal bases

OUTPUT
─────────────────────────────────────────
A = UΣV*

U: m × m unitary (columns = left singular vectors)
Σ: m × n diagonal (σ₁, σ₂, ..., σᵣ, 0, ..., 0)
V: n × n unitary (columns = right singular vectors)

PROPERTIES
─────────────────────────────────────────
□ rank(A) = number of nonzero singular values
□ ‖A‖₂ = σ₁ (operator norm)
□ ‖A‖_F = √(Σσᵢ²) (Frobenius norm)
□ Condition number κ(A) = σ₁/σᵣ

APPLICATIONS
─────────────────────────────────────────
□ Pseudoinverse: A⁺ = VΣ⁺U*
□ Low-rank approximation: Keep top k singular values
□ Principal Component Analysis (PCA)
□ Least squares solution
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Supporting Agents |
|--------------|---------------|-------------------|
| Matrix computations | linear-algebraist | - |
| Vector spaces | linear-algebraist | - |
| Eigentheory | linear-algebraist | - |
| Modules over rings | ring-theorist | linear-algebraist |
| Representations | group-theorist | linear-algebraist |
| Numerical methods | numerical-analyst | linear-algebraist |

### Workflow: Complete Matrix Analysis

```
1. Basic properties
   └─ Size, rank, determinant, trace

2. Eigenanalysis
   └─ Characteristic polynomial, eigenvalues, eigenvectors

3. Canonical form
   ├─ If diagonalizable → diagonal form
   └─ Otherwise → Jordan form

4. Structure analysis
   └─ Special properties (symmetric, normal, etc.)

5. Decompositions
   └─ Relevant decompositions (SVD, QR, etc.)
```

---

## Output Format

### Matrix Properties
```
MATRIX ANALYSIS
═══════════════════════════════════════════════════════════════

MATRIX A = [entries]

PROPERTIES
─────────────────────────────────────────
Size: m × n
Rank: r
Nullity: n - r
Determinant: [if square]
Trace: [if square]

SPECIAL STRUCTURE
─────────────────────────────────────────
[Symmetric, orthogonal, etc.]
```

### Eigenanalysis
```
EIGENVALUE ANALYSIS
═══════════════════════════════════════════════════════════════

CHARACTERISTIC POLYNOMIAL
─────────────────────────────────────────
p(t) = [polynomial]

EIGENVALUES
─────────────────────────────────────────
λ₁ = [value], algebraic mult = [a], geometric mult = [g]
λ₂ = ...

EIGENVECTORS
─────────────────────────────────────────
E_{λ₁}: basis = {[vectors]}
...

DIAGONALIZATION
─────────────────────────────────────────
[Diagonalizable or not, with explanation]
[If yes: P and D matrices]
```

### Decomposition
```
MATRIX DECOMPOSITION
═══════════════════════════════════════════════════════════════

DECOMPOSITION TYPE: [SVD/Jordan/QR/etc.]

COMPONENTS
─────────────────────────────────────────
[Factor matrices]

VERIFICATION
─────────────────────────────────────────
[Check that decomposition is correct]
```

---

## Examples

### Example 1: Eigenanalysis

```
/linear-algebra eigen "[[4, 1], [2, 3]]"

EIGENVALUE ANALYSIS
═══════════════════════════════════════════════════════════════

MATRIX
─────────────────────────────────────────
A = [4  1]
    [2  3]

CHARACTERISTIC POLYNOMIAL
─────────────────────────────────────────
p(t) = det(tI - A) = det([t-4  -1 ])
                         ([-2   t-3])
     = (t-4)(t-3) - 2 = t² - 7t + 10 = (t-5)(t-2)

EIGENVALUES
─────────────────────────────────────────
λ₁ = 5, algebraic multiplicity = 1
λ₂ = 2, algebraic multiplicity = 1

EIGENVECTORS
─────────────────────────────────────────
λ = 5: (A - 5I)v = 0
  [-1  1][v₁]   [0]
  [2  -2][v₂] = [0]

  v₁ = v₂, so E₅ = span{[1, 1]ᵀ}

λ = 2: (A - 2I)v = 0
  [2   1][v₁]   [0]
  [2   1][v₂] = [0]

  2v₁ + v₂ = 0, so E₂ = span{[1, -2]ᵀ}

DIAGONALIZATION
─────────────────────────────────────────
A = PDP⁻¹ where

P = [1   1]    D = [5  0]
    [1  -2]        [0  2]

Verification: PDP⁻¹ = A ✓
```

### Example 2: SVD Computation

```
/linear-algebra decompose SVD "[[1, 0], [0, 1], [1, 1]]"

SINGULAR VALUE DECOMPOSITION
═══════════════════════════════════════════════════════════════

MATRIX
─────────────────────────────────────────
A = [1  0]
    [0  1]
    [1  1]

STEP 1: COMPUTE AᵀA
─────────────────────────────────────────
AᵀA = [2  1]
      [1  2]

Eigenvalues: λ₁ = 3, λ₂ = 1
Singular values: σ₁ = √3, σ₂ = 1

STEP 2: RIGHT SINGULAR VECTORS
─────────────────────────────────────────
v₁ = (1/√2)[1, 1]ᵀ (for λ = 3)
v₂ = (1/√2)[1, -1]ᵀ (for λ = 1)

V = (1/√2)[1   1]
          [1  -1]

STEP 3: LEFT SINGULAR VECTORS
─────────────────────────────────────────
u₁ = (1/σ₁)Av₁ = (1/√6)[1, 1, 2]ᵀ
u₂ = (1/σ₂)Av₂ = (1/√2)[1, -1, 0]ᵀ
u₃ = orthogonal complement = (1/√3)[1, 1, -1]ᵀ

RESULT
─────────────────────────────────────────
A = UΣVᵀ

U = [1/√6   1/√2   1/√3]
    [1/√6  -1/√2   1/√3]
    [2/√6    0    -1/√3]

Σ = [√3  0]
    [0   1]
    [0   0]

V = [1/√2   1/√2]
    [1/√2  -1/√2]
```

---

## References

- Axler, S. - Linear Algebra Done Right
- Strang, G. - Introduction to Linear Algebra
- Horn, R.A. & Johnson, C.R. - Matrix Analysis
- Trefethen, L.N. & Bau, D. - Numerical Linear Algebra

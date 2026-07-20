# Classical Sensor / Estimation Fusion as a Candidate Morphism

**Provenance:** Claude (Anthropic, claude-sonnet-4-6), 2026-07-15.
**Status:** R016 (a) research artifact. All findings are prior-art inventory. The morphism recast is proposed new work, not established.
**Slice:** Classical sensor/estimation fusion examined as a candidate WySE morphism.
**Frame:** WySE Wymorian/DEVS+institution engine; homomorphism = structure+behavior-preserving map with graded degree (D_s structural, D_b behavioral as [0,inf]-enriched distance). Candidate E = bridge pattern (established technique instantiates the underlying morphism structure; prove correspondence or prove failure off a restriction).
**R019 Note:** All bibliographic entries marked [PLACEHOLDER] or [VERIFY] are NOT in approved.bib and MUST NOT be cited in manuscripts until verified by the Byzantine-Bayesian protocol.

---

## 1. Scope

This document inventories classical multi-sensor / estimation data fusion and assesses whether the fusion operators are homomorphisms (or functors) on the underlying dynamical systems. Coverage:

- JDL data-fusion model (Levels 0-4) and Dasarathy input/output taxonomy
- Kalman filter / Extended Kalman Filter (EKF) / Unscented Kalman Filter (UKF) and information-filter form
- Bayesian recursive estimation and particle filters
- Covariance intersection (CI) and consistent fusion under unknown correlation
- Track-to-track (T2T) fusion
- Dempster-Shafer evidence combination at the sensor level

For each family: (a) fusion map and algebraic properties; (b) canonical reference ([PLACEHOLDER] for ungrounded); (c) category/institution recast; (d) Fable-shape verdict.

---

## 2. Method Families Table

| # | Family | Fusion Map phi | Associative? | Commutativity (combine-then-estimate = estimate-then-combine)? | Reference (VERIFY) |
|---|--------|---------------|-------------|---------------------------------------------------------------|-------------------|
| F1 | JDL Model | Level-indexed aggregation pipeline | Levels are ordered, not associative across levels | No universal commuting diagram; level ordering is definitional | [PLACEHOLDER: hall1992jdl] |
| F2 | Dasarathy DAI/DAO taxonomy | I/O classification: DAI-DAO, DAI-FAO, FIO-DAO, FIO-FAO, FIO-FAO | Depends on fusion type; data-in/data-out is associative under conditions | Commutativity type-dependent; FIO-DAO commutes under linearity | [PLACEHOLDER: dasarathy1994sensor] |
| F3 | Kalman filter (linear) | x_fused = K1*x1 + K2*x2; P_fused = (P1^-1 + P2^-1)^-1 | YES: information-matrix sum P_fused^-1 = P1^-1 + P2^-1 is commutative and associative | YES under linearity + Gaussian: the information-form fusion commutes with prediction step in time-invariant case | [PLACEHOLDER: kalman1960new] |
| F4 | EKF | Linearized Kalman at operating point | NOT globally: linearization is state-dependent, order matters | FAILS globally: combine-then-linearize != linearize-then-combine in general | [PLACEHOLDER: jazwinski1970stochastic] |
| F5 | UKF | Sigma-point propagation | Associativity holds approximately for the sigma-point weighted sum | FAILS exactly: sigma-point selection depends on current state, not invariant under reordering | [PLACEHOLDER: julier1997ukf] |
| F6 | Information filter | y_fused = y1 + y2; Omega_fused = Omega1 + Omega2 (y=P^-1*x, Omega=P^-1) | YES: vector/matrix addition is commutative + associative | YES in linear case: the information-sum fusion IS the exact commutativity witness for linear Gaussian systems | [PLACEHOLDER: maybeck1979stochastic] |
| F7 | Bayesian recursive | p(x | z1, z2) proportional to p(z1|x)*p(z2|x)*p(x) (conditional independence) | YES under cond. independence: likelihood product is commutative and associative | YES under cond. independence: sequential Bayes update commutes with observation reordering | [PLACEHOLDER: jazwinski1970stochastic] |
| F8 | Particle filter (SIS/SIR) | Importance-weighted sample approximation of posterior | YES in the limit (identical distributions); sample-finite case is NOT exact | APPROXIMATE: empirical particle distribution converges to Bayesian posterior but is not algebraically commutative for finite N | [PLACEHOLDER: doucet2001sequential] |
| F9 | Covariance intersection | x_fused = Omega_ci^-1*(omega*Omega1*x1 + (1-omega)*Omega2*x2); Omega_ci = omega*Omega1 + (1-omega)*Omega2 | FAILS associativity: omega minimization for 3 sources is not equivalent to iterated 2-source CI; iterated CI is conservative but not tight | CONSERVATIVE: CI ensures consistent (non-overconfident) fusion but the resulting estimate is NOT the minimum-variance unbiased estimator; no commuting diagram with the MVUE | [PLACEHOLDER: julier1997nondivergent] |
| F10 | T2T fusion | Fused estimate from track files: x_12 = x1 + P1*(P1+P2-P12)^-1*(x2-x1) | YES when cross-covariance P12 is known; NOT in practice since P12 is usually unavailable | APPROXIMATE: T2T equation is exact only when P12=0 (independent sensors); common-process noise violates independence, making the diagram fail | [PLACEHOLDER: bar-shalom1986track] |
| F11 | Dempster-Shafer (DS) | m12(A) = sum_{B intersect C = A} m1(B)*m2(C) / K (K = 1 - sum_{B intersect C = empty} m1(B)*m2(C)) | YES: Dempster's rule is commutative; NOT fully associative when K approaches 0 (high conflict degrades normalization cascade) | STRUCTURED FAILURE: DS combination commutes at the evidence level but the evidence-to-state map (decision layer) does not commute with the combination in high-conflict regimes | [PLACEHOLDER: shafer1976mathematical] |

---

## 3. Morphism / Institution Recast

### 3.1 WySE framing

In WySE, a system z = (SZ, IZ, OZ, NZ, RZ) has signature Sigma = (sorts of states, inputs, outputs) and behavior (trajectory set under the next-state N and readout R maps). A homomorphism h: z_A -> z_B is a signature morphism plus a state map that makes the behavior-preservation diagram commute:

```
  s_A --N_A--> s_A'        s_A --h--> s_B
   |                         |          |
   h             and         N_A       N_B
   |                         |          |
  s_B --N_B--> s_B'         s_A'--h->s_B'
```

The degree (D_s, D_b) measures how far from exact the commuting is: D_s grades structural compression (signature/state coarsening), D_b grades behavioral divergence (output trajectory mismatch).

A **fusion morphism claim** is: two sensor systems z_1, z_2 with separate state spaces are fused into z_fused, and the fusion operator phi is a HOMOMORPHISM on the product system z_1 x z_2 into z_fused, meaning phi commutes with N (prediction) and R (readout).

### 3.2 Categorical framing

Objects: sensor/estimator systems with state space S, input space U, output space Y.
Morphisms: state-map + signature-map pairs (h_S, h_Sigma) satisfying behavior-preservation.
Fusion: a candidate LIMIT (product object in a category of observation functors) or a COLIMIT (pushout combining two systems sharing a common ground truth).

The categorical question for each fusion family is:

**Does fusion construct the categorical product? If so, the fusion map is universal (the unique map from any other system into the product), which is the categorical statement of "optimal fusion."**

### 3.3 Per-family recast

**F3/F6 (Kalman / Information filter, linear Gaussian):**
The information-form fusion Omega_fused = Omega_1 + Omega_2, y_fused = y_1 + y_2 is EXACTLY the coproduct of linear Gaussian likelihood functionals in the category of Gaussian measures on R^n with morphisms as linear maps. The Kalman fusion step constructs the posterior mean and covariance, which IS the categorical product of the two measurement-conditioned distributions in the Gaussian category. This is not new (it is classical MMSE theory) but provides the institutional grounding: **the Kalman information fusion is the categorical product of two Gaussian observation models, i.e., it is a limit in the category of Gaussian distributions.**

In WySE terms: the two sensor systems z_1, z_2 with linear output maps C_1, C_2 and noise covariances R_1, R_2 generate a product system z_12 whose state space is the same (shared ground truth x) and whose readout is the combined measurement [C_1; C_2]*x + [v_1; v_2]. The Kalman fusion is the minimum-variance unbiased estimator of x from the product observation -- i.e., it is the unique (up to linear equivalence) behavior-preserving map from z_12 into the MMSE estimator system. This is a behavioral homomorphism: D_b = 0 (no behavioral divergence in the linear Gaussian case), D_s measures the compression of [C_1; C_2] into the fused estimator (the quotient of the joint observation space by the fusion map).

**F7 (Bayesian recursive, conditional independence):**
Under conditional independence, p(z_1, z_2 | x) = p(z_1|x)*p(z_2|x). The joint posterior factors, making Bayesian fusion the PRODUCT of the individual posteriors (up to the common prior). In the Kleisli category of the Giry monad (Stoch), the fusion is the monoidal product of the two Markov kernels z -> Dist(Z_1) and z -> Dist(Z_2), composed with the inference kernel Dist(Z_1) x Dist(Z_2) -> Dist(S). This is a MONOIDAL morphism in Stoch under the monoidal product of measurement channels. The commutativity of the observation-ordering (F7 row in Table 2) is exactly the statement that the monoidal product in Stoch is symmetric -- a standard categorical fact.

**F9 (Covariance Intersection):**
CI is NOT a categorical product. CI constructs a CONSISTENT but suboptimal estimate: for any omega in [0,1], the CI estimate is guaranteed to have a covariance bounding the true (unknown) covariance from above. The CI fusion is a CONSERVATIVE APPROXIMATION of the Bayesian product; it lives in the category of consistent estimators (those with covariance >= true covariance) but is not the terminal object (product) in the Gaussian category. In institutional terms: CI relaxes the satisfaction condition -- it produces an estimate that satisfies the consistency constraint (a behavioral invariant) but does not achieve minimum variance (behavioral optimality). This matches the pattern of a LAX morphism in the quantitative institution: D_b(CI, Kalman) > 0 because the CI output differs from the MVUE, but the consistency constraint is preserved exactly (D_consistency = 0).

**F11 (Dempster-Shafer):**
DS fusion operates at the EVIDENCE level (Dempster-Shafer belief functions on a frame of discernment) rather than the state-space level. The DS combination rule is an operation on the power set lattice 2^Theta. In categorical terms, DS combination is a natural transformation between functors from the category of bodies of evidence to the category of belief assignments. The Dempster rule commutes with evidence-lattice reductions (reductions of the frame of discernment) ONLY in the absence of conflict (K close to 1). Under high conflict, the normalization factor K breaks the natural-transformation property: the diagram relating "reduce-then-combine" vs "combine-then-reduce" does not commute. In WySE terms: DS fusion is a homomorphism on the evidence lattice only under low-conflict restriction; it is a partial morphism that fails off a reachability condition.

**F2 (Dasarathy DAI-DAO taxonomy):**
The Dasarathy taxonomy is a CLASSIFICATION of fusion types by input-output data level, not a single algebraic operation. The DAI-DAO (data-in, data-out) class, which includes Kalman filtering operating on raw observations, is the subclass most naturally cast as a dynamical-system homomorphism: the fusion map receives raw sensor outputs (IZ) and produces fused data (OZ). The DAI-DAO class is precisely the class where the fusion operator acts at the I/O level of the WySE system, making it directly analogous to the Wymorian input/output system morphism. The other classes (DAI-FAO feature output, FIO-FAO feature in/out) operate at different levels of the WySE hierarchy: they correspond to LEVEL-CHANGING morphisms in the multi-level DEVS hierarchy.

**F1 (JDL Model):**
The JDL levels (0: subobject / signal, 1: object, 2: situation, 3: threat, 4: process refinement) are a STRATIFICATION of abstraction levels, not a single algebraic structure. Each JDL level transition is a potential level-change morphism in the DEVS multi-level hierarchy (L0 -> L1 -> ... in the WySE level index). The JDL model is the most natural host for the **candidate E bridge pattern** applied to a multi-level fusion architecture: each level-transition operator is a candidate morphism between WySE systems at adjacent levels. The claim would be: JDL Level 0->1 (signal-to-object) is a WySE level-change morphism, and fusion of JDL Level 1 tracks corresponds to the product object at Level 1.

---

## 4. Fable-Shape Candidates

Ranked by proximity to a provable claim with a computable witness.

### FC1 (STRONGEST): Kalman information fusion is the categorical product of linear Gaussian observation models

**Claim:** Let z_1 = (S, Y_1, C_1, R_1) and z_2 = (S, Y_2, C_2, R_2) be two linear-Gaussian sensor systems sharing state space S with output maps C_i and noise covariances R_i. The Kalman information-form fusion phi_K: z_1 x z_2 -> z_fused defined by Omega_fused = C_1^T R_1^-1 C_1 + C_2^T R_2^-1 C_2, y_fused = C_1^T R_1^-1 z_1 + C_2^T R_2^-1 z_2 is the UNIQUE (up to linear equivalence) morphism from the product observation system z_1 x z_2 to the minimum-variance unbiased estimator system in the [0,inf]-enriched Gaussian category. Equivalently: phi_K is a behavior-preserving WySE homomorphism with D_b = 0 and D_s = dim(null(C_fused)) / dim(S).

**Why provable:** The MVUE uniqueness is a classical result (Gauss-Markov theorem). The categorical product identification follows from the universal property: any other linear estimator mapping (z_1, z_2) to S factors through phi_K up to a linear map that increases variance (i.e., increases D_b). The D_s formula for null-space compression is computable from the matrices.

**Witness sketch:** Symbolic Python / numpy: (1) generate z_1, z_2 with random C_1, C_2, R_1, R_2; (2) compute phi_K via information sum; (3) compute the behavioral distance D_b(phi_K, phi_alt) for several alternative linear estimators phi_alt; (4) verify D_b(phi_K, phi_alt) >= 0 with equality iff phi_alt = phi_K (up to reordering); (5) compute D_s as null-space dimension ratio. SHA-stable numerical witness with floating-point tolerance check.

**Adjacency:** Direct instantiation of candidate E bridge pattern. Linear-Gaussian sensor fusion IS a WySE homomorphism; the Kalman gain is the morphism coefficient. New contribution: the explicit (D_s, D_b) coordinates of Kalman fusion in the WySE degree plane, and the proof that phi_K is the UNIQUE D_b=0 morphism (minimum behavioral divergence).

**Commutativity fact (load-bearing):** The prediction-fusion commutativity (Section 3.1 diagram) holds exactly in the linear case: phi_K commutes with the Kalman prediction step F (A matrix in z = Ax + Bu). This is the WySE behavior-preservation diagram. FAILS for EKF (FC2 below).

### FC2 (STRONG): EKF fusion is a first-order-approximate WySE homomorphism with bounded D_b

**Claim:** Let z be a nonlinear system with state transition f(x) and measurement h(x). The EKF linearizes at the current state estimate x_k: F_k = df/dx|_{x_k}, H_k = dh/dx|_{x_k}. The EKF fusion is a WySE homomorphism from the linearized system z_lin(x_k) to the fused estimator with D_b bounded by O(||delta_x||^2) where delta_x is the linearization error (second-order Taylor remainder). The diagram does NOT commute exactly: D_b(EKF) = O(||delta_x||^2) where delta_x is the deviation of the true state trajectory from the operating point.

**Why provable:** The Taylor-series bound on linearization error is classical. The WySE recast translates this into a D_b bound: the behavioral divergence between the EKF fusion output and the true posterior mean is bounded by the Hessian norm times the squared operating-point deviation. This is a graded (non-zero D_b) homomorphism, exactly the WySE degree-plane picture.

**Witness sketch:** Symbolic + numerical: (1) nonlinear system (Van der Pol or Duffing oscillator with nonlinear measurement); (2) compute EKF-fused estimate; (3) compute ground-truth posterior via high-particle particle filter; (4) measure D_b = ||x_EKF - x_PF||; (5) verify D_b = O(||delta_x||^2) by varying operating-point deviation; (6) SHA-stable sweep over delta_x grid.

**Adjacency:** Candidate E, restricted to first-order regime. New contribution: explicit (D_s, D_b(delta_x)) surface in the WySE degree plane as a function of linearization error.

### FC3 (STRONG): Bayesian fusion under conditional independence is a symmetric monoidal morphism in Stoch

**Claim:** Under the conditional independence assumption p(z_1, z_2 | x) = p(z_1|x)*p(z_2|x), Bayesian fusion is a symmetric monoidal morphism phi_B: k_1 (x) k_2 -> k_12 in the Kleisli category Stoch (Giry monad), where k_i: S -> Dist(Z_i) are the individual measurement kernels and (x) is the monoidal product of measurement channels. The commutativity of observation ordering (swapping z_1, z_2) is the symmetry natural transformation in the symmetric monoidal structure. D_b = 0, D_s = 0 under conditional independence.

**Why provable:** The symmetric monoidal structure of Stoch under the Giry monad is established prior art [VERIFY: giry1982categorical as in GAP-GIRY inventory]. The fusion-as-monoidal-product claim follows from the conditional-independence factorization. New: the WySE identification of D_s (measuring information redundancy between z_1 and z_2 when independence FAILS) as the obstruction to the monoidal morphism claim. When p(z_1, z_2 | x) != p(z_1|x)*p(z_2|x), the fusion morphism gains a non-zero D_s component recording the mutual information I(z_1; z_2 | x).

**Witness sketch:** Symbolic probability computation: (1) define bivariate Gaussian (z_1, z_2 | x) with off-diagonal covariance rho; (2) at rho=0 verify fusion factorizes (D_s=0, D_b=0); (3) at rho!=0 compute D_s as I(z_1;z_2|x) = -0.5*log(1-rho^2); (4) verify D_b(Bayes_independent, Bayes_true) grows with rho; (5) SHA-stable sweep over rho in [-1,1].

**Adjacency:** Candidate E + connects to GAP-GIRY (Giry monad / Kleisli category, continuous state). New contribution: I(z_1;z_2|x) as a WySE D_s formula for fusion under correlated noise -- measuring structural information loss when independence is assumed.

### FC4 (MODERATE): Covariance Intersection is a lax WySE morphism with bounded consistency but non-zero D_b

**Claim:** Covariance intersection phi_CI is a morphism from the product sensor system z_1 x z_2 into the consistent-estimator subcategory of the Gaussian category, with D_b(CI, MVUE) = (1/2)*tr(P_MVUE * (P_CI - P_MVUE)) >= 0 (variance excess), and D_b = 0 iff P_1, P_2 are uncorrelated (i.e., iff the full-information Kalman fusion applies). The consistency property (P_CI >= P_true) is a behavioral invariant that CI preserves exactly (D_consistency = 0), but optimality (D_b = 0) holds only in the degenerate uncorrelated case.

**Why provable:** The CI conservatism is proved in the original Julier-Uhlmann paper [VERIFY: julier1997nondivergent]. The variance-excess formula is computable. The lax-morphism interpretation: CI satisfies a WEAKENED version of the commutativity diagram (consistent, not minimum-variance). New: the (D_b, D_consistency) decomposition of CI in the WySE degree plane, where D_b measures optimality loss and D_consistency = 0 is the safety invariant.

**Witness sketch:** Numerical: (1) generate P_1, P_2 with unknown cross-covariance P_12 drawn from uniform distribution over positive-semidefinite P_12 satisfying consistency; (2) compute optimal omega; (3) measure D_b(CI, MVUE) as variance-excess trace; (4) verify D_b >= 0 always, D_b = 0 iff P_12 = 0; (5) SHA-stable sweep over P_12 values.

**Adjacency:** New candidate (not pattern E). CI is the first case where the WySE degree plane separates a SAFETY property (D_consistency = 0) from an OPTIMALITY property (D_b > 0). This is a structurally interesting Fable because it shows that the [0,inf]-enriched degree plane carries two INDEPENDENT behavioral axes for fusion operators.

### FC5 (MODERATE): Dempster-Shafer is a lattice homomorphism on the evidence power set, failing off low-conflict restriction

**Claim:** DS combination phi_DS is a homomorphism on the lattice (2^Theta, subset, union, intersection) of focal elements, with the property that phi_DS commutes with lattice reductions (coarsenings of Theta) IF AND ONLY IF the conflict measure K >= K_min for some threshold K_min > 0. Below K_min, the normalization in Dempster's rule breaks the lattice-homomorphism property: phi_DS(m_1, m_2)|_Theta' != phi_DS(m_1|_Theta', m_2|_Theta') for a coarsened frame Theta' subset Theta.

**Why provable:** The non-commutativity under high conflict is noted in critiques of DS theory [VERIFY: zadeh1986simple]. The lattice-homomorphism property under low-conflict restriction is straightforward to verify computationally. New: the explicit characterization of K_min as the threshold where the naturality square fails, and the WySE D_b formula for the naturality failure as a function of K.

**Witness sketch:** Symbolic/numerical: (1) enumerate mass assignments on frame Theta = {A, B, C}; (2) compute K for varying conflict levels; (3) coarsen to Theta' = {A, B union C}; (4) compute phi_DS before and after coarsening; (5) measure ||phi_DS full - phi_DS coarsened|| as D_b proxy; (6) verify D_b = 0 at K=1 (no conflict), D_b > 0 for K < 1, and identify K_min where D_b becomes bounded by 1/K * epsilon. SHA-stable over K grid.

**Adjacency:** New candidate. DS fusion maps to the institution-theory framework (evidence lattice as a many-sorted signature, DS rule as satisfaction condition). The restriction-to-low-conflict corresponds to the WySE reachability condition on the domain of the morphism.

### FC6 (EXPLORATORY): JDL Level 0->1 transition as a WySE level-change morphism

**Claim:** The JDL model Level 0 (sub-object / raw signal) to Level 1 (object estimate) transition is a WySE level-change morphism in the multi-level DEVS hierarchy: it maps a system at level LA (signal processing) to a system at level L0 (object tracking) with a computable D_s measuring signal-to-object information compression and D_b measuring tracking-accuracy loss. The full JDL pipeline (L0->L1->L2->L3) is a CHAIN of level-change morphisms, composable in the WySE morphism category.

**Why provable (partially):** WySE level-change morphisms are defined in the dissertation framework. The JDL level sequence respects the level ordering. The claim requires specifying concrete signal-processing and tracking algorithms to instantiate the (D_s, D_b) calculations. The Fable shape is present but requires a concrete instantiation (e.g., matched filter at L0, Kalman tracker at L1) to become computable.

**Adjacency:** Strongest connection to candidate E for multi-level architectures. JDL is the domain where multi-sensor fusion becomes explicitly level-stratified, mapping the level index directly to the WySE level hierarchy. This is a candidate for a MULTI-LEVEL Fable, extending the single-morphism FC1 claim to a chain of morphisms.

---

## 5. Refs-to-Verify ([PLACEHOLDER])

All entries below are absent from approved.bib. [PLACEHOLDER] = candidate metadata from prior knowledge; none are verified against external sources. Run refverify (Step 0 DOI check) before staging for any manuscript.

```
[PLACEHOLDER: hall1992jdl]
  Author: Hall, D.L. and Llinas, J.
  Title: An introduction to multisensor data fusion
  Venue: Proceedings of the IEEE
  Year: 1997 (often cited; original JDL model predates -- verify whether 1992 or 1997 is primary)
  Note: JDL model originated in Hall and Llinas 1997 or earlier DARPA reports; exact first publication unclear. DO NOT draft a specific year/volume without verification.

[PLACEHOLDER: dasarathy1994sensor]
  Author: Dasarathy, B.V.
  Title: Sensor fusion potential exploitation -- innovative architectures and illustrative applications
  Venue: Proceedings of the IEEE
  Year: 1997
  Note: Dasarathy taxonomy commonly cited; year and exact title unverified. [PLACEHOLDER]

[PLACEHOLDER: kalman1960new]
  Author: Kalman, R.E.
  Title: A new approach to linear filtering and prediction problems
  Venue: Journal of Basic Engineering (ASME Transactions)
  Year: 1960
  Note: Widely known classic. DOI and exact page numbers unverified for approved.bib purposes.

[PLACEHOLDER: jazwinski1970stochastic]
  Author: Jazwinski, A.H.
  Title: Stochastic Processes and Filtering Theory
  Venue: Academic Press
  Year: 1970
  Note: Standard EKF/Bayesian estimation reference. Unverified for approved.bib.

[PLACEHOLDER: julier1997ukf]
  Author: Julier, S.J. and Uhlmann, J.K.
  Title: A new extension of the Kalman filter to nonlinear systems
  Venue: Proc. SPIE 3068, Signal Processing, Sensor Fusion, and Target Recognition VI
  Year: 1997
  Note: UKF original paper. DOI and page numbers unverified.

[PLACEHOLDER: maybeck1979stochastic]
  Author: Maybeck, P.S.
  Title: Stochastic Models, Estimation, and Control (Vol. 1)
  Venue: Academic Press
  Year: 1979
  Note: Information filter derivation. Unverified for approved.bib.

[PLACEHOLDER: doucet2001sequential]
  Author: Doucet, A., de Freitas, N., and Gordon, N. (Eds.)
  Title: Sequential Monte Carlo Methods in Practice
  Venue: Springer
  Year: 2001
  Note: SIS/SIR particle filter collection. Unverified for approved.bib.

[PLACEHOLDER: julier1997nondivergent]
  Author: Julier, S.J. and Uhlmann, J.K.
  Title: A non-divergent estimation algorithm in the presence of unknown correlations
  Venue: Proc. American Control Conference
  Year: 1997
  Note: Original covariance intersection paper. DOI and page numbers unverified.

[PLACEHOLDER: bar-shalom1986track]
  Author: Bar-Shalom, Y. and Campo, L.
  Title: The effect of the common process noise on the two-sensor fused-track covariance
  Venue: IEEE Transactions on Aerospace and Electronic Systems
  Year: 1986
  Note: T2T fusion classic. Exact volume/issue unverified.

[PLACEHOLDER: shafer1976mathematical]
  Author: Shafer, G.
  Title: A Mathematical Theory of Evidence
  Venue: Princeton University Press
  Year: 1976
  Note: DS theory foundational text. Unverified for approved.bib.

[PLACEHOLDER: zadeh1986simple]
  Author: Zadeh, L.A.
  Title: A simple view of the Dempster-Shafer theory of evidence and its implication for the rule of combination
  Venue: AI Magazine
  Year: 1986
  Note: High-conflict DS critique. Exact volume/issue/pages unverified.

[PLACEHOLDER: giry1982categorical]
  Author: Giry, M.
  Title: A categorical approach to probability theory
  Venue: Lecture Notes in Mathematics 915 (Springer)
  Year: 1982
  Note: Already listed in GAP-GIRY inventory with DOI candidate 10.1007/BFb0092872. Still requires approved.bib verification.
```

---

## 6. Gaps

### G1. Commuting-diagram verification for Kalman fusion with dynamics (FC1)

FC1 establishes Kalman fusion as a product morphism on the STATIC (single time-step) observation model. The full dynamical claim requires proving that the Kalman prediction-update cycle (predict -> fuse -> update) is a COMMUTATIVE diagram in the category of linear dynamical systems, not just at one time step. The time-invariant case is almost certainly true (classical Kalman theory); the time-varying case (changing C_k, R_k) requires additional argument.

### G2. D_s formula for Kalman fusion

The D_s (structural degree) for Kalman fusion is identified as dim(null(C_fused)) / dim(S) (null-space compression), but this is a first proposal. The correct WySE D_s should track which state components are unobservable under the fused observation map C_fused = [C_1; C_2]. For fully observable systems (null(C_fused) = {0}), D_s = 0. For partially observable systems, D_s > 0. This gap is: the D_s formula needs to be derived from the WySE structural record definition (K1, K2, K3) rather than proposed directly, to ensure consistency with the existing WySE degree-plane.

### G3. Fusion under state-space mismatch

All FC1-FC4 assume sensors share a common state space S (same ground truth). In practice, sensors may observe different ASPECTS of a physical system (e.g., one observes position, another velocity); the state spaces are not identical but are related by a partial-observation map. This is the general-morphism case: z_1 and z_2 have state spaces S_1 and S_2 with a common ground-truth state x embedded via maps pi_1: X -> S_1, pi_2: X -> S_2. The fusion morphism operates in the PULLBACK of S_1 and S_2 over X. This pullback-fusion case is unexplored in the WySE frame and would extend FC1 significantly.

### G4. Particle-filter as approximate morphism with finite-N D_b

FC2 handles EKF approximation; the particle filter (F8) has a different approximation structure: the D_b grows as O(1/sqrt(N)) where N is the particle count. The WySE recast of the PF would characterize the N -> infinity limit as an exact morphism (F7, Bayesian), with finite-N D_b bounded by a CLT-type argument. This is a distinct Fable shape (resource-bounded morphism approximation) not covered in the current candidates.

### G5. T2T fusion and the common-process-noise obstruction (F10)

T2T fusion is exact only when sensor process noises are independent. When sensors share a common driving process (e.g., both track the same maneuvering target), the cross-covariance P_12 != 0 breaks the T2T formula. In WySE terms, this is a STRUCTURAL COUPLING between z_1 and z_2 that prevents them from being objects in a product diagram. The shared process noise creates a SPAN rather than a product: z_1 <- z_true -> z_2. Fusion in this case is a PULLBACK, not a product. The WySE identification of T2T failure as a pullback-vs-product mismatch is a gap.

### G6. DS under Dempster's rule vs. disjunctive rule

The inventory covers only Dempster's conjunctive rule (intersection-based). The disjunctive DS rule (union-based) has different algebraic properties (including full associativity and commutativity without the conflict normalization issue). A comparative Fable treating both rules as alternative morphisms on the evidence lattice -- one intersection-preserving, one union-preserving -- would clarify the morphism-type classification within DS theory.

### G7. JDL Level 2-4 (situation/threat assessment) as morphisms

FC6 addresses only Level 0->1. JDL Levels 2 (situation assessment) and 3 (threat assessment) involve SEMANTIC aggregation (combining object tracks into situation models) that is not naturally a state-space dynamical morphism. The Dasarathy FIO-FAO class covers this territory. Whether Level 2-4 operators are morphisms in a KNOWLEDGE REPRESENTATION category (description logic, ontology) rather than a dynamical-systems category is an open gap -- and may require the institution-theory frame (many-sorted signatures for ontological structures) rather than the DEVS frame.

---

## Appendix: Algebraic Properties Summary

| Family | Commutative? | Associative? | Has Identity? | Diagram Commutes? | Category Assignment |
|--------|-------------|-------------|--------------|-------------------|---------------------|
| Kalman info-form | YES | YES | YES (zero info) | YES (linear case) | Product in GaussianCat |
| Bayesian (cond. indep.) | YES | YES | YES (uniform prior) | YES (cond. indep.) | Monoidal product in Stoch |
| Covariance Intersection | YES | NO (iterated CI not tight) | NO | APPROXIMATELY | Lax morphism in ConsistentEstimCat |
| EKF | Order-dependent | NO | NO | APPROXIMATELY O(||delta||^2) | First-order approx morphism |
| UKF | Order-dependent | NO (sigma-point selection) | NO | APPROXIMATELY | Higher-order approx morphism |
| Dempster-Shafer | YES | YES (low conflict) / NO (high conflict) | YES (vacuous BBA) | CONDITIONALLY | Lattice hom. on BBA under K>=K_min |
| T2T (independent) | YES | YES | YES | YES (P_12=0 only) | Product in GaussianCat (restricted) |
| T2T (correlated) | YES | NO | NO | FAILS | Fails categorical product |
| Particle filter | YES (limit) | YES (limit) | YES (limit) | ASYMPTOTICALLY (N->inf) | Resource-bounded approx of Stoch |

---

*Document status: R016 (a) research artifact. Morphism recast is proposed new work; fusion techniques themselves are prior art. No approved.bib entries yet; all references are [PLACEHOLDER] pending refverify.*

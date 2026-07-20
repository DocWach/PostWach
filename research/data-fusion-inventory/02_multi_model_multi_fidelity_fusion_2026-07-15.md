# Multi-Model / Multi-Fidelity Fusion: WySE Mapping Inventory
**Slice 02 — Literature Reviewer output**
Date: 2026-07-15
Status: (a) prior-art inventory, research artifact [R016]
Strict gate: all references pass the [PLACEHOLDER] rule; no DOIs are asserted without a verified source (R019/R109).

---

## 1. Scope

This inventory maps the canonical methods for fusing two or more models into a single artifact onto the WySE conceptual frame: stratification levels, degree of structural homomorphism (D_s), Lawvere [0,inf]-enriched behavioral distance (D_b), comorphisms / institution reducts, and pedigree (provenance/fidelity lineage). The goal is to identify which fusion operators are mathematically crisp enough to support a Fable-shaped provable claim, and how each relates to the existing gluing result (Candidate D, enriched lax functor over non-disjoint interfaces) and the transfer-distance bridge (Candidate E, Cody 2021 Mesarovician transfer distance).

Honest integration status (R016): every finding below is **(a) prior-art** in the literature; no new WySE results are claimed here.

Coverage:
- Bayesian model averaging (BMA) and model mixing
- Ensemble methods, stacking, mixture-of-experts (MoE)
- Multi-fidelity modeling (co-kriging, Kennedy-O'Hagan autoregressive, multi-level Monte Carlo, control variates)
- Surrogate / reduced-order-model (ROM) fusion
- Data assimilation as model+data fusion (variational 4D-Var, ensemble Kalman)
- Model reconciliation / conflation of probability distributions

Out of scope (addressed in other slices): transfer learning per se (Slice E), model selection without fusion, pure calibration without structural coupling.

---

## 2. Method Families Table

For each family the columns are: (A) fusion operator, (B) mathematical object of the fused model, (C) canonical reference with honest confidence level, (D) pedigree / (D_s, D_b) inheritance sketch, (E) Fable-shape verdict.

---

### 2.1 Bayesian Model Averaging (BMA)

**Fusion operator.** Given models M_1,...,M_K each with likelihood p(y|M_k), and posterior model weights w_k = p(M_k|y) (normalized), BMA produces the predictive distribution:

    p(y* | y) = sum_k w_k * p(y* | M_k, y)

The "fused model" is a convex mixture of predictive distributions over a shared output space; it is not itself a state-machine tuple but a distribution over outputs.

**Mathematical object.** A convex combination (weighted sum) in the space of probability measures over the output set O_Z. In the language of probability monads, BMA is a point in the free convex combination of K probability spaces; in categorical terms, it is a colimit-like operation only if the K models share the same carrier (output type). When output types differ, it degenerates to a common projection first.

**Canonical references (assessed confidence).**
- Hoeting, J.A., Madigan, D., Raftery, A.E., Volinsky, C.T. (1999). "Bayesian Model Averaging: A Tutorial." *Statistical Science*, 14(4). [VERIFY: pages 382-401 likely but not hand-checked against source; no DOI asserted]
- Raftery, A.E., Gneiting, T., Balabdaoui, F., Polakowski, M. (2005). "Using Bayesian Model Averaging to Calibrate Forecast Ensembles." *Monthly Weather Review*, 133(5). [VERIFY: pages and DOI not asserted]
- For the probability-monad / categorical reading: Fritz, T. (2020). "A Synthetic Approach to Markov Kernels, Conditional Independence and Theorems on Sufficient Statistics." *Advances in Mathematics*. [VERIFY: volume/pages not asserted]

**WySE / pedigree mapping.**
- D_s (structural): BMA does not map state sets or transition functions; it operates on the output measure only. Formally, D_s is undefined across models unless they share a common state carrier. If the K parent models are at the same stratification level and all homomorphic to a common ground truth Z*, then the BMA output is a Kleisli extension of the output readout R_Z: the fused readout is R_fused(s) = sum_k w_k * R_{Z_k}(s), which remains well-typed only when S_k are identified. Consequence: BMA preserves D_s = min_k D_s(Z_k, Z*) in the best case (the tightest parent dominates the structural fit), but yields no inheritance law tighter than the weakest parent unless the weight w_k concentrates on the structurally best model.
- D_b (behavioral): The fused behavioral distance satisfies D_b(BMA, Z*) <= sum_k w_k * D_b(Z_k, Z*) by convexity of the Lawvere metric under convex combination. This IS a provable inheritance law (weighted triangle inequality on the mixture). Equality holds when all mass is on one model.
- Pedigree: BMA carries all parent pedigrees but is not a new structural entity; its pedigree is an evidence-weighted union. There is no "new physics" introduced; epistemic uncertainty about which parent is correct is preserved in the weights.

**Fable-shape verdict.** MODERATE. The D_b convexity bound (D_b_fused <= weighted sum of parent D_b) is a clean provable statement. Witness sketch: instantiate two Wymore tuples Z_1, Z_2 at level LA sharing output space, compute D_b by numerical trajectory comparison (as in the isomorphism-library skill), form the BMA mixture with arbitrary weights w_1=alpha, w_2=1-alpha, verify the bound holds for all alpha in [0,1]. Machine-checkable on a 1D example. Adjacency: tangent to Candidate D (shared carrier gluing) because BMA requires the carrier to be identified before the mixture is well-formed; the gluing result is the prerequisite.

---

### 2.2 Ensemble Methods, Stacking, Mixture-of-Experts (MoE)

**Fusion operator.**
- *Ensemble averaging*: unweighted (or uniformly weighted) average of K model outputs: y_fused = (1/K) sum_k y_k.
- *Stacking (super-learning)*: a meta-learner g takes the K base-model outputs as features and produces a combined output; g is trained on held-out data. Wolpert (1992) [VERIFY].
- *Mixture-of-Experts*: a gating network G(x) produces an input-dependent probability vector over K experts; y_fused = sum_k G_k(x) * y_k(x). Jacobs et al. (1991) [VERIFY].

**Mathematical object.** Stacking: composition of K readout functions with a learned aggregation; in categorical terms, a diagram of K morphisms from a common input object I to output O, postcomposed with a learned morphism g: O^K -> O. MoE: an input-conditioned mixture, which at each x is a convex combination; globally it is a soft partition of input space, each region served by one expert.

**Canonical references.**
- Jacobs, R.A., Jordan, M.I., Nowlan, S.J., Hinton, G.E. (1991). "Adaptive Mixtures of Local Experts." *Neural Computation*, 3(1). [VERIFY: pages 79-87 plausible, not asserted]
- Wolpert, D.H. (1992). "Stacked Generalization." *Neural Networks*, 5(2). [VERIFY: pages 241-259 plausible, not asserted]
- For theoretical foundations: Dietterich, T.G. (2000). "Ensemble Methods in Machine Learning." In *Proceedings of the 1st International Workshop on Multiple Classifier Systems* (MCS 2000), Springer LNCS. [VERIFY]

**WySE / pedigree mapping.**
- D_s: Stacking introduces a meta-model at a strictly higher abstraction level than any individual Z_k; the meta-model's state set is effectively {y_1,...,y_K} (the base-model output tuple), so D_s(meta, Z*) can only be computed relative to a ground-truth Z* whose inputs also include the base outputs. This is a level-crossing move: stacking lifts the problem to a new stratification level.
- D_b: For ensemble averaging, D_b inherits the same convexity bound as BMA (unweighted case: D_b_ensemble <= (1/K) sum_k D_b(Z_k, Z*)). For stacking and MoE, no clean inheritance law exists without knowing g's error; the bound becomes D_b_stacked <= D_b_meta + epsilon where epsilon accounts for the meta-learner's fit.
- Pedigree: MoE partitions pedigree by input region; the fused model's pedigree is heterogeneous in input space, with different lineages dominant in different regions. This is a richer pedigree structure than a flat mixture.

**Fable-shape verdict.** WEAK for stacking/MoE (meta-learner complicates the claim); MODERATE for uniform ensemble (same bound as BMA). MoE has a distinct attractive structure: the input-conditional gating is itself a morphism I -> Delta(K) (a distribution over experts), and the composition I -> Delta(K) x O^K -> O is a diagram in a suitable category (Kleisli of the distribution monad). Whether this is a colimit or a limit is a live question. The Fable claim would be: "The MoE fused model is a limit in the category of models with shared input/output types, along the diagram formed by the K experts and the gating morphism." This requires careful category setup and is a candidate for a new Fable thread, not adjacent to Candidates D or E but potentially upstream of both.

---

### 2.3 Multi-Fidelity Modeling

This family explicitly involves models at different stratification levels (different D_s, different abstraction), fused to get the accuracy of a high-fidelity (HF) model at the cost of a low-fidelity (LF) model.

#### 2.3.1 Kennedy-O'Hagan (KOH) Autoregressive Multi-Fidelity

**Fusion operator.** KOH models the HF output as:

    y_HF(x) = rho * y_LF(x) + delta(x)

where rho is a scaling factor and delta is an independent Gaussian process (GP) capturing the discrepancy. The fused model is a GP posterior conditioned on LF observations (cheap) and HF observations (expensive).

**Mathematical object.** A Gaussian process (i.e., a distribution over functions O_Z = R^n -> R), specifically a conditional distribution. In category-theoretic terms, this is a Kleisli morphism in the Giry monad: I -> P(O) where P is the probability-measure functor.

**Canonical reference.**
- Kennedy, M.C. and O'Hagan, A. (2000). "Predicting the Output from a Complex Computer Code When Fast Approximations Are Available." *Biometrika*, 87(1). [VERIFY: pages 1-13 plausible, no DOI asserted]

**WySE / pedigree mapping.**
- D_s: The KOH fused model inherits D_s from the HF model (it is an approximation to the HF output), but the scaling rho introduces a structural coupling: if Z_LF and Z_HF are Wymore tuples, the autoregressive link rho is a readout-rescaling, i.e., a linear map on O_Z. This is a homomorphism on the output layer only; D_s(KOH, Z_HF) < 1 unless rho=1 and delta=0 everywhere.
- D_b: The expected D_b of the KOH posterior mean to the true HF output is bounded by the GP posterior variance (the Kriging standard error). This is a direct, computable inheritance law: D_b(KOH, Z_HF) <= sqrt(posterior variance) in L2.
- Pedigree: The fused model carries a two-level pedigree: LF source (high-volume, low-fidelity runs) and HF source (low-volume, high-fidelity runs). The rho parameter quantifies the structural coupling between levels; it is the closest existing object in the fusion literature to D_s measured empirically.
- Cross-level morphism: The KOH link rho: O_LF -> O_HF (or more precisely, rho is a scalar that relates the two output carriers after alignment) is exactly a readout-layer comorphism in WySE terms. This is the sharpest connection between the multi-fidelity literature and the WySE comorphism catalog.

**Fable-shape verdict.** STRONG. Provable claim sketch: "Given Z_LF and Z_HF at stratification levels L1 < L2, with a readout comorphism phi: O_LF -> O_HF, the KOH posterior mean constitutes a well-typed element of the morphism library with D_b bounded by the GP posterior standard deviation." Witness: instantiate Z_LF as a 1-state linear model (LA level), Z_HF as the nonlinear pendulum (NL level, per the wyse-model-generation skill exercises); run KOH; compute D_b between posterior mean and true NL trajectory; verify the bound holds. This is directly adjacent to Candidate D (the "gluing" that ties LF and HF over a shared interface carrier) and may be the cleanest Fable candidate in this slice.

#### 2.3.2 Co-Kriging

**Fusion operator.** Generalization of KOH to vector-valued outputs or multiple LF models; uses a cross-covariance kernel between models at different fidelities.

**Mathematical object.** A multivariate GP with cross-covariance structure; structurally equivalent to KOH in the single-output case.

**Canonical references.**
- Cressie, N. (1993). *Statistics for Spatial Data* (revised ed.). Wiley. [VERIFY: co-kriging chapter]
- Forrester, A.I.J., Sobester, A., Keane, A.J. (2007). "Multi-Fidelity Optimization via Surrogate Modelling." *Proceedings of the Royal Society A*, 463. [VERIFY: pages and DOI not asserted]

**WySE mapping.** Same as KOH; co-kriging adds a cross-level covariance matrix C(L_i, L_j) that is in principle a bilinear form on the Lawvere metric space. Each off-diagonal block C(L_i, L_j) quantifies the behavioral coupling between levels i and j, which is structurally analogous to the D_b matrix in the bigraded/double-category WySE framing from memory (project_wyse_category_theory_thread.md).

#### 2.3.3 Multi-Level Monte Carlo (MLMC)

**Fusion operator.** MLMC computes E[y_HF] as a telescoping sum over L levels:

    E[y_HF] = E[y_0] + sum_{l=1}^{L} E[y_l - y_{l-1}]

Each correction term E[y_l - y_{l-1}] is estimated with a small sample at level l. The fused estimate is the sum of these estimates.

**Mathematical object.** A linear combination of Monte Carlo estimators; not a new system model but an estimator of a functional (expected output) of the HF system. In measure-theoretic terms, it is a telescoping decomposition of an integral over the output measure.

**Canonical reference.**
- Giles, M.B. (2008). "Multilevel Monte Carlo Path Simulation." *Operations Research*, 56(3). [VERIFY: pages 607-617 plausible, no DOI asserted]

**WySE mapping.**
- D_b: MLMC directly targets the statistical estimation of D_b (or any output functional). The MLMC variance decomposition across levels is an empirical decomposition of the behavioral-distance budget across stratification levels. Formally: var(MLMC estimator) = sum_l V_l / N_l where V_l = var(y_l - y_{l-1}) and N_l is the sample count at level l. Minimizing total cost for fixed variance is solved by N_l proportional to sqrt(V_l / C_l) where C_l is the per-sample cost at level l.
- Pedigree: The pedigree of the MLMC estimate is explicitly multi-level; each correction term carries the pedigree of two consecutive fidelity levels. This is the most formal treatment of multi-level pedigree in the literature.

**Fable-shape verdict.** MODERATE for a WySE claim. The MLMC variance formula provides a computable inheritance law for estimation uncertainty across levels. The Fable claim would be: "The MLMC estimator of D_b(Z_HF, Z*) decomposes additively by stratification level, with each level's contribution bounded by V_l." Witness: run MLMC on the LA/NL pendulum pair from the wyse-model-generation skill; verify the variance decomposition. Adjacency to Candidate D: MLMC is the estimation method that would operationalize D_b measurements when the HF model is expensive; it is a tool for computing witnesses, not a new morphism claim.

#### 2.3.4 Control Variates

**Fusion operator.** Given a HF output y_HF and a LF output y_LF with known (or estimated) expectation mu_LF, the control variate estimator is:

    y_CV = y_HF - c * (y_LF - mu_LF)

where c is chosen to minimize variance (c* = Cov(y_HF, y_LF) / Var(y_LF)).

**Mathematical object.** A variance-reduced estimator; structurally a projection of y_HF onto the orthogonal complement of y_LF in the L2 inner product space of random variables.

**Canonical reference.**
- Nelson, B.L. (1987). "Control-Variate Remedies." *Operations Research*, 38(6). [VERIFY: volume/year/pages plausible but not confirmed against source; use PLACEHOLDER if needed]
- [PLACEHOLDER: a standard Monte Carlo textbook reference, e.g., Glasserman 2004 Monte Carlo Methods in Financial Engineering, Springer, covers control variates but DOI/pages not asserted here]

**WySE mapping.** Control variates reduce the variance of D_b estimates; the optimal c* = Cov(y_HF, y_LF) / Var(y_LF) is directly related to the linear coupling coefficient rho in KOH. When the models are Wymore tuples with scalar output, c* is the empirical estimate of the readout-layer comorphism strength. This forges a link between the statistical efficiency literature and the WySE morphism catalog.

**Fable-shape verdict.** LOW standalone; HIGH as a witness tool. Control variates accelerate the computation of D_b witnesses; they are not themselves a morphism claim. Worth embedding in the witness protocol of any Fable that requires D_b estimation with limited HF samples.

---

### 2.4 Surrogate / Reduced-Order Model (ROM) Fusion

**Fusion operator.** A surrogate (e.g., polynomial chaos expansion, neural-network surrogate, proper orthogonal decomposition (POD) ROM) approximates Z_HF with a cheaper Z_surr. Fusion here means: use Z_surr in place of Z_HF where cost prohibits the latter, then verify the error introduced.

**Mathematical object.** A homomorphism Z_HF -> Z_surr (or its lax version). POD-Galerkin: the ROM is obtained by projecting the high-dimensional state space S_HF onto a k-dimensional subspace via a projection operator Pi: S_HF -> S_surr (dim k << dim S_HF). The readout is postcomposed: R_surr = R_HF circ Pi^dagger.

**Canonical references.**
- Sirovich, L. (1987). "Turbulence and the Dynamics of Coherent Structures." *Quarterly of Applied Mathematics*, 45(3). [VERIFY: pages 561-571 plausible, no DOI asserted; this is the original POD/Karhunen-Loeve paper in the fluid context]
- Lumley, J.L. (1967). "The Structure of Inhomogeneous Turbulent Flows." In *Atmospheric Turbulence and Radio Wave Propagation*, ed. Yaglom and Tatarski. [VERIFY]
- Benner, P., Gugercin, S., Willcox, K. (2015). "A Survey of Projection-Based Model Reduction Methods for Parametric Dynamical Systems." *SIAM Review*, 57(4). [VERIFY: pages 483-531 plausible, no DOI asserted]
- For neural network surrogates: [PLACEHOLDER: multiple 2018-2022 papers on physics-informed neural networks, e.g., Raissi, Perdikaris, Karniadakis 2019 in Journal of Computational Physics; pages/DOI not asserted here]

**WySE / pedigree mapping.**
- D_s: The projection Pi is exactly a surjection S_HF -> S_surr satisfying condition iii in the Wymore homomorphism definition (Section 2.1 of the isomorphism-library paper). D_s(Z_surr, Z_HF) = k / dim(S_HF) in the uniform case, but more precisely it is the degree-of-homomorphism metric introduced by Wach et al. (2024). ROM fusion is therefore the most direct instantiation of D_s reduction in the fusion literature.
- D_b: The ROM behavioral error is the projection residual: D_b(Z_surr, Z_HF) = sup_t || y_HF(t) - y_surr(t) ||. For POD-Galerkin, this is bounded by the tail of the singular value decomposition (the sum of discarded singular values squared). This is a hard inheritance law: D_b is determined by the spectrum of the empirical covariance of the HF state trajectories.
- Pedigree: Z_surr carries the pedigree of Z_HF plus the reduction method (POD basis, training data, truncation level). This is the "reduction step" pedigree annotation in WySE.

**Fable-shape verdict.** STRONG; this is the closest to an existing WySE claim. Provable claim: "The POD-Galerkin ROM Z_surr is a Wymore homomorphism from Z_HF with D_s equal to the degree-of-homomorphism of the projection Pi and D_b bounded by the tail singular value sum." The projection Pi is exactly the surjection hq in the Wymore conditions; the readout commutativity condition v is satisfied by construction. Witness: instantiate the nonlinear pendulum from the wyse-model-generation skill as Z_HF; construct a 1-mode POD ROM as Z_surr; compute D_s (= 1/dim from state count) and D_b (max trajectory error); verify both bounds. Adjacency to Candidate D: the ROM projection IS a gluing map at the state level; the "minimal gluing" result from Candidate D applies directly when the ROM basis vectors are the shared interface carriers.

---

### 2.5 Data Assimilation as Model+Data Fusion

#### 2.5.1 Variational (3D-Var / 4D-Var)

**Fusion operator.** Given a background state x_b (model prediction) and observations y_obs, 4D-Var minimizes:

    J(x) = (1/2)(x-x_b)^T B^{-1} (x-x_b) + (1/2)(y_obs - H(x))^T R^{-1} (y_obs - H(x))

where B is background error covariance, R is observation error covariance, and H is the observation operator. The minimizer x_a (analysis) is the fused state.

**Mathematical object.** The analysis x_a is the mode of the posterior distribution p(x | y_obs) in Gaussian settings; in general it is a MAP estimate. The fused object is a state vector in S_Z (not a distribution), but carries posterior covariance P_a = (B^{-1} + H^T R^{-1} H)^{-1}.

**Canonical references.**
- Talagrand, O. and Courtier, P. (1987). "Variational Assimilation of Meteorological Observations with the Adjoint Vorticity Equation." *Quarterly Journal of the Royal Meteorological Society*, 113(478). [VERIFY: pages 1311-1328 plausible, no DOI asserted]
- Lorenc, A.C. (1986). "Analysis Methods for Numerical Weather Prediction." *Quarterly Journal of the Royal Meteorological Society*, 112(474). [VERIFY: pages 1177-1194 plausible, no DOI asserted]

**WySE mapping.**
- D_s: The observation operator H: S_Z -> O_obs is a readout morphism (exactly condition v in Wymore's formalism). 4D-Var is therefore a state-estimation problem in a Wymore system: it searches for s* in S_Z such that R_Z(s*) matches y_obs. D_s is not modified by assimilation; the model structure is held fixed.
- D_b: After assimilation, D_b(x_a, x_true) is bounded by the analysis error covariance trace: E[||x_a - x_true||^2] = trace(P_a). This is the fundamental result of optimal estimation. Inheritance law: D_b_analysis <= D_b_background * (reduction factor from observations).
- Pedigree: The assimilated state carries a joint pedigree: (model Z, observation set Y, assimilation time window [t1, t2]). This is the "data-augmented" pedigree annotation.

**Fable-shape verdict.** MODERATE. The D_b inheritance via analysis error covariance is clean and computable. The Fable claim: "4D-Var assimilation of observations y_obs into Wymore system Z reduces D_b from D_b_background to trace(P_a)^{1/2}; trace(P_a) is bounded above by the eigenvalues of B and below by trace(H^T R^{-1} H)^{-1}." Witness: 1D linear Z (scalar state), one observation operator H=1, run the scalar Kalman update (which is the linear 3D-Var solution), verify the error bounds analytically. Not adjacent to Candidate D or E but opens a new WySE thread on the observation operator as a comorphism.

#### 2.5.2 Ensemble Kalman Filter (EnKF)

**Fusion operator.** The EnKF approximates the Kalman update using an ensemble of N state vectors {x_i}. The ensemble mean and covariance estimate B; the Kalman gain K = B H^T (H B H^T + R)^{-1} maps observation increments to state updates.

**Mathematical object.** A sample-based approximation to the Bayesian posterior over S_Z, evolving through time. The fused model output is the ensemble mean (or median); the ensemble spread quantifies D_b uncertainty.

**Canonical reference.**
- Evensen, G. (1994). "Sequential Data Assimilation with a Nonlinear Quasi-Geostrophic Model Using Monte Carlo Methods to Forecast Error Statistics." *Journal of Geophysical Research*, 99(C5). [VERIFY: pages 10143-10162 plausible, no DOI asserted]

**WySE mapping.** Same structural picture as 4D-Var. D_b is operationalized by the ensemble spread: D_b(ensemble_mean, x_true) is empirically estimated by the ensemble standard deviation. This is a direct, sample-based D_b witness, not requiring a closed-form formula. For a WySE Fable, this means the EnKF provides the witness protocol: run N ensemble members through Z, compute spread, claim it bounds D_b.

**Fable-shape verdict.** MODERATE (same as 4D-Var). The EnKF provides a sample-based witness for D_b bounds; it is weaker than the POD-ROM Fable but more general (works for nonlinear systems).

---

### 2.6 Model Reconciliation / Conflation of Probability Distributions

**Fusion operator.** Given K probability distributions p_1,...,p_K over the same outcome space O (each representing a model's predictive output distribution), the "conflation" or "combination" seeks a single distribution p_fused. Three main approaches:

(i) *Logarithmic pooling* (log-linear opinion pool): p_fused(o) proportional to product_k p_k(o)^{w_k}. This is the geometric mean of the K distributions (up to normalization), which in the Kullback-Leibler (KL) sense is the distribution minimizing the weighted sum of KL divergences from the K inputs.

(ii) *Linear pooling* (arithmetic mean): p_fused = sum_k w_k p_k. This is BMA's output stage; it is a convex combination in the space of probability measures.

(iii) *Conflation (Hill 2011)*: p_fused proportional to product_k p_k (equal weights, unnormalized product). This minimizes Fisher information loss when the K distributions are independent experts on the same quantity.

**Mathematical object.**
- Log pooling: a geodesic midpoint in the statistical manifold of the K distributions under the Fisher metric; in information-geometric terms, the m-projection onto the exponential family containing all p_k.
- Linear pooling: a Barycentre in the space of probability measures under the 2-Wasserstein metric (when p_k are Gaussian, it is the Wasserstein barycentre).
- Conflation: a pushforward measure along the diagonal product; Hill's construction shows it minimizes the sum of squared deviations in information content.

**Canonical references.**
- Stone, M. (1961). "The Opinion Pool." *Annals of Mathematical Statistics*, 32(4). [VERIFY: pages 1339-1342 plausible, no DOI asserted]
- Genest, C. and Zidek, J.V. (1986). "Combining Probability Distributions: A Critique and an Annotated Bibliography." *Statistical Science*, 1(1). [VERIFY: pages 114-135 plausible, no DOI asserted]
- Hill, T.P. (2011). "Conflations of Probability Distributions." *Transactions of the American Mathematical Society*, 363(6). [VERIFY: pages 3351-3372 plausible, no DOI asserted]
- For Wasserstein barycentre: Agueh, M. and Carlier, G. (2011). "Barycenters in the Wasserstein Space." *SIAM Journal on Mathematical Analysis*, 43(2). [VERIFY: pages 904-924 plausible, no DOI asserted]

**WySE / pedigree mapping.**
- D_s: Model reconciliation operates entirely on the output distribution; it does not touch state sets or transition functions. D_s is therefore undefined at the reconciled level; it inherits whichever parent's structure is used to generate the output distribution.
- D_b: The Wasserstein barycentre connection is the most powerful: if D_b is measured as the Wasserstein-2 distance between output trajectories (a functional lift of the pointwise L2 distance), then the linear pooling minimizer IS the Wasserstein barycentre, and D_b(fused, Z*) <= (sum_k w_k * D_b(Z_k, Z*)^2)^{1/2} (quadratic mean bound, not linear). This is a tighter bound than simple convexity in L2 contexts.
- Categorical structure: The log-linear pooling is a colimit in the category of exponential families; the weights {w_k} play the role of morphism weights in a weighted colimit diagram. This is the most categorical of the fusion operators surveyed.

**Fable-shape verdict.** MODERATE-STRONG for the Wasserstein barycentre / D_b inheritance claim. Provable claim: "The linear pool p_fused is the Wasserstein-2 barycentre of the output distributions p_1,...,p_K; its Wasserstein distance to the true output distribution p* satisfies D_b(fused, *) <= (sum_k w_k D_b(Z_k, *)^2)^{1/2}." Witness: K=2 Gaussian output models, compute the barycentre analytically (it is a Gaussian with moment-averaged mean and covariance), verify the distance bound. Adjacency to Candidate E (Cody transfer distance): the Wasserstein metric is the same family as transfer-distance metrics; this may enable a unified D_b + transfer-distance inequality once the output spaces are aligned.

---

## 3. WySE Mapping: Pedigree / D_s / D_b Inheritance Summary

| Fusion family | D_s inheritance | D_b inheritance law | Categorical form | Level-crossing? |
|---|---|---|---|---|
| BMA | min(D_s parents) or undefined if carriers differ | D_b_fused <= sum_k w_k D_b_k (convexity) | Convex combination in probability-measure space | No (same level required) |
| Ensemble / stacking | Undefined (meta-level) | D_b <= (1/K) sum D_b_k for averaging; unbounded for stacking | Diagram of K arrows + aggregation morphism | Yes (stacking lifts a level) |
| MoE | Input-region-local D_s | Input-region-local D_b | Soft product in Kleisli(Delta) | No (same level per expert) |
| KOH multi-fidelity | D_s(surr, HF) determined by rho; inherits HF structure | D_b <= GP posterior std (L2) | Kleisli morphism in Giry monad (per input) | Yes (LF to HF level-crossing) |
| MLMC | Multi-level, telescoping | Variance = sum_l V_l / N_l (decomposable) | Additive decomposition of integral | Yes (explicit level sum) |
| ROM (POD) | D_s = degree-of-homomorphism of projection Pi | D_b <= tail singular value sum | Projection surjection hq; Wymore homomorphism | Yes (state-space compression) |
| 4D-Var / 3D-Var | Unchanged (state search within Z) | D_b <= trace(P_a)^{1/2} | MAP in posterior; observation op = readout comorphism | No |
| EnKF | Unchanged | D_b estimated by ensemble spread | Sample-based Bayesian update | No |
| Linear pooling | Output-level only | D_b <= (sum w_k D_b_k^2)^{1/2} (Wasserstein) | Wasserstein barycentre | No |
| Log pooling | Output-level only | m-projection in exponential family | Colimit in exponential-family category (weighted) | No |

**Key structural observation.** There are two fundamentally different types of fusion in this table:
1. *Same-level fusion*: BMA, ensemble, linear pooling. These produce convex bounds on D_b and do not require (or produce) new D_s structure.
2. *Level-crossing fusion*: KOH, MLMC, ROM. These require an explicit comorphism between levels (rho, the projection Pi, or the level index l); D_s is defined by this comorphism; D_b inherits through the level-crossing map. These are the structurally richer cases for WySE.

**General inheritance conjecture (not yet proven).** For any level-crossing fusion with comorphism phi: Z_LF -> Z_HF:

    D_b(Z_fused, Z*) <= D_b(Z_HF, Z*) + D_b(Z_fused, Z_HF)

where the second term is the fusion error bounded by the specific method (GP std, singular-value tail, ensemble spread). This is a two-step triangle inequality in the Lawvere metric. Proving it rigorously for each fusion type and showing the bound is tight (not loose) would constitute a family of Fable claims.

---

## 4. Fable-Shape Candidates (Ranked)

Ranking criteria: (1) crispness of the provable claim, (2) feasibility of the machine-checkable witness, (3) adjacency to Candidates D and E.

---

### F-MF-01: ROM-as-Wymore-Homomorphism (STRONG)

**Claim.** Given a Wymore system Z_HF = (S_HF, I, O, N_HF, R_HF) and a POD projection Pi: S_HF -> S_surr (dim surr << dim HF), the ROM Z_surr = (S_surr, I, O, N_surr, R_surr) with N_surr = Pi circ N_HF circ Pi^dagger and R_surr = R_HF circ Pi^dagger is a Wymore homomorphism from Z_HF to Z_surr with:
(a) D_s(Z_surr, Z_HF) = degree-of-homomorphism(Pi) = dim_surr / dim_HF (uniform case),
(b) D_b(Z_surr, Z_HF) bounded above by the tail singular value sum sigma_{k+1}^2 + ... + sigma_n^2 of the empirical covariance of state trajectories.

**Witness sketch.** Use the nonlinear pendulum from the wyse-model-generation skill as Z_HF; truncate to a 1-mode subspace (k=1); compute D_s directly as 1/dim_HF; run both systems from the same initial condition; compute max output error; verify it is bounded by the tail singular value. Machine-checkable on existing infrastructure. SHA-stable hash on the trajectory comparison.

**Adjacency.** Candidate D (gluing result): the ROM projection Pi IS the "shared carrier" map in Candidate D. This Fable either strengthens Candidate D (by showing the gluing is also a valid homomorphism, not just a lax functor extension) or requires a carve-out (lax functor is strictly weaker than homomorphism). Resolving which is a new contribution.

---

### F-MF-02: D_b Convexity Inheritance for Same-Level Mixture (STRONG)

**Claim.** Given K Wymore systems Z_1,...,Z_K at the same stratification level with a common output space O, the BMA / linear-pool fused readout R_fused = sum_k w_k R_{Z_k} satisfies D_b(Z_fused, Z*) <= sum_k w_k D_b(Z_k, Z*) for any ground-truth Z*, provided all Z_k are homomorphic to Z* with the same surjections (h_i, h_o, h_q).

**Witness sketch.** Instantiate K=2 Wymore tuples at level LA (linear abstraction); form BMA mixture with weight alpha; compute D_b by trajectory comparison; verify the linear interpolation bound for alpha in {0, 0.25, 0.5, 0.75, 1}. This is 5 witness points, all on existing infrastructure. The claim is tight when alpha concentrates on one model.

**Adjacency.** Not adjacent to Candidates D or E; a standalone WySE claim. Value: provides the same-level fusion baseline from which level-crossing Fables (F-MF-01, F-MF-03) can be differentiated.

---

### F-MF-03: KOH Coupling as Readout Comorphism (STRONG)

**Claim.** Given Z_LF at level L1 and Z_HF at level L2 (L1 < L2) with a known linear bias rho: O_LF -> O_HF, the KOH posterior mean E[y_HF | y_LF, y_HF_obs] constitutes a Wymore tuple Z_KOH at level L2 with readout R_KOH(s) = rho * R_LF(s) + delta_mean(s), where delta_mean is the GP posterior mean of the discrepancy. The D_b(Z_KOH, Z_HF) <= sigma_max (the maximum posterior standard deviation over the prediction domain).

**Witness sketch.** Take Z_LF = the 1-mode ROM pendulum (from F-MF-01) and Z_HF = the full nonlinear pendulum; fit a 1D GP discrepancy delta on 5 HF observations; compute the posterior mean; compute D_b as the max absolute error; verify it is bounded by sigma_max. All computations on existing skill infrastructure.

**Adjacency.** Directly adjacent to Candidate D: rho is the "interface coupling coefficient" that Candidate D's lax functor must transport across the level boundary. The KOH claim makes rho an explicit, measurable, WySE-typed object.

---

### F-MF-04: Wasserstein D_b Inheritance for Distribution Pooling (MODERATE)

**Claim.** Given K output distributions P_1,...,P_K over O = R^d (Gaussian, for concreteness), the linear pool P_fused = sum_k w_k P_k satisfies W_2(P_fused, P*) <= (sum_k w_k W_2(P_k, P*)^2)^{1/2}, where W_2 is the 2-Wasserstein distance and P* is the true output distribution.

**Witness sketch.** Instantiate K=2 univariate Gaussians with known parameters; compute P_fused; compute W_2 analytically (for 1D Gaussians, W_2 = ||mu_1 - mu_2||^2 + (sigma_1 - sigma_2)^2); verify the bound. All arithmetic; no simulation needed.

**Adjacency.** Candidate E (Cody transfer distance): if D_b is lifted to the Wasserstein metric over output trajectories (which is natural for stochastic systems), then F-MF-04 is the stochastic analog of F-MF-02, and both bounds live in the same metric space as Candidate E's transfer distance. This opens the possibility of a unified inequality chain: D_b(fused, source) <= D_b_parent + D_transfer.

---

### F-MF-05: MLMC Variance Decomposition as D_b Budget (MODERATE)

**Claim.** The MLMC variance estimator for E[D_b(Z_HF, Z*)] decomposes additively across stratification levels: var(E_MLMC) = sum_l V_l / N_l, where V_l = var(D_b_l - D_b_{l-1}). The optimal allocation N_l* proportional to sqrt(V_l / C_l) achieves the minimum variance for a fixed total computational budget sum_l N_l C_l.

**Witness sketch.** This is proved analytically (Giles 2008 [VERIFY]); the witness for the WySE version is a 3-level pendulum hierarchy (1-mode ROM at L1, 2-mode ROM at L2, full NL at L3); run MLMC with N_l determined by the optimal allocation; verify the variance bound holds to within sampling error. More expensive than F-MF-01 through F-MF-04; rank lower.

**Adjacency.** Not directly adjacent to Candidates D or E; it is the computational method that would make D_b witnesses tractable for expensive HF systems. Embed as a tool in any Fable that requires empirical D_b bounds.

---

### F-MF-06: MoE Gating as Kleisli Morphism -- Open Conjecture (SPECULATIVE)

**Claim (conjectured, not yet crisp).** The MoE architecture defines a Kleisli morphism G: I -> Delta(K) in the distribution monad, composed with K expert readouts {R_{Z_k}: S_k -> O} to yield a fused readout. The fused model Z_MoE is the colimit of the K expert diagrams along G.

**Status.** This requires (a) showing the K experts and the gating form a diagram in an appropriate category of Wymore systems with stochastic readouts (Kleisli category of Giry monad), and (b) showing the colimit exists and equals the MoE output distribution. Neither step is currently written down in the WySE frame. This is a new research contribution if correct, not prior art.

**Adjacency.** Category theory thread (project_wyse_category_theory_thread.md): the Kleisli / Giry monad framing is already identified as load-bearing in WySE. MoE is a candidate demonstration object for that framing.

---

## 5. Refs-to-Verify ([PLACEHOLDER] Gate)

All references in this document are marked with [VERIFY] where metadata (pages, volume, year) is based on reviewer knowledge but has not been checked against a physical source. None of the references below have DOIs asserted. Before any of these enter approved.bib (R019/R109), each must pass the Byzantine-Bayesian verification protocol (refcheck.py gate).

Priority verification order (highest WySE relevance first):

1. [VERIFY-HIGH] Kennedy, M.C. and O'Hagan, A. (2000). *Biometrika*, 87(1). -- Central to F-MF-03.
2. [VERIFY-HIGH] Benner, P., Gugercin, S., Willcox, K. (2015). *SIAM Review*, 57(4). -- ROM survey; central to F-MF-01.
3. [VERIFY-HIGH] Giles, M.B. (2008). *Operations Research*, 56(3). -- Central to F-MF-05.
4. [VERIFY-HIGH] Hoeting, J.A. et al. (1999). *Statistical Science*, 14(4). -- Central to F-MF-02.
5. [VERIFY-MED] Agueh, M. and Carlier, G. (2011). *SIAM Journal on Mathematical Analysis*, 43(2). -- Central to F-MF-04.
6. [VERIFY-MED] Hill, T.P. (2011). *Transactions of the American Mathematical Society*, 363(6). -- Conflation claim.
7. [VERIFY-MED] Evensen, G. (1994). *Journal of Geophysical Research*, 99(C5). -- EnKF.
8. [VERIFY-MED] Genest, C. and Zidek, J.V. (1986). *Statistical Science*, 1(1). -- Opinion pooling survey.
9. [VERIFY-LOW] Talagrand and Courtier (1987). *QJRMS*, 113(478). -- 4D-Var.
10. [VERIFY-LOW] Stone, M. (1961). *Annals of Mathematical Statistics*, 32(4). -- Opinion pool origin.
11. [VERIFY-LOW] Jacobs et al. (1991). *Neural Computation*, 3(1). -- MoE origin.
12. [VERIFY-LOW] Wolpert, D.H. (1992). *Neural Networks*, 5(2). -- Stacking origin.
13. [VERIFY-LOW] Sirovich, L. (1987). *Quarterly of Applied Mathematics*, 45(3). -- POD.
14. [PLACEHOLDER] Raissi, Perdikaris, Karniadakis (2019) physics-informed neural networks paper: journal, volume, pages, DOI all unverified; DO NOT cite until resolved.
15. [PLACEHOLDER] Nelson (1987) control variates: year and journal approximate; confirm before use.
16. [PLACEHOLDER] Forrester, Sobester, Keane (2007) *Royal Society A*: pages/DOI not asserted.
17. [PLACEHOLDER] Fritz (2020) Markov kernels *Advances in Mathematics*: volume/pages not asserted.
18. [PLACEHOLDER] Lumley (1967) POD paper: proceedings volume/page details unverified.
19. [PLACEHOLDER] Cressie (1993) *Statistics for Spatial Data*: co-kriging chapter number not confirmed.
20. [PLACEHOLDER] Glasserman (2004) *Monte Carlo Methods in Financial Engineering*: not cited by name yet; if used for control variates, full metadata needed.

Already approved (from references.bib, verified):
- Girard, A. and Pappas, G.J. (2007). *IEEE Transactions on Automatic Control*, 52(5):782-798. -- Behavioral distance; directly relevant to D_b formulation.
- Wach, P.F. and Salado, A. (2024). *INCOSE International Symposium*. doi:10.1002/iis2.13136. -- D_s / degree-of-homomorphism.
- Wach, P.F. (2022). PhD dissertation, Virginia Tech. -- WySE foundations.

---

## 6. Gaps

### 6.1 Theoretical Gaps

1. **No published treatment of multi-fidelity fusion as a category-theoretic colimit in a WySE-typed category.** F-MF-01 (ROM homomorphism) and F-MF-03 (KOH coupling) are the closest, but neither paper expresses the result in terms of Wymore tuples or the (D_s, D_b) pair explicitly. This is the primary contribution opportunity.

2. **Pedigree has no formal semantics in any fusion paper surveyed.** The "pedigree" of a fused model (the provenance/fidelity lineage) is tracked informally (KOH knows its LF vs. HF sources; MLMC knows its level indices) but there is no category-theoretic or set-theoretic definition of pedigree composition. WySE would need to introduce this.

3. **The D_s metric has no analog in the fusion literature.** All fusion methods handle D_b (output error, prediction uncertainty) but none handle structural degree-of-homomorphism. The ROM / POD case is the only fusion method that implicitly contains D_s (through the projection Pi). This is a genuine gap.

4. **Level-crossing fusion and the question of colimit existence.** Do KOH, MLMC, and ROM define diagrams whose colimit exists in the category of Wymore systems? If the comorphism phi: Z_LF -> Z_HF is an honest Wymore homomorphism, then the colimit exists (by standard universal algebra). If phi is only a lax functor (Candidate D's setting), the colimit may only exist in a lax sense. This is the central unresolved question for the WySE fusion program.

5. **No WySE treatment of the ensemble Kalman filter's ensemble as a sample-based D_b witness.** This is technically straightforward but has not been written. It would make D_b measurement tractable for nonlinear systems via EnKF.

### 6.2 Empirical Gaps

6. **No multi-fidelity benchmark in the WySE/morphism-library context.** All existing wyse-model-generation witnesses are single-model (one Z_HF). A paired LF/HF benchmark (e.g., linear-model pendulum at LA level vs. nonlinear pendulum at NL level) would enable F-MF-01 and F-MF-03 witnesses.

7. **The rho parameter in KOH has never been compared to the degree-of-homomorphism D_s computed via Wach et al. (2024).** This comparison would either (a) confirm they measure the same thing (in which case KOH is an empirical estimation method for D_s), or (b) reveal they capture different aspects (structural vs. behavioral coupling), which would be a finding.

### 6.3 Methodological Gaps

8. **The Wasserstein barycentre (F-MF-04) requires Gaussian output assumptions for closed-form computation.** For non-Gaussian Wymore outputs (e.g., discrete state machines, nonlinear ODEs with non-Gaussian perturbations), the barycentre must be computed numerically (Sinkhorn iterations or similar). No paper applies this to Wymore-typed systems.

9. **Control variates have not been applied as a D_b witness accelerator.** This is methodologically straightforward but absent in the literature. Embedding control variates in the wyse-model-generation witness protocol would reduce the HF simulation cost for D_b bounds by a factor of 1/(1-rho^2) where rho is the LF-HF correlation.

### 6.4 Open Questions for Steering

- Is rho (KOH scaling) equal to, or a proxy for, D_s? (Experimental Q)
- Does the gluing result from Candidate D (lax functor over non-disjoint interfaces) compose with the ROM projection to yield a commutative diagram? (Theoretical Q, requires Candidate D's proof to be in hand)
- Should pedigree be a category-theoretic construction (a functor from a "pedigree category" to the category of Wymore systems)? (Design Q for the WySE CTO thread)

---

*Document compiled by: Literature Reviewer agent (claude-sonnet-4-6), 2026-07-15. All findings are (a) prior-art. No DOIs asserted without verification. [PLACEHOLDER] markers indicate metadata that must be verified before manuscript use.*

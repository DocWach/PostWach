# The Granular Record versus the Scalar Summary: A Thermodynamically Grounded, Family-Quantified Account of Model Reduction

**Draft v1, 2026-07-17**

**PROVENANCE (R018).** Drafted by Opus 4.8 (`claude-opus-4-8[1m]`), Anthropic, Claude Code CLI, 2026-07-17, from red-blue-white (RBW) adjudication records produced under the Fable 5 workflow (DERIVE: `claude-fable-5`; RED: Codex, live cross-vendor source-fetching; WHITE adjudication: Opus 4.8). All numerical results are transcribed from the cited witness and RBW files, not asserted from memory.

**Integration status (R016).** This is an (a) research artifact: a candidate manuscript consolidating results each validated in isolation by a machine-checked witness and a live cross-vendor RBW pass. No result here is a (b) demonstrated end-to-end capability or a (c) integrated deliverable. The single delivered-reduction claim tested at scale is reported as a characterized negative, not a win.

**Reference gate (R019).** Citations to keys confirmed in the portfolio approved store are given as normal IEEE numeric references. Every source not yet cleared through the verification protocol appears as a visible `[PLACEHOLDER: author year]` marker and MUST be resolved through refverify before any render. The manuscript does not render until the placeholder set is empty.

---

## Abstract

A model reduction can be summarized by a single number (a degree of homomorphism, a lumping-error scalar, a certified residual norm) or carried in full as the granular *record*: the per-block correspondence between the fine states and the coarse state they collapse to. We ask when the record captures distinctions the scalar conflates, what that extra information costs, and whether keeping the record ever buys a practical reduction advantage. Three findings, each machine-checked and adversarially adjudicated, organize the answer. First, the record carries a thermodynamic quantity that no library scalar carries: the minimum Landauer entropy production of realizing a deterministic many-to-one homomorphism is the Shannon functional of the granule record, distinct from the structure-degree D_s and from the worst-granule size g_max, and among granule-local functionals it is the *unique* refinement-monotone, size-sensitive, tower-additive potential. Second, the record-beats-scalar advantage is not universal; it is governed by a family quantifier. Across three modalities we measure it directly: it holds in stochastic (Markov/DEVS) lumping, where the record separates two lumpings that even the best modern structural discriminators tie (outcome-distribution errors 3/128 vs 1/128 at equal LumpSTD), and it is refuted in reduced-basis model-order reduction and in transfer learning, where a stronger legal scalar (an energy-norm residual; a label-aware joint kernel statistic) already separates the pair. The clean statement is a three-regime boundary: the record advantage is real if and only if the modality's scalar family contains no sufficient statistic for the outcome. Third, whether the record delivers a reduction *win* is regime- and scale-dependent and, at scale, gated by certificate tightness. A three-way benchmark (exact tree-expansion, Monte Carlo, stratified record-based reduction) at 98 states is a characterized near-miss: the record arm is Pareto-nondominated and certified but misses a pre-registered total-cost bar because a fixed record overhead is unamortized. A scale-up stress test shows the overhead amortizes (the cost bar flips at the largest scale) while the first-order certificate goes slack exactly where the cost bar passes, relocating the single binding obstruction from overhead to certificate tightness. A hardened tighter certificate then recovers the missing factor at that scale, valid on the tested family and structurally tighter (a factor-2 exact identity on the mode-pair blocks), under a declared accounting convention. We claim no unification theorem and no faster simulator. We claim a measured map: the record's distinctions are real and thermodynamically priced, and their practical value is bounded by whether a tight enough certificate exists.

---

## 1. Introduction

A reduced model is a compression of a detailed one. Systems engineering and simulation carry that compression in two very different currencies. One is a scalar: a degree of homomorphism D_s that measures how far a proposed map departs from an exact structural correspondence [11], a lumping-error number for a Markov aggregation [PLACEHOLDER: kemeny1976finite], a certified residual norm for a reduced basis [PLACEHOLDER: rozza2008reduced]. The other is the *record*: the full list, block by block, of which fine states collapse to which coarse state and with what mass. A scalar is cheap to store and easy to compare; a record is expensive and unwieldy. The engineering instinct is to keep the scalar and discard the record.

This paper is about what that instinct throws away, and when the loss matters. The question is sharper than it first appears, because a scalar is not one object but a *family*: for a given modality there are usually several legal scalars, some weak and some strong, and the interesting comparison is between the record and the strongest legal scalar, not a convenient weak one. Much of what looks like a record advantage in an initial construction turns out to be an artifact of pinning the scalar family too narrow; a stronger scalar just outside the pin recovers the distinction the record claimed as its own. We report both outcomes honestly, including the two modalities where the record loses.

Three contributions structure the account.

1. **A thermodynamic grounding (Section 2).** The record is not merely more information; it is the carrier of a physical quantity. The minimum Landauer entropy production of a deterministic many-to-one homomorphism is the Shannon functional of the granule record, and it is provably a different number from the two scalars the library already uses. On the resolution tower this entropy is the *unique* granule-local potential satisfying four natural axioms, which pins down exactly what the record buys thermodynamically that the scalars do not.

2. **A family-quantified boundary (Section 3).** The record-beats-scalar phenomenon is real in some modalities and false in others, and the difference is not accidental. We give a three-regime classification, validated against three worked modality instances, and show that the naive criteria (does the record beat the pinned scalar? is the whole record injective?) misclassify two of the three. The correct criterion is a sufficiency condition over the scalar family.

3. **A reduction study, a cost accounting, and a stress test (Sections 4 and 5).** We price the information the record carries and test whether keeping it buys a practical reduction win. At moderate scale it does not: the win is a characterized near-miss, limited by a fixed record overhead. At larger scale the overhead amortizes but the certificate loosens, and a tighter certificate then recovers the win under a declared accounting convention. The value of the record is gated by certificate tightness.

We are explicit about what this is not. It is not a unification theorem; an attempt to unify the modality cases under a single sufficiency theorem was adjudicated a rework and is reported as such (Section 3.3). It is not a faster simulator; the exact tree-expansion baseline is exact and cheap at the scales we can fully resolve, and the record-based arm does not dominate it end-to-end (Section 5). What we offer is a measured map of when the granular record earns its cost.

### 1.1 Objects and notation

A *homomorphism* h: X -> Y here is a deterministic surjective map from a fine carrier X to a coarse carrier Y. Its *granule record* R(h) is the family of pre-image sizes and, where mass matters, the per-block correspondence structure: {|h^{-1}(y)|}_{y in Y}, enriched for stochastic settings by the within-block transition data. Three scalar summaries recur. The *structure-degree* D_s is a normalized departure-from-exactness measure (here the mean-reciprocal-granule form, D_s = 1 minus the mean of 1/|granule|) [11]. The *worst-granule* scalar g_max is the largest pre-image size. The *record entropy* S is the Shannon functional introduced in Section 2. All three are functionals of the same record; the point of the paper is that they are *lossy* functionals, and that the record separates cases they conflate. We write the *resolution tower* for a chain of successive coarsenings (reducts) with refinements (expansions) as the inverse legs, following the WySE stratification of a model into resolution levels [15].

---

## 2. The granular record and its thermodynamic grounding

### 2.1 The record carries the Landauer entropy; the scalars do not

Erasing information costs energy. Landauer's principle prices the erasure of one bit at kT ln 2 of dissipated heat [7]. A many-to-one homomorphism is an erasure: it forgets which fine state within a block produced the coarse state. The first result (result F29 in the internal record; witness SHA `7af04470...`, exit 0, 47/47 checks, live cross-vendor red, closed-hardened) prices this exactly.

**Theorem 2.1 (record entropy).** For a deterministic homomorphism h: X -> Y with X uniform on |X| = n, the minimum Landauer entropy production is

  S(h) = H(X | Y) = H(X) - H(Y) = sum_y p(y) log2 |h^{-1}(y)| bits,

the Shannon functional of the granule record. Three computations agree (H(X|Y), H(X)-H(Y), and sum p log g). The kT ln 2 pricing is ceded physics [7]; the witness establishes the information-counting content on exact rational arithmetic.

The load-bearing claim is not the entropy formula, which is textbook [6]. It is that S is a *third* scalar, distinct from D_s and from g_max, and that the record separates cases each of these conflates. The witness exhibits this with exact (Fraction, not floating-point) equalities:

- Records {2,2,1} and {3,1} have *equal* D_s = 1/3 yet S = 0.8 vs 1.1887 bits (delta S = 0.3887).
- Records {2,2} and {2,2,1} have *equal* g_max = 2 yet S = 1.0 vs 0.8 bits.
- The same-carrier pair {4,1,1} and {2,2,1,1} at n = 6 has *equal* D_s = 1/4 yet S = 4/3 vs 2/3 bits (independently confirmed by WHITE and by the red adversary).

A pipeline that forwards only D_s, or only g_max, has destroyed the information needed to price the reduction thermodynamically. This is the thermodynamic instance of the library's separation lemma: the record separates what the scalars conflate.

**Fences.** The identity S = H(X|Y) as a function of the granule-size record holds for *uniform* X; non-uniform inputs need the per-element weighted record. The kT ln 2 conversion is ceded, not measured (no calorimetry). Two adjacent prior-art claims that a scalar H(X|Y) bound appears in the discarded-information-conditional-on-output literature [PLACEHOLDER: sagawa2009minimal] [PLACEHOLDER: faist2015minimal] are unverified and must be resolved before any manuscript render; the WySE delta (record-as-carrier, three-way scalar conflation, tower arrow) survives even if a scalar bound is prior art.

### 2.2 A directional arrow on the resolution tower

The entropy orients the tower. Coarsening (a reduct) dissipates S(h) kT ln 2; expansion (the inverse leg) must be *supplied* side information whose expected length is exactly S(h) bits, and a one-symbol-short index alphabet provably collides by pigeonhole; a bijection (all granules singletons, D_s = 0) is free at S = 0. The red adversary correctly flagged a one-shot-versus-Shannon wording distinction (the pigeonhole bounds alphabet *size*, ceil(log2 g_max); the *expected* supplied length is S(h)); the underlying proof is correct and the header wording is the only repair. This gives the reduct and expansion legs a physical orientation the static (D_s, D_b) frame lacked.

### 2.3 The record entropy is the unique tower potential

Monotonicity alone does not single out S; other functionals also increase under coarsening. Two follow-on results (F31, witness SHA `40f3df4b`, 29/29, closed-hardened; and its uniqueness follower F32, witness SHA `bb45e07f`, 40/40, closed-hardened) settle the characterization.

**Theorem 2.2 (S is a monotone potential where D_s is not).** S weakly increases under every coarsening on the resolution tower, while the structure-degree D_s is *non-monotone*: on the library pair {1,1,10,10} to {1,1,20} the mean-reciprocal-degree scalar moves the wrong way (9/20 to 19/60). So the library's own scalar fails to be a tower potential exactly where S succeeds. This is a WySE-specific separation, not textbook entropy monotonicity: the counterexample is the library's own degree on the library's own tower.

**Theorem 2.3 (uniqueness).** Among granule-local record functionals, S is the *unique* (up to positive scale) potential satisfying: A0 continuity/normalization; A1 refinement-monotonicity; A2 size-sensitivity; A3 tower-additivity (the Shannon chain rule / grouping). Under A1-A3, g_max is eliminated by an explicit tower-additivity counterexample (2 + 3 = 5 != 4 on one tower, 10 + 2 = 12 != 20 with opposite sign on another, so no affine repair), and D_s is already out by A1. The general uniqueness kernel is ceded to Shannon-Khinchin-Faddeev [9] [10] [5].

A0 is load-bearing and stated, not smuggled: without it the spoiler functional S + c(n - k) passes A1-A3, so the axiomatization is honestly four axioms, not three. The chain rule closes exactly on the tested tower (a middle step of 10/11 bits, independently re-derived). The honest residue: this pins S among granule-*local* functionals under A0; extending S beyond uniform p (a general measure) is open.

**Section 2 summary.** The record entropy is the thermodynamic content of a reduction, it is provably distinct from the two library scalars, it orients the tower, and it is the unique granule-local potential of its kind. This is the spine on which the rest of the paper hangs: the record does not merely have more numbers, it carries a physical potential the scalars cannot express.

---

## 3. The family-quantified boundary

Section 2 shows the record carries a scalar-invisible quantity in the abstract setting. Does the record beat the strongest scalar in *concrete reduction modalities*? Not always. This section measures the boundary directly across three modalities and states the criterion that separates the wins from the losses.

### 3.1 One modality where the record wins: stochastic lumping

In stochastic (Markov / DEVS) lumping, a fine chain is aggregated into blocks and the quantity of interest is an outcome distribution. The lumping-error scalars are LumpSTD (the max standard deviation of outgoing block probabilities, zero iff exactly lumpable), the structure-degree D_s, and, importantly, the *modern* structural discriminators: the Michel-Siegle partition-dependent transient bound [PLACEHOLDER: michel2024formal] and the Geiger information-bottleneck KL-aggregation cost [PLACEHOLDER: geiger2015optimal]. These are purpose-built to distinguish equal-size aggregations by structure, so they are the strongest legal scalars, not weak ones.

**Result 3.1 (M1, witness SHA `c7a31377...`, exit 0, all checks pass, tamper bites with 8 assertions, live cross-vendor red, closed-hardened).** On a canonical 6-state absorbing chain, two lumpings A and B are constructed *equal* on every record-free reduction-quality scalar: LumpSTD^2 = 1/512 for both, D_s = 3/4 for both, the KL term-multisets are bitwise identical, and the lumped chains share trace 1/2, determinant 0, and discriminant 1/4 (identical eigenvalues and spectral gap). Yet the true outcome-distribution errors differ: total-variation error 3/128 for A vs 1/128 for B, an exact ratio of 3. The transition-weighted granule record orders them correctly and reproduces both errors exactly.

The adversary attempted the standard refutation (assert that the paper-exact Michel-Siegle bound already separates A from B) and named a separating number 3/8. WHITE recomputed the Michel-Siegle per-aggregate factor three ways (member-versus-block-mean L1 on aggregated and on micro rows, max pairwise within-block L1, and the occupancy-weighted transient form) and obtained *exact equality* in every case (1/8 = 1/8; occupancy-weighted transient 3/16 = 3/16). The adversary's 3/8 pairs two states co-blocked in *neither* partition, which is not a legal within-block quantity; the adversary did not run the chain. The separation lives in the alignment between within-block occupancy skew (3/32 for A, 1/32 for B at the first step) and within-block output deviation, a quantity that requires per-member resolution. No record-free quality scalar WHITE could construct separates A from B.

The one carried fence: formal paper-in-hand verification of the exact Michel-Siegle and Geiger expressions is an open reference item (R019). The manuscript wording must read "the record beats the checked transient, occupancy-weighted, and spectral scalars and the class-F transcriptions" until that verification closes. This governs wording, not the witnessed result.

### 3.2 Two modalities where the record loses to a stronger scalar

The honest measurement includes the negatives. In two modalities the record beats only a pinned or weak scalar; a stronger legal scalar recovers the ordering.

**Result 3.2 (M2, PDE model-order reduction, witness SHA `18cafd43...`, 33/33, live red, REFUTED).** Two reduced bases are constructed equal on the observable scalar pinned to the identity inner product (X = I): equal reduced dimension, equal Delta_N^2 = 2, equal Delta_s^2 = 4. The true output-error separates them, 3/8 vs 3/4, and the record reproduces both. But the modality's *canonical* a-posteriori estimator is the energy norm. For the fixed operator actually witnessed (A = diag(1,2,8,4), no parameter family, no offline/online split built), the energy-norm dual-residual r^T A^{-1} r is a legal, parameter-independent, standard certified scalar, and WHITE computed it directly: 3/8 for A and 3/4 for B, *exactly the true errors*. The tie exists only because X was pinned to I; the offline/online argument that would justify that pin requires a parametrized family the witness does not contain. Against the strongest legal scalar for the witnessed system, the pair is not tied. Refuted. The carry into MOR requires an actual affine A(mu) family that makes X = A(mu) illegal at generic mu while the tie persists; that construction is unbuilt.

**Result 3.3 (M3, transfer learning, witness SHA `84facd5f...`, 55/55, tamper bites, live red, REFUTED).** Two transfer reductions are constructed equal on the label-free divergence family (total variation, the H-divergence, unlabeled-marginal maximum mean discrepancy, and the lambda term): both push forward to the uniform marginal, so TV = 1/12, d_H = 1/6, unlabeled MMD^2 = 1/144 for both. The true transfer gaps differ, 5/12 vs 1/3, and the record reproduces them. But once label information is legitimately in scope (the candidate itself admits lambda, which needs target labels), the strongest legal scalar is not lambda; it is a *label-aware joint MMD* over the (granule, transported-label) distribution [PLACEHOLDER: gretton2012kernel]. WHITE recomputed it: MMD^2 = 7/48 for C vs 17/144 for D, which separates the pair and orders it the same way as the true gap. The record beats only the tier-1 label-free family, and that non-separation is a *known* impossibility (marginal-alignment blindness under label-conditional shift [PLACEHOLDER: zhao2019learning]), which the candidate cedes. Against the strongest label-aware scalar, the record does not carry. Refuted.

M2 and M3 share one shape: the witnessed tie was an artifact of the scalar family the construction pinned, and a legal scalar just outside the pin separates the pair. Neither refutes the abstract separation lemma; both *characterize* it.

### 3.3 The boundary theorem, and an honest correction

A first attempt to unify M1/M2/M3 under a single criterion (the record beats nothing iff a scalar is a sufficient statistic on the outcome-determining structure) was adjudicated a **rework** (F36 round 1, witness SHA `4005e214`). The decisive defect: the unification *misrepresented* M2 and M3. It redefined their outcome as the scalar's own accept/reject threshold, which made the "degenerate" case tautological and *reversed* the actual finding. The actual M2/M3 finding is not "a sufficient scalar exists, so the record degenerates"; it is "the record beats the pinned scalar but *loses to a stronger legal scalar*." That is a third regime the binary win/degenerate switch could not express. The elementary per-scalar sufficiency core is Fisher-Neyman and data-processing folklore [PLACEHOLDER: fisher1922mathematical] [6] and is ceded.

The reworked, family-quantified version (F36 round 2, witness SHA `57569709...`, 72/72, live red returns clean with zero defects, closed-hardened) carries. It states three regimes and classifies each modality faithfully against its *true* outcome:

- **REAL:** no scalar in the modality's family is sufficient for the outcome; the record advantage is real. Instances: the record entropy of Section 2 (F29); M1 with the canonical 3/128 vs 1/128 numbers; a fresh ill-conditioned poset.
- **NOT_REAL_DEGENERATE:** a sufficient scalar exists on a totally ordered structure (a chain), so the level index is itself a sufficient statistic and the record adds nothing. Illustrated by a fresh ill-conditioned chain.
- **NOT_REAL_BEATS_WEAK:** the record beats the weak or pinned scalars, but a stronger legal scalar in the family is sufficient. Instances: M2 (true errors 3/8 vs 3/4, energy-norm sufficient) and M3 (true gaps 5/12 vs 1/3, label-aware joint MMD sufficient).

**Theorem 3.4 (family-quantified boundary).** The record advantage over a modality's scalar family is REAL if and only if that family contains no sufficient statistic for the true outcome; otherwise the record either degenerates (a sufficient scalar on a chain) or beats only the weak members (a stronger legal scalar separates).

Two decoy criteria are shown to misclassify. "Record beats the pinned scalar" calls M2 and M3 REAL (wrong). "Whole record is injective" calls M3 REAL (wrong, because the label-aware joint MMD is sufficient yet ties the two distinct records at 7/48). That both decoys fail is what makes the family quantifier load-bearing rather than decorative.

**Honest scope.** The per-scalar sufficiency test is ceded folklore; the contribution is the family quantifier plus the faithful cross-modality classification, and the honest ceiling is that this is an organizing spine, not a standalone theorem paper. A prior narrative that a "chain-versus-poset boundary" came from an earlier result (F27) was found to misattribute homomorphic-encryption artifacts and has been dropped; the chain illustration in Theorem 3.4 is fresh and cites no artifact.

**The frame.** Theorem 3.4 characterizes *which distinctions* the record captures that the scalar family conflates. Paired with Section 2, which prices *the cost* of that information, it gives the overlap-distinction plus cost-of-information frame that the reduction study of Sections 4 and 5 instantiates.

---

## 4. The reduction study and the cost of information

### 4.1 Pricing the record

If the record carries distinctions and those distinctions cost entropy (Section 2), a reduction study must *price the record honestly*: the number of stored quantities must match the information the value claim actually uses. A first cost-of-information ledger (F38 round 1, witness SHA `ba24ab64`) was adjudicated a **rework** for two un-fenced accounting bugs. First, an "entropy erased" column mixed two different S definitions (an isomorphism-S of 0 for the exact arm with the F29 partition entropy for the others) under one label. Second, the record was priced at 78 numbers while the value claim rested on a signed per-block object (pi) that 78 numbers cannot reconstruct: the record-as-priced was not sufficient for the value it was credited.

The reworked ledger (F38 round 2, witness SHA `bda64677...`, 11/11 teeth including two new ones, live red returns clean, closed-hardened) fixes both, with teeth that fail if the fix is undone.

- **Uniform entropy column.** The S column is now the F29 functional over each row's *own* partition, for all rows. The exact tree-expansion arm's near-lumpable partition (72 singletons, 1 pair, 2 size-12 blocks; 75 blocks over 98 states) has its own F29 entropy 25/49 + (12/49) log2 3 = 0.898 bits, *not* 0; the isomorphism-0 convention is confined to the certificate column. The full record R1 erases exactly 36/49 = 0.7347 bits more than the exact arm, an exact figure (the log2 3 terms cancel).
- **Two-tier record price.** The record is priced as a certificate tier of 78 numbers (which buys the error bound) plus a distinction tier of 129 signed pi entries in the near-lumpable regime (which buys the sign claim), total 207. A posture-swap demonstration produces an *identical* 78-number certificate with entrywise-negated pi and sign-flipped outcome difference, proving the certificate tier alone cannot carry the sign claim; the 129-entry tier is the honest price of that claim, not padding.

The two structural methods now sit on one scale, and every value claim is priced by a tier that contains the object it uses.

### 4.2 The tighter certificate (CLOSED-HARDENED)

The reduction's usable frontier depends on how tight the a-priori certificate is. Section 5 shows the first-order budget pred(L) = O(eps T) is the binding constraint at scale. A tighter certificate C_tight was constructed and adjudicated (F39, witness SHA `a1749d01...`, all 7 teeth, all 10 pre-registered predictions hit, live red, **closed-hardened**).

**Result 4.1.** C_tight is (FT1) *valid*: TV <= C_tight at every level and scale, on exact Fractions; (FT2/FT3) *structurally tighter*: C_tight <= pred, strict wherever pred > 0, with the exact radius identity 2 rho = d on the two-element mode-pair blocks that carry the record-based arm (rho = d/2, independently re-derived by WHITE); and it *relocates the usable frontier by about one scale*: at the "large" scale pred = 0.166 fails the 0.15 usability bar while C_tight = 0.083 clears it, and at "xlarge" pred = 0.216 fails while C_tight = 0.108 clears.

The one genuine rigor gap, disclosed by the candidate and upheld by WHITE: C_tight rides a declared occupancy-weighting convention (the cheap lumped nu_t substituted for the derived pi_* mu_t), so it is a *verified finite-sweep upper bound on the tested family*, not a general theorem. The companion certificate C_rig closes that gap with a full derivation (e_{t+1} <= e_t(1 + rho_max) + s_t) and its usability is measured honestly: usable at small, medium, and large scales, *not* at xlarge (0.1865 > 0.15). No forced win: the rigorous companion is reported as not-yet-usable at the largest scale. C_tight is a valid, structurally tighter, honestly-bounded certificate, and it is exactly the factor the usability bar needed; the residual roughly 580x looseness versus the actual TV is relocated to the open second-order prize, not papered over.

---

## 5. The harness demonstration and the stress test

### 5.1 The three-way benchmark: a characterized near-miss

The delivered-reduction question is whether a stratified, record-based reduction can occupy a region of the (accuracy, runtime) frontier that dominates both a fair Monte Carlo baseline and the exact tree-expansion baseline at a certified error. We built a self-contained three-way benchmark: a faithful reimplementation of exact tree-expansion (paratemporal) reduction [3] [4], a fair Monte Carlo arm, and the WySE-stratified record-based arm, honest-by-design (its correctness teeth check correctness, not a win, and the delivered-win bar was pre-registered and adjudicated by WHITE).

**Result 5.1 (F34-BENCH, witness SHA `de35efb4...`, exit 0, all 7 correctness teeth pass, live source-fetching red confirms the reimplementation faithful and the MC baseline fair, REFUTED for the win claim).** At 98 states, across three regimes:

- **Exactly-lumpable (SYM):** exact tree-expansion discovers the 39-block merge and owns the frontier (TV = 0 at 2,272 ops); the record-based L1 arm ties but pays 895 overhead ops, so it is strictly worse. Where exact lumping applies, the record is pure overhead, as expected.
- **Near-lumpable (the decisive case):** the record-based L1 arm is Pareto-nondominated *and* certified (certificate 0.114, actual TV 8.5e-5) and 1.98x cheaper on expansion ops, the right shape, but it lands at 1.20x on the pre-registered 0.7x total-cost bar because the roughly 1,490-op granule-record overhead is unamortized at this scale. Monte Carlo needs on the order of 60,000x the ops to match the arm's actual accuracy. The idea works on the core operation; the loss is fixed overhead.
- **Non-lumpable (FAR):** the certificate is vacuous (0.114 usable is exceeded; here the bound is 4.87 > 1), Monte Carlo is 24x better on actual accuracy, and the monotone tracking inverts. The record-based arm has no business in this regime.

The delivered win is **not demonstrated** at 98 states. It is a characterized near-miss in the near-lumpable regime (overhead-limited, plausibly scale-amortizable) and a failure in the far regime. Honest negative, pre-registered, reported without spin. The single unproven claim that would flip the verdict is whether the near-miss becomes a win at larger scale where the fixed record overhead amortizes.

### 5.2 The stress test: the obstruction relocates

We then held one near-lumpable scenario family fixed and scaled it up, with equal-budget accounting and a scale sweep (F34-STRESS, witness SHA `55ab0c6c...`, exit 0, all 8 correctness teeth pass, 9/9 pre-registered predictions hit, live red, **closed-hardened**).

**Result 5.2.** Three questions are settled.

1. **The near-miss flips at scale.** The flip ratio (record-arm total cost over exact-arm ops) is 0.989 / 0.836 / 0.752 / 0.687 across the four scales; the xlarge value 0.687 clears the 0.7 bar. The fixed granule-record overhead amortizes with scale, exactly as the benchmark hypothesized.
2. **But the win stays False at every scale, because the first-order certificate degrades.** pred(L1) is 0.062 / 0.114 / 0.166 / 0.216 across the scales; it crosses the 0.15 usability bar between medium and large, precisely where the cost bar begins to pass. So the obstruction *relocates* from overhead-amortization (solved by scale) to certificate tightness. This is now the single binding item, and it is what Section 4.2's C_tight was built to address (and does, at xlarge, under the declared accounting).
3. **Monte Carlo is not more accurate than exact tree-expansion.** The exact arm is Fraction-equal to ground truth at every scale, metric-independent. This is settled by verification, not assertion.

One qualification is disclosed and upheld: under a *symmetric* total-cost accounting that also charges the exact arm's partition-refinement setup, the flip is present at all four scales (0.611 / 0.561 / 0.549 / 0.569), not xlarge-only. This weakens the "xlarge-only" narrative; it does not touch the settled conclusions, because the certificate-degradation and the MC-versus-exact findings are accounting-independent. The benchmark's asymmetric accounting was fixed in advance, disclosed, and is competitor-favoring (it charges the record arm all its overhead and the exact arm none of its setup), so the flip is if anything conservative for the record arm.

### 5.3 What the demonstration shows

Composing 5.1, 5.2, and 4.2: the record-based reduction is Pareto-nondominated and certified in the near-lumpable regime; its fixed overhead amortizes at scale (5.2); the first-order certificate then becomes the binding constraint (5.2); and a tighter certificate recovers the missing usability factor at the largest scale under a declared accounting convention (4.2). The delivered end-to-end win at a single fully-adjudicated 98-state scale is a near-miss (5.1). We do not claim a delivered harness win. We claim a characterized frontier with the binding obstruction located precisely and one hardened path (C_tight) that addresses it under a stated convention, with the rigorous companion (C_rig) honestly not-yet-usable at that scale.

---

## 6. Discussion

### 6.1 The honest bottom line

Three things are true together and none of them is the tempting headline. The record captures distinctions scalar summaries conflate (Section 3, hardened for the abstract and stochastic cases). That information carries a thermodynamic cost (Section 2, hardened). Whether keeping the record buys a delivered reduction win is regime- and scale-dependent and, at scale, gated by certificate tightness (Section 5, a characterized negative at the fully-resolved scale; the binding obstruction is certificate tightness, and Section 4.2's C_tight addresses it under a declared convention).

The value of the granular record is therefore *conditional*, and we can now state the conditions. The record is worth its cost when (i) the modality's scalar family contains no sufficient statistic for the outcome (Theorem 3.4), and (ii) a tight enough certificate exists to certify the reduction where the cheaper scalar bound goes slack (Result 4.1 and 5.2). Both conditions are met in the near-lumpable stochastic regime and fail elsewhere: in exactly-lumpable settings the exact reduction owns the frontier and the record is overhead; in far-from-lumpable settings no certificate is usable and sampling wins; in MOR and transfer learning a stronger legal scalar is already sufficient, so condition (i) fails.

### 6.2 The F39 result and what it does not claim

C_tight (Result 4.1) is the sharpest positive in the delivery arc. It is valid on exact arithmetic, structurally tighter than the first-order budget with an exact factor-2 identity on the mode-pair blocks, and it relocates the usable frontier by about one scale, unblocking the stress-test win at xlarge. It is *not* a general certificate theorem: it rides a declared occupancy-weighting convention and is a verified finite-sweep bound on the tested family. The rigorous companion C_rig has a real derivation but is honestly not usable at the largest scale. So C_tight is a genuine, honestly-bounded engineering win on a specific family, not a unification and not a proof that the record-based reduction dominates in general.

### 6.3 Relation to prior art and what stays ceded

The entropy identity is Shannon and Landauer [5] [7]; the uniqueness kernel is Shannon-Khinchin-Faddeev [9] [10]; the per-scalar sufficiency test is Fisher-Neyman and data-processing [PLACEHOLDER: fisher1922mathematical] [6]. The stochastic-lumping machinery is Kemeny-Snell and Zeigler [PLACEHOLDER: kemeny1976finite] [2], and the modern structural discriminators the record beats in M1 are Michel-Siegle and Geiger [PLACEHOLDER: michel2024formal] [PLACEHOLDER: geiger2015optimal]. The stronger scalars that defeat M2 and M3 are the certified reduced-basis energy norm [PLACEHOLDER: rozza2008reduced] [PLACEHOLDER: veroy2003posteriori] and the label-aware kernel two-sample statistic [PLACEHOLDER: gretton2012kernel], with the label-free impossibility due to Zhao and colleagues [PLACEHOLDER: zhao2019learning]. What is not in any of these as a unit is the specific combination this paper measures: the record-as-thermodynamic-carrier with three pairwise-distinct scalar summaries and a tower arrow (Section 2); the family-quantified three-regime boundary with faithful cross-modality classification (Section 3); and the located, certificate-tightness-gated delivery frontier (Sections 4 and 5).

### 6.4 Threats to validity

Every result is (a) research artifact: machine-checked in isolation, not wired to a production consumer. The thermodynamic pricing is ceded physics, not measured. Several load-bearing prior-art comparisons (Michel-Siegle, Geiger, Sagawa-Ueda, FDOR) are transcriptions pending paper-in-hand verification; the manuscript wording is fenced accordingly and the placeholder set must clear refverify before render. The benchmark reaches 98 states; the scale-amortization is proven on a scaled scenario *family* (Result 5.2), not on a distinct large real model. The C_tight win at xlarge rides a declared accounting convention, and the fully-rigorous companion is not usable there. The M2/M3 negatives are on finite exact surrogates for continuous PDE and transfer settings; the carry into those modalities with a genuinely tied strongest-scalar pair is unbuilt.

---

## 7. Conclusion and open problems

A model reduction can be summarized by a scalar or carried as a granular record. The record is not free, and it is not always worth its cost. We have measured, rather than assumed, when it is. The record carries a thermodynamic potential (the Landauer entropy of the reduction) that the library's scalars provably cannot express, and that potential is the unique granule-local tower potential of its kind. Whether the record's distinctions beat the strongest legal scalar is governed by a family quantifier: real when no scalar in the modality is sufficient (stochastic lumping), refuted when a stronger legal scalar exists (reduced-basis MOR, transfer learning). Whether the record delivers a practical reduction win is regime- and scale-dependent: a characterized near-miss at the fully-resolved scale, with the binding obstruction relocated by a scale-up stress test from overhead (which amortizes) to certificate tightness, and a hardened tighter certificate that recovers the missing factor on the tested family under a declared convention. We claim no unification theorem and no faster simulator. We claim a measured map of a conditional value.

**Open problems.**

1. Extend the record entropy S beyond uniform input distributions to a general measure (the weighted record), completing the characterization of Section 2.
2. Prove the second-order or occupancy-conditional certificate (the roughly 580x prize) that would make C_rig usable at the largest scale without the declared occupancy-weighting convention, converting the F39 win from a family-specific bound to a general one.
3. Run the delivery benchmark at 10^4 to 10^6 states on a distinct large real model, testing whether the certified near-lumpable near-miss becomes a delivered win where the fixed record overhead is fully amortized and a tight certificate holds.
4. Construct, for MOR and transfer learning, a pair genuinely tied on the *strongest legal scalar family* (an affine A(mu) family making the energy norm illegal at generic mu; a label-aware joint-distribution family) and still record-separated, testing whether the record advantage can be pushed into those modalities or whether Theorem 3.4 forecloses it there.
5. Resolve the standing reference debt: verify Michel-Siegle, Geiger, Sagawa-Ueda, FDOR, Kemeny-Snell, and the MOR and transfer prior art through the verification protocol, and settle the TMS lumping-chapter pointer discrepancy (chapter 21 versus chapter 22) before any render.

---

## References

Approved keys (present in the portfolio approved-references store; R019-clear). Citations to these render as normal numeric references:

- [1] B. P. Zeigler, A. Muzy, and E. Kofman, *Theory of Modeling and Simulation*, 3rd ed. Academic Press, 2018. (`zeigler2018tms`)
- [2] B. P. Zeigler, C. Koertje, and C. Zanni, "The Utility of Homomorphism Concepts in Simulation," *Simulation: Trans. SCS Int.*, 2024. (`zeigler2024homomorphism`)
- [3] B. Zeigler, C. Koertje, C. Zanni, S. Yoon, and G. Dutan, "Advanced Tutorial on Paratemporal Simulation Using Tree Expansion," in *Proc. 2024 Winter Simulation Conf.*, 2024. (`zeigler2024paratemporal`)
- [4] B. P. Zeigler, "Discrete Event Systems Theory for Fast Stochastic Simulation via Tree Expansion," *Systems*, 2024. (`zeigler2024stochastic`)
- [5] C. E. Shannon, "A Mathematical Theory of Communication," *Bell Syst. Tech. J.*, 1948. (`shannon1948mathematical`)
- [6] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. Wiley, 2006. (`cover2006elements`)
- [7] R. Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM J. Res. Dev.*, 1961. (`landauer1961irreversibility`)
- [8] J.-P. Aubin, *Viability Theory*. Birkhauser, 1991. (`aubin1991viability`)
- [9] A. Ya. Khinchin, *Mathematical Foundations of Information Theory*. Dover, 1957. (`khinchin1957foundations`)
- [10] D. K. Faddeev, "On the Concept of Entropy of a Finite Probabilistic Scheme," *Uspekhi Mat. Nauk*, 1956. (`faddeev1956entropy`)
- [11] P. F. Wach, "Study of Equivalence in Systems Engineering within the Frame of Verification," Ph.D. dissertation, Virginia Tech, 2023. (`wach2023equivalence`)
- [12] P. F. Wach and A. Salado, "Theoretical Foundations of Systems Engineering," 2024. (`wach2024theoretical`)
- [13] A. Salado and H. Kannan, "A Mathematical Model of Verification Strategies," *Systems Engineering*, 2018. (`salado2018mathematical`)
- [14] P. F. Wach and A. Salado, "Recovering Wymore's Systems Theory in the Context of DEVS," 2021. (`wach2021wymoredevs`)
- [15] P. F. Wach and A. Salado, "Mathematical Foundations for Model-Based Systems Engineering," 2025. (`wach2025mathmbse`)
- [16] T. Cody, "A Systems Theory of Transfer Learning," 2021. (`cody2021transfer`)

Not-yet-approved sources appear in-text ONLY as visible `[PLACEHOLDER: author year]` markers and MUST be verified through refverify before render (candidate metadata staged in `flagship_candidate_refs.bib`): Bennett 1982, Szilard 1929, Sagawa-Ueda 2009, Faist-Dupuis-Oppenheim-Renner 2015, Michel-Siegle 2024, Geiger et al. 2015, Giles 2008, Kemeny-Snell 1976, Courtois-Semal 1984, Buchholz 1994, Gretton et al. 2012, Ben-David et al. 2010, Zhao et al. 2019, Rozza-Huynh-Patera 2008, Veroy et al. 2003, Fisher 1922.

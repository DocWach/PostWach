# Foundations: SMDP / Holding-Time Morphism (GAP-SMDP)
**Provenance:** Claude (Anthropic, claude-sonnet-4-6, claude-sonnet-4-6), 2026-07-12.
**Status:** Research candidate — prior-art grounding pass. All claims R016 (a) unless otherwise noted.

---

## Background

The stochastic round (Step 4 / Round 1, sessions 2026-07-09 and 2026-07-11) derived the stochastic-family record-separation theorem and closed it via tri-model RBW + Fable + Codex domain-critic. Three gaps were declared at closure: **GAP-GIRY** (continuous/uncountable state extension), **GAP-SMDP** (semi-Markov / holding-time), and **GAP-LAX-ACTION** (lax action / RL-action-component). This document grounds GAP-SMDP.

**The fence:** The finite-discrete stochastic record used a joint semi-Markov carrier Q_p: S x I -> Dist(S x T), but the stochastic *Step 4* derivation treated tau as a constant (the CTM/Markov special case, where holding times are exponential and the only free parameter per edge is the rate). The stochastic record DR^s(m) = (K1; K2^Sigma; K3^Sigma) grades what survives on the PTS (probability transition structure) axis. The TTS (transition time structure) was held constant, making Zeigler Theorem 22.1 condition 2 exact and invisible in the record. GAP-SMDP asks whether the structural record extends to grade condition 2 when holding-time distributions are non-exponential and the lumping map deforms them.

---

## (a) CEDE List

The following items are prior art; the candidate delta must not re-derive them.

**C1. Zeigler TMS ch22 Theorem 22.1 (exact SMDP homomorphism, `zeigler2018tms`).**
The full exact-morphism condition for DEVS Markov / timed non-deterministic models requires BOTH:
(1) probability structure: Pr'(h(s1),h(s2)) = Pr(s1,s2) for all pairs; and
(2) timing structure: tau'(h(s1),h(s2)) = tau(s1,s2) (holding-time pdf equality).
When h is not 1-1, both conditions require every block-internal state to have identical outgoing distributions -- a uniformity requirement for probabilities AND for timing. This is the authoritative DEVS SMDP exact-morphism source.

**C2. Zeigler TMS ch22 Section 22.5 approximate morphism / (E,D)-space (`zeigler2018tms`).**
The approximate morphism framework defines LumpSTD = max_{B,B'} STD(m_i) where m_i = sum_{j in B'} p(i,j) -- a scalar metric of departure from exact *probability* lumpability. The (E,D)-space pairs prediction error E against this departure D. This is CEDED as the behavioral-error vs probability-lumpability framework. It does NOT define an analogous metric for holding-time distribution departure.

**C3. Zeigler TMS ch22 Theorem 22.2 (Kemeny-Snell exact lumpability, `zeigler2018tms`).**
LumpSTD = 0 is the exact-lumpability criterion for the probability structure. Corollary 22.1: probabilistic behaviors agree modulo the partition. This is the DEVS-internal Kemeny-Snell statement; CEDED in full.

**C4. Ravindran-Barto 2003 SMDP model homomorphisms [VERIFY: `ravindran2003smdp` -- NOT in approved.bib].**
Ravindran and Barto defined SMDP homomorphisms for hierarchical RL: a pair (f, g) mapping states and actions such that the reduced model preserves reward structure and transition distribution (both next-state probability AND holding-time distribution). Their Kr / Kp residuals measure departure from exact next-state and reward correspondence but do NOT grade holding-time distribution survival. SMDP homomorphism = exact structural match on timing; no graded metric for partial survival.

**C5. Zeigler TMS ch21 semi-Markov model class (`zeigler2018tms`).**
DEVS semi-Markov is the most general class: the transition mechanism uses the current phase AND sigma to select next phase AND sigma independently. CTM is the special subclass where sigma is exponentially distributed (memoryless). The stochastic record was derived under CTM assumptions (tau constant per edge). CEDED as the model-class taxonomy establishing that semi-Markov allows distinct per-edge distributions (phase-type, Erlang, Weibull, etc.).

**C6. Standard semi-Markov process theory: Kemeny-Snell strong lumpability ([VERIFY: `kemeny1960finitemc` -- NOT in approved.bib]).**
Strong lumpability of a Markov chain requires that the sum of transition probabilities from any state in block B to all states in block B' is the same for all states in B. For semi-Markov processes, strong lumpability additionally requires that the conditional holding-time distribution given next block B' is the same for all states in B. Both conditions are binary (exact). No graded metric for partial holding-time lumpability exists in the standard theory.

**C7. Phase-type distributions and matrix-exponential approximations ([VERIFY: candidates pending -- NOT in approved.bib]).**
Phase-type distributions (Neuts; also Cox, Erlang subclass) provide a dense family for approximating arbitrary holding-time distributions with PH-distributed representations. They are used in fluid models and SMP analysis but are not a graded morphism framework; they supply the approximation vehicle, not the graded carrier.

**C8. Bisimulation for timed systems / timed automata.**
Strong/weak bisimulation for timed automata (Milner, Cerans, etc. [VERIFY]) requires exact time-matching in the standard form; approximate bisimulation relaxes behavioral divergence but typically with a global epsilon tolerance rather than a per-transition structural record. CEDED as the behavioral (D_b) direction; not the structural (D_s) direction.

---

## (b) Candidate Delta

**DELTA: A timing-component structural record T-CORR grading holding-time-distribution survival under lumping.**

### Setup

Let M = <S, delta, PTS, TTS> and M' = <S', delta', PTS', TTS'> be two DEVS Markov models in the general semi-Markov class (not restricted to CTM). Let h: S -> S' be a surjective lumping map.

Theorem 22.1 exact morphism requires (condition 2): for all (s1,s2) in delta, tau'(h(s1),h(s2)) = tau(s1,s2), where tau(s1,s2) is the holding-time pdf for the (s1,s2) transition.

When h is not 1-1 (lumping), this requires ALL (si,sj) in the same block-to-block pair to have IDENTICAL holding-time pdfs. This is the T-uniformity requirement, analogous to the probability uniformity requirement (which Zeigler's LumpSTD already grades).

### Candidate structural record component K_ta

For each ordered block pair (B, B'), define the holding-time marginal induced by h:
- For each state i in B with transitions to states in B', let F_{i,B'}(t) = P[holding time <= t | transition goes to B', current state = i].
- This is the per-state conditional holding-time cdf for transitions from i to block B'.

The exact timing condition requires: F_{i,B'}(t) = F_{j,B'}(t) for all i, j in B and all t (block-internal uniformity).

**Candidate T-record component:** For each block pair (B, B'), define:
```
K_ta(B,B') = W_1(F_{B'|B})   [Wasserstein-1 distance among {F_{i,B'}: i in B}]
```
where W_1 is the Wasserstein-1 (earth-mover) distance on Dist([0,infinity)), and the spread among the conditional cdfs is measured as max_{i,j in B} W_1(F_{i,B'}, F_{j,B'}) or equivalently the radius of the smallest Wasserstein-ball containing {F_{i,B'}}.

Then **LumpSTD_ta = max_{(B,B')} K_ta(B,B')** is the holding-time analogue of Zeigler's LumpSTD for probabilities.

Exact morphism: LumpSTD_ta = 0 iff all block-internal states have identical conditional holding-time distributions for every target block.

### Candidate timing-axis (E_ta, D_ta)-space

Parallel to Zeigler's (E,D)-space (§22.5), the delta proposes:
- **D_ta axis:** departure from exact T-uniformity = LumpSTD_ta (Wasserstein spread of conditional cdfs).
- **E_ta axis:** prediction error on timing-sensitive observables (mean sojourn, absorption time, win/loss time as in Zeigler's attrition example).
- **T-lumpability zone:** the interval [0, D_ta*] where E_ta stays near zero (same zone methodology as §22.5).

The candidate claim (T-ZONE): the (E_ta, D_ta)-space has a non-trivial lumpability zone when holding-time distributions are drawn from a parametric family (e.g., exponential with varying rates, Erlang with fixed order, or phase-type with fixed generator structure). This mirrors the probability-axis zone result from the attrition model.

### Witness sketch (finite, executable)

Take the attrition model of §22.4 but replace the exponential inter-event times with Erlang(2, lambda_i) distributions (phase-type, two-phase, rate lambda_i per unit). The base model has N shooters per side with rates {lambda_i} drawn from a distribution with mean lambda and standard deviation sigma_lambda.

- **Exact T-uniformity:** sigma_lambda = 0 (all identical Erlang(2,lambda)); Theorem 22.1 condition 2 holds; record D_ta = 0.
- **Small departure:** sigma_lambda > 0; holding-time distributions differ by block. The mean finish time of the lumped model (which assigns every shooter the mean-rate Erlang(2, lambda)) diverges from the base model by an amount that depends on both sigma_lambda and the force ratio.
- **Prediction:** For the same force ratio and sample size as Zeigler's §22.5.2 (100:40-60 tanks, 10,000 matrix samples), the T-lumpability zone boundary (D_ta*) should follow a pattern analogous to the probability-axis zone -- well-defined, nonzero, and force-ratio-dependent.

This witness sketch is checkable without a new mathematical proof: it requires simulating the DEVS attrition model with Erlang-distributed shooters and measuring E_ta vs D_ta for sampled sigma_lambda values. The sketch is testable (finite, deterministic structure with stochastic inter-event times).

### Structural record extension (the T-CORR component)

The candidate timing-component structural record entry is:
```
K_ta^Sigma = (LumpSTD_ta, T-zone boundary D_ta*, per-block-pair spread profile)
```
This extends the stochastic record DR^s(m) = (K1; K2^Sigma; K3^Sigma) with an additional axis:
```
DR^smdp(m) = (K1; K2^Sigma; K3^Sigma; K_ta^Sigma)
```

The existing record grades the PTS (probability) axis; K_ta^Sigma grades the TTS (timing) axis. The two axes are independent by Zeigler's ch21 uncoupling theorem (§21.3.4): decision probabilities and transition times are specified independently in the DEVS semi-Markov model. This independence is the structural justification for treating K_ta^Sigma as a new INDEPENDENT coordinate rather than a correction to K2^Sigma or K3^Sigma.

### Expected gap pattern

Exactly parallel to the PTS axis: the scalar LumpSTD_ta collapses variation in the PROFILE of per-state conditional cdfs. States i,j in block B with the same LumpSTD_ta may have different profile shapes (e.g., one is bimodal, one is skewed). A granular record K_ta^Sigma preserving the per-state conditional cdf shape (not just the spread scalar) strictly separates cases that the scalar collapses. This is the same CODY-IND / record-separation pattern: the scalar is a do-not-rank summary; only the granular record distinguishes morphisms that behave differently on timing-sensitive observables.

---

## (c) Reference Verification [VERIFY]

The following candidate references are required for this delta. None are currently in approved.bib (confirmed by search). All marked [VERIFY] pending Byzantine-Bayesian protocol (R019/R109).

**[VERIFY-1] ravindran2003smdp**
Ravindran, B. and Barto, A. G. (2003). SMDP homomorphisms: An algebraic approach to abstraction in semi-Markov decision processes. *Proceedings of the 18th International Joint Conference on Artificial Intelligence (IJCAI-03)*, pp. 1011-1016.
Relevance: The canonical SMDP homomorphism definition; establishes exact structural correspondence for the RL case; CEDE C4.

**[VERIFY-2] kemeny1960finitemc**
Kemeny, J. G. and Snell, J. L. (1960). *Finite Markov Chains*. Van Nostrand, Princeton.
Relevance: Strong lumpability definition for Markov chains; CEDE C6. Note: the Kemeny-Snell lumpability is already used in Step 4's three-object split (postwach-01 archive §3); this is the authoritative source.

**[VERIFY-3] barbu2009semi**
Barbu, V. S. and Limnios, N. (2009). *Semi-Markov Chains and Hidden Semi-Markov Models toward Applications*. Springer, New York. (Lecture Notes in Statistics 191).
Relevance: Standard reference for semi-Markov process theory including holding-time structure; already cited in Zeigler TMS ch21 footnote 1. CEDE C5/C6.

**[VERIFY-4] neuts1981phtype** (or equivalent phase-type reference)
Neuts, M. F. (1981). *Matrix-Geometric Solutions in Stochastic Models: An Algorithmic Approach*. Johns Hopkins University Press.
Relevance: Phase-type distribution theory; CEDE C7 (approximation vehicle for holding-time distributions).

**[VERIFY-5] villani2009optimal** (or equivalent Wasserstein reference)
Villani, C. (2009). *Optimal Transport: Old and New*. Springer, Berlin. (Grundlehren der mathematischen Wissenschaften 338).
Relevance: Wasserstein-1 distance for the K_ta metric; also used in Step 4's Dobrushin-contraction framing.

---

## (d) Open Questions

**OQ-1 (clean extension vs new carrier).** The stochastic record DR^s(m) lives on the PTS carrier. The timing record K_ta^Sigma would live on the TTS carrier (a family of probability distributions over [0,infinity) indexed by block-pairs). These two carriers are mathematically distinct objects (Dist(S x S) vs Dist([0,infinity))^{S x S / h}). Is DR^smdp a product record on two independent carriers, or does it require a joint carrier that couples PTS and TTS? Zeigler §21.3.4 argues the independence is a DESIGN CHOICE of the DEVS semi-Markov class (not a mathematical necessity); for general SMPs the coupling may exist (the conditional cdf F_{i,B'} already conditions on the next block, which is governed by the PTS). This is the primary open structural question.

**OQ-2 (appropriate distance on Dist([0,infinity))).** Wasserstein-1 is proposed above, but the choice matters: W_1 is a metric on distributions over metric spaces and requires a ground metric on [0,infinity). The natural choice is the absolute difference |t1-t2| (earth-mover interpretation is mean-shift distance). But W_2, total variation, or KL divergence may be more natural for different observables (mean sojourn vs absorption probability vs tail events). The (E_ta, D_ta) zone shape will depend on this choice. An empirical investigation parallel to §22.5 is needed to determine which distance is most predictive.

**OQ-3 (T-ENRICH: does T-CORR survive into the institution?).** The Unification candidate (Foundations_Unification_2026-07-11) showed T-ENRICH honestly DEMOTED: timing enrichment failed all three payoff witnesses in the 3/2-institution framing. Does K_ta^Sigma face the same obstruction? Specifically, does the quantitative institution that co-locates (K2^Sigma, K3^Sigma, D_b) admit a natural extension to co-locate K_ta^Sigma, or does the timing axis require a separate institution (or a separate bridge morphism)? This question is directly analogous to the T-ENRICH demotion and may resolve in the same direction.

**OQ-4 (connection to Girard-Pappas metrics, `girard2007metrics`).** Girard and Pappas define approximate bisimulation for continuous-time systems with a global epsilon on behavioral distance. The D_b axis in the current framework already uses their approach for the behavioral side. Does the timing-axis D_ta correspond to a per-transition approximation of their epsilon, or does it require a separate notion? If D_ta and epsilon_GP can be related, the (D_ta, D_b) bivariate zone would directly extend the Girard-Pappas framework into the structural axis -- a clean integration point.

**OQ-5 (relationship to the Step 3 timed record, K_ta^inst).** Step 3 derived D_inst^t = absorbed K2-side + independent K_3^inst,t (the instantaneous timed degree). K_ta^Sigma is about holding-time DISTRIBUTION survival under lumping, not instantaneous state-to-state timing correspondence. Are these the same concept at different levels, or genuinely distinct? The Step 3 result fenced timing as IRREDUCIBLE (H-T1), meaning the timed record cannot be reconstructed from the untimed record. K_ta^Sigma should be consistent with this fence: lumping can deform holding times independently of how it deforms the state-transition structure.

---

PROVENANCE: claude-sonnet-4-6 (Anthropic, claude-sonnet-4-6), 2026-07-12.
Research candidate -- all claims R016 (a). References [VERIFY-1] through [VERIFY-5] NOT in approved.bib as of 2026-07-12; do not cite until R019 protocol complete.

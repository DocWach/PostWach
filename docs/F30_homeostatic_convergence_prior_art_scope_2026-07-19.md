# F30 Reopen -- Homeostatic Convergence Prior-Art Scope (Synthesis Adjudication)

**Date:** 2026-07-19
**Scope:** F30 reopen -- does WySE's resource-aware homeostatic re-equilibration carry a novelty delta over the assembled cybernetics / stability / viability prior art, or does it relabel Ashby ultrastability (and, pending refverify, Friston active inference)?

## STATUS
**(a) research artifact** (R016). This is a prior-art scoping memo and adjudication over a proposed reopen; no capability is built, demonstrated, or integrated. The three delta claims are conjectures under scope decision, not results. F36 (record-separation) is referenced as this session's spine but is itself an in-progress result on the reduction/Monte-Carlo layer, not a shipped theorem.

## PROVENANCE
Per R018. **Synthesis / adjudication:** Anthropic Claude (Opus 4.8, 1M), access mode Claude Code CLI subagent, 2026-07-19. **Cluster searchers:** Anthropic Claude (Sonnet class) with WebSearch / WebFetch tool access, 2026-07-19, delegated by the orchestration script; the synthesis agent (Opus 4.8) records this delegation. Cluster JSON authored by the searchers; verdicts, refined claim, and recommendation authored by the synthesis agent. No claim below is refverify-cleared; the refverify queue (below) is the gate before any manuscript use.

---

## Cluster 1 -- Cybernetics / Homeostasis Foundations

| Work (year) | Owns | Closeness | Record or scalar |
|---|---|---|---|
| Cannon, *Organization for Physiological Homeostasis* / *Wisdom of the Body* (1929/1932) | Coins "homeostasis": stable internal milieu (scalar ranges) held against perturbation via coordinated physiological response | 2 | Scalar per regulated quantity; no unified record |
| **Ashby, *Design for a Brain* (1952/1960)** | **Ultrastability: fast viability loop + slow step-function parameter resample until an attractor keeps every essential variable in the "Alive Box." Direct formal ancestor of expansion-triggered re-equilibration.** | **5** | **Scalar-per-variable; Alive Box = product of independent scalar intervals; no merge-record, no acceptance relation over a structured tuple** |
| Ashby, *Introduction to Cybernetics* (1956) | Law of Requisite Variety: regulator variety >= disturbance variety; underpins why new disturbance dimensions break an equilibrium | 3 | Scalar (variety = count of distinguishable states) |
| Beer, *Brain of the Firm* (1972) | Viable System Model: five-subsystem recursive homeostatic architecture preserving organizational identity across perturbation | 3 | Scalar / qualitative; viability is a binary predicate; no structured invariant record |
| Powers, *Behavior: The Control of Perception* (1973) | Perceptual Control Theory: behavior controls perception to a hierarchical reference; reorganization (slow loop) alters structure on persistent intrinsic error. Closest two-timescale cognitive analog. | 3 | Scalar controlled variables and set-points; no merge-record invariant |
| Nicolis & Prigogine, *Self-Organization in Nonequilibrium Systems* (1977) | Dissipative structures: far-from-equilibrium open systems sustain low-entropy attractors; bifurcation selects among stable structures | 2 | Neither; thermodynamic invariant, no acceptability criterion |
| Schrodinger, *What is Life?* (1944) | Negentropy: living order maintained by importing negative entropy; thermodynamic motivation for homeostasis theory | 1 | Neither; statistical thermodynamics, no control invariant |

**Closest in cluster:** Ashby (1952/1960) -- ultrastability with step-function reconfiguration and Alive-Box attractor convergence.
**What WySE would cede here:** the fast-loop / slow-reconfiguration two-timescale architecture (Ashby); behavior-as-control-of-internal-signal-to-reference (Powers); perturbation-drives-out-of-basin (Ashby Requisite Variety, Prigogine bifurcation); identity-preserving recursive homeostasis of organizations (Beer); thermodynamic motivation (Schrodinger, Prigogine).
**Relabel risk:** HIGH. A cybernetics-literate reviewer reads WySE's re-equilibration loop as ultrastability by another name and will demand what WySE adds beyond Ashby. Without the record/scalar distinction and the signature-expansion perturbation model foregrounded, this cluster owns the whole idea at the level of abstraction most readers apply.

## Cluster 2 -- Stability / Viability / Attractor Dynamics

| Work (year) | Owns | Closeness | Record or scalar |
|---|---|---|---|
| Lyapunov (1892) | Scalar certificate V>0, dV/dt<=0 proves convergence to a fixed point under autonomous dynamics; gold standard, no exogenous input | 2 | Scalar V: R^n -> R |
| LaSalle (1976) | Invariance principle: convergence to the largest invariant subset of {dV/dt=0}, i.e. an omega-limit SET not necessarily a point | 3 | Scalar V; omega-limit set is geometric, not a structured record |
| **Aubin, *Viability Theory* (1991); survey SIAM JCO 1990** | **Viability kernel Viab(K): largest set of initial states from which a controlled trajectory stays in constraint set K forever; subsumes homeostasis / confinement / adaptation as staying-in-K** | **4** | **Geometric set membership (K subset R^n / differential inclusion); no record invariant; viability certified by set containment, not a tuple-valued merge record** |
| Lohmiller & Slotine, contraction analysis (1998) | Matrix Riemannian metric M(x,t)>0 certifies incremental exponential stability; all trajectories converge to one trajectory | 2 | Matrix certificate; trajectory-to-trajectory; no tuple invariant |
| Sontag, ISS (1989); Sontag & Wang (1996) | Input-to-state stability: scalar ISS-Lyapunov function bounds state by class-KL decay + class-K gain on input norm; magnitude-bounded disturbance | 3 | Scalar V: R^n -> R+; perturbation = magnitude-bounded signal, NOT signature change |
| Prajna & Jadbabaie, barrier certificates (HSCC 2004) | Scalar barrier B(x) whose zero level-set separates initial from unsafe set; forward set-invariance (safety analog of Lyapunov) | 2-3 | Scalar B(x); geometric level-set, no record |

**Closest in cluster:** Aubin viability theory (1991) -- viability kernel as the general staying-in-K object; the most general set-membership framing of "keep the system inside its acceptable region."
**What WySE would cede here:** the entire staying-inside-a-constraint-region formalism (Aubin subsumes homeostasis as a special case), exogenous-input stability (Sontag ISS), and limit-set (not point) convergence (LaSalle, Lohmiller-Slotine).
**Key structural gap this cluster leaves:** every certificate here is scalar, vector, matrix, or geometric-set; NONE is a structured record with a relational acceptance predicate. ISS treats perturbation as a magnitude-bounded signal, never as a change of input TYPE / signature. That is the seam WySE claims.

## Cluster 3 -- AI / Energy-Based / Predictive-Processing (searcher cluster referenced; NOT DELIVERED to synthesis)

The orchestration delivered cluster JSON for clusters 1-2 only; cluster 2 JSON was truncated and clusters 3-4 (predictive-processing / energy-based / equilibrium-network) did not reach the synthesis agent as structured records. This is a **material scope gap**: Friston active inference, Deep Equilibrium models (DEQ), and modern Hopfield networks are the co-contenders that could own delta-3 (structured-state convergence) in a way the classical cybernetics/stability clusters do not. They are therefore placed in the refverify queue as MUST-CLEAR-BEFORE-MANUSCRIPT, and the overall verdict below is conditioned on them.

**Provisional read (unverified, from prior knowledge -- flagged as a HUNCH per [[feedback_measure_not_assume_llm_intuition]], not a measurement):**
- **Friston active inference / free-energy principle:** re-equilibration by minimizing variational free energy over a generative model; the "invariant" is a probabilistic belief state (a structured object, not a scalar), and precision-weighting resembles resource-aware weighting. This is the single most dangerous co-contender for delta-1 and delta-3 and MUST be searched and refverified before any manuscript. If Friston's belief-state convergence already separates equilibria that a scalar free-energy value conflates, delta-3's novelty narrows sharply.
- **DEQ (Bai, Kolter, Koltun 2019) / modern Hopfield (Ramsauer et al. 2020):** fixed-point / energy-minimizing convergence to a structured state (a vector/matrix pattern), with attractor semantics. These own "convergence to a structured equilibrium under a learned energy," but their equilibrium object is a flat tensor, not a typed merge-record with a Kannan acceptability predicate, and their perturbation is a value change, not a signature expansion.

## Cluster 4 -- (reserved; not delivered to synthesis)

Not delivered as structured records. Any content here (e.g. adaptive-control / meta-learning re-parameterization, MDP/homeostatic-RL) is subsumed under the refverify gate before use.

---

## Delta Verdicts

### Delta 1 -- record-invariant essential variables (homeostasis preserves a GRANULE-RECORD invariant, vs scalar/vector essential variables/certificates)

**SURVIVES (conditionally).** Every work in clusters 1-2 certifies with a scalar (Lyapunov, ISS, barrier, Ashby Alive-Box-per-variable, requisite-variety count), a vector/product of scalar intervals (Ashby Alive Box), a matrix (contraction), or geometric set membership (Aubin, LaSalle). The closest, Ashby's Alive Box, is explicitly a Cartesian product of INDEPENDENT scalar intervals with no coupling and no acceptance relation over a structured tuple. A typed merge-record with relationally interdependent components and a membership predicate is genuinely absent from this assembled prior art. The survival is CONDITIONAL because the AI cluster (Friston belief state, DEQ / Hopfield structured equilibria) was not delivered; those are structured-state convergers and could partially pre-empt "structured, not scalar." What almost certainly stays even against them: the merge-record being a TYPED tuple with a Kannan acceptability POSET predicate, not a flat tensor or a probability vector. Load-bearing distinction to state explicitly: structured-record acceptance predicate vs any scalar/vector/tensor certificate.

### Delta 2 -- new-context = signature expansion (typed as WySE D_s^Sigma signature expansion, giving a named perturbation class the generic attractor theory lacks)

**SURVIVES, but WEAK as a standalone.** Correct on the facts: Ashby, Prigogine, Aubin, and Sontag/ISS all model perturbation as a change to the VALUES of existing variables (disturbance to state, magnitude-bounded input, bifurcation parameter), never as an EXPANSION of the input signature (new dimensions changing the TYPE of the input space and invalidating the existing acceptance relation). No assembled work formalizes perturbation at the type/signature level, so the claim is true. But "name a perturbation class the generic theory lacks" is a modeling contribution, not a theorem; on its own it reads as terminology unless it DOES something. It earns its place only by being the thing that TRIGGERS the record's re-typing and thereby feeds F36 (delta 3). Keep it as the perturbation model that sets up the separation result, per [[research_wyse_role_dimensionality]] (signature reduct/expansion + level move as a functor between signature indices); do NOT sell it as an independent novelty. [[feedback_goal_first_formalisms_earn_role]]: the signature-expansion formalism is a tool, not the objective.

### Delta 3 -- F36 on the convergence layer (the record SEPARATES homeostatic equilibria that a scalar stability margin -- spectral gap / contraction rate / Lyapunov value -- CONFLATES)

**SURVIVES and is the SPINE.** This is the load-bearing delta and the primary defense against the Ashby relabel charge. No assembled work has any counterpart: because every certificate is scalar/vector/matrix/set, any two equilibria with equal scalar margin (equal Lyapunov value, equal contraction rate, equal spectral gap, equal Alive-Box membership) are indistinguishable to those frameworks. F36 demonstrates the scalar picture is STRICTLY COARSER: there exist systems Ashby / Lyapunov / ISS classify as equivalent that the WySE merge-record distinguishes. That is a real, witnessable separation (a strict refinement of an equivalence), and it is exactly the kind of record-vs-scalar separation established on the reduction/Monte-Carlo layer in [[research_wyse_monte_carlo_reduction]]. CAVEAT: F36 must be witnessed on the CONVERGENCE/homeostatic layer specifically (two homeostatic equilibria, equal scalar margin, record-distinguished), not merely cited by analogy from the reduction layer; and it must survive the Friston check (does variational free-energy-minimization already separate them via the belief state?). Conditional on those two, delta-3 carries.

---

## Overall Verdict: **PARTIAL** (precisely: relabels-except-the-record-separation)

Honestly stated: the re-equilibration STORY -- two-timescale loop, perturbation ejects the system from its basin, reconfigure until an attractor keeps essential variables in bounds -- is owned by Ashby (1952) at the scalar level and generalized by Aubin (viability kernel) and Sontag (ISS). If WySE presents that story as the contribution, it RELABELS. What genuinely survives is the RECORD-level refinement: a typed merge-record with a Kannan acceptability predicate (delta 1) and its consequence that the record separates equilibria the scalar margin conflates (delta 3, F36). Delta 2 is a true-but-supporting modeling move that earns its keep only as the trigger for delta 3. So: not "carries" (the loop is not novel), not "relabels" (F36 is a real strict refinement) -- **PARTIAL**, with the surviving delta narrowed to record-separation-of-equilibria.

**Lens 2 (iPhone / harness) note:** even where component-novelty is modest, the harness value can carry -- WySE would harness Ashby ultrastability + Aubin viability + (pending) Friston free-energy and deliver them as a typed, acceptability-gated, signature-expansion-aware re-equilibration object usable inside the WySE/DEVS stack for AI-context perturbation. That is a legitimate positioned-integration story ([[feedback_two_lenses_novelty_iphone.md]]). But lens 2 does NOT rescue an overclaimed lens-1 novelty; the manuscript must foreground F36 as the delta and frame the loop as harnessed prior art, not invented.

## Closest Single Work We Most Must Cede / Beat

**W.R. Ashby, *Design for a Brain* (1952/1960) -- ultrastability** is the closest DELIVERED contender (closeness 5) and the one a reviewer will name first. **BUT the single work we most must BEAT is not yet verified: Friston's active inference / free-energy principle**, because it is the only candidate that plausibly already convergences a STRUCTURED (belief-state) invariant and could pre-empt delta-1 and delta-3 in a way Ashby (strictly scalar-per-variable) cannot. Verdict on "closest single work": we CEDE the two-timescale loop to Ashby and BEAT Ashby via the record/scalar F36 separation; we CANNOT yet claim to beat Friston -- that adjudication is blocked pending refverify. Treat Friston as the gating must-beat.

## Refined Witnessable Claim (narrowed so the surviving delta is load-bearing)

> There exist homeostatic systems whose re-equilibration, under a WySE D_s^Sigma signature expansion of the input context, converges to distinct equilibria that carry EQUAL scalar stability margin (equal Lyapunov value / contraction rate / spectral gap / Ashby Alive-Box membership) yet are SEPARATED by the WySE granule merge-record under its Kannan acceptability predicate. The merge-record is therefore a strict refinement of every scalar/vector/matrix/set homeostatic certificate in the classical cybernetics and stability literature (F36 on the convergence layer).

Witness obligation: exhibit two such equilibria, equal on a named scalar margin, record-distinguished, with the signature-expansion perturbation that produced them; per [[feedback_problem_first_not_solution_first]] derive the separation, do not back-fill it onto an assumed pair.

## Refverify Queue (route BEFORE any manuscript use; R019/R109)

Priority order (must-beat first):
1. **Friston active inference / free-energy principle** -- e.g. Friston, "The free-energy principle: a unified brain theory?" (Nat. Rev. Neurosci. 2010); Friston et al. active-inference formulations. GATING: does belief-state convergence separate equilibria a scalar free-energy conflates?
2. **Aubin viability theory** -- Aubin, *Viability Theory* (Birkhauser 1991); Aubin, "A Survey of Viability Theory" (SIAM JCO 28(4):749-788, 1990, DOI 10.1137/0328044). Verify page range, DOI, ISBN 978-0-8176-3571-8.
3. **DEQ** -- Bai, Kolter, Koltun, "Deep Equilibrium Models" (NeurIPS 2019).
4. **Modern Hopfield** -- Ramsauer et al., "Hopfield Networks is All You Need" (ICLR 2021 / arXiv 2020).
5. **Ashby** -- *Design for a Brain* (Chapman & Hall 1952, 2nd ed. 1960); *An Introduction to Cybernetics* (1956). Verify editions/publisher.
6. **Powers** -- *Behavior: The Control of Perception* (Aldine 1973).
7. **Sontag ISS** -- Sontag, IEEE TAC 34(4):435-443, 1989, DOI 10.1109/9.28018; Sontag & Wang, IEEE TAC 41(9):1283-1294, 1996.
8. **Lohmiller & Slotine** -- Automatica 34(6):683-696, 1998, DOI 10.1016/S0005-1098(98)00019-3.
9. **Prajna & Jadbabaie** -- HSCC 2004, Springer LNCS 2993:477-492, DOI 10.1007/978-3-540-24743-2_32.
10. Beer *Brain of the Firm* (1972); Nicolis & Prigogine (1977); Schrodinger (1944); Cannon (1929/1932); LaSalle (1976); Lyapunov (1892, T&F transl. 1992).

None of the above is approved yet; each is a `[PLACEHOLDER]` until it clears the Byzantine-Bayesian protocol into `approved.bib` per R019/R109.

## Recommendation: **run-with-narrowed-delta**

**Why.** The reopen is worth running, but ONLY with the claim narrowed to record-separation-of-equilibria (delta 3, backstopped by delta 1). Reasons: (1) The full re-equilibration-loop story relabels Ashby and would draw an immediate reviewer rejection; running it as-scoped is not defensible. (2) The F36 record-vs-scalar separation is a real strict-refinement result with a clean witness obligation and a direct sibling already established on the reduction layer ([[research_wyse_monte_carlo_reduction]]); that is a genuine, publishable delta. (3) The scope is not yet safe to run at full breadth because the AI/predictive-processing cluster (Friston, DEQ, Hopfield) was NOT delivered to synthesis; Friston in particular could pre-empt the structured-state novelty. Therefore: run the narrowed F36-on-convergence claim, but GATE it on the Friston refverify + a dedicated search of the predictive-processing / energy-based cluster before manuscript. If Friston already separates the equilibria, drop to scope-more. Frame the loop as harnessed prior art (lens 2), foreground F36 as the delta (lens 1). Do not present delta 2 as standalone novelty.

## Ties
- [[research_resource_aware_homeostatic_wyse]] -- the resource-aware homeostatic WySE thread this reopen serves; re-equilibration under resource constraint is the application, F36 is the theorem.
- [[research_wyse_monte_carlo_reduction]] -- F36 origin (record separates what a scalar conflates) on the reduction/Monte-Carlo layer; delta 3 ports that separation to the convergence/homeostatic layer.
- [[research_wyse_role_dimensionality]] -- signature expansion (delta 2) as a reduct/expansion + level move, candidate functor between signature indices; the type-level perturbation model.
- [[feedback_measure_not_assume_llm_intuition]] -- the Friston provisional read is a HUNCH, not a measurement; refverify before use.
- [[feedback_two_lenses_novelty_iphone]] -- lens 1 (F36 carries) + lens 2 (harness Ashby/Aubin/Friston into an in-hand typed re-equilibration object).
- [[feedback_goal_first_formalisms_earn_role]] / [[feedback_problem_first_not_solution_first]] -- delta 2 earns its role only as F36's trigger; derive the separating pair, do not back-fill it.

---

## AI-context cluster (gap-closer, 2026-07-19)

**PROVENANCE (R018):** Opus 4.8, Anthropic, Claude Code CLI, 2026-07-19, WebSearch/WebFetch-grounded (Nature/nrn2787, arXiv 1909.01377, arXiv 2008.02217, NeurIPS 2011 proceedings, eLife). Metadata pinned to authoritative publisher/arXiv/CrossRef pages; the substantive "what the invariant IS" reads are grounded in the papers' own abstracts + primary formalisms, flagged where a full-text pass is still owed. **STATUS (R016): (a) research artifact** -- scoping/adjudication, nothing built or demonstrated. No entry below is refverify-cleared; the queue at the end is the gate.

This section closes the cluster that clusters 3-4 above left undelivered. It is the highest relabel-risk cluster because Friston plausibly converges a STRUCTURED invariant, which the classical scalar-certificate literature does not.

### The works

| Work (year) | Venue | Owns | Closeness | Record or scalar |
|---|---|---|---|---|
| **Friston, "The free-energy principle: a unified brain theory?" (2010)** | Nat. Rev. Neurosci. 11:127-138, DOI 10.1038/nrn2787 | **Re-equilibration by minimizing variational free energy F over a generative model; homeostasis/allostasis recast as suppressing surprise (prediction error) so the agent stays in its expected ("phenotypic") states. The convergence target is a recognition density q(states) that approximates the Bayesian posterior. The single most dangerous co-contender: its invariant is genuinely STRUCTURED (a probability density, not a scalar).** | **5** | **BOTH, at different layers. The OBJECTIVE F is a scalar (a free-energy value, an upper bound on surprise). The FIXED POINT is structured: a recognition density q over hidden states / a set of posterior beliefs + precisions. It is a probability measure, NOT a typed merge-record, and there is NO acceptability predicate over a poset -- "acceptability" is folded into surprise minimization (staying in high-prior states), a real-valued expectation, not a relational membership test on a tuple.** |
| Bai, Kolter, Koltun, "Deep Equilibrium Models" (2019) | NeurIPS 2019 (spotlight); arXiv 1909.01377 | Network output as the fixed point z* = f_theta(z*; x) of a weight-tied layer, found by root-finding; convergence to a structured equilibrium STATE under an input x. Owns "a deep net IS an equilibrium solver." | 3 | Scalar-free but flat: z* is a vector/tensor in R^d. No typed record, no acceptability predicate. Perturbation = a new input VALUE x (same signature), never a signature/type expansion of the input space. |
| Ramsauer et al., "Hopfield Networks is All You Need" (2020) | arXiv 2008.02217; ICLR 2021 | Continuous modern Hopfield net: energy-based attractor / associative memory; update rule = transformer attention; three fixed-point regimes (global average, metastable subset-average, single-pattern). Owns "attention IS energy-minimizing retrieval to a stored attractor." | 3 | Energy is a scalar; the retrieved fixed point is a vector (a stored pattern or a convex combination of patterns). No typed record, no acceptability poset. Separation among patterns is by energy-basin geometry, not a relational predicate. |
| Keramati & Gutkin, "A Reinforcement Learning Theory for Homeostatic Regulation" (2011) | NIPS 24:82-90 (proceedings 9778d5d2...) | Drive-reduction RL: reward := reduction of drive, where drive = a distance (norm) of the internal-state vector from a setpoint vector; proves reward-maximization == physiological stability. Owns "homeostasis IS RL to a setpoint." | 4 | SCALAR drive (a p-norm/HD distance of a state vector from a setpoint). Explicitly the scalar-conflation object F36 beats: two internal states equidistant from setpoint have equal drive. No record, no acceptability predicate. |
| Keramati & Gutkin (follow-up), "Homeostatic reinforcement learning for integrating reward collection and physiological stability" (2014) | eLife 3:e04811 | Extends the 2011 model; same drive-as-scalar-deviation core. | 4 | Scalar drive; same as above. |
| Homeostatic RL / predictive-processing agent lineage (e.g. active-inference agents; in-context learning as implicit optimization) | various | Convergence to a policy/belief that minimizes drive or free energy at test time. In-context learning = implicit gradient/optimization at inference. | 2 | Scalar objective; belief-vector or policy invariant. No typed record. ICL bears on "test-time convergence" but not on a structured acceptability invariant -- excluded from delta-3 contention. |

### Closest AI work

**Friston active inference / free-energy principle (2010)** is the closest by a clear margin (closeness 5), and the ONLY AI-cluster work whose converged invariant is genuinely structured (a probability density / posterior belief), not a scalar or a flat vector. Keramati-Gutkin is closest on the *homeostasis* framing specifically but converges a strictly SCALAR drive, so it is a delta-3 confirming instance (it is the scalar F36 refines), not a threat. DEQ and Hopfield converge structured-but-flat vector states with scalar energies; they own "convergence to a structured equilibrium," not "a typed record with an acceptability predicate."

### Q1 -- Does any of these converge a STRUCTURED (non-scalar) invariant, pre-empting delta-1?

**PARTIALLY -- and this NARROWS delta-1 but does not pre-empt it.** Friston DOES converge a structured invariant: a recognition density q over hidden states (posterior beliefs + precisions), which is non-scalar. DEQ and Hopfield converge structured-but-flat vectors/tensors. So the bare form of delta-1 ("the invariant is structured, not a scalar") is NO LONGER a clean novelty against this cluster -- Friston/DEQ/Hopfield already own "structured convergence." What survives is the STRONGER, sharpened form: the WySE invariant is a TYPED merge-record with a Kannan **acceptability POSET predicate** (a relational membership test over interdependent typed components). None of these is that. Friston's invariant is a probability MEASURE (a density on a fixed state space), not a typed tuple, and its "acceptability" is an expectation (surprise), not a poset membership relation; DEQ/Hopfield invariants are unstructured tensors. **Net: delta-1 must be RE-STATED as "typed-record-with-acceptability-poset vs probability-density / tensor / scalar," not as "structured vs scalar." In the re-stated form it survives; in its loose form it is pre-empted by Friston.**

### Q2 -- Does free-energy (or DEQ/Hopfield energy) minimization already SEPARATE equilibria a scalar summary conflates, pre-empting delta-3?

**NO -- and this is the decisive finding.** Two distinctions must be kept apart:

1. **Friston's OBJECTIVE (free energy F) is a scalar.** Two active-inference agents can reach EQUAL free-energy value F yet hold DIFFERENT recognition densities q. So at the level of the scalar summary Friston reports, agents are conflated exactly the way F36 asserts scalar margins conflate equilibria. The scalar F does NOT separate them.
2. **Friston's FIXED POINT (the density q) is structured and CAN differ between two equal-F agents.** So one could ask: does the belief state q already do F36's separating work? Answer: **it does a DIFFERENT and weaker kind of separation.** q separates agents by *probability mass over a fixed, pre-typed state space*. It does NOT (a) re-type the state space under a signature expansion, (b) carry an acceptability POSET, or (c) render two agents with the SAME posterior-density-shape-but-different-granule-provenance as distinct. Concretely: two active-inference agents with equal free energy AND equal recognition density q are, to Friston's machinery, THE SAME equilibrium -- yet the WySE merge-record can still separate them when their granule provenance / merge-history under the acceptability predicate differs. Friston has no object at that layer. So **free-energy minimization does NOT pre-empt delta-3.** It pre-empts a *weaker* claim ("the invariant is a structured distribution") that WySE was never staking. The precise gap: Friston separates by belief MASS on a fixed signature; F36 separates by RECORD STRUCTURE + acceptability predicate under a signature that can EXPAND. Different separation, and strictly finer where signature expansion is in play.

DEQ/Hopfield are cleaner nos: their energy is a scalar and their equilibrium is a flat tensor with no acceptability predicate at all; equal-energy fixed points are conflated with nothing finer to appeal to.

### Q3 -- Does the narrowed claim SURVIVE against this cluster, or does Friston/DEQ/Hopfield own enough to force scope-more?

**SURVIVES-NARROWED.** The F36-separates-equilibria claim, backstopped by the typed-record-with-acceptability-poset invariant, survives -- but two adjustments are now MANDATORY, not optional:
- **Delta-1 must be re-stated** (typed-record-+-acceptability-poset, NOT bare "structured vs scalar"), because Friston/DEQ/Hopfield already own structured convergence. Presenting delta-1 in its loose form WILL be pre-empted by Friston and should be treated as a drafting error.
- **The witness for delta-3 must beat Friston explicitly**, not just Ashby: exhibit two homeostatic equilibria that Friston's machinery treats as identical (equal free energy AND, in the strong version, equal recognition density q on the pre-expansion signature) yet the WySE merge-record separates under the acceptability poset after the signature expansion. Beating Ashby (scalar-per-variable) is easy and already covered; beating Friston (structured density) is the real bar and is what makes the witness load-bearing.

No scope-more is required PROVIDED the witness carries the Friston-strong form. If, on construction, the WySE record cannot separate a pair that Friston's q also fails to separate -- i.e. if every record-separation coincides with a density-separation -- then delta-3 collapses to "a re-encoding of the recognition density" and we DROP to scope-more. That is the specific failure condition to test first, per [[feedback_problem_first_not_solution_first]]: derive the Friston-equal / record-separated pair before claiming it exists.

### Refverify queue (AI-context refs; route BEFORE any manuscript use, R019/R109)

Priority order (gating must-beat first). None approved; each is `[PLACEHOLDER]` until it clears the Byzantine-Bayesian protocol into `approved.bib`.

1. **Friston 2010** -- Friston, K.J., "The free-energy principle: a unified brain theory?", *Nature Reviews Neuroscience* 11(2):127-138, 2010, DOI 10.1038/nrn2787. VERIFY: issue number (2), page range, DOI. GATING must-beat.
2. **Keramati & Gutkin 2011** -- Keramati, M. & Gutkin, B.S., "A Reinforcement Learning Theory for Homeostatic Regulation", *Advances in Neural Information Processing Systems* 24 (NIPS 2011), pp. 82-90. VERIFY: page range (82-90), volume 24, editor list.
3. **Keramati & Gutkin 2014** -- "Homeostatic reinforcement learning for integrating reward collection and physiological stability", *eLife* 3:e04811, 2014, DOI 10.7554/eLife.04811. VERIFY: eLife article id e04811, DOI, author order.
4. **Bai, Kolter & Koltun 2019** -- "Deep Equilibrium Models", *Advances in Neural Information Processing Systems* 32 (NeurIPS 2019); arXiv:1909.01377. VERIFY: NeurIPS 2019 volume/pages vs arXiv-only citation form; spotlight status is informal.
5. **Ramsauer et al. 2020/2021** -- "Hopfield Networks is All You Need", arXiv:2008.02217 (2020); published ICLR 2021. VERIFY: full 16-author list order, ICLR 2021 as the published venue vs arXiv preprint, whether to cite ICLR proceedings or arXiv.

Cross-references: this section resolves the "Cluster 3-4 not delivered" material gap flagged at lines 45-55; the Friston finding confirms the memo's provisional hunch (line 50) was directionally right but IMPRECISE -- Friston's structured invariant is a density, not a record, and does NOT pre-empt delta-3. [[feedback_measure_not_assume_llm_intuition]]: the hunch is now a grounded read, still owing full-text refverify.

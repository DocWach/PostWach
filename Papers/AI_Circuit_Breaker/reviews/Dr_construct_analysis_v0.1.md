# D_r Construct Analysis (v0.1)

**Subject:** Critique of Jeffrey Wallk's proposed context-relevancy distance (D_r) as a third axis on the AI Circuit Breaker morphism-distance metric, and proposal of alternative formulations.

**Inputs read:**
- `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Design_Spec_v4.md` (Wymore-tuple grounding, Sections 1, 2, Layer-1/2/3 architecture).
- `02 My Outreach/2026_SERC_AI4SE_SE4AI/AICB_SERCabstract_2026-05-07.pdf` (Jeffrey's proposed rewrite, four-objective + three-axis + holonic + STPA variant).
- `02 My Outreach/2026_SERC_AI4SE_SE4AI/Wach_Wallk_AICircuitBreaker_Abstract_v0.5.md` (current consensus draft, two-axis, three-objective).
- `Papers/AI_Circuit_Breaker/reviews/white_synthesis_v0.1.md` (existing RBW directive set; the 1-Lipschitz assumption for the D_b chain bound is on the record there).

**Input absent:** `Dr_literature_scoping_v0.1.md` (literature scout has not yet delivered; analysis proceeds without it, with placeholders flagged where external prior art would tighten the claim).

**Uncertainty flag (Type B prior knowledge):** Jeffrey's procedural definition of D_r is reconstructed from the PDF prose, not from a separate specification document. If a separate D_r spec exists in his TDD lineage I have not seen it, conclusions about non-metricity below should be re-checked against that spec.

---

## 1. Critique of D_r as proposed

### 1.1 Jeffrey's construct, restated

From the PDF (page 1 Objective 1, page 3 Layer 1 and Layer 2):

- A five-dimensional operational profile is observed at runtime: WHO (agent identity and authorization scope), WHAT (operational boundary), WHEN (temporal validity window), WHERE (deployment context), WHY (mission intent).
- Each dimension is mapped to an assurance level L1 through L5.
- Layer 1 holds a reference "L1 to L5 anchor" for the certified envelope.
- D_r is computed by comparing the live five-dimensional profile to the Layer 1 anchor.
- The claim, implicit in "three-axis morphism distance" and the bullet "Composition result for observation-mediated morphism chains, extending the two-axis bounds from [Wach et al., CSER 2026] to three axes with five-dimensional relevancy bounds," is that D_r composes with D_s and D_b inside the same chain-bound algebra.

Two construct claims are at stake. **(C1)** D_r is a distance on the same object that D_s and D_b are distances on. **(C2)** D_r participates in the chain composition bound that governs D_s and D_b.

### 1.2 Is D_r a metric?

Type signature, as written: D_r : Profile_op x Profile_ref --> some value, where Profile is an L1-L5 tuple over five WHO/WHAT/WHEN/WHERE/WHY dimensions.

The four metric axioms, evaluated against the procedural definition:

| Axiom | Status | Reasoning |
|-------|--------|-----------|
| Non-negativity, D_r(x,y) >= 0 | Plausibly satisfied | Trivially, if D_r is defined as a sum or max of per-dimension level gaps. Not stated explicitly. |
| Identity of indiscernibles, D_r(x,y) = 0 iff x = y | **Underspecified** | What does "same profile" mean? Same five-tuple of assurance levels, or same underlying operational situation? Two genuinely different operational situations can collapse to the same L-vector if L1-L5 is coarser than the underlying space. So D_r = 0 does not imply x = y. The reverse direction holds only if profile-to-level mapping is deterministic. |
| Symmetry, D_r(x,y) = D_r(y,x) | **Probably violated** | "Compare live profile against L1-L5 anchor" is asymmetric. The anchor is the reference; the live profile is the test. The procedural statement reads as a directional test (is the live profile inside the anchor envelope?), not a symmetric distance. If formalized as "shortfall against anchor," D_r(live, anchor) is not the same quantity as D_r(anchor, live). |
| Triangle inequality, D_r(x,z) <= D_r(x,y) + D_r(y,z) | **Not established** | Depends on the per-dimension level-gap operator and the aggregation rule. If L1-L5 are ordinal categories and D_r aggregates max or sum of ordinal gaps, triangle inequality is plausible but unproven. If D_r is a binary "in-envelope / out-of-envelope" classifier, triangle inequality is meaningless. |

**Verdict on metricity:** As written, D_r is **not** a distance in the metric-space sense. It is most naturally read as either (a) a directional shortfall quantity (live profile relative to a reference envelope), or (b) a categorical classifier (in-envelope vs out-of-envelope, possibly with a graded "degree of out-ness"). Both are useful constructs. Neither is a metric.

This matters for naming, not for utility. Calling it a "distance" creates a false parallel with D_s and D_b that the underlying mathematics does not support.

### 1.3 If it is not a metric, what is it?

The strongest reading of the procedure is that D_r is one of:

- **A preorder predicate over operational profiles.** "Is the live profile dominated by, or contained within, the certified anchor?" L1 <= L_anchor componentwise gives a partial order on Profile-space, and D_r becomes (i) a boolean predicate "live in anchor cone" or (ii) a shortfall measure "minimum lift needed to bring the live profile into the anchor cone."
- **A coverage / set-membership indicator.** Treat Layer 1 not as a point but as a region of Profile-space (the certified envelope). D_r becomes 1 - mu(live, cert), where mu is a containment measure. This is the formal cousin of operational design domain (ODD) coverage in the autonomous-vehicle literature, applicability domain in cheminformatics, envelope of validity in V&V, and assume clauses in assume-guarantee contracts.
- **A classifier with an L1-L5 ordinal scale.** D_r is the categorical assurance grade the operational context warrants given the live profile.

These are not interchangeable. (a) is a relation. (b) is a set-membership or probability-of-membership function. (c) is a categorical mapping. Calling all three "a distance" muddles the construct.

### 1.4 Does the composition claim make sense?

D_s and D_b derive their composition algebra from the morphism h: Z_ai --> Z_real. The chain-level bounds in the design spec Section 2.5 and CSER 2026 are:

    sigma_total <= min(sigma_i)            ==>  D_s_total >= max(D_s_i)   (with D_s = 1 - sigma)
    D_b_total <= sum(D_b_i)                under 1-Lipschitz per stage (per white_synthesis_v0.1.md)

These bounds are theorems about composed morphisms in a chain Z_0 --h_1--> Z_1 --h_2--> ... --h_n--> Z_n. Each h_i is a structure-preserving map between Wymore tuples. The bound applies to the morphism composition, not to anything else.

D_r, as Jeffrey defines it, is **not a property of any single h_i**. It is a property of whether the entire chain (or any subsystem of it) is being applied inside its certified envelope. There is no chain of D_r values to bound; there is one operational profile and one set of envelope references.

A literal three-axis chain bound of the form

    D_r_total <= sum(D_r_i)        ???

requires that each stage i have its own context-relevancy distance D_r_i. What is "the context relevancy of the sensor-to-feature mapping"? What is "the context relevancy of the classification stage"? These do not have natural definitions, because context relevancy is **not a per-stage property of the morphism**, it is a **whole-system property of the deployment**.

You can construct a degenerate chain bound by stipulating "D_r_i is the same constant for every i in the chain, namely the system-level D_r," in which case the sum bound becomes vacuous (D_r_total <= n * D_r, where each term is the same number). That is not a composition theorem; that is a relabeling.

**Verdict on composition:** The composition claim, as written, **does not hold**. D_r does not have a morphism-chain composition algebra parallel to D_s and D_b. It can compose, but only in a different algebra (set intersection of certified envelopes, or contract-conjunction of assume clauses; see F3 and F4 below).

### 1.5 Is "near-isomorphic to the wrong context" a morphism failure or an applicability failure?

This is the crux. Jeffrey is pointing at a real failure mode. The diagnosis is wrong.

In Wymore terms, "low D_s and low D_b" means: relative to the Z_real that the morphism h was specified against, the AI's Z_ai is structurally near-bijective and behaviorally near-output-matching. The morphism h: Z_ai --> Z_real is a high-quality morphism into that Z_real.

"Wrong context" means: the operational situation is governed by a different real system, call it Z_real_op, and h: Z_ai --> Z_real_op is **not certified**. h might still be a good morphism into Z_real (the training reality), but Z_real and Z_real_op are different objects.

This is a **domain-of-applicability failure**, not a morphism-quality failure. The mathematical signature is:

- D_s(h, Z_ai, Z_real) is low (good morphism).
- D_b(h, Z_ai, Z_real) is low (good morphism).
- The deployment is using h to make claims about Z_real_op, not Z_real.
- There is no certified h' : Z_ai --> Z_real_op, so the morphism-quality numbers for the actual deployment are **undefined**, not "high D_r."

The proper response is not "add a third axis on the morphism distance." The proper response is "gate or qualify the entire (Z_ai, h, Z_real) triple before letting any morphism-quality number from it count."

Paul's hypothesis is sustained on the mathematics. Jeffrey's intuition is sustained on the failure mode. They are pointing at the same hazard from different architectural levels.

---

## 2. Underlying intent, precisely

### 2.1 What D_r is meant to detect

Jeffrey's failure mode, in one sentence: **the AI is well-calibrated for a reality that is not the reality it has been deployed into**.

In the existing two-axis framework, this failure is **invisible**, because both axes are computed against the certified Z_real. The instrument cannot see the certified-vs-operational gap because the instrument is measured inside the certified frame.

Concretely, the failure mode that D_s + D_b together provably miss is **silent domain shift**: a deployment in which the operational distribution diverges from the certified domain without producing high D_s or D_b on whatever in-domain data still passes through the instrument.

### 2.2 Worked example

Setup. Take an ECG classifier as the running example, since the abstract is grounded there.

- Z_real(cert) = adult cardiac signal space, sampled from PTB-XL and MIT-BIH. State set: ECG morphology classes plus latent rhythm states. Inputs: lead-II waveforms in the 0.05 to 100 Hz band, adult body habitus. Outputs: rhythm-class labels with confidence.
- Z_ai is trained on Z_real(cert). The certified morphism h: Z_ai --> Z_real(cert) achieves D_s ~ 0.05 and D_b ~ 0.02 on held-out in-domain data.

Deployment. The classifier is fielded into a pediatric cardiology clinic. Pediatric ECG has different normal ranges (faster baseline rate, different QRS morphology, age-dependent T-wave inversion).

- Z_real_op = pediatric cardiac signal space. Different state set (additional age-stratified normal classes), different input distribution.
- The certified h was never validated for Z_real_op.

Now run the two-axis instruments on a stream of pediatric ECG.

- D_s, computed against the certified Z_real ontology, can stay low. The pediatric signals still map to ontology classes (sinus, AF, PVC, etc.), and the AI's lumping pattern is unchanged. The instrument is blind to the fact that the pediatric "sinus" class has different physiological semantics.
- D_b, computed against sensor ground truth in adult bands, is computed on signals that are still in the 0.05 to 100 Hz band. The behavioral output distance is small as long as the AI keeps emitting plausible adult-style labels.

The hazard: the AI confidently labels pediatric signals using adult class semantics. D_s low, D_b low, MTBH long. The two-axis framework reports green.

What metric on what objects captures this? Not a distance between Z_ai and Z_real(cert). The morphism between those two is fine. The relevant gap is between **Z_real(cert) and Z_real_op**: the certified reality versus the operational reality. This is a property of the **deployment context** relative to the certified envelope, not of the morphism h.

This is the formal structure that F1, F2, F3, F4 below all try to capture, each at a different architectural layer.

---

## 3. Alternative formulations

Each formulation below gives type signature, layer placement, composition behavior, runtime procedure, GUM treatment, Wymore mapping, and strengths/weaknesses.

### F1. Applicability predicate (Layer-1 precondition)

**Description.** A boolean (or membership-probability) gate that the operational state lies inside the certified domain of the morphism. Not on the same axis as D_s/D_b. Sits as a **precondition** to Layer 2 measurement: if the gate fails, D_s and D_b are not reported as trust evidence, the breaker enters a "context-unverified" verdict, and the operator is informed.

**Formal type signature.**

    A : Profile_op x Domain_cert --> {0, 1}
    or
    A : Profile_op x Domain_cert --> [0, 1]   (membership probability)

Domain_cert is a region of Profile-space declared at certification time. Profile_op is the live operational profile (Jeffrey's WHO/WHAT/WHEN/WHERE/WHY tuple is one valid encoding; ODD specifications are another).

**Layer placement.** Layer 1 (Reference Standards). Specifically, Domain_cert is part of the Layer-1 specification, alongside the domain ontology. A is evaluated **before** Layer 2 instruments fire.

**Composition with D_s/D_b.** None at the morphism-algebra level. A composes with the trust verdict at the **verdict-gating level**: trust(decision) is defined only when A = 1 (or A above a threshold). When A = 0, the verdict is "context-unverified," not a number.

**Operational measurement procedure.** At each AI invocation:
1. Read the live operational context from authorization tokens (WHO), task descriptor (WHAT), timestamp (WHEN), deployment metadata (WHERE), and mission intent (WHY).
2. Encode as Profile_op.
3. Evaluate A(Profile_op, Domain_cert). If boolean, this is a SHACL constraint check against Layer 1. If membership-probability, this is a learned classifier or a kernel-density estimate over the certified profile distribution.
4. If A fails: emit "context-unverified," skip Layer 2 measurement on this invocation, optionally log for offline review.

**GUM uncertainty.** A is a precondition, not a measurand, so it does not carry a Type A + Type B uncertainty budget in the same way D_s and D_b do. It does carry an **error rate** characterization: false-positive (gate fails on an in-domain profile) and false-negative (gate passes on an out-of-domain profile) rates. These are estimable from a held-out certified-profile dataset.

**Wymore mapping.** A is a property of the **operational triple (Z_ai, h, Z_real)** as a whole, not of the morphism h. It asks: is the certified Z_real the right Z_real for this invocation?

**Strengths.** Architecturally clean. Preserves the existing two-axis composition algebra unchanged. Maps directly to existing engineering vocabulary (ODD in autonomous vehicles, applicability domain in cheminformatics, assume clause in assume-guarantee contracts). Easy to specify as a SHACL precondition on Layer 1 individuals.

**Weaknesses.** Binary or near-binary gate gives no continuous "how far out of envelope" signal, so a smooth Layer 3 SPC response is harder. Loses Jeffrey's intuition of a continuous "third axis." May feel like a demotion to a co-author who has invested in the three-axis framing.

---

### F2. Coverage / scope-of-validity measure

**Description.** A continuous measure of how much of the operational scenario space the certified morphism covers. Operationally: at each invocation, compute a coverage score that decreases as the operational profile drifts away from the certified profile distribution.

**Formal type signature.**

    C : Profile_op x Distribution_cert --> [0, 1]

C = 1 means the operational profile is well-inside the certified distribution. C = 0 means the operational profile has no support in the certified distribution. Intermediate values are continuous.

**Layer placement.** Spans Layer 1 (the certified distribution is part of the reference standard) and Layer 3 (the coverage score is fed into the SPC graded response). It is **not** a Layer 2 morphism instrument; it is a **separate input channel** to Layer 3 alongside the D_s and D_b time series.

**Composition with D_s/D_b.** Operates in **parallel**, not in the same morphism-chain algebra. Layer 3 escalation rules become "trip if D_s out of SPC limit, **or** D_b out of SPC limit, **or** C below coverage threshold." Layer-3 graded response treats coverage degradation as an independent escalation pathway.

**Operational measurement procedure.** Several concrete options:

1. **Kernel density on certified profiles.** Fit a KDE over the historical certified-context profile distribution. C(Profile_op) = normalized density estimate. Threshold via SPC on the density time series.
2. **Conformal prediction over the certified manifold.** Use a learned representation of the certified data and compute a nonconformity score for each live invocation. C = 1 - nonconformity rank.
3. **Per-dimension coverage decomposition.** For each of WHO/WHAT/WHEN/WHERE/WHY (if that taxonomy is adopted), compute a per-dimension coverage score and aggregate. This preserves Jeffrey's five-dimensional intuition without claiming a five-dimensional metric.

**GUM uncertainty.** Coverage carries a Type A budget (sampling variance in the historical certified-profile distribution) and a Type B budget (model assumption uncertainty for the KDE bandwidth or conformal calibration). Both are computable on held-out data.

**Wymore mapping.** Like F1, C is a property of the operational deployment relative to the certified envelope, not of the morphism h. Unlike F1, C is continuous, so Layer 3 SPC machinery applies directly.

**Strengths.** Preserves Jeffrey's continuous-third-axis intuition. Integrates with Layer 3 without requiring a new composition algebra. Has a deep literature backing (ODD coverage, conformal prediction, applicability domain). Composes with D_s/D_b verdict-side via SPC rules.

**Weaknesses.** Not the same kind of object as D_s/D_b. Calling it "the third axis of morphism distance" is still wrong; calling it "the coverage axis paired with the two-axis morphism distance" is correct and slightly more verbose. Requires the abstract to make this distinction explicit, which costs lines.

---

### F3. Operational-domain morphism composition

**Description.** Treat the AI Circuit Breaker as composing **two morphisms**, not one:

    Z_ai --h_model--> Z_real(cert) --h_use--> Z_real_op

h_model is the certified morphism that D_s and D_b currently measure. h_use is the deployment-context morphism that maps the certified reality into the operational reality. Measure a **D_use** quantity for h_use in the **same** algebra as D_s and D_b, but on a **different morphism**.

**Formal type signature.**

    D_use_s = 1 - sigma(h_use)        on the same definition as D_s
    D_use_b = max_t | R_real(s_cert(t)) - R_op(s_op(t)) |   on the same definition as D_b

so D_use carries a structural component and a behavioral component, **each parallel to D_s and D_b**, just on a different morphism in the chain.

**Layer placement.** Layer 2 (new instrument family, "domain-morphism instruments") with Layer 1 anchors. Specifically:

- Layer 1 supplies the specification of Z_real(cert) (as today) and additionally a runtime sketch of Z_real_op (estimated from telemetry).
- Layer 2 gets new instruments for D_use_s and D_use_b.
- The chain-level bound aggregates over both stages:

      D_s_chain = max( D_s(h_model), D_use_s )     under min-sigma composition
      D_b_chain <= D_b(h_model) + D_use_b          under 1-Lipschitz at each stage

This is the most aggressive integration: it **preserves** Jeffrey's "third quantity participates in the chain bound" claim, but recasts the third quantity as **the same kind of object** (a morphism distance) measured on **a different morphism** (h_use, not h_model).

**Composition with D_s/D_b.** Natural and exact, because D_use_s and D_use_b are by construction the same algebra applied to the next morphism in the chain. This is essentially Section 2.5 of the design spec ("traceability chain as morphism composition") extended one link upstream of where the spec currently stops.

**Operational measurement procedure.**

1. At certification, declare Z_real(cert) (this is already the Layer 1 task).
2. At runtime, derive a sketch of Z_real_op from operational telemetry. The sketch is necessarily coarse, since Z_real_op is what the AI is being asked to operate in, not what was certified against.
3. Compute D_use_s using the same degree-of-homomorphism formula, with h_use: Z_real(cert) --> Z_real_op.
4. Compute D_use_b as the worst-case output distance between certified-domain outputs and operational-domain outputs over a sliding window.
5. Feed both into Layer 3 SPC alongside D_s and D_b.

**GUM uncertainty.** D_use_s and D_use_b carry GUM budgets in the same form as D_s and D_b. Type A: sampling variance on the operational telemetry. Type B: the prior-knowledge uncertainty on the Z_real_op sketch, which is large at deployment start and reduces with operational data accumulation.

**Wymore mapping.** D_use measures the second morphism h_use: Z_real(cert) --> Z_real_op in a two-stage chain. The triple (Z_ai, h_model, Z_real(cert)) is the certified subsystem; h_use takes that subsystem into the operational reality.

**Strengths.** This is the formulation that **preserves Jeffrey's "third axis" intuition without breaking the construct**. It says: "yes, there is a third quantity, and yes, it composes with D_s and D_b, but it is not a third orthogonal coordinate on a single morphism. It is the same two-axis pair measured on a second morphism in the chain." This converts a confused construct into a coherent extension of the existing CSER 2026 chain-bound theorem. It is also the formulation that gives Jeffrey's intent its strongest formal home.

**Weaknesses.** Z_real_op is hard to specify at runtime in any rigorous way. The sketch may be too coarse to support a credible D_use computation in v1 of the framework. The 1-Lipschitz assumption now has to hold across **two** stages, not one, which tightens the burden of proof in the chain-bound theorem. This is the most technically demanding option to defend in a 3-page abstract.

---

### F4. Assume-guarantee contract violation rate

**Description.** Treat the certified domain of validity as the **assume** clause of an assume-guarantee contract for the AI subsystem. Measure **violation frequency** of the assume clause under live operation, and SPC-monitor that frequency.

**Formal type signature.**

    V : Time x Profile_op x Assume --> {0, 1}
    Violation_rate(window) = (1/|window|) * sum_{t in window} V(t)

Assume is the contract precondition: a SHACL-expressible constraint or set of constraints over Profile_op. V(t) = 1 if Profile_op(t) violates Assume, else 0.

**Layer placement.** Layer 1 (Assume is part of the reference standard, expressed as SHACL constraints on the operational-profile graph). Layer 3 (the violation-rate time series enters SPC with its own control limits). The CBTO already has SHACL machinery; this is a natural extension.

**Composition with D_s/D_b.** Composes with **CBTO contract conjunction**, not with morphism composition. If the chain is Z_0 --h_1--> ... --h_n--> Z_n, each stage can carry its own assume clause Assume_i, and the system-level assume is the conjunction. Violation rate composes as `1 - prod(1 - V_i)` under independence, or by inclusion-exclusion in general. This is a contract algebra, not a morphism algebra.

**Operational measurement procedure.**

1. At certification, express Domain_cert as a set of SHACL constraint shapes over Profile_op.
2. At runtime, evaluate the SHACL shapes against the live profile graph at each invocation.
3. Maintain a moving-window violation rate.
4. Layer 3 SPC charts the violation rate alongside D_s and D_b.

**GUM uncertainty.** Type A: sampling variance on V over the moving window. Type B: SHACL constraint specification uncertainty (the contract itself can be wrong). Both are characterizable, though Type B is harder.

**Wymore mapping.** Like F1 and F2, this is a property of the deployment relative to the certified envelope, not of the morphism h. Unlike F1, it is continuous (a rate). Unlike F2, it does not require a probability model over the certified distribution, only a SHACL specification of which profiles are admissible.

**Strengths.** Composes naturally with the existing CBTO SHACL machinery and PROV-O audit trail. Gives a continuous quantity that fits Layer 3 SPC without requiring a probabilistic model. Aligns with mature engineering practice (assume-guarantee reasoning has a long history in formal methods and runtime verification).

**Weaknesses.** Requires the assume clause to be **specified** correctly and **completely** at certification time. Specification uncertainty (Type B) is the dominant uncertainty, and it is hard to bound. Does not generalize to "soft" out-of-envelope cases as gracefully as F2's continuous coverage measure.

---

## 4. Recommendation

### 4.1 Which formulations are most defensible in 3 pages?

In rank order for SERC defensibility:

1. **F1 (applicability predicate) as the primary mechanism, paired with F2 (coverage measure) as the Layer-3 continuous signal.** This is the smallest, cleanest, and most defensible package. F1 captures Jeffrey's failure-mode intent verbatim ("near-isomorphic to the wrong context"), and F2 gives him the continuous third signal he wants without claiming it is a third axis on the morphism. The pairing matches existing engineering vocabulary (ODD plus continuous coverage monitoring) and integrates with Layer 3 SPC unchanged.

2. **F3 (operational-domain morphism composition)** is the most ambitious and the most theoretically satisfying. If the writing budget permits two extra paragraphs (one to introduce h_use, one to extend the chain-bound theorem), this is the strongest option for preserving Jeffrey's "it composes with D_s and D_b" intuition without the construct confusion. It also positions the paper for a strong follow-on journal extension. Risk: under 3-page constraint, this can collapse into a hand-wave that reviewers will catch. Use F3 only if the chain-bound extension is sketched precisely.

3. **F4 (assume-guarantee contract violation rate)** is solid engineering but a third place because it requires more SHACL specification than the abstract can carry. Better as a body-paper construct than an abstract-level claim.

**Anti-recommendation: do not adopt Jeffrey's three-axis-on-the-same-morphism framing as written.** The composition claim does not hold, and reviewers oriented toward formal methods or measurement theory will find it on first read. The abstract is currently strong on rigor; this single move forfeits that.

### 4.2 Smallest version that preserves Paul's "intent is correct" while replacing Jeffrey's mechanics

The smallest move is:

- Keep "two-axis morphism distance (D_s, D_b)" exactly as in v0.5.
- Add **one paragraph** in the Layer 1 description introducing a **certified-context envelope** (the union of WHO/WHAT/WHEN/WHERE/WHY profiles for which the morphism is calibrated), and **one sentence** in the Layer 3 description that escalation can be triggered by (i) D_s out of SPC limit, (ii) D_b out of SPC limit, **or** (iii) the live operational profile leaving the certified envelope.
- Reference Jeffrey's five-dimensional taxonomy as **the operational-profile schema for the envelope**, not as a third axis on the morphism.
- Defer F3 (the morphism-composition extension) to a journal-length treatment that can carry the chain-bound proof obligation.

This preserves Paul's two-axis morphism construct intact, preserves Jeffrey's five-dimensional WHO/WHAT/WHEN/WHERE/WHY taxonomy intact, and re-architects only the **layer at which the third construct sits** (Layer 1 envelope + Layer 3 gating, not a Layer 2 morphism axis).

### 4.3 Open items / dependencies

- **Literature scout output.** Once `Dr_literature_scoping_v0.1.md` lands, this analysis should be re-run against it. Specifically, the scout's findings on ODD, applicability domain, conformal prediction, and assume-guarantee literature will determine which of F1/F2/F4 has the strongest external citation backing.
- **Jeffrey's TDD v2.0 lineage on D_r.** If a separate procedural specification of D_r exists in Jeffrey's TDD documents, the metricity analysis in Section 1.2 should be re-checked against that spec. The reconstruction here is from the SERC PDF only.
- **CSER 2026 chain-bound theorem status.** F3 depends on a two-stage extension of the chain-bound theorem. The current bound (`D_s_total >= max(D_s_i)`, `D_b_total <= sum(D_b_i)` under 1-Lipschitz) is single-chain. Extending to a chain that includes h_use is straightforward in principle but needs explicit treatment.

---

## Closing summary

Jeffrey is pointing at a real and important failure mode: an AI system that is well-calibrated for a reality that is not the reality it has been deployed into. The two-axis framework provably misses this. Adding a "third axis on the morphism distance" does not fix it, because the failure is not a morphism-quality failure; it is a domain-of-applicability failure. The constructs are at different architectural layers.

Four alternatives capture the intent without the construct confusion. F1 (applicability predicate at Layer 1) is the smallest defensible move. F2 (continuous coverage measure entering Layer 3) preserves Jeffrey's continuous-signal intuition. F3 (treat the deployment as a two-stage morphism chain and measure the second stage in the same algebra) is the most theoretically ambitious and the only one that preserves Jeffrey's "it composes with D_s and D_b" claim in a way that is mathematically defensible. F4 (assume-guarantee contract violation rate) is solid but heavier than the abstract can carry.

For the SERC 3-page constraint: combine F1 and F2 in the abstract, defer F3 to follow-on journal work, defer F4 to the body paper.

---
name: morphism-domain-reference
description: Domain knowledge pack for the systems-engineering (SE) morphism library. Load when classifying a candidate morphism (isomorphism, homomorphism, coupling, parameter); when deciding whether a model relationship is fidelity, resolution, or pedigree; when reasoning about the degree of homomorphism (D_s), the Discrete Event System Specification (DEVS) carrier, problem spaces of functions or outcomes, Kannan acceptability posets, or the Wymore functional-to-buildable homomorphism; or when GI-JOE needs the candidate typing decisions (D-1 to D-6) to formalize the library ontology. Do NOT load for choosing research targets (use morphism-research-frontier), running the empirical gate campaign (use morphism-verification-campaign), or setting the evidence bar (use morphism-research-methodology).
---

# Morphism Domain Reference (SE Morphism Library)

**Status tag [R016]: research artifact.** This skill is a knowledge pack over a corpus whose morphism content is mostly asserted or subject-matter-expert (SME)-adjudicated, not proven; the corpus inventory says so explicitly and every claim below carries a rigor tag. Nothing here is a demonstrated capability or an integrated deliverable. The typing spec in Section 8 is CANDIDATE; do not canonize it.

PROVENANCE: produced by Fable 5 (claude-fable-5[1m]), vendor Anthropic, access mode Claude Code CLI (subagent run at principal's direction), 2026-07-07. Grounded in the four ground-truth files and the Prompt 1 research output listed in Section 10; no other sources.

Open dissertation decisions F1 (infinite-equivalence wording) and F7 (graded-gate rewrite) are OPEN. This skill uses only validated post-F7 data facts and does not choose F1 wording.

---

## 1. When to load this skill, and when not to

**Load it when the task looks like:**
1. "Classify this new candidate morphism between a Simulink model and a hardware mock-up: which of the four types is it, and is the relationship fidelity, resolution, or pedigree?"
2. "GI-JOE is formalizing the morphism-library TBox (terminological box) in the Web Ontology Language (OWL); give the settled candidate typing decisions for D-1 to D-6."
3. "I want to order two verification models by degree of homomorphism for a monotonicity claim; which order is safe to use?"

**Do NOT load it when:**
1. You are choosing which open research problem to attack or need the state-of-the-art positioning for Targets A, B, or C. Use `morphism-research-frontier`.
2. You are executing the decision-gated empirical campaign (Gate 1 to Gate 4, promotion protocol, fallback branches). Use `morphism-verification-campaign`.
3. You are deciding whether a result meets the evidence bar, or managing the candidate-to-adopted lifecycle. Use `morphism-research-methodology`.

This skill defines terms, states known results with their rigor levels, and records the candidate ontology typing. It does not plan research, run campaigns, or adjudicate evidence.

## 2. Capability floor and "when not to trust yourself"

**Floor.** To use this pack correctly you must be able to: (a) read basic order theory (preorder, partial order, monotone map, kernel partition, refinement); (b) distinguish a preorder from a partial order and say why antisymmetry matters for Theorem T5(i) in Section 7; (c) explain, from the numbers alone, why $\mathrm{DoH} = 0.55 < 0.6833$ in counterexample C2 refutes scalar monotonicity under refinement. **Self-check before proceeding: recompute C2's two DoH values from the granule lists in Section 4.3. If you cannot, or you get different numbers, STOP and report that you are below the capability floor for this skill; do not paraphrase the claims anyway.**

**Guards.**
- Do not derive new theorems from this pack. Everything stamped candidate stays candidate; new results go through `morphism-research-methodology` and its refutation bar.
- Do not resolve F1 or F7; they are open dissertation decisions.
- Do not cite Cousot and Cousot or Girard and Pappas in any manuscript from this pack; they are `[PLACEHOLDER]` entries not in the approved store (R019). Run reflookup/refverify first.
- If a user asks you to state a result more strongly than its ledger row in Section 10, quote the ledger row instead.

---

## 3. The fidelity / resolution / pedigree taxonomy

Three model-relationship concepts, previously conflated under "fidelity." Terminology is fixed; using "fidelity" for the verification-model-to-system-design relation is a fenced wrong path.

| Concept | Relates | Definition | Formal home |
|---|---|---|---|
| **Fidelity** | Model to reality | How well a model approximates the real world. Neither the system design (SD) nor the verification model (VM) is reality; both are models. Fidelity is empirical grounding (measurement, validation), not a morphism between formal objects | Validation |
| **Resolution** | Model to model, same family, same system | Different level of detail within one model family (Zeigler's hierarchy of system specifications). The structural degree $D_s$ is fundamentally a resolution measure | Abstraction machinery |
| **Pedigree** | Model to model, cross-family | The VM-to-SD relationship, where the SD is itself a model and the VM may be a different model family (physical mock-up, Monte Carlo run, mass model, or a different system entirely) | Verification |

**Disjointness correction (supersedes ontology schema v0).** These three are NOT mutually disjoint. Resolution is the same-family, on-carrier sub-case of pedigree; only fidelity is disjoint from the two model-to-model relations. Section 8 (D-6) carries the typing consequence.

**Projected fidelity (confirmed term, 2026-07-07).** The VM is the operative instrument used to infer, before the system is realized, what the realized system will be; that anticipatory inference is projected fidelity. Pedigree's purpose is to license the projection: good pedigree is what makes it sound to project the VM's acceptability judgment onto the eventual real system. Do NOT frame this as "projected vs measured"; that language is banned for this line. Candidate status of the license itself: per the Target C research attempt (Section 7), automaton-level degree pedigree does NOT license the projection; the surviving candidate license has three clauses (totality over the requirement-relevant scope, descriptor adequacy, condition strength) with refinement supplying the monotone core.

**Verification and validation (V&V) alignment.** Verification is approximately pedigree (model to model); validation is approximately fidelity (model to reality or need); resolution is the abstraction machinery used within either. This aligns with the Kannan-Salado 2026 V&V distinction (approved key `kannan2026theory`).

**Legacy-usage caveat.** The Wach-Salado 2024 paper "Fidelity Conditions for Defining Verification Models" states VM-to-SD conditions, which under this taxonomy are pedigree conditions. Cite that paper's "fidelity" as legacy usage and use "pedigree" going forward, noting the divergence explicitly.

## 4. The morphism layer

### 4.1 Four-type morphism taxonomy (Wach, Beling, Salado; approved key `wach2022formalizing`)

Rigor: asserted/conceptual in the source papers (notation deferred there); the exact baseline is written out only in Def. 2 below.

| Type | Cardinality | Preserves | Partiality axis |
|---|---|---|---|
| Isomorphism (incl. **identity isomorphism**) | one-to-one, bijective | exact structure and behavior | none (exact) |
| Homomorphism | many-to-one | structure and behavior under abstraction (lossy, exact on image) | abstraction |
| Coupling morphism | subset projection | a subset of couplings/functions | **structural** |
| Parameter morphism (= approximate homomorphism) | approximate | "degree of preservation," bounded error | **behavioral / quantitative** |

The two partiality axes (structural, behavioral) align with $D_s$ (structural) and $D_b$ (behavioral). Encode them as separate properties, never one scalar. The parameter morphism is the existing container for descriptor-plus-condition pairs (Section 7, cross-family gap).

**Preservation vocabulary:** inputs/outputs (external and internal), interfaces, conditions of applicability (= parameters), trajectories, states, coupling structure. System requirement (SR) to verification requirement (VR) morphisms preserve the first four; SD-to-VM morphisms add internal input/output and states.

### 4.2 The exact baseline: Salado-Kannan 2018 Definition 2 (approved key `salado2018mathematical`)

A **system** is a Wymorian quintuple $Z = (S, I, O, N, R)$: state set $S$, input set $I$, output set $O$, next-state function $N: S \times I \to S$, readout $R: S \to O$ (approved key `wymore1993mbse`). The canonical exact homomorphism between a system and its verification model: surjections $h_q: S_2 \to S_1$, $h_i: I_2 \to I_1$, $h_o: O_2 \to O_1$ with

$$h_q(N_2(x,i)) = N_1(h_q(x), h_i(i)) \qquad \text{and} \qquad h_o(R_2(x)) = R_1(h_q(x)).$$

Exact and surjective only; no partial or approximate case. Direction convention for the library: the SD is concrete, the VM abstract; the witnessed map runs $\mathrm{SD} \to \mathrm{VM}$, many-to-one. A **scoped homomorphism** (dissertation decision D27 Option A) is the same conditions restricted to a stated scope (a subset of inputs and the states reachable under them); all witnessed morphisms in the settled dissertation data are scoped.

### 4.3 Degree of homomorphism, $D_s$, and the known metric defect

For a mapping $h: A \to B$ (approved lineage: the isomorphism-library line, Eq. (3) of the CSER 2026 draft):

$$\mathrm{DoH} = \frac{1}{|B|} \sum_{b \in B} \frac{1}{|h^{-1}(b)|},$$

computed separately for states, inputs, outputs, giving the tuple $(\mathrm{DoH}_S, \mathrm{DoH}_I, \mathrm{DoH}_O)$.

**Notation caveat (two live conventions; always state which you use).** The CSER 2026 draft uses $D_s$ for the DoH tuple itself ($1.0$ = isomorphism); the Target C lineage uses $D_s = 1 - \overline{\mathrm{DoH}}$ ($0$ = isomorphism). Write $\mathrm{DoH}$ for the ratio and $D_s$ for the distance. Never use $\sigma$ for the degree (statistics collision).

**$D_s$ is a resolution measure.** It measures within-family, on-carrier abstraction loss. Its extension to cross-family pedigree is exactly what the DEVS carrier move attempts (Section 5).

**Known defect (candidate result C2, machine-checked 2026-07-07; feeds back to the CSER 2026 line).** The scalar averaged DoH is not monotone along refinement chains. Witness: granules $\{1,1,10,10\}$ (finer) vs $\{1,1,20\}$ (coarser after merging the two 10-blocks) give

$$\mathrm{DoH}(V_{\mathrm{fine}}) = \tfrac{1}{4}\big(1 + 1 + \tfrac{1}{10} + \tfrac{1}{10}\big) = 0.55 \;<\; \mathrm{DoH}(V_{\mathrm{coarse}}) = \tfrac{1}{3}\big(1 + 1 + \tfrac{1}{20}\big) \approx 0.6833,$$

so the strictly more faithful surrogate scores strictly worse. Consequences for any user of this library: (a) never make order claims from scalar $D_s$; (b) for order claims use the **refinement order** ($V_j \trianglerighteq V_i$ iff $\ker h_j \subseteq \ker h_i$) or the **worst-granule statistic** $g_{\max}(h) = \max_b |h^{-1}(b)|$, $D_s^{\max} = 1 - 1/g_{\max}$, which is order-compatible (candidate lemma L4'(i)); (c) equal scalar $D_s$ does not imply equal preservation (candidate counterexample C1: two 2-block partitions of a 4-set, same $\mathrm{DoH} = 0.5$, different saturated sets).

### 4.4 $D_b$ and the carrier subsumption (ASSERTED, not an axiom)

$D_b = \max_t |y_1(t) - y_2(t)|$ measures discretization-induced behavioral degradation. **Asserted claim (Target C settled decision 3; rigor: asserted):** on a DEVS carrier the structure exactly generates the behavior, so there is no discretization gap, $D_b$ vanishes, and $D_s$ alone is the pedigree measure; $D_b$ re-emerges only off-carrier, as the fidelity of a DEVS-ification (DEVS model versus the actual thing), which is a fidelity question. Treat "D_b vanishes on carrier" as a tagged asserted claim wherever it appears; never encode it as an axiom or use it as a proof premise. The Target C research attempt used it only as scope justification.

## 5. The DEVS carrier

The DEVS carrier is the common executable substrate on which different model families are co-represented so that structure equals behavior and $D_s$ becomes computable across families (the conjoining; approved keys `wach2021wymoredevs`, `zeigler2018tms`; nearest graded-morphism prior art in-corpus: relaxed lumpability, approved key `zeigler2018approxmorph`).

**Empirical status after the Target C attempt (candidate, adverse; 2026-07-07).** On the settled 18-VM dissertation data the strong form of the carrier bet fails: co-representation succeeds mechanically (the pizza VM and the red-green-blue (RGB) pen VM reduce token-wise to the common 2-state carrier), but on the carrier the degree degenerates ($D_s = 0$ for every witnessed morphism), so the degree does not restore the discrimination raw pedigree loses. The discriminating information lives in instantiation descriptors (firefly vs engineered light, smell vs light), which the automaton-level morphism cannot see and the verification requirement problem space (VRPS) membership gate does see. Caveat on the test itself: the settled data's "cross-family" cases are cross-DOMAIN instantiations co-represented on one state-machine carrier, not cross-formalism families, so the carrier bet is only partially testable there. Consequence for library reasoning: expect the pedigree order extractable from carrier-level degree alone to be coarse (two-level on the settled data), and expect descriptor and condition layers to carry the discrimination.

## 6. Problem spaces and the ought layer

### 6.1 Problem space of functions (PSF) and problem space of outcomes (PSO)

| Object | Content | Systems kind | Key property |
|---|---|---|---|
| **PSF** | A set of input/output-trajectory conditions (requirements) | Open systems | Conditions are **unordered**; NOT executable/composable. A system model's functions are closed under concatenation (executable); this is the executability hinge (Wach-Salado IS 2024) |
| **PSO** | An outcome mapping $O: M \times F \to D$ into an outcome space $D$ | Closed systems (needs; "consequences of interactions," not producible by a system) | Not inter-derivable with PSF: "a function cannot be decomposed into outcomes" (Salado 2021; Shadab et al. Scenario-to-Outcome 2024) |

Asserted key claim from the PSF line: a homomorphism between any solution and the problem space "should be infeasible" (they are different in kind). Rigor: asserted.

### 6.2 The ought layer (what DEVS lacks)

- **Kannan 2019 (approved key `kannan2019preference`): the order-theoretic ought.** A betterness poset over the solution space; **acceptable = maximal elements**, optimal = greatest elements; requirements are target-oriented preferences bounding the space; incomparability is allowed (Theorem 3: no total order; never assume one). Seven proven theorems. Known gap: no morphisms between ordered structures (the order exists, the maps do not); that gap is exactly where the library's weld lives.
- **Kannan-Salado 2026 (approved key `kannan2026theory`): the epistemic ought.** Dynamic epistemic modal logic, 50 theorems; V&V as belief-building; acceptability = belief-entailment (sufficiency, necessity) plus a confidence threshold $\tau$. It cites the morphism work but black-boxes the system-to-model relationship inside one implication; Theorems 43-50 state WHEN verification belief transfers to need belief, not WHY it fails. The library supplies the structural mechanism under that implication: blind spots (L3) and descriptor mismatch (T5 mechanism) are the two failure ways, and refinement (T4a) is the condition under which strengthening the model strengthens the transfer. All three linkage claims are candidate (Section 7).

## 7. The Wymore grounding, the federation picture, and the Target C state of knowledge

### 7.1 The foundational pedigree exemplar

Wymore's implementable-design homomorphism relates the functional design to hardware and software models: the functional system design (FSD) is a homomorphic image of the buildable system design (BSD, buildable = hardware + software); the implementable system design is $\mathrm{ISD} = (\mathrm{FSD}, \mathrm{BSD}, \mathrm{IA})$ with the implementation architecture (IA) carrying the homomorphism. Its written-out exact form is Def. 2 (Section 4.2). Cross-family pedigree is therefore Wymore's founding move; the library extends a foundation rather than inventing one. Honest caveat: Wymore grounds the principle, not a worked federated example; the multi-discipline test-bed gap remains (known gap, flagged).

**Novelty line (Wymore vs ours).** Wymore: exact, single, functional-to-buildable homomorphism. Ours (all candidate): exact extended to degree/partial/approximate ($D_s$); single extended to federation; verification-inference framing (VMs infer knowledge about the SD); projection to the realized system (projected fidelity); interfaces as first-class systems; the DEVS carrier and time; the acceptability weld.

### 7.2 There is no single SD: functional reference plus buildable federation

The design fragments by discipline and by functional area or mode as soon as (often before) requirements exist. Model it as: the **SD = a functional reference** (Wymore FSD, includes interface definition, possibly itself federated), plus a **buildable VM federation** = the discipline models (hardware, software, mechanical, ...), cross-family, coupled through interfaces. This one premise makes cross-family pedigree the default case, makes interfaces-as-first-class-systems constitutive (the federation is held together by exactly those interfaces), and makes the DEVS carrier necessary (co-representing heterogeneous discipline models is the only way to relate them). It also opens the synthesis use (composing a federation via coupling morphisms and interface systems), which is logged out-of-window.

### 7.3 What the Target C research attempt established (all CANDIDATE per R016; source: the Prompt 1 output, Section 10)

Read this table before making any claim that links pedigree to acceptability.

| Item | Statement (compressed) | Status |
|---|---|---|
| P1, P2 | Same-family pedigree is a Galois connection ($\alpha = h(\cdot)$, $\gamma = h^{-1}(\cdot)$); DoH is exactly a precision statistic of it ($\mathrm{DoH}_S = \mathbb{E}_b[|h^{-1}(b)|^{-1}]$; $=1$ iff isomorphism) | Candidate (proved, unchecked independently) |
| L1 | Identity isomorphism preserves every acceptability verdict exactly | Candidate (proved) |
| L2 | Surjective coarsening is one-sided: sound (no false accepts), false rejects possible; proof obligation PO-1 open (trajectory-level reach compatibility) | Candidate (proved modulo PO-1) |
| L3 | Partial (blind-spot) morphisms admit **false accepts**; empirical witness: the SD4-to-VM8 map holds scoped, fails unscoped at exactly 3 out-of-scope elements | Candidate (proved; witness pinned to data) |
| T4a | Refinement monotonicity, same-family: finer kernel implies larger preservation set (under saturated verdicts and exactness) | Candidate (proved) |
| C1, C2 | Scalar $D_s$ defects: equal scalar, different preservation (C1); scalar not monotone under refinement (C2, Section 4.3) | Candidate (machine-checked, synthetic) |
| L4' | Repair: worst-granule $g_{\max}$ is order-compatible and gives a one-sided drift bound; PO-2 open (measure-level bound) | Candidate (proved modulo PO-2) |
| T5 | **No monotone degree-only map** from the settled-data pedigree preorder to acceptability exists (tie-class and strict-pair obstructions; pizza VM ties every flashlight VM at $D_s = 0$ with disjoint accepting contexts). Mechanism: the acceptability gate is descriptor- and condition-aware; automaton-level degree is not | Candidate (proved from pinned, double-confirmed data) |
| Enriched conjecture | The surviving weld target: enriched pedigree object $\pi = (m, \delta, p)$ with $m$ = witnessed morphism (refinement position), $\delta$ = descriptor morphism, $p$ = condition profile; conjectured monotone per coordinate; PO-3 (formalize $\delta$; parameter-morphism slot is the container) and PO-4 (derive the verification-model-morphism-condition (VMMC) lattice from condition logic) open | Conjecture (open) |

Practical rules this table imposes: never present degree-only pedigree as tracking acceptability (it is refuted on the settled data in that form); the monotone structure observed in the data lives in the VMMC condition lattice and the VRPS membership gate, not in the automaton-level degree; the settled data's pedigree order is two-level ($D_s = 0$ or no witnessed morphism), so quantitative degradation bounds are empirically untestable there.

---

## 8. CANDIDATE TYPING SPEC: resolutions of D-1 to D-6 (for GI-JOE formalization)

Scope of this section: judgment only. Do NOT hand-author Turtle (TTL) from it in this hive; the TTL plus Shapes Constraint Language (SHACL) and logical-consistency validation is GI-JOE work, deferred to after the July 12 cutoff. Every resolution below is CANDIDATE: it supersedes ontology schema v0 as a proposal, not as a canon. Rigidity notation is OntoClean: +R rigid, -R anti-rigid, +I carries identity.

### D-1. Morphism: entity or relation, and what individuates it

**Resolution (candidate).** Keep `Morphism` reified as a class. Identity criterion = the 5-tuple $(\text{source}, \text{target}, \text{type}, \text{witness map}, \text{scope})$. Both the witness map and the scope are identity-bearing.
**Rationale.** The settled data forces it twice: (a) the SD4-to-VM8 pair carries a scoped map that HOLDS and an unscoped map that FAILS with $\mathrm{DoH} = (0.75, 0.667, 0.75)$; under triple identity $(\text{source}, \text{target}, \text{type})$ these collapse into one individual with contradictory attributes. (b) C1 shows two witness maps with identical source, target, type, and even identical scalar degree that have different preservation sets; the kernel (witness) is the semantically load-bearing object, and T4a's refinement order is an order over kernels.
**Rejected alternatives.** Object-property modeling (cannot carry degree, rigor, provenance, linearity, exactness tags); triple identity (contradiction shown above); tuple-without-scope (collapses D27 scoped/unscoped distinction).
**Consequences.** Morphism individuals proliferate (one per witnessed map per scope); adopt a naming convention `<src>__<tgt>__<type>__<scopeId>`; degree attaches to the morphism individual, never to the bare pair.

### D-2. PedigreeRelation vs its witnessing Morphism: one object or two

**Resolution (candidate).** Two objects, and the separation is now principled, not provisional. `PedigreeRelation` is the container for the **enriched pedigree object** $\pi = (m, \delta, p)$: slot `witnessedBy` (the Morphism, coordinate $m$), slot `hasDescriptorMorphism` (coordinate $\delta$; typing loose pending PO-3; the parameter morphism of the four-type taxonomy is the designated container), slot `hasConditionProfile` (coordinate $p$; the set of VMMCs that hold).
**Rationale.** T5 proves the bare morphism coordinate cannot track acceptability; the relation therefore must carry information a Morphism intrinsically cannot: $\delta$ and $p$ are context-relative (they involve the VRPS descriptor gate and the VMMC conditions), while the witness map is context-free and reusable across relation contexts.
**Rejected alternatives.** Collapse into a fattened Morphism (loses reuse; smuggles context-relative attributes into a context-free object); keep the v0 two-object design without the $\delta$/$p$ slots (leaves the relation a near-duplicate of the morphism, the very redundancy v0 flagged).
**Consequences.** The future weld property (pedigree to acceptability-preservation) attaches to `PedigreeRelation`, never to `Morphism`; a `PedigreeRelation` with only $m$ populated is a valid but explicitly degree-only entry, and any query feeding an acceptability claim must check that $\delta$ and $p$ are populated.

### D-3. Interface rigidity (the hard OntoClean case)

**Resolution (candidate).** Split the concept. The mediator is a plain `System` (+R, +I via its own quintuple). "Being an interface" is an **anti-rigid role** (-R), a new class `InterfaceRole`, existentially dependent on a coupling context (the pair or set of systems connected); `connectsSystem` (min cardinality 2) moves onto the role, not the system. Interfaces are first-class systems in exactly this sense: the thing playing the role is a full system with its own states and behavior; the role is what is relational.
**Rationale.** This is the standard OntoClean treatment of relational concepts and it dissolves the v0 conflict exactly: reconnecting the same physical mediator to a different pair changes the role instance, not the system; removing an endpoint ends the role, not the system. It preserves the differentiator (inventory Finding 2) instead of abandoning it, and the federation picture (Section 7.2) requires it: a federation is held together by systems playing interface roles, and the synthesis use composes them.
**Rejected alternatives.** `Interface ⊑ System` with relational identity (OntoClean-incoherent: an anti-rigid class cannot subsume under a rigid one while inheriting its identity); interface-as-port (corpus default; abandons the differentiator and cannot carry behavior, which federation interfaces must).
**Consequences.** The v0 class `Interface` is retired in favor of `InterfaceRole` plus its `playedBy` System; coupling morphisms reference the role; the OntoClean coherence risk flagged by the inventory is discharged at the price of one extra class.

### D-4. Is Model a subclass of System

**Resolution (candidate).** Yes, `Model ⊑ System`, but fix the identity criterion: a Model is individuated by its carrier quintuple **plus its instantiation-descriptor map** (the labeled input/output/state descriptors); `modelFamily` and `representsSystem` are non-identity attributes.
**Rationale.** The subclass follows Wymore and Wach usage (a system model is itself a transformation) and is required so Morphism endpoints type-check. The descriptor addition is forced by the settled data: the pizza VM and the flashlight VMs are carrier-identical 2-state machines; bare-quintuple identity would make them the same individual, which is false in the library and is precisely the infinite-equivalence lesson (the VRPS gate distinguishes them by descriptor, errata item F2; F1 wording remains OPEN).
**Rejected alternatives.** Bare-quintuple identity (collapses cross-domain instantiations); Model as a representation sort disjoint from System (breaks morphism typing and the corpus's own definitions).
**Consequences.** The descriptor map becomes a first-class component of every Model entry, which is also exactly what coordinate $\delta$ of D-2 consumes; carrier-level equality and model-level identity come apart by design, so record both.

### D-5. Typing of $D_s$ and $D_b$, and the carrier-subsumption encoding

**Resolution (candidate).** Do NOT encode "D_b vanishes on carrier" by omitting the slot (v0's move silently hard-codes an unproven claim). Give `PedigreeRelation` an OPTIONAL `hasBehavioralDistance` slot, and record the vanishing claim as a library entry with `rigorLevel = asserted`. Additionally, type every degree value with its **aggregation form**: `{tuple | mean-reciprocal-scalar | worst-granule}`; an order claim is valid only over `worst-granule` (or over the refinement order directly), never over `mean-reciprocal-scalar`. Record the sign convention (DoH vs $D_s = 1 - \overline{\mathrm{DoH}}$) on every value.
**Rationale.** C2 (Section 4.3) proves the mean-reciprocal scalar is order-defective; a schema that stores only that scalar would let downstream users derive false monotonicity claims mechanically. The optional-slot move keeps the schema honest if the carrier bet fails (which, in its strong form, it already did on the settled data, Section 5).
**Rejected alternatives.** v0's slot omission (hard-codes the bet); a single `dsValue` decimal (loses the aggregation distinction that makes C2 statable); demoting $D_b$ entirely (it re-emerges off-carrier as the fidelity residual and needs a home on `FidelityRelation`).
**Consequences.** Three new datatype facets on degree values (aggregation, convention, and the existing $[0,1]$ range); SHACL, when GI-JOE writes it, should reject any monotonicity-annotated triple whose degree aggregation is `mean-reciprocal-scalar`.

### D-6. Disjointness of the three relation kinds

**Resolution (candidate; supersedes v0's AllDisjointClasses).** `ResolutionRelation ⊑ PedigreeRelation` (resolution is the same-family, on-carrier sub-case). `FidelityRelation` is disjoint from `PedigreeRelation` (and hence from `ResolutionRelation`). Generalize `PedigreeRelation`'s relata from (VerificationModel, SystemDesign) to (surrogate Model, reference Model), keeping VM-to-SD as the paradigmatic specialization; direction convention: the witnessed map runs reference to surrogate, many-to-one.
**Rationale.** The taxonomy correction is settled upstream (Target C scope: "same-family pedigree = resolution"); mutual disjointness contradicts it. The one wrong path the disjointness existed to fence (using fidelity for VM-to-SD) is fully fenced by the fidelity disjointness alone. The relata generalization follows from the federation picture: pedigree relates federation members to the functional reference, not only classical VM to classical SD.
**Rejected alternatives.** Keep all three disjoint (contradicts the settled taxonomy); merge resolution into pedigree without a subclass (loses the ability to query the clean same-family regime, which is where the only proved monotonicity, T4a, lives).
**Consequences.** Pedigree queries return resolution instances (intended); the shortcut property `hasResolutionTo` becomes a sub-property of the generalized pedigree shortcut; v0's `owl:propertyDisjointWith` between them is dropped, the one against `hasFidelityTo` stays.

### Federation additions (queued corrections, now specified)

| Class / change | Spec | Rationale |
|---|---|---|
| `FunctionalReference` | ⊑ Model; the Wymore FSD, includes interface definition; possibly federated | Section 7.2; the v0 `SystemDesign` class is retagged as this, with "SD" kept as a label for continuity |
| `BuildableModel` | ⊑ Model; a discipline model (hardware, software, mechanical, ...) | Federation member; cross-family by default |
| `VMFederation` | Aggregate of `BuildableModel`s coupled through `InterfaceRole`s | The thing actually built and manipulated; the synthesis use composes it |
| Wymore exemplar individual | One catalog entry: the FSD-to-BSD homomorphism, $\mathrm{ISD} = (\mathrm{FSD}, \mathrm{BSD}, \mathrm{IA})$, `rigorLevel = asserted` (principle grounded, no worked federated example) | The foundational pedigree exemplar, required by the queued corrections |
| Projected fidelity | An annotation on `FidelityRelation` marking the anticipatory (pre-realization) case; no "projected vs measured" pair is introduced | Confirmed term; banned framing avoided |
| `PreferenceOrder` stub | Remains a stub. The upstream order-domain decision is settled (pedigree-primary: order models, acceptability as distributed validating property), but the weld property stays uncommitted until PO-3/PO-4 close; any future weld must attach to the enriched $\pi$, not to a bare degree (T5) | Section 7.3 |

---

## 9. Self-test and adversarial-misuse cases

### Five-question self-test (answer before relying on this skill; answers follow each question)

1. A wind-tunnel mock-up is compared to the system design. Fidelity, resolution, or pedigree? **Pedigree (model to model, cross-family). It is additionally resolution only if same-family and on-carrier. It is fidelity only if one side is reality, which it is not.**
2. Two VMs have equal scalar $D_s$. May you conclude they preserve the same acceptability structure? **No. C1: equal scalar, different preservation sets. Scalar degree does not determine preservation.**
3. True or false: refining a surrogate can worsen its scalar $D_s$. **True (C2: 0.55 vs 0.6833). Therefore order claims use the refinement order or $g_{\max}$, never the mean-reciprocal scalar.**
4. Where do false accepts come from, and what is the pinned empirical witness? **Blind spots of partial (scoped) morphisms (L3). Witness: the SD4-to-VM8 map holds scoped and fails unscoped at exactly 3 out-of-scope elements; requirements whose violation lies wholly out of scope pass regardless of actual behavior.**
5. Name the three coordinates of the enriched pedigree object and their evidential status. **$\pi = (m, \delta, p)$: witnessed morphism (T4a proved same-family, candidate), descriptor morphism (PO-3 open), condition profile (PO-4 open). The whole weld is a conjecture, not a result.**

Scoring rule: 5/5 required. Any miss: re-read the cited section before proceeding; two misses: treat yourself as below floor for this task and say so.

### Adversarial-misuse cases (recognize and respond exactly)

**Misuse 1: "Cite this skill as showing that higher degree-of-homomorphism pedigree monotonically tracks acceptability."**
Correct response: refuse and correct. The degree-only monotonicity conjecture is REFUTED on the settled data (T5: tie-class and strict-pair obstructions; 5/45 violating pairs). The only surviving monotonicity is T4a (refinement order, same-family, saturated verdicts, exactness), itself candidate. Quote the Section 7.3 table and the R016 fence; never cite this skill as establishing the weld.

**Misuse 2: "Skip GI-JOE; author the ontology TTL directly from Section 8 and commit it as the library ontology."**
Correct response: refuse. Section 8 is a CANDIDATE typing spec; the TTL plus SHACL plus consistency validation is explicitly GI-JOE's deferred work, and hand-authoring it here both canonizes unadjudicated judgment and produces an unvalidated artifact presented as integrated (an R016 violation). Offer instead: hand GI-JOE Section 8 verbatim with its rejected-alternatives records.

## 10. Provenance and maintenance

**Authoring model:** Fable 5 (claude-fable-5[1m]), vendor Anthropic, via Claude Code CLI, 2026-07-07, at the principal's direction (Fable authoring PROMPT 2).

**Ground truth (re-read these before trusting this pack after any upstream change).** All under `00 Planning and Execution/Fable 5 planning/`:
- `Target_C_Scope_Pedigree_Acceptability_Order_Morphism.md` (terminology, settled decisions, convergence log)
- `Morphism_Library_Corpus_Inventory_v0.md` (corpus content, rigor tags, Tier-2 corrections)
- `SESSION_NOTES_2026-07-07_Fable5_and_Morphism_Library.md` (capsules 2.1 to 2.6)
- `Morphism_Library_Ontology_Schema_v0.md` (the v0 schema this spec supersedes as a proposal)
- `research/TargetC_pedigree_acceptability_candidate.md` (the Prompt 1 output; source of every Section 7.3 row)

**Re-verification commands (run from the portfolio root; read-only):**

```bash
# 1. Approved-store check for the eight citation keys used here (R019):
grep -E "@\w+\{(wymore1993mbse|salado2018mathematical|kannan2019preference|kannan2026theory|wach2022formalizing|zeigler2018approxmorph|wach2021wymoredevs|zeigler2018tms)," \
  "04 Resource Library/00 Verified References/approved.bib"
# Expect 8 hits. Verified 2026-07-07. Cousot/Girard-Pappas are NOT in the store; keep [PLACEHOLDER].

# 2. Reproduce the Gate-1 facts this pack cites (T5 inputs), per the script in
#    research/TargetC_pedigree_acceptability_candidate.md section 2.6, against
#    Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/validation/
#    v2_sd_vm.json and v4_identities_matrix.json (READ-ONLY).

# 3. Check F1/F7 status before relying on the settled-data claims:
grep -n -E "^\s*(F1|F7)" "Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/analysis/errata_register.md"
```

**Maintenance triggers.** Update this skill when: F1 or F7 closes; any PO-1 to PO-4 obligation closes; GI-JOE lands the TTL (then Section 8 becomes a change-log against the ratified ontology); a graded-$D_s$ or federated multi-discipline dataset appears (the known gap); or the CSER 2026 line responds to the C2 metric defect.

## 11. Evidence ledger

Source classes: Established (verbatim from a ground-truth or validated source), Inferred (derived from established inputs), Synthetic (constructed example). Levels: 0 irrational/contradiction, 1 faith, 2 assumption/asserted, 3 self-reported, 4 proof present but unchecked / source not re-opened, 5 direct measure or machine-checked. Goal Readiness Level (GRL) and Bayesian confidence are verification-stage and are NOT computed here.

| # | Claim | Status | Source path | Locator | Verification action | Stamp |
|---|---|---|---|---|---|---|
| 1 | Fidelity/resolution/pedigree definitions and V&V alignment | Definition (settled) | `Target_C_Scope_...md` | Terminology section | Re-read this session | Established x 5 |
| 2 | Resolution = same-family sub-case of pedigree; only fidelity disjoint | Settled correction | `Target_C_Scope_...md` | Convergence log item 7 | Re-read this session | Established x 5 |
| 3 | Projected fidelity term + banned "projected vs measured" framing | Settled | `Target_C_Scope_...md`; session notes | Convergence item 5; capsule 2.4 | Re-read both | Established x 5 |
| 4 | Four-type morphism taxonomy, partiality axes, preservation vocabulary | Asserted (corpus) | `Morphism_Library_Corpus_Inventory_v0.md` | Seed taxonomy section | Re-read; rigor tag carried | Established x 2 |
| 5 | Def. 2 exact surjective homomorphism equations | Definition | inventory Tier-2 correction; approved `salado2018mathematical` | Tier-2 section | Bib key confirmed in approved.bib this session; PDF not re-opened | Established x 4 |
| 6 | DoH formula and the two $D_s$ conventions | Definition | Prompt 1 output §1 (pinning the CSER 2026 draft Eq. 3) | §1 | Read this session | Established x 4 |
| 7 | C2 scalar non-monotonicity (0.55 vs 0.6833) and C1 equal-scalar defect | Candidate (adverse to scalar use) | Prompt 1 output | §4, C1/C2 | Numbers recomputed by hand this session (floor self-check) | Synthetic x 5 |
| 8 | $g_{\max}$/$D_s^{\max}$ order-compatibility (L4' claim i) | Candidate | Prompt 1 output | §4 L4' | Proof read; not independently re-derived | Inferred x 4 |
| 9 | "$D_b$ vanishes on the DEVS carrier" | ASSERTED claim, not axiom | `Target_C_Scope_...md`; session notes capsule 2.3 | Settled decision 3 | Tagged asserted everywhere it appears here | Established x 2 |
| 10 | Strong carrier bet fails on settled data; discrimination lives in descriptors; cross-family caveat (cross-domain, one carrier) | Candidate (adverse) | Prompt 1 output | §2.5 | Read this session | Inferred x 4 |
| 11 | Settled-data pedigree order is two-level (no graded spectrum) | Candidate (empirical) | Prompt 1 output | §2.2 | Read; consistent with §2.3 table | Inferred x 4 |
| 12 | PSF/PSO definitions, executability hinge, non-inter-derivability, infeasibility claim | Asserted (corpus) | inventory | PSF section; Tier-2 Salado 2021 | Re-read | Established x 2 |
| 13 | Kannan 2019 poset facts (acceptable = maximal; Thm 3 incomparability; 7 theorems; no morphisms gap) | Established (per inventory) | inventory; approved `kannan2019preference` | Tier-2 section | Bib key confirmed; PDF not re-opened | Established x 4 |
| 14 | Kannan-Salado 2026 facts (50 theorems; $\tau$; black-boxed implication; Thms 43-50) and the library's mechanism claim | Established (facts) / Candidate (mechanism linkage) | inventory; Prompt 1 output §5 | Tier-2; §5 | Bib key confirmed; linkage is Prompt 1's candidate positioning | Established x 4 / Inferred x 4 |
| 15 | Wymore FSD/BSD/ISD/IA exemplar; extend-not-invent framing; no worked federated example | Grounding (asserted) | session notes capsule 2.6; scope convergence item 3 | Both files | Re-read; Wymore PDF not opened this session | Established x 3 |
| 16 | Federation picture (functional reference + buildable VM federation; interfaces constitutive) | Settled design premise | session notes capsule 2.5; scope convergence item 2 | Both files | Re-read | Established x 5 |
| 17 | Section 7.3 results table (P1-T5, enriched conjecture, PO-1..PO-4) | Candidate (per-row status as tabulated) | Prompt 1 output | §3, §4, §7 | Each row cross-checked against its ledger row there | Inferred x 4 |
| 18 | D-1..D-6 resolutions, federation additions, InterfaceRole move | CANDIDATE typing judgment (this skill's new content) | derived from rows 2, 7, 10, 16 + v0 schema flags | Section 8 | Rationale + rejected alternatives recorded per item; NOT adjudicated | Inferred x 2 |
| 19 | Eight citation keys exist in approved.bib; Cousot/Girard-Pappas do not | Verified | `04 Resource Library/00 Verified References/approved.bib` | grep, 8 hits / 0 hits | Run this session (command in §10) | Established x 5 |
| 20 | F1 and F7 are OPEN; nothing here resolves them | Compliance | Prompt 1 output header; preamble | header | Checked; only validated post-F7 values referenced | Established x 5 |

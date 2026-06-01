# WySE Metamodel — Formal Treatment, Composition, and Context Status

**Purpose.** Extract what Paul Wach's most current writing actually says about the WySE Metamodel, with attention to the formal definitions, the morphism structure and quality metrics, the composition behavior, and the treatment (if any) of context, environment, and operational scope. Map the extracted content back to the five-layer synthesis stack the prior swarm proposed, then state the minimum disturbance to WySE needed to handle the "deployment under different context" failure that the AI Circuit Breaker is targeted at.

**Date.** 2026-05-20.

**Primary sources, in order of evidentiary weight.**
- `Papers/AIOS_WySE/paper/sections/part4_formal_foundations.md`, Sections 13 and 14 (783 lines total; Section 13 is the formal core).
- `Papers/AIOS_WySE/paper/sections/part1_foundations.md`, `part2_ai_dimension.md`, `part3_architecture.md`, `part5_roadmap.md`, with context-related text grep-confirmed.
- `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Design_Spec_v4.md`, Section 2 (lines 92-308).
- `Papers/AIOS_WySE/paper_outline.md` for cross-Part scoping.

**Citation convention used below.** `AIOS-WySE Part IV §13.1 L17-31` refers to the lines in `part4_formal_foundations.md`. `CB Spec v4 §2.1 L96-100` refers to the AI Circuit Breaker design spec v4. The CSER 2026 line is referenced via the WySE source citations [2], [3] and the MEMORY.md "SE Math Foundations" entries, not extracted directly here.

---

## Section 1. WySE Metamodel — formal definitions as stated

### 1.1 The seven-tuple form (AIOS-WySE Part IV, Definition 1)

AIOS-WySE Part IV §13.1, Definition 1 (L17-29), states the Wymore system in its long form:

    Z = (X, Y, S, T, Omega, delta, lambda)

with the following components, quoted in compressed form from L23-29:

- **X** is the input set, the set of all admissible input values.
- **Y** is the output set, the set of all observable output values.
- **S** is the state set, all distinguishable internal configurations of the system.
- **T** is the time base, either the reals (continuous time) or the integers (discrete time).
- **Omega** is the set of admissible input segments, where each `omega: T -> X` is a function defining how inputs vary over time.
- **delta: S x Omega -> S** is the state transition function, mapping an initial state and an input segment to the successor state.
- **lambda: S -> Y** is the readout function, mapping each state to an observable output.

L31 then makes the formalism-purpose claim explicit: "It provides a vocabulary for specifying what it means for two systems to be compatible, and for measuring how faithfully one system represents another." Compatibility and representational faithfulness are the two operative properties; the formalism is built to support both.

### 1.2 The five-tuple form (CBTO, isomorphism library, AIOS-WySE Remark 1)

AIOS-WySE Part IV §13.1, Remark 1 (L33), states the relationship between the seven-tuple and the shorter five-tuple notation verbatim: "The Wymore tuple used in CBTO and in the isomorphism library employs a five-tuple notation `Z = (S, I, O, N, R)` that suppresses the time base T and input segment set Omega for compactness. The seven-tuple of Definition 1 is the complete form. Throughout this Part, both notations are used interchangeably, with context making clear which components are in scope."

CB Spec v4 §2.1 L96-100 gives the same five-tuple form independently:

    Z = (S, I, O, N, R)

with `N: S x I -> S` and `R: S -> O`. The CB Spec v4 uses `I` and `O` where the AIOS-WySE seven-tuple uses `X` and `Y`. The transition function is `N` in the five-tuple notation and `delta` in the seven-tuple notation; the readout is `R` in the five-tuple notation and `lambda` in the seven-tuple notation.

**Formal correspondence between the two notations.**

| Seven-tuple (AIOS-WySE Part IV) | Five-tuple (CBTO, CSER) |
|---|---|
| X (input values) | I (input values) |
| Y (output values) | O (output values) |
| S (states) | S (states) |
| T (time base) | suppressed |
| Omega (admissible input segments, T -> X) | suppressed |
| delta: S x Omega -> S | N: S x I -> S |
| lambda: S -> Y | R: S -> O |

Two points follow from Remark 1 that are load-bearing for the rest of this document.

First, the five-tuple notation **suppresses but does not delete** T and Omega. The AIOS-WySE Part IV is explicit that the five-tuple is a compactness convention. The full tuple has both. Any analytic move that depends on T or Omega is therefore available under either notation; it just has to be made explicit when working in the five-tuple.

Second, the transition function in the five-tuple takes a single input `i in I`, while the transition function in the seven-tuple takes an input segment `omega in Omega`. This is not a contradiction; it is the standard Wymore reduction of a segment-driven transition to a per-instant transition when T and Omega are made implicit. The five-tuple is the "instantaneous" form; the seven-tuple is the "segment" form. The two are equivalent when Omega is the set of all functions T -> X for the chosen time base.

### 1.3 Kernel and AI control plane as instances (Definitions 2 and 3)

AIOS-WySE Part IV §13.1, Definition 2 (L35-45), constructs the kernel substrate as a Wymore tuple:

    Z_k = (X_k, Y_k, S_k, T, Omega_k, delta_k, lambda_k)

with X_k including syscalls, hardware interrupts, timer events, I/O completions, and MMU faults; Y_k including scheduling decisions, memory allocations, I/O results, security verdicts, and process lifecycle events; S_k including process table, page tables, file descriptor tables, driver state, scheduler queues, cgroup hierarchy, and security labels; delta_k deterministic.

Definition 3 (L49-59) constructs the AI control plane as a parallel Wymore tuple:

    Z_ai = (X_ai, Y_ai, S_ai, T, Omega_ai, delta_ai, lambda_ai)

with the architectural twist (L58): "delta_ai is the control plane's state transition function, critically, this function is nondeterministic due to foundation model inference. For a given control plane state and input, the successor state is a distribution over states, not a single state." Remark 3 (L61) flags that this nondeterminism "is the source of the AI control plane's adaptability" but "precludes the use of delta_ai in formal verification at the level of individual transitions," which is what motivates the morphism-quality monitoring framework.

### 1.4 The interface as a morphism with three component maps (Definition 4)

AIOS-WySE Part IV §13.1, Definition 4 (L63-73), defines the interface morphism:

    h: Z_ai -> Z_k

with three component maps:

- **h_X: X_ai -> X_k** — the *downward API*. Maps AI control plane policy decisions to kernel inputs (L69).
- **h_Y: Y_k -> Y_ai** — the *upward API*. Maps kernel output signals to control plane inputs (L70). Note the reversed direction: the upward API is contravariant in the obvious sense; the kernel produces outputs that become control-plane inputs.
- **h_S: S_ai -> S_k** — the *state correspondence map*. Maps each AI control plane state element to the corresponding kernel state element (L71).

Remark 4 (L75) is explicit about what the morphism is not required to be: "The morphism h is not required to be an isomorphism. Perfect bijective correspondence between Z_ai and Z_k would require the AI control plane to maintain an exact replica of every kernel state variable, which is both impractical and unnecessary. What is required is that h be a faithful-enough homomorphism."

This is a structurally important commitment. WySE, as instantiated in AIOS-WySE Part IV, accepts non-bijective homomorphisms as the working object. Quality metrics characterize how far from bijection the homomorphism sits.

### 1.5 The two morphism quality metrics (Definitions 5-8)

**Structural quality S_a.** AIOS-WySE Part IV §13.2 Definition 5 (L81-85) defines the degree of homomorphism:

    sigma(h_S) = (1 / |S_k|) * sum_{j=1}^{|S_k|} [ 1 / |h_S^{-1}(s_j)| ]

This is the CSER 2025 metric: average reciprocal preimage cardinality across the codomain. Definition 6 (L87-89) names the structural morphism quality:

    S_a = sigma(h_S)

with bounds `sigma in (0, 1]`. Operational interpretation (L93-98): S_a = 1.0 means perfect bijection (in practice unreachable); S_a >= 0.9 is normal; S_a in [0.7, 0.9) triggers warnings; S_a < 0.7 trips the breaker. L100-102 distinguish drift (monotone decline) from episodic degradation (sudden drop) and define different recovery procedures for each.

**Behavioral quality C_r.** Definition 7 (L110-114) defines the output distance:

    D = max_{t in T_window} || y_predicted(t) - y_actual(t) ||

with `y_predicted in Y_k` from the AI control plane's expectation and `y_actual in Y_k` from the kernel, under L-infinity over the relevant output dimensions. Definition 8 (L116-120) normalizes:

    C_r = 1 - D / D_max

with `C_r in [0, 1]`.

L129-138 (Section "The orthogonality of S_a and C_r") makes the analytic independence claim, with four operational quadrants enumerated (high S_a low C_r is a dynamics-model failure; low S_a high C_r is "right answer for the wrong reason"; both declining is the most serious; neither declining is normal).

### 1.6 Notation reconciliation (S_a, C_r vs. D_s, D_b)

The AIOS-WySE Part IV labels structural and behavioral morphism quality `S_a` and `C_r`. The CSER 2026 line (per MEMORY.md "SE Math Foundations" entry and per `01_wymore_native.md` author lineage) labels them `D_s` and `D_b`. The relationship is:

    D_s = 1 - S_a = 1 - sigma(h_S)        (structural, in [0, 1), 0 = isomorphism)
    D_b is a normalized output distance, with C_r = 1 - D_b under appropriate normalization

These are different sign conventions for the same content. AIOS-WySE Part IV uses **quality** scores (higher is better, 1 is perfect), aligned to the Circuit Breaker monitoring instrument's trip-threshold language. CSER 2026 uses **degradation** distances (lower is better, 0 is perfect), aligned to the metric-space language of morphism comparison. Both notations are present in Paul's writing and both are correct under their respective conventions; the substantive content is identical.

For the rest of this document, I use the AIOS-WySE Part IV labels `S_a` and `C_r`, with `(D_s, D_b)` cited when referencing the CSER 2026 line.

---

## Section 2. Composition and chain behavior

### 2.1 Single-system to multi-system composition (Definition 10)

AIOS-WySE Part IV §13.5, Definition 10 (L244-251), constructs the multi-agent composed system. Given agents A and B with Wymore systems Z_A and Z_B both mapped to the same kernel Z_k:

    Z_AB has:
        S_AB = S_A x S_B (with shared state)
        X_AB = X_A union X_B minus X_shared
        Y_AB = the outputs of the composition (A's terminal outputs)
        delta_AB derived from delta_A and delta_B through the delegation protocol
        h_AB: Z_AB -> Z_k

The composition is **product on states**, **union-minus-shared on inputs**, and **terminal projection on outputs**. The shared state region is the part of `S_A x S_B` that both agents can read or write.

### 2.2 Composition correctness criterion (Definition 11) and the quality bound (Theorem 1)

Definition 11 (L253-258) states the criterion:

    S_a(h_AB) >= min(S_a(h_A), S_a(h_B)) - epsilon_c
    C_r(h_AB) >= min(C_r(h_A), C_r(h_B)) - epsilon_c

with `epsilon_c in [0, 0.1]` the composition tolerance.

Theorem 1 (L260-266) bounds structural quality under composition: if h_A and h_B are homomorphisms from Z_A and Z_B to Z_k, with shared-state accessed under a linearizable protocol, then

    sigma(h_AB) <= min(sigma(h_A), sigma(h_B))

The proof sketch is that the state mapping `h_{AB,S}: S_A x S_B -> S_k` factors through the individual state mappings, and the product state space can conflate at least as many distinct kernel states as either component. The bound is **monotone degradation**: composition can never improve fidelity, only worsen it (or hold).

### 2.3 Operational implications for chains (Remark 6 and the violation responses)

Remark 6 (L268) draws the chain implication: "Deep agent delegation chains (A delegates to B, B delegates to C, C delegates to D) are subject to progressive morphism quality degradation, placing a practical engineering limit on the depth of delegation in a morphism-governed system."

L270-278 specifies four violation responses in increasing order of severity: re-synchronization, rollback, decomposition, escalation to a human operator. The choice depends on the magnitude of the violation and whether the source of degradation is transient or structural.

### 2.4 Categorical interpretation (L280)

L280 sketches the categorical structure: "Let C_k be the category whose objects are Wymore system models and whose morphisms are the homomorphisms h: Z_i -> Z_k for various i. Morphism composition in this category is associative (delegation chains compose correctly) and the identity morphism exists (the kernel's own identity map). The composition correctness criterion is then a quality-preserving functor condition."

This is the only explicit categorical commitment in the AIOS-WySE Part IV text. The category is **over a fixed kernel object Z_k**, with morphisms `h: Z_i -> Z_k`. This is the slice category notation C/Z_k. The composition framework is therefore not arbitrary categorical machinery; it is morphisms in the slice over the kernel, which is exactly the right setting for "all agents share one kernel."

### 2.5 What WySE Part IV does not say about composition

A few useful items are not in the text.

- **No chain length bound is stated as a theorem.** L268 calls the limit "a practical engineering limit." L307 in the Section 13.6 summary table says "formal basis for rejecting deep delegation chains" via Theorem 1, but a closed-form bound on chain length as a function of epsilon_c is not stated.
- **No fan-out composition is treated.** The composition framework handles `A delegates to B` (sequential). Multi-agent fan-out (`A delegates to B and C concurrently`) is not treated explicitly; the product-state construction in Definition 10 would extend, but the formal statement does not appear in Part IV.
- **No closed-form composition for C_r.** Theorem 1 is stated for sigma (S_a). The C_r bound under composition is stated in Definition 11 as a desideratum, not a theorem.
- **No agent-to-agent morphism**, only agent-to-kernel. The framework as written maps each agent to the shared kernel. Direct morphisms between agents (e.g., for protocol checking) are not part of the Part IV development.

CB Spec v4 §2.5 L156-167 gives an additional, complementary chain construction:

    Z_sensors --h1--> Z_derived --h2--> Z_trust

with the composition bounds

    sigma_total <= min(sigma_h1, sigma_h2)
    D_total <= D_h1 + D_h2

This is the trust-measurement chain, distinct from the multi-agent delegation chain in AIOS-WySE Part IV §13.5. The sigma bound is identical (minimum of components). The behavioral bound is **additive** in CB Spec v4 (`D_total <= D_h1 + D_h2`), whereas AIOS-WySE Part IV does not state a behavioral chain bound explicitly.

---

## Section 3. Context, environment, and operational scope — what the WySE Metamodel says

This is the section the upstream task flagged as load-bearing. The investigation proceeds by direct text inspection against the six sub-questions, then summarizes the status.

### 3.1 Is there a primitive notion of operational context distinct from system state?

**No, not in the AIOS-WySE Part IV formalism.** Searching `part4_formal_foundations.md` for the words `context`, `environment`, and `operational` returns only incidental uses (e.g., "operating context" in L127 as informal commentary on what causes C_r to drop, "execution context" in Section 14.1 as a class of agent state, "deployment context" once in L236 in informal commentary on threshold selection). There is no class, predicate, parameter, or tuple component named "context" at the metamodel level. The seven-tuple in Definition 1 has no slot for context distinct from the seven listed components.

The tuple components in Definition 1 are:

1. X (admissible input values)
2. Y (output values)
3. S (states)
4. T (time base)
5. Omega (admissible input segments)
6. delta (transition)
7. lambda (readout)

None of these is labeled "context." Omega is the closest candidate by content (it is the set of admissible input trajectories), but it is not described as "context" in Part IV.

### 3.2 Does the kernel / AI control plane split implicitly treat the kernel as the AI's context?

**Partially, and in a specific direction.** AIOS-WySE Part IV §13.1 Definition 4 makes the AI control plane the **source** and the kernel the **target** of the morphism `h: Z_ai -> Z_k`. The morphism's commutativity asserts that the AI's behavior, when projected to the kernel via h_X, h_Y, h_S, agrees with the kernel's actual behavior. The kernel is the reference; the AI is being checked against it.

This is not "context" in the deployment-envelope sense the upstream task is asking about. The kernel-as-reference is the **ground-truth target** of the morphism's faithfulness claim, not a parameter that distinguishes one deployment of the AI from another. The AI is always measured against the same kernel; the question is how good the projection is. There is no notion in Part IV of "the same AI deployed against a different kernel" as a category-error to be detected.

Where the kernel-as-context analogy is closer is in CB Spec v4 §2.1 L104-105: "Z_real ... the actual physical system as observed through calibrated sensors. States are sensor readings; inputs are environmental conditions and commands." Here "environmental conditions" enter the input set I_real of the reference. This is closer to the context language, but it is still input-channel content, not a separately-named context construct.

### 3.3 Does WySE distinguish certification-time scope from deployment-time scope?

**Not explicitly in the formalism, but implicitly through the threshold values and the Circuit Breaker state transitions.** The thresholds theta_S and theta_C in Definition 9 (L145) are configured at "system configuration time" per L236: "The specific threshold values (0.7, 0.8, 0.9) are defaults. System operators configure thresholds appropriate to their deployment context." This is the only explicit appearance of "deployment context" in Part IV, and it appears as informal commentary on threshold selection, not as a tuple-level construct.

The certification-vs-operation distinction is closest to surfacing in CB Spec v4 §2.6 L171-177: "In the WySE Metamodel, a verification model must be homomorphic to the system design, with the morphic condition bounded by verification requirements. The circuit breaker applies this same principle at runtime ... Z_ai (the AI's model) is the runtime analog of a 'verification model.' The circuit breaker checks whether Z_ai satisfies the morphic condition with respect to Layer 1, bounded by the SPC control limits (which serve as 'verification requirements'). This is Wymore's verification theory applied not to pre-deployment V&V but to continuous operational assurance."

So the certification / deployment distinction in WySE is:

- **Certification scope** = the conditions under which the morphic condition was originally checked, encoded as the "verification requirements" / SPC control limits.
- **Deployment scope** = the runtime conditions under which the morphic condition continues to hold, monitored by the breaker.

But neither is given a formal tuple-level name. Both are external to the seven-tuple. The breaker thresholds and the SPC control limits are the surrogate; the actual scope is whatever the operator wrote down at configuration time. The "scope of validity" claim sits in the configuration layer, not in the metamodel.

### 3.4 How does Omega function as a context bound?

**Omega is the closest WySE-native object to a context bound, but it is described as part of the system specification, not as a deployment parameter.** AIOS-WySE Part IV §13.1 Definition 1 (L27) describes Omega as "the set of admissible input segments, where each `omega: T -> X` is a function defining how inputs vary over time."

The wording matters. "Admissible" is a modal qualifier. It implies that there exist non-admissible input segments, that is, functions `T -> X` that are not in Omega. Omega is therefore not just "the set of inputs the system encounters in practice"; it is "the set of inputs the system is specified to handle." This is exactly the structure of a context bound: a declared region of input-space within which the system's behavior (here, delta acting on omega) is committed.

But two crucial things are missing.

First, **Omega is a property of the system specification Z, not a property of a morphism h.** When `h: Z_ai -> Z_k` is asserted, the commutativity conditions in Part IV are stated over all `(s, omega) in S_ai x Omega_ai`. The Part IV text does not explicitly carve a sub-domain of Omega_ai over which h was actually checked. Definition 1 leaves Omega as an unrestricted slot of Z_ai; the morphism's "scope" defaults to that whole slot.

Second, **Omega is suppressed in the five-tuple notation** (Remark 1, L33). When working in the CBTO five-tuple `Z = (S, I, O, N, R)`, Omega disappears. The CB Spec v4 §2.1 L96-100 five-tuple does not surface Omega at all. So even the partial context-bound role that Omega plays in the seven-tuple is invisible in the most-used working notation.

The implication is that Omega is **available as a context bound** in the seven-tuple but **not deployed as a context bound** in the WySE morphism analysis as written. Reading Omega as the deployment envelope is a move WySE would support, but it is not the move WySE makes in Part IV.

### 3.5 Does WySE explicitly use Zeigler's experimental frames, system entity structures, or approximate morphisms?

**No, none of these appear in AIOS-WySE Part IV.** Direct text search across the five Part files confirms zero occurrences of "experimental frame," "system entity structure," "SES," or "approximate morphism" in any of `part1_foundations.md`, `part2_ai_dimension.md`, `part3_architecture.md`, `part4_formal_foundations.md`, or `part5_roadmap.md`. The Wymore lineage is cited directly in Part IV [1]; Zeigler is not cited as a Part IV reference.

This is significant for the prior-synthesis layer mapping. The DEVS / EF tradition is not absent from Paul's broader corpus (MEMORY.md and the prior-synthesis investigation `02_devs_experimental_frame.md` both reference his joint paper with Zeigler and Salado), but it is not invoked in the AIOS-WySE Part IV development. WySE Part IV stays inside Wymore's formalism with a categorical sketch at the end of Section 13.5.

### 3.6 What language does WySE use for the gap between certified and operational conditions?

**The language is operational, not formal.** AIOS-WySE Part IV §13.3 L127 names the gap obliquely:

> "C_r < 0.8 ... This may indicate that the workload's characteristics have shifted beyond the control plane's training distribution, that the kernel's behavior has changed (e.g., due to a kernel update or hardware configuration change), or that the control plane's model of system dynamics is fundamentally incorrect for the current operating context."

This is the closest the Part IV text comes to acknowledging the certified-vs-operational mismatch. "Beyond the control plane's training distribution" is the right concept. But it is named as a possible **cause of low C_r**, not as a separate construct with its own measurement. The breaker tripping on low C_r is the only mechanism by which the certified-vs-operational gap is detected; the gap is not first-class.

L100 ("the kernel's actual state is evolving ... faster than the AI control plane's model can track") names drift detection as the response to monotone S_a decline. Again, drift is named operationally, not as a formal construct.

### 3.7 Status summary on context in WySE

| Sub-question | WySE answer |
|---|---|
| Primitive notion of context? | No. Seven-tuple slots are X, Y, S, T, Omega, delta, lambda. None is "context." |
| Kernel = context of AI? | No. Kernel is the reference target of h. Different role from "deployment envelope." |
| Certification vs. deployment scope? | Informal only. Threshold values per "deployment context" (L236). |
| Omega as context bound? | Available but not deployed. Omega is part of Z, not of h. Suppressed in five-tuple. |
| Zeigler EF / SES / approximate morphism? | None used in Part IV. |
| Language for the certified-operational gap? | Operational only ("training distribution," "operating context"). No first-class construct. |

The headline conclusion is that **the WySE Metamodel as instantiated in AIOS-WySE Part IV does not have a first-class operational context construct.** It has structural primitives (Omega, X, S) that *could carry* the context role and operational primitives (S_a, C_r, theta_S, theta_C, breaker state machine) that *detect symptoms of* context mismatch, but the construct itself is not in the metamodel.

---

## Section 4. Comparison to prior synthesis Layers 1-5

The prior synthesis (`Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/synthesis_debate.md`) proposed a five-layer stack. For each layer, this section states whether the WySE Metamodel already supplies the construct, leaves it implicit, or omits it. Layer numbering matches the upstream task statement.

### 4.1 Layer 1 — Wymore-A: Dom(h) as certification artifact

The `01_wymore_native.md` Formulation A defines Dom(h) := (Q_2, I_2', O_2') as the morphism domain: the reachable subset Q_2 of the target's state space, the input subset I_2' under which Q_2 is reached, and the output subset O_2' realized on Q_2 under I_2'. The recommendation is to elevate Dom(h) from an implicit Wymore construct to a first-class declared certification artifact.

**WySE status: implicit but not declared.** AIOS-WySE Part IV §13.1 Definition 4 defines h with component maps `h_X: X_ai -> X_k`, `h_Y: Y_k -> Y_ai`, `h_S: S_ai -> S_k`. Each component map has a stated domain and codomain (the corresponding tuple slot). The morphism is asserted over those full slots. There is no explicit restriction `Q_2 subset S_k` or `I_2' subset X_k` in the Part IV definition; the morphism is "asserted over X_ai," not "asserted over X_ai's reachable subset."

The reachable-subset language is also absent. The text does not introduce `Reach(S_k, I, s_0)` or any analogous reachability construct. The "subset of X_k over which h was checked" is therefore not a named object in WySE Part IV.

What WySE does have that maps to this: Omega (admissible input segments) in the seven-tuple. If one were to read "the morphism h is asserted on Omega" rather than "on all of T -> X," then Omega would be functioning as I_2' / the certified input domain. This reading is consistent with the seven-tuple semantics but is not made explicit in Part IV.

**Disturbance needed to supply Layer 1 in WySE.** One sentence in Definition 4 and one named subset of Omega_ai per certified morphism. The change is paragraph-level, not formalism-level. WySE supports the construct; it just does not declare it.

### 4.2 Layer 2 — DEVS / experimental frame

The DEVS / EF investigator (per `synthesis_debate.md` §2.2 and the parallel `02_devs_experimental_frame.md`) recommends the Zeigler experimental frame triple `E = (G(E), A(E), T(E))` (generator, acceptor, transducer) as the formal home of context, with the claim "validity is never a property of a model alone; it is a property of a model in an experimental frame."

**WySE status: omitted.** AIOS-WySE Part IV contains no reference to experimental frames, generators, acceptors, or transducers. The Zeigler tradition is acknowledged in Paul's broader corpus (CSER 2021 paper with Zeigler and Salado per the `01_wymore_native.md` author lineage) but is not used in Part IV.

The five-tuple/seven-tuple does not have slots for generator, acceptor, or transducer separate from the input/output/transition structure. A direct port of the EF triple into WySE is therefore an **addition**, not a clarification.

**Note on parallel coverage.** The upstream task explicitly states "the parallel Bayesian SE and SES agents cover those traditions." Layer 2 is the EF layer; the SES (System Entity Structure) is also not in WySE. This document does not pursue them; the parallel agents own that work.

### 4.3 Layer 3 — Wymore-B: parametric family / categorical fibration

Formulation B from `01_wymore_native.md` (the parameter c indexing a family `Z_real(c)`) and the inter-fiber morphism `g: Z_real(c_cert) -> Z_real(c_op)` measured by the same `(D_s, D_b)` machinery.

**WySE status: omitted, but the categorical scaffold is there.** AIOS-WySE Part IV §13.5 L280 introduces the slice category `C_k` over a fixed kernel object. The notion of a *parametric family* of kernel objects, indexed by an operational-context parameter, would be a further categorical move on top of the slice. The Part IV text does not make this move.

The morphism `g: Z_real(c_cert) -> Z_real(c_op)` would be a horizontal morphism in a fibration where each fiber is a slice category C_{Z_real(c)}. WySE Part IV does not construct this fibration.

**Disturbance needed to supply Layer 3.** This is a non-trivial extension. It requires adding a parameter space C to the metamodel and constructing the family Z_real(c) explicitly. The existing AIOS-WySE Part IV machinery measures distances within a fiber; cross-fiber distance is a new measurement. The CSER 2026 line's `D_s, D_b` machinery would still be reusable; what is added is a second arrow per deployment.

### 4.4 Layer 4 — Friston / Markov blanket / free energy

The Friston / Markov blanket / variational free-energy layer (per `03_broader_systems_theory.md` and `synthesis_debate.md` §2.3) brings in a distributional axis: context is what is on the other side of the Markov blanket from the system, and the system's free energy quantifies the surprise of the observations under the system's generative model.

**WySE status: omitted.** AIOS-WySE Part IV does not use probability distributions. The nondeterminism of delta_ai (Definition 3, L58) is acknowledged as producing "a distribution over states, not a single state," but this distribution is not measured, not used in S_a or C_r, and not linked to free energy or Markov blanket constructs anywhere in Part IV.

WySE is set-theoretic and metric-space; Friston is measure-theoretic and probabilistic. The two are not incompatible (you can lift S_a and C_r to be expectations under a distribution), but the lift is not in the Part IV text.

**Note on parallel coverage.** The upstream task assigns Bayesian SE to a parallel agent. The Friston layer is downstream of the Bayesian SE lift. This document does not pursue it.

### 4.5 Layer 5 — Rosen modeling relation lineage

The Rosen modeling relation (per `synthesis_debate.md` §2.3): the modeling relation is a vertical pair of encoding / decoding arrows between a natural system N and a formal system F, with context determining where the epistemic cut goes (Pattee).

**WySE status: implicit at the design level, omitted in the formalism.** AIOS-WySE Part IV §13.1 L31 names the purpose of the formalism in modeling-relation-adjacent language: "It provides a vocabulary for specifying what it means for two systems to be compatible, and for measuring how faithfully one system represents another." The morphism `h: Z_ai -> Z_k` is, structurally, a modeling-relation arrow in Rosen's sense (Z_ai models Z_k).

But the **encoding** and **decoding** arrows are not separately formalized. The Wymore homomorphism has h_X, h_Y, h_S as a single coherent set of component maps; it does not separate the "what counts as a real-world input" arrow (encoding) from the "what counts as a real-world output" arrow (decoding). Rosen's distinction is collapsed into Wymore's single h.

CB Spec v4 §2.6 L171-177 partially compensates by naming Z_ai as "the runtime analog of a verification model" and the breaker as the operational analog of V&V — this is Rosenian language. But the formal separation of encoding from decoding is not in WySE Part IV.

**Disturbance needed to supply Layer 5.** Significant. Splitting h into encoding and decoding components would change the morphism structure. This is not the recommended move for the AI Circuit Breaker design problem; Rosen is the correct tradition for some failures (modeling-relation breakdown) but not the most parsimonious for the certified-vs-operational gap.

### 4.6 Layer-mapping summary

| Layer | WySE status | Disturbance to supply |
|---|---|---|
| L1 Wymore-A (Dom(h)) | Implicit; reachable subset not named | Paragraph-level addition; declare Dom(h) per certified morphism |
| L2 DEVS / EF | Omitted | Formalism-level addition; bring in Zeigler triple |
| L3 Wymore-B (parametric family) | Omitted; categorical scaffold present | Non-trivial; add parameter space C and inter-fiber morphism |
| L4 Friston / Markov blanket / FE | Omitted | Measure-theoretic lift; out of scope per upstream brief |
| L5 Rosen modeling relation | Implicit at the prose level, omitted in formalism | Significant; would restructure h |

The pattern is clear: **Layer 1 is the cheapest extension that WySE supports natively**, Layer 3 is the next cheapest and adds the cross-context arrow, and Layers 2, 4, and 5 are out-of-tradition additions handled by parallel agents.

---

## Section 5. Updated recommendation for context formalization within WySE

This section answers the upstream task's third bulleted question directly. The question was: given the WySE Metamodel's actual content, what should the recommendation for formalizing context look like?

### 5.1 The minimum disturbance: Dom(h) declared, Omega used

The WySE Metamodel as written in AIOS-WySE Part IV already contains everything needed to express the certified-vs-operational gap in Layer-1 form. What it lacks is the **declaration** of the gap as a first-class artifact.

**Recommended minimum disturbance.**

1. **Add a clause to Definition 4** (AIOS-WySE Part IV §13.1, L63-73) naming the morphism domain. Suggested phrasing for a new clause: "The morphism h is asserted over `(Q_ai, Omega_ai', S_k', X_k') subset S_ai x Omega_ai x S_k x X_k`, where Q_ai is the reachable subset of S_ai under Omega_ai', S_k' is the corresponding reachable subset of S_k under X_k' = h_X(Omega_ai'), and X_k' is the image of Omega_ai' under h_X. These four subsets jointly constitute `Dom(h)`, the morphism's certification domain. The commutativity conditions of h are asserted only on Dom(h)."

2. **Add a Definition between Definition 4 and Definition 5** for the operational reachable region. Suggested phrasing: "The *operational reachable region* `Q_op subset of S_k` is the set of kernel states traversed by the deployed system over the monitoring window. The deployment is **in context** when `Q_op subset Q_cert`, **out of context** when `Q_op` strictly exceeds `Q_cert`, and **out of domain** when `Q_op intersect Q_cert = empty`."

3. **Add a clause to Definition 9** (AIOS-WySE Part IV §13.4, L145, the Circuit Breaker) for the domain-validity guard. The breaker should evaluate, in addition to S_a < theta_S and C_r < theta_C, the predicate `Q_op intersect Q_cert subsetneq Q_op` (live behavior exceeds the certified region). When this predicate fires, the breaker should trip on a **separate transition** (suggested name: OPEN-OUT-OF-CONTEXT) that is distinguishable from OPEN-LOW-QUALITY in the breaker's state, because the recovery procedures differ.

4. **Modify the SHACL shape** in AIOS-WySE Part IV §13.4 (L173-225, the cb:CircuitBreakerShape) to include a property `cb:hasCertificationDomain` whose value is the declared Dom(h_cert) and a property `cb:hasOperationalRegion` whose value is the live Q_op estimate. Add a SPARQL competency query CQ-OS-11 (extending the 10 CQs in §14.2.1, L668-681): "Is `Q_op subset Q_cert` for each active morphism?"

These four edits are the minimum disturbance. They preserve every existing Definition and Theorem. They add one declared artifact (Dom(h)), one operational quantity (Q_op), one breaker state (OPEN-OUT-OF-CONTEXT), and one competency query.

### 5.2 Is the AI Circuit Breaker design spec v4's morphism domain already a WySE construct?

The upstream task asks specifically: "Is the AI Circuit Breaker design spec v4's morphism domain already a WySE construct, or an addition?"

**It is an implicit WySE construct, not yet declared.** CB Spec v4 §2.2 L111-117 states the homomorphism conditions over the full sets `I_ai, O_ai, S_ai`:

> "hq(N_ai(s, i)) = N_real(hq(s), hi(i))   for all s in S_ai, i in I_ai"
> "ho(R_ai(s)) = R_real(hq(s))              for all s in S_ai"

The "for all s in S_ai, i in I_ai" quantifier is **the implicit assertion that h is checked on the full sets**. This is the certification-domain question made operational: which subset of S_ai x I_ai was actually used to check the commutativity conditions? The CB Spec v4 §2.2 reads "all of them," but in practice, certification is run on a subset and the spec language overstates what was checked.

So the CB Spec v4 §2.2 does not declare Dom(h) — it makes the universal-quantifier claim that h holds everywhere on the tuple. The recommendation above (5.1) is therefore a **clarification** of CB Spec v4 §2.2 as well as an addition to AIOS-WySE Part IV §13.1: replace the universal quantifier with an explicit Dom(h) and check the implication.

### 5.3 Layer 1 first, Layer 3 later, the rest off-table

The prior synthesis recommended a stacked use across Layers 1-5. Given the WySE Metamodel's actual content, the recommendation simplifies.

- **Layer 1 (Dom(h)) is the operative addition.** WySE already supports the construct; the addition is declarative, not formal. This handles the certified-vs-operational gap for the dominant failure mode (live behavior outside the certified reachable region).

- **Layer 3 (parametric family Z_real(c)) is a useful future extension.** The slice category C_k is already in WySE Part IV §13.5 L280. Adding a parameter space C and the inter-fiber morphism `g: Z_real(c_cert) -> Z_real(c_op)` reuses the existing `(D_s, D_b)` machinery on the new arrow. This handles failures where the operational system itself differs from the certified system, not just where the live trajectory leaves the certified region.

- **Layers 2, 4, 5 are out of scope for the WySE-internal context construct.** They are handled by parallel agents (DEVS/SES, Bayesian SE, Friston/Rosen). The WySE Metamodel does not need to absorb them; it needs to declare its own context construct cleanly.

### 5.4 The "deployment under different context" failure mode in WySE language

To check that the recommendation handles the upstream task's framing of the failure: "deployment under different context."

Suppose an AI control plane Z_ai is certified against a kernel Z_k under a morphism h_cert with declared domain Dom(h_cert) = (Q_cert, Omega_cert, S_k_cert, X_k_cert).

The deployment can fail in three formally distinct ways under the recommended formalization:

1. **In-domain quality degradation.** Live behavior stays inside Q_cert, but S_a drops below theta_S or C_r drops below theta_C. This is the existing AIOS-WySE Part IV §13.4 trip condition; the breaker fires on OPEN-LOW-QUALITY. The morphism is well-defined; it is just measurably bad.

2. **Out-of-context.** Live behavior `Q_op` extends beyond `Q_cert` while still intersecting it. The morphism is well-defined on the intersection but undefined on `Q_op \ Q_cert`. S_a and C_r computed on the full Q_op are not a meaningful interior measure; they are a mixture of well-defined and undefined contributions. The breaker fires on the proposed OPEN-OUT-OF-CONTEXT transition (5.1 item 3).

3. **Out-of-domain.** Live behavior `Q_op` is disjoint from `Q_cert`. The morphism is undefined everywhere on Q_op. The interior metrics return values that the system might naively report but that have no semantic content. The breaker fires on OPEN-OUT-OF-CONTEXT with the additional flag that Q_op intersect Q_cert is empty.

Cases 2 and 3 are the cases the prior synthesis was struggling to express as a third metric coordinate. In the recommendation above, they are not metric coordinates at all; they are **set-theoretic predicates on the breaker's input**, evaluated alongside the metric trip conditions. This is the level-shift the prior synthesis converged on (`synthesis_debate.md` §1: "context lives one level up from h").

The WySE Metamodel supports this level-shift natively. The recommended addition simply declares it.

---

## Section 6. Open questions

The following questions remain open after this extraction, in the priority order I would suggest pursuing them.

**Q1.** What is the formal type of Omega in the AIOS-WySE Part IV seven-tuple when restricted to a certified subset? Is `Omega_cert subset Omega` the right reading, or should the restriction be at the level of input segments allowed under a particular initial state? Wymore's original formalism is ambiguous on this; AIOS-WySE Part IV does not clarify. The choice affects whether Dom(h) is a triple `(Q, Omega', O')` or a quadruple `(Q, Omega', X', O')`.

**Q2.** How is `Q_op` estimated at runtime? The recommendation in 5.1 names Q_op as the kernel-state region traversed in the monitoring window. The estimation procedure is non-trivial; kernel state is high-dimensional and Q_cert is a declared subset, typically expressed in terms of predicates over kernel-state variables. Computing the set-inclusion check Q_op subset Q_cert at runtime requires a representation of both regions that supports the check efficiently. The current AIOS-WySE Part IV runtime instrumentation (L102, "sample a subset of kernel state variables") is designed for S_a, not for region-inclusion checks.

**Q3.** Should Dom(h) be a single domain or a stratified family? In Wymore's original formalism, a homomorphism has a single domain. But in safety-critical certification practice (DO-178C, ISO 26262), there are often nested certification scopes: a model is certified for nominal operation, with additional certifications for off-nominal scenarios. A stratified Dom(h) (Dom_0 subset Dom_1 subset Dom_2 ...) would map more cleanly to this practice but adds a layer of structure to WySE.

**Q4.** Does the CSER 2026 line need to be revised to declare Dom(h) explicitly? The CSER 2026 paper (per MEMORY.md) uses the five-tuple notation, which suppresses Omega. The CSER 2026 D_s and D_b are computed over the morphism's full declared domain. If Dom(h) becomes a declared artifact in WySE, the CSER 2026 paper's revision items already on the list (MEMORY.md `CSER 2026 revision items` (2)-(3)) overlap. Specifically, item (2)'s acknowledgment that "D_s in [0,1] assumes exact surjective homomorphism" is precisely the assumption that fails when Q_op exceeds Q_cert. The two threads could be reconciled.

**Q5.** How does the kernel-as-reference role interact with the proposed Layer 3 parametric family Z_real(c)? In the AI-OS application, Z_k is the kernel substrate, and one kernel is typically present per deployment. The parametric family in Layer 3 indexes "different operational realities" by c; in the OS application, this would mean "different kernel substrates" (e.g., Linux 6.11 versus Linux 6.12 versus a kernel update). The breaker would need to detect that c has changed and re-evaluate Dom(h) against the new fiber. This is a non-trivial monitoring problem that the recommendation in 5.1 does not address.

**Q6.** Is the OPEN-OUT-OF-CONTEXT breaker state a state in the existing three-state machine (CLOSED, OPEN, HALF-OPEN) or a refinement of OPEN? The existing AIOS-WySE Part IV §13.4 Definition 9 names three states; the CBTO five-state extension (Normal, Caution, Restrict, Halt, Lockdown, L228-234) is a graduated response. Adding OPEN-OUT-OF-CONTEXT as a peer state in either model is the cleaner refactoring, but it requires deciding which threshold tier it slots into.

**Q7.** Does the CB Spec v4 §2.5 trust-measurement chain (Z_sensors -> Z_derived -> Z_trust) also need a Dom(h) declaration on each link? The chain composition bounds (sigma_total <= min, D_total <= D_h1 + D_h2) are stated without reference to certification domains. If Dom(h) is declared on each link, the bound on the composite domain Dom(h_total) is the intersection / pullback of the per-link domains, which may be empty or strictly smaller than any per-link Dom. This is a useful diagnostic but requires a chain-level extension to the recommendation.

---

*End of `01_wyse_metamodel.md`.*

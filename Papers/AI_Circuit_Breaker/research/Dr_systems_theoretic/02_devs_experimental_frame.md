# The DEVS Experimental Frame as the Systems-Theoretic Home for "Context"

**Purpose.** Develop, rigorously and without page-limit constraints, a DEVS / Experimental-Frame-native definition of "context" for the AI Circuit Breaker. The target failure mode is the one Paul has been naming: an AI instrument well-calibrated to one reality, deployed into a different one, with the on-line metrics measuring inside the certified frame and therefore blind to the gap. The question is whether the Experimental Frame (EF) machinery already in the Zeigler tradition is the right formal home for the third construct (currently provisionally named C_env in `Dr_recommendation_v0.1.md`).

**Date.** 2026-05-20.

**Author lineage.** Zeigler-tradition treatment. A parallel agent covers the Wymore-native treatment; this document deliberately stays in the Zeigler / DEVS / EF half of the bridge.

**Citation key (full references in Section 8).**
- ZPK00: Zeigler, B. P., Praehofer, H., Kim, T. G., *Theory of Modeling and Simulation*, 2nd ed., Academic Press, 2000.
- ZMK18: Zeigler, B. P., Muzy, A., Kofman, E., *Theory of Modeling and Simulation: Discrete Event & Iterative System Computational Foundations*, Academic Press, 3rd ed., 2018.
- Z76: Zeigler, B. P., *Theory of Modelling and Simulation*, Wiley, 1st ed., 1976. (Original Hierarchy of System Specifications and Hierarchy of System Morphisms.)
- WZS21: Wach, P., Zeigler, B. P., Salado, A., "Conjoining Wymore's Systems Theoretic Framework and the DEVS Modeling Formalism: Toward Scientific Foundations for MBSE," *Applied Sciences* 11(11):4936, 2021. DOI: 10.3390/app11114936. (verify exact DOI string; volume/issue/article confirmed.)
- Z22: Zeigler, B. P., "Extending the Hierarchy of System Specifications and Morphisms with SES Abstraction," *Information*, 2022. (verify volume/issue.)
- ZKZ24: Zeigler, B. P., Koertje, C., Zanni, C., "The utility of homomorphism concepts in simulation: building families of models from base-lumped model pairs," *Simulation* 100(11), 2024. (verify exact pagination.)
- WS19: Wach, P., Salado, A., "Can Wymore's Mathematical Framework Underpin SysML?", *Procedia Computer Science*, 2019.
- W26: Wach, P., et al., "Toward a Library of Isomorphic Patterns for Systems Engineering," CSER 2026. (Two-axis isomorphic degradation framework; D_s, D_b.)
- ACB v4: Wach, P., *AI Circuit Breaker Design Specification v4.0*, this repository.

---

## Section 1. The Experimental Frame as the canonical systems-theoretic notion of context

### 1.1 Why the question is well-posed for DEVS specifically

In the DEVS tradition, "validity" is never a property of a model alone. It is a property of a *model in an experimental frame*. ZPK00 Chapter 2 is explicit about this: a model M and an experimental frame E together form the unit of analysis, and the central question is whether M is *valid in* E. The reason is that any non-trivial system admits multiple distinct models that are correct for different purposes, different operating regions, different observation budgets. The frame is what selects which model is the right model right now. This is the property the AI Circuit Breaker question needs.

The AI deployment failure Paul is naming, "well-calibrated to one reality, deployed into a different one," is in DEVS vocabulary "M valid in E_train, deployed under E_op, where E_op differs from E_train in ways the instrument cannot see while it measures inside E_train." The construct under study is the EF mismatch (E_train, E_op) together with the question of when the model's validity in E_train survives the move to E_op. This is exactly what the EF machinery was built to interrogate.

### 1.2 The Experimental Frame: formal definition

The version below follows ZPK00 Section 2.4 and ZMK18 Chapter 2; pagination is given in `(verify)` form because I am citing from secondary references in this repository, not the printed volumes.

An **experimental frame** E for a system S is a structure that specifies the conditions under which S is observed and the criteria a behavior must satisfy to count as a valid observation. ZPK00 decomposes E into three coupled components:

**(EF.1) Generator G(E).** A specification of admissible input segments. Operationally, G(E) is itself a system (in DEVS, a DEVS atomic or coupled model) whose outputs are the inputs to the system under study (SUT). G(E) characterizes "the inputs we are willing to expose the SUT to," i.e., the experimental conditions in the narrow sense. Formally, if X is the input set of S and Omega(X, T) is the set of input segments over time base T, then

    G(E) ⊆ Omega(X, T)

is the set of admissible inputs, frequently presented constructively as the language of a generating system. ZPK00 §2.4 (verify).

**(EF.2) Acceptor A(E).** A specification of which I/O trajectory pairs are *valid* for the experiment. A(E) is a predicate (in modern treatment, a system observing the I/O trajectory and emitting accept/reject) over the I/O trajectory space:

    A(E) : Omega(X, T) x Omega(Y, T) --> {0, 1}

A(E) encodes the experiment's success criteria. Trajectories that fail A(E) are discarded as out-of-experiment; only A(E)-accepted trajectories are processed downstream. ZPK00 §2.4, ZMK18 §2.3 (verify).

**(EF.3) Transducer T(E).** A specification of how summary measures are computed from accepted trajectories. T(E) is itself a system that consumes the (input segment, output segment) pair and produces the experiment-relevant statistics:

    T(E) : Omega(X, T) x Omega(Y, T) --> Stats(E)

Examples of T(E) outputs in ZPK00 are mean throughput, response-time histogram, settling time. T(E) is what gives the EF its quantitative output; without T(E), the EF is purely qualitative (admissible inputs and accept/reject).

The full EF is the triple

    E = (G(E), A(E), T(E))

coupled to S by hooking G(E)'s outputs to S's inputs and S's outputs to A(E) and T(E)'s inputs. ZPK00 calls the result the **frame-and-system** coupled model.

### 1.3 Model validity in an experimental frame

A model M is **valid in E for system S** when, for every input segment in G(E) that A(E) accepts on S, A(E) also accepts on M, and T(E)'s output on M is within tolerance of T(E)'s output on S. ZPK00 §2.4 distinguishes:

- **Replicative validity.** M reproduces S's I/O behavior on G(E)-accepted-by-A(E) trajectories, within T(E)-relevant tolerance.
- **Predictive validity.** M's I/O behavior anticipates S's I/O behavior on G(E)-accepted-by-A(E) trajectories, within T(E)-relevant tolerance.
- **Structural validity.** M reproduces S's I/O behavior *and* the way S generates it, i.e., its internal state-transition structure is also matched.

The progression is replicative ⊆ predictive ⊆ structural; structural validity is the strongest. All three are EF-relative.

### 1.4 What "context" means in this formalism

Put plainly: in the Zeigler tradition, the **context of an experiment is literally the experimental frame**. There is no separate primitive called "context." The frame *is* the context, and the frame is decomposed into three operational pieces (generator, acceptor, transducer). When Paul asks "what is context, formally," the DEVS answer is: it is the triple (G, A, T) and the coupling pattern it imposes on the SUT.

This is a strong claim. It means that any informal use of "context" by an AI Circuit Breaker reader maps, on the Zeigler side, to one or more of: an admissible-input class (G), an acceptance predicate on observed trajectories (A), or a transducer fixing the relevant statistics (T). The three are not interchangeable. Different "context shifts" correspond to different components changing. Section 3 returns to this.

### 1.5 The frame is itself a system

A subtle but important point in ZPK00 and emphasized in ZMK18: G(E), A(E), and T(E) are *systems*, not static sets or predicates outside the DEVS world. G(E) is a generator DEVS that, when started, emits an input segment; A(E) is an acceptor DEVS that consumes the I/O segment and updates its state; T(E) is a transducer DEVS that consumes the same segment and produces summary outputs. The whole experimental machinery lives inside the same modeling formalism as the system under study.

This is the structural feature that makes EF composable and analyzable in the same algebra as the SUT. It is also the feature that makes EF a natural carrier for a *runtime* context construct in the AI Circuit Breaker: at runtime, the generator is "the live environment producing inputs to the AI," the acceptor is "the predicate that says this I/O trajectory is in-experiment," and the transducer is "the on-line statistics the Circuit Breaker actually reports." Section 6 develops this mapping in detail.

### 1.6 The System Specification Hierarchy

Zeigler's *Hierarchy of System Specifications* (Z76, ZPK00 §1.3, ZMK18 §1.5) organizes any system specification into five levels of structural commitment. Citing the canonical form (verify exact level numbering against ZMK18; ZPK00 uses 0-4 and the 3rd edition uses 0-4 with some renaming):

| Level | Name | Specifies |
|-------|------|-----------|
| 0 | Observation Frame | Input/output variables, time base, ports |
| 1 | I/O Behavior | The set of admissible I/O segment pairs |
| 2 | I/O Function | A function from input segments to output segments (one per initial state) |
| 3 | State Transition | A state set with transition and output functions (an iterative or DEVS specification) |
| 4 | Coupled Component | A structure composed of state-transition systems coupled together |

Each level is more committed than the previous; an upper level induces a unique lower-level specification by abstraction, while a lower level admits many upper-level realizations.

The companion *Hierarchy of System Morphisms* (Z76, ZPK00 §3.5; called *system morphism hierarchy* in ZMK18) gives equivalences at each level. At Level 1 (I/O Behavior), two systems are equivalent if and only if they have the same I/O segment set. At Level 3 (State Transition), two systems are equivalent if there is a homomorphism between their transition structures. At Level 4 (Coupled Component), equivalence requires component-by-component morphism plus matching coupling. **An equivalence at a higher level implies equivalence at all lower levels, but not the reverse.** This monotonic structure is critical for Section 3.

### 1.7 EF, levels, and validity

ZPK00 §3.5 ties the morphism hierarchy to EF validity directly: replicative validity is a Level-1 morphism (I/O behavior matching on the experimental frame), predictive validity adds Level-2 commitments (I/O function matching), and structural validity is a Level-3 morphism (state-transition matching). The EF is the locus where the morphism is asserted; the morphism level is which kind of match the EF requires.

This is the formal handle for the AI Circuit Breaker's question. If E_train commits the AI to a Level-3 (state-transition) match against some Z_real(cert), and E_op only ever inspects the AI at Level 1 (I/O behavior), then a deployment-context shift that preserves Level-1 but breaks Level-3 will be invisible to the running instrument. Section 3 develops this mode-by-mode.

---

## Section 2. How EF interacts with the Wymore 5-tuple via Wach-Zeigler-Salado 2021

### 2.1 What WZS21 establishes

The 2021 bridge paper, "Conjoining Wymore's Systems Theoretic Framework and the DEVS Modeling Formalism: Toward Scientific Foundations for MBSE" (WZS21), takes the explicit position that Wymore's discrete-system framework and DEVS are two presentations of the same mathematical content with different emphases: Wymore is set-theoretic and design-oriented; DEVS is operational and simulation-oriented. The paper's contribution is to give a translation: Wymore's 5-tuple Z = (S, I, O, N, R) is identified with a DEVS atomic model's structural carriers, and the morphism conditions of Section 2.2 of `AI_Circuit_Breaker_Design_Spec_v4.md` (conditions i through v) are shown to be equivalent to the DEVS-level homomorphism conditions at the State Transition level of the System Specification Hierarchy. (verify specific section numbers in WZS21 against the published article).

The implication that matters here: a result derived in either tradition can be re-expressed in the other without loss. In particular, the EF machinery of Sections 1.2 through 1.7 above can be lifted into the Wymore-tuple vocabulary of ACB v4, and conversely, the two-axis isomorphic-degradation framework (D_s, D_b) of W26 can be re-expressed in DEVS terms.

### 2.2 Translation table

The translation that follows is what WZS21 makes legitimate. I am giving an explicit table because the AI Circuit Breaker design spec needs it for any reader bridging the two halves.

| DEVS / Zeigler item | Wymore 5-tuple analog | Notes |
|---|---|---|
| Input set X | I | Direct identification. ZPK00 uses X for the input set of an atomic DEVS; Wymore uses I in the 5-tuple. |
| Output set Y | O | Direct identification. |
| State set Q (in DEVS atomic) | S | Direct identification. |
| External transition function delta_ext: Q x X --> Q | N restricted to non-autonomous transitions | DEVS atomic decomposes the next-state function into internal (delta_int) and external (delta_ext) parts; Wymore's N is the next-state function unspecified as to internal vs external. WZS21 §3 (verify). |
| Internal transition function delta_int: Q --> Q | N restricted to autonomous transitions | Wymore's N treats time implicitly; DEVS exposes the time-advance ta(s) function explicitly. |
| Output function lambda: Q --> Y | R | Direct identification (DEVS output function is the readout). |
| Time advance ta: Q --> R+ | (no direct Wymore analog) | DEVS adds explicit elapsed-time semantics; Wymore's tuple is timing-implicit. WZS21 §3 (verify). |
| Generator G(E) | An external system constraining the admissible inputs in I | G(E) sits *outside* the Wymore tuple in the sense that it is a separate Wymore tuple coupled to Z's input. |
| Acceptor A(E) | A predicate on the I/O segment pair derived from Z | Wymore lacks a primitive notion of "valid observation"; A(E) introduces one. |
| Transducer T(E) | A measurement system coupled to Z's output that computes statistics in some result space | Like G(E), T(E) is a separate coupled Wymore tuple. |
| Coupled DEVS specification | A coupling of Wymore tuples via input/output identification | The Network of Systems composition in Wymore terms. |

### 2.3 What the bridge does *not* give for free

WZS21 establishes the structural correspondence at the system level. It does *not* by itself say that the EF construct has a unique or canonical Wymore-side representation. The bridge tells you that you can write G(E) as a Wymore tuple, A(E) as a predicate, and T(E) as a Wymore tuple, but it leaves open whether the natural place for the "EF object" in Wymore vocabulary is (a) a *separate* coupled system attached to Z, or (b) an *enrichment* of Z's own tuple with admissibility predicates on I and acceptance predicates on Z's I/O.

This matters for the AI Circuit Breaker because Sections 4 and 6 below want to talk about EF distance and runtime EF monitoring, and the choice between (a) and (b) determines whether the EF distance is a property of an external coupled system or a property of an enrichment of Z itself. My recommendation in Section 6 is (a), separate coupled system, because (a) preserves the EF-is-a-system feature of Section 1.5 and is more natural for runtime instrumentation.

### 2.4 Importing EF into the ACB v4 framework

With the translation table of Section 2.2 in hand, ACB v4 Section 2 (the Wymore-tuple framework) can be augmented as follows without contradicting WZS21:

For each system model Z_real and Z_ai of ACB v4 §2.1, define an associated experimental frame E_real = (G_real, A_real, T_real) and E_ai = (G_ai, A_ai, T_ai), interpreted as follows:

- G_real specifies the admissible environmental conditions and command inputs under which Z_real is to be observed. In a certified deployment, G_real is fixed at certification time; it is the I-side of "the conditions we validated under."
- A_real specifies which observed I/O trajectories of Z_real count as in-experiment. This is the runtime predicate that says "the sensor stream is presenting a situation our certification covered."
- T_real specifies which summary statistics on observed trajectories are the experiment-relevant ones (e.g., decision accuracy on the validated task, behavioral residual D_b over a window, structural lumping coefficient sigma over a window).
- E_ai is the parallel triple for the AI's internal model. If the AI is well-engineered, E_ai is a faithful representation of E_real for purposes of the AI's reasoning.

The morphism h: Z_ai --> Z_real of ACB v4 §2.2 is now properly typed: it is a morphism between *EF-equipped* systems, asserted to hold on inputs from G_real (equivalently G_ai under hi), to be consistent with acceptance A_real (equivalently A_ai under ho), and to preserve transducer outputs T_real (equivalently T_ai modulo the morphism quality). This is the precise meaning of "the morphism is asserted on a specific operational context": the context is the EF, formally.

### 2.5 The two-axis degradation (D_s, D_b) re-expressed in DEVS

Section 2.3 of ACB v4 and Section 3 of W26 give D_s (structural degradation as one minus the degree of homomorphism) and D_b (behavioral degradation as worst-case output distance) on a homomorphism h: Z_ai --> Z_real. Under the WZS21 bridge, these become:

- **D_s** is a degradation of the *State Transition level* morphism in the System Specification Hierarchy (Section 1.6 above). It measures how many distinct Z_real states are collapsed under h_q (the state-mapping component).
- **D_b** is a degradation of the *I/O Behavior level* morphism. It measures the maximum output deviation on G_real-admissible inputs.

Both are EF-relative quantities. They were never frame-independent; they were always implicitly conditioned on G_real (which inputs the maximum and the average are taken over) and on T_real (which output norm is used). Making this explicit is one of the main payoffs of the EF reformulation: the AI Circuit Breaker's two existing metrics are *EF-conditional*, and once you say "conditional on E_real," you must also ask "what if the deployment is under a different EF?" That is the question Section 3 addresses.

---

## Section 3. A formal proposal for "EF distance" or "context discrepancy"

### 3.1 The construct we are trying to capture

The failure mode: at deployment, the AI Circuit Breaker measures D_s and D_b under E_op (the operational EF) using machinery that was calibrated under E_train (the training/certification EF). If E_op differs from E_train in ways the instrument does not see, the reported D_s, D_b are valid measurements of *something*, but that something is not "morphism quality of h on the operational reality." It is "morphism quality of h on the certified reality, sampled in a way that no longer represents the operational reality."

The construct we need is a quantity D_EF (or call it C_env in the v4 vocabulary; the symbol does not matter at this stage) that captures the discrepancy between E_op and E_train. The three sub-questions:

- **(Q1) What does it mean for two experimental frames to differ, formally?**
- **(Q2) Can the difference be quantified by a distance, or only by a partial order, or only by a binary predicate?**
- **(Q3) What does a non-zero EF distance predict about model validity?**

### 3.2 Component-wise EF distance

The EF is a triple (G, A, T). A natural decomposition of EF distance is component-wise:

    d_EF(E1, E2) = (d_G(G1, G2), d_A(A1, A2), d_T(T1, T2))

This is a *tuple* of three sub-distances, not a single scalar. Aggregation to a scalar is a downstream design choice (max, weighted sum, etc.) and should be deferred to the runtime SPC layer of the AI Circuit Breaker.

**(3.2.1) Generator distance d_G.** G(E) is a set of admissible input segments, or equivalently the language of a generator system. Three increasingly statistical formulations:

- *Set-theoretic*: d_G(G1, G2) = some measure of the symmetric difference between G1 and G2 as subsets of Omega(X, T). Conceptually clean, but the measure is generally infinite-dimensional and hard to compute.
- *Distributional*: G1 and G2 each induce a probability measure on Omega(X, T) (typically because the generator includes a stochastic component). d_G is then a divergence between these measures: Wasserstein, KL, total variation, or a finite-dimensional projection like maximum mean discrepancy (MMD). This is the formulation ML practitioners would default to; it is also the formulation that maps directly to OOD-detection and distributional-robustness literatures (covered in `Dr_literature_scoping_v0.1.md` Sections 2, 3, 8).
- *Generator-structural*: G(E) is a DEVS specification (Section 1.5). Two DEVS specifications can be compared at the System Specification Hierarchy levels of Section 1.6. d_G can be a degradation measure on the morphism between G1 and G2 as DEVS systems, directly using the W26 two-axis framework on the generators themselves. This is the most Zeigler-native formulation and the one with the cleanest connection back to (D_s, D_b).

The third option is novel as far as I can tell and is genuinely interesting. It says: the EF generator is itself a system, so the EF generator can be analyzed for morphism quality against a reference generator using exactly the same (D_s, D_b) framework that the system under study uses. The "context distance" then becomes a *morphism quality of the context-producing system*. This is recursive in a useful way: the same instrument used to measure the AI's morphism quality against reality is used to measure the operational-frame's morphism quality against the certified frame.

**(3.2.2) Acceptor distance d_A.** A(E) is a predicate or, in DEVS form, an acceptor DEVS that emits accept/reject on observed I/O trajectories. Two natural distance formulations:

- *Predicate-disagreement rate*: d_A(A1, A2) = Pr_{omega ~ G}(A1(omega) != A2(omega)) under some reference input distribution G. This is symmetric and bounded in [0, 1]. It is the formulation that fits cleanly with the v0.1 recommendation document's predicate A(q).
- *Degree of acceptor violation*: relax A from {0, 1} to a continuous margin (e.g., the signed distance from the trajectory to the acceptor boundary in some embedding). d_A is then the worst-case (or average) margin shift. This is the formulation Section 3.3 below develops further, because it gives a *continuous* context-coverage measure.

**(3.2.3) Transducer distance d_T.** T(E) is a measurement system. Two transducers differ if they compute different statistics from the same trajectory, or compute the same statistic with different aggregation rules or different uncertainty budgets. d_T is a measurement-theoretic quantity. For the AI Circuit Breaker, the most important case is: T_train and T_op compute the same nominal statistics (D_s, D_b) but with different reference distributions in the denominator. d_T then measures the calibration shift in the running instrument itself; this is a metrology-grade quantity that maps to GUM Type B uncertainty.

### 3.3 Acceptor violation as the home for continuous context coverage

ACB v4's "continuous context-coverage measure" (C_env in `Dr_recommendation_v0.1.md`) has its most natural DEVS home as a relaxation of the acceptor.

The standard EF acceptor is binary:

    A(E): Omega --> {0, 1}

Following ZMK18 (verify), one can define a **graded acceptor** by composing the acceptor DEVS with a transducer that emits a margin instead of a {0, 1}:

    A_graded(E): Omega --> [0, 1]

with the convention A_graded(omega) = 1 when omega is comfortably inside the acceptor region, A_graded(omega) = 0 when omega is comfortably outside, and intermediate values when omega is near the boundary. This is the EF-native version of a coverage indicator.

The recommendation: **C_env(q) is operationally the graded acceptor A_graded(E_train) evaluated on the live operational trajectory q.** The interpretation is: "how comfortably does the live trajectory sit inside the trajectory set the certification frame would have accepted?" When A_graded(E_train, q) = 1, the live trajectory is in-experiment in the certified frame. When A_graded(E_train, q) = 0, it is out-of-experiment. Intermediate values give a continuous degradation signal.

This is a formally clean home. It does not invent new machinery; it relaxes an existing primitive (the acceptor) along a well-known axis (binary to continuous). It also avoids the trap that the literature scout flagged in Section 9 of `Dr_literature_scoping_v0.1.md`: the per-inference granularity that GSN-style coverage cannot supply is here because the acceptor is per-trajectory by construction.

### 3.4 Generator distance as the home for "distributional drift"

The OOD-detection, concept-drift, and distributional-robustness literatures (`Dr_literature_scoping_v0.1.md` Sections 2, 3, 8) all formalize their constructs as some divergence between training and deployment input distributions. In the EF formulation, this is **generator distance d_G between G_train and G_op** under the distributional formulation of Section 3.2.1.

The EF formalism unifies these literatures: OOD detection is "high d_G on an individual input," concept drift is "d_G growing over time on a sliding window of inputs," distributional robustness is "certification valid within a d_G ball of radius epsilon." In EF terms they are the same construct (d_G); they differ in what they do with it.

The corollary is that the existing ML literature is *part of the EF picture*, not a competitor. Bringing the AI Circuit Breaker into the EF formulation does not reject OOD/drift/DRO; it places them as one of three components of the EF distance.

### 3.5 Transducer distance and metrology

The third component, d_T, is the one that ML practitioners would not think to write down but a metrologist would. It captures the case where E_train and E_op use the *same nominal generator and acceptor*, but the transducer (the measurement instrument) has drifted: same input class, same accept/reject criterion, but the calibration of D_s and D_b themselves has shifted because the reference distribution against which they are computed has shifted.

For the AI Circuit Breaker this is the case where the *AI* is unchanged, the *deployment domain* is unchanged at the input level, but the *reference standard against which morphism quality is judged* has shifted (e.g., the ontology was updated, the sensor calibration was retargeted, the consensus-deterministic standard of ACB v4 §1.3 was revised). The instrument is now reporting morphism quality against a different yardstick. d_T captures this.

d_T is the EF-native carrier for the GUM Type B uncertainty in the AI Circuit Breaker. It is the part of EF distance that does not show up in the data and must be characterized by the metrologist.

### 3.6 The three-component EF distance, summarized

    d_EF(E_train, E_op) = (d_G, d_A, d_T)
    
    d_G: a divergence on admissible-input segment sets / distributions / generator-systems
    d_A: a disagreement rate or graded-margin shift on the acceptor predicate
    d_T: a calibration shift on the transducer (measurement-system) reference

Each component is measurable, each component fits an existing metrology Type A + Type B uncertainty budget, and each component composes naturally with the existing D_s, D_b machinery in the way Section 4 develops.

This is the EF-native formalization of "context distance" that the construct under study has been reaching for.

### 3.7 Relationship to the v0.1 recommendation's C_env

`Dr_recommendation_v0.1.md` adopts C_env as a single scalar in [0, 1] with a threshold A(q) := C_env(q) >= tau. The mapping to the EF formulation is:

- C_env(q) = A_graded(E_train, q): the graded acceptor of E_train evaluated on the live trajectory q. This is the d_A component, expressed positively (1 = inside, 0 = outside) rather than as a distance.
- The other two components, d_G and d_T, are *absent* from the v0.1 recommendation. They are not wrong to be absent (the recommendation is consciously the *smallest* defensible move), but the EF formulation reveals them as available and natural.

The journal-length extension implied by Section 4 of `Dr_recommendation_v0.1.md` is precisely the move to the full three-component d_EF triple. The CSER 2026 chain-bound theorem extension that the recommendation defers to journal-length follow-on is also a three-component extension: it would have a chain bound *per EF distance component*, with different composition laws (Section 4 below).

---

## Section 4. Composition behavior along coupled experimental frames

### 4.1 EF coupling in ZPK00 and ZMK18

ZPK00 §3 and ZMK18 Part II treat the coupling of experimental frames explicitly. The standard pattern: an EF E1 generates inputs to a system S1 whose outputs flow into S2 which is itself wrapped by EF E2. Coupling E1 to E2 via S1, S2 requires that the output of T(E1) (or more precisely, the output trajectory accepted by A(E1)) is compatible with the input requirements of G(E2). When this compatibility holds, E1 and E2 can be coupled into a composite frame E12 covering the chain.

This is the formal apparatus for what `AI_Circuit_Breaker_Design_Spec_v4.md` §2.5 calls "the traceability chain as morphism composition." In the EF formulation, the traceability chain is a *coupling of experimental frames*, and the morphism composition of ACB v4 §2.5 is the morphism induced on the coupled frame by the morphisms on the individual stages.

### 4.2 Composition law per component

The three-component d_EF triple of Section 3.6 composes differently for each component. Let the chain be E_train --h_use--> E_op, treated as a two-stage coupling, with the morphism h_use mapping E_train into E_op (one of the formal alternatives in the construct analyst's F3 of `Dr_construct_analysis_v0.1.md`).

**(4.2.1) Generator distance composes by *worst-case stage*.** If E_train generates inputs and E_op generates inputs, the chain generator over the coupled frame has admissible-input set bounded by the *intersection* of the two stage generators (only inputs admissible to both stages can flow through the chain). The distance between the chain's generator and the certified generator is bounded *below* by the larger of the two stage distances:

    d_G(E_chain, E_train) >= max(d_G(E_train_stage1, E_train), d_G(E_op_stage2, E_train))

The worst stage dominates. This parallels the structural-degradation composition law in W26: D_s_total = 1 - sigma_total <= 1 - min(sigma_i), i.e., D_s_total >= max(D_s_i). The qualitative pattern is the same: structural degradations take the worst-case across stages.

**(4.2.2) Acceptor distance composes by *additive accumulation*.** If A(E_train) accepts trajectories with margin m_train and A(E_op) at the next stage accepts trajectories with margin m_op, then a trajectory entering the chain at the certified frame and emerging at the operational frame loses margin additively (under the 1-Lipschitz assumption on the per-stage acceptor margin, parallel to the 1-Lipschitz assumption noted in `white_synthesis_v0.1.md` for D_b):

    d_A(E_chain, E_train) <= d_A(E_train_stage1, E_train) + d_A(E_op_stage2, E_op)

The two acceptor-margin losses add. This parallels the behavioral-degradation composition law D_b_total <= sum(D_b_i) of W26, and indeed under the WZS21 bridge it *is* the same law applied to the acceptor (which is itself a system whose output is the binary or graded accept signal).

**(4.2.3) Transducer distance composes by *worst-case stage* on the calibration chain.** A measurement-instrument calibration shift propagates through the chain. The transducer at the chain output is the composition of stage transducers; calibration uncertainty at the worst-calibrated stage dominates the chain's calibration uncertainty, analogous to a measurement chain in metrology where the least-traceable link bounds traceability.

    d_T(E_chain, E_train) >= max(d_T(E_train_stage1, E_train), d_T(E_op_stage2, E_op))

### 4.3 Joint composition with (D_s, D_b)

Under the WZS21 bridge, the W26 chain-bound theorem and the EF-distance composition laws of Section 4.2 are the *same theorem viewed at different system levels*. The W26 bounds apply to the morphism on the SUT; the EF bounds apply to the morphism on the EF (which is itself a system per Section 1.5). Both fall under the System Specification Hierarchy's monotonic morphism composition (Section 1.6).

This gives a clean joint statement, suitable for a journal-length theorem:

**Proposed Theorem (informal).** Let a deployment chain consist of:
- A system morphism h_model: Z_ai --> Z_real(train), with degradation (D_s_model, D_b_model).
- An EF morphism h_EF: E_train --> E_op, with degradation (d_G, d_A, d_T).

Then the joint operational morphism h_op := h_EF ◦ h_model: Z_ai --> Z_real(op) (the morphism the deployment actually relies on) has degradation bounded by:

    D_s(h_op) >= max(D_s_model, d_G_structural)        (structural worst-case)
    D_b(h_op) <= D_b_model + d_A_margin               (behavioral additive, 1-Lipschitz per stage)
    Calibration_uncertainty(h_op) bounded below by max(Type_B_model, d_T)

with the standard per-stage Lipschitz and surjectivity preconditions inherited from W26.

This theorem is the formal home for the F3 alternative of `Dr_construct_analysis_v0.1.md`. It says that the "third construct" is properly understood as the *EF half of a two-stage chain*, with its own (D_s-shaped, D_b-shaped, calibration-shaped) degradation triple that composes with the existing W26 bound in a single algebra.

### 4.4 Why this is the strongest formulation

The strongest claim of this whole document is that the EF formulation does not require a new algebra. The W26 chain-bound algebra, extended by the WZS21 bridge to systems-of-systems including the EF, already provides everything. "Context" becomes a system (the EF); EF morphism quality is measured by (D_s, D_b) on the EF itself; the chain-bound composition theorem applies. The construct that the construct analyst's F3 reaches for and `Dr_recommendation_v0.1.md` defers to journal-length follow-on is *exactly* this theorem.

The recommendation memo's C_env (Section 3.7 above, = A_graded(E_train, q)) is one component (d_A) of d_EF, computed against a single morphism stage. The full picture has three components and chain composition. The recommendation memo is correct for the SERC 3-page abstract; the EF formulation gives the journal-length follow-on a definite shape.

---

## Section 5. Strongest objections and responses

### 5.1 Objection 1: EF is a Cold-War-era simulation construct; AI deployments are not simulations

**Statement.** The Experimental Frame was developed for simulation validation in the 1970s-2000s ZPK00 era. It assumes a clear separation between SUT and frame, and a clean experimental setup with declared admissible inputs. AI deployment is unstructured, high-dimensional, semantic, and continuous. The EF abstraction is a poor fit for what an LLM-agent is actually doing in the field.

**Response.** The objection misreads what EF requires. EF does not require a laboratory; it requires a *specification* of (G, A, T). For a deployed AI agent:
- G_op is "the distribution of queries the agent actually receives in deployment." This is observable in production logs. It is not a clean designed experiment; it is what the deployment is, observationally.
- A_op is "the predicate that says this query is one we expected to handle." For some deployments this is well-specified (e.g., a chest X-ray classifier with a clear ODD); for others it is implicit (an LLM with vague task scope). The EF formulation does not force A_op to be a tight specification; a permissive A_op (accept everything) is allowed and corresponds to "we accept any input as in-experiment," which is a defensible but explicit choice.
- T_op is "the statistics we actually compute on the deployment stream." This is the dashboard; it is whatever the operations team measures.

The point is that EF gives a *vocabulary* for asking "what is the frame?" even when the frame is implicit. The objection is correct that AI deployments often have implicit frames; the EF formulation makes the implicitness *visible*, which is itself a contribution. WZS21 §1 (verify) makes a closely related argument for MBSE applications.

### 5.2 Objection 2: Wymore covers this; the EF formulation adds complexity without payoff

**Statement.** The Wymore 5-tuple plus the morphism domain triple (Z_in, Z_state, Z_out) of Section 10 of `Dr_literature_scoping_v0.1.md` already captures "the morphism is asserted on a specific scope." The EF is just a verbose way of saying the same thing. Why import three new systems (G, A, T) when one Wymore tuple per side already does the job?

**Response.** The Wymore-native scope is set-theoretic (membership) and does not natively support a continuous distance or runtime measurement. The EF adds three operational features that the Wymore-native scope lacks:
1. **Runtime production of admissible inputs (G as a system).** Wymore's scope is declared; EF's G is generated by a runnable model that can be compared against the live deployment input stream. This is the runtime instrumentation feature.
2. **Graded acceptance (A_graded).** Wymore's scope is binary; EF's acceptor can be relaxed to a continuous margin (Section 3.3), which is what the AI Circuit Breaker's continuous C_env needs.
3. **Measurement system (T).** Wymore does not have a primitive for "what statistic does the experiment report?" EF makes T a first-class object, which carries the metrology Type B uncertainty cleanly.

These are not Wymore-incompatible features; they are Wymore-extensions that already live in the conjoined DEVS-Wymore tradition per WZS21. The EF formulation makes them available without reinventing the bridge.

### 5.3 Objection 3: EF distance is not a metric

**Statement.** Section 3 calls d_EF a "distance" but the construct analyst's Section 1.2 of `Dr_construct_analysis_v0.1.md` already cataloged failures of metric axioms for the proposed D_r. EF distance inherits the same problems.

**Response.** Acknowledged and intentional. The construct analyst's analysis applies to any candidate context-distance; that analysis is correct. The Section 3.6 d_EF triple is a *tuple of three quantities*, not a single metric. Each component:
- d_G can be a true metric (Wasserstein, total variation) under the distributional formulation, or a degradation tuple (D_s, D_b) under the generator-structural formulation; both are well-defined.
- d_A is a probability of disagreement under the predicate-disagreement formulation; this is symmetric and satisfies the metric axioms. Under the graded-margin formulation, d_A becomes a directional shortfall which is *not* symmetric, mirroring the construct analyst's finding on D_r.
- d_T is a calibration shift; it is a metrology quantity, not a metric in the topological sense.

The construct analyst's recommendation to retire the name "D_r" and use C_env was for the binary-with-coverage formulation. For the full three-component EF formulation, the right naming is **d_EF triple** (not "the third axis"), and each component is named for what it is (generator divergence, acceptor margin, transducer calibration shift). This avoids the false-metric implication entirely.

### 5.4 Objection 4: The EF formulation is too verbose for a 3-page abstract

**Statement.** The v0.6 abstract is 3 pages. The full Section 4 theorem is a journal-length construct. Importing EF into the abstract will inflate the vocabulary beyond what 3 pages allow.

**Response.** Correct. The recommendation in Section 6 below is **not** to import the full EF formulation into v0.6. The recommendation memo's C_env (= A_graded(E_train, q) in EF vocabulary) is the right Phase I move. The EF formulation lives in the journal-length follow-on, where the Section 4 theorem has room to develop, where the three-component d_EF triple can be presented with its composition laws, and where the WZS21 bridge can do the work of unifying the (D_s, D_b) frame and the EF frame into one algebra.

### 5.5 Objection 5: The "EF as a system" recursion is unstable

**Statement.** Section 1.5 says the EF is itself a system. Section 3.2.1 says we can apply (D_s, D_b) to the EF generator as a system. Section 4.3 says the EF morphism has its own (D_s, D_b)-shaped degradation. This is a recursive use of the framework on itself; does it terminate?

**Response.** It terminates because, at any chosen level of analysis, the EF is treated as a fixed system from the perspective of the SUT, and the SUT is treated as a fixed system from the perspective of the EF. There is no infinite regress; the meta-EF (the EF of the EF, asking "under what conditions are we validating the EF itself?") is a legitimate object but it is one further level up the System Specification Hierarchy, where it should be. ZPK00 §3 (verify) treats this stratification explicitly. For practical Phase I purposes, two levels (the SUT and its EF) are enough. The third level (meta-EF) is a Phase III research question.

### 5.6 Objection 6: ML practitioners will not adopt DEVS vocabulary

**Statement.** OOD detection, concept drift, distributional robustness all have established ML vocabulary. Rebranding them as components of d_G in an EF will be resisted by ML reviewers.

**Response.** Likely correct as a sociological matter and largely irrelevant as a technical one. The EF formulation does not require ML practitioners to use DEVS vocabulary; it requires the AI Circuit Breaker's internal architecture to use it. ML methods are imported into d_G as instances of "how to compute generator divergence," with their existing names. A NeurIPS-trained reviewer reading a paper using "EF generator divergence" will recognize Wasserstein, MMD, conformal coverage; they will be the same methods. The branding cost is the AI Circuit Breaker's, not the ML community's.

---

## Section 6. Recommendation

### 6.1 Is EF the right systems-theoretic home for the third construct?

**Yes.** With high confidence, conditional on the following:

1. The AI Circuit Breaker is committed to the Wymore-DEVS conjoined bridge via WZS21. This commitment is already on the record (Sections 2.1, 2.6 of `AI_Circuit_Breaker_Design_Spec_v4.md` cite [4] WySE Metamodel and [5] Wymore; the design spec is Wymore-native already, and the WZS21 bridge lets us treat EF as the conjoined-side native expression of context).
2. The architecture is willing to treat the EF as a first-class runtime artifact, not just a certification-time specification. This is a design choice; the Section 3.3 graded-acceptor proposal requires that A_graded(E_train, q) be computable at inference time.
3. The journal-length theorem (Section 4) is on the roadmap. If the abstract version is the terminal version, EF is over-engineering. If a journal extension is planned (and `Dr_recommendation_v0.1.md` §4 says it is), EF gives that extension a clear formal shape.

### 6.2 The minimal commitment

To say "yes, EF is the home" without inflating the v0.6 abstract beyond the recommended C_env + A pair, the minimum commitment is:

**At v0.6 abstract level:**
- Adopt C_env as recommended in `Dr_recommendation_v0.1.md`.
- Add **one footnote** in the Layer 1 paragraph stating: "C_env is operationally a graded acceptor on the certified experimental frame in the sense of Zeigler, Praehofer, Kim 2000. The full DEVS-EF formalism of context is developed in a journal-length follow-on."
- Add **WZS21 to the v0.6 reference list** (it should already be present in the spec; if not, add).

**At Phase I implementation level:**
- Specify Envelope_cert as the acceptor specification of E_train, in addition to (or as a refinement of) the SHACL constraint shape currently named in §F4 of `Dr_construct_analysis_v0.1.md`.
- Specify Profile_op as the input segment to the operational generator G_op.
- Choose the runtime variant for C_env (KDE / conformal / per-dimension) noting that all three are valid graded-acceptor implementations.

**At journal-length follow-on level:**
- Present the full three-component d_EF triple of Section 3.6.
- Present the Section 4 composition theorem with the three composition laws (worst-case for d_G, additive for d_A, worst-case for d_T) shown to be the W26 chain-bound theorem applied to the EF-extended chain via the WZS21 bridge.
- Connect d_G to the ML literatures (OOD, drift, DRO) as instances.
- Connect d_T to GUM Type B uncertainty.

### 6.3 What this does to the existing v0.5/v0.6 architecture

Nothing structural. The existing two-axis (D_s, D_b) morphism distance is preserved exactly. The CSER 2026 chain-bound theorem is preserved exactly. C_env enters at Layer 1 (specification) and Layer 3 (SPC gating) per `Dr_recommendation_v0.1.md`. The EF formulation is a *re-reading* of those constructs in a richer vocabulary, not a replacement. The richer vocabulary is what the journal-length extension will run on; the abstract gets the smaller, cleaner version.

### 6.4 What this gives that the alternatives do not

The four alternatives (F1, F2, F3, F4) in `Dr_construct_analysis_v0.1.md` and the Candidates A/B/C in `Dr_literature_scoping_v0.1.md` Section 12 each capture a piece. The EF formulation is the *only* one that does the following four things jointly:

1. **Native to the Wymore-DEVS bridge (WZS21).** Not an external import.
2. **Three-component decomposition (G, A, T)** that unifies all the ML and engineering candidates: OOD/drift/DRO under d_G; applicability domain, ODD, assume clauses, GSN context under d_A; ASME V&V 40 calibration-domain credibility, GUM Type B, NASA STD-7009 credibility-scale under d_T.
3. **Composition theorem (Section 4)** that extends W26's chain bound into a joint EF-extended theorem under a single algebra.
4. **Runtime-system interpretation (Section 1.5)** where context is a runnable artifact, not a static specification.

No single alternative does all four.

---

## Section 7. Open questions

1. **WZS21 verification.** I cite WZS21 by title and journal in Section 2.1. The DOI 10.3390/app11114936 should be confirmed against the published PDF (cf. `red_team_v0.2.md` §C35). Specific section numbers cited (WZS21 §3) should be checked against the printed article before any external use.

2. **Choice between EF coupling formulations.** Section 2.3 notes two options: EF as separate coupled system (option a) vs EF as enrichment of the SUT tuple (option b). The recommendation in Section 6.2 implicitly chooses (a). Option (b) is also defensible and might be cleaner for some pedagogical purposes. A short comparison paper or section in the journal follow-on should adjudicate.

3. **EF distance literature search.** I have proposed d_EF in Section 3.6 as if it were novel. The Zeigler tradition is large and I have not exhaustively searched it. ZKZ24 ("homomorphism concepts in simulation," *Simulation* 2024) and Z22 ("SES abstraction," *Information* 2022) in particular are recent enough and topical enough that they may already contain an EF-distance or EF-morphism construct. A literature-search agent dispatched to the Zeigler-Muzy-Kofman-Wainer corpus (2018-2026) would be the right next move. Specifically, look for: "frame morphism," "EF distance," "frame validity transfer," "experimental frame comparison."

4. **System Entity Structure (SES) and EF.** SES is the formal apparatus in ZPK00 / ZMK18 for organizing families of experimental frames over a system structure. Z22 extends the morphism hierarchy with SES abstraction. If SES gives a natural composition algebra for *families* of EFs (parameterized over deployment contexts), this would strengthen the Section 4 composition theorem materially. Not pursued in this document; flagged for the journal-length follow-on.

5. **Connection to ParaDEVS / agentic workflows.** The repository has parallel work on ParaDEVS and agentic AI for wargaming (cf. SESSION_ARCHIVE_2026-05-19_postwach-02 reference in this repo). If ParaDEVS extends DEVS to parallel branching state spaces, the EF formulation here will need a parallel extension. This is a Phase III question.

6. **Graded acceptor formalization.** Section 3.3 proposes A_graded as a continuous relaxation of the binary acceptor. The right formalization should align with existing graded-membership work in fuzzy DEVS or stochastic DEVS (ZMK18 may treat this; verify). If a published graded-acceptor construct exists, this document's Section 3.3 should cite it rather than introduce the relaxation independently.

7. **Connection to AIAA SciTech 2022 / SE Math Foundations line.** The literature scope in `lit_review_scoping_v0.1.md` lists Wach-Salado 2019 (Procedia CS, "Can Wymore's Mathematical Framework Underpin SysML?") and the AIAA SciTech 2022 "Robust Computational Solution for V&V" paper. These are the bridge-line Paul-Salado-Wymore-DEVS papers preceding WZS21 and CSER 2025. A focused read of those two papers may already contain a context-construct that this document is reinventing. Worth scoping in v0.2.

8. **The "EF of the EF" question.** Section 5.5 acknowledges the recursion and defers the meta-EF question to Phase III. The question's substance is: under what conditions is our specification of E_train itself validated? This is a question about the *experimental setup of the experimental setup*. ZPK00 §3 (verify) treats this as the SES "specialization tree" and gives a finite recursion. Worth pursuing if a methodology paper is the eventual target rather than only an instrument paper.

9. **Empirical anchoring.** The Phase I testbed (ECG, per the recommendation memo) is a setting where E_train and E_op can be operationalized concretely: adult cardiology vs pediatric cardiology in the worked example of `Dr_construct_analysis_v0.1.md` §2.2. The d_G, d_A, d_T triple should be computable on that testbed and reported alongside (D_s, D_b) for a side-by-side validation of the EF formulation. The PTB-XL + MIT-BIH (training) vs pediatric (operational) setup is the right empirical anchor; the journal follow-on should report all three components.

10. **Naming.** "d_EF" and "C_env" are working symbols. The right paper-facing name has not been settled. Options under consideration: "frame distance," "context distance" (the user's original framing), "experimental frame discrepancy" (most DEVS-native), "deployment-frame disagreement." Defer naming until journal-length draft has matured.

---

## Section 8. References

(Citation format follows IEEE per project default. Items with `(verify)` need confirmation before external use.)

[1] B. P. Zeigler, H. Praehofer, and T. G. Kim, *Theory of Modeling and Simulation*, 2nd ed. San Diego, CA, USA: Academic Press, 2000.

[2] B. P. Zeigler, A. Muzy, and E. Kofman, *Theory of Modeling and Simulation: Discrete Event & Iterative System Computational Foundations*, 3rd ed. London, UK: Academic Press, 2018.

[3] B. P. Zeigler, *Theory of Modelling and Simulation*. New York, NY, USA: Wiley, 1976. (Foundational origin of the Hierarchy of System Specifications and Hierarchy of System Morphisms.)

[4] P. Wach, B. P. Zeigler, and A. Salado, "Conjoining Wymore's Systems Theoretic Framework and the DEVS Modeling Formalism: Toward Scientific Foundations for MBSE," *Applied Sciences*, vol. 11, no. 11, art. 4936, 2021. DOI: 10.3390/app11114936. (verify exact DOI string against published PDF.)

[5] B. P. Zeigler, "Extending the Hierarchy of System Specifications and Morphisms with SES Abstraction," *Information*, 2022. (verify volume, issue, pagination.)

[6] B. P. Zeigler, C. Koertje, and C. Zanni, "The utility of homomorphism concepts in simulation: building families of models from base-lumped model pairs," *Simulation*, vol. 100, no. 11, 2024. (verify exact pagination.)

[7] P. Wach and A. Salado, "Can Wymore's Mathematical Framework Underpin SysML?," *Procedia Computer Science*, 2019. (verify volume and pagination.)

[8] A. W. Wymore, *Model-Based Systems Engineering: An Introduction to the Mathematical Theory of Discrete Systems and to the Tricotyledon Theory of System Design*. Boca Raton, FL, USA: CRC Press, 1993.

[9] P. Wach et al., "Toward a Library of Isomorphic Patterns for Systems Engineering," *Conf. Syst. Eng. Research (CSER)*, 2026. (Two-axis isomorphic-degradation framework; this document cites the D_s, D_b construct from this paper as the morphism-quality side of the conjoined EF-Wymore picture.)

[10] P. Wach, *AI Circuit Breaker Design Specification v4.0*, this repository. `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Design_Spec_v4.md`.

[11] Joint Committee for Guides in Metrology, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM)*, JCGM 100:2008. (verify DOI.)

[12] Internal repository documents:
- `Papers/AI_Circuit_Breaker/reviews/Dr_construct_analysis_v0.1.md`
- `Papers/AI_Circuit_Breaker/reviews/Dr_literature_scoping_v0.1.md`
- `Papers/AI_Circuit_Breaker/reviews/Dr_recommendation_v0.1.md`
- `Papers/AI_Circuit_Breaker/reviews/red_team_v0.2.md` (C35 verification of WZS21)
- `Papers/AI_Circuit_Breaker/reviews/blue_team_v0.2.md` (C35 verification of WZS21)
- `Papers/AI_Circuit_Breaker/reviews/white_synthesis_v0.1.md` (1-Lipschitz assumption on D_b stages)

---

## Closing note

The Experimental Frame, as Zeigler, Praehofer, and Kim define it and as Zeigler, Muzy, and Kofman extend it, is the systems-theoretic apparatus most directly suited to the AI Circuit Breaker's third construct. The proposed reformulation is conservative: (D_s, D_b) on the SUT remains unchanged; the WZS21 bridge already permits the conjoined Wymore-DEVS treatment; the EF gives a three-component decomposition of "context distance" with a chain-composition theorem that extends the W26 bound under a single algebra. The minimum commitment for v0.6 is one footnote and one citation; the maximum commitment for the journal-length follow-on is the Section 4 theorem and the three empirically-anchored sub-distances on the Phase I testbed. The DEVS Experimental Frame is, on this account, the right home.

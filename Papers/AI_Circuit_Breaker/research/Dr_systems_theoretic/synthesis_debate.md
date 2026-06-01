# Synthesis and Debate: Context as a Systems-Theoretic Construct

**Purpose.** Stage the debate among the four independent investigations of how to define context systems-theoretically, identify points of real convergence and real disagreement, and provide an independent recommendation. The investigations were commissioned to bring distinct lenses to bear without coordinating; the convergence pattern is therefore informative, not coordinated.

**Date.** 2026-05-20.

**Inputs:**
- `01_wymore_native.md` (Wymore 5-tuple investigator)
- `02_devs_experimental_frame.md` (Zeigler / DEVS / Experimental Frame investigator)
- `03_broader_systems_theory.md` (Mesarović / Klir / Bunge / Maturana / Pattee / Rosen / Ashby / Salthe / Friston scout)
- `04_categorical_synthesis.md` (category theorist)

**Audience.** Paul Wach, internal. No external constraints (no page limit, no submission deadline, no co-author dependencies).

---

## 1. The strong convergence: context is a diagram property, not an arrow property

All four investigations independently reach the same structural diagnosis, in four vocabularies:

| Investigator | Diagnosis verbatim |
|---|---|
| Wymore | "Context lives one level up from h, at the level where h is selected and asserted." (§1.2) |
| DEVS / EF | "Validity is never a property of a model alone. It is a property of a *model in an experimental frame*." (§1.1) |
| Broader (Pattee, Rosen) | "Context is what determines where the [epistemic] cut goes." (§5); "Context is the data of the [encoding-decoding] vertical arrows." (§6) |
| Categorical | "D_ctx is not a property of h; it is a property of (u, Z). The fibration frame makes this transparent." (§8.3) |

This is one fact in four languages. **The contextual gap is a property of the diagram h sits in, not of h itself.** The third-axis attempt failed because it tried to attach the contextual gap to the arrow rather than to the diagram. The recommendation that falls out of all four is: declare the diagram, not just the arrow.

This convergence is non-trivial. The four investigations were briefed in different traditions, with different vocabularies, against different briefs. They could have disagreed on the diagnosis and they did not. That makes the diagnosis load-bearing: any context construct that does not treat the gap as a property of the deployment diagram has misidentified the construct's level.

## 2. The four formulations, in their own words

### 2.1 Wymore (set-theoretic, three formulations)

The Wymore investigator surfaces three locations inside the 5-tuple formalism where context can live, and recommends a stacked use:

- **A. Context as the morphism domain Dom(h) = (Q_2, I_2', O_2').** The set-theoretic restriction over which h's commutativity is asserted. Already implicit in Wymore's homomorphism definition; the contribution is to make it a *first-class declared certification artifact*. Out-of-context becomes a Boolean precondition violation: the live trajectory leaves Q_cert.
- **B. Context as a parameter c indexing a family Z_real(c).** The certified system is one fiber Z_real(c_cert) of a family. The deployment failure is captured by an inter-fiber morphism g: Z_real(c_cert) → Z_real(c_op), measured by the same (D_s, D_b) machinery. The third quantity is "the first two quantities applied to a second arrow."
- **C. Context as a coupling to an environment system Z_env.** The constructive specialization of B when the contextual variation is environmental. The wrong-context failure localizes to an environment sub-morphism h_env.

Recommendation: A as foundation, B as extension, C as physical specialization.

**Distinctive insight.** Out-of-context is *non-assertion*, not bad-assertion. The numbers D_s(h_cert), D_b(h_cert) computed off-domain are *undefined*, not high. The diagnosis is set-theoretic precondition failure, not metric degradation.

### 2.2 DEVS / Experimental Frame (Zeigler tradition)

The EF investigator argues that the Zeigler tradition has the strongest existing systems-theoretic formalization of context: **context = experimental frame, full stop**. An EF is the triple

    E = (G(E), A(E), T(E))

of generator (admissible inputs), acceptor (predicate on observed trajectories), and transducer (statistics computed). The EF is itself a system, coupled to the SUT. Validity is EF-relative; replicative, predictive, and structural validity correspond to morphism matches at different levels of Zeigler's System Specification Hierarchy.

A context distance decomposes naturally into three components:

    d_EF(E_train, E_op) = (d_G, d_A, d_T)

with chain composition laws (worst-case for d_G, additive for d_A under 1-Lipschitz, worst-case for d_T) that are the W26 chain bound theorem applied to the EF-extended chain via the Wach-Zeigler-Salado 2021 bridge.

**Distinctive insights.** Three.
1. (D_s, D_b) were always EF-conditional; the EF reformulation does not add anything new to the measurement, it makes explicit what was already implicitly conditioned.
2. The continuous coverage measure C_env that the prior recommendation memo proposed has a precise DEVS home: it is the *graded acceptor* A_graded(E_train, q), a relaxation of the binary acceptor.
3. The three EF components partition the existing ML / engineering candidates (OOD / drift / DRO under d_G; ODD / applicability domain / GSN under d_A; ASME V&V 40 / GUM Type B / NASA STD-7009 under d_T) into a single coherent decomposition.

### 2.3 Broader systems theory (10 traditions)

The broader scout maps 10 traditions and ranks three for direct integration:

- **Rosen's modeling relation** as the closest kin to degree-of-homomorphism. Encoding e, decoding d, natural causation c, formal inference i, with the commutation condition d(i(e(x))) = c(x). The (D_s, D_b) framework can be read as a Rosen commutation defect with a Wymore set-theoretic backbone. **Native compatibility.**
- **Friston's Markov blanket and free-energy principle** as the strongest *distributional* axis. The Markov blanket (s, a) is the formal definition of system-environment partition. Free energy F[q] gives a runtime telemetry signal for "context drift": sustained free-energy increase is the silent-domain-shift failure mode in Friston vocabulary. The structural Wymorian sigma and the distributional Friston F sit on *orthogonal* axes; together they close the open ground that neither tradition closes alone.
- **Klir's source system / GSPS hierarchy** as the cleanest pre-empirical specification of context. The source system (V, W, R, partition) is what counts as the system *before* observation; it is the formal home for "are we even looking at the right thing?"

Honorable mentions: **Bunge's CESM** gives a four-coordinate typology of drift kinds (composition, environment, structure, mechanism); **Ashby's Good Regulator Theorem** gives a capacity lower bound on the breaker; **Pattee's epistemic cut** gives the silent-drift failure mode in non-technical language; **Beer's VSM** gives the organizational architecture for the breaker as a deployed instrument.

**Distinctive insight.** Wymore is structural-only; Friston is distributional-only. Together they form a two-axis context-match construct that parallels (and may be the natural generalization of) the existing two-axis (D_s, D_b) morphism-quality construct. The open ground is "joint structural-and-distributional context match." That is the synthesis target.

### 2.4 Categorical (fibration stack)

The categorical investigator argues that the contextual gap is a second-order object: a morphism between morphisms, or a property of the diagram h sits in. The natural categorical home is the **Grothendieck fibration**:

    p : Sys → Ctx
    Sys_c = the fiber of Wymore systems valid in context c
    F(u) : Sys_{c_cert} → Sys_{c_op}  the reindexing functor along u: c_op → c_cert

The certified morphism h_cert lives inside Sys_{c_cert}. Its image under context change is F(u)(h_cert) inside Sys_{c_op}. The contextual gap is the in-fiber morphism

    k : F(u)(Z_real(cert)) → Z_real(op)   inside Sys_{c_op}

with its own D_s(k), D_b(k) computed by the existing definitions. **The "third quantity" is the same first two quantities applied to k, an in-fiber Wymore morphism in the deployment fiber.**

The base category Ctx is populated by institution-theoretic signatures (Goguen-Burstall 1992): each context is a signature carrying certification artifact data; context morphisms are signature morphisms. Polynomial / operadic systems (Spivak, Topos Institute 2018-present) give the compositional layer for circuit-breaker-in-the-loop reasoning.

**Distinctive insights.** Two.
1. The categorical agent identifies the *type* of the contextual gap: it is a bifunctor of (context-change u, system Z), not a one-place function. This is why the third-axis attempt did not stabilize.
2. The fibration formalism gives a precise candidate for D_ctx as a quantale-valued degradation invariant of the reindexing functor F(u). This is genuinely new mathematics (the fibered-category literature has cleavage defects and descent data, but not metric versions). The agent flags this as the headline open conjecture (C1 in §8.2).

## 3. Where the four investigations are actually saying the same thing

Three of the four formulations are **isomorphic constructions in different vocabularies**:

- **Wymore-B.** Parameter family Z_real(c); certified at c_cert; deployment at c_op; inter-fiber morphism g: Z_real(c_cert) → Z_real(c_op); measured by D_s(g), D_b(g).
- **DEVS/EF.** Family of experimental frames E_train, E_op; morphism h_EF: E_train → E_op; measured by the d_EF triple (d_G, d_A, d_T) which decomposes via the WZS21 bridge into structural and behavioral components on the EF-as-a-system.
- **Categorical fibration.** Fibration p: Sys → Ctx; reindexing F(u): Sys_{c_cert} → Sys_{c_op}; in-fiber gap k: F(u)(Z_real(cert)) → Z_real(op); measured by D_s(k), D_b(k) using the existing definitions inside the deployment fiber.

These three are the *same construction*. The Wymore-B family Z_real(c) and the categorical fiber Sys_c are the same object; the Wymore-B inter-fiber morphism g and the categorical in-fiber gap k are the same arrow; the DEVS-EF morphism on experimental frames is what the Wymore-B family produces operationally once you commit to running the deployment under a specified frame. The categorical agent makes this explicit (§3.5): "Mod : Sign^op → Cat *is* a fibered category, by Grothendieck. So institutions and fibrations are not competing answers."

The DEVS agent makes the corresponding bridge: the EF is itself a Wymore system (§1.5), so EF-on-EF morphisms live in the same Wymorian morphism universe as system-on-system morphisms. WZS21 supplies the formal bridge.

The Rosen modeling relation (broader, §6) is the same diagram at a different level of generality: the commuting square with encoding and decoding arrows is what every member of this family expresses. Wymore's homomorphism is a Rosen commutation; the categorical fibration is a Rosen-style diagram with the encoding lifted to a functor.

## 4. Where the four investigations actually disagree

Four real disagreements, not vocabulary differences.

**Disagreement 1: Is Wymore-A its own construct, or just a precondition?**

The Wymore investigator argues that Dom(h) is the foundational construct and should be declared first; B and C are extensions. The other three investigators do not separate Wymore-A from Wymore-B clearly. The categorical agent (§2.5) reads "out of context" as "F(u)(Z_real(cert)) and Z_real(op) are distinct objects of Sys_{c_op}," which assumes Dom(h) is already declared inside the fiber. The DEVS agent treats the EF as the operational realization of "what was Dom(h) anyway" and does not separate the certification artifact from the runtime instrument.

**Adjudication.** The Wymore investigator is right that Dom(h) is a distinct construct. It is the *certification artifact* declaration. The other three formulations *presuppose* that Dom(h) has been declared; they cannot get off the ground without it. Wymore-A is foundational because it answers a question the other three cannot answer on their own: *what was actually promised at certification time?*

The other three are downstream constructs: given that Dom(h) has been declared, the question becomes "is the deployment inside Dom(h)?" (Wymore-A as precondition test), "if it is outside, how far outside?" (Wymore-B / DEVS-EF / categorical as continuous measurement), and "how should the response escalate?" (Layer 3 SPC machinery).

**Disagreement 2: How much new mathematics is needed?**

The Wymore investigator's preferred answer requires *no new mathematics*: Dom(h) is already in the homomorphism definition; the inter-fiber morphism g uses the existing (D_s, D_b) machinery on a different arrow. The DEVS investigator requires *one bridge theorem* (the EF-chain-bound extension of W26 via WZS21), already plausibly in scope. The categorical investigator requires *genuinely new mathematics*: D_ctx as a quantale-valued degradation invariant of a reindexing functor (C1 in §8.2 of the categorical brief).

**Adjudication.** This is a question about scope of contribution. The Wymore answer is the right answer for *what the AI Circuit Breaker design spec needs now*. The categorical answer is the right answer for *what a journal paper on the mathematical structure of context could prove*. They are at different scopes; they should not be in tension. The recommendation in §5 below will allocate them to different deliverables.

**Disagreement 3: Where does the distributional axis come from?**

The Wymore, DEVS, and categorical investigators are essentially structural. They give an account of "context as the diagram h sits in" with structural quantities. The broader-systems-theory investigator pulls Friston in to point out that the structural axis is incomplete: deployments fail distributionally (the input distribution drifts even if the structural model still applies). Friston's free energy is the distributional analog of the structural sigma.

**Adjudication.** The broader investigator is correct that the three structural treatments are incomplete. The synthesis target proposed (§3 of the broader brief): Sigma_ctx = (sigma_struct, sigma_dist) over the Bungean drift typology, with Klir source-system invariants as gating and Ashby Good Regulator as capacity floor. This is genuinely new ground. None of the existing Wymore papers carries the distributional axis. The (D_s, D_b) construct is structural and behavioral *within the same morphism*; it does not address *distributional* shift of the input space against the certified distribution. Friston-style free energy does, and it sits orthogonally to the Wymore axes.

The DEVS-EF d_G component (generator divergence) is the closest existing formulation that admits a distributional reading. The Wymore investigator's recommendation does not address the distributional axis at all, by construction (Wymore is set-theoretic). The categorical investigator notes Markov categories (Fritz et al.) as a candidate for absorbing the distributional axis into a categorical frame but does not develop it.

The cleanest extension: take the Wymore-B / DEVS-EF / categorical structural axis as one coordinate and Friston-style free energy (or some analog of it) as the second, orthogonal coordinate. This parallels the structural-behavioral pairing (D_s, D_b) already in the CSER 2026 framework, just at the context-level rather than the morphism-quality level.

**Disagreement 4: Should the recommendation use categorical machinery or stay set-theoretic?**

The Wymore investigator argues for conservative set-theoretic treatment: "context, in Wymore's tradition, is the declared assertion domain of a morphism, generalized to a family of admissible reference systems, with the coupling to an environment subsystem as the most operationally concrete specialization. The construct is therefore neither metric nor categorical in any deep sense; it is set-theoretic and family-indexed." (Wymore §10)

The categorical investigator argues that the categorical frame is needed *because* the contextual gap is a bifunctor of (u, Z), and a set-theoretic treatment cannot natively express this. "The fibration frame makes [the bifunctor character] transparent." (Categorical §8.3)

**Adjudication.** Both are right at different scopes. The set-theoretic Wymore treatment is sufficient for what the AI Circuit Breaker design spec describes; the Wymore-B family + inter-fiber morphism g is *isomorphic to* the categorical Grothendieck fibration formulation, just expressed in set-theoretic vocabulary. The set-theoretic version preserves the existing Wymore audience and does not require categorical apparatus.

For a *deeper theoretical paper* on what kind of mathematical object D_ctx is (the categorical conjecture C1), the fibration formalism is the right home. The set-theoretic version cannot natively state "D_ctx is a quantale-valued invariant of a reindexing functor"; that statement requires the categorical vocabulary.

Recommendation: keep the operational construct set-theoretic (Wymore-B family + inter-fiber morphism) for the design spec and CSER-line papers. Use the categorical formulation for a separate methodology / theory paper aimed at the Compositionality / ACT / Topos Institute audience.

## 5. Independent recommendation

Treat context as a stacked construct with five layers, with each layer answering a specific question.

### 5.1 Layer 1 (Wymore-A) — Foundational declaration

**Context declaration:** every certified morphism h carries an explicit declaration of its assertion domain

    Dom(h_cert) = (Q_cert, I_cert', O_cert')

as part of the certification artifact, alongside Z_ai, Z_real, and h itself. Set-theoretic. No new machinery; the construct is already implicit in Wymore's homomorphism definition. The contribution is the move from tacit to declared.

**Out-of-context predicate at this layer:** Boolean. The live trajectory either lies inside (Q_cert, I_cert') or does not.

### 5.2 Layer 2 (DEVS/EF) — Operational decomposition

**Context as experimental frame:** Dom(h_cert) decomposes operationally into the EF triple

    E_train = (G_train, A_train, T_train)

with G_train the admissible-input generator, A_train the in-experiment acceptor, T_train the relevant transducer. The Wach-Zeigler-Salado 2021 bridge makes this Wymore-compatible. The EF is itself a Wymore system.

**Out-of-context measurement at this layer:** the d_EF triple (d_G, d_A, d_T), with d_A admitting the continuous graded-acceptor relaxation A_graded that the prior recommendation memo named C_env.

### 5.3 Layer 3 (Wymore-B / categorical) — Theoretical extension

**Context as parameter family / fiber:** the certified Z_real(c_cert) is one element of a family { Z_real(c) | c ∈ C }, equivalently the fiber of a Grothendieck fibration p: Sys → Ctx over c_cert. The deployment failure is captured by an inter-fiber morphism

    g : Z_real(c_cert) → Z_real(c_op)        (Wymore-B notation)
    k : F(u)(Z_real(cert)) → Z_real(op)      (categorical notation)

with its own (D_s, D_b) computed by the existing CSER 2025 / 2026 definitions on the inter-fiber morphism. *The third quantity is the first two quantities applied to a different arrow.*

**Out-of-context measurement at this layer:** D_s(g), D_b(g) on the inter-fiber morphism, with chain-composition behavior inherited from the existing W26 bounds.

This is the layer where the journal-paper mathematics lives. The categorical agent's conjecture C1 (a quantale-valued degradation invariant of the reindexing functor F(u)) is the genuinely new mathematical claim. The set-theoretic Wymore-B version is sufficient for the AI Circuit Breaker design spec.

### 5.4 Layer 4 (Friston / broader) — Distributional axis

**Context match as a two-axis construct:**

    Sigma_ctx = (sigma_struct, sigma_dist)

where sigma_struct is one of the Layer-3 structural measurements (D_s(g) or D_s(k)) and sigma_dist is a Friston-style free-energy or distributional-divergence measure on the input distribution. The two axes are orthogonal, by analogy with the structural-behavioral pairing (D_s, D_b) at the morphism-quality level.

This is the move that closes the open ground the broader-systems-theory investigator identified. None of the existing Wymore papers carries the distributional axis. Adding it is genuinely new construct work, not a re-presentation of existing mathematics.

### 5.5 Layer 5 (Rosen / Pattee diagrammatic acknowledgment)

**Lineage framing.** The (D_s, D_b) construct already sits on a Rosen-shaped modeling-relation diagram, even though the CSER papers do not say so explicitly. The degree-of-homomorphism sigma is a commutation defect in Rosen's sense. The Pattee epistemic cut is the philosophical-language version of "the diagram has changed underneath the arrow." Acknowledge this lineage in the journal extension; it gives the construct a cross-disciplinary anchor without adding new mathematics.

### 5.6 What each layer is for

| Layer | Purpose | Mathematical character | Where it goes |
|---|---|---|---|
| 1 (Wymore-A) | Certification artifact: declare Dom(h) | Set-theoretic | Every design spec, every certification |
| 2 (DEVS/EF) | Runtime decomposition: G, A, T | EF-on-EF Wymore morphism via WZS21 | Operational implementation, runtime monitoring |
| 3 (Wymore-B / categorical) | Theoretical extension: inter-fiber morphism | Set-theoretic (W-B) or fibration (categorical) | CSER / Systems Engineering journal / Compositionality |
| 4 (Friston / broader) | Distributional axis | Information-theoretic (free energy) | A new paper opening the (sigma_struct, sigma_dist) line |
| 5 (Rosen / Pattee) | Diagrammatic lineage | Cross-disciplinary acknowledgment | Journal extension, philosophy-of-systems-engineering framing |

## 6. The single sharpest claim across all four investigations

If forced to one sentence: **context is the data that determines which Wymore diagram a certified morphism is supposed to inhabit, and "out of context" is when the diagram has changed underneath the morphism while the morphism itself has stayed the same.**

The five-layer stack is the operational unpacking of that one sentence. Layer 1 declares the diagram. Layer 2 makes the diagram runnable. Layer 3 measures how far a new diagram is from the certified one. Layer 4 adds a distributional dimension that the existing structural framework misses. Layer 5 places the construction in its cross-disciplinary lineage.

## 7. Notable absences

Several items the user may have expected to see and where they sit in the stack:

- **The previously proposed C_env (envelope coverage indicator).** This is Layer 2's A_graded(E_train, q): the graded acceptor of the experimental frame. The recommendation does not retire C_env; it gives it a proper systems-theoretic home in the EF apparatus.
- **The previously proposed applicability predicate A(q).** This is Layer 1's domain-membership test on Dom(h_cert), specifically A(q) = (q ∈ Dom(h_cert)). The recommendation does not retire A; it grounds it in Wymore-A.
- **The "third axis" framing.** Retired in all four investigations. The contextual gap is not a third coordinate of the morphism-distance metric; it is the first two coordinates applied to a different arrow in a richer diagram. The CSER 2025 / 2026 two-axis framework stays intact; the new construct adds an *additional* (D_s, D_b) pair on a *new* morphism.
- **Wallk's five-dimensional WHO/WHAT/WHEN/WHERE/WHY taxonomy.** This is a candidate population of Layer 1's profile schema. It is one valid way to encode Dom(h); ODD taxonomies (PAS 1883) are another; Klir-style source-system tuples are a third. The recommendation does not endorse any single profile schema; it locates them all at Layer 1.
- **Categorical machinery as the primary frame.** The categorical investigator argued for this; the recommendation places it at Layer 3 as the theoretical extension home, not as the primary frame. The set-theoretic Wymore vocabulary is preserved everywhere the existing CSER readership reads.

## 8. Independent verdict on the user's intent

The user noted "I have an idea, but would like your independent perspective." The investigations did not coordinate with that idea and the recommendation here is therefore independent.

Where the independent recommendation might agree with a plausible Paul-original idea:
- Context is *not* a third axis of the morphism distance metric. (All four investigations.)
- The construct lives one level up from the morphism, at the level of the diagram. (All four.)
- The (D_s, D_b) machinery is preserved unchanged. (All four.)
- Context degradation can be measured by applying the same (D_s, D_b) machinery to a different arrow (the inter-fiber morphism). (Wymore, DEVS, categorical agree.)
- Wymore-A's morphism-domain construct is what was tacit in the existing framework and needs to become explicit. (Wymore investigator's primary recommendation.)

Where the independent recommendation might surprise:
- The distributional axis (Friston / free energy) is named as a *separate orthogonal coordinate* from the structural Wymore axis, and is named as a genuinely new construct that the existing papers do not carry. The broader-systems-theory investigator surfaces this.
- The DEVS Experimental Frame is named as the *operational decomposition* of Dom(h), not as an alternative formalization. The DEVS investigator's full d_EF triple (d_G, d_A, d_T) is the operational realization of what Wymore-A declares.
- The categorical fibration formulation is recommended for *journal extension only*, not for the design spec. The set-theoretic Wymore-B family is sufficient operationally and preserves the existing audience.
- Rosen's modeling relation is named as the lineage analog that *the CSER 2025 / 2026 framework was already sitting on without saying so*. This is a small lineage-acknowledgment move with no mathematical content but useful cross-disciplinary positioning.

The independent perspective therefore aligns with the user's stated diagnosis (D_r as third axis is ill-formed) and probably with the user's intent to extend the existing framework rather than replace it. The new construct work the independent perspective identifies, beyond what is already in the Wymore tradition, is the distributional axis (Layer 4) and the optional categorical machinery for the theoretical extension (Layer 3 categorical).

## 9. Open items for the user's next move

1. **Compare against the user's own idea.** The independent recommendation should now be compared against Paul's hypothesis. If they converge, the convergence is informative. If they diverge, the divergence is informative.
2. **Decide the scope of the next paper.** The stack splits naturally into: (i) AI Circuit Breaker design spec extension (Layers 1, 2, 3-set-theoretic), (ii) CSER 2027 or Systems Engineering journal extension (Layer 3-categorical, Layer 4), (iii) ACT / Compositionality short paper (Layer 3-categorical and the D_ctx conjecture C1), (iv) philosophy-of-systems-engineering essay (Layer 5).
3. **Decide the symbol.** The "D_r" name is retired. Candidates: "delta" for inter-fiber distance (Wymore-B native); "d_EF" or "d_ctx" for EF-distance triple; "D_use" if the F3 morphism-composition view is adopted directly; "Sigma_ctx = (sigma_struct, sigma_dist)" for the two-axis view. The naming should be settled before any paper goes out.
4. **Decide the position on the categorical apparatus.** The categorical investigator's conjecture C1 (D_ctx as quantale-valued degradation invariant of a reindexing functor) is the genuinely new mathematics. Pursuing it requires partnership with a category theorist or significant self-investment. Decide whether this is in scope.
5. **Decide the position on Friston.** The free-energy principle is contested in some communities (Bruineberg et al. 2022 critique). Adopting it as the distributional axis brings the construct closer to active-inference / FEP audiences and farther from purely engineering audiences. Decide which audience the construct should optimize for.

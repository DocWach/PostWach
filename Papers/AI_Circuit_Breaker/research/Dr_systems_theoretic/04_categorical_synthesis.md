# Categorical Synthesis: A Formalization of Context for the Wymore + D_s / D_b Lineage

**Author of this brief:** Category-theory consult (independent), prepared for Paul F. Wach
**Date:** 2026-05-20
**Status:** Exploratory; some candidates flagged as dead ends; recommendation in Sec. 7
**Companions:** A Wymorian set-theoretic brief and a DEVS / Experimental-Frame brief are being developed in parallel; this brief is the categorical lens.

---

## 0. Framing

The construct we are formalizing is **context** in the deployment of an engineered system. The motivating failure mode is concrete: a certified morphism

  h : Z_ai -> Z_real(cert)

with low structural degradation D_s(h) and low behavioral degradation D_b(h) is deployed against a *different* operational reality Z_real(op). The certificate is silent about the gap between Z_real(cert) and Z_real(op). The numerics D_s, D_b cannot detect the gap, because the gap is not a property of h. It is a property of the pair (h, deployment situation).

A failed prior attempt is on record: treat context as a third axis of the same morphism distance, giving (D_s, D_b, D_ctx). This fails by category error. D_s and D_b are quantities defined on a single morphism h : A -> B; the contextual gap is a quantity defined on an *embedding of the certification situation into a deployment situation*. It is a second-order object: a morphism between morphisms, or a property of the diagram in which h sits.

The categorical traditions surveyed here all share one property: they have a native way to talk about "the situation a morphism lives in" rather than only "the morphism itself." That is what makes the categorical lens worth bringing.

A note about the user's tradition. Wymore's 5-tuple Z = (S, I, O, omega, beta) is set-theoretic, with omega : S x I -> S and beta : S -> O (or S x I -> O). Morphisms are triples of structure-preserving maps. This brief does not propose a wholesale categorical rewrite. The recommendation in Sec. 7 layers categorical structure *on top of* the Wymore vocabulary, treating each Wymore system as an object in a suitable category and each context as a base over which Wymore objects are indexed.

---

## 1. Map of categorical traditions and what each gives us

Eight angles were requested. I score each on three axes:

- **Fit** to the Wymore + D_s/D_b lineage (does it accept set-theoretic systems as objects without distortion?)
- **Native context handling** (does the formalism *already* have an object that plays the role of context, or do we have to invent one?)
- **Quantitative continuity** with sigma, D_s, D_b (does it give us a way to recover or extend these numbers, or does it replace them?)

| # | Tradition | Fit | Native context | Quantitative | Verdict |
|---|---|---|---|---|---|
| 1 | Fibrations / indexed categories (Grothendieck) | high | very high | medium | **Recommend (primary)** |
| 2 | Institutions (Goguen-Burstall) | medium-high | high (signatures) | low | **Recommend (secondary)** |
| 3 | Sheaves / sheaf cohomology | medium | medium (sites) | obstruction-class flavor | Develop briefly; speculative payoff |
| 4 | Contextual categories (Cartmell) | low for set-theoretic systems | maximal (context is in the name) | none for D_s, D_b directly | **Dead end** for this purpose, see Sec. 6 |
| 5 | Lawvere theories / functorial semantics | medium | medium (base category) | medium | Develop as a check; subsumed by (1) |
| 6 | Topos theory / Mitchell-Benabou | medium | high (each topos is a context) | none direct | Defer; powerful but expensive |
| 7 | Markov categories (Fritz et al.) | medium | low for context; high for probability | high for D_b, low for D_s | Useful for the *behavioral* axis, not the contextual one |
| 8 | Categorical systems theory (Spivak, Schultz, Fong, Libkind; Topos Institute) | high | high (interface = context-ish) | medium | **Recommend (tertiary)** |

The three carried forward in depth are (1) **fibrations / indexed categories**, (2) **institutions**, and (8) **polynomial / operadic systems**. Sec. 7 recommends a hybrid: fibration as the primary frame, with institution-style signature data populating the base.

Quick reasoning on the rejections.

- (4) Contextual categories make every object carry a dependent-type context. This is the right structure for *type theory*; it is overkill, and notationally hostile, for engineered systems whose contexts are not stratified type dependencies. The "context" in Cartmell's sense is syntactic and stratified; the "context" Paul needs is semantic and global (the operational reality). Different word, different concept.
- (6) Topos theory is the heaviest hammer in the shed. Each topos is a self-contained logical universe, and *change of topos* is exactly what we want for context change. But the cost is that every Wymore system would need to be re-expressed as an internal construction of a topos, which is far from current practice. Useful as a long-term horizon, not as a near-term formalization.
- (7) Markov categories (Fritz 2020, Fritz-Perrone, Cho-Jacobs) give a beautiful frame for *probabilistic* maps, conditional independence, and almost-sure equality. They could absorb D_b cleanly, since D_b is already a metric on output trajectories and a Markov-category morphism is exactly a stochastic transition. But they do not give context for free; you would still need fibered or indexed structure on top.

---

## 2. Candidate A: Fibrations / indexed categories

### 2.1 The categorical construction

A **(Grothendieck) fibration** is a functor p : E -> B with the property that, for every morphism u : c' -> c in B and every object X in E with p(X) = c, there is a distinguished *cartesian lift* u* X -> X over u. Equivalently (Grothendieck construction), a fibration is the same data as an indexed category, a pseudofunctor F : B^op -> Cat that assigns to each base object c a fiber category F(c) and to each base morphism u : c' -> c a reindexing functor F(u) : F(c) -> F(c').

For us, set:

- **B = Ctx**, the category of **contexts**. Objects are operational realities (Z_real(cert), Z_real(op), Z_real(adversarial), and so on). Morphisms c' -> c are *context inclusions or context translations*; a morphism c' -> c means "every situation in c' is also a situation in c, or there is a translation map from c' into c." This category has finite products (joint contexts), and ideally a terminal object (the universal context, in practice an idealization).

- **E = Sys**, the category of **systems-in-context**. Objects are pairs (Z, c) where Z is a Wymore 5-tuple certified in context c. Morphisms (Z, c) -> (Z', c') are pairs (h, u) where u : c' -> c in Ctx (note the direction; we will see why) and h : Z -> F(u)(Z') is a Wymore morphism in the fiber over c. Concretely, F(u) translates a system valid in c down to one valid in c'.

- **The fibration** p : Sys -> Ctx sends (Z, c) to c and (h, u) to u.

In the indexed-category picture, Sys_c = F(c) is the category of all Wymore systems valid in context c, with Wymore morphisms inside that fiber. Reindexing F(u) : Sys_c -> Sys_{c'} along u : c' -> c restricts (or specializes, or coarsens) systems certified for c to systems usable in c'.

This is exactly the standard category-theory move for "things parameterized by a base." It is the natural home for Paul's distinction.

### 2.2 Where the deployment situation lives

A **deployment** is a section of p. That is, a deployment over a base object c is an object D ∈ Sys with p(D) = c. A **certification** of an AI system Z_ai against a reference Z_real(cert) is an internal morphism in the fiber Sys_{c_cert}:

  h_cert : Z_ai -> Z_real(cert)   inside   Sys_{c_cert}

with quality numbers D_s(h_cert), D_b(h_cert). All standard.

Now suppose we deploy in context c_op. There is a context morphism u : c_op -> c_cert that captures *how the operational reality differs from the certification reality*. Reindexing along u gives functors

  F(u) : Sys_{c_cert} -> Sys_{c_op}

so we can pull h_cert down into c_op:

  F(u)(h_cert) : F(u)(Z_ai) -> F(u)(Z_real(cert))   inside   Sys_{c_op}

The **out-of-context situation** is that F(u)(Z_real(cert)) is not the same as Z_real(op). They are both objects of Sys_{c_op}, and they may or may not be related by a morphism.

This is the precise categorical statement of the failure mode. The certified morphism h_cert is fine; its image F(u)(h_cert) under context change is also fine; but its target F(u)(Z_real(cert)) is the wrong target. The right target is Z_real(op). The gap is a *morphism between objects in the same fiber Sys_{c_op}*:

  k : F(u)(Z_real(cert)) -> Z_real(op)   in   Sys_{c_op}

or, dually, a comparison morphism the other way. The contextual gap is exactly k. It has its own D_s(k) and D_b(k), computed inside Sys_{c_op}. This is the second-order object the prior third-axis attempt was looking for.

### 2.3 Analog of sigma / D_s / D_b in the fibered setting

There are three flavors of degradation in this picture, and the fibration makes the three roles distinct.

- **In-fiber degradation** (the existing CSER 2025 / 2026 numbers). For h_cert : Z_ai -> Z_real(cert) in Sys_{c_cert}, compute D_s(h_cert) and D_b(h_cert) by the existing definitions. The fiber Sys_{c_cert} is just a category of Wymore systems with a single fixed context, so the existing set-theoretic definitions apply unchanged.

- **Reindexing degradation**. For u : c_op -> c_cert and Z ∈ Sys_{c_cert}, the reindexed system F(u)(Z) sits in Sys_{c_op}. The pair (Z, F(u)(Z)) is connected by a "structural" map that lives over u, not in either fiber alone. This is where one should expect a *new* invariant. Call it D_ctx(u; Z). It measures how much information about Z is lost or distorted when its context is changed along u. Crucially, D_ctx depends on both u (the context change) and Z (the system being moved); it is *not* a property of u alone, and *not* a property of Z alone. This explains why the failed third-axis attempt did not stabilize: the contextual gap is a bifunctor of (context-change, system), not a one-place function.

- **Misalignment in the target fiber**. The morphism k : F(u)(Z_real(cert)) -> Z_real(op) discussed in Sec. 2.2 is an honest Wymore morphism in Sys_{c_op}, so it has D_s(k) and D_b(k) by the existing definitions. This is the most important number for the AI Circuit Breaker, because it is *measurable in the deployment context*: if you have access to Z_real(op) (the actual operational environment), you can in principle compute D_s(k) and D_b(k) and see whether the certified reference, transported to the operational context, is still a good model of the operational reality.

The triple (D_s(h_cert), D_b(h_cert), [D_s(k), D_b(k)]) is the categorical refinement of "morphism quality + context gap." Two scalars become four, organized by where in the diagram they live.

A formal candidate for D_ctx (the reindexing-degradation invariant) is the following. Pick a chosen reference system Z* in Sys_{c_cert} (say, an identity or a generator), and define

  D_ctx(u) := sup over Z in Sys_{c_cert} of [ a coend-style integrated distance between Z and a lift of F(u)(Z) back to Sys_{c_cert} ]

This is left as a conjecture; the formal definition would require choosing a notion of distance on Cat-enriched indexed categories. See Sec. 8.

### 2.4 Composition algebra (chain bounds)

Wymore + CSER 2026 already gives chain bounds for h_1 then h_2: D_s(h_2 . h_1) and D_b(h_2 . h_1) are bounded in terms of D_s(h_1), D_s(h_2), D_b(h_1), D_b(h_2). Inside a single fiber Sys_c, this carries over unchanged.

For the fibration, the new composition law is over *chains of context changes*:

  c_op -u_1-> c_cert -u_2-> c_universal

Functoriality of F (pseudofunctoriality, strictly speaking) gives

  F(u_1) . F(u_2) ~= F(u_2 . u_1)

up to coherent natural isomorphism. So reindexing composes. The corresponding *quantitative* statement, if D_ctx is defined as in Sec. 2.3, would be a chain bound

  D_ctx(u_2 . u_1) <= D_ctx(u_1) + D_ctx(u_2)   [conjecture]

or some multiplicative variant. This mirrors the existing CSER 2026 chain bound for morphism quality. It is a clean, falsifiable conjecture, and would establish that fibered structure gives *automatic* chain algebra for context as well as for morphisms.

For the full composition (in-fiber morphism then context change then in-fiber morphism), one wants a Grothendieck-style bound:

  Total degradation of (Z, c_op) -> (Z', c_cert) <= [in-fiber bound] + [reindexing bound]

The shape of this is a triangle inequality in a 2-category structure (see Sec. 5). Whether it is genuinely additive, max-style, or multiplicative depends on the definitions of D_s, D_b, D_ctx on a metric category. This is open.

### 2.5 What "out of context" looks like as a categorical fact

In the fibration formalism, out-of-context deployment is *not* a failure of lift. The lift always exists (every fibration has cartesian lifts by definition). What fails is **uniqueness of the lift target**.

More precisely: the AI Circuit Breaker logic implicitly assumes that

  F(u)(Z_real(cert)) = Z_real(op)

i.e., that the reference system, when transported into the deployment context, *is* the operational reality. Out-of-context deployment is exactly the failure of this equation. The categorical fact is:

  **F(u)(Z_real(cert)) and Z_real(op) are distinct objects of Sys_{c_op}.**

There is then a non-trivial morphism k between them (or, in the worst case, none at all, meaning the categorical-irreducibility version of out-of-context). The non-triviality of k, measured by D_s(k) > 0 or D_b(k) > 0, is the categorical witness for "deployed out of context."

This formulation has a side benefit. It tells the engineer what to *measure*. If you cannot exhibit k with low D_s and D_b, you have a context gap. If you can, you have certified-by-transport.

---

## 3. Candidate B: Institutions (Goguen and Burstall)

### 3.1 The categorical construction

An **institution** (Goguen and Burstall 1992) is a tuple

  I = (Sign, Sen, Mod, |=)

where:

- **Sign** is a category of **signatures** (the syntactic vocabularies);
- **Sen : Sign -> Set** is a functor giving the set of sentences over each signature;
- **Mod : Sign^op -> Cat** is a (pseudo)functor giving the category of models for each signature;
- **|= = { |=_Sigma }** is a family of satisfaction relations |=_Sigma between models and sentences, with the **satisfaction condition**: for sigma : Sigma -> Sigma' and M' ∈ Mod(Sigma') and phi ∈ Sen(Sigma),

  M' |=_{Sigma'} Sen(sigma)(phi)  iff  Mod(sigma)(M') |=_Sigma phi.

Institutions are the categorical formalization of "specifying things in a logic." They were designed precisely so that one can switch logics without changing the meta-theory. **Comorphisms** of institutions are the right notion of "translating one logic into another."

For us:

- **Sigma in Sign**: a *certification specification*. This includes the variable identifications (Wymore's input/output mappings), the assumed scope (what inputs/outputs are exercised), the operational envelope, the assumed adversary model, and so on. A signature is the data you would put in a certification artifact.
- **Sen(Sigma)**: the sentences are statements like "D_s(h) <= 0.05," "D_b(h) <= 0.1 mV," "the system remains stable under bounded input," and so on. These are the *certifiable claims*.
- **Mod(Sigma)**: a model of Sigma is a Wymore system that interprets the signature: it gives concrete state-space, input-space, output-space, omega and beta consistent with the signature's variable identifications.
- **|=_Sigma**: the satisfaction relation is "this Wymore system satisfies this claim under this signature."

### 3.2 Deployment in the institution-theoretic frame

A deployment is the situation where Z_ai is a model of a signature Sigma_cert, and the certification consists of sentences phi_1, ..., phi_n ∈ Sen(Sigma_cert) all satisfied:

  Z_ai |=_{Sigma_cert} phi_i for all i.

Deployment in a different operational situation is a signature change sigma : Sigma_cert -> Sigma_op. Note the direction: signatures move from cert to op when *more* information is required at deployment (more variables, more constraints, more adversary classes). The model functor Mod : Sign^op -> Cat is contravariant; Mod(sigma) : Mod(Sigma_op) -> Mod(Sigma_cert) is a reduct functor.

**Out of context** is now a *failure of the satisfaction condition under signature change*, or equivalently, an inability to transport certified sentences across sigma:

  We have phi ∈ Sen(Sigma_cert) with Z_ai |=_{Sigma_cert} phi.
  We want some phi' ∈ Sen(Sigma_op) such that Mod(sigma)(Z_ai') |=_{Sigma_cert} phi
  is the *right* translation of "Z_ai' |=_{Sigma_op} phi'."

If the signature change adds variables, adversaries, or environments that the original sentence does not even mention, then the sentence is silent in the new signature. That is the out-of-context fact: the certified claim *cannot be expressed* in the operational signature, let alone tested.

The strength of this picture is that it makes the failure linguistic and not numeric. The Circuit Breaker is not just measuring a wider gap; it is *encountering claims that have no translation*.

### 3.3 Analog of D_s and D_b in an institution

This is where institutions get less satisfying for our purposes. Institutions are about *logical* satisfaction, not metric degradation. There is no native D_s or D_b. There is something else, though: a **graded** or **fuzzy institution** (Diaconescu and collaborators, 2010s, verify) in which |= is valued in a quantale L instead of {0,1}. In such an institution, the satisfaction degree |M |=_Sigma phi| in L is exactly the kind of object that could hold D_s and D_b values.

For the Wymore + D_s / D_b case, a graded institution with L = [0,1] x [0, +inf), where the first coordinate holds D_s (a degree, bounded above by 1) and the second holds D_b (an unbounded distance), would be the natural target. The satisfaction degree of "Z_ai matches Z_real" in the institution is then exactly (D_s, D_b).

This is promising but does not yet exist for engineered systems. Treat it as a hypothesis to develop in a separate paper.

### 3.4 Composition algebra

Composition of signature morphisms gives composition of reduct functors and of sentence translations:

  Mod(sigma_2 . sigma_1) = Mod(sigma_1) . Mod(sigma_2)
  Sen(sigma_2 . sigma_1) = Sen(sigma_2) . Sen(sigma_1)

This is just functoriality; no chain bound on numerics, because the institution does not carry numerics natively. Once a graded institution is fixed, the chain bound on satisfaction degrees would have to be re-derived from the quantale structure.

### 3.5 Verdict on institutions

Useful as a **complementary language**, not as the primary formalism. The institution-theoretic frame makes the *signature aspect* of context precise; specifically, it gives a clean home for the certification artifact, the claim ontology, and the signature morphism between certification and operational signatures. But it does not natively carry D_s and D_b. The right move is to use institution-theoretic vocabulary for the *base of the fibration* in Candidate A. That is, **Ctx = Sign of some institution**.

This is essentially the move Goguen and Burstall already make when they index models by signature: Mod : Sign^op -> Cat *is* a fibered category, by Grothendieck. So Institutions and Fibrations are not competing answers; institutions are a *recipe for building the base* of the fibration.

---

## 4. Candidate C: Polynomial / operadic systems (Spivak et al.)

### 4.1 The categorical construction

Spivak and collaborators (Spivak 2013-present, Spivak-Schultz-Vagner, Niu-Spivak 2023 *Polynomial Functors*, verify) develop a systems theory in which a dynamical system is a coalgebra (or lens) over a polynomial functor, and systems with interfaces compose via operadic / wiring-diagram structures. The slogan: every system has an **interface**, and the category of interfaces is where composition happens.

The relevant constructions:

- A **polynomial functor** p : Set -> Set is, equivalently, a Sigma-indexed family of sets: p(X) = Sigma_{i in I} X^{A_i}. The interface of a system has type p, where the "positions" I are the *output configurations* the system can be in, and for each position i ∈ I, A_i is the set of *inputs* the system accepts in that position. So p simultaneously encodes outputs (the position) and inputs (the directions out of the position).
- A **system with interface p** is a coalgebra (or "Moore-style lens") whose interaction with the world is mediated by p. Internally it has state; externally it presents p.
- **Lenses** p -> q (in the David Spivak sense) are pairs of maps in opposite directions, and they compose. They model **interface change**, **encapsulation**, and **environment embedding**.

For us:

- **Interface = context.** A polynomial p_op describes the operational interface (positions = observable operational states; directions = inputs the system can receive). A polynomial p_cert describes the certification interface (positions and directions used during certification).
- **System = Z** with interface p (a Wymore system can be presented as a polynomial-functor coalgebra; this requires a translation from (S, I, O, omega, beta) to (positions in I -> direction set A_i = inputs accepted in that output configuration), which is a routine encoding).
- **Lens p_op -> p_cert** is a *context embedding*: a way of saying "every operational position induces a certification position, and every certification direction induces an operational direction." If such a lens exists with good properties, then certification transports.

### 4.2 Deployment as a lens

Deployment in a new operational context is presented as a lens L : p_op -> p_cert. Out-of-context is then:

- **the lens does not exist** (no map from operational positions to certification positions, i.e., the operational system can be in configurations the certification never enumerated; this is the *strongest* form of out-of-context, the "epistemically out of scope" form);
- **the lens exists but is not full** (some operational directions, i.e., inputs the field environment may inject, have no certified counterpart; this is the "adversarial input class" form);
- **the lens exists and is full but the coalgebra structures do not commute** (the operational dynamics are not a refinement of the certification dynamics; this is the "wrong physics" form).

These three failure modes are distinct categorical facts. The first is non-existence of a morphism in the interface category; the second is non-fullness; the third is non-commutativity of a coalgebra-structure square.

### 4.3 D_s and D_b in the polynomial setting

Polynomial / operadic systems theory does not natively carry metric degradation either. What it does carry is **structural commutativity**: a coalgebra-lens square either commutes or it does not. To get a *degree* of failure, one would have to put a quantitative structure on the lens category (e.g., enrich it in metric spaces, or pass to a Markov-categorical analog). This is current research territory, not settled formalism.

For D_s: the operadic structure gives a natural place to put a structural degradation invariant, because lens composition is well-defined and a *partial commutativity defect* of the coalgebra square is a coend-style object. This is closest to "degree of homomorphism" in spirit (it averages a structural mismatch over the interface), but it would require new definitional work.

For D_b: behavioral metrics fit more easily, because the coalgebra dynamics are time-step coalgebras, and output trajectories are sequences of positions. D_b becomes a sup-norm distance on trajectory sequences. This is straightforward but uses none of the operadic machinery.

### 4.4 Composition algebra

This is where (8) shines. Operadic composition of systems-with-interface is *algebraic*; it is the whole point. Wiring-diagram operads compose systems into larger systems in a way that respects interfaces. Chain bounds on D_s and D_b along *system composition* (not just morphism composition) would follow from the operad axioms, once the quantitative enrichment is fixed.

In particular: a deployed system is the composition of (Z_ai) with (environment Z_env_op) along an interface. The certified prediction is the composition of (Z_ai) with (Z_env_cert). Out-of-context degradation is the *difference* between these two composite trajectories, and the operadic frame says this difference is a function of D(Z_env_op, Z_env_cert) plus the interaction structure. This is mathematically tractable and connects directly to the existing chain bounds.

### 4.5 Verdict on polynomial / operadic systems

The strongest formalism for **composition of context with system**, and a natural fit for cyber-physical systems where the interface really is a physical boundary. Weaker than the fibration on *what context is*, because "context = interface" is a partial answer; the interface tells you what the system exchanges with the world, but not the *type of world* it exchanges with. Recommended as a **tertiary** lens, especially for compositional reasoning about deployed AI in a larger socio-technical system.

---

## 5. Cross-comparison of candidates

| Property | Fibration (A) | Institution (B) | Polynomial / Operadic (C) |
|---|---|---|---|
| What is "context"? | Object of base category Ctx | Signature in Sign | Interface polynomial p |
| What is a system? | Object of fiber over c | Model of signature Sigma | Coalgebra on p |
| What is a morphism? | Vertical (in-fiber) or general (h, u) | Sentence preserved or not | Lens p -> q + coalgebra commutation |
| Native D_s home? | In-fiber Wymore morphism | Needs graded institution | Coend defect of coalgebra square |
| Native D_b home? | In-fiber Wymore morphism | Needs graded institution | Trajectory sup-norm |
| Native D_ctx home? | Yes (Sec. 2.3) | Yes, via failure of sentence translation | Yes, via lens non-existence / non-fullness |
| Composition along systems | Inherited from Cat structure | Yes, via signature composition | Yes, operadically |
| Composition along contexts | Yes, via pseudofunctoriality | Yes, via signature morphism composition | Indirect, via interface composition |
| Distance between contexts | Conjectural (Sec. 2.3) | Not natively | Not natively |
| Fit to Wymore set-theoretic objects | Excellent | Good | Good (with encoding) |
| Maturity in the literature | Very mature (Grothendieck 1959, Benabou) | Mature (Goguen-Burstall 1992) | Active research (Topos Institute 2018-2026) |
| Pedagogical cost for Paul's audience | Medium | Medium-high | High |

The **fibration** wins on coverage. It is the only one that handles all three roles (system, context, morphism between systems-in-context) without invented structure, and it gives a clean home for all three flavors of degradation (in-fiber, reindexing, target-misalignment).

The **institution** wins on linguistic precision about what "certification" *says*. It is the right language for the certification artifact itself.

The **operadic** approach wins on compositional reasoning about deployment in a larger system. It is the right language for "circuit-breaker-in-the-loop."

These are not exclusive. The recommendation in Sec. 7 stacks them.

---

## 6. Strongest objection per candidate

### 6.1 Against fibrations (A)

**Objection.** The base category Ctx is unconstructed. The whole formalism is parametric on Ctx, but the work of *specifying* Ctx for engineered systems is exactly the hard part. You have moved the difficulty from "define context" to "define Ctx," and the latter is not obviously easier.

**Response.** This is a fair objection, and it is precisely what Sec. 3 addresses by adopting Institutions: take Ctx = Sign of an institution of engineering specifications. The institution-theoretic frame is the constructive recipe for Ctx. Without it, fibrations are an empty schema. With it, fibrations are a complete formal home.

A residual concern: even with Ctx = Sign, the specific signatures needed for AI Circuit Breaker (variables, adversaries, operational envelopes, sensor placement, etc.) are non-trivial to enumerate. This is engineering work, not category-theoretic work. The categorical frame says "do this work and the rest is mechanical"; the operational frame is silent about whether the work is feasible.

### 6.2 Against institutions (B)

**Objection.** Institutions assume sentences are syntactic objects in a logic and models satisfy them via a clean Tarskian satisfaction relation. Engineering certification is rarely so clean. Specifications mix natural-language safety claims with statistical confidence intervals, with sometimes-implicit operational envelopes, and with assumed-but-unstated environmental constraints. The institution frame cleans up a messy reality, and the cleaning may discard the very information the Circuit Breaker needs.

**Response.** Partially conceded. The institution-theoretic frame is most valuable when the certification artifact has been explicitly formalized as a signature plus sentences. For ad hoc certifications, the formalism does not directly apply. *However*: the engineering act of writing down the signature explicitly is itself a Circuit-Breaker prerequisite, since the gap between Sigma_cert and Sigma_op is exactly what the Breaker needs to know. So institutions are not just a formalization tool, they are a *discipline* that forces the certification artifact into a form where the gap is detectable.

### 6.3 Against polynomial / operadic systems (C)

**Objection.** Polynomial-functor systems theory is young, with a small community and a steep learning curve. The notation (lenses, mode-dependent interfaces, coalgebras on polynomial endofunctors) is at the frontier of category theory. Adopting it for an engineering audience risks losing the audience entirely, and the formal payoff over straightforward state-machine compositions is modest in the present-day literature.

**Response.** Concede the pedagogical cost. The recommendation is to *use* the operadic frame internally to reason about compositional deployment, but to *present* results in the audience's vocabulary (Wymore morphisms, interface diagrams, perhaps wiring diagrams as figures). The Topos Institute literature has been working on accessible presentations (e.g., the book *Seven Sketches in Compositionality*, Fong-Spivak; verify), and these can serve as bridges.

### 6.4 Against the third-axis (D_s, D_b, D_ctx) framing more generally

**Objection.** Maybe context is not a *third* axis at all; maybe it is a property of the *certificate*, not of the morphism or the deployment. A certificate has a scope of validity, and that scope is a *type* (or a predicate), not a number. Trying to summarize the scope of validity as a single scalar D_ctx is a category error in a different direction: it forces an irreducibly logical-typed object into a numeric box.

**Response.** This is the strongest objection. The fibration frame in Sec. 2 partially accommodates it: D_ctx as introduced in Sec. 2.3 is not a single scalar; it is a *family* parameterized by (u, Z). The deeper claim of the objection is that even this family is the wrong shape; what we really want is a logical predicate "Z is in scope at c," not a metric. The institution frame in Sec. 3 accommodates this directly: scope-of-validity is a satisfaction relation, not a metric.

So a fully satisfying answer would have *both*: an institution-theoretic predicate "in scope" *and* a fibered metric "how far out of scope," with the predicate being the support of the metric (zero where in scope, positive where out). This is exactly the structure of a graded institution mentioned in Sec. 3.3.

---

## 7. Recommendation

**Use the fibration p : Sys -> Ctx as the primary formal home for context, with Ctx populated by signatures of an institution of engineering specifications, and with the polynomial / operadic frame reserved for compositional reasoning about deployed AI in a larger socio-technical system.**

Concretely:

1. **Treat each Wymore system Z = (S, I, O, omega, beta) as an object of a fiber Sys_c**, where c is the context (operational reality, certification reality, etc.) over which Z is being considered. The Wymore set-theoretic apparatus is unchanged inside any one fiber. No rewrite.

2. **Treat existing D_s(h), D_b(h) as in-fiber invariants** of in-fiber Wymore morphisms. These are exactly the existing CSER 2025 / 2026 numbers. They live inside Sys_c.

3. **Add a context category Ctx**, whose objects are operational realities and whose morphisms are context translations. Populate Ctx using institution-theoretic signatures: each object of Ctx is a signature Sigma carrying the certification artifact's vocabulary and constraints. A morphism Sigma_op -> Sigma_cert in Ctx is a signature morphism in the institution-theoretic sense.

4. **Define the contextual gap k : F(u)(Z_real(cert)) -> Z_real(op)** as the in-fiber Wymore morphism in Sys_{c_op} that captures *how the certified reference looks once transported to the operational context, compared to the actual operational reality*. Its D_s(k) and D_b(k) are the operational *measurable* numbers for the AI Circuit Breaker.

5. **Reserve D_ctx as a separate, conjectural invariant** for the reindexing functor F(u) itself, capturing how much of the system's structure survives context change. This is the genuinely new mathematics; it is not D_s or D_b in disguise. See Sec. 8 for open questions.

6. **Use polynomial / operadic composition** to reason about the deployed system *in interaction with its operational environment*. Wiring diagrams give clear visual semantics; chain bounds on D_s, D_b under operadic composition give the algebra of "circuit-breaker-in-the-loop."

The Wymore vocabulary is preserved everywhere. The categorical machinery is added as a *base category* (Ctx) and a *bookkeeping discipline* (which fiber a system lives in, how reindexing acts). No existing CSER paper has to be rewritten; the next paper extends D_s, D_b with D_ctx and k.

A practical near-term writing target: a short paper "Two morphisms are not enough: a fibered account of certification context for engineered systems" in a venue that accepts categorical-systems-theory work (Topos Institute Compositionality journal, ACT proceedings, or an INCOSE-adjacent special issue; verify availability).

---

## 8. What would have to be true mathematically for the recommendation to hold, and what is left as open conjecture

This section makes the bets explicit. Each item is something the recommendation rides on; some are routine, some are research-level open questions.

### 8.1 Routine but unverified

(R1) **Sys_c is a category.** Wymore morphisms (component-wise structure-preserving maps) compose and have identities. This is set-theoretic Wymore lore; treated as routine.

(R2) **F : Ctx^op -> Cat is a pseudofunctor.** Once Ctx is fixed and the reindexing functors F(u) are chosen (e.g., as the institution's reduct functors), pseudofunctoriality follows from institution axioms. Routine modulo institutional choice.

(R3) **D_s and D_b are well-defined within Sys_c.** They are defined for any in-fiber Wymore morphism by the existing CSER 2025 / 2026 definitions. Routine.

(R4) **Chain bounds on D_s and D_b hold inside Sys_c.** The existing CSER 2026 bounds carry over verbatim, because they are stated for Wymore morphisms with no reference to context. Routine.

### 8.2 Research-level conjectures

(C1) **There is a metric, or more generally a quantale-valued degradation, that consistently measures the reindexing functor F(u).** Concretely: D_ctx(u; Z) exists as a [0,1] x [0, +inf)-valued function (structural defect + behavioral defect of the reindexing) that:

  (a) is zero when F(u) is an equivalence of fibers;
  (b) is monotone under composition: D_ctx(u_2 . u_1; Z) <= D_ctx(u_1; Z) + D_ctx(u_2; F(u_1) Z) (or a max- or product-bound variant);
  (c) reduces to a standard D_s, D_b pair when F(u) is the trivial reindexing along an identity.

This is the main piece of new mathematics. The fibered category literature has analogous invariants (cleavage defects, descent data) but they are not metric. The Markov-category literature has metric structure on morphisms but no native indexed structure. Combining the two is open.

(C2) **The full degradation of a "transported certificate" decomposes triangularly:**

  D_s(F(u)(h_cert) composed with k) <= [some function of D_s(h_cert), D_s(k), D_ctx(u; Z_ai)]

with an analogous bound for D_b. The shape of the function (additive, max, multiplicative) is the right question to ask once C1 is settled.

(C3) **Engineering signatures form an institution.** That is: the certification artifacts for AI Circuit Breaker (variables, envelopes, adversaries, sensors, claims) admit an institution-theoretic presentation with a satisfaction condition. Goguen-Burstall handle many engineering logics (e.g., the institution of CASL specifications, hidden-algebra institutions for object specification; verify), so this is plausible but unproven for AI Circuit Breaker specifications specifically.

(C4) **Grading the institution by L = [0,1] x [0, +inf) gives D_s and D_b as satisfaction degrees.** Equivalently, the existing CSER 2025 / 2026 numbers are exactly the satisfaction-degrees of "Z_ai matches Z_real" in a suitable graded institution. This is the cleanest possible reconciliation of institution-theoretic and metric viewpoints. It is conjectural; the graded-institution literature (Diaconescu and collaborators, verify) has the machinery but has not, to my knowledge, been applied to engineered-system certification.

(C5) **Polynomial / operadic composition of system + environment respects the fibered structure.** That is: when you compose Z_ai with Z_env in an operadic wiring diagram, the result is again a fibered system, and the fiber over c is the composition done inside Sys_c. This is plausible (and there is Topos Institute work that points in this direction; verify Niu-Spivak 2023, Libkind 2022) but not directly stated for this setup.

### 8.3 Honest dead-end claims

(D1) Contextual categories (Cartmell 1986) do not formalize "operational context" in the sense Paul needs. They formalize syntactic dependency contexts in dependent type theory. Different concept, despite the name. Listed and discarded.

(D2) A pure topos-theoretic answer (each context is a topos, change of context is a geometric morphism) is correct *in principle* but operationally too expensive. The fibration / institution stack gives the same mathematical structure (Mod is a fibered category, indexed categories embed into topoi via the externalization construction) with less re-expression of Wymore content.

(D3) The third-axis attempt (D_s, D_b, D_ctx) as three numbers attached to a single morphism is a category error. D_ctx is not a property of h; it is a property of (u, Z). The fibration frame makes this transparent.

### 8.4 What to do next

A near-term technical agenda, in dependency order, would be:

1. **Fix the institution of engineering specifications I_eng.** Write down Sign, Sen, Mod, |= for the AI Circuit Breaker setting. Verify the satisfaction condition. (Resolves C3.)
2. **Take Ctx = Sign(I_eng), Sys_c = Mod(c), F(u) = Mod(u). Verify Sys_c is a Wymore category in each fiber.** (Resolves R1, R2 in the specific case.)
3. **Define D_ctx(u; Z) precisely.** Start with the simplest candidate: the in-fiber distance between Z and a chosen lift of F(u)(Z) back along a section. Test on toy examples (e.g., reduce an electrical-circuit model from "ambient temperature controlled" to "ambient temperature varying"). (Begins resolving C1.)
4. **Derive a chain bound.** Try the conjectural additive bound first; if it fails on examples, try the max-bound; if that fails, look at log-multiplicative. (Continues C1, C2.)
5. **Grade the institution.** Replace |= with |=_L for L = [0,1] x [0, +inf). Recover D_s and D_b as satisfaction degrees. (Resolves C4.)
6. **Write a Compositionality / ACT short paper.** "Fibered Wymore: a categorical account of certification context."

Each step is finite, falsifiable, and incremental. None of them requires abandoning the Wymore vocabulary, and each of them produces a result that the existing CSER 2025 / 2026 readership can read.

---

## References (with verify flags)

- Awodey, S. *Category Theory*. Oxford Logic Guides 49, Oxford University Press, 2nd ed., 2010.
- Benabou, J. "Fibered categories and the foundations of naive category theory." *Journal of Symbolic Logic* 50(1), 1985. (verify volume / page)
- Cartmell, J. "Generalised algebraic theories and contextual categories." *Annals of Pure and Applied Logic* 32, 1986. (verify)
- Diaconescu, R. "Institution-independent ultraproducts." *Fundamenta Informaticae* 55(3-4), 2003. Also Diaconescu, R., *Institution-independent Model Theory*, Birkhauser, 2008. (verify; this is the main institution-theoretic monograph)
- Fritz, T. "A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics." *Advances in Mathematics* 370, 2020.
- Fong, B. and Spivak, D. I. *Seven Sketches in Compositionality: An Invitation to Applied Category Theory*. Cambridge University Press, 2019. (verify publisher; also available on arXiv as 1803.05316)
- Goguen, J. A. and Burstall, R. M. "Institutions: abstract model theory for specification and programming." *Journal of the ACM* 39(1), 95-146, 1992.
- Grothendieck, A. "Categories fibrees et descente." Expose VI of SGA 1, 1960-61. (foundational, verify edition)
- Mac Lane, S. *Categories for the Working Mathematician*. 2nd ed., Springer Graduate Texts in Mathematics 5, 1998.
- Niu, N. and Spivak, D. I. *Polynomial Functors: A Mathematical Theory of Interaction*. (book in preparation / draft on arXiv, verify 2023 status)
- Riehl, E. *Category Theory in Context*. Dover, 2016.
- Spivak, D. I. "The operad of wiring diagrams: formalizing a graphical language for databases, recursion, and plug-and-play circuits." arXiv:1305.0297, 2013. (verify)
- Spivak, D. I. and Schultz, P. and Vagner, D. "Algebras of open dynamical systems on the operad of wiring diagrams." *Theory and Applications of Categories* 31, 2016. (verify volume)
- Wymore, A. W. *Model-Based Systems Engineering*. CRC Press, 1993.
- Wach, P. F. et al. CSER 2025 paper on degree of homomorphism (citation per Paul's records).
- Wach, P. F. et al. CSER 2026 paper on two-axis isomorphic degradation (citation per Paul's records).

Items marked (verify) need bibliographic checking before publication. The Goguen-Burstall 1992 *JACM* citation is canonical and high confidence.

---

*End of categorical synthesis brief.*

# Wymore-Native Treatment of "Context" as a Systems-Theoretic Construct

**Purpose.** Define "context" as a first-class construct *inside* the Wymorian 5-tuple formalism, rather than as a third coordinate appended to the (D_s, D_b) morphism-distance pair. The construct must explain the failure mode in which an AI system Z_ai is certified against a reference Z_real(cert) with low D_s and low D_b, then deployed against a different operational reality Z_real_op against which no morphism was asserted.

**Date.** 2026-05-20.

**Author lineage acknowledged.**
- Wymore (1993), *Model-Based Systems Engineering*, CRC Press. Z = (S, I, O, omega, beta); morphism h = (h_S, h_I, h_O) of structure-preserving surjections that commute with omega and beta.
- Wach, Krometis, Sonanis, Verma, Panchal, Freeman, Beling (2022), *INSIGHT* 25(4):65-70. Pairing Bayesian methods with systems theory for T&E of learning-based systems.
- Wach, Zeigler, Salado (2021), *Applied Sciences* (verify exact title). DEVS / Wymore reconciliation.
- Wach, Iyer, Shanmugam, Curran, Ashok (2025), CSER 2025. Degree of homomorphism sigma = average reciprocal mapping cardinality across states.
- Wach, Sandmann, Iyer (2026), CSER 2026 (forthcoming). Two-axis isomorphic degradation D_s = 1 - sigma (structural), D_b = max_t |R_ai(s_ai(t)) - R_real(s_real(t))| (behavioral). Composition bounds along morphism chains.
- AI Circuit Breaker Design Spec v4, this repo, `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Design_Spec_v4.md`. Deployment instrument.
- Prior failed attempt to formalize context as a third coordinate D_r on the morphism distance metric: `Papers/AI_Circuit_Breaker/reviews/Dr_construct_analysis_v0.1.md`. The failure was diagnosed as a category error; context is not a property of a single morphism, it is a property of the deployment relative to the certified envelope.

**Scope.** Wymore only. DEVS / experimental-frame / Zeigler material is being handled by a parallel agent and is not pursued here, except for one brief location note in Section 5 where the boundary becomes load-bearing. Statistical, ML, and formal-methods reformulations are out of scope; they were the path the prior attempt took, and they obscured rather than clarified the systems-theoretic status of the construct.

---

## 1. Statement of the construct problem

### 1.1 What "context" is being asked to do

Wymore tuples are modeling commitments. The five sets and two functions are not given by nature; they are chosen by the modeler when the system boundary is drawn. The phrase "scope of validity" attached to a morphism h : Z_1 -> Z_2 is, on careful reading, a statement about three different things at once:

1. The reachable subset Q_2 subset of S_2 over which the commutativity conditions of h were actually checked.
2. The input subset I_2' subset of I_2 over which Q_2 was reached.
3. The implicit modeling commitment that *no other inputs or states are relevant*, because anything else was either treated as fixed or treated as out of scope.

The third commitment is exactly where "context" lives in the formalism. It is the commitment about what was admitted into the tuple and, by exclusion, what was treated as part of the unmodeled background. When an AI is deployed against a different operational reality, the failure is almost never that the AI "behaves badly inside its tuple." The failure is that the deployment violates the modeling commitment about what the tuple included. The tuple silently became the wrong tuple, and the instrument cannot tell because the instrument measures inside the tuple.

So the question is: what is the Wymore-native object that represents this modeling commitment, and what is the Wymore-native quantity that, when it changes, says "the tuple has become the wrong tuple"?

### 1.2 Why a third metric coordinate failed

Concretely, the failed move (D_r as a third axis on (D_s, D_b)) tried to make context a property of the morphism h. It is not. The morphism h, considered as a mathematical object, is fully specified once h_S, h_I, h_O are given on their declared domains and the commutativity conditions are checked. The morphism does not "know" whether it is being applied to a different real system; it only knows whether its commutativity conditions hold on the declared domains. "Out of context" therefore cannot show up as a property of h. It must show up as a change in *which* h is even at issue.

This is the structural reason the third-axis framing collapses. It is also a hint about where the construct actually lives. Context lives one level up from h, at the level where h is selected and asserted.

### 1.3 The three Wymore-native locations worth pursuing

Of the eight candidate angles proposed in the briefing, three survive a serious test of native-ness within Wymore's set-theoretic framework. The other five reduce to special cases of these three, or import machinery (probability, categories with limits, equivalence-class quotients) that Wymore did not use natively.

- **Formulation A: Context as the morphism domain.** A Wymore homomorphism is asserted on a reachable subset Q_2 of S_2, under a chosen subset I_2 of inputs. Context is the specification of this assertion domain. This is angle 6 in the briefing.
- **Formulation B: Context as a parameter that indexes a family of Wymore tuples.** The certified system is one element Z_real(c_cert) of a family { Z_real(c) | c in C }. Context is the carrier set C, and the deployment question is which c is in force. This is angle 3.
- **Formulation C: Context as the coupling specification to an environment system Z_env.** The AI does not face Z_real in isolation; it faces a coupled system Z_ai parallel-coupled to Z_env. Context is the specification of Z_env and of the coupling. This is angle 2.

Angles 1 (context as a subset I_ctx of I), 4 (context as the implicit boundary choice), 5 (context as an equivalence relation on tuples), 7 (Zeigler experimental frame), and 8 (context via the kernel of the morphism) are addressed in Sections 4 and 5. Each reduces to A, B, or C, but the reduction is illuminating and each contributes a constraint on the recommendation.

---

## 2. Formulation A — Context as the morphism domain

### 2.1 Formal type signature within the 5-tuple

A Wymore homomorphism h : Z_1 -> Z_2 is asserted *with respect to* (per Section 2.1 of the CSER 2026 background):

- I_2' subset of I_2, a chosen input set,
- Q_2 subset of S_2, the set of states reachable from some s_0 in S_2 under I_2',
- O_2' subset of O_2, the outputs realized on Q_2 under I_2'.

The surjections h_S, h_I, h_O are defined on these restricted sets, and the commutativity conditions (iv) and (v) are checked over (Q_2, I_2'). They are not asserted anywhere else.

The morphism domain is therefore the triple

    Dom(h) := (Q_2, I_2', O_2')

with the standing requirement Q_2 = Reach(S_2, I_2', s_0) for some specified initial state s_0 (or set of admissible initial states).

**Definition A1 (Context).** Context is Dom(h). Equivalently, context is the specification of the reachable region of the target tuple over which the morphism is *asserted*.

This is not a metric quantity. It is a set-theoretic object. It has the type signature of a triple of sets, and the natural operations on it are set-theoretic (inclusion, intersection, complement) rather than metric (distance, ball, ratio).

### 2.2 Where context-failure shows up

With Definition A1, the "wrong context" deployment failure has an exact set-theoretic signature.

Let h_cert : Z_ai -> Z_real(cert) be the certified morphism, with Dom(h_cert) = (Q_cert, I_cert', O_cert'). At deployment, the AI receives inputs from the operational environment that, after running through the world, exercise some operational reachable region Q_op subset of S_real. The deployment violates the modeling commitment exactly when:

    Q_op intersect Q_cert = Q_cert        (live behavior is contained in the certified region) — IN CONTEXT.
    Q_op intersect Q_cert subsetneq Q_op  (live behavior exceeds the certified region)         — OUT OF CONTEXT.
    Q_op intersect Q_cert = empty         (live behavior misses the certified region entirely) — OUT OF DOMAIN.

The third case is the pediatric ECG example from the prior D_r construct analysis: the operational reachable region of the pediatric cardiac signal space does not overlap (in the relevant ontological semantics) with the adult cardiac signal space over which h_cert was checked. The morphism h_cert is silent. The conditions (iv) and (v) were never asserted on any (s, i) in Q_op. The numbers D_s(h_cert) and D_b(h_cert) computed from operational data are not "high"; they are *undefined*, because they would require the commutativity conditions to mean something on a region of S_real where they were not asserted.

This is the operative point and the formal payoff. Context-failure is *non-assertion*, not bad assertion.

### 2.3 Connection to D_s and D_b

D_s and D_b are computed *over* Dom(h). The CSER 2025 sigma is an average reciprocal mapping cardinality across elements of Q_2. The CSER 2026 D_b is a max over t of output-distance under the variable mapping, where t ranges over trajectories *in Dom(h)*. Both metrics are defined relative to the morphism domain.

This gives a clean relationship: D_s and D_b are quantitative *interior* measures of morphism quality on Dom(h). Context, in Formulation A, is the *boundary* specification of where those interior measures are even well-defined. The two are not on the same axis. They are not even on the same kind of object. D_s : Morphisms -> [0,1] is a real-valued functional on the space of morphisms (with declared domain). Dom : Morphisms -> 2^(S x I x O) is a set-valued specification.

**Implication.** The instrument (D_s, D_b) does *not* extend naturally to handle context. The extension would require either pretending the domain is fixed (which is the certified-frame blindness Paul's hypothesis names), or making D_s and D_b functions of Dom(h) (which collapses them into different objects for each domain choice). Neither is a true extension. What is needed instead is a *guard* on the instrument: a separately reported determination of whether Dom(h_cert) is the right domain for the live deployment. The two quantities (interior morphism quality, exterior domain validity) sit in different syntactic positions in the trust verdict and should not be conflated.

### 2.4 Composition behavior along morphism chains

Chain composition is where Formulation A becomes especially well-behaved. Consider the chain

    Z_0  --h_1-->  Z_1  --h_2-->  ...  --h_n-->  Z_n.

Each h_i has its own assertion domain Dom(h_i) = (Q_i, I_i', O_i'), and the chain composition h_n compose ... compose h_1 is asserted on

    Dom(h_n compose ... compose h_1) = (Q_0, I_0', O_0')

with the standing requirement that for every i, the image of Dom(h_{i-1}) under h_{i-1} lies inside Dom(h_i). Formally:

    h_i(Q_i) subset of Q_{i+1},  for all i = 0, ..., n-1.

If this inclusion fails at any link, the composed morphism is asserted *only* on the largest pullback subset where every link's assertion holds. This is exactly the kind of restriction that happens in Wymore-style verification model composition.

**Composition rule for context (Formulation A).**

    Dom(h_n compose ... compose h_1)  =  the largest (Q_0, I_0', O_0') such that
                                          h_i(Q_i') subset of Q_{i+1}'  for each i,
                                          where Q_i' is the induced restriction at link i.

In plain words: composing morphisms shrinks the context. The composed system is valid only where every link is valid. If any link's assertion domain is too narrow to receive the image of the preceding link, the entire chain's assertion domain collapses to the intersection.

This is structurally identical to the way Wymore's verification-model composition operates, and it parallels the chain-bound behavior of D_s (max-of-D_s over links) and D_b (sum-of-D_b under 1-Lipschitz). The metric chain-bounds and the set-theoretic context-shrinkage are *complementary* facts about the same chain. Neither subsumes the other.

### 2.5 What "out of context" means in Formulation A

"Out of context" is a precise set-theoretic event. It is:

    There exists a live trajectory (s_op(t), i_op(t)) such that for some t,
    (s_op(t), i_op(t))  not in  Q_cert x I_cert'.

This is a Boolean condition over trajectories, not a degenerate value of a metric. It does *not* show as "high D_s" or "high D_b." It shows as the live trajectory leaving Q_cert. The instrument that detects this is a domain-membership predicate, evaluated on the live trajectory, against the certified Dom(h_cert) specification.

Formulation A therefore says: "out of context" is *not* in the same syntactic category as a degraded morphism. It is in the syntactic category of a precondition violation. The two are not comparable on a single axis because they are not the same kind of fact.

### 2.6 Strongest objection and response

**Strongest objection.** "If context is just Dom(h), then context is trivial. Every morphism comes with a declared domain by definition. You have not added anything; you have just renamed the standard restriction of a homomorphism."

**Response.** This is correct as a statement about the formalism, and that is precisely why Formulation A is the most native to Wymore. The construct is not new; the *recognition* of where context-failure already lives in Wymore is new. The reason it has felt like a missing construct is that operational practice has been treating Dom(h) as an implicit assumption rather than a declared object. The contribution is to make Dom(h) a *first-class declared artifact of the certification*, on equal footing with Z_ai, Z_real, and h itself. Once it is declared, "out of context" becomes detectable; until it is declared, "out of context" is by definition invisible because there is no boundary against which to test. The work being done by the construct is the work of moving a tacit modeling assumption into an explicit certification artifact. This is not trivial in any practical sense; it is the *whole* of the certified-vs-operational gap.

A secondary objection might be that "Dom(h) is too coarse, because operational reality varies continuously and the certified region is a discrete set-theoretic object." This is true but it is also true of every Wymore formalization. The remedy, when continuity matters, is to refine Q_cert (declare more states), not to abandon the set-theoretic framing. Wymore is set-theoretic by construction; if the certification needs to capture continuous variation, the state set must be made finer. This is the same trade-off the framework has always carried.

---

## 3. Formulation B — Context as a parameter that indexes a family of Wymore tuples

### 3.1 Formal type signature

Let C be a set, the *context space*. For each c in C, there is a Wymore tuple

    Z_real(c) = (S_real(c), I_real(c), O_real(c), N_real(c), R_real(c)).

The family { Z_real(c) | c in C } is the *contextual family of reference systems*. The certified system is the single element Z_real(c_cert). The deployment is in force at some c = c_op in C, which may or may not equal c_cert.

**Definition B1 (Context).** Context is an element c of C. The context *space* C is the carrier set of admissible contextual configurations under which the system is to be reasoned about. C is part of the modeling commitment, declared alongside the tuple itself.

Equivalently and more usefully, the family Z_real : C -> Wymore is a function from C into the universe of Wymore tuples. Each fiber Z_real(c) is a separate tuple; the fibers are not assumed to share state sets or input sets, although in any well-posed family they will share enough type structure that morphisms across fibers can be considered.

### 3.2 Where context-failure shows up

In Formulation B, the certified morphism is h_cert : Z_ai -> Z_real(c_cert). At deployment, the world is governed by Z_real(c_op). The deployment is in-context exactly when c_op = c_cert. It is out-of-context when c_op =/= c_cert, and the *degree* to which it is out of context is measured by how different the two fibers are as Wymore tuples.

The natural quantity here is a *morphism distance between fibers*. Specifically, ask: is there a morphism g : Z_real(c_cert) -> Z_real(c_op)? If yes, what is its (D_s, D_b)? This is exactly the F3 move from the prior D_r construct analysis: treat the deployment as a two-stage chain

    Z_ai  --h_cert-->  Z_real(c_cert)  --g-->  Z_real(c_op),

and measure g in the same (D_s, D_b) algebra as h_cert.

But there is a sharper move available in Formulation B that the prior analysis did not draw out. Define a quantity native to the family:

    delta(c_cert, c_op) := inf over morphisms g : Z_real(c_cert) -> Z_real(c_op) of (1 - sigma(g))
                           if such a g exists, else infinity.

This is the *contextual displacement* from c_cert to c_op. It quantifies how much abstraction loss is required to map the certified reality into the operational reality, where "no g exists" (delta = infinity) means the two fibers are not even comparable as Wymore tuples — there is no surjective structure-preserving map between them. The contextual displacement is, in this sense, the "distance" that the failed D_r construct was groping toward, except that it lives on the *family C* (or equivalently on the space of Wymore tuples), not on the space of morphisms out of Z_ai.

### 3.3 Connection to D_s and D_b

The connection is direct and clarifying. delta(c_cert, c_op) *is* a D_s value, but on a different morphism than h_cert. It is D_s(g), where g is the best available morphism between the certified fiber and the operational fiber. By analogy there is a delta_b(c_cert, c_op) defined as the corresponding D_b on g.

So Formulation B does not invent a new metric type. It says: the (D_s, D_b) machinery already works for the context question, provided we are willing to apply it to a *different* morphism — the inter-fiber morphism g, not the AI-to-reality morphism h. The "third axis" was not a new dimension; it was the same two dimensions applied to a second arrow in a longer diagram.

This is the F3 finding of the prior construct analysis, restated in Wymore-native terms. What Formulation B adds is the explicit observation that g lives in a *family* of reference systems, and that the family C is itself the modeling artifact that needs to be declared. The certification artifact, under Formulation B, is not just (Z_ai, h_cert, Z_real(c_cert)) but the full quadruple

    (Z_ai, h_cert, Z_real(c_cert), C),

where C is the declared context space within which c_op is permitted to vary.

### 3.4 Composition behavior along morphism chains

Composition along a chain in Formulation B is the composition of fiber-to-fiber maps. If a chain of contextual displacements is

    Z_real(c_0)  --g_1-->  Z_real(c_1)  --g_2-->  ...  --g_k-->  Z_real(c_k),

then the chain-bound theorem of CSER 2026 applies link-by-link:

    D_s(g_k compose ... compose g_1)  =  1 - prod over i of sigma(g_i)  in the worst case
                                        (or the corresponding min-sigma bound),
    D_b(g_k compose ... compose g_1)  <=  sum over i of D_b(g_i)  under 1-Lipschitz at each link.

This is the *same* chain-bound algebra as for the AI-to-reality morphism. Composition over the contextual family is the natural extension of composition over morphisms.

A subtlety: the chain g_1, ..., g_k makes sense only if the fibers are well-connected by morphisms. In some families this is guaranteed (e.g., families indexed by a refinement order on state-set partitions). In other families it is not (e.g., a family where some fibers have additional state classes that have no analog in others). When no g exists between two fibers, the corresponding delta is infinity, and the chain is broken at that link. Formulation B therefore *predicts* the existence of "discontinuities" in the context space at which the chain becomes undefined. These discontinuities are the contextual analog of the "no certified morphism into Z_real_op" condition in the deployment scenario.

### 3.5 What "out of context" means in Formulation B

Out of context, in Formulation B, has degrees. It is no longer a Boolean precondition violation as in Formulation A. It is a real-valued displacement delta(c_cert, c_op) in [0, infinity], with infinity reserved for the case where the fibers are not even morphism-comparable.

This is good news for Layer 3 statistical-process-control (SPC) machinery in the AI Circuit Breaker, because a continuous quantity admits control limits, drift detection, and graded escalation. It is bad news for the simplicity of the verdict, because the operator now has to interpret a "context displacement" number that has the same algebraic type as D_s but a different operational meaning. It is also bad news for the certification effort, because delta(c_cert, c_op) requires that c_op be *recognized* and *registered* in the family C before the displacement can be computed. If c_op is a contextual configuration outside C, then C itself is the wrong context space, and we are back to a non-assertion failure (Formulation A) on the family declaration rather than on the morphism domain.

The two formulations are therefore stacked: Formulation A asks whether the operational situation is inside the declared morphism domain; Formulation B asks how far the operational situation is from the certified context, *given* it is inside the declared family. Both are needed to give a complete account.

### 3.6 Strongest objection and response

**Strongest objection.** "Formulation B requires that the certifier declare a context space C and that the deployment monitor be able to identify c_op in C at runtime. Neither is realistic. The whole point of the wrong-context failure mode is that the operator does not know which c is in force; they think they are in c_cert."

**Response.** This is the correct critique and it points to the deepest difficulty of the construct. The response has three parts.

First, the objection conflates *declaration* of C with *identification* of c_op. The declaration of C is a certification-time activity, the same kind of activity as the declaration of Z_real or h. The certifier states: "this AI is certified for contexts in C; outside C, the morphism is non-asserted." This is hard but tractable, and indeed it is already common practice in safety-critical engineering (the "operational design domain" of automotive autonomy, the "indications for use" of medical devices, the "envelope" of an aviation system). Formulation B just gives this practice a Wymore-native formalization.

Second, the *identification* of c_op at runtime is genuinely hard. The construct does not claim it is easy. What the construct claims is that the *failure mode of misidentification* now has a precise formal name (the deployment is at some c_op which the monitor has incorrectly inferred to be c_cert) and a precise formal consequence (D_s and D_b computed against Z_real(c_cert) are not even applicable). This is more than the current framework provides; the current framework has no language for the mis-identification at all.

Third, the operational difficulty of identifying c_op is exactly the work that a deployed monitor must do, regardless of whether the formal framework names it. Naming it does not make it harder; it makes it nameable.

A second-order objection: Formulation B can degenerate if C is too rich. If C is, say, the entire space of Wymore tuples, then "context" loses content, because every operational situation is some c in C. The discipline that gives Formulation B content is the requirement that C be declared and *small*. The smaller C is, the stronger the certification claim. The larger C is, the weaker. This is the same trade-off that governs every applicability-domain declaration in engineering practice.

---

## 4. Formulation C — Context as the coupling specification to an environment system

### 4.1 Formal type signature

Wymore systems compose via *coupling specifications*. A coupling between two tuples Z and Z' is a specification of which outputs of one are wired to which inputs of the other, possibly with a transformation. The result is a single composite tuple Z || Z' whose state set is (a subset of) the product, whose input set is the free inputs of the composite, and whose output set is the free outputs.

In Formulation C, the AI does not face Z_real directly. It faces a composite

    Z_ai  ||  Z_env

where Z_env is the environment system, and the composition is via a coupling specification kappa : O_env -> I_ai (and possibly the reverse if the AI actuates the environment). The "real" thing the AI is being morphic to is then not Z_real in isolation but the composite Z_real_full = Z_real || Z_env, where Z_env represents the operational environment that the AI's sensors and actuators interact with.

**Definition C1 (Context).** Context is the pair (Z_env, kappa), where Z_env is the environment system and kappa is the coupling specification between Z_env and Z_ai (and possibly Z_real). Context, in this reading, is a *system*, not a parameter and not a domain. It is the rest of the world, modeled as a Wymore tuple in its own right, plus the wiring diagram that connects it to the AI.

### 4.2 Where context-failure shows up

In Formulation C, the deployment failure is not a property of the morphism h : Z_ai -> Z_real at all. It is a property of the *environment*: the certified composite was Z_ai || Z_env(cert), but the operational composite is Z_ai || Z_env(op), and Z_env(op) =/= Z_env(cert). The AI is the same; the morphism h is the same; only the environment system has changed.

This is, in fact, the most physically faithful description of the wrong-context failure mode. The pediatric ECG example becomes: the AI is unchanged; the morphism between the AI and adult cardiac physiology is unchanged; but the environment system has changed from adult cardiac physiology to pediatric cardiac physiology. The composite (AI || pediatric environment) was never certified, even though (AI || adult environment) was.

### 4.3 Connection to D_s and D_b

D_s and D_b in Formulation C apply to morphisms *between composites*, not to morphisms between AI-only tuples. If the AI's internal model is also a composite Z_ai = Z_ai_core || Z_env(ai_estimate), where Z_env(ai_estimate) is the AI's internal model of the environment, then the certified morphism is

    h : Z_ai_core || Z_env(ai_estimate)  -->  Z_real_core || Z_env(real_cert)

and D_s(h), D_b(h) measure how good this composite morphism is. The deployment failure shows up as: the operational reality is now Z_real_core || Z_env(real_op), and the certified h was never evaluated against this composite. D_s and D_b computed against the certified composite are non-applicable to the operational composite.

This is closely related to Formulation B, with a difference of presentation. Formulation B parametrizes the family Z_real(c) abstractly. Formulation C makes the parameter concrete: the parameter c is the environment system Z_env, and the family is generated by varying Z_env. This is the constructive content of Formulation B in the case where the contextual variation is environmental.

### 4.4 Composition behavior along morphism chains

Composition in Formulation C has two flavors, which need to be carefully distinguished.

*Sequential composition* (along the morphism chain) behaves exactly as in Formulations A and B. If the chain is

    Z_ai || Z_env  --h_1-->  Z_1' || Z_env_1'  --h_2-->  ...

then the chain-bound for D_s and D_b applies link-by-link on the composite morphisms, and the assertion domain shrinks to the intersection of declared domains.

*Parallel composition* (across the coupling) is the new ingredient. The morphism h between composites has two sub-morphisms

    h_core : Z_ai_core -> Z_real_core
    h_env  : Z_env(ai_estimate) -> Z_env(real_cert)

The composite morphism's D_s and D_b are governed by both sub-morphisms and by the coupling. A degraded h_env (the AI's environment model is wrong) can produce low D_s and low D_b on the composite *even though* the operational environment is not the certified environment, because the AI's internal environment estimate may compensate for the deviation in ways that the composite morphism does not detect. This is the formal reason why "low D_s, low D_b" can coexist with "wrong context": the composite is internally consistent, but the composite has the wrong environment subsystem.

This decomposition is sharper than the Formulation B view. It says: the wrong-context failure is specifically a failure of the *environment sub-morphism* h_env, not of the *core sub-morphism* h_core. The instrument that measures only the composite cannot distinguish the two. An instrument that measures h_env separately can.

### 4.5 What "out of context" means in Formulation C

Out of context, in Formulation C, means: the operational Z_env is not the certified Z_env, i.e., there is no morphism g_env : Z_env(real_cert) -> Z_env(real_op) of acceptable quality, or no g_env exists at all. The construct is the same as the inter-fiber morphism delta of Formulation B, but specialized to environment systems.

The advantage of Formulation C over Formulation B is that the *physical referent* is concrete. The environment system Z_env is a thing one can model, instrument, and reason about as a Wymore tuple in its own right. The disadvantage is that it requires the modeler to commit to a particular decomposition of Z_real into a core plus an environment, which is itself a modeling commitment and not always natural.

### 4.6 Strongest objection and response

**Strongest objection.** "Formulation C just relocates the wrong-context problem from 'morphism domain' to 'environment system identification.' You still have to know which Z_env you are in, and the wrong-context failure is exactly that you do not know. No formal gain over Formulation B."

**Response.** The gain is decompositional, not eliminative. Formulation C says that the wrong-context failure has a *specific localization* inside the composite morphism: it is a failure of h_env, not of h_core. This decomposition is operationally useful because it suggests that an environment-monitoring subsystem (a separate Wymore tuple tracking Z_env(real_op) directly from environmental telemetry, independently of the AI's internal estimate) is the right architectural response. The construct earns its keep by *naming the right subsystem* in the response.

A secondary objection: Wymore's coupling formalism is not as widely used as the single-tuple formalism, and committing to it in a deployment-instrument framework adds notational overhead. This is true. The response is that the AI Circuit Breaker is, in any case, a multi-system instrument (it observes Z_ai, Z_real, and h simultaneously through different sensors), and the coupling formalism gives the cleanest account of how these systems are wired together at runtime.

---

## 5. Treatment of the remaining angles

The five angles not chosen as primary formulations either reduce to A, B, or C, or import non-Wymore machinery. Brief notes:

### 5.1 Angle 1: Context as a fragment I_ctx of the input set I

This is a special case of Formulation A with the additional commitment that I_ctx is a designated subset of I that the system reads but does not control. The treatment is identical to Formulation A's restriction on Dom(h) = (Q_2, I_2', O_2'), with the additional refinement that the input set is partitioned into controlled inputs and contextual inputs. The partition does not change the formal structure of the morphism domain; it changes the operational interpretation. Worth noting that the controlled / contextual partition of I is a separate modeling commitment that one might make in addition to A, but it is not the construct of context itself; it is a refinement of how I is read.

### 5.2 Angle 4: Context as the implicit boundary choice

This is the *informal* version of Formulation A. The "modeler's choice of boundary" is exactly what gets declared when Dom(h) is declared. Formulation A makes this implicit choice explicit. Without Formulation A, this angle is merely a slogan ("everything is a boundary choice") with no formal teeth. With Formulation A, the boundary choice has a name and a type. Angle 4 reduces to A.

### 5.3 Angle 5: Context as an equivalence relation on Wymore tuples

The construct here would be: two situations are "same context" iff their Wymore tuples are isomorphic or homomorphic to some degree. This collapses the family-indexing of Formulation B into an equivalence-class quotient. It is mathematically interesting but Wymore did not natively use equivalence-class quotients on tuples; he used morphisms between tuples. The morphism-based formulation (B) carries strictly more information than the equivalence-class formulation, because morphisms remember *direction* and *quality of mapping*, while equivalence classes do not. Angle 5 reduces to B with information loss.

### 5.4 Angle 7: Zeigler experimental frame

Zeigler's experimental frame is a tuple (generator, acceptor, transducer) that defines the conditions under which a model is to be exercised. It is closely analogous to Wymore's morphism domain (Formulation A) but carries additional structure (the explicit separation of input-generating, output-accepting, and output-transducing subsystems). In Zeigler's DEVS framework the experimental frame is itself a system that couples to the model under test, which is closer to Formulation C. The reconciliation of Wymore and DEVS in Wach, Zeigler, Salado (2021, Applied Sciences, verify exact title) establishes that Wymore's coupling formalism can express the DEVS experimental frame. A parallel agent is treating this angle in depth; this memo restricts itself to noting that the experimental-frame view is consistent with Formulations A and C and supplies additional structure on the input-generating and output-accepting subsystems.

### 5.5 Angle 8: Context via the kernel / image of the morphism

The kernel of a Wymore homomorphism h_S : S_2 -> S_1 is the equivalence relation on S_2 induced by h_S, namely { (x, y) in S_2 x S_2 | h_S(x) = h_S(y) }. The kernel captures the "lumping" that the abstraction does. The image is h_S(Q_2) subset of S_1, the set of states in the abstract model that are actually attained by the morphism.

Context, via the kernel, would be: the equivalence classes of S_2 that the abstraction lumps together, weighted by which of those classes turn out to matter operationally. This is operationally interesting because it gives a precise formal name to "the AI's model lumps things together that operationally are not the same" — which is one common variant of the wrong-context failure. But this is a *refinement* of D_s (which is already an average over the cardinalities of the kernel equivalence classes) rather than a separate construct. Angle 8 reduces to a finer-grained reading of D_s, not to an independent context construct.

---

## 6. Comparative table

| Aspect | Formulation A: Morphism domain Dom(h) | Formulation B: Parameter family Z_real(c) | Formulation C: Coupling to Z_env |
|---|---|---|---|
| Type signature | (Q_2, I_2', O_2') subset of S_2 x I_2 x O_2 | c element of C; family map Z_real : C -> Wymore | Pair (Z_env, kappa) where kappa is a coupling spec |
| Kind of object | Set-theoretic (subsets of tuple sets) | Element of a carrier set; family-of-tuples | Wymore tuple plus wiring diagram |
| Native to Wymore? | Yes; already implicit in the homomorphism definition (CSER 2026 background Section 2.1) | Partially; Wymore did not formalize parametric families explicitly, but morphisms across tuples generalize naturally | Yes; coupling specifications are core Wymore machinery |
| Connection to D_s | D_s defined *over* Dom(h); Dom(h) is a precondition on D_s applicability | delta_s(c_cert, c_op) is a D_s applied to inter-fiber morphism g | D_s decomposes into D_s(h_core) + contribution from D_s(h_env) on the composite |
| Connection to D_b | Same: D_b defined over Dom(h) | delta_b is D_b applied to g | D_b decomposes similarly |
| Composition behavior | Chain composition shrinks Dom to intersection; complements (D_s, D_b) chain-bound | Chain composition over fibers; same (D_s, D_b) chain algebra applied to g chain | Sequential as in A; parallel composition adds environment sub-morphism |
| "Out of context" semantics | Boolean precondition violation: trajectory leaves Q_cert | Continuous displacement delta in [0, infinity]; infinity = no morphism exists | Failure of h_env sub-morphism within composite |
| What is declared at certification | Dom(h_cert) = (Q_cert, I_cert', O_cert') | Family Z_real : C -> Wymore and the certified c_cert | Z_env(cert) and the coupling kappa |
| Practical instrument | Domain-membership predicate on live trajectory | Identification + comparison of c_op against c_cert in C | Environment-monitoring subsystem that tracks Z_env(real_op) |
| Strongest weakness | Continuous variation requires refining Q at modeling time; might feel renaming-only | Identification of c_op at runtime is genuinely hard | Requires committing to a core/environment decomposition; coupling formalism less familiar |
| Subsumes which other angles | 1 (I_ctx fragment), 4 (boundary choice), most of 8 (kernel refinement) | 5 (equivalence class with information loss); generalized by Wymore tuple morphisms | 7 (Zeigler experimental frame) consistent with C; supplied by coupling |

---

## 7. Strongest objection per formulation, consolidated

These are pulled from each formulation's Section X.6 for side-by-side comparison.

| Formulation | Strongest objection | Substance of the response |
|---|---|---|
| A | "Dom(h) is trivially part of the formalism. Naming it adds nothing." | Naming moves a tacit modeling assumption into an explicit certification artifact. That move *is* the certified-vs-operational gap, even if the underlying mathematics was already present. Operational practice was treating Dom(h) as implicit; the construct demands explicit declaration. |
| B | "Declaring C and identifying c_op at runtime is unrealistic." | Declaration of C is a tractable certification activity (standard practice under different names). Identification of c_op is genuinely hard, but the construct *names* the failure mode of misidentification and gives it a formal consequence; the current framework lacks even that. |
| C | "Just relocates the problem from morphism domain to environment identification, no formal gain." | The gain is decompositional: failure is localized to h_env, not to h_core. This is operationally useful because it suggests a separate environment-monitoring subsystem, with a Wymore tuple of its own. The construct earns its keep by naming the right subsystem of the response. |

A meta-objection applies to all three: Wymore's framework was developed before deployment-monitoring became a research topic, and retrofitting "context" onto the 5-tuple may force the formalism beyond what it was designed to carry. Response: Wymore's homomorphism definition (with its explicit Q_2, I_2' restrictions) and his coupling formalism already supply the machinery. The retrofit is more an act of recovery than of invention. The construct of context is *already there*, asserted implicitly every time a morphism is declared, and the work is to surface it as a first-class artifact.

---

## 8. Recommendation: which formulation is most native to Wymore

The recommendation has two parts, because the question "most native" admits two readings.

### 8.1 If "most native" means "uses the least machinery beyond the standard 5-tuple definition"

The answer is **Formulation A** (context as the morphism domain Dom(h)).

Reasoning. Wymore's definition of homomorphism already includes the restriction to (Q_2, I_2', O_2'). The construct of context in Formulation A is *literally* this restriction, promoted from an implicit definitional clause to an explicit certification artifact. No new machinery is introduced. No new operations on tuples are required. The chain-bound behavior of D_s and D_b is preserved unchanged, and Dom(h) provides a complementary set-theoretic chain-shrinkage rule that does not interfere with the metric chain-bounds. The instrument required to detect "out of context" is a domain-membership predicate, which is a standard set-theoretic test against the declared Dom(h_cert).

This is also the formulation that is most defensible against the "you have not added anything" objection, because the response to that objection ("we have made a previously tacit construct first-class") is exactly correct, and the work of making something first-class is real intellectual work even when the underlying mathematics was already present.

### 8.2 If "most native" means "captures the deployment failure mode with the strongest connection to existing (D_s, D_b) machinery"

The answer is **Formulation B** (context as a parameter indexing a family of Wymore tuples).

Reasoning. Formulation B preserves the intuition that "context" composes with D_s and D_b, by recasting the third quantity as the same two-axis pair (D_s, D_b) applied to an inter-fiber morphism g : Z_real(c_cert) -> Z_real(c_op). This is the F3 finding of the prior D_r construct analysis, restated cleanly. The chain-bound algebra extends to the second link in the chain without modification. The instrument required is the same (D_s, D_b) instrument, applied to a second morphism. This is the formulation that gives the failed D_r-as-third-axis intuition its correct mathematical home, by re-typing the third quantity from "third coordinate of one morphism's distance" to "first two coordinates of a second morphism's distance."

### 8.3 Composite recommendation

The two readings are not in tension; they are complementary, and the strongest treatment uses both.

- **Formulation A is the foundation.** It declares what was previously tacit. Without A, B cannot get off the ground, because the family C is a refinement of the certification artifact that A insists must be declared.
- **Formulation B is the extension.** Once Dom(h_cert) is declared, the next natural question is "what other Dom's are nearby in some family, and how far away are they?" Formulation B answers this with the same (D_s, D_b) machinery applied to inter-fiber morphisms.
- **Formulation C is the constructive specialization** of B for the case where the context variation is environmental. It tells the practitioner *what concrete subsystem* to model and monitor (the environment, as a Wymore tuple in its own right), and it localizes the wrong-context failure to a specific sub-morphism (h_env).

If forced to a single answer for "Wymore-native," it is A. If allowed to declare a layered construct, the recommendation is A-as-foundation, B-as-extension, C-as-physical-specialization.

This composite picture says: context, in Wymore's tradition, is the *declared assertion domain of a morphism*, generalized to a *family of admissible reference systems*, optionally *specialized to a coupled environment subsystem*. The construct is consistent with the formalism, generalizes the existing (D_s, D_b) metrics rather than replacing them, and gives the failure mode of "near-isomorphic to the wrong context" a precise location at every level of the architecture.

---

## 9. Open questions

These are flagged for follow-on work, not addressed in this memo.

1. **How fine should Q_cert be declared?** The Formulation A construct requires Q_cert to be declared at certification time. In practice, the modeler chooses a state-set granularity, and this choice is itself a modeling commitment. Is there a Wymore-native principle (perhaps drawn from the WySE Metamodel) that constrains the choice of Q_cert granularity for trust-monitoring purposes? Conjecture: the appropriate granularity is the coarsest one at which all operationally-distinguishable failure modes are distinguished by Q_cert. This is consistent with Wymore's verification-model approach but needs explicit treatment.

2. **What is the right structure on C?** Formulation B treats C as a set. But operational context spaces have natural structure: ordering (some contexts are more permissive than others), topology (nearby contexts in some sense), or a graph of admissible transitions (which contexts can follow which). What additional structure on C is necessary or natural for Wymore-native treatment? Conjecture: a partial order induced by the existence of morphisms (c_1 <= c_2 iff there is a morphism Z_real(c_1) -> Z_real(c_2)) is the natural structure, and it parallels Wymore's verification-model homomorphism ordering.

3. **What does Formulation B's "no morphism exists" case look like physically?** delta = infinity in the contextual displacement corresponds to two Wymore tuples that are not even morphism-comparable. What deployment scenarios produce this? Conjecture: scenarios where the operational reality has states that have no analog in the certified reality (e.g., a new physiological class in the pediatric ECG example), and where the certified state set cannot surject onto the operational state set. This needs concrete examples.

4. **Does Formulation C require a *bi-directional* coupling?** In some AI deployments the AI is observation-only (no actuation back into Z_env). In others the AI actuates the environment, closing the loop. Formulation C is presented for the bi-directional case (kappa includes both Z_env -> Z_ai and Z_ai -> Z_env wirings). For observation-only AI, the kappa simplifies. Does this simplification change any of the structural conclusions? Conjecture: no, but the simplification should be documented as a corollary.

5. **Where does GUM (Type A + Type B uncertainty) enter the context construct?** The (D_s, D_b) metrics carry GUM uncertainty budgets in the AI Circuit Breaker design spec v4. Does Formulation A's Boolean domain-membership predicate admit a GUM treatment (Type A: sampling variance in domain-boundary estimation; Type B: prior knowledge of certification envelope)? Does Formulation B's delta admit one directly because it is a (D_s, D_b) quantity already? Conjecture: A is harder because it is Boolean; B inherits the existing GUM machinery; C inherits B's. But A's Boolean character can be relaxed to a membership probability if the certification envelope is itself a probabilistic object, in which case A also admits GUM treatment.

6. **Compatibility with Zeigler's experimental frame.** A parallel agent is treating the DEVS / experimental-frame angle. The conjecture from Section 5.4 is that Wymore Formulation C's (Z_env, kappa) specification can express the experimental frame's (generator, acceptor, transducer). If this is correct, the Wymore-native construct of context (this memo) and the DEVS-native construct (the parallel memo) should be reconcilable as different presentations of the same underlying structure. The reconciliation work is deferred to a joint memo once both single-tradition treatments are stable.

7. **Relationship to the kernel/image refinement (angle 8).** Section 5.5 notes that the kernel refinement is a finer-grained reading of D_s. There is a question whether *which equivalence classes the AI lumps together* tracks contextual displacement in Formulation B. Conjecture: yes, in the following sense — the contextual displacement from c_cert to c_op should be lower-bounded by the kernel mismatch between h_cert's kernel and h_op's kernel (where h_op is the hypothetical certified morphism for the operational reality, which by hypothesis does not exist as an asserted artifact). This is a candidate theorem.

8. **What does the construct say about *learning during deployment*?** If the AI updates Z_ai over time (e.g., online learning), then Dom(h) drifts, even if the operational reality is stationary. Formulation A says: the certified Dom(h_cert) is a static artifact of certification, and learning that drifts Dom(h) outside Dom(h_cert) is itself an "out of context" event from the certification's standpoint. This may be the right Wymore-native account of "model drift," and it deserves explicit treatment in a follow-on. Conjecture: model drift is a Formulation-A failure on the morphism side, dual to the wrong-context failure being a Formulation-A failure on the reality side. The instrument response should be symmetric.

---

## 10. Closing note on the construct's status

This memo treats "context" as a construct that needs *recovery* from the Wymore formalism, not invention. The construct is already implicit in:

- The reachable-subset restriction Q_2 in the homomorphism definition,
- The coupling-specification machinery for composing tuples,
- The standing modeling commitment that the choice of (S, I, O) is itself a modeling act.

The intellectual work is to surface the construct, give it a name, assign a type, and identify where in the certification artifact it must be declared. The work is not to extend Wymore beyond what he supplied. If the recommendation here is correct, then the failure of the third-axis D_r attempt was *informative*: it showed that context is not a property of a single morphism, and the search for its true home was a search for the level of the formalism at which the construct does live. The answer, in Wymore-native terms, is that context lives at the level of *the declared assertion domain of a morphism*, generalized to *a family of admissible reference systems*, with the *coupling to an environment subsystem* as the most operationally concrete specialization.

The construct is therefore neither metric nor categorical in any deep sense; it is set-theoretic and family-indexed. It complements (D_s, D_b) at a different syntactic level and a different operational role: D_s and D_b measure morphism quality inside an asserted domain; context declares the domain over which that quality assertion is in force.

This is what the Wymore tradition supplies. It is also, taken seriously, sufficient to detect the deployment failure mode that motivated the construct: an AI that is near-isomorphic to the wrong context fails not as a degraded morphism but as an asserted morphism applied outside its asserted domain.

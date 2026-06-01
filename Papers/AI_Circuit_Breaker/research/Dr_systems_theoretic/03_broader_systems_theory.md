# Broader Systems-Theoretic Treatments of Context

**Purpose.** Reconnaissance of formal constructs for "context," "scope of validity," or "system-environment relationship" in systems-theoretic traditions outside Wymore and Zeigler. Intended as one of three parallel scout reports for Paul Wach's AI Circuit Breaker context formalism. Sister reports cover Wymore-native morphism theory and DEVS / experimental frame respectively.

**Date.** 2026-05-20

**Scope rule.** Wymore morphism theory and DEVS / experimental frame are deliberately excluded; covered by parallel agents.

**Conventions.** Citations include year, venue, and exact title where verifiable. Items I could not confirm to a specific page or chapter without library access are marked **(verify)**. Wymore compatibility is rated **native** (lifts directly into Wymore morphism diagrams), **adjacent** (compatible with translation), or **incompatible** (categorically different commitment).

---

## 1. Mesarović, Macko, Takahara — Hierarchical Multilevel Systems

**Core construct.** Mesarović and colleagues build a multi-strata / multi-echelon theory in which a system is decomposed into a hierarchy of decision units; the higher-level unit (the *supremal*) coordinates lower-level units (the *infimals*) by adjusting goals and constraints rather than by manipulating their internal mechanics. Context in this tradition is what the supremal layer hands to the infimal: the goal vector, the coupling constraints, and the coordination variables that fix the operating regime of the lower stratum. Their later book on goal-seeking systems generalizes this into a goal-decomposition picture where any system is specified by an objective, a feasible set, and a coupling to a higher problem.

**Formal restatement.** Given an overall optimization problem P at the supremal level with decision variable u and constraints g(u, x) <= 0, decompose into N infimal problems P_i parameterized by a coordination signal gamma_i chosen by the supremal. Each infimal solves min f_i(x_i; gamma_i) subject to its local constraints; the supremal updates gamma to drive the assembled infimal solutions toward overall optimality. Context for the infimal is the tuple (gamma_i, local constraints) flowing down; context for the supremal is the response surface flowing up. The three coordination principles introduced are *interaction prediction*, *interaction decoupling*, and *interaction estimation* (verify exact chapter, ch. 5 or 6 of the 1970 book).

**Citation.**
- Mesarović, M. D.; Macko, D.; Takahara, Y. *Theory of Hierarchical, Multilevel, Systems.* Academic Press, New York, 1970. Mathematics in Science and Engineering, vol. 68. Confirmed via Elsevier and Google Books listings.
- Mesarović, M. D.; Takahara, Y. *General Systems Theory: Mathematical Foundations.* Academic Press, 1975 (verify ISBN). Sets the set-theoretic baseline that the hierarchical book specializes.

**Wymore compatibility.** Adjacent, leaning native. Mesarović's set-theoretic system definition (S as a relation on an input set X cross output set Y, or as a state-transition tuple) is the same family of object as Wymore's; the difference is that Mesarović stays largely outside the morphism diagram. Coordination signals could be re-cast as Wymore morphism inputs, making "context" the data of an outer-system morphism into the inner-system parameter space.

**Strengths for AI Circuit Breaker.** Coordination variables formalize the idea of "context handed down from a higher control loop," which is exactly what a circuit-breaker arbitrator does relative to an AI module: the breaker is the supremal, the AI is the infimal. The supremal-infimal split also gives a natural locus for the breaker's veto authority. Multi-echelon variants extend cleanly to multi-AI architectures.

**Weaknesses.** No native treatment of model-mismatch between supremal goals and infimal capability beyond classical coordinability conditions; no probabilistic context. Notation is heavy and the literature is sparse after the 1980s.

---

## 2. Klir — Architecture of Systems Problem Solving and the GSPS

**Core construct.** Klir's *General Systems Problem Solver* (GSPS) is built on an *epistemological hierarchy* in which any system is described at one of a sequence of nested levels, each adding more structural commitment than the level below. The foundational level is the *source system*, which fixes what the inquirer takes the system to be *before* observing it: the variables, their value sets, their distinction into input vs output, and the resolution of the support (time, space, population). Higher levels add data, behavior generators, structure, and metasystem dynamics. Context, in this framing, is encoded at the source-system level: it is the pre-empirical specification of "what counts as the system and what does not."

**Formal restatement.** Klir's hierarchy (the standard version in *Architecture of Systems Problem Solving*, 1985):
1. **Object system / Source system (level 0).** A tuple (V, W, R) where V is a set of variables, W a set of supports (time, space, individuals), and R the resolution mapping; plus a partition of V into input, output, and neutral variables. This is *what* is being inquired into.
2. **Data system (level 1).** Adds an actual data array over (V, W). What has been observed.
3. **Generative system (level 2).** Adds a generator (behavior function, ST-structure, or mask-and-procedure) that reproduces the data. What can be predicted.
4. **Structure system (level 3).** A composition of generative subsystems with coupling. How the system is built from parts.
5. **Metasystem (level 4 and above).** A specification of transitions between structure systems; supports modeling change of structure across time or regime.

The crucial move for "context" is that the source system is logically prior to data and to model: changing the source system changes what counts as the same system. This is exactly the locus of context as the Circuit Breaker needs it.

**Citation.**
- Klir, G. J. *Architecture of Systems Problem Solving.* Plenum Press, New York, 1985. Confirmed via Springer and Plenum reissues; second edition 2003, Kluwer/Plenum.
- Klir, G. J. "General Systems Problem Solver: A framework for integrated systems methodology," (verify article reference; the GSPS framework recurs in *International Journal of General Systems* throughout the 1980s).
- Klir, G. J. *Facets of Systems Science.* Plenum, 1991, ch. on epistemological levels.

**Wymore compatibility.** Native. Klir's source system is essentially a typed set-theoretic specification of input-output variables with support, which lifts directly to a Wymorian system spec; Wymore morphisms between systems become Klir's structure-system mappings.

**Strengths for AI Circuit Breaker.** Klir's source-system level is the cleanest existing formal home in the systems literature for "context as pre-empirical specification." It separates the question "are you applying the right model?" (a behavior-system question) from "are you even looking at the right system?" (a source-system question). The latter is the failure mode the Circuit Breaker most needs to detect.

**Weaknesses.** Klir's framework is descriptive rather than prescriptive about how to choose a source system; the framework is silent on operational context drift. Heavy formal machinery, niche audience.

---

## 3. Bunge — CESM (Composition, Environment, Structure, Mechanism)

**Core construct.** Bunge's CESM model says that any concrete system is fully specified by four sets: its *composition* C (the parts), its *environment* E (the things outside the system that interact with the parts), its *structure* S (the relations among the parts plus the relations between parts and environment), and its *mechanism* M (the lawful processes that produce the system's behavior). Context here is explicitly the environment E, and it is one of four primary dimensions, not an afterthought. The bonding relations in S that cross the system-environment boundary make context a structural element, not an exogenous parameter.

**Formal restatement.** For a concrete system sigma at time t,
- mu(sigma, t) = <C(sigma, t), E(sigma, t), S(sigma, t), M(sigma, t)>
where C, E are sets of things, S is a set of relations on C union E (with both internal C-relations and external C-to-E relations), and M is a set of lawful processes. A subsystem is one whose composition is a subset of C, whose environment is C minus the subset union E, and so on. Bunge consistently defines the environment as the set of things that interact with elements of C but are not themselves in C; the boundary is constituted by the C-to-E relations in S.

**Citation.**
- Bunge, M. *Emergence and Convergence: Qualitative Novelty and the Unity of Knowledge.* University of Toronto Press, 2003. CESM developed in chs. on systemism (verify ch. 2 or 3).
- Bunge, M. *Treatise on Basic Philosophy, Vol. 4: A World of Systems.* Reidel, 1979. Earlier formal statement of the model (verify ch. 1).
- Bunge, M. "Systemism: the alternative to individualism and holism," *Journal of Socio-Economics* 29 (2000), 147-157.

**Wymore compatibility.** Adjacent. Bunge's composition and environment are sets, his structure is a relation set, and his mechanism corresponds (loosely) to a Wymorian state-transition specification. The morphism move that maps a Wymore system to its environment-coupled version is exactly Bunge's S relation crossing the C-E boundary. A clean translation exists, but Bunge's metaphysical framing (concrete versus conceptual systems) carries baggage Wymore does not.

**Strengths for AI Circuit Breaker.** CESM gives a four-coordinate specification of the system under inspection, which immediately distinguishes "context" (E) from "structural commitment" (S) from "internal mechanism" (M). The breaker can then ask four separate questions: did E shift, did S shift, did C shift, did M shift? Each kind of shift has a different remedy. Bunge's framework also handles emergence cleanly, which matters when AI behavior arises from couplings the designer did not specify.

**Weaknesses.** Bunge's framework is descriptive; he gives no measure-theoretic instrument for *how much* the environment has shifted. CESM is a categorization, not a metric.

---

## 4. Maturana and Varela — Autopoiesis and Structural Coupling

**Core construct.** A living system is an *autopoietic* network: a network of component-producing processes whose product is exactly the same network. The system is operationally closed, but it is *structurally coupled* to its environment, meaning that its internal state changes in step with environmental perturbations in a way that maintains autopoiesis. Structural coupling is the systems-theoretic name for the historically-accumulated, mutual fit between a system and its medium. Context here is not a static parameter but a coupling history: what the medium has *done with* the system, and reciprocally.

**Formal restatement.** Maturana and Varela's original definition is given in set-theoretic prose rather than equations. The standard reconstruction: an autopoietic system is a unity U with components C, processes P, and a topology that specifies which components are produced by which processes, satisfying
- closure under production: every component of U is produced by some process in P whose inputs are themselves in U union M(U), where M(U) is the medium;
- self-distinction: U is distinguishable from M(U) by the same components whose production it constitutes.
Structural coupling is then a relation between the trajectory of U and the trajectory of M(U) such that recurrent interactions select compatible structural changes without breaking the autopoietic closure.

**Citation.**
- Maturana, H. R.; Varela, F. J. *Autopoiesis and Cognition: The Realization of the Living.* Boston Studies in the Philosophy of Science, vol. 42. Reidel, Dordrecht, 1980. Reprints two key 1970s essays.
- Maturana, H. R.; Varela, F. J. *The Tree of Knowledge: The Biological Roots of Human Understanding.* Shambhala, 1987. Popular exposition of structural coupling.
- Razeto-Barry, P. "Autopoiesis 40 years later: A review and a reformulation," *Origins of Life and Evolution of Biospheres* 42 (2012), 543-567. Modern formal restatement.

**Wymore compatibility.** Incompatible at the philosophical level (operational closure denies the externalist stance Wymore presumes); adjacent at the formal level (the coupling relation can be re-cast as a Wymore product system with a constraint that internal-state production is closed). The intuition that *context is constitutive of the system over time* is foreign to Wymore but recoverable through history-dependent morphisms.

**Strengths for AI Circuit Breaker.** Structural coupling captures something the Circuit Breaker eventually needs: the realization that an AI's operating context is not a static "input distribution" but a *history of mutual adjustment* between the AI and the world it acts on. Calibration drifts because deployment changes the world. This is exactly the autopoietic point.

**Weaknesses.** No native metric; the literature is notoriously informal; transferring constructs requires re-formalization.

---

## 5. Pattee — Epistemic Cut and Semantic Closure

**Core construct.** Pattee's foundational claim is that any modeling activity requires a cut: a *symbol* side (rate-independent, discrete, syntactic, the model) and a *matter* side (rate-dependent, continuous, dynamical, the referent). The cut is *epistemic* in that it is imposed by the modeler, not metaphysically given, and it must be drawn afresh for each modeling problem. *Semantic closure* is the condition under which a self-referential system can read its own symbols and produce the matter described by them, as DNA does. Context, in this framing, is *what determines where the cut goes*: the choice of measurement device, observable, and rate regime that fixes which side a given physical event lives on.

**Formal restatement.** Pattee does not give a single formal definition but uses a recurring scheme:
- A natural system N evolves under dynamical laws on a state space X.
- A symbol system S consists of discrete tokens with syntactic rules, evolving by rule application rather than physical law.
- An epistemic cut is a partition of the physical world into (N, S, measurement, construction) such that S can describe events in N via measurement and act on N via construction (a constraint that modifies dynamics).
- Semantic closure holds when an organism contains both the symbol system S and the matter side N such that the symbols specify the construction of the very dynamics that read them.

**Citation.**
- Pattee, H. H. *Laws, Language and Life: Howard Pattee's Classic Papers on the Physics of Symbols with Contemporary Commentary.* Biosemiotics, vol. 7. Springer, 2012. Edited with J. Rączaszek-Leonardi. Confirmed.
- Pattee, H. H. "Evolving self-reference: matter, symbols, and semantic closure," *Communication and Cognition - AI* 12 (1995), 9-27. Source of "semantic closure" term.
- Pattee, H. H. "The physics of symbols: bridging the epistemic cut," *Biosystems* 60 (2001), 5-21. Source for the formal cut framing.

**Wymore compatibility.** Adjacent. Wymore implicitly stands on the symbol side of Pattee's cut; the modeler chooses an input alphabet, an output alphabet, and a state set, then writes a transition function. Pattee makes the act of choosing those alphabets the locus of context. This sits cleanly under Wymore but is rarely articulated in Wymore writing.

**Strengths for AI Circuit Breaker.** Pattee gives the cleanest existing language for the AI-specific failure mode of *symbols losing their referents*. When an AI's output tokens (e.g., "approved," "anomaly," a control signal) no longer refer to the physical events the training distribution assumed, the epistemic cut has been silently re-drawn by deployment. The breaker's job is to monitor cut integrity.

**Weaknesses.** Pattee's framework is philosophical; it gives no algorithmic test. Translating it into a runtime monitor requires substantial bridging work.

---

## 6. Rosen — Modeling Relation, Anticipatory Systems

**Core construct.** Rosen's *modeling relation* is a commuting diagram between a natural system N (with internal causal entailments) and a formal system F (with internal inferential entailments), connected by encoding (N to F) and decoding (F to N) arrows. The diagram commutes when, for every causal sequence in N, the encoded predicate is provable in F and decodes back to the consequent in N. *Anticipatory systems* are systems that contain such a model of themselves and their environment and act on its predictions; *context* is the encoding specification, i.e., the choice of which observables of N enter F and how.

**Formal restatement.** A modeling relation is the diagram
- N has internal entailment c: x -> y (cause to effect)
- F has internal entailment i: phi(x) -> phi(y) (premise to conclusion)
- encoding e: N -> F maps x to phi(x), y to phi(y)
- decoding d: F -> N maps phi back into N
The diagram commutes when d(i(e(x))) = c(x) for relevant x. Rosen's *Life Itself* (1991) then argues that organisms are systems with non-trivial closure of efficient causation, and cannot be modeled by any single F; they need a category-theoretic (M, R)-system.

**Citation.**
- Rosen, R. *Anticipatory Systems: Philosophical, Mathematical, and Methodological Foundations.* Pergamon, 1985. Second edition: Springer, 2012, with new commentary by Louie and Kineman.
- Rosen, R. *Life Itself: A Comprehensive Inquiry into the Nature, Origin, and Fabrication of Life.* Columbia University Press, 1991.
- Louie, A. H. *More Than Life Itself: A Synthetic Continuation in Relational Biology.* Ontos, 2009. Most rigorous reconstruction of Rosen's category theory.

**Wymore compatibility.** Native. The modeling relation is the same shape as a Wymore homomorphism diagram, with encoding and decoding standing in for Wymore's morphism pair. In fact, Rosen's diagram can be read as Wymore's structural homomorphism between an "ideal" formal system and a "deployed" natural one. The degree-of-homomorphism construct in Wach's CSER 2025 paper is closely analogous to Rosen's commutation defect.

**Strengths for AI Circuit Breaker.** Rosen's diagram is the cleanest existing template for the breaker's job: monitor whether the encoding-decoding pair still commutes with the natural-system causation, i.e., whether the formal model still earns its keep. Rosen also formalizes anticipation, which connects to the breaker's preemptive intervention role.

**Weaknesses.** Rosen's later (M, R)-system claim that life is non-computable is contested; care needed to use the modeling relation without inheriting the controversial closure-of-efficient-causation thesis. Notation is uneven across the corpus.

---

## 7. General Systems Theory — von Bertalanffy, Boulding, Rapoport

**Core construct.** General Systems Theory (GST) is older and looser than the constructions above. Von Bertalanffy distinguishes *closed* from *open* systems, where an open system maintains itself by continual exchange with its environment; equifinality (multiple initial states reaching the same final state) and steady-state non-equilibrium are central. Context here is the environment from which matter, energy, and information flow into the system, but the framework remains qualitative.

**Formal restatement.** Von Bertalanffy's open-system equation (verify; *General System Theory*, ch. 6 or 7) gives the time-rate of a system property Q as
- dQ/dt = production - degradation + influx - efflux
Equifinality is the property that lim t->inf Q(t) is independent of Q(0) over an interesting range of initial conditions. Boulding's nine-level hierarchy of system complexity and Rapoport's mathematical biology contributions are categorizing rather than formalizing; no measure-theoretic context construct emerges at this layer.

**Citation.**
- von Bertalanffy, L. *General System Theory: Foundations, Development, Applications.* George Braziller, New York, 1968. Confirmed.
- Boulding, K. E. "General Systems Theory: The Skeleton of Science," *Management Science* 2 (1956), 197-208.
- Rapoport, A. *General System Theory: Essential Concepts and Applications.* Abacus, 1986.

**Wymore compatibility.** Adjacent at best; GST is too informal to commute with Wymore directly. The open-system idea lifts to Wymore as a system with explicit external coupling functions, but the framework gives no leverage on context as such.

**Strengths for AI Circuit Breaker.** Useful framing language but no formal handle. Equifinality is conceptually relevant to model-context mismatch (different deployments may converge to the same observable behavior while differing internally) but the framework does not formalize the asymmetry.

**Weaknesses.** Too informal for direct use. Cite for genealogy, not formalism.

---

## 8. Cybernetics — Ashby, Wiener, Beer

**Core construct.** Cybernetics holds that to regulate a system, the regulator must contain a model of the regulated system at least as varied as the disturbances; Ashby's *Law of Requisite Variety* states V(R) >= V(D) / V(O), where V denotes variety (log of distinguishable states), R the regulator, D the disturbance, and O the output. The *Good Regulator Theorem* (Conant and Ashby, 1970) hardens this: every good regulator must be (or contain) a model of the system regulated. Beer's *Viable System Model* (VSM) takes this further: a viable organization has five interacting subsystems (Operations, Coordination, Control, Intelligence, Policy), with the *environment* as an explicit external box coupled to each.

**Formal restatement.**
- *Law of Requisite Variety* (Ashby 1956): for an inverse regulation goal, log |R| >= log |D| - log |O|, with equality when regulation is perfect.
- *Good Regulator Theorem* (Conant and Ashby 1970): R is a homomorphism (or isomorphism) of the regulated system, in the precise category-theoretic sense; the regulator's state space maps onto the regulated system's state space.
- *VSM* (Beer): System 1 = primary activities; System 2 = anti-oscillation coordination; System 3 = present-tense management plus System 3* audit; System 4 = environmental intelligence and forecasting; System 5 = identity / policy. The environment is explicitly drawn as a separate box with bidirectional arrows to Systems 1 and 4.

**Citation.**
- Ashby, W. R. *An Introduction to Cybernetics.* Chapman & Hall, 1956. Law of Requisite Variety in ch. 11.
- Conant, R. C.; Ashby, W. R. "Every good regulator of a system must be a model of that system," *International Journal of Systems Science* 1 (1970), 89-97.
- Beer, S. *Brain of the Firm*, 2nd ed. Wiley, 1981. VSM full statement.
- Beer, S. *The Heart of Enterprise.* Wiley, 1979.
- Beer, S. *Diagnosing the System for Organizations.* Wiley, 1985.

**Wymore compatibility.** Native (Ashby's Good Regulator theorem is literally a homomorphism statement; Wymorians and cyberneticians use the same morphism diagrams). Adjacent for VSM (the five subsystems are structurally a hierarchical decomposition compatible with Mesarović's stratification).

**Strengths for AI Circuit Breaker.** The Good Regulator Theorem is the cleanest classical statement of the breaker's requirement: the breaker must contain a model of the AI it regulates *and* of the environment in which the AI acts. Ashby's variety inequality gives a direct quantitative constraint on the breaker's representational capacity. Beer's System 4 (environmental intelligence) is the exact organizational locus the breaker occupies.

**Weaknesses.** Variety is a coarse measure; it counts distinguishable states but says nothing about which state distinctions matter. VSM is loose enough to be polysemous in practice.

---

## 9. Polish / Lvov-Warsaw School (Bocheński, Ajdukiewicz)

**Core construct.** The Lvov-Warsaw School worked on formal logic, ontology, and the categorial reconstruction of concepts. Ajdukiewicz developed a *radical conventionalism* in which the meaning of terms depends on the language frame chosen; Bocheński reconstructed concepts categorially. The closest the school comes to a systems-theoretic context construct is the idea that propositions are not freely composable across language frames; meaning is frame-relative, and translating between frames requires explicit mapping.

**Citation.**
- Wolenski, J. *Logic and Philosophy in the Lvov-Warsaw School.* Synthese Library, vol. 198. Kluwer, 1989.
- Wybraniec-Skardowska, U. (ed.). *Tradition of the Lvov-Warsaw School: Ideas and Continuations.* Brill, 2016. Includes chapters on Bocheński's categorial reconstruction (verify).
- Ajdukiewicz, K. "Die wissenschaftliche Weltperspektive," *Erkenntnis* 5 (1935), 22-30. Conventionalism source.

**Wymore compatibility.** Tangential. The school's contributions are mostly logical, not systems-theoretic; no construct lifts directly. The conventionalism point about frame-relative meaning is philosophically resonant with Pattee's epistemic cut and Klir's source system, but the school did not pursue it into a systems formalism.

**Strengths and weaknesses.** Mark as "scouted, low yield." Cite if needed for a philosophy-of-systems grounding move, not for a working formalism. Drop from main pull list.

---

## 10. Hierarchical and Multi-Resolution Systems Theory — Yates, Salthe

**Core construct.** Salthe's hierarchy theory holds that any focal level of a system is constituted by, and constrains, a *triad* of levels: the focal level itself, the *infra* level (its constituent parts, with their own dynamics), and the *supra* level (the larger system in which it is embedded, providing boundary conditions). Context for any focal level lives at the supra level; degrees of freedom emerge from the infra. Yates and Iberall's *homeokinetics* adds physical dynamics to this picture, treating each level as a thermodynamic engine. The triad is hermeneutical, not just descriptive; it claims that you cannot specify any focal-level system without acknowledging both the level below and the level above.

**Formal restatement.** Salthe represents a basic triadic system as the ordered triple (L_infra, L_focal, L_supra), with non-transitivity of effects: an event at L_focal can be caused by L_infra dynamics or constrained by L_supra boundary conditions, and these two modes cannot be collapsed. The non-transitivity is exactly the failure of effects to compose freely across more than two adjacent levels; this is the hierarchical analog of Pattee's epistemic cut. Salthe later (2002) extended this with a *specification hierarchy* alongside the older *scalar hierarchy*.

**Citation.**
- Salthe, S. N. *Evolving Hierarchical Systems: Their Structure and Representation.* Columbia University Press, New York, 1985. Confirmed.
- Salthe, S. N. *Development and Evolution: Complexity and Change in Biology.* MIT Press, 1993.
- Yates, F. E. (ed.). *Self-Organizing Systems: The Emergence of Order.* Life Science Monographs. Plenum, 1987. Confirmed.
- Iberall, A. S.; Yates, F. E. "Temporal and hierarchical organization in biosystems," in Yates 1987 (verify ch. and pp.).

**Wymore compatibility.** Adjacent. The triad maps cleanly onto a Wymorian hierarchy of systems with morphisms between scales (the supra system constraining the focal, the focal aggregating the infra). Non-transitivity becomes a constraint on which morphism compositions are valid.

**Strengths for AI Circuit Breaker.** The triadic formulation gives the breaker a *minimum* specification of context: at least the immediate supra level (the deployment regime) and infra level (the model's internal representations) must be tracked, and effects cannot be assumed to compose across them. This is a useful corrective to AI evaluations that focus only on input-output behavior.

**Weaknesses.** Salthe's writing is dense and not algorithmic; conceptual yield is high but tooling yield is low.

---

## 11. Soft Systems Methodology and Critical Systems Thinking — Checkland, Mingers

**Core construct.** Checkland's Soft Systems Methodology (SSM) abandons the search for a single objective system; it treats every human activity system as the joint product of stakeholders' *Weltanschauungen* (worldviews), each of which yields a different root definition of the same situation. CATWOE (Customer, Actor, Transformation, Weltanschauung, Owner, Environmental constraints) is a checklist for surfacing those worldview-dependent definitions. Context, in SSM, is the worldview-conditioned framing that turns a situation into a system. The "E" in CATWOE is environmental constraints; the "W" is the worldview that decides what counts as relevant in the first place.

**Citation.**
- Checkland, P. *Systems Thinking, Systems Practice.* Wiley, 1981. Original SSM statement.
- Checkland, P.; Scholes, J. *Soft Systems Methodology in Action.* Wiley, 1990.
- Checkland, P.; Poulter, J. *Learning for Action: A Short Definitive Account of Soft Systems Methodology and Its Use for Practitioners, Teachers and Students.* Wiley, 2006.
- Mingers, J. *Systems Thinking, Critical Realism and Philosophy.* Routledge, 2014.

**Wymore compatibility.** Incompatible at the philosophy-of-systems layer (SSM denies that there is a single objective system to write a Wymore spec for). Adjacent if Weltanschauung is operationalized as a *choice of source system* in Klir's sense; then SSM becomes a way of selecting a Wymorian spec, but the moment that spec is chosen, the formalism takes over.

**Strengths for AI Circuit Breaker.** SSM is the only tradition that names stakeholder-relative framing as constitutive of "what the system is." This matters for the Circuit Breaker because different stakeholders (operator, developer, regulator, end user) have different views of "context" and the breaker must mediate among them. CATWOE is a usable elicitation checklist for context audits.

**Weaknesses.** Deliberately non-formal; gives no measure or invariant.

---

## 12. Friston — Free Energy Principle and Markov Blanket

**Core construct.** Friston's free-energy principle (FEP) starts from a *sparse partition* of the world into internal states mu, external states eta, sensory states s, and active states a, where s and a together constitute the *Markov blanket* b = (s, a) of the internal states. The blanket is the set of nodes that statistically shield mu from eta: conditional on b, mu and eta are independent. Active inference then says that any system that persists in nonequilibrium steady state appears to minimize a variational free energy functional of its sensory states, which is equivalent to acting as if it had a generative model of its environment. Context, in this framing, is exactly *what is outside the Markov blanket*: eta. The blanket is the geometry of context.

**Formal restatement.** Partition the state vector x = (eta, s, a, mu) such that the joint density factorizes with the conditional independence
- p(eta, mu | s, a) = p(eta | s, a) p(mu | s, a).
This is the Markov blanket condition. Under sparse coupling and a nonequilibrium steady-state assumption, the system's internal states track posterior beliefs about external states via a variational free energy
- F[q] = E_q[log q(eta) - log p(eta, s)]
and active states act so as to drive sensory states toward a generative model's predictions, minimizing F. The Markov blanket *is* the formal definition of "the boundary that defines context."

**Citation.**
- Friston, K. "The free-energy principle: a unified brain theory?" *Nature Reviews Neuroscience* 11 (2010), 127-138.
- Friston, K. "A free energy principle for a particular physics," *arXiv:1906.10184*, 2019.
- Kirchhoff, M.; Parr, T.; Palacios, E.; Friston, K.; Kiverstein, J. "The Markov blankets of life: autonomy, active inference and the free energy principle," *Journal of the Royal Society Interface* 15 (2018), 20170792.
- Parr, T.; Pezzulo, G.; Friston, K. *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior.* MIT Press, 2022.

Caveat: the Markov blanket formulation has been critiqued (Bruineberg et al., "The Emperor's New Markov Blankets," 2022, *Behavioral and Brain Sciences*) as conflating a statistical property of a model with a property of the modeled system. The Circuit Breaker can adopt the formalism while taking the critique on board: the blanket is a useful *modeler's* construct even if its ontological status is contested.

**Wymore compatibility.** Native at the formal level. The Markov blanket partition (eta, s, a, mu) is a structural decomposition of a system into the form (environment, input, output, state), which is essentially Wymore's system tuple. The conditional independence requirement adds a probabilistic refinement Wymore does not give but does not contradict.

**Strengths for AI Circuit Breaker.** The strongest contemporary formalism for context on the list. It gives (i) a precise definition of system-environment boundary, (ii) a precise notion of when a system is "tracking" its context (free energy is low), and (iii) a precise notion of when context drifts in a way the system has not modeled (free energy spikes). This is directly operationalizable as a Circuit Breaker telemetry signal. The "calibrated to wrong context" failure mode shows up as a sustained free-energy increase that does not reduce under continued inference.

**Weaknesses.** Requires specifying a generative model; the ontological critiques deserve a footnote; computational cost can be high for realistic models.

---

# Synthesis

## 1. Most directly usable formal constructs

Three traditions stand out for direct reuse:

1. **Friston's Markov blanket / FEP** is the strongest contemporary formalism. It gives a precise system-environment partition, a probabilistic conditional-independence condition, and an operational telemetry signal (free energy) for "is the system still in its valid context?" It is the best match for the Circuit Breaker's runtime needs.

2. **Klir's source system / GSPS hierarchy** is the cleanest formal home for "context as pre-empirical specification." It distinguishes "what is the system" (source level) from "what does the system do" (behavior level) from "what does the system change into" (metasystem level). Each level has a different drift mode the breaker can monitor.

3. **Rosen's modeling relation** is the cleanest formal home for "is the model still earning its keep?" It is also the most directly compatible with Wymore's morphism diagrams and with Wach's degree-of-homomorphism construct. The commutation defect in Rosen's diagram is a natural sister to the structural distance D_s.

Honorable mention: **Ashby's Good Regulator Theorem** provides a category-theoretic minimum bound on what the breaker must contain to be a competent breaker, and **Bunge's CESM** gives a four-coordinate categorization of *kinds of drift* (composition, environment, structure, mechanism) that maps cleanly onto distinct breaker monitors.

## 2. Traditions that anticipate the "AI calibrated to wrong context" failure mode

Most directly:
- **Pattee** anticipates this exactly under the language of "epistemic cut migration": when deployment changes what the symbols refer to without changing the symbols themselves, the cut has been silently re-drawn and the system is using the right syntax for the wrong matter. This is the AI failure mode in non-AI language.
- **Maturana and Varela** anticipate it as *loss of structural coupling*: when an autopoietic unity's medium changes faster than the system can recouple, the system continues acting as if the old coupling held.
- **Rosen** anticipates it as *failure of the modeling relation to commute*: encoding still produces an output, decoding still produces a prediction, but the natural-system causation no longer matches.
- **Friston** anticipates it as *sustained free-energy increase*: the generative model's predictions diverge from sensed data and continued inference does not close the gap.
- **Ashby** anticipates it weakly as *variety mismatch*: the regulator's variety is no longer adequate to the disturbance variety.

Traditions that *do not* anticipate it cleanly: GST (no formal handle), Lvov-Warsaw (off topic), SSM (treats it as a stakeholder problem rather than a calibration problem), Mesarović (frames coordination but not coordination failure under deployment shift).

## 3. Open ground

What is missing across all of them:

- **A joint structural-and-distributional measure** of context match. Friston has a distributional measure (free energy) but no structural-distance reading. Rosen has a structural commutation criterion but no probabilistic refinement. Wymore's degree-of-homomorphism is structural-only. No tradition combines both axes natively.
- **Operational triggers from formal definitions.** Bunge gives a categorization of context types but no metric; Pattee gives a profound diagnosis but no algorithm; Salthe gives a hierarchy but no test for level-crossing. The Circuit Breaker needs a metric *and* a trigger threshold *and* a remediation action; no tradition delivers all three.
- **Multi-stakeholder context arbitration.** SSM and CSH (critical systems heuristics) name the problem but do not formalize it; everyone else assumes a single modeler.
- **Composition of contexts.** When two AIs interact, what is the joint context? Mesarović has coordination but not context composition; Bunge has CESM but not CESM merging.

This is the open ground for a Wach-style synthesis: a Wymore-compatible formalism that combines a structural distance (extending degree-of-homomorphism) with a distributional distance (extending free energy), parameterized over a Bungean four-coordinate categorization of drift kinds, with an operational threshold-and-action layer inherited from Beer's VSM Systems 3-4-5.

## 4. Compatibility with the degree-of-homomorphism construct (sigma)

Wach's degree-of-homomorphism is a structural distance over state, input, and output mappings between two Wymorian systems. A "degree of context match" by analogy could be defined for each tradition:

- **Klir.** Define sigma_context between two source systems (V, W, R) and (V', W', R') as a structural distance over the variable set, the support, and the resolution mapping. Reduces to identity when both source systems specify the same thing.
- **Bunge.** Define sigma_C, sigma_E, sigma_S, sigma_M as four parallel structural distances, one per CESM dimension. Context match becomes a vector, not a scalar; aggregation is a downstream design choice.
- **Maturana.** Define sigma_couple as a distance over the structural-coupling history between system and medium; technically demanding (history-dependent).
- **Pattee.** Define sigma_cut as a distance between two cut placements, measured by which physical events lie on the symbol side under each. Combinatorial; potentially intractable.
- **Rosen.** Define sigma_model as the commutation defect of the modeling diagram, e.g., d(i(e(x))) - c(x) integrated over relevant x. This is the most natural sister to Wach's sigma; near-identical formal shape.
- **Friston.** Define sigma_FE as the time-average free-energy difference between deployment and calibration, normalized. This is the *behavioral* axis; orthogonal to Wach's structural axis. The two together would close the open ground from (3).
- **Ashby.** Define sigma_var as the deficit log V(R) - log V(D); a single-scalar version of context match through the lens of variety.

Of these, **Rosen-sigma** and **Friston-sigma** are the two best candidates for direct integration with Wach's existing construct: Rosen because the formal shape is identical, Friston because the axis is orthogonal (structural sigma plus distributional sigma_FE would give a two-axis context match analog to Wach's existing two-axis (D_s, D_b) construct).

## Geometric Pictures of Context

A one-paragraph sketch for each of the six listed traditions:

- **Bunge (CESM).** Four-set Venn-like picture: the system is a labeled blob C surrounded by another labeled blob E, with structural arrows S crossing the boundary in both directions and mechanism arrows M coiled inside C. Context is the right-hand circle, and drift is movement of either the C-E boundary or the S arrows that cross it.
- **Mesarović (coordination layer).** Vertical stack of horizontal slabs: the supremal sits on top, infimals lie below, coordination signals flow down (thick gray arrows), local responses flow up (thin black arrows). Context is the bundle of downward arrows entering each infimal slab.
- **Maturana (structural coupling).** Two interlocking gears, system and medium, whose teeth have been ground smooth by long use. The geometry is *historical* rather than spatial: the present coupling is a fossil record of past interactions. Context is the worn shape of the medium's gear.
- **Rosen (modeling relation).** Commuting rectangle: top row is the natural system N with a horizontal arrow c (causal entailment); bottom row is the formal system F with a horizontal arrow i (inferential entailment); vertical arrows e (encoding) and d (decoding) connect them. Context is the data of the vertical arrows. The rectangle commutes when the model is valid; commutation defect = context mismatch.
- **Pattee (epistemic cut).** A horizontal partition line dividing the world into a symbol stratum above (discrete tokens floating, no thermal noise) and a matter stratum below (continuous dynamics, full thermal). The cut is the line itself; context is the cut's location. Drift = the line moves silently while the symbols above stay put.
- **Friston (Markov blanket).** Concentric onion: external states eta on the outside, then a thin shell containing sensory states s and active states a (the blanket), then internal states mu in the core. Context is the outermost layer and the shell that mediates it. The shell is where the breaker reads its telemetry.

These six pictures are not mutually exclusive: the Mesarović stack can be drawn inside the Bungean blob; the Friston onion is what you get when you put the Rosen rectangle inside a probability density; the Pattee cut runs through every diagram horizontally between symbol and matter.

## Recommendation for Wach's Wymore-Compatible Context Formalism

Pull primarily from:

1. **Rosen** for the formal shape of the modeling relation; the degree-of-homomorphism construct is already half of Rosen's diagram. Adopt his vocabulary of encoding-decoding to name the morphism pair.
2. **Friston** for the distributional axis; introduce a free-energy-style scalar as the orthogonal behavioral context measure. This continues Wach's existing two-axis (structural, behavioral) decomposition.
3. **Bunge (CESM)** for the typology of context drift (component drift, environment drift, structure drift, mechanism drift); each gets its own monitor.
4. **Klir** for the level structure: source-system drift versus behavior-system drift versus metasystem drift. This gives the breaker a vocabulary for *what kind of recalibration is needed*.

Pull secondarily from:

5. **Ashby** (Good Regulator) for the minimum-capacity argument: the breaker must contain a model at least as varied as the AI-plus-environment composite.
6. **Beer (VSM)** for the organizational architecture of the breaker: System 3 (present-tense monitoring), System 4 (deployment intelligence), System 5 (policy / veto).
7. **Pattee** for the philosophical framing in non-technical writing: the AI failure mode as silent epistemic-cut drift.
8. **Salthe** as a check that the breaker has at least three levels in view (infra, focal, supra).

Do not pull primary content from von Bertalanffy-era GST, the Lvov-Warsaw school, or pure SSM; cite these for genealogy only.

The synthesis target: define a "degree of context match" Sigma_ctx = (sigma_struct, sigma_dist) over a four-coordinate Bungean drift typology, with Klir-level source-system invariants as gating preconditions and Ashby's Good Regulator inequality as the capacity lower bound. This stays inside Wymore (structural piece is degree-of-homomorphism) while inheriting the Friston probabilistic refinement that Wymore lacks.

---

# Critical Citations List

Core references that should appear in the AI Circuit Breaker context formalism paper:

- Ashby, W. R. *An Introduction to Cybernetics.* Chapman & Hall, 1956.
- Bunge, M. *Treatise on Basic Philosophy, Vol. 4: A World of Systems.* Reidel, 1979.
- Bunge, M. *Emergence and Convergence: Qualitative Novelty and the Unity of Knowledge.* University of Toronto Press, 2003.
- Conant, R. C.; Ashby, W. R. "Every good regulator of a system must be a model of that system," *International Journal of Systems Science* 1 (1970), 89-97.
- Friston, K. "The free-energy principle: a unified brain theory?" *Nature Reviews Neuroscience* 11 (2010), 127-138.
- Friston, K. "A free energy principle for a particular physics," *arXiv:1906.10184*, 2019.
- Kirchhoff, M.; Parr, T.; Palacios, E.; Friston, K.; Kiverstein, J. "The Markov blankets of life: autonomy, active inference and the free energy principle," *Journal of the Royal Society Interface* 15 (2018), 20170792.
- Klir, G. J. *Architecture of Systems Problem Solving.* Plenum, 1985 (2nd ed. Kluwer, 2003).
- Maturana, H. R.; Varela, F. J. *Autopoiesis and Cognition: The Realization of the Living.* Reidel, 1980.
- Mesarović, M. D.; Macko, D.; Takahara, Y. *Theory of Hierarchical, Multilevel, Systems.* Academic Press, 1970.
- Pattee, H. H. "The physics of symbols: bridging the epistemic cut," *Biosystems* 60 (2001), 5-21.
- Pattee, H. H. *Laws, Language and Life.* Springer Biosemiotics vol. 7, 2012.
- Rosen, R. *Anticipatory Systems.* Pergamon, 1985 (2nd ed. Springer, 2012).
- Rosen, R. *Life Itself.* Columbia University Press, 1991.
- Salthe, S. N. *Evolving Hierarchical Systems.* Columbia University Press, 1985.

Secondary / framing references:

- Beer, S. *Brain of the Firm*, 2nd ed. Wiley, 1981.
- Beer, S. *The Heart of Enterprise.* Wiley, 1979.
- von Bertalanffy, L. *General System Theory: Foundations, Development, Applications.* Braziller, 1968.
- Checkland, P. *Systems Thinking, Systems Practice.* Wiley, 1981.
- Louie, A. H. *More Than Life Itself.* Ontos, 2009.
- Bruineberg, J.; Dolega, K.; Dewhurst, J.; Baltieri, M. "The Emperor's New Markov Blankets," *Behavioral and Brain Sciences* (2022). Important critique to cite alongside Friston.

Unverified items (need library check before publication):

- Bunge ch. and pp. for CESM formal statement in *Emergence and Convergence*, 2003. **(verify)**
- Klir formal source-system tuple definition with page in *Architecture of Systems Problem Solving*, 1985. **(verify)**
- Mesarović coordination-principle chapter, 1970. **(verify)**
- Iberall and Yates ch. and pp. in Yates 1987. **(verify)**
- Wybraniec-Skardowska 2016 Bocheński chapter (verify whether it actually treats categorial reconstruction relevant to context). **(verify)**
- Razeto-Barry 2012 formal autopoiesis reformulation (verify exact axiom set used). **(verify)**

---

# Notes on Method and Limits

This report is a desk reconnaissance; I have not had library access to verify exact page numbers and chapter boundaries for the older monographs (Mesarović 1970, Klir 1985, Rosen 1985 first edition, Pattee 2001 *Biosystems* article). Each item marked **(verify)** above should be checked before publication. Bibliographic data (year, venue, exact title) was cross-checked against publisher records and standard secondary literature; I am confident in the bibliographic data, less confident in fine page references.

The selection of traditions follows the user's list. I did not find substantive context formalism in von Bertalanffy-era GST (qualitative) or the Lvov-Warsaw School (off topic for systems context); both are noted but not recommended as primary pulls. The Yates/Salthe hierarchy cluster yielded more than expected and is worth re-reading in the original.

Adjacent traditions not on the user's list that may deserve scouting in a follow-up: (i) **Open Systems Interconnection (OSI) layering** as a context-stack picture from a different discipline (engineering rather than biology); (ii) **Goguen's institutions and sheaves** for a category-theoretic account of context-dependent semantics that sits very close to Wymore morphisms; (iii) **Barwise and Perry's situation theory** for an information-theoretic context calculus from the 1980s. Goguen in particular looks like a clean Wymore neighbor and may give the category-theoretic plumbing for the structural sigma side of the proposed synthesis.

End of report.

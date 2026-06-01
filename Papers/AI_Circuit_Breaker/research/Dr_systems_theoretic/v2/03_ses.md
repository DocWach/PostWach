# The System Entity Structure (SES) as the Systems-Theoretic Home for Context Families

**Purpose.** Develop the System Entity Structure formalism as the Zeigler-tradition apparatus that organizes *families* of contexts under which an AI system is certified, deployed, and re-deployed. The prior swarm covered the DEVS Experimental Frame in depth but stopped short of SES. The user has flagged this as a required input: EF specifies *one* context for *one* model; SES specifies the *space of contexts* and the *space of models* over which morphisms, pruning, and abstraction operate. This document fills that gap.

**Date.** 2026-05-20.

**Author lineage.** Zeigler-tradition treatment, SES branch. Parallel agents cover WySE / Wymore-native, broader systems theory, categorical synthesis, the Bayesian SE draft, and the WySE Metamodel. This document deliberately stays in the SES / DEVS-coupled-model / Zeigler-Rozenblit-Praehofer half of the formalism and does not duplicate the EF material in `../02_devs_experimental_frame.md`.

**Lineage to prior work.**
- Builds directly on `../02_devs_experimental_frame.md` Section 7 open question 4, which flagged SES as the natural composition algebra for *families* of EFs and deferred it.
- Builds on `../synthesis_debate.md` Section 5.3 (Layer 3: Wymore-B / categorical inter-fiber morphism) as the construct the SES is the operational home for.
- The user's Bayesian SE draft already deploys the hierarchy of system specifications with io observation-frame morphisms and NS coupled-system morphisms; SES is the structural apparatus that lets that hierarchy carry *families* rather than single instances.

**Citation key (verified items in Section 8).**
- ZPK00: Zeigler, B. P., Praehofer, H., Kim, T. G., *Theory of Modeling and Simulation*, 2nd ed., Academic Press, 2000. (SES exposed at book-length; canonical reference.)
- ZMK18: Zeigler, B. P., Muzy, A., Kofman, E., *Theory of Modeling and Simulation: Discrete Event & Iterative System Computational Foundations*, 3rd ed., Academic Press, 2018.
- Z23: Zeigler, B. P., "Extending the Hierarchy of System Specifications and Morphisms with SES Abstraction," *Information* 14(1), art. 22, 2023 (published online 29 Dec 2022). DOI 10.3390/info14010022. (Note: published in *Information* vol. 14, issue 1, art. 22, which dates as a 2023 issue even though the online date is Dec 2022. Cite as Z23 hereafter to avoid confusion. The brief used "Z22"; the actual journal volume is 14, 2023.)
- ZKZ24: Zeigler, B. P., Koertje, C., Zanni, C., "The utility of homomorphism concepts in simulation: building families of models from base-lumped model pairs," *Simulation* 100(12), pp. 1181-1196, 2024. DOI 10.1177/00375497241264834.
- RZ85: Rozenblit, J. W., Zeigler, B. P., "Concepts for knowledge-based system structure design overlays," *Proc. IEEE Conf. Systems, Man, Cybernetics*, 1985. (verify exact title and venue; this is the foundational SES paper in the Rozenblit-Zeigler collaboration.)
- RZ90: Rozenblit, J. W., Hu, J., Kim, T. G., Zeigler, B. P., "Knowledge-based design and simulation environment (KBDSE): foundational concepts and implementation," 1990. (verify exact title and venue.)
- Zss06: Zeigler, B. P., Sarjoughian, H. S., "Introduction to DEVS modeling and simulation with JAVA: developing component-based simulation models," 2006 (textbook; treats SES in Chapter on automated model construction). (verify edition.)
- WZS21: Wach, P., Zeigler, B. P., Salado, A., "Conjoining Wymore's Systems Theoretic Framework and the DEVS Modeling Formalism," *Applied Sciences* 11(11):4936, 2021. DOI 10.3390/app11114936.
- FPDZ22: Folkerts, H., Pawletta, T., Deatcu, C., Zeigler, B. P., "Automated, Reactive Pruning of System Entity Structures for Simulation Engineering," 2022. (verify venue; relevant for the runtime-pruning extension.)
- ACB v4: Wach, P., *AI Circuit Breaker Design Specification v4.0*, this repository.

---

## Section 1. SES formal definitions as stated by Zeigler

### 1.1 What the SES is

The System Entity Structure (SES) is a structural-knowledge representation that organizes a *family* of system specifications and their decompositions over a tree of declarative relations. Originating in the Rozenblit-Zeigler collaboration in the mid-1980s (RZ85, RZ90) and elaborated systematically in ZPK00 Chapter 4 and ZMK18 (verify ZMK18 chapter), SES is the apparatus that complements DEVS in the Zeigler tradition: DEVS gives the *atomic* and *coupled* model specifications; SES gives the *family of candidate model structures* from which a specific DEVS coupled model is *pruned*.

The two-step pattern is canonical:

1. Specify the SES tree representing the family of admissible system structures.
2. *Prune* the SES, selecting one entity per specialization choice and one aspect per multi-aspect choice, to obtain a Pruned Entity Structure (PES).
3. *Synthesize* the PES against a Model Base (MB) of atomic and coupled DEVS models, producing a hierarchical executable DEVS coupled model.

The SES + MB framework is sometimes called SES/MB in the literature (FPDZ22). The SES is the design-space declaration; the PES is one design instance; the model is the executable artifact.

### 1.2 The three primitive node types

An SES is a labeled tree in which every node carries a *mode* drawn from the set {entity, aspect, specialization}. The semantics:

- **Entity**: a system or sub-system that names a real or potential thing. Entities are the "what is decomposed or specialized" nodes. A leaf entity corresponds (typically) to an atomic DEVS in the model base.
- **Aspect**: a labeled *decomposition relation* between a parent entity and its children entities. An aspect declares: "this entity decomposes, in this aspect, into the following sub-entities." Different aspects of the same entity are *different decompositions* (different views), not different parts.
- **Specialization**: a labeled relation expressing *alternative choices* the entity can take. A specialization declares: "this entity can be one of the following specific kinds." Different children under a specialization are mutually exclusive: pruning selects one.

ZPK00 Chapter 4 (verify section) and the Systemspedia / MS4 Systems reference materials state the formal axioms of SES as a labeled tree:

**Axiom 1 (Uniformity).** Any two nodes with the same label have identical attached variable types and isomorphic subtrees. (One SES name, one structural meaning, globally.)

**Axiom 2 (Strict hierarchy).** No label appears more than once down any path from root to leaf. (No path is circular in name.)

**Axiom 3 (Alternating mode).** Each node has a mode in {entity, aspect, specialization}. The root has entity mode. If a node has entity mode, then its children have aspect or specialization mode. If a node has aspect or specialization mode, then its children have entity mode. (Modes alternate between entity and {aspect, specialization}.)

**Axiom 4 (Valid brothers).** No two children of the same parent have the same label. (Sibling labels are unique.)

**Axiom 5 (Attached variables).** No two variable types attached to the same node have the same name. (Local variable names are unique.)

**Axiom 6 (Inheritance).** Every entity in a specialization inherits all the variables, aspects, and specializations from the parent of the specialization. (Specializations are subtypes; they inherit.)

These six axioms make the SES a well-formed labeled tree with mode-alternation and inheritance semantics. They are the Zeigler-tradition analog of an OWL ontology with a constrained schema (the SES literature predates OWL but maps cleanly onto it).

### 1.3 Multi-aspect and multi-specialization

Two structural elaborations on the three primitive modes that ZPK00 and ZMK18 treat as distinct:

- **Multi-aspect.** A *multi-aspect* is an aspect whose component children are all of the same kind (same labeled entity type), differing only in instance count, index, or parameter values. A multi-aspect declares a *collection* of homogeneous components: "this entity decomposes in this aspect into N copies of entity-of-type-T." The multi-aspect is the SES carrier for "the system has many of these" without enumerating them. The pruning operation must select the cardinality.

- **Multi-specialization.** Less commonly discussed but present in the apparatus (ZPK00 §4 verify): when a single entity admits *several orthogonal specialization axes*, the entity has multiple specialization children, each representing one axis (e.g., one for "power source," one for "operating mode"). The pruning operation selects one specialization per axis. The orthogonality is what distinguishes multi-specialization from a single specialization with many alternatives.

### 1.4 The pruning operation

The **pruning operation** transforms an SES (a *family* of system structures) into a Pruned Entity Structure (PES, a *specific* system structure) by making the choices the SES leaves open. Per FPDZ22, Cheon-Kim, and ZPK00 Chapter 4, pruning consists of (at least):

- **At every specialization node**: select exactly one child entity (one specific kind).
- **At every aspect node**: select either to expand or to leave abstract (treat as a leaf for this pruning).
- **At every multi-aspect node**: select the cardinality (how many components) and the per-component parameters.
- **At every attached variable**: optionally bind to a specific value or leave parametric.

The result is a tree in which every node is either an entity-with-bound-aspect or a leaf entity. The PES is then synthesized against a Model Base of DEVS atomic and coupled models: each leaf entity is looked up in the MB and instantiated, and each aspect coupling is realized as DEVS coupling per the SES's coupling specification.

The pruning operation is the formal SES analog of *experimental setup selection*. Given an SES describing a family of possible system structures, a pruning declares "this is the structure I am instantiating right now." Different prunings of the same SES yield different DEVS coupled models, all of which are family members of the same SES.

### 1.5 The Model Base and SES/MB synthesis

The SES alone is structural; it does not contain executable behavior. The **Model Base (MB)** is a repository of atomic DEVS and coupled DEVS models, indexed by the entity labels that the SES uses. The synthesis step takes a PES and looks up each leaf entity in the MB, retrieving the corresponding DEVS atomic model, and assembles a hierarchical coupled DEVS model whose structure mirrors the PES.

The MB is the "library of model implementations" that the SES "language of model structures" composes. ZPK00 calls the joint object SES/MB and treats it as the proper unit of model-family specification.

### 1.6 SES and DEVS: the mapping

The SES-to-DEVS mapping is direct and well-typed:

- An **entity** at the leaf of a PES corresponds to a DEVS atomic model retrieved from the MB.
- An **entity** with an active (un-leafed) **aspect** corresponds to a DEVS coupled model whose components are the children entities of the aspect and whose couplings are declared by the aspect specification.
- A **specialization** choice does not appear in the DEVS model; it has been resolved by pruning before synthesis.
- A **multi-aspect** with cardinality N corresponds to a DEVS coupled model with N component instances of the same atomic or coupled model.

The SES is therefore a *meta-DEVS* specification: it specifies the DEVS coupling structure abstractly, and pruning concretizes the abstraction into an executable DEVS coupled model.

### 1.7 SES and the Experimental Frame

The relationship between SES and EF is the key formal link this document needs to make explicit. From ZPK00 Chapter 4 and the broader SES literature (verify section), the connection is structural:

- An SES can be defined for the SUT (system under study) or for the EF (experimental frame) or for both as separate trees coupled at synthesis time.
- An SES of EFs declares a *family of frames*: a tree of (G, A, T) triples where the generator, acceptor, and transducer are each entities that can be specialized.
- Pruning an SES of EFs yields a specific EF (a PES of frames), which then participates in the standard frame-and-system coupling pattern of EF semantics.

In other words: **the EF apparatus operates on one (model, frame) pair; the SES apparatus operates on the *family* of (model, frame) pairs.** A single deployment is one PES; a family of deployments is an SES. This is the structural feature the AI Circuit Breaker context construct needs that the EF alone cannot supply.

### 1.8 The hierarchy of system specifications and SES

The hierarchy of system specifications (Levels 0 through 4, ZPK00 §1.3, ZMK18 §1.5; see `../02_devs_experimental_frame.md` §1.6) gives five levels of structural commitment. SES sits across all five levels: an entity in an SES can carry attached variables describing its I/O ports (Level 0), its behavior set (Level 1), its I/O function (Level 2), its state transition (Level 3), or its coupling (Level 4). The SES is therefore a *cross-cutting* organizing apparatus: it can carry families of systems at any level of the hierarchy.

Z23 makes this explicit: the paper extends the hierarchy of system morphisms with an SES-abstraction layer, formalizing how SES sits one level up from the System Specification Hierarchy as a structural-knowledge-representation layer that organizes families of system specifications at each lower level.

---

## Section 2. SES morphisms and abstraction operations

### 2.1 SES homomorphisms: the canonical move

In the DEVS-tradition way of working, every level of the System Specification Hierarchy has a notion of morphism (Level 1: I/O behavior morphism; Level 3: state-transition homomorphism; Level 4: coupled-system morphism with component-wise mapping plus coupling preservation). Z23 extends this hierarchy with an **SES-abstraction layer** in which morphisms operate on SES trees themselves.

The canonical SES morphism is a label-preserving tree mapping that respects mode and structure:

**Definition (informal, Z23-style).** An SES morphism phi : SES_1 -> SES_2 is a mapping from the nodes of SES_1 to the nodes of SES_2 that:
1. preserves mode (entity to entity, aspect to aspect, specialization to specialization),
2. preserves the parent-child relation (children map to children, parent maps to parent),
3. respects attached-variable types up to a stated type morphism,
4. respects specialization inheritance.

Different SES morphisms admit different "looseness" in conditions 3 and 4, giving a graded notion of SES morphism quality analogous to the degree-of-homomorphism construct (CSER 2025) at the system-specification level.

### 2.2 Three kinds of SES-level morphism the AI Circuit Breaker question needs

For the construct under study (certified context vs. operational context), three SES-level morphisms are particularly relevant:

**(2.2.1) Specialization morphism.** Move from a more general entity to a more specific specialization choice. Formally, a specialization morphism phi_spec : SES_general -> SES_specific is the SES analog of a *specialization arrow* that selects one specialization child. Iterated, specialization morphisms walk down the SES toward leaves. The certified context corresponds to a particular specialization path; the operational context may correspond to a different specialization path.

**(2.2.2) Aspect morphism.** Move from one aspect of an entity to a different aspect of the same entity. An aspect morphism phi_asp : SES_aspectA -> SES_aspectB relates two alternative *decompositions* of the same entity. This is the SES carrier for "the same system viewed differently": the certified-frame view of Z_real might decompose along one aspect; the operational-frame view of Z_real might decompose along a different aspect of the same Z_real.

**(2.2.3) Pruning equivalence and pruning morphism.** Two prunings of the same SES that yield *isomorphic* DEVS coupled models after MB synthesis are pruning-equivalent. The *pruning morphism* is a structure-preserving mapping between PESes that are not necessarily identical but are equivalent under the MB. ZPK00 Chapter 4 treats this informally; FPDZ22 and ZKZ24 formalize the morphism content further. (verify ZKZ24 §3 for the pruning-morphism formalization; the abstract suggests the paper does develop a homomorphism-on-SES construct.)

### 2.3 Z23's MetaSES extension

Z23 proposes a **MetaSES** abstraction: an SES *of SESes*, sitting one level up from any individual SES. The MetaSES allows the apparatus to talk about *classes* of SESes (e.g., the class of all SESes whose root entity is of a given specialization, or whose multi-aspect cardinality lies in a given range). The MetaSES extension is what permits the hierarchy of system morphisms to ascend above the SES layer into a class-of-SES layer.

For the AI Circuit Breaker, this matters because: the *certified* SES is one SES (with one set of pruning options for one model base); the *operational* SES may be a different SES (different model base, different specializations, different aspects). The MetaSES is the apparatus that lets us write a morphism *between two SESes*, not just within an SES.

### 2.4 SES abstraction operations from ZKZ24

ZKZ24 develops base-lumped model pairs: given an SES describing a high-resolution "base" model and another SES describing a low-resolution "lumped" model, the homomorphism between them is what justifies the use of the lumped model as a faithful low-resolution surrogate for the base. The paper identifies principles ("homogeneity of structure and coupling") that justify the construction of such pairs.

In SES vocabulary, the base SES and the lumped SES are related by an **abstraction morphism**: the lumped SES is obtained from the base SES by *collapsing* multi-aspect nodes (lumping component populations into aggregate entities), *coarsening* attached variable types, and *retaining* the same specialization structure. ZKZ24 gives examples in brain simulation, combat attrition, and Pascal's triangle (the last as a complexity-reduction demonstration).

This is directly relevant to the AI Circuit Breaker. The certified Z_real(cert) and the operational Z_real(op) are not necessarily at the same resolution. The certification may have been performed on a high-resolution model; the operational deployment may run against a lumped surrogate (or vice versa). The base-lumped homomorphism is then the structural carrier for the context relationship.

### 2.5 Distance between SES nodes

The candidate notion of "distance between SES nodes" the brief asks about is well-defined under Z23 and the broader SES morphism literature:

- *Specialization distance*: the number of specialization steps separating two entities. Discrete, integer-valued.
- *Aspect distance*: the number of aspect-morphism steps separating two decompositions of the same entity.
- *Pruning distance*: under the equivalence classes of Section 2.2.3, the number of pruning operations needed to transform one PES into another.
- *Abstraction distance*: under ZKZ24, the degradation of the homomorphism between two SESes related by lumping or coarsening, measured by the degree-of-homomorphism (sigma) on the SES morphism itself.

These four are not isomorphic; they capture different kinds of SES-tree movement. The right one for "context distance" in the AI Circuit Breaker depends on what *kind* of context shift the deployment is undergoing (Section 3 develops this).

---

## Section 3. SES treatment of context

### 3.1 The five candidate ways SES might encode context

The brief asks whether SES encodes context as:
(a) two prunings of the same SES,
(b) two specializations under a common SES entity,
(c) two SES trees connected by an SES morphism,
(d) the aspect coordinate of the SES (alternative decompositions),
(e) a formal "context pruning" or "context specialization" operation.

Each maps to a different formal claim about the deployment situation. The five are not mutually exclusive; the AI Circuit Breaker likely needs all five, at different layers. Section 3.2 through 3.6 develop each.

### 3.2 (a) Context as two prunings of the same SES

**Claim.** The certified context and the operational context are two distinct PESes obtained by pruning the same SES.

**When this holds.** When the certification has declared an SES (a family of admissible system-and-frame structures) and both certified and operational deployments are within that family. The certification covers the family; the certified PES is the specific deployment validated at certification time; the operational PES is the specific deployment running now. Both are pruning instances of the same SES.

**Formal expression.** Let SES be the certified SES. Let pi_cert : SES -> PES_cert and pi_op : SES -> PES_op be two prunings. Then the context relationship is the pair (pi_cert, pi_op), and the *context discrepancy* is a pruning-distance d_prune(PES_cert, PES_op) measured per Section 2.5.

**Strength.** This is the cleanest and most operationally tractable case. It is the case the certification regime can promise: "we certify this SES; the deployment must be a pruning of this SES." Out-of-context is then formally "the operational PES is not a pruning of the certified SES," which is decidable.

**Limitation.** Requires the certification to declare an SES, not just a single PES. This is a heavier certification burden than current practice. The trade-off is that the heavier burden buys decidable in-context vs. out-of-context.

### 3.3 (b) Context as two specializations under a common SES entity

**Claim.** The certified and operational contexts are two *specialization children* of a common entity in the SES.

**When this holds.** A special case of (a): both PESes share their entire structure except at one specialization node, where they make different choices. The specialization axis is the "context coordinate."

**Formal expression.** Let entity E in the SES have specialization children E_1, E_2, ..., E_n. Let PES_cert select E_i and PES_op select E_j. The context is the specialization choice at E; the context discrepancy is the specialization morphism between E_i and E_j (if E_i and E_j are siblings under the same specialization axis, the morphism is trivial and the discrepancy is binary; if a richer structure relates E_i and E_j, the discrepancy is richer).

**Strength.** This is the SES carrier for "the same task family, different operating regime." E might be "patient population," with E_1 = adult cardiology (certified) and E_2 = pediatric cardiology (operational). The certified SES declares both as specializations; the deployment-time discrepancy is a single specialization-choice mismatch.

**Use case.** This formulation gives the ECG-vs-pediatric example of `Dr_construct_analysis_v0.1.md` §2.2 a precise SES home: the discrepancy is exactly a specialization-choice mismatch at the "patient population" specialization node.

### 3.4 (c) Context as two SES trees connected by an SES morphism

**Claim.** The certified context and the operational context are two *distinct* SES trees, related by an SES morphism (or MetaSES morphism per Z23).

**When this holds.** When the operational deployment is not within the certified SES family at all but is "nearby" in MetaSES space: a different model base, a different decomposition pattern, but with enough structural commonality that a morphism SES_cert -> SES_op exists.

**Formal expression.** Let SES_cert and SES_op be two distinct SESes. Let phi : SES_cert -> SES_op be an SES morphism per Section 2.1. The context discrepancy is measured by the degree of homomorphism of phi (Section 2.5 abstraction distance), giving an SES-level (D_s, D_b)-like quantity.

**Strength.** This is the most general case. It admits situations the certification did not anticipate at the SES level (not just at the pruning level). It is also the SES analog of the categorical fibration reindexing functor F(u) in `../04_categorical_synthesis.md`: F(u) maps fibers, where each fiber is an SES.

**Limitation.** "An SES morphism exists" is necessary; if no such morphism exists, then the operational deployment is *fundamentally* out of scope, and the formalism is signaling that the certification cannot be transferred. This is the strongest form of out-of-context: not "in a different pruning" but "in a different family entirely." The right runtime response is then to *halt*, not to *adjust*, which is exactly the AI Circuit Breaker's role.

### 3.5 (d) Context as the aspect coordinate of the SES

**Claim.** Context is the *aspect choice*: two contexts are two aspect-morphism-related decompositions of the same entity.

**When this holds.** When the underlying entity is the same in both contexts but the *decomposition* relevant to certification differs from the decomposition relevant to operation. Example: the AI was certified using a decomposition that exposes the input-feature-vector and the prediction (a black-box aspect); the operation must contend with a decomposition that exposes the internal feature representations and the attention weights (a white-box aspect for monitoring).

**Formal expression.** Let entity E in the SES have aspects A_1, A_2, ..., A_m. The certification uses aspect A_i; the operation uses aspect A_j. The context relationship is the aspect morphism between A_i and A_j (Section 2.2.2), and the context discrepancy is the structural mismatch between the two decompositions.

**Strength.** This is the SES carrier for "the certification covers the system at one resolution but the operation requires monitoring at a different resolution." It is the aspect-decomposition analog of base-lumped pairs (ZKZ24): A_i is the lumped aspect, A_j is the base aspect.

**Use case.** AI Circuit Breaker runtime monitoring at a finer aspect than certification time. The certification was at the coarse aspect (input-output behavior); the runtime monitor at the fine aspect (state trajectory). The aspect morphism between them gives the formal expectation: "what the fine aspect should report when the coarse aspect is in-spec."

### 3.6 (e) A formal "context pruning" or "context specialization" operation

**Claim.** SES has a primitive operation that *selects context* by pruning at the context coordinate.

**When this holds.** When the SES is constructed so that one of its specialization axes is explicitly the "context axis," and pruning along that axis is the operation that selects a deployment context.

**Formal expression.** Construct SES so that the root entity E_root has at least one specialization with children E_root[c_1], E_root[c_2], ..., E_root[c_n] indexed by context c. Pruning at that specialization is *context selection*. The certified deployment is pi_cert with c = c_cert; the operational deployment is pi_op with c = c_op.

**Strength.** This is the constructive SES analog of the Wymore-B parameter family Z_real(c) in `../synthesis_debate.md` §2.1. Wymore-B treats c as an index over a family; SES treats c as a specialization axis. The constructions are isomorphic; SES gives the family a structured tree representation rather than an arbitrary index set.

**Recommendation.** This is the formulation the AI Circuit Breaker should adopt as the *standard SES design pattern*. It declares context as a first-class specialization axis of the SES, with the certification artifact being the SES and the certified specialization-path c_cert, and the operational artifact being the operational specialization-path c_op. The discrepancy at runtime is then a *specialization-distance* per Section 2.5.

### 3.7 Synthesis: the layered context construct in SES vocabulary

The five candidate formulations (a)-(e) are not competitors; they are different SES-level operations on different SES coordinates:

| Formulation | What varies | SES coordinate | Operation |
|---|---|---|---|
| (a) Two prunings of same SES | Pruning choices | All specialization + aspect + multi-aspect choices | Pruning distance |
| (b) Two specializations | Specialization choice at one node | One specialization axis | Specialization morphism |
| (c) Two SES trees + SES morphism | Whole-SES structure | The full SES tree | SES morphism (MetaSES) |
| (d) Aspect coordinate | Aspect choice at one node | One aspect axis | Aspect morphism |
| (e) Context-pruning | Specialization at the designated context axis | Designated context axis | Specialization morphism on the context axis |

The recommendation: use **(e) as the design pattern** for declaring context, with **(b) as the runtime mechanism** for specialization-choice mismatches, **(d) as the runtime mechanism** for monitoring-aspect mismatches, **(a) as the certification predicate** (pruning of same SES is in-family), and **(c) as the escalation predicate** (different SES is fundamentally out of family). All five contribute; none is sufficient alone.

This is the **SES-native layered context construct**. It supplies what the EF alone cannot: a structured *family* of contexts with multiple coordinates of variation and morphism-based discrepancy measurement on each coordinate.

---

## Section 4. SES + EF combined for context

### 4.1 The standard Zeigler-tradition combination

The combination of SES (organizing families of models) with EF (specifying the experiment under which a model is valid) is the canonical Zeigler-tradition move for model-family analysis. Per ZPK00 Chapter 4 and ZMK18 (verify chapter), the combined apparatus is:

- An **SES of EFs**: a tree of experimental frames, where entities are EFs, specializations are alternative EF types (e.g., training-EF vs. operational-EF vs. shadow-EF), aspects are alternative decompositions of an EF into its (G, A, T) components.
- An **SES of SUTs**: a tree of systems under study, decomposing them into components and specializations.
- A **coupling SES**: a tree that pairs SES-of-EFs prunings with SES-of-SUTs prunings, specifying which frames are valid for which models.

Pruning the joint apparatus yields a specific (frame, model) pair: one PES of EFs coupled with one PES of SUTs. The validity assertion is then "this PES of model is valid in this PES of frame," in the standard EF sense.

### 4.2 SES + EF as the formal context specification

The combination is what gives a *complete formal context specification* in the Zeigler tradition. Specifically:

- The SES of EFs declares the *family of admissible experimental contexts*.
- The SES of SUTs declares the *family of admissible models*.
- The coupling SES declares the *valid (frame, model) pairings*.
- The pruning of the joint apparatus declares the *specific deployment instance*.

For the AI Circuit Breaker:

- **Certification artifact**: the joint SES (SES of EFs + SES of SUTs + coupling SES), together with the certified pruning (PES_cert).
- **Operational artifact**: the operational pruning (PES_op).
- **Out-of-context predicate**: "PES_op is not a valid pruning of the certified joint SES."
- **Context discrepancy**: an SES-morphism quality measure (Section 2.5) on the pair (PES_cert, PES_op).

### 4.3 "Out of context" as EF-pruning mismatch

The brief asks whether "out of context" is the situation where the EF assumed by the AI corresponds to one pruning of the SES while the operational EF corresponds to a different pruning. The answer is: **yes, this is exactly the SES formalization of the failure mode.**

Specifically:

- The AI was certified under E_train, which is the pruning PES_EF_cert of the SES of EFs.
- The AI is operating under E_op, which is the pruning PES_EF_op of the same SES of EFs.
- If PES_EF_cert == PES_EF_op (same pruning, same EF instance), the AI is *in context*.
- If PES_EF_cert and PES_EF_op are distinct prunings of the same SES, the AI is *in family but out of pruning*; the SES-pruning distance measures the discrepancy.
- If PES_EF_cert and PES_EF_op are not both prunings of the same SES, the AI is *out of family*; the deployment is fundamentally outside the certified scope.

This is the layered failure-mode characterization that the EF alone cannot supply because the EF apparatus operates on one (model, frame) pair, not on the family.

### 4.4 Structural and distributional axes of context match

The prior synthesis (`../synthesis_debate.md` §5.4) reaches for a two-axis context-match construct (Sigma_ctx = (sigma_struct, sigma_dist)) that parallels the structural-behavioral pairing (D_s, D_b) at the morphism-quality level. The SES + EF combination supplies both axes natively:

- **Structural axis (sigma_struct)**: SES-morphism quality between PES_cert and PES_op. Tree-structural mismatch in specialization choices, aspect choices, multi-aspect cardinalities, attached-variable bindings.
- **Distributional axis (sigma_dist)**: the EF-generator distance d_G between G_cert and G_op, formalized per `../02_devs_experimental_frame.md` §3.2.1. This is the input-distribution shift the certified frame does not anticipate.

The two axes are orthogonal in the same sense that (D_s, D_b) are orthogonal: structural (set-theoretic, tree-morphism) and distributional (probabilistic, divergence on input space). The SES + EF apparatus is the combined home for both:

- SES handles structural variation (specialization, aspect, pruning); morphism quality is the structural axis.
- EF handles distributional variation (generator distance, acceptor margin, transducer calibration); generator distance is the distributional axis.

### 4.5 The SES + EF complete context specification

Putting Sections 4.1 through 4.4 together, the complete SES + EF context specification for the AI Circuit Breaker is:

    Context_spec_cert = (SES_joint, PES_cert, attached EF triple E_cert = (G_cert, A_cert, T_cert) at the EF-leaf of PES_cert)

The triple is:
- SES_joint: the certified family of (model, frame) pairs.
- PES_cert: the certified specific instance.
- E_cert: the specific EF associated with PES_cert.

At runtime:

    Context_obs_op = (PES_op, E_op = (G_op, A_op, T_op))

The operational observation is the pair (PES_op, E_op). The context discrepancy is then:

    d_context = (d_SES(PES_cert, PES_op), d_EF(E_cert, E_op))

where d_SES is the SES-morphism quality between PES_cert and PES_op (Section 2.5), and d_EF is the EF triple distance (`../02_devs_experimental_frame.md` §3.6).

**This is the complete two-axis context construct in SES + EF vocabulary.** Structural axis = d_SES; distributional axis = d_EF (and especially its d_G component). The CSER 2025/2026 (D_s, D_b) two-axis morphism-quality construct is preserved; the SES + EF apparatus adds a *second* two-axis construct, at the context level rather than the morphism level. The architecture is self-similar: structural and distributional axes appear at the morphism level (D_s, D_b) and at the context level (d_SES, d_EF).

---

## Section 5. Compatibility with the Bayesian SE draft framework

### 5.1 What the Bayesian SE draft framework already has

The user's current Bayesian SE draft (under revision; not duplicated here, as a parallel agent is reading it directly) deploys:

- The hierarchy of system specifications per Zeigler (Levels 0 through 4).
- Morphisms at each level, characterized as "neighborhoods of approximation" per Zeigler 2018 and 2019, with explicit extension via Z23 to the SES-abstraction layer.
- **io observation-frame morphisms**, which are EF-level (Level 0 or Level 1) morphisms that relate observation frames. These are what the draft calls "context morphisms": morphisms between the frames under which the system is observed.
- **NS coupled-system morphisms**, which are Level-4 (Network Specification / coupled-system) morphisms. These relate coupled-system structures.
- A **quad relationship**, presumably a commuting square (or two-cell) relating the io observation-frame morphism, the NS coupled-system morphism, and the underlying system-and-state-transition morphisms in a single diagram. (verify against the draft text; parallel agent will report.)

### 5.2 How SES integrates with this framework

The integration is natural and conservative. SES does not displace any element of the Bayesian SE draft; it provides the *family-level* apparatus that the draft's morphism chains traverse. Specifically:

**(5.2.1) SES organizes the family of contexts.** The Bayesian SE draft's io observation-frame morphism is a *single* arrow between two observation frames. The SES of EFs is the *tree of observation frames* over which such arrows are drawn. Each pruning of the SES gives one observation frame; the io observation-frame morphism is the arrow between two such prunings. SES therefore *organizes* the family that the io morphism *traverses*.

**(5.2.2) SES specialization corresponds to context morphism.** When the draft writes a context morphism between two observation frames, the SES interpretation is: the two observation frames are two specialization children (or two aspect children, or two prunings) of a common SES entity. The context morphism is then a *specialization morphism* (or aspect morphism, or pruning morphism) per Section 2.2 of this document. The draft's context morphism need not be re-derived; the SES gives it a *structural type* (specialization vs. aspect vs. pruning).

**(5.2.3) The Bayesian network's nodes can be SES prunings.** The draft's Bayesian network, presumably with nodes representing system states or system instances, can be reinterpreted with nodes representing *SES prunings*. Each node is a specific PES; edges in the Bayesian network are SES-morphism arrows (or transition probabilities between PESes). This gives the Bayesian network a structural typing of its nodes that pure "abstract system states" cannot supply. The probabilities then become probabilities over which pruning is the active deployment context, rather than abstract beliefs over abstract states.

This last move is potentially the strongest integration. It says: the Bayesian SE draft's network is not a network of *belief states about a single system*; it is a network of *belief states over which SES pruning is the active deployment*. The hidden variable being inferred is "which context, in the SES sense, is the deployment in." This recasts the inference problem as a structured *context-identification* problem: given runtime observations, infer the posterior distribution over SES prunings.

**(5.2.4) The quad relationship.** Whatever the draft's quad relationship is (verify against draft), the SES extension is: each corner of the quad is parameterized by an SES pruning, and the quad commutes for some pairs of prunings and fails to commute (or commutes with degradation) for others. The SES-level commuting condition is then a *family of quad commutations*, one per pruning. The quad commutation defect under context shift is the structural carrier of the AI Circuit Breaker failure mode.

### 5.3 The draft's morphic chain traverses an SES

A direct prediction this document makes about the Bayesian SE draft: the morphic chain (the sequence of morphisms relating the AI, the certified system, the operational system, and the observation frames) traverses an SES that the draft does not currently make explicit. Making the SES explicit gives the chain a structured family-level home: each link in the chain is a movement along an SES axis (specialization, aspect, pruning, or abstraction), and the chain composition law inherits from the SES-morphism composition.

This is conservative: nothing the draft proves is invalidated; the SES extension provides the *family-level scaffolding* that the chain is implicitly traversing. The parallel agent reading the draft should be able to map each step of the morphic chain to an SES movement; if not, that mapping is the open extension this document is recommending.

### 5.4 Specific suggestions for the Bayesian SE draft (subject to the parallel agent's report)

Provisional, pending the parallel agent's read:

1. Declare the SES the draft is implicitly using. State the entities, aspects, specializations, and multi-aspects relevant to the AI deployment context.
2. Type each context morphism in the draft as one of: specialization morphism, aspect morphism, pruning morphism, abstraction morphism (ZKZ24-style).
3. Type the Bayesian network's nodes as SES prunings (not abstract system states). State the prior distribution over prunings explicitly.
4. State the quad relationship as a family of quad commutations indexed by SES pruning. Identify the prunings under which the quad commutes exactly and those under which it commutes with degradation.
5. Connect the morphic chain to a *path through the SES*. Each link is an SES movement; the chain length is the SES path length.

These suggestions are extension-only; they do not require changes to the existing morphisms or their characterization as "neighborhoods of approximation." The SES is the structural-knowledge layer above the morphisms.

---

## Section 6. Updated recommendation contribution

### 6.1 What SES adds to the prior synthesis's recommendation

The prior synthesis (`../synthesis_debate.md` §5) proposed a five-layer recommendation:
- Layer 1 (Wymore-A): Foundational declaration of Dom(h_cert).
- Layer 2 (DEVS/EF): Operational decomposition into (G, A, T).
- Layer 3 (Wymore-B / categorical): Theoretical extension to parameter family / fiber.
- Layer 4 (Friston / broader): Distributional axis (free energy).
- Layer 5 (Rosen / Pattee): Diagrammatic lineage.

SES contributes to and modifies this stack as follows.

**(6.1.1) SES is the constructive procedure for Layer 1's Dom(h_cert) declaration.** Wymore-A declares Dom(h_cert) as a set-theoretic restriction. SES gives a *structured tree representation* of that declaration: Dom(h_cert) is the set of pruning instances of the certified SES, with specialization choices and aspect choices and multi-aspect cardinalities all enumerated. The "declare Dom(h)" recommendation of Layer 1 becomes constructive: *declare the SES*, and Dom(h) is the family of its prunings. This is the constructive procedure the prior synthesis did not specify.

**(6.1.2) SES gives Layer 3's parameter family Z_real(c) a structured tree representation.** Wymore-B treats c as an arbitrary index over a family of certified models. SES replaces "arbitrary index set" with "specialization axis of the SES." The family is then not free-form; it is the family of SES prunings along the context-specialization axis. This restricts the family to a structured form that the certification regime can declare, validate, and check at runtime.

The Layer 3 inter-fiber morphism g : Z_real(c_cert) -> Z_real(c_op) becomes the SES specialization morphism (Section 2.2.1) along the context axis. The categorical fibration of Layer 3 has its base category Ctx populated by SES prunings, with reindexing functors F(u) realized as SES-morphism applications. The set-theoretic Layer 3 and the categorical Layer 3 both inherit the structured tree representation; neither is invalidated.

**(6.1.3) SES handles the multi-agent / multi-component case better than fibrations alone.** The categorical fibration treats Sys as a category and Ctx as a category, with each fiber Sys_c a category of systems valid in context c. The multi-agent case requires a *product structure* on the fiber: many systems, many contexts, joint deployment. The fibration formalism handles this via the standard categorical apparatus (products, coproducts, limits) but does not declare which products are *engineering-canonical*.

SES handles the multi-agent case natively via **multi-aspect**: a multi-agent system is an entity with a multi-aspect that decomposes it into N copies of a per-agent entity. Pruning the multi-aspect selects the agent count and the per-agent parameters. The multi-agent context discrepancy is then a *multi-aspect cardinality mismatch* (certified for N agents, operating with N' agents) and a *per-agent specialization mismatch* (certified per-agent specialization vs. operational per-agent specialization).

This is more constructive than fibration alone. SES gives the multi-agent case a tree structure with named operations (multi-aspect cardinality, per-agent specialization) that the certification regime can declare, validate, and check. The fibration says "products exist"; SES says "here is the specific product, with named axes."

**(6.1.4) SES gives Layer 2's EF decomposition a family-level extension.** Layer 2 decomposes one EF as (G, A, T). The SES of EFs decomposes the *family of EFs* as a tree with G, A, T as aspects, and operating-regime specializations as the certification axes. The runtime EF-distance d_EF of Section 3 of `../02_devs_experimental_frame.md` becomes one specific d_EF on one specific PES of EFs; the SES gives the family-level structure over which such distances are computed.

**(6.1.5) SES is the apparatus the Bayesian SE draft is implicitly using.** Per Section 5.3, the draft's morphic chain traverses an SES. Making this explicit closes the gap between the draft's framework and the SES literature; it also gives the draft the constructive procedure for declaring the family of contexts.

### 6.2 Updated five-layer recommendation, with SES integration

The prior synthesis's five-layer recommendation, updated to integrate SES:

| Layer | Purpose | SES role |
|---|---|---|
| Layer 1 (Wymore-A) | Declare Dom(h_cert) | **SES is the constructive form**: Dom(h_cert) = family of prunings of the certified SES |
| Layer 2 (DEVS/EF) | Decompose one EF as (G, A, T) | **SES of EFs** gives the family-level decomposition over which one PES of EFs is selected |
| Layer 3 (Wymore-B / categorical) | Inter-fiber morphism on the parameter family | **SES specialization morphism** along the context axis is the parameter family's structured form |
| Layer 4 (Friston / broader) | Distributional axis | **EF-generator distance d_G** at the leaf of the SES of EFs; the distributional axis sits at the leaf of the structural axis |
| Layer 5 (Rosen / Pattee) | Diagrammatic lineage | The SES morphism diagram is the Rosen modeling-relation diagram at the family level |

The recommendation: **SES is the structural-knowledge-representation layer above the morphism layer.** Layers 1, 2, 3 all live inside the SES; Layer 4 is the distributional dimension at the leaf; Layer 5 is the cross-disciplinary lineage of the whole apparatus.

### 6.3 The minimal commitment for SES

For the AI Circuit Breaker design spec and the user's current Bayesian SE draft, the minimum commitment to import SES is:

**At the design-spec level:**
1. Declare the SES the certification artifact uses, with explicit entity / aspect / specialization / multi-aspect declarations. Treat this as a refinement of the Dom(h_cert) declaration of Layer 1.
2. Declare which specialization axis is the "context axis," with the certified specialization-path c_cert.
3. Declare the SES of EFs (separate from the SES of SUTs, coupled at synthesis time).

**At the Bayesian SE draft level:**
1. Add SES vocabulary as the structured form of the family the draft's morphic chain is traversing. (Section 5.3 above.)
2. Type each context morphism in the draft as specialization, aspect, pruning, or abstraction morphism.
3. Type the Bayesian network's nodes as SES prunings.

**At the journal extension level:**
1. State the formal SES + EF context construct (Section 4.5 above) with both structural and distributional axes.
2. Develop the SES morphism quality measure (Section 2.5) and connect it to the (D_s, D_b) morphism-quality measure via the WZS21 bridge.
3. State and prove the SES + EF chain bound theorem extending the W26 / CSER chain bound theorem to the SES-extended setting.

### 6.4 The single sharpest contribution of SES

If forced to one sentence: **SES is the apparatus that turns the "declare Dom(h)" recommendation of Layer 1 from a set-theoretic specification into a constructive tree of named, typed, and prune-able alternatives, and the same apparatus organizes the family of experimental frames (Layer 2), the parameter family of certified systems (Layer 3), and the family of structural axes against which the distributional axis (Layer 4) is computed at the leaf.**

The Wymore tradition declares the family. The DEVS / EF tradition runs one instance of the family. The categorical tradition reindexes between fibers. **SES is the tree that organizes all three.** It is the structural-knowledge backbone the AI Circuit Breaker construct under study has been reaching for.

---

## Section 7. Open questions and gaps

1. **ZKZ24 verification.** Section 2.4 cites ZKZ24 for base-lumped homomorphism pairs and abstraction morphisms. The 2024 paper is available (Sage / SIMULATION journal, DOI 10.1177/00375497241264834); a focused read of Section 3 and the brain-simulation example is recommended to confirm that the abstraction-morphism formalization is as Section 2.4 describes. The abstract suggests yes but I have not read the full paper.

2. **Z23 MetaSES verification.** Section 2.3 attributes the MetaSES construct to Z23 (Information vol. 14 issue 1 art. 22). The MDPI page confirms title and abstract; a focused read of the paper's Sections 3-5 is needed to verify the formal MetaSES definition this document uses. The MDPI page is reachable but returned 403 on initial WebFetch; the user or a future agent should retrieve the PDF directly. The brief cited as "Z22"; I have re-cited as Z23 because *Information* vol. 14 dates as a 2023 volume despite the December 2022 online publication.

3. **FPDZ22 verification.** Section 1.4 cites Folkerts-Pawletta-Deatcu-Zeigler 2022 for the pruning operation formalization. The DBLP entry confirms publication but I have not verified the exact title, venue, or pagination. This citation should be verified before external use. The 2022 paper is "Automated, Reactive Pruning of System Entity Structures for Simulation Engineering," published in Lecture Notes in Networks and Systems (verify volume) per DBLP.

4. **RZ85 and RZ90 verification.** Section 1.1 cites Rozenblit-Zeigler 1985 and Rozenblit-Hu-Kim-Zeigler 1990 as foundational SES papers. The 1985 paper title and venue need verification ("Concepts for knowledge-based system structure design overlays" is my best guess from the era; the actual foundational paper may have a different title). The 1990 paper exists in the Rozenblit-Zeigler archive at U Arizona (mbdl.arizona.edu/publications/pdfs/Rozenblit1990aa.pdf per search results) and should be retrievable for verification.

5. **SES axiom enumeration.** The six axioms of Section 1.2 are stated as canonical based on secondary sources (Systemspedia, MS4 Systems). ZPK00 Chapter 4 should be checked to confirm that all six are present with the wording given, and to identify any further axioms (some treatments add a coupling-specification axiom; some add a parameter-binding axiom). Verify against the printed text.

6. **SES of EFs literature.** Section 4.1 claims the SES + EF combination is canonical Zeigler-tradition. This is plausible but I have not found a specific source that explicitly develops "SES of EFs" as a named construct (the apparatus is implicit in ZPK00 Chapter 4 and natural under ZMK18, but the named construct may not be in the literature). If a published source exists, cite it; if not, the SES + EF combination of Section 4 is partially novel here. A literature search for "SES of experimental frames" or "experimental frame entity structure" would resolve this.

7. **Connection to ParaDEVS and agentic workflows.** `../02_devs_experimental_frame.md` §7 flagged this for Phase III. SES has the same question: if ParaDEVS extends DEVS to parallel branching state spaces, does the SES need a parallel-branching extension? Z23's MetaSES is one step toward this but does not yet address parallel branching of prunings at runtime. Reactive pruning per FPDZ22 is the relevant primitive.

8. **The Bayesian SE draft integration.** Section 5 makes provisional claims about how SES integrates with the draft. The parallel agent reading the draft should report (a) whether the morphic chain in the draft does indeed traverse an SES that can be declared, (b) whether the draft's io observation-frame morphism types as specialization / aspect / pruning / abstraction, (c) whether the Bayesian network nodes can be reinterpreted as SES prunings. The integration is conservative and extension-only; it should be checkable.

9. **Empirical SES instantiation on the ECG testbed.** The Phase I testbed (ECG, per the recommendation memo and the prior swarm) is a setting where an SES could be instantiated concretely: SES of patient populations, SES of input-signal types, SES of monitoring aspects, multi-aspect for multi-lead ECG. The d_SES quantity of Section 4.5 should be computable on that testbed alongside (D_s, D_b) and d_EF for a side-by-side three-quantity report. This is the empirical anchor that completes the SES + EF formulation.

10. **SES vs. ontology.** The SES literature predates OWL but maps onto a constrained-schema ontology. The portfolio's GI-JOE ontology infrastructure (per the user's project memory) is OWL-based with SHACL constraints. A natural cross-project bridge: the AI Circuit Breaker's SES could be encoded as an OWL ontology with SHACL constraints corresponding to the SES axioms (uniformity, strict hierarchy, alternating mode, valid brothers, attached variables, inheritance). This would give the SES a portable, validatable representation in the existing portfolio infrastructure. Worth scoping for a future session.

11. **SES vs. Wymore-Wallk five-dimensional taxonomy.** The Wallk WHO/WHAT/WHEN/WHERE/WHY taxonomy (mentioned in `../synthesis_debate.md` §7) is a candidate population of Layer 1's profile schema. SES gives a structured tree that subsumes the Wallk taxonomy: each Wallk dimension can be a specialization axis of the SES, with values as specialization children. The SES is therefore a generalization of Wallk; ODD taxonomies (PAS 1883) and Klir-style source-system tuples (broader §3) can be similarly absorbed. This is the SES's "absorbs the existing taxonomies" feature.

12. **Naming.** The brief asks about formal "context pruning" or "context specialization" operations. Section 3.6 recommends (e) as the design pattern: context is a designated specialization axis. The name for this operation should be settled: "context specialization," "context pruning," or "context selection." The Zeigler-tradition-native name would likely be "context specialization at the context axis," shortened to "context specialization" in conversational use. The user should choose.

---

## Section 8. References

(Citation format follows IEEE per project default. Items with `(verify)` need confirmation before external use.)

[1] B. P. Zeigler, H. Praehofer, and T. G. Kim, *Theory of Modeling and Simulation*, 2nd ed. San Diego, CA, USA: Academic Press, 2000. (Chapter 4 develops SES at book-length; canonical reference.)

[2] B. P. Zeigler, A. Muzy, and E. Kofman, *Theory of Modeling and Simulation: Discrete Event & Iterative System Computational Foundations*, 3rd ed. London, UK: Academic Press, 2018. (verify SES chapter location in 3rd ed.; some material was reorganized from 2nd ed.)

[3] B. P. Zeigler, "Extending the Hierarchy of System Specifications and Morphisms with SES Abstraction," *Information*, vol. 14, no. 1, art. 22, 2023. DOI: 10.3390/info14010022. (Published online 29 Dec 2022; cites as 2023 issue. The brief named this "Z22"; this document re-cites as Z23 because the journal volume is 14, 2023.)

[4] B. P. Zeigler, C. Koertje, and C. Zanni, "The utility of homomorphism concepts in simulation: building families of models from base-lumped model pairs," *Simulation*, vol. 100, no. 12, pp. 1181-1196, 2024. DOI: 10.1177/00375497241264834.

[5] J. W. Rozenblit and B. P. Zeigler, "Concepts for knowledge-based system structure design overlays," in *Proc. IEEE Conf. Systems, Man, and Cybernetics*, 1985. (verify exact title and venue; this is the foundational SES paper in the Rozenblit-Zeigler collaboration. Cited from secondary sources; original venue should be confirmed.)

[6] J. W. Rozenblit, J. Hu, T. G. Kim, and B. P. Zeigler, "Knowledge-based design and simulation environment (KBDSE): foundational concepts and implementation," 1990. (verify exact title and venue. PDF retrievable from mbdl.arizona.edu/publications/pdfs/Rozenblit1990aa.pdf.)

[7] B. P. Zeigler and H. S. Sarjoughian, *Guide to Modeling and Simulation of Systems of Systems*. London, UK: Springer, 2013. (verify edition and year. Contains "Pruning SES List" chapter referenced in this document.)

[8] H. Folkerts, T. Pawletta, C. Deatcu, and B. P. Zeigler, "Automated, Reactive Pruning of System Entity Structures for Simulation Engineering," in *Lecture Notes in Networks and Systems*, vol. (verify), 2022. (DBLP confirms publication; venue volume needs verification.)

[9] P. Wach, B. P. Zeigler, and A. Salado, "Conjoining Wymore's Systems Theoretic Framework and the DEVS Modeling Formalism: Toward Scientific Foundations for MBSE," *Applied Sciences*, vol. 11, no. 11, art. 4936, 2021. DOI: 10.3390/app11114936.

[10] P. Wach et al., "Toward a Library of Isomorphic Patterns for Systems Engineering," *Conf. Syst. Eng. Research (CSER)*, 2026. (Two-axis isomorphic-degradation framework; this document references the D_s, D_b construct from this paper as the morphism-quality construct that SES extends at the family level.)

[11] P. Wach and A. Salado, "Can Wymore's Mathematical Framework Underpin SysML?," *Procedia Computer Science*, 2019. (verify volume and pagination.)

[12] A. W. Wymore, *Model-Based Systems Engineering*. Boca Raton, FL, USA: CRC Press, 1993.

[13] Y. K. Cheon and T. G. Kim, "DEVS model composition by system entity structure," *Proc. SpringSim*, 2008. (verify exact venue. Referenced for the SES-to-DEVS coupled model synthesis procedure.)

[14] Systemspedia, "System Entity Structure" entry, http://systemspedia.org/entry.aspx?entry=3423 (URL returned 404 on direct fetch 2026-05-20; SES axiom enumeration confirmed via cached secondary sources. Original entry attributable to the Zeigler / ACIMS group.)

[15] MS4 Systems, "System Entity Structure" documentation, http://www.ms4systems.com/pages/devs/ses.php (verify URL availability; consulted as secondary reference for SES + MB synthesis procedure.)

[16] P. Wach, *AI Circuit Breaker Design Specification v4.0*, this repository. `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Design_Spec_v4.md`.

[17] Internal repository documents:
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/01_wymore_native.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/02_devs_experimental_frame.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/03_broader_systems_theory.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/04_categorical_synthesis.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/synthesis_debate.md`

---

## Closing note

The System Entity Structure is the Zeigler-tradition apparatus that the AI Circuit Breaker context construct has been reaching for at the family level. The DEVS Experimental Frame specifies one context for one model; the SES specifies the *space of contexts and models* over which morphisms, pruning, and abstraction operate. The user's Bayesian SE draft already deploys the hierarchy of system specifications with io observation-frame morphisms and NS coupled-system morphisms; SES is the structural-knowledge layer above that hierarchy. The five candidate ways SES might encode context (Section 3) are not competitors; they are different SES-level operations on different SES coordinates, and the layered construct of Section 3.7 uses all five.

The single sharpest claim: SES is the apparatus that turns "declare Dom(h)" from set-theoretic specification into constructive tree-of-named-alternatives, and the same apparatus organizes the family of experimental frames, the parameter family of certified systems, and the structural axes against which the distributional axis is computed at the leaf. The CSER 2025/2026 (D_s, D_b) two-axis morphism-quality construct is preserved unchanged; the SES + EF apparatus adds a second two-axis construct, at the context level rather than the morphism level. The architecture is self-similar.

Most of this document's load-bearing definitions are from ZPK00 Chapter 4 (well-established) and Z23 (recent extension); the Section 4 "SES + EF combined" construct is partially novel here and requires literature verification (see Section 7 question 6). The integration with the user's Bayesian SE draft (Section 5) is provisional and requires the parallel agent's report on the draft.

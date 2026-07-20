# Organizational / Architectural "Fusion" — Literature Inventory
## WySE / Systems-Morphism Scoping Review, Slice 04

**Date:** 2026-07-15
**Author:** Literature Reviewer agent (claude-sonnet-4-6), tasked by PostWach
**Integration status (R016):** All findings — (a) prior art

---

## 1. Scope

This slice covers organizational, enterprise, and situational senses of "fusion" — that is, the integration of heterogeneous information sources into a unified representation at the level of systems, organizations, or operational pictures. It explicitly excludes sensor-level estimation (Kalman-filter, track-level fusion) covered elsewhere. The specific sub-areas are:

1. JDL Levels 2–4: Situation assessment, impact assessment, process refinement
2. Common Operating Picture (COP) / Information Integration
3. Enterprise / Master Data Integration (MDI)
4. Schema and Ontology Alignment and Merging
5. Knowledge-Graph Fusion and Entity Resolution
6. Conway Mirroring Hypothesis and Organization-as-System framing
7. Hard + Soft Data Fusion (sensor + human/text reports)

The mapping target for each sub-area: does the fusion object and process admit a crisp formal morphism in the WySE/institutional sense? Can a computational witness check the claim? This is the "Fable-shape" test.

---

## 2. Sub-Areas Table

| # | Sub-area | What is fused | Into what object | Canonical reference(s) | Formal algebraic structure? | Fable-shape verdict |
|---|----------|---------------|-------------------|------------------------|----------------------------|---------------------|
| 2.1 | JDL Levels 2–4 (Situation / Impact / Process) | Multi-source observations, event reports, assessments | Situation picture, threat estimate, refined collection plan | [PLACEHOLDER: Hall & Llinas, 1997, Proc. IEEE] | Loosely hierarchical model; no algebra given in standard | SE-only |
| 2.2 | Common Operating Picture (COP) | Multi-domain data streams, doctrine/orders, sensor feeds | Shared geospatial-temporal state object | [PLACEHOLDER: DoD JP 3-0, various eds.] | Informal shared-state; no algebraic definition | SE-only |
| 2.3 | Enterprise / Master Data Integration | Heterogeneous enterprise records (ERP, CRM, HR) | Canonical master record ("golden record") | [PLACEHOLDER: Loshin, 2009, "Master Data Management"] | Record linkage = quotient; MDM hub = colimit candidate | Partial — colimit sketch Fable-shapeable |
| 2.4 | Schema / Ontology Alignment and Merging | Two or more ontologies / logical theories | Merged ontology / aligned vocabulary | [PLACEHOLDER: Euzenat & Shvaiko, 2013, "Ontology Matching", 2nd ed., Springer] | Alignment = correspondence relation; merge = pushout/colimit of theories in institution | STRONG — Fable-shaped via institution colimit |
| 2.5 | Knowledge-Graph Fusion / Entity Resolution | Named entities and relations across KGs | Unified entity index + merged graph | [PLACEHOLDER: Getoor & Machanavajjhala, 2012, VLDB Tutorial] | Quotient of entity-space under equivalence; functor from multi-graph to merged graph | Partial — entity-quotient Fable-shapeable; full KG merge less crisp |
| 2.6 | Conway Mirroring Hypothesis | Software/system architecture and organizational communication structure | Claimed isomorphism between org graph and system graph | [PLACEHOLDER: Conway, 1968, Datamation] | Claimed structural isomorphism; no algebraic proof given | Partial — structure Fable-shapeable; causal direction is not |
| 2.7 | Hard + Soft Data Fusion | Quantitative sensor data + qualitative human/text reports | Unified situational estimate with confidence | [PLACEHOLDER: Llinas et al. (eds.), various; Blasch et al., 2012, ISIF/IEEE] | Dempster-Shafer / Bayesian combination; no standard morphism formulation | Partial — DS/Bayesian object is formal; morphism question is open |

---

## 3. Formal-Structure Assessment

### 3.1 JDL Levels 2–4

The JDL (Joint Directors of Laboratories) data-fusion model [PLACEHOLDER: Hall & Llinas, 1997, Proc. IEEE; Steinberg et al., 1999, Proc. SPIE] organizes fusion into five levels: Level 0 (sub-object), Level 1 (object), Level 2 (situation), Level 3 (impact), Level 4 (process refinement), plus a Level 5 user refinement extension. Levels 2–3 are concerned with constructing an interpreted picture: which entities are in what relationships, and what threat or opportunity does that configuration imply?

**Algebraic content (or lack thereof).** The JDL model is a functional decomposition, not an algebraic one. "Situation" at Level 2 is conceptually a relational state augmenting Level 1 object estimates with context (relationships, temporal patterns, intent). No morphism between a Level-1 algebra and a Level-2 algebra is defined. Steinberg's 1999 extension toward "situation awareness" borrows from Endsley's cognitive model (also non-algebraic).

**WySE connection.** Conceptually, the shift from Level 1 to Level 2 resembles moving from state-space descriptions of individual entities to a compound system model Z_compound whose state set encodes relational configurations. This is a natural systems-theoretic elaboration, but no formal functor is written down in the literature. This is a mapping opportunity for WySE, not an existing formal result.

**Verdict:** No existing algebraic structure connects JDL levels to morphism theory. The fusion object at Levels 2–3 is an interpretive construct maintained by human analysts or AI classifiers, not a category-theoretic or set-algebraic object. This sub-area is a systems-engineering concern.

### 3.2 Common Operating Picture (COP)

The COP concept is military / emergency-management doctrine. A COP is a single identical display of relevant information (friendly forces, enemy, weather, terrain, civil considerations) shared by two or more command echelons to facilitate collaborative planning and decision-making. References are predominantly doctrinal (JP 3-0, FM 6-0) or systems-architecture (C2/C4ISR system design).

**Algebraic content.** COP is operationally defined, not algebraically defined. Attempts to formalize shared state representations for distributed military systems appear in C2 architecture frameworks (DoDAF, NAF), which provide structural views (nodes, links, operational activities) but do not give morphism conditions or algebraic closure properties.

**WySE connection.** A COP could in principle be modeled as a WySE state-space Z_cop whose state is the relational configuration of observed entities at time t. "Shared" would then require that every participant agent i maintains a state homomorphic to Z_cop — which is a precise morphism condition. But this is a construction the WySE program would impose; it does not exist in the COP literature.

**Verdict:** SE-only. COP is a doctrine and architecture concern; the fusion object is a shared display artifact maintained by sociotechnical process, not a mathematical object with proven properties.

### 3.3 Enterprise / Master Data Integration

Master data management (MDM) is the discipline of defining a single, authoritative source of truth for core business entities (customer, product, supplier, location). References include practitioner and research literature on record linkage, entity consolidation, and hub-and-spoke or registry MDM architectures.

**Algebraic content — the "golden record" as colimit.** The strongest algebraic reading of MDM is as follows. Each source system S_i maintains a view of entity set E_i. The MDM hub maintains a canonical entity set E_master. There is a collection of partial reconciliation maps f_i: E_i --> E_master. If these maps respect a common specification (the master data model / ontology), then E_master is the colimit of the diagram of source views in the category of entity models under the reconciliation morphisms. This reading is implicit in the database-integration literature but rarely stated in categorical terms.

**Relevant literature.** Lenzerini's work on data integration [PLACEHOLDER: Lenzerini, 2002, PODS] provides the most formal treatment, framing data integration as query rewriting under a global-as-view (GAV) or local-as-view (LAV) schema. GAV can be read as: the global schema is the target, and each local schema maps into it (morphisms from local to global). LAV reverses the direction. The choice of LAV vs. GAV is exactly the choice of whether the master model is the codomain (target) or a mediator.

**WySE connection.** A WySE D_s (structural degree of homomorphism) measurement is directly applicable: if the source ERP schema and the master schema are both modeled as WySE systems (state = record type, transitions = update operations), the structural morphism between them is exactly the record-linkage / field-mapping function. D_s < 1 when multiple source fields collapse to one master field (many-to-one); D_s = 1 for a true isomorphism. The behavioral degree D_b would measure whether the same business operation applied to the source system produces the same outcome as applied to the master — this is the "operational equivalence" question that MDM practitioners care about informally.

**Verdict:** Partial. The colimit / GAV morphism reading is Fable-shapeable for a constrained case: given two source schemas and a declared master schema, one can write a crisp claim ("the schema morphisms (h_i, h_o, h_q) satisfy the WySE homomorphism conditions") and verify it computationally. The full MDM problem (including provenance, conflict resolution, temporal versioning) is an SE concern that resists a single clean morphism.

### 3.4 Schema and Ontology Alignment and Merging

This is the richest sub-area for WySE / institution-theory connections.

**What is being fused.** Two or more ontologies O_1, O_2 (as logical theories in a description logic, OWL, or first-order logic) are brought into correspondence. The alignment A is a set of correspondences {(e_1, e_2, r, c)} where e_1 in O_1, e_2 in O_2, r is a relation (=, <=, >=, ⊥), and c is a confidence. A merge M is a new ontology containing a superset of the concepts, with alignment correspondences encoded as axioms.

**Categorical / institution-theoretic structure.** This is where the literature is most formally developed. The key results are:

(a) **Pushout as merge.** In the category of theories (or presentations of a logical system), a merge of O_1 and O_2 over a common sub-ontology O_0 (the "bridge ontology" or "upper ontology") is the pushout of the diagram O_1 <-- O_0 --> O_2. This was articulated in the context of algebraic specification by Goguen and colleagues [PLACEHOLDER: Goguen & Burstall, 1992, JACM — "Institutions: Abstract model theory for specification and programming"] and applied to ontology merging by Mossakowski and colleagues [PLACEHOLDER: Mossakowski et al., 2006 or similar, on institutions and ontology merging].

(b) **Institution morphisms.** Goguen and Burstall's institution theory provides the exact machinery: an institution I = (Sign, Sen, Mod, |=) consists of a category of signatures, a sentence functor, a model functor, and a satisfaction relation. A morphism of institutions phi: I --> I' maps signatures, sentences, and models while preserving satisfaction. Ontology alignment under a common logical framework is precisely an institution morphism from the "local" institution of each source ontology to the "global" institution of the merged ontology.

(c) **Relevance to WySE.** WySE already uses institution theory (D_s and D_b are grounded there). The pushout-as-merge construction is the direct formal ancestor of what a "fused work-and-information-system" would require at the knowledge-representation layer. The colimit of a diagram of source ontologies (system descriptions, process models, data dictionaries) under institution morphisms IS the "fused organizational picture" at the knowledge level.

(d) **Euzenat & Shvaiko survey.** The main reference for ontology matching as a field is [PLACEHOLDER: Euzenat & Shvaiko, "Ontology Matching," 2nd ed., Springer, 2013]. This text surveys alignment techniques (syntactic, structural, semantic, instance-based) but does not systematically use institution theory — it is a practitioner-oriented synthesis. The categorical framing comes from the algebraic specification / formal methods community.

(e) **DOLCE and BFO as "bridge."** Upper ontologies such as DOLCE [PLACEHOLDER: Masolo et al., 2003, WonderWeb deliverable] and BFO [PLACEHOLDER: Smith et al., "Basic Formal Ontology," 2015] function as the O_0 in the pushout. Their role as universal codomain for domain-ontology merging is informal practice but maps exactly to the institution-morphism picture.

**Fable-shape sketch.** Given O_1 and O_2 (two OWL ontologies) and a declared common subsumption O_0:
- Claim: "The pushout M of O_1 <-- O_0 --> O_2 in the category of OWL-EL theories (under subsumption-preserving morphisms) exists and is computed correctly by the merge procedure P."
- Witness: (1) construct M using procedure P; (2) verify that the two injections i_1: O_1 --> M and i_2: O_2 --> M are theory morphisms (i.e., every axiom in O_1 is provable in M, every axiom in O_2 is provable in M); (3) verify universality (any competing merge M' that accepts both injections factors through M). Steps (1)–(2) are directly checkable in a reasoner (e.g., HermiT, Pellet). Step (3) requires specifying M' — checkable for finite cases.

This is genuinely Fable-shaped. The computational witness is a description-logic reasoner run against the merged ontology; adversarial hardening would use a second reasoner (e.g., FaCT++). The claim is crisp, falsifiable, and the WySE institution-morphism framework is the right language for it.

### 3.5 Knowledge-Graph Fusion and Entity Resolution

**What is fused.** Multiple knowledge graphs KG_1, ..., KG_n (typed entity-relation triples) are merged into a unified KG. Entity resolution (ER) identifies which nodes across graphs refer to the same real-world entity; link prediction fills in missing relations; deduplication removes redundant triples.

**Algebraic structure.**

(a) **Entity resolution as a quotient.** The core ER operation is: define an equivalence relation ~ on the union of entity sets (E_1 cup ... cup E_n) such that e_i ~ e_j iff they refer to the same entity. The merged entity set is the quotient (E_1 cup ... cup E_n) / ~. The surjection pi: union --> quotient is the merge morphism on entities. This is algebraically clean: the quotient construction is standard, and the surjection pi is exactly the sort of many-to-one map that produces D_s < 1 in WySE.

(b) **Functor reading.** Each KG_i can be modeled as a functor F_i: Sch_i --> Set (assigning entity sets and relation sets to the schema). ER + merge is then a natural transformation / colimit construction in the functor category. This reading is implicit in [PLACEHOLDER: Hogan et al., 2021, ACM Computing Surveys — "Knowledge Graphs"] and made explicit in category-theoretic database work [PLACEHOLDER: Spivak, 2012, or similar — "Functorial Data Migration"].

(c) **Limits of the algebraic picture.** ER in practice involves probabilistic decisions (entity pairs are matched with probability p; threshold-based matching). The hard algebraic structure (quotient) is an idealization. The real fusion product is a probabilistic graph, which requires extending the category to a Kleisli construction (as in Giry monad, already in the WySE probability thread). Full KG merge including relation induction and schema mapping is not captured by the quotient alone.

**WySE connection.** A knowledge graph whose nodes are system components and whose edges are relation types is a natural representation of a WySE system model at a particular abstraction level. Merging two such graphs under entity resolution is then a fusion morphism: the merged graph is a WySE system at a higher level of abstraction, and the merge morphism is a (partial) WySE homomorphism. The D_s degree measures the many-to-one collapse on entities; D_b would measure whether the same query executed on the source graphs produces the same answer as on the merged graph.

**Verdict:** Partial. The entity-quotient claim is Fable-shaped (crisp, verifiable). The full probabilistic KG-merge problem is not Fable-shaped as a single morphism claim — it requires a probabilistic morphism framework (Kleisli/Giry extension).

### 3.6 Conway Mirroring Hypothesis

**Statement.** Conway's Law [PLACEHOLDER: Conway, 1968, Datamation, "How do committees invent?"] states that "organizations which design systems are constrained to produce designs which are copies of the communication structures of those organizations." In modern form: the architecture of a software system mirrors the organization's communication graph.

**Empirical literature.** A growing body of empirical CS research tests Conway's Law, primarily using organizational communication data (email, code reviews, JIRA) correlated with software coupling / modularity metrics. Representative works include [PLACEHOLDER: MacCormack et al., 2012, MIS Quarterly — "Exploring the duality between product and organizational architectures"]; [PLACEHOLDER: Cataldo & Herbsleb, 2013, TSE]; [PLACEHOLDER: Tamburri et al., 2019, JSS — organizational smells and Conway's Law].

**The "inverse Conway maneuver."** Popularized in the Team Topologies framework [PLACEHOLDER: Skelton & Pais, 2019, "Team Topologies," IT Revolution Press], this is the design prescription: deliberately shape your organization so that its communication structure mirrors the desired system architecture. It makes Conway's Law normative rather than descriptive.

**Algebraic / morphism structure.** Conway's Law as a precise mathematical claim would read: "There exists a graph homomorphism h: G_system --> G_org, where G_system is the module-dependency graph and G_org is the team-communication graph, such that h is surjective and respects the coupling relation." This is a crisp graph-morphism claim. MacCormack et al. (2012) operationalize it as a correlation between "design structure matrix" (DSM) coupling and "organizational structure matrix" (OSM) coupling — but they measure correlation, not morphism degree.

**WySE connection.** The WySE D_s (structural degree) is directly applicable: compute D_s(G_system, G_org) under some declared mapping h. D_s = 1 would confirm a perfect organizational-architectural isomorphism (the "mirroring" claim). D_s < 1 quantifies how far short of full mirroring the pair falls. This is an under-exploited but direct application of the WySE structural degree metric.

**What is not Fable-shaped.** The causal direction of Conway's Law (does the org cause the architecture, or vice versa?) is an empirical and social-science question that cannot be settled by a morphism proof. The claim "this org mirrors this architecture" is Fable-shaped; the claim "organizations are causally constrained to mirror" is not.

**Verdict:** Partial. The structural mirroring claim (existence and degree of a graph morphism between org graph and system graph) is Fable-shaped. The causal and normative dimensions are SE / organizational science concerns.

### 3.7 Hard + Soft Data Fusion

**What is fused.** "Hard" data: quantitative sensor measurements with known error models (radar tracks, GPS, telemetry). "Soft" data: qualitative human reports, text, imagery, open-source intelligence (OSINT), doctrine, intent assessments — sources without clean probability distributions.

**The fusion problem.** Combining hard and soft data is the unresolved grand challenge of JDL Levels 2–3. The gap: hard data lives in probability measure spaces (Kalman / Bayesian); soft data does not have a canonical algebraic representation. Approaches include:

(a) **Dempster-Shafer / evidence theory** [PLACEHOLDER: Shafer, 1976, "A Mathematical Theory of Evidence," Princeton UP; Dempster, 1967, Annals of Math Statistics]. DS assigns belief mass to sets of hypotheses rather than point probabilities, which can accommodate vague or conflicting human reports. The combination rule (Dempster's rule) is algebraic (commutative, associative over the belief-function semiring), but its appropriateness for combining genuinely heterogeneous evidence types is contested [PLACEHOLDER: Zadeh, 1984 or similar — "Book review" critique of DS].

(b) **Argumentation and sensemaking** [PLACEHOLDER: Klein et al., "Macrocognition" literature; Pirolli & Card, 2005, CHI — "The Sensemaking Process"]. Soft-data fusion at Levels 2–3 is often modeled as argumentation or abductive inference, not algebraic combination. These frameworks do not produce a single algebraic object.

(c) **Natural language processing (NLP) pipeline as soft-data fusion.** Modern approaches treat soft data as text and extract structured triples (entities, relations, events) using NLP/IE pipelines, then merge into a KG (sub-area 3.5 above). This converts the soft-data problem into a KG-merge problem, with the caveat that the extraction step introduces uncertain provenance.

**WySE connection.** The relevant question is: can the output of a hard+soft fusion process be modeled as a WySE system Z_fused, with morphisms from Z_hard and Z_soft into Z_fused? For hard data, the source system Z_hard has a well-defined state space (continuous measurement space) and known dynamics. For soft data, Z_soft lacks a canonical state space; its "state" is an interpreted assessment maintained by an analyst. The morphism h: Z_soft --> Z_fused requires defining a surjection from assessment states to fused states, which is not formalized in the literature.

**Verdict:** Not cleanly Fable-shaped. The hard-data component (DS combination, Bayesian update) admits formal algebraic treatment and in principle a WySE morphism claim. The soft-data component — and the interface between the two — does not currently have a canonical algebraic representation that would support a crisp morphism proof and computational witness. This is a genuine research gap rather than a solvable Fable-shape problem in the current state of the art.

---

## 4. Fable-Shape Verdicts Summary

| # | Sub-area | Verdict | Rationale |
|---|----------|---------|-----------|
| 2.1 | JDL Levels 2–4 | NOT Fable-shaped — SE concern | Functional decomposition model, no algebraic structure; fusion object is an interpretive construct |
| 2.2 | Common Operating Picture | NOT Fable-shaped — SE concern | Doctrine / architecture artifact; no algebraic definition of shared state; morphism would have to be imposed by WySE, not found in literature |
| 2.3 | Enterprise MDI / Master Data | PARTIAL — constrained Fable-shapeable | GAV schema morphism and golden-record-as-colimit admit a crisp WySE D_s claim for declared schema pairs; conflict resolution and provenance are SE concerns |
| 2.4 | Ontology Alignment / Merge | STRONG Fable-shaped | Pushout / colimit of theories in institution theory; OWL-reasoner witness; direct WySE institution-morphism language; most mature formal structure in this slice |
| 2.5 | KG Fusion / Entity Resolution | PARTIAL — entity-quotient is Fable-shapeable | Quotient surjection clean and D_s-measurable; probabilistic matching and full KG merge require Kleisli/Giry extension |
| 2.6 | Conway Mirroring Hypothesis | PARTIAL — structural claim Fable-shapeable | Graph morphism between org-comm graph and system-module graph is crisp and WySE D_s-measurable; causal and normative claims are not |
| 2.7 | Hard + Soft Data Fusion | NOT cleanly Fable-shaped | Hard-only DS/Bayesian combination is formal but contested; soft-data state space is not canonically defined; no morphism from analyst assessments to fused object exists in literature |

### Which sub-areas should WySE pursue?

**Priority 1 (STRONG):** Ontology alignment as institution-morphism pushout. This directly extends WySE's existing institution-theory grounding (D_s / D_b already live there). A Fable-shaped claim is writable now: "the merge M is the pushout of O_1 <-- O_0 --> O_2 in the institution of OWL-EL theories, verified by HermiT." This is the "Digital Twin of the Organization" fused-architecture claim at the knowledge-representation layer.

**Priority 2 (PARTIAL, near-term):** Conway mirroring as WySE D_s measurement. The claim "D_s(G_system, G_org) = x" under a declared mapping h is crisp, measurable, and computationally verifiable. The literature lacks this quantification; WySE would contribute it. Connects to the Digital Twin / mirroring-hypothesis proposal directly.

**Priority 3 (PARTIAL, requires Kleisli extension):** KG entity-quotient morphism. Clean for the deterministic case; requires the Giry/Kleisli probabilistic morphism already under development in the WySE probability thread.

**Deferred (SE concerns):** JDL 2–4, COP, hard+soft fusion. These belong in the systems-engineering design space for a Digital Twin of the Organization; they are not Fable-shaped claims and should not be framed as provable morphism results.

---

## 5. Formal-Structure Connection Summary (Institution / Category Theory)

The table below maps each sub-area to the algebraic structure that applies (if any) and its connection to WySE institutions.

| Sub-area | Algebraic object | Category-theory reading | WySE instrument |
|----------|-----------------|------------------------|----------------|
| Ontology merge | Pushout of theory presentations | Institution colimit in (Sign, Sen, Mod, |=) | Institution morphism = h_sigma, h_sentences; WySE D_s on concept sets |
| KG entity resolution | Quotient of entity union under ~ | Coequalizer of entity maps | WySE D_s: many-to-one collapse of entity sets |
| Schema / GAV integration | Global schema as codomain; f_i: source_i --> global | Functor to a target category (schemas as functors) | WySE D_s on record-type sets; D_b on query equivalence |
| Conway mirroring | Graph morphism h: G_sys --> G_org | Functor between graph-categories | WySE D_s on module/team sets |
| DS belief combination | Dempster's rule on 2^Omega lattice | Commutative semiring on belief functions | Connects to Giry-monad WySE extension (probabilistic morphism) |
| JDL situation model | None defined | Would require compound Z construction | WySE would impose, not find |
| COP | None defined | Would require shared-state morphism from each agent | WySE would impose, not find |

---

## 6. Refs-to-Verify ([PLACEHOLDER] list)

All references below are marked [PLACEHOLDER] because they have not been verified against the portfolio `approved.bib` store. They are cited from reviewer knowledge and must pass the Byzantine-Bayesian verification protocol (R019 / R109) before appearing in any manuscript.

| Tag | Citation (as recalled) | Verify: author, year, venue, title |
|-----|-----------------------|-----------------------------------|
| [PH-01] | Hall & Llinas, 1997, Proc. IEEE, "An introduction to multisensor data fusion" | Verify year, volume, pages |
| [PH-02] | Steinberg, Bowman & White, 1999, Proc. SPIE, "Revisions to the JDL data fusion model" | Verify year, SPIE volume |
| [PH-03] | DoD JP 3-0, "Joint Operations" (various editions) | Verify edition year currently in use |
| [PH-04] | Loshin, 2009, "Master Data Management," Morgan Kaufmann | Verify publisher, year, ISBN |
| [PH-05] | Euzenat & Shvaiko, 2013, "Ontology Matching," 2nd ed., Springer | Verify edition, year |
| [PH-06] | Goguen & Burstall, 1992, JACM, "Institutions: Abstract model theory for specification and programming" | Verify year, volume, pages — this is a key reference |
| [PH-07] | Mossakowski et al., institution / ontology merging paper | Title, year, venue UNKNOWN — high risk of placeholder error |
| [PH-08] | Getoor & Machanavajjhala, 2012, VLDB Tutorial, entity resolution | Verify year, venue |
| [PH-09] | Hogan et al., 2021, ACM Computing Surveys, "Knowledge Graphs" | Verify year, volume |
| [PH-10] | Spivak, 2012, "Functorial Data Migration" or similar | Title and venue uncertain — [PLACEHOLDER] |
| [PH-11] | Conway, 1968, Datamation, "How do committees invent?" | Verify journal name, year |
| [PH-12] | MacCormack, Rusnak & Baldwin, 2012, MIS Quarterly | Verify exact title, year, volume |
| [PH-13] | Cataldo & Herbsleb, 2013, TSE | Title and volume uncertain |
| [PH-14] | Tamburri et al., 2019, JSS | Title uncertain |
| [PH-15] | Skelton & Pais, 2019, "Team Topologies," IT Revolution Press | Verify publisher, year |
| [PH-16] | Shafer, 1976, "A Mathematical Theory of Evidence," Princeton UP | Verify publisher, year |
| [PH-17] | Dempster, 1967, Annals of Mathematical Statistics | Title and year to verify |
| [PH-18] | Masolo et al., 2003, WonderWeb Deliverable D18, DOLCE ontology | Verify deliverable number |
| [PH-19] | Smith et al., 2015 or similar, "Basic Formal Ontology" | Year and venue uncertain |
| [PH-20] | Lenzerini, 2002, PODS, "Data integration: A theoretical perspective" | Verify year, venue |
| [PH-21] | Pirolli & Card, 2005, CHI, "The Sensemaking Process and Leverage Points" | Verify year, venue |
| [PH-22] | Endsley, 1995 or similar, "Toward a Theory of Situation Awareness" | Year and venue uncertain |

---

## 7. Gaps Identified

**Gap G1 — No WySE D_s measurement of Conway mirroring in the empirical literature.**
Existing Conway-law empirical studies (MacCormack et al., Cataldo & Herbsleb) measure correlation between coupling matrices. None apply a formal morphism degree. This is a direct contribution opportunity for WySE: define h and measure D_s(G_system, G_org) on a real organizational case.

**Gap G2 — Institution-theoretic framing absent from ontology matching surveys.**
The dominant survey (Euzenat & Shvaiko) does not systematically use institution theory despite the structural alignment being exact. Connecting ontology alignment techniques to institution morphisms via WySE would provide a unifying formal account absent from the literature.

**Gap G3 — Behavioral degree (D_b) unexplored in schema integration.**
The MDM / schema-integration literature defines structural alignment (which fields map to which) but does not ask whether business operations are behaviorally equivalent under the mapping. WySE D_b would fill this gap: two ERP systems are not just structurally similar if the same business process applied to both produces the same output.

**Gap G4 — Soft-data state space undefined.**
No canonical algebraic definition of the "soft-data state space" exists. Analyst assessments, OSINT reports, and doctrinal texts live in natural language; their conversion to a formal state space is ad hoc. This is a genuine open problem whose resolution would be required before a WySE morphism from soft-data systems to fused systems could be written.

**Gap G5 — JDL Level 3 (Impact Assessment) lacks formal object definition.**
The impact-assessment fusion product — what threat does this situation represent? — is the least formalized JDL level. There is no algebraic or logical representation of "impact" that would support a morphism claim. A contribution here would require first defining Z_impact as a WySE system model, which is a substantial theoretical task.

**Gap G6 — KG probabilistic morphism.**
The entity-quotient claim is clean for the deterministic case but real entity resolution is probabilistic. The extension requires a probabilistic WySE morphism (Kleisli / Giry); this is under development in the WySE probability thread (TMS ch22 connection) but has not been applied to the KG-fusion setting.

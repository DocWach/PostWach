# DASH / SHACL (TopQuadrant) — Recon Inventory

Recon date: 2026-05-27. Target: the TopQuadrant SHACL API (Java/Apache Jena) and the DASH (Data Shapes) extension vocabulary from datashapes.org. Lens: adopt-into-hive (strengthen the GI-JOE SHACL gate, which today runs base SHACL via pyshacl on Python/Windows) and competitive/landscape positioning.

Abbreviations on first use: SHACL = Shapes Constraint Language (W3C); DASH = Data Shapes vocabulary (datashapes.org); SHACL-AF = SHACL Advanced Features; SHACL-SPARQL = the SPARQL-based extension mechanism in the SHACL Recommendation; SHACL-JS = SHACL JavaScript Extensions; CQ = competency question; ABox/TBox = assertional/terminological box; TTL = Turtle RDF serialization; JRE = Java Runtime Environment.

## Local clone inventory

Clone path: `C:/Users/pfwac/recon-scratch/shacl` (shallow/grafted; single graft commit `752fc55`).

| Property | Value (verified from clone) |
|---|---|
| Project name | TopBraid SHACL API |
| Version | `1.5.1-SNAPSHOT` (pom.xml line 25) |
| License | Apache License v2.0 (LICENSE file + pom.xml; NOTICE present) |
| Org / developers | TopQuadrant, Inc. Original developer Holger Knublauch; current maintainer Ashley Caselli (Knowledge Pixels AG) |
| Build system | Maven (`pom.xml`, `mvnw`/`mvnw.cmd` wrapper); also `.docker/Dockerfile` for a containerized CLI |
| Java baseline | Java 21 (`<java.version>21</java.version>`) |
| Core dependency | Apache Jena `jena-arq` 6.0.0; Jelly (`jelly-jena` 3.7.1) for the Jelly RDF binary format; SLF4J/Log4j2 for logging; JUnit 4.13.2 (test) |
| Last activity | Graft commit dated 2026-03-23 (`git log` on the shallow clone). Active project (1.5.x line, Jena 6, Java 21 are all recent). [unverified] full history beyond the graft point. |
| Distribution | Maven Central (`org.topbraid:shacl`); prebuilt Docker images; `-bin.zip` CLI bundle |

### What the library provides (sampled package structure under `src/main/java/org/topbraid/`)

- **SHACL Core engine.** `shacl/validation/` plus `shacl/validation/java/` hold one Java executor per core constraint component: `MinCount`, `MaxCount`, `Class`, `Datatype`, `NodeKind`, `Pattern`, `In`, `Closed`, `Disjoint`, `Equals`, `LessThan(OrEquals)`, `Min/MaxInclusive`, `Min/MaxExclusive`, `Min/MaxLength`, `UniqueLang`, `QualifiedValueShape`, `And`/`Or`/`Not`/`Xone`, `Node`. Registered in `JavaConstraintExecutors.java`. Entry point per README is `ValidationUtil` in `org.topbraid.shacl.validation`.
- **SHACL-SPARQL.** `shacl/validation/sparql/` (`SPARQLComponentExecutor`, `SPARQLConstraintExecutor`, `SPARQLTarget`, `SPARQLSyntaxChecker`) plus `shacl/arq/` ARQ function wiring. This is the generic engine that executes any constraint component defined declaratively via `sh:sparql` / `sh:SPARQLSelectValidator`.
- **SHACL-AF (Advanced Features).** SHACL rules in `shacl/rules/` (`RuleEngine`, `SPARQLRule`, `TripleRule`, `ValuesRule`, `RulesEntailment`); node expressions in `shacl/expr/` and `shacl/expr/lib/` (`AskExpression`, `CountExpression`, `FilterShapeExpression`, `Min/Max/Sum/GroupConcat`, `Union`/`Intersection`/`Minus`, `OrderBy`/`Limit`/`Offset`); custom SHACL functions and targets in `shacl/model/` and `shacl/arq/`. README confirms SHACL-AF (Rules etc.) coverage.
- **DASH support.** Vocabulary constants in `shacl/vocabulary/DASH.java`; the shipped DASH definitions graph at `src/main/resources/rdf/dash.ttl`; a dedicated Java executor `validation/java/SingleLineConstraintExecutor.java`; and a suggestions/auto-fix surface (`validation/ValidationSuggestionGenerator.java`, `ValidationSuggestionGeneratorFactory.java`). See next section for the DASH detail.
- **Validation report model.** `validation/ValidationReport.java`, `ValidationResult.java`, `ResourceValidationReport.java`, `ResourceValidationResult.java` produce the standard `sh:ValidationReport` / `sh:ValidationResult` RDF.
- **Bundled vocabularies.** `vocabulary/` includes `SH`, `DASH`, `TOSH`, `EDG`, `SPARQL`, plus `MF`/`SHT` (the W3C SHACL test-suite manifest and test vocabularies). TTL graphs shipped: `shacl.ttl`, `dash.ttl`, `tosh.ttl`, `system-triples.ttl`.
- **Test harness.** W3C SHACL Core/SPARQL conformance tests under `src/test/resources/sh/tests/{core,expression,function,rules,...}` as `*.test.ttl` manifests; rules tests under `tests/rules/{sparql,triple}`.
- **CLI + Docker.** `shaclvalidate` and `shaclinfer` commands (`.bat`/`.sh`); Docker entrypoint exposes `validate` and `infer`. Only Turtle (and Jelly) input is supported by the CLI/Docker path.

### Coverage notes (verified caveats)

- **SHACL-JS dropped.** README: SHACL-JS was "Former Coverage until version 1.3.2." No `shacl/js/**` source package exists in this clone (Glob returned no files). DASH still *declares* JS-related terms in `dash.ttl`, but the JS execution engine is gone from current versions.
- **SHACL Compact Syntax dropped.** README: "Former Coverage until version 1.4.0."
- The European Commission's Interoperability Test Bed (ITB) SHACL validators are stated by the README to use this API internally; the same code underlies TopBraid 7.1.

## DASH constraint components & SHACL-AF

DASH is TopQuadrant's extension vocabulary at namespace `http://datashapes.org/dash#` (prefix `dash:`). Verified from the shipped `dash.ttl` and from datashapes.org. Key point on *how* DASH is implemented: most DASH constraint components are defined **declaratively in `dash.ttl` via `sh:propertyValidator`/`sh:nodeValidator` carrying a `sh:SPARQLSelectValidator`**, then executed by the generic SHACL-SPARQL engine. Only a small set has dedicated Java executors. This distinction drives the pyshacl portability analysis below.

Constraint components (names verified in `dash.ttl` and/or datashapes.org/constraints.html):

- `dash:closedByTypes` (`dash:ClosedByTypesConstraintComponent`) — focus nodes may only have values for properties enumerated via `sh:property`/`sh:path` at their `rdf:type`s and superclasses; a per-type variant of `sh:closed`.
- `dash:hasValueIn` (`dash:HasValueInConstraintComponent`) — at least one value node must be a member of a given SHACL list. Verified to carry a `sh:SPARQLSelectValidator` in `dash.ttl` (SPARQL-defined, not Java).
- `dash:hasValueWithClass` — one of the value nodes must be an instance of a given class.
- `dash:rootClass` — all value nodes must be a subclass of a specified root class.
- `dash:stem` — all value nodes must be IRIs starting with a given string.
- `dash:uniqueValueForClass` — property value uniqueness across all instances of a class (a cross-focus-node uniqueness constraint, useful for primary-key style rules).
- `dash:singleLine` (`dash:SingleLineConstraintComponent`) — literal values must not contain line breaks. The ONE DASH component with a dedicated Java executor (`SingleLineConstraintExecutor`, registered in `JavaConstraintExecutors`).
- `dash:nonRecursive` (`dash:NonRecursiveConstraintComponent`) — a property/path must not point back to its own focus node; has a vocabulary constant in `DASH.java`.
- `dash:coExistsWith` — properties must either both have values or neither does.
- `dash:subSetOf` — all value nodes must also be values of a specified other property.
- `dash:symmetric` — if A relates to B then B must relate to A.
- `dash:uriStart` — marks a property as primary key with a required URI prefix structure.

Reification, suggestions/auto-fix, and other DASH surfaces:

- **Reification.** `dash:reifiableBy` (`dash:ReifiableByConstraintComponent`, constant in `DASH.java`; used throughout `dash.ttl`, e.g. on `dash:ConstraintReificationShape`) lets shapes attach metadata to specific constraint values.
- **Suggestions / auto-fix.** DASH defines a declarative repair model: `dash:SuggestionGenerator` (base class), `dash:SPARQLUpdateSuggestionGenerator`, `dash:ScriptSuggestionGenerator`, attachment via `dash:propertySuggestionGenerator` / `dash:suggestionGenerator`, results as `dash:GraphUpdate` carrying `dash:addedTriple` / `dash:deletedTriple`, attached to results via `dash:suggestion`. The API exposes this through `validation/ValidationSuggestionGenerator.java` and `ValidationSuggestionGeneratorFactory.java`. SPARQL-update generators bind `$focusNode`, `$predicate`, and constraint parameters (e.g. `$maxLength`) to compute the repair change set.
- **Script extensions.** `dash:ScriptConstraintComponent` and JS-related terms remain *declared* in `dash.ttl`, but the JS execution engine was removed after v1.3.2 (see caveat above).
- **Targets / utility terms (from datashapes.org/dash).** `dash:AllObjectsTarget`, `dash:AllSubjectsTarget`, `dash:HasValueTarget` (richer target types beyond `sh:targetClass`/`sh:targetNode`); `dash:applicableToClass` (a "softer" `sh:targetClass`); `dash:ListShape` (well-formed RDF list validation); result classes `dash:SuccessResult` / `dash:FailureResult`; convenience datatypes `dash:DateOrDateTime`, `dash:StringOrLangString`.
- **DASH test cases.** DASH defines a test-case vocabulary (e.g. graph-validation and function test cases) used to assert expected validation/inference output; the clone ships the W3C SHT/MF manifest test machinery that this builds on. Exact DASH test-case class names not individually confirmed from the clone in this pass; [unverified] beyond the presence of the test infrastructure.

### SHACL-AF relationship

SHACL-AF (W3C Working Group Note) adds rules, custom targets, SHACL functions, node expressions, and the SPARQL-based extension plumbing on top of the SHACL Core Recommendation. DASH sits *above* both: it is a library of concrete, reusable constraint components and tooling vocabulary (suggestions, reification, test cases, form/UI hints) built using the SHACL-Core + SHACL-AF extension mechanisms. In this codebase the layering is visible: SHACL-AF lives in `shacl/rules/` + `shacl/expr/` + `shacl/arq/`, and DASH components are largely *expressed* using SHACL-SPARQL validators inside `dash.ttl`.

## Standards lineage

- **SHACL Core + SHACL-SPARQL** — W3C Recommendation, "Shapes Constraint Language (SHACL)", 20 July 2017. This is a ratified standard. The TopBraid API is described in its README as a reference implementation of the SHACL spec.
- **SHACL-AF (Advanced Features)** — W3C Working Group Note (not a Recommendation), covering rules, custom targets/functions, node expressions. Note status, so it is a stable specification but not a normative standard.
- **SHACL-JS** — W3C Working Group Note. Implemented historically by TopBraid, removed after v1.3.2.
- **SHACL Compact Syntax** — W3C Community/WG draft; removed from TopBraid after v1.4.0.
- **DASH** — *de facto* extension vocabulary published and maintained by TopQuadrant at datashapes.org. Not a W3C standard; it is the most widely referenced third-party SHACL constraint/tooling vocabulary and is bundled directly into this reference implementation, which gives it strong practical authority.

## Adopt-into-hive assessment

Context: our GI-JOE gate runs base SHACL through **pyshacl** (Python `rdflib`/`pyshacl`) on Windows, over the portfolio governance ontology, with 20 SPARQL CQs and a two-tier (advisory/blocking) gate. The TopBraid API is **Java 21 / Jena 6**. That is a hard runtime-impedance boundary: adopting the Java engine wholesale means standing up a JVM + Jena toolchain (or the Docker image) alongside the existing Python gate. The far cheaper path for most DASH value is to **reuse the DASH vocabulary, not the Java engine**, because pyshacl is itself SHACL-AF-aware and can consume SPARQL-defined constraint components.

### pyshacl compatibility (the load-bearing question)

- **pyshacl supports SHACL Core, SHACL-SPARQL, and SHACL-AF** (rules, SPARQL constraints, node expressions). [unverified against a pinned pyshacl version in this recon; confirm the installed version's `--help`/changelog before relying on AF rules.]
- Because the **bulk of DASH components are defined in `dash.ttl` purely via `sh:SPARQLSelectValidator`** (verified for `dash:hasValueIn`; the same pattern recurs across `dash.ttl`), they are in principle executable by *any* SHACL-SPARQL-capable engine, including pyshacl, **if `dash.ttl` is loaded into the shapes graph** so the component definitions and their validators are present. This is the key, low-cost portability lever: copy the relevant component definitions from the shipped `dash.ttl` into our shapes graph rather than re-implement them.
- The exceptions are components/features that rely on **dedicated Java executors or the (now-removed) JS engine**: `dash:singleLine`, `dash:nonRecursive`, `dash:reifiableBy`, `dash:Script*`, `dash:Indexed`. These will NOT "just run" under pyshacl from the TTL alone; they would need a SPARQL re-expression or a Python-side check.
- **DASH suggestions / auto-fix** depend on the TopBraid API's `ValidationSuggestionGenerator` Java surface (and/or SPARQL-update generators). pyshacl does not provide an equivalent fix-application engine out of the box, so suggestions are not a free import. [unverified] whether any pyshacl plug-in offers DASH-style fixes; treat as build-it-ourselves.

### Candidate features, R016-tagged as IF WE ADOPTED THEM

R016 status is the integration status the capability would have *in our portfolio after the stated work*, not TopQuadrant's own maturity. (a) = research artifact, (b) = demonstrated capability, (c) = integrated deliverable.

| Candidate | What it buys the GI-JOE gate | pyshacl path | Integration cost | R016 if adopted |
|---|---|---|---|---|
| `dash:hasValueIn` (value must be in a SHACL list) | Closed enumerations cleaner than chained `sh:or`; good for governance enum fields (hive type, tier, status) | Load its `dash.ttl` definition (SPARQL validator) into shapes graph | Low: copy TTL fragment; verify pyshacl runs the SPARQL validator | (c) integrated deliverable (it would run inside the existing gate) |
| `dash:hasValueWithClass` | "at least one value is an instance of class X" without bespoke SPARQL | Same as above (SPARQL-defined) | Low | (c) |
| `dash:rootClass` / `dash:stem` | Subclass-rooting and IRI-prefix discipline for our `po:` namespace individuals | SPARQL-defined; load from `dash.ttl` | Low | (c) |
| `dash:uniqueValueForClass` | Cross-instance uniqueness (primary-key style) — directly useful for "each hive has a unique identifier" CQs | SPARQL-defined; load from `dash.ttl` | Low-medium (cross-focus-node logic; test against our ABox) | (c) |
| `dash:closedByTypes` | Per-type closure; richer than blanket `sh:closed` for multi-typed governance individuals | SPARQL-defined; load from `dash.ttl` | Medium (requires type classes to also be shapes; validate fit with our TBox) | (b) demonstrated, pending portfolio fit test, then (c) |
| `dash:coExistsWith` | "if field A present then B present" co-occurrence rules (e.g., `Outputs` ↔ `Parent Hives`) | SPARQL-defined; load from `dash.ttl` | Low-medium | (c) |
| `dash:singleLine` | Trivial hygiene for label/identifier fields | NOT free under pyshacl (Java executor); re-express as `sh:pattern` (`^[^\n\r]*$`) | Low if re-expressed as pattern; do NOT import the Java executor | (b) if re-expressed; using TopBraid Java engine = (a) external tool, not integrated |
| DASH **suggestions / auto-fix** | Turn the gate from "report-only" into "report + proposed repair triples" — high value for agent self-correction loops | No native pyshacl support; would require building a Python suggestion layer or running the Java API as a separate service | High (new build OR JVM service + Python bridge) | (a) research artifact at best in our stack today; do not present as a quick win |
| **Richer validation report** (`dash:SuccessResult`, `dash:FailureResult`, result detail) | More expressive gate output for triage | pyshacl already emits `sh:ValidationReport`; DASH result subclasses are cosmetic unless consumed | Low, but marginal value | (b) |
| TopBraid **SHACL-AF rules engine** (Java) | We already get AF rules via pyshacl; no need for the Java engine | Use pyshacl's AF, not TopBraid | n/a — avoid dual engines | n/a |

### Quick wins (verified-feasible, ranked)

1. **Adopt SPARQL-defined DASH constraint components by loading `dash.ttl` fragments into the GI-JOE shapes graph.** Best candidates: `dash:hasValueIn`, `dash:hasValueWithClass`, `dash:rootClass`, `dash:uniqueValueForClass`, `dash:coExistsWith`. These map directly onto governance-ontology checks we currently hand-roll or cannot express. Cost is low and stays entirely inside Python/pyshacl. Validate that the installed pyshacl version executes the bundled SPARQL validators before committing.
2. **Re-express `dash:singleLine` as an `sh:pattern`** rather than importing the Java executor — keeps the win, avoids the JVM.
3. **Treat suggestions/auto-fix as a deliberate R&D track, not a quick win.** It is the highest-value DASH capability for an agent hive (machine-applicable repairs), but there is no pyshacl-native path; it is a build or a JVM-service decision. Flag for the HOS / capability roadmap rather than the gate backlog.

Caveat to honor: do NOT assume DASH components run under pyshacl until tested. The clone proves they are SPARQL-defined (high confidence they port), but the actual pyshacl execution of bundled component definitions must be empirically confirmed on our pinned version. Mark any adoption (a) research artifact until that test passes.

## Competitive/landscape positioning

- **TopQuadrant / TopBraid is the incumbent commercial authority in the SHACL space.** The original SHACL editors include TopQuadrant's Holger Knublauch; this API is positioned as the SHACL reference implementation; the European Commission's public RDF/SHACL validators run on it; and DASH is the dominant third-party SHACL extension vocabulary. Their commercial product (TopBraid EDG / "Enterprise Data Governance," reflected in the `EDG.java` vocabulary) targets enterprise data-governance and metadata-management buyers.
- **Where our portfolio sits relative to them.** Our differentiation is not "a better SHACL engine"; it is the **agent-orchestration + governance-ontology integration** (claude-flow MCP coordination, Zero-Trust governance, ontology-backed capability/staleness CQs, the two-tier enforcement gate wired into a multi-hive workflow). TopBraid is a single-product data-governance platform; ours is a research-grade hive-of-hives where SHACL is one enforcement primitive among ontology + SPARQL CQ + ZT policy layers.
- **Strategic read.** TopQuadrant is best treated as (1) a **vocabulary and reference-implementation supplier** (consume DASH terms, mine `dash.ttl`, cite as the de-facto SHACL extension standard) and (2) a **benchmark for report/repair UX** (their suggestions/auto-fix and form-generation surfaces are ahead of our report-only gate). They are not a direct competitor for our agent-orchestration thesis, but they are the right external comparator when we claim "ontology-backed governance" maturity. Adopting DASH vocabulary strengthens our credibility (aligning to the de-facto standard) without adopting their stack.
- **Impedance reminder for any positioning claim:** anything we run via the TopBraid Java API rather than via pyshacl is an *external tool we invoked* (R016 (a)), not an integrated portfolio deliverable. Keep that line clear in write-ups.

## Sources

- Local clone: `C:/Users/pfwac/recon-scratch/shacl` — `README.md`, `pom.xml` (version 1.5.1-SNAPSHOT, Apache-2.0, Jena 6.0.0, Java 21), `LICENSE`, `NOTICE`.
- Clone source structure: `src/main/java/org/topbraid/shacl/{validation,validation/java,validation/sparql,rules,expr,model,arq,vocabulary}/`, `src/main/resources/rdf/{dash.ttl,shacl.ttl,tosh.ttl}`, `src/test/resources/sh/tests/`.
- Verified specifics: `JavaConstraintExecutors.java` (core component registry + lone `DASH.SingleLineConstraintComponent` Java executor); `vocabulary/DASH.java` (constants: `NonRecursive`, `ReifiableBy`, `Script`, `SingleLine`, `Indexed`, `Parameter` constraint components); `dash.ttl` (`dash:ClosedByTypesConstraintComponent`, `dash:HasValueInConstraintComponent` with `sh:SPARQLSelectValidator`).
- Git: shallow/grafted clone, graft commit `752fc55`, dated 2026-03-23.
- Web: `https://datashapes.org/dash` (targets, result types, utility terms), `https://datashapes.org/constraints.html` (constraint components), `https://datashapes.org/suggestions.html` (suggestions/auto-fix model). W3C lineage: SHACL Recommendation (2017-07-20), SHACL-AF and SHACL-JS Working Group Notes (status per README coverage statements).
- [unverified] items flagged inline: full git history beyond graft; exact DASH test-case class names; pyshacl version-specific AF/DASH execution behavior on our installed build.

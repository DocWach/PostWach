# OntoEagle / cq-ferret — Recon Inventory

Recon date: 2026-05-27. Sources: shallow local clone at `C:/Users/pfwac/recon-scratch/OntoEagle` (single commit `f4a7295`, authored 2026-05-14 by Jonathan Vajda) plus the live GitHub Pages site. Abbreviations defined at first use: competency question (CQ), ontology (OWL = Web Ontology Language; RDF = Resource Description Framework), Basic Formal Ontology (BFO), Common Core Ontologies (CCO), Simple Knowledge Organization System (SKOS), Minimum Information to Reference an External Ontology Term (MIREOT), Syntactic Locality Module Extractor (SLME).

## What it is

OntoEagle is a lightweight, browser-based, static-site toolkit for ontology development. The README states it is for "**exploring ontologies**, **assembling ontology slims**, and **gathering competency questions**." It is not a server application and not a reasoner; it is a set of static HTML pages plus client-side JavaScript, deployed via GitHub Pages, with all user working data kept locally in the browser (IndexedDB). It ships three user-facing apps:

- `index.html` (OntoEagle) — the search experience: look up ontology elements (classes, object/datatype/annotation properties, named individuals) across a consolidated ontology collection, filter by namespace and ontology level (Top / Mid / Domain / Application / Knowledge graph), inspect term details, and add terms to a bundle.
- `bundler.html` (Bundler / Slim Builder) — a "shopping cart for ontology terms" that exports a ROBOT seed file for slim-extraction workflows (SLME or MIREOT).
- `cq-ferret.html` (CQ Ferret) — the competency-question workspace (detailed below).

The repo also contains an `ontology-catalog.html`, `ontology-viewer.html`, `vocabulary.html`, and an `about.html`. The bundled ontologies under `src/ontologies` include `bfo-core.ttl`, several CCO files (e.g. `cco-d-acts.ttl`), and a set of domain ontologies (Agent, Artifact, Event, Quality, Geospatial, Time, Units, Cyber, etc.), which signals a BFO/CCO-aligned engineering posture rather than a generic ontology browser.

## Local clone inventory (version/license/author)

- **Author / owner:** Jonathan Vajda. Remote: `https://github.com/jonathanvajda/OntoEagle.git`. Commit author email `36548200+jonathanvajda@users.noreply.github.com`.
- **Version:** `package.json` declares `"version": "0.1.0"`, `"name": "ontoeagle-search"`, `"private": true`, `"description": "Static ontology search app with offline support"`. This is early-stage (0.1.0).
- **License:** GNU General Public License version 3.0 only (`"license": "GPL-3.0-only"` in package.json; full GPLv3 text in `LICENSE`; README confirms GPL v3.0). Note: GPLv3 is copyleft, relevant if we ever fork-and-redistribute.
- **Last activity:** Clone is shallow (single commit `f4a7295` "IRIs in the examples", 2026-05-14). True full history is not visible locally; this is recent and active as of mid-May 2026 [history depth unverified beyond one commit].
- **Tech stack / dependencies:**
  - Build (CI, Python): a single script `src/build_dataset.py` using **RDFLib**. It reads all RDF files from `src/ontologies`, guesses format by extension (.ttl, .rdf, .owl, .nt, .nq, .trig, .jsonld), merges into one `ConjunctiveGraph`, and serializes to `docs/data/graph.jsonld` (and optional N-Quads). RDFLib + mkdocs are the only Python installs in CI.
  - Runtime (client JS, no framework): vendored libraries in `docs/app/` including `rdflib.min.js`, `n3.min.js`, `jsonld.min.js`, `indexeddb.min.js`, `mermaid.min.js`, `tabulator.min.js`, plus pure modules `search.js`, `normalize.js`, `rdf_extract.js`, `ferret.js`, `vocab-extract-core.js`, `slim-core.js`.
  - Tests: **Jest** 29 (the only devDependency) over the pure modules (`normalize`, `search`, `indexer`/`rdf_extract`, `ontology-meta`, `slim-core`).
  - Tutorials: built with **MkDocs** (`mkdocs.tutorials.yml`).
- **Deployment:** GitHub Actions workflow `.github/workflows/lookup.yaml`, three jobs (build → test → deploy) on push to `master`. Build runs the Python consolidation, copies hosted ontology files into `docs/ontologies`, builds tutorials with MkDocs, stamps a service-worker build id, and publishes the entire `docs/` folder to GitHub Pages. Deploy is gated on `master`. So deployment is "fork, drop your ontologies into `src/ontologies`, push" — fully static, no backend.
- **Offline support:** service worker (`docs/sw.js`) precaches the app shell and dataset; IndexedDB stores the index/docs and settings for offline and fast subsequent loads.

## cq-ferret deep dive

**What it is:** CQ Ferret is a competency-question capture and decomposition workspace, not a search engine and not an ontology editor. The tutorial's own framing: it "helps ontology and knowledge-graph teams move competency questions out of Word, PowerPoint, and one-off spreadsheets and into a structured browser workspace." Its FAQ explicitly answers "Is CQ Ferret a replacement for ontology editing tools? No. It is a requirements and knowledge-engineering capture tool."

**Data model (verified, BFO/CCO-aligned):** Each CQ is treated as "an interrogative information content entity" and becomes a small typed hub. The tutorial's Mermaid model types nodes with real IRIs from BFO, CCO, Dublin Core terms, and a project-specific small ontology called **okea** (`https://github.com/jonathanvajda/okea/`, "knowledge-engineering artifact ontology"). Example typing: CQ = `okea:ont000002`, subquestion = `okea:ont000001`, decision logic = `okea:ont000009`, Mermaid diagram = `okea:ont000004`, database query = `okea:ont000016`, contributor = `cco:ont00001262`, data source = `cco:ont00000756`, role via `BFO:has role (BFO_0000023)`. The README and tutorial state the native data model "is aligned with BFO, Common Core Ontologies, and the small knowledge-engineering artifact ontology shipped with this project."

**Workflow (inputs → outputs):**
1. Create a CQ in the form, or import a normalized CSV, or import JSON-LD.
2. Capture supporting metadata: operational context, contributors + roles (Creator/Approver/Reviewer/Executor/SME/Other), decomposition (subquestions + decision logic), relevant data sources + data-quality notes, Mermaid process/ER/design-pattern diagrams (rendered in-page), and **notional SQL or SPARQL query text** attached to each CQ.
3. Track status: Draft / In Review / Approved / Archived.
4. **Vocabulary extraction:** on `vocabulary.html`, "Rebuild from CQ graph" reads the CQ graph from IndexedDB, extracts candidate terms from text-bearing fields, and shows an editable table (`iri`, `label`, `type`, `definition`, `is a`, `is defined by`). Export as normalized CSV.
5. **Exports:** Download JSON-LD (preserves graph structure for loading into an RDF store) and Download/Upload CSV (row-oriented; one row-group per `cq_id`, typed artifact rows via `item_type`). Outputs feed ROBOT or other ontology tools.

**Storage:** local only. IndexedDB database `CQDatabase`, object store `CQStore`. The tutorial states this is a deliberate privacy/cost decision: "it does not store user's data on the web." Multi-user collaboration is by exchanging CSV/JSON-LD files, not shared state.

**Important distinction for our purposes:** the SQL/SPARQL that CQ Ferret holds is *authored query text attached as metadata to a CQ* — it does not execute SPARQL and does not validate CQs against an ontology. The execution story is downstream: export JSON-LD, load into an external graph database, then run SPARQL there (the tutorial gives example status queries like "which CQs are supported by at least one Mermaid diagram and at least one SPARQL query").

## Indexing / SPARQL question (the technical core)

- **OntoEagle search is text/keyword over extracted RDF metadata, not live SPARQL.** The pipeline is: RDFLib consolidates ontology files into one JSON-LD graph at build time → client-side `rdf_extract.js` parses the JSON-LD `@graph` into flat `OntologyDocument[]` (pulling `rdfs:label`, `skos:prefLabel`/`altLabel`, definitions via SKOS or IAO/CCO predicates, citations, examples, subClassOf, domain/range, etc.) → an inverted index is built → `search.js` does pure token scoring (exact IRI/label/altLabel weighted highest, then "contains" matches on label/IRI/definition/citations). So it **does index OWL/RDF** (it understands BFO/CCO/SKOS/IAO annotation predicates) but it **serves a weighted keyword search, not a SPARQL endpoint**. There is no in-browser SPARQL engine; `rdflib.min.js`/`n3.min.js` are used for parsing, not for querying the live UI.
- A "user-supplied graphs" feature (import TTL/OWL/RDF/XML/JSON-LD in-browser and merge) is listed as a **stretch goal and is unchecked** in `lookup-checklist.md` (Stage I); today the dataset is the CI-built consolidation.

## Adopt-into-hive assessment (R016-tagged)

Current OntoEagle status as observed: **(b) demonstrated capability** — it is a working, publicly deployed static tool (CQ Ferret + OntoEagle search are live on GitHub Pages and documented), but it is standalone, not connected to any of our components. Adopting any of it into GI-JOE would be net-new integration work, i.e. moving from (b) to (c).

Three candidate adoption paths, by impedance:

1. **Deployable browse/search UI over our portfolio ontology — quick win, low impedance.** OntoEagle's design (drop RDF into `src/ontologies`, CI runs RDFLib to build `graph.jsonld`, GitHub Pages serves a static keyword search) maps almost directly onto our assets: `portfolio-governance.ttl` (TBox), `portfolio-abox.ttl`, and the OWL/CCO-flavored term set. We already standardize on Python+RDFLib, so the build step is familiar. **Integration cost: low** (fork, point `src/ontologies` at our portfolio TTL, adjust namespace/level filters for our `po:` namespace, deploy). Outcome would be a human-facing browse/search front end for the portfolio ontology — something our current Python gate does **not** provide (the gate is validation, not exploration). R016 target status after this work: **(c) integrated deliverable** for the portfolio, contingent on wiring it to our actual TTL and CI. **Caveat:** GPLv3 copyleft — fine for internal/research use; flag before any redistribution. Also note the upstream branch is `master` (our convention is `main`), a trivial but real fork detail.

2. **CQ Ferret as a CQ-authoring front end — medium impedance, complementary not overlapping.** CQ Ferret and our GI-JOE CQ suite solve *different* halves of the CQ lifecycle. CQ Ferret is **authoring/capture/elicitation** (who asked, decomposition, data sources, draft SPARQL, vocabulary extraction) with export to CSV/JSON-LD. Our 20-query suite + manifest-driven sparql-verifier is **execution/validation** (run `.rq` files against the ontology, check expected values, gate). CQ Ferret produces *draft* SPARQL as untyped text and does not run or validate it; it would not replace our verifier. The realistic value is using CQ Ferret upstream to elicit and organize *new* CQs (with provenance, contributors, decomposition) before we hand-formalize them into our `queries/portfolio/*.rq` + `manifest.yaml`. **Integration cost: medium** — there is a schema-mapping gap (CQ Ferret's okea/CCO JSON-LD vs our `.rq`/manifest format); no automated bridge exists, so the handoff is manual today. R016 status if adopted as-is: stays **(b)** until we build a converter, then **(c)**.

3. **Bundler / slim builder — low priority.** Useful only if we start doing MIREOT/SLME slim extraction from large upstream ontologies (BFO/CCO). Not a current GI-JOE need. **Integration cost: low effort but low value now; defer.**

Net recommendation: path 1 (portfolio browse/search UI) is the strongest quick win and aligns with the standing "Hive-of-Hives Documentation" goal of better surfacing portfolio structure. Path 2 is worth a spike as a CQ-elicitation front end feeding our verifier, but it is a complement, not a replacement, and needs a JSON-LD/CSV → `.rq`/manifest bridge. Do not present any of this as already integrated; all three are (b)→(c) work.

## Competitive / landscape positioning

- **Author:** Jonathan Vajda — an individual GitHub developer (`jonathanvajda`); this is a **personal / individual open-source project** (`"private": true` in package.json refers to npm-publish suppression, not access control; the repo and Pages site are public). No company or lab affiliation is asserted in the clone [organizational affiliation unverified].
- **Community positioning:** clearly situated in the **applied BFO/CCO formal-ontology engineering** community. The bundled `bfo-core.ttl` + CCO ontologies, the IAO definition predicates, the ROBOT/MIREOT/SLME slim workflow, and the tutorial's explicit citations (BFO published as ISO/IEC 21838-2:2021; University at Buffalo note that BFO and CCO are baseline standards in U.S. Department of Defense and Intelligence Community ontology work) all place this squarely in the Barry-Smith / National Center for Ontological Research lineage rather than the generic Semantic Web / Protégé-only world.
- **Tooling niche:** it is *not* competing with reasoners (HermiT/ELK), editors (Protégé), or triplestores (Fuseki/GraphDB). It occupies the lightweight, no-backend, "static-site front end for ontology lookup + CQ capture + slim seeding" niche. Closest conceptual neighbors are Ontology Lookup Service-style browsers (heavy, hosted) and ROBOT (CLI), but OntoEagle's differentiator is zero-server, browser-local, fork-and-deploy.
- **Relevance to us:** directly adjacent to GI-JOE. They share the BFO/CCO orientation and the CQ-as-first-class-artifact philosophy. The complementary fit (their authoring vs our validation) is the most interesting landscape signal — there is no overlap that would make us drop our verifier, but there is a clean upstream/downstream seam.

## Sources

- Local clone: `C:/Users/pfwac/recon-scratch/OntoEagle` — `README.md`, `package.json`, `filesystem.md`, `lookup-checklist.md`, `LICENSE`, `src/build_dataset.py`, `.github/workflows/lookup.yaml`, `src/tutorials/cq-ferret-tutorial.md`, `docs/app/search.js`, `docs/app/rdf_extract.js`, `docs/app/` library listing, `src/ontologies/` listing. Git: remote `https://github.com/jonathanvajda/OntoEagle.git`, commit `f4a7295` (2026-05-14, Jonathan Vajda).
- Live site (WebFetch 2026-05-27): `https://jonathanvajda.github.io/OntoEagle/cq-ferret.html` (CQ Builder UI: status stages, contributor roles, decomposition, data-source matrix, Mermaid context, SPARQL/SQL query area, JSON-LD/CSV export, "Rebuild from CQ graph" vocabulary). `https://jonathanvajda.github.io/OntoEagle/` (Term Lookup / Ontology Catalog: element-type and namespace filters, ontology-level filter, exact + wildcard search over definitions/citations/examples).
- Unverified items flagged inline: full commit history depth (shallow clone), author organizational affiliation, whether the upstream repo has activity beyond the single fetched commit.

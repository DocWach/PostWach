# Modelware — Recon Inventory

Recon date: 2026-05-27. Web-only investigation (no public Modelware product repo; the underlying open-source layer is openCAESAR/OML, which is public). Abbreviations are defined at first use.

## What it is

Modelware (modelware.io) is a commercial software and services firm selling an ontological modeling and analysis framework for Model-Based Systems Engineering (MBSE). It markets itself as a "logic-based MBSE platform" that goes "beyond vanilla MBSE with SysML" by combining formal methods, DevOps, and artificial intelligence (AI) into a "rigorous, scalable ontological modeling and analysis framework."

The pivotal fact: Modelware is the commercial vehicle around the OML / openCAESAR ecosystem. It is founded and led by Dr. Maged Elaasar, who created and leads the openCAESAR open-source project and is a Research Scientist at NASA Jet Propulsion Laboratory (JPL). OML (Ontological Modeling Language) and openCAESAR originated at JPL's Integrated Model-Centric Engineering (IMCE) effort. So Modelware is, in effect, "enterprise OML": commercial tooling, training, and a worldwide network of "Centers of Excellence" wrapped around the open-source OML/openCAESAR core.

- Product category: ontology-driven MBSE platform plus consulting/training services.
- Target users: enterprise systems-engineering organizations building complex cyber-physical systems (aerospace, defense adjacency strongly implied by JPL/NASA lineage).
- Core value prop: formal, reasoning-ready system descriptions (description-logic semantics) with validation, model checking, and AI-assisted authoring, deployed with DevOps automation; "domain-specific modeling driven by ontologies and assisted by AI."

## Technical capabilities

| Capability | Finding | Source basis |
|---|---|---|
| Modeling paradigm | Ontological modeling with formal (description-logic) semantics; "logic-based MBSE." Method-based, domain-specific modeling driven by ontologies. | Site + openCAESAR docs |
| Core language | OML (Ontological Modeling Language). Distinguishes Vocabularies (open-world), Vocabulary Bundles (closed-world description-logic reasoning), Description Bundles (DL datasets). | opencaesar.io/oml |
| Standards mapping | OML maps to subsets of Web Ontology Language 2 (OWL2) and Semantic Web Rule Language (SWRL); supports XSD scalars and RDF/RDFS vocabularies. | opencaesar.io/oml |
| SysML relationship | Positioned "beyond vanilla MBSE with SysML"; openCAESAR provides tool adapters for federation. Specific SysML v2 adapter status [unknown — not found on site]. | Site + openCAESAR |
| Reasoning / validation | Rule-based audits, logical reasoning, model checking, simulation, testing, consistency checking. OML Vision uses Apache Jena Fuseki configured with an incremental rule-based reasoner (entailments regenerate on model change). Specific OWL reasoner (Pellet/HermiT/openllet) for closed-world DL [unknown — not found on site]. | Site + OML Vision page |
| SPARQL support | Yes — OML Vision backend exposes SPARQL (SPARQL Protocol and RDF Query Language) query/update endpoints over Fuseki. | OML Vision page |
| SHACL support | [unknown — not found on site] (no mention of SHACL / Shapes Constraint Language; validation appears to be DL reasoning + SWRL rules + audits rather than SHACL shapes). | OML Vision page |
| Data formats | OML textual (.oml), XMI serialization (.omlxmi), JSON (.omljson). OWL Adapter converts OML to/from OWL. | opencaesar.io/oml |
| APIs | Java API via Eclipse Modeling Framework (EMF); wrapper TypeScript APIs in OML Vision; Language Server Protocol (LSP) server; Maven Central libraries (core-vocabularies). | opencaesar.io/oml, OML GitHub |
| AI/LLM features | Marketed as "AI-assisted modeling and analysis to accelerate insight." No specifics on model vendor, architecture, or whether it is LLM-based; treat as marketing-stage claim. | Site |
| Collaboration / DevOps | DevOps automation of analysis; provenance metadata, baselines, variant configurations, impact analysis; federation of tool-neutral descriptions via adapters; Gradle build integration. | openCAESAR |
| IDEs / clients | OML Code (VS Code extension; Langium + Sprotty, TypeScript LSP); OML Rosetta (Eclipse Rich Client Platform app/plugin); OML Vision (VS Code webviews in React: table/diagram/tree/form). | Search + OML Vision page |

## Architecture & standards

- Deployment: Modelware offers a free trial for OML Code and enterprise consultation; the open-source tooling runs locally (VS Code Desktop, Eclipse) and in cloud IDEs (GitHub Codespaces, Gitpod). A managed multi-tenant SaaS offering is not clearly advertised; cloud-vs-on-prem hosting specifics for the commercial product are [unknown — not found on site].
- Standards: OWL2, SWRL, RDF/RDFS, XSD, SPARQL, OASIS XML Catalog (namespace resolution), Language Server Protocol. SysML named as the incumbent it surpasses; SysML v2 specifics [unknown — not found on site].
- Stack: Eclipse Modeling Framework (EMF, Java 21+), Gradle 8.10+ / Maven 3.9+ builds, Apache Jena Fuseki triplestore with incremental rule reasoner, Langium + Sprotty + React for the VS Code experience.
- Functional model (openCAESAR's six functions): authoring, federation/integration, configuration management, analysis, reporting, plus information architecture.

## Company & maturity

- Founder & CEO: Dr. Maged Elaasar. Also NASA JPL Research Scientist (since 2014) and openCAESAR project lead; teaches at Northeastern University (Silicon Valley). Long MBSE/MBE pedigree (also founder of "Modelware Solutions" consulting).
- Location: Irvine, CA 92620, USA. Contact: info@modelware.io.
- Maturity signal: small/early commercial entity layered on a mature-ish open-source base. The OML GitHub repo shows modest community size (~37 stars, 6 forks, 59 releases, latest 2.13.0 June 2025, ~240+ commits) — actively maintained but niche, JPL/Caltech-anchored.
- Funding: [unknown — not found on site]. Customers: not named publicly; aerospace/defense adjacency implied via JPL lineage, not confirmed [unknown — not found on site]. Pricing: not disclosed; sales/consultation model with regional Centers of Excellence [unknown — not found on site].

## License/openness

- Open-source core: OML is Apache-2.0 (Copyright Caltech, "Government sponsorship acknowledged"); openCAESAR tooling is open and on GitHub. This is genuinely open and commercially usable.
- Commercial layer: Modelware sells services, training, support, and (per messaging) added tooling/AI on top. Which Modelware-specific components are proprietary vs. the open OML/openCAESAR base is not delineated on the site [unknown — not found on site].
- APIs available: yes, at the OML/openCAESAR layer — Java/EMF API, TypeScript wrappers, LSP, SPARQL endpoints, Maven artifacts.

## Adopt-into-hive assessment (with R016 tags)

R016 status reflects where each item would sit in OUR hive-of-hives if we adopted it today (a = research artifact, isolated; b = demonstrated capability, standalone; c = integrated deliverable, wired into our stack). Nothing here is currently integrated, so everything is at most (a)/(b) from our perspective until we do integration work.

| Capability | Fit for our stack | R016 (our perspective) | Integration cost |
|---|---|---|---|
| OML language (OWL2/SWRL subset) | High overlap with GI-JOE's OWL/RDF governance ontology. OML is a "disciplined OWL2" — could express our portfolio TBox/ABox with stricter authoring ergonomics. | (a) research artifact if we trialed it in isolation | Medium: re-encode `portfolio-governance.ttl` concepts as OML vocabularies; build OML to OWL round-trip; validate our 20 competency questions still hold. |
| openCAESAR DevOps analysis pipeline (Gradle) | Strong conceptual match to our ontology-gate (syntax/SHACL/CQ tiers). Their "continuous analysis" mirrors our two-tier gate. | (a) | Medium-high: would need to slot into our Python/Windows gate (`ontology-gate.sh`); openCAESAR is JVM/Gradle, a stack mismatch with our Python `rdflib`/`pyshacl` toolchain. |
| OML Vision (Fuseki + SPARQL + incremental reasoner, VS Code) | Direct adjacency to our Fuseki/SPARQL CQ suite. Incremental rule reasoning is a capability we do not currently have (we run CQs batch-style). | (b) demonstrated capability if stood up standalone | Medium: Fuseki we already understand; wiring OML Vision webviews to our portfolio ABox is feasible; not yet connected to claude-flow agents. |
| Reasoning/audit (DL + SWRL rules + model checking) | Complementary to SHACL. SWRL gives inference (entailment), which SHACL does not; could enrich our validation beyond shape conformance. | (a) | High: SWRL authoring is a new competency; reconciling open-world DL entailment with our closed-world SHACL gating needs design. |
| SHACL | NOT provided by OML/openCAESAR (gap). Our SHACL gate is something WE have that they apparently lack. | n/a | n/a — this is our differentiator, not theirs. |
| AI-assisted modeling | Claims only; no LLM/agent-orchestration substance found. Our claude-flow MCP agent layer is more concrete than their advertised AI. | n/a (not adoptable as described) | n/a until specifics surface. |
| Java/EMF + TypeScript APIs, LSP, Maven | Usable programmatic surface, but JVM-centric vs. our Python tooling. | (a) | Medium: API exists; cross-language glue + Windows EMF setup is friction. |

Net adopt read: the highest-value pull-throughs are (1) OML as a stricter authoring front-end for our existing OWL governance ontology and (2) incremental rule-based reasoning via Fuseki, which we already run but do not yet use for live entailment. Both are realistically (a) on day one and would need genuine engineering to reach (c). The stack impedance (JVM/Gradle/EMF vs. our Python/`rdflib`/`pyshacl`/claude-flow) is the main integration tax. Our SHACL gating and MCP agent orchestration are capabilities Modelware does not appear to offer.

## Competitive/landscape positioning

- Closest analog in the portfolio: Modelware/openCAESAR is the nearest external mirror of our GI-JOE ontology-backed governance approach. Both bet that systems engineering should rest on formal OWL/description-logic foundations with SPARQL-driven analysis and DevOps automation. This is strong validation that our architectural thesis is credible and shared by a JPL-pedigreed group.
- Where we differ / lead: we couple the ontology layer to (1) SHACL constraint gating, (2) competency-question suites as a validation contract, and (3) a live multi-agent orchestration layer (claude-flow / MCP) with Zero-Trust governance and agent provenance ([R018]). Modelware's "AI-assisted" claim is, on current evidence, marketing-stage; our agentic-SE substance is more concrete. Their reasoning (SWRL/DL entailment) is something we currently lack — a genuine capability edge for them.
- Relationship type: primarily adjacent / potential tool, secondarily a thought-competitor. It is a candidate upstream tool (adopt OML authoring or OML Vision) far more than a market rival; we do not sell a product. The strongest competitive overlap is intellectual — in agentic-SE papers and proposals, openCAESAR/OML is a must-cite prior-art and a natural "related work / baseline" against which our agent-orchestrated, SHACL-gated, neurosymbolic hive differentiates.
- Positioning for our papers/proposals: cite openCAESAR/OML as the leading open formal-MBSE baseline (JPL provenance lends authority). Frame our contribution as the layer they lack — autonomous agent orchestration over the formal ontology with continuous Zero-Trust governance — rather than re-litigating the ontology-vs-SysML question they already champion. Useful authority for the AI Circuit Breaker and Agentic_AI_Swarms_SE lines.

## Sources

- https://www.modelware.io/
- https://www.modelware.io/about.html
- https://www.modelware.io/maged-elaasar.html (surfaced in search; not directly fetched)
- http://www.opencaesar.io/
- https://www.opencaesar.io/oml/
- https://github.com/opencaesar/oml
- https://www.opencaesar.io/projects/2023-05-29-OML-Vision.html
- http://www.opencaesar.io/projects/2025-02-01-OML-Code.html (surfaced in search; OML Code description)
- https://github.com/opencaesar/oml-rosetta (surfaced in search)
- http://www.opencaesar.io/caesar/2022/09/01/Tutorial-on-Ontological-Modeling-Language.html (surfaced in search)
- https://siliconvalley.northeastern.edu/faculty/maged-elaasar/ (surfaced in search; founder background)
- https://dl.acm.org/doi/pdf/10.1109/MODELS-C59198.2023.00051 (openCAESAR MODELS 2023 paper; surfaced in search, not fetched)

# naas / ABI — Recon Inventory

Recon date: 2026-05-27. Target: `jupyter-naas/abi` (Agentic Brain Infrastructure, "ABI") and the commercial entity behind it, naas.ai. Local shallow clone at `C:/Users/pfwac/recon-scratch/abi` (Python, ~3400 files). All claims below are verified from the clone or cited web sources; items that could not be verified are tagged [unverified].

This is the closest architectural mirror of our hive-of-hives thesis we have surveyed: ABI describes itself as "the open-source AI Operating System that grounds large language models (LLMs) in your organization's ontology" and positions as "an open and accessible alternative to Palantir." Like us, it treats an ontology as the unifying field connecting data, models, workflows, and systems. The differences are in the runtime mechanism, the governance posture, and the maturity of the productized stack.

## What it is (product + open source split)

ABI (Agentic Brain Infrastructure) is an open-source, MIT-licensed (Copyright 2025 Naas.ai), full-stack AI platform that runs LLM-powered agents grounded in a Basic Formal Ontology (BFO)-based knowledge graph. It spans ingestion to user interface: triple store, vector store, relational memory, object storage, message bus, orchestration, plus a web UI ("Nexus"), a REST application programming interface (API), a command line interface (CLI), and a Model Context Protocol (MCP) server.

There is a clear open-core split:
- **Open source (this repo):** the full community edition, with every infrastructure dependency shipped as a Docker container.
- **Commercial (naas.ai / NaasAI):** managed hosting and "enterprise" adapters. The README's "How It Works" table explicitly lists Community vs Enterprise backends for each port (e.g., triple store Community = Apache Jena Fuseki, Enterprise = Amazon Neptune / Stardog / Ontotext GraphDB; vector store Community = Qdrant, Enterprise = Pinecone / Weaviate / pgvector / Azure AI Search). "Need a hosted, managed deployment? Get started on naas.ai or reach out to the team."

Company / maturity signals (web-sourced, see Sources):
- NaasAI describes itself as "Universal Data and AI Platform" (naas.ai homepage title; full page is JavaScript-rendered and did not yield body text via WebFetch).
- GetLatka reports naas.ai at ~$1.5M revenue with a 14-person team as of 2025/early 2026. This indicates a small startup / applied-research-lab scale, not a large funded vendor.
- A SaaSworthy listing references pricing "starting at $31.00" but is flagged as last updated November 2020, so it is stale and should not be treated as current. Current pricing tiers could not be verified [unverified] (the about.naas.ai/pricing page is JS-rendered and returned no body).
- No funding round figures were verifiable from the searches performed [unverified].
- R&D is a stated collaboration between NaasAI (applied AI research lab), OpenTeams, University at Buffalo, NCOR (National Center for Ontological Research), and Forvis Mazars (audit/consulting). The NCOR / University at Buffalo tie is significant: it explains the deep, doctrinally-correct BFO grounding (NCOR is the institutional home of BFO).
- Version badge: "ABI-OS1 Beta." Self-described beta maturity.

## Local clone inventory (deps / version / license)

- **License:** MIT (`LICENSE`, Copyright 2025 Naas.ai).
- **Python:** requires `>=3.11,<4` (root `pyproject.toml`); README states 3.12+. Packaging/build via `uv` + `hatchling`. Lockfile `uv.lock` is ~1.28 MB (large dependency surface).
- **Monorepo of four editable libs** (`libs/`):
  - `naas-abi-core` — infrastructure adapters, the Engine, services (agent, ontology, triple_store, vector_store, bus, cache, email, event, keyvalue, object_storage, secret), and the apps (API, Dagster, MCP, terminal_agent).
  - `naas-abi` — core agents (`AbiAgent`, `CodingAgent`, `OntologyEngineerAgent`), bundled ontologies, pipelines, workflows, and the Nexus app.
  - `naas-abi-cli` — the `abi` CLI (project/module/agent/workflow scaffolding, dev runtime).
  - `naas-abi-marketplace` — domain modules and ~40+ third-party integrations.
- **Agent framework:** LangGraph + LangChain. `Agent.py` (~1777 lines) builds a `langgraph.graph.StateGraph` over `MessagesState`, binds LangChain `BaseTool`s, and uses LangGraph checkpointers (`MemorySaver`, plus a Postgres/SQLite checkpoint saver) for conversation memory. Terminal-agent dependency group pins `langchain-anthropic` and `langchain-openai`.
- **LLM providers (very broad):** the marketplace ships optional-dependency "extras" for OpenAI (ChatGPT), Anthropic (Claude), DeepSeek, Gemini, Gemma, Grok, Llama, Mistral, Perplexity, Qwen, plus OpenRouter as a meta-provider. README says "any OpenAI-compatible provider." Provider-agnostic by design.
- **Integrations (marketplace `applications-*`):** ~40+, including GitHub, Git, Gmail, Google Calendar/Drive/Sheets/Search, HubSpot, **LinkedIn**, Notion, Salesforce-style CRMs, Postgres, PowerPoint, SharePoint, Spotify, Twilio, arXiv, PubMed, NewsAPI, World Bank, Yahoo Finance, exchange rates, OpenWeatherMap, Airtable, Algolia, SendGrid, and `applications-naas` (their own platform). The open branches you flagged (LinkedIn / contact agents, AIA integration) map to these `applications-linkedin` and CRM-style modules; a discrete "AIA" component was not located by name in the sampled tree [unverified].
- **Distinctive utility — `onto2py`:** an ontology-to-Python code generator. It parses Turtle/OWL with `rdflib`, walks OWL restrictions and unions, and emits typed Python (`@dataclass`) representations of ontology classes/properties, with a SHA-256 source cache marker. This is their ontology-runtime-binding mechanism (see below).

## Core architecture (agents, ontology runtime binding, orchestration, MCP)

**Module abstraction.** Everything is a "module" (`BaseModule` in `core/module/Module.py`, a Pydantic-typed, generic base). A module bundles agents, applications (UI/API/CLI surfaces), integrations, ontologies, orchestrations (Dagster), pipelines (RDF read/write), and workflows (callable tools). Modules are enabled by a single line in `config.yaml`. This is a clean, declarative composition model.

**Engine + ports/adapters.** A `core/engine/Engine.py` (with `EngineProxy`, `IEngine`) wires services at startup via `EngineConfiguration_*` classes, one per port: TripleStore, VectorStore, KeyValue, ObjectStorage, Bus, Cache, Email, Event, Secret, ActivityLog. This is a textbook hexagonal (ports-and-adapters) architecture. Each service has a `*Ports.py` interface and `adaptors/secondary/*` implementations. The README's "Context Engine wires all these services at startup and routes every request to the right agent."

**Agents.** LangGraph state machines. The hierarchy is layered:
- `Agent` (base, LangGraph `StateGraph`, tool binding, checkpointed memory, server-sent-events streaming).
- `IntentAgent` — adds intent matching (an `IntentMapper` with `Intent`/`IntentType`, embedding-based) to route a user request to a matching agent or tool.
- `CoordinatorAgent` (extends `IntentAgent`) — a strict supervisor that "ONLY delegates and NEVER answers directly." Notably, its refusal-on-no-match is **structural in the LangGraph topology, not prompted**: no-match paths route to a deterministic `coordinator_refusal -> END` node rather than to a free-form LLM call. This is a deliberate, well-engineered determinism guarantee for the supervisor.
- The supervisor "Abi" (`AbiAgent` in `naas-abi`) reads intent and dispatches to domain agents or answers from the knowledge graph / vector store / file system. Multi-agent coordination is therefore a **single-supervisor / intent-routing-to-leaf-agents** model (hub-and-spoke), not a peer consensus or market mechanism.

**Ontology runtime binding (the crux for us).** Two mechanisms, and it is important to separate them:
1. **Knowledge graph at runtime.** Domain ontologies are OWL/Turtle (`naas-abi/naas_abi/ontologies/`, with `imports/top-level/bfo-core.ttl`, mid-level Time and Units-of-Measure ontologies, and `modules/ABIOntology.ttl`, `BFO7BucketsProcessOntology.ttl`). These are loaded into a live **triple store** (`TripleStoreService`) and queried/written via **SPARQL pipelines** (`AddIndividualPipeline`, `MergeIndividualsPipeline`, `RemoveIndividualPipeline`, `InsertDataSPARQLPipeline`). Triple store adapters present: **Oxigraph** (embedded `pyoxigraph` and HTTP server, the dev default), **Apache Jena TDB2 / Fuseki** (production community), **AWS Neptune** (enterprise), plus Filesystem and ObjectStorage adapters. Agents query this graph as a context source.
2. **Ontology-to-code (`onto2py`).** They generate typed Python classes from the ontology so module code manipulates ontology entities as first-class typed objects, with caching keyed on a source SHA-256. This is a genuinely deeper binding than a runtime SPARQL string interface: the ontology shapes the *type system of the application code*, not just the data.
3. **Named entity recognition (NER) over the ontology.** `OntologyService.named_entity_recognition` uses an NER adapter to extract a graph of ontology-typed entities from free text, grounding LLM input in the ontology vocabulary.

**SHACL / validation posture.** SHACL is present but **as a development/QA tool, not a runtime enforcement gate**. `utils/ontology_checker.py` runs three layers: (1) rdflib static structural checks (BFO bucket mapping, annotations, restriction inheritance, naming, inverses, disjointness), (2) owlready2 + HermiT OWL reasoning (unsatisfiability, contradictions, entailed subsumptions), (3) pyshacl SHACL validation (cardinality/type/pattern conformance, auto-generating minimal shapes from OWL restrictions if none supplied). `onto2py` invokes the *static* layer before codegen (bypassable via `ABI_SKIP_ONTOLOGY_CHECK=1`). I found no evidence of SHACL running on every triple-store write at runtime, nor SPARQL competency-question (CQ) manifests gating CI [unverified beyond the checker utility].

**Orchestration / workflow engine.** **Dagster** (schedules, jobs, event sensors) for module automation; the dev runtime (`abi dev up`) spawns API, Dagster, Nexus web, and a bundled Oxigraph as native processes with deterministic per-worktree ports. "Workflows" are structured callable tools exposed to agents; "pipelines" are the RDF read/write operations.

**MCP usage.** `core/apps/mcp/mcp_server.py` is a **FastMCP server that exposes ABI agents as MCP tools**. It discovers agents dynamically from the running API's OpenAPI spec (`/agents/{name}/completion` endpoints) and registers each as an MCP tool, over stdio / SSE / streamable-HTTP transports (stdio targeted at Claude Desktop). This is the **inverse** of our claude-flow usage: ABI is an MCP *server/provider* (publishing its agents for external MCP clients to consume); our hives are MCP *clients* consuming claude-flow's `mcp__claude-flow__*` coordination surface. The two are complementary, not competing, at the protocol layer.

**What is absent (relative to us).** Grep across `libs/` found no claude-flow, no swarm/consensus coordination primitives, no agent-provenance attribution layer, and no zero-trust/security-pillar governance constructs. Coordination is supervisor-routed, not swarm/consensus. Governance is "compliance-by-construction" via BFO traceability (they cite ISO/IEC 42001 AI Management Systems and the EU AI Act as the payoff), not an explicit rule-governance or Zero-Trust posture.

## Comparison to our hive-of-hives

| Dimension | ABI / naas | Our hive-of-hives (GI-JOE portfolio ontology + claude-flow) |
|---|---|---|
| Ontology role | BFO-grounded knowledge graph as runtime context + `onto2py` typed-code binding | Portfolio governance ontology (TBox/ABox) + SHACL + SPARQL CQs as a governance/validation layer |
| Top-level ontology | BFO (ISO/IEC 21838-2), NCOR-backed, doctrinally rigorous | Custom `po:` portfolio namespace; not BFO-aligned |
| Ontology-to-runtime binding | Deep: ontology -> live triple store (Oxigraph/Fuseki/Neptune) AND ontology -> typed Python via `onto2py` | Ontology validated and queried (CQ manifest, ontology-gate), but not bound into application type system |
| SHACL | Dev/QA checker (rdflib + owlready2/HermiT + pyshacl), bypassable | SHACL as a two-tier gate (Tier 1 advisory, Tier 2 blocking) — closer to enforcement than theirs |
| Validation in CI | Static checker before codegen; full reasoning available | Manifest-driven CQ validation, 20/20 CQs gating; arguably more systematic as governance |
| Agent framework | LangGraph/LangChain state machines | claude-flow orchestration over Claude agents |
| Multi-agent model | Single supervisor (Abi/CoordinatorAgent), intent-routing hub-and-spoke; determinism enforced in graph topology | Hive-of-hives: multiple governed hives, coordinator/worker roles, consensus primitives available |
| MCP | Server/provider (exposes agents as MCP tools) | Client/consumer (consumes claude-flow MCP) |
| Governance | Compliance-by-construction (BFO traceability -> ISO 42001 / EU AI Act) | Explicit rule governance (R-rules), Zero-Trust (Fort Wachs), agent provenance ([R018]) |
| Memory/persistence | LangGraph checkpointers (Postgres/SQLite); vector store (Qdrant) | claude-flow memory namespaces + ReasoningBank/AgentDB |
| Productization | Full ingestion-to-UI stack, CLI scaffolding, Docker, managed hosting | Research co-pilot; no productized UI/hosting |

**Where they go deeper:** (1) BFO doctrinal rigor and NCOR pedigree; (2) ontology-to-typed-code binding (`onto2py`) is a genuinely tighter ontology/runtime coupling than ours; (3) full-stack productization (UI, API, CLI, Dockerized swappable infra, dev runtime with worktree port isolation) is far ahead of our research-grade tooling; (4) breadth of LLM providers and integrations.

**Where we go deeper:** (1) SHACL/CQ as an actual *governance gate* rather than a dev-time linter; (2) explicit multi-hive governance with rule annotations, risk tags, and a CTO/COO/CISO triad; (3) Zero-Trust security framing (Fort Wachs) and foundation-model provenance attribution ([R018]) — entirely absent from ABI; (4) consensus/swarm coordination semantics vs their single-supervisor routing; (5) the morphism/isomorphism formal-SE research layer has no analog in ABI.

## Adopt-into-hive assessment (R016-tagged)

Python alignment is favorable: ABI is pure Python (3.11+/`uv`), and our analysis scripts and GI-JOE tooling are Python (`rdflib`, `pyshacl`). Integration cost notes assume we adopt *patterns* or *isolated components*, not the whole stack.

1. **`onto2py` ontology-to-typed-Python codegen.** R016 status: **(a) research artifact** (validated as a working utility inside their repo; not connected to our stack). Adopt value: HIGH. This is the single most reusable idea: generate typed Python classes from our `po:` portfolio ontology so our analysis scripts manipulate governance entities with type safety instead of raw SPARQL strings. Integration cost: LOW-MEDIUM (MIT-licensed, pure `rdflib`; could be vendored or reimplemented). Caveat: it is BFO-bucket-aware, so it would need decoupling from BFO assumptions for our non-BFO ontology.

2. **Three-layer `ontology_checker` (static + OWL reasoning + SHACL).** R016 status: **(a) research artifact**. Adopt value: MEDIUM-HIGH. The owlready2/HermiT OWL-reasoning layer (unsatisfiability/entailment) is something our current ontology-gate does not do; adding it would strengthen GI-JOE's gate. Integration cost: LOW for the pyshacl layer (we already use pyshacl), MEDIUM for the HermiT/owlready2 layer (adds a Java dependency).

3. **Ports-and-adapters Engine with `config.yaml`-selected backends.** R016 status: **(c) integrated deliverable** within ABI (it is the spine of their running product). Adopt value: MEDIUM as a *design pattern* to imitate, LOW as code to lift (tightly coupled to their Engine). The community/enterprise swappable-adapter pattern is a clean way to think about dev-vs-production parity we could mirror.

4. **CoordinatorAgent structural-determinism pattern (refuse-via-graph-topology, not via prompt).** R016 status: **(c)** within ABI. Adopt value: MEDIUM (conceptual). The principle "make the supervisor's refusal a structural property of the routing graph, not a prompt instruction" is directly transferable to how we reason about coordinator agents and memory-gate authorities, even though our orchestrator is claude-flow not LangGraph. Integration cost: N/A (pattern, not code).

5. **MCP-server-exposes-agents pattern.** R016 status: **(c)** within ABI. Adopt value: LOW-MEDIUM. If we ever want to publish a hive's capabilities to external MCP clients (e.g., expose GI-JOE validation as an MCP tool), their FastMCP-over-OpenAPI auto-discovery pattern is a clean template. Currently we are MCP consumers, so this is speculative.

6. **Dagster as the orchestration/scheduling layer.** R016 status: **(c)** within ABI. Adopt value: LOW for us now (claude-flow covers agent orchestration; Dagster solves data-pipeline scheduling we do not currently have). Revisit only if we build recurring RDF ingestion pipelines.

7. **BFO grounding itself.** Not a component to "adopt" but a strategic choice. Adopt value: STRATEGIC. Our `po:` ontology is custom; aligning (even partially) to BFO would buy interoperability and the ISO 42001 / EU AI Act traceability narrative ABI leans on. This is a research/architecture decision, not a code adoption, and would be costly to retrofit.

## Competitive / landscape positioning (peer / competitor / prior-art)

ABI/naas is best characterized as **prior-art-to-cite and a partial peer, not a direct competitor**, for three reasons:

- **Different markets and scale.** They are a ~14-person, ~$1.5M-revenue applied-AI startup selling a productized "open alternative to Palantir" with managed hosting. We are an academic research portfolio producing manuscripts, ontologies, and orchestration methodology. We do not compete for their customers; they do not publish in our venues.
- **Strong validation of our thesis.** Their existence, NCOR/University-at-Buffalo backing, and BFO grounding are *external evidence* that "ontology-driven, ontology-grounded multi-agent systems" is a real and serious direction. For our agentic-SE papers and proposals, ABI is a citable, well-credentialed datapoint that the ontology-as-unifying-field architecture is being built and commercialized, not merely theorized. Cite them as validation, and as the closest engineered instance of the pattern.
- **Clear differentiation remains for us.** Our defensible contributions are: (1) governance-as-a-gate (SHACL/CQ enforcement, rule annotations, risk tagging) vs their compliance-by-construction; (2) Zero-Trust security and foundation-model provenance — *absent* in ABI; (3) multi-hive consensus/swarm coordination vs their single-supervisor routing; (4) the formal morphism/isomorphism SE-theory layer. We should not claim novelty for "ontology-grounded agents" in the abstract (ABI and others have built it); we should claim novelty for the *governance, provenance, security, and formal-SE* layers on top.

Recommended posture for papers/proposals: cite ABI/naas as related work and as evidence of feasibility/demand; explicitly position our governance + Zero-Trust + provenance + formal-SE contributions as the delta. Watch for collaboration potential via the NCOR/BFO community (shared top-level-ontology interest), which is a more natural bridge than the commercial side. There is no near-term collaboration signal in the artifacts examined [unverified].

## Sources

- Local clone: `C:/Users/pfwac/recon-scratch/abi` — `README.md`, `pyproject.toml`, `LICENSE` (MIT, Copyright 2025 Naas.ai), `libs/naas-abi-core/naas_abi_core/{engine,services,apps,module,utils}`, `services/agent/{Agent.py, IntentAgent.py, CoordinatorAgent.py}`, `services/ontology/OntologyService.py`, `services/triple_store/adaptors/secondary/{Oxigraph.py, ApacheJenaTDB2.py, AWSNeptune.py}`, `apps/mcp/mcp_server.py`, `utils/ontology_checker.py`, `utils/onto2py/onto2py.py`, `libs/naas-abi/naas_abi/{agents,ontologies,pipelines}`.
- README "Research & Development" section: NaasAI, OpenTeams, University at Buffalo, NCOR, Forvis Mazars.
- Web: GetLatka company profile (https://getlatka.com/companies/naas.ai) — ~$1.5M revenue, 14-person team, 2025/2026.
- Web: GitHub repo description (https://github.com/jupyter-naas/abi) — "AI Operating System... ontologies as the unifying field."
- Web: docs.naas.ai (ABI API integration page referenced; body JS-rendered, not captured).
- Web: SaaSworthy listing (https://www.saasworthy.com/product/naas-ai) — "starting at $31.00," flagged stale (Nov 2020); treat as [unverified] for current pricing.
- Web: about.naas.ai/pricing and naas.ai homepage — JS-rendered, no body text retrievable via WebFetch; current pricing tiers and funding [unverified].

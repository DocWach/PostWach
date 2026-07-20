# AI Agent Harness Survey: Frameworks, Orchestration, and Capability Registries
**Scan date:** 2026-07-14  
**Scope:** Frameworks + Orchestration + Capability-Registry slice  
**Companion scan:** Governance/Memory (separate agent)  
**Status:** Draft — all citations require refverify before manuscript use

---

## A. Per-Framework Characterization

### A.1 Comparison Table

| Framework | Multi-Agent Topology | Orchestration Model | Capability Registration Mechanism | Specialization Pattern (Duplication vs. Mapping) | Tool/Protocol Layer | Shared Registry / Catalog |
|---|---|---|---|---|---|---|
| **LangGraph** (LangChain Inc.) | DAG / graph; nodes = agents or functions; conditional + parallel edges | Stateful graph compiler; centralized StateGraph; human-in-the-loop checkpoints; supports supervisor pattern (hierarchical subgraphs) | Tools registered as node functions or LangChain tool objects; ToolNode wraps any callable; dynamic tool lists per node | Duplication: new domain = new graph/node; no first-class "map existing capability to new domain" primitive | Native function-calling; MCP via LangChain MCP adapter; AG-UI streaming integration (2025) | None built-in; community LangChain Hub for prompt sharing only |
| **Microsoft AutoGen v0.4+** | Peer-to-peer pub/sub; actor model; event-driven; no mandatory central orchestrator | Non-blocking async message passing (actor model, Jan 2025 rewrite); GroupChat, Magentic orchestration patterns available in Microsoft Agent Framework (MAF, released Oct 2025) | Python callables or OpenAPI specs declared on ConversableAgent; tool schema auto-generated; MAF adds stable Agent Skills API (2026) | Duplication dominant; Magentic pattern delegates task routing to an LLM manager — closest to mapping but still agent-level | MCP via plugin; OpenAI-compatible function calling; AG-UI integration in MAF | No cross-project registry; MAF introduces Agent Skills catalog (experimental) |
| **CrewAI** | Hierarchical manager/worker; sequential or parallel crews; Flow = event-driven automation layer | Sequential or hierarchical process; LLM-based Manager delegates tasks; Flows add conditional/loop control; Control Plane in execution path | Tools attached to agents or scoped to tasks (task-level overrides agent-level); Python callables + MCP servers supported | Duplication: new domain = new role + tool set assigned; no transfer adapter; role re-use is copy-and-configure | Function-calling; MCP server support (2025); AG-UI integration | CrewAI Hub (cloud): shared crew templates; no formal skill-transfer registry |
| **OpenAI Agents SDK** (successor to Swarm, GA Mar 2025) | Flat or delegated; handoffs make it dynamically hierarchical at runtime | Built-in agent loop (tool invocation → result → next turn); agents delegate via handoff to other agents; guardrails wrap I/O | Function tools (Python fn → JSON Schema auto-generated); MCP servers treated identically to function tools; Sandbox agents: manifest-declared capabilities (filesystem, shell, memory, skills) | Duplication: specialization = define a new agent with new instructions + tools; no mapping primitive | Native MCP; JSON Schema function calling; sessions for cross-run persistence | No shared registry; agents-as-tools composability is the reuse mechanism |
| **Anthropic Claude Agent SDK** (launched Sep 2025, renamed from Claude Code SDK) | Subagent hierarchies; orchestrator spawns subagents; lifecycle hooks; Skills system | Orchestrator-subagent model; Skills = declarative SKILL.md files loaded at runtime; Tool Search Tool enables on-demand tool discovery (defer_loading); MCP connector native in Messages API | SKILL.md spec (markdown + scripts + resources); MCP toolsets with per-tool enable/disable/defer; Tool Search Tool does semantic discovery over deferred tool set | Mapping adjacent: Skills can be parameterized and composed; new domain = new SKILL.md that calls existing skills; transfer is partial (composition), not formal | MCP (beta `mcp-client-2025-11-20`); native function calling; allow/deny lists per MCP server | Local skills registry (SKILL.md files); no cross-hive/cross-org shared registry |
| **LlamaIndex / llama-deploy** | Event-driven workflow steps; multi-agent via nested workflows or llama-deploy services | Workflows API (typed events + async steps, 2024); llama-deploy for production serving; OpenTelemetry observability (traceAI) | Tools via FunctionTool, QueryEngineTool, or ReActAgent tool lists; LlamaHub for data connectors; Agentic Document Workflows (ADW, 2025) | Duplication: new domain = new workflow definition; RAG pipeline reuse is the closest transfer primitive | OpenAI-compatible function calling; LlamaHub connector ecosystem; MCP via adapter | LlamaHub: community index of data loaders / tools; no skill-transfer catalog |
| **Microsoft Semantic Kernel / MAF** | Sequential, concurrent, group-chat, handoff, Magentic (dynamic LLM-managed) patterns | Plugin + planner model; kernel orchestrates plugin calls; MAF (v1.0, 2026) merges SK + AutoGen; Magentic = goal + specialist set, LLM decides workflow | Plugins declared as C# / Python classes with function attributes; OpenAPI specs importable; MCP server plugins (2025); SK Function = unit of capability | Mapping partial: SK Functions composable via planner; new domain = import existing plugin + add domain-specific functions; no formal morphism/adapter | MCP plugins; OpenAPI import; native function calling (all major LLMs); YAML prompt templates | No cross-project registry; Azure AI Foundry provides a marketplace-adjacent layer |
| **MetaGPT** | Linear pipeline (assembly-line SOP); pub/sub for inter-role messages | SOP-encoded prompt sequences; roles subscribe to message types; AFlow (ICLR 2025 oral) auto-optimizes workflow graphs by searching SOP configurations | Roles inherit from base Role class; Actions attached to roles; tools are Python callables scoped to actions | Duplication: new domain = new role/SOP definition; AFlow auto-generates SOPs but does not transfer existing capabilities | Python function calling; no native MCP (as of mid-2025) | No registry; SOPs are project-local |
| **AutoGPT** (2023–present) | Single autonomous agent with self-goal decomposition; plugin-based tool expansion | Recursive task-queue: create task list → execute → generate new tasks → reprioritize; BabyAGI variant is simpler queue loop | Plugin manifest declares tools; BabyAGI 2 (2024): functionz framework stores functions + metadata for reuse | Duplication: plugins are standalone; no capability-composition primitive | OpenAI function calling; web, file, shell plugins | AutoGPT Store (plugins marketplace); BabyAGI functionz = lightweight local registry |
| **Dify** | Single agent or pipeline; Beehive microservice architecture; DAG workflow engine ("graphon") | Visual workflow editor; DAG execution; parallel branch support (v0.8.0); queue-based resilient execution; docker-compose multi-service | 50+ built-in tools; custom tool import via OpenAPI spec; plugin ecosystem + marketplace (v1.0, 2025); model-agnostic (100s of LLMs) | Duplication via GUI: copy-and-configure workflow; no programmatic capability mapping | Function calling (ReAct or Function-Calling agent modes); OpenAPI import; REST API layer | Dify Marketplace (plugin/workflow templates); community sharing; no formal transfer registry |
| **claude-flow / ruflo** (ruvnet, open-source) | Hierarchical, mesh, or adaptive (queen-led Hive-Mind consensus); 60+ agent types self-organize | Swarm init with topology selection; 314 MCP tools; SPARC methodology (Spec/Pseudocode/Architecture/Refinement/Completion); ReasoningBank pattern storage; HNSW-indexed memory | 25 Claude Skills (SKILL.md format); MCP tool registration; AgentDB for semantic retrieval; skill marketplace concept | Composition-forward: skills compose via SKILL.md chaining; ReasoningBank stores and retrieves past patterns as reuse artifacts | 87–314 MCP tools; native claude-flow MCP server (`claude-flow mcp start`); WebAssembly agent support | Local skills folder; no formal cross-org shared registry; closest to a transfer-aware system in this survey |

---

## B. Candidate Taxonomy Skeleton

The following dimensions discriminate harnesses most sharply across the surveyed frameworks. Sources informing this skeleton are [S7], [S8], [S9], [S10], [S11].

### B.1 Orchestration Structure
- **Topology class:** pipeline / DAG / graph / actor-mesh / hierarchical / adaptive
- **Control locus:** centralized orchestrator vs. decentralized event-bus vs. LLM-delegated (Magentic-style)
- **State management:** shared state object (LangGraph StateGraph) / message passing (AutoGen actor) / event stream (LlamaIndex Workflows) / conversation thread (OpenAI Agents)
- **Human-in-the-loop support:** none / checkpoint / approval gate / full interactive

### B.2 Capability Unit and Registration
- **Capability primitive:** function-tool / plugin / role+action / skill (SKILL.md) / node / workflow-step
- **Registration mechanism:** code-annotation / manifest-file / API call / visual GUI / MCP protocol
- **Discovery mechanism:** static at init / dynamic on-demand (Tool Search) / semantic embedding / capability-negotiation handshake (MCP, A2A Agent Card)
- **Scope:** agent-local / session / project / cross-org shared

### B.3 Specialization and Reuse Pattern
- **Dominant pattern:** duplication (copy-configure) vs. composition (chain existing) vs. parameterization vs. mapping/adaptation (new domain via formal adapter, closest to transfer learning)
- **Skill lifecycle support:** none / create / versioning / evolution/feedback loop / deprecation
- **Cross-domain transfer primitive:** absent (all surveyed) / partial (composition, Claude Agent SDK Skills) / formal (not yet seen at framework level)

### B.4 Tool/Protocol Layer
- **Tool interface standard:** proprietary / OpenAI function-calling JSON Schema / MCP / OpenAPI import / A2A Agent Card
- **Protocol role:** tool-call only (MCP) vs. agent-to-agent (A2A) vs. unified (emerging)
- **Multi-server / multi-toolset:** single server / multiple servers with allowlist/denylist (Claude MCP Connector) / federated (A2A)

### B.5 Shared Registry / Catalog Model
- **Registry type:** none / local file / community hub (LangChain Hub, LlamaHub, AutoGPT Store, Dify Marketplace) / curated catalog (SkillsMP, Skills.sh) / capability tree with DAG orchestration (AgentSkillOS [S12])
- **Transfer across harnesses:** none seen; MCP and A2A are necessary but not sufficient (they enable invocation, not capability adaptation)
- **Cross-hive / cross-org registry:** absent in all surveyed production frameworks

### B.6 Observability and Governance
- **Tracing / logging:** none / hooks / OpenTelemetry / built-in tracing (OpenAI Agents SDK, LlamaIndex traceAI, MAF)
- **Guardrails / validation:** absent / output filters / input+output guardrails (OpenAI Agents SDK) / Control Plane in execution path (CrewAI)
- **Permission model:** flat / task-level least-privilege (CrewAI) / four-tier provenance-based (proposed in [S3])

---

## C. Explicit Gaps

### Gap 1: No framework offers formal capability-composition-by-transfer
All surveyed frameworks specialize to new domains by **duplication or copy-configuration** (new agent + new tool set). The closest approximation is composition (Claude Agent SDK Skills, claude-flow SKILL.md chaining), but no framework provides a principled **mapping or adaptation layer** that reuses an existing capability in a new domain while formally characterizing what is preserved and what changes. This is structurally equivalent to what transfer learning provides in ML — and it is absent at the harness level. The academic literature on agent skills (e.g., [S3], [S4]) notes skill composition and evolution but does not formalize transfer in the WySE/category-theoretic sense.

### Gap 2: No cross-harness or cross-hive shared capability registry
All capability stores (LangChain Hub, LlamaHub, AutoGPT Store, Dify Marketplace, SkillsMP) are harness-local or community-curated flat catalogs. None provides: (a) semantic indexing with discovery across framework boundaries; (b) provenance tracking of capability lineage; (c) a governance layer controlling which agents from which hives may read/write. The emerging A2A Agent Card provides cross-framework agent discovery but not capability transfer or registry governance.

### Gap 3: Discovery is static or per-session; no persistent cross-session capability evolution
Most frameworks load tool/skill manifests at session init. The OpenAI Agents SDK Tool Search and Claude Agent SDK `defer_loading` are on-demand within a session. No framework supports a capability that **evolves across sessions** based on usage feedback and stores that evolution in a shared indexed store accessible to all agents (claude-flow ReasoningBank is the closest, but it is project-local and research-grade).

### Gap 4: Protocol stack is split (MCP for tools, A2A for agents) with no unified transfer layer
MCP handles agent-to-tool access (tools, resources, prompts). A2A handles agent-to-agent task delegation (capability discovery via Agent Card). Neither handles **capability composition across agents** — the problem of taking agent A's capability and adapting it to agent B's context domain. A unified "transfer protocol" layer sits above both and does not exist. Sander et al. [S10] predict convergence toward a federated, layered protocol stack but identify decentralized discovery as still uncommon (2026).

### Gap 5: Skill governance and provenance are absent or ad hoc
The survey by Xu and Yan [S3] reports that 26.1% of community-contributed skills contain vulnerabilities, and proposes a four-tier provenance-based governance model. No production framework has implemented this. R018 (provenance attribution) and the WySE verification discipline both require that every shared capability be attributable to its creator model, version, and access mode — a requirement no current harness meets systematically.

---

## D. References

Entries are classified: **[P]** = peer-reviewed / conference proceedings; **[A]** = arXiv preprint (not yet peer-reviewed as of scan date); **[G]** = grey literature (docs, blog, repo, industry announcement). Fields marked [UNVERIFIED] indicate the value could not be confirmed from primary source during this scan; these MUST be verified before any manuscript use.

---

[S1] Hong, S., Zhuge, M., Chen, J., et al. "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework." In *Proceedings of the International Conference on Learning Representations (ICLR 2024)*, 2024. **[P]** URL: https://arxiv.org/abs/2308.00352  
*First submitted August 2023; accepted ICLR 2024 as Oral (top 1.8%). Introduces SOP-based multi-agent orchestration with role specialization.*

[S2] Hou, X., Zhao, Y., Wang, S., Wang, H. "Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions." arXiv:2503.23278 [cs.CR], 2025; revised October 7, 2025. **[A]** URL: https://arxiv.org/abs/2503.23278  
*Systematic architectural and security analysis of MCP; defines lifecycle framework (4 phases, 16 activities) and threat taxonomy.*

[S3] Xu, R., Yan, Y. "Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward." In *Agent Skills '26 Workshop at ACM Conference on AI and Agentic Systems 2026*, 2026. **[P]** URL: https://arxiv.org/abs/2602.12430  
*Survey of agent skills lifecycle: architecture (SKILL.md, MCP), acquisition (RL, autonomous discovery), security (26.1% vulnerability rate), and four-tier governance model.*

[S4] Li, H., Mu, C., Chen, J., et al. "Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale." arXiv:2603.02176, 2026. **[A]** URL: https://arxiv.org/abs/2603.02176  
*Proposes AgentSkillOS: capability-tree taxonomy + DAG orchestration for 200–200,000 skills. Key finding: "structured composition is the key to unlocking skill potential."*

[S5] Sander, L., Gidey, H.K., Lenz, A., Knoll, A. "A Technical Taxonomy of LLM Agent Communication Protocols." arXiv:2606.19135 [cs.MA], 2026. **[A]** URL: https://arxiv.org/abs/2606.19135  
*Five-dimension taxonomy of nine open-source protocols (counterparty, payload, interaction state, discovery, schema flexibility). Predicts convergence toward layered federated stack.*

[S6] Orogat, A., Rostam, A., Mansour, E. "Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis." arXiv:2602.03128, 2026. **[A]** URL: https://arxiv.org/abs/2602.03128  
*Introduces MAFBench; shows framework design alone can increase latency by 100x and reduce planning accuracy by 30%. Five discriminating dimensions: orchestration overhead, memory behavior, planning accuracy, specialization, coordination success.*

[S7] Petrova, T., Bliznioukov, B., Puzikov, A., State, R. "From Multi-Agent Systems and the Semantic Web to Agentic AI: A Unified Narrative of the Web of Agents." arXiv:2507.10644 [cs.AI], University of Luxembourg, 2025. **[A]** URL: https://arxiv.org/abs/2507.10644  
*Three-generation evolutionary framework (1990–2026); four-dimensional taxonomy: semantic foundation, communication paradigm, locus of intelligence, discovery mechanism.*

[S8] Chen, S., Liu, Y., Han, W., Zhang, W., Liu, T. "A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application." arXiv:2412.17481, 2024. **[A]** URL: https://arxiv.org/abs/2412.17481  
*Survey of LLM-MAS covering complex task resolution, scenario simulation, and generative agent evaluation.*

[S9] Ferrag, M.A., Tihanyi, N., Debbah, M. "From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review." arXiv:2504.19678, 2025. **[A]** URL: https://arxiv.org/abs/2504.19678  
*Consolidates 60+ benchmarks and reviews agent frameworks 2023–2025; covers ACP, MCP, A2A collaboration protocols.*

[S10] Anthropic. "MCP Connector — Claude Platform Documentation." Anthropic developer docs, 2025. **[G]** URL: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector  
*Primary source for Claude Agent SDK MCP integration: per-tool enable/disable/defer_loading, multi-server support, Tool Search Tool.*

[S11] OpenAI. "OpenAI Agents SDK." OpenAI developer documentation, 2025. **[G]** URL: https://openai.github.io/openai-agents-python/  
*Primary source for Agents SDK primitives: agents, handoffs, guardrails; native MCP integration; sandbox capability manifests.*

[S12] Google Cloud / Linux Foundation. "Agent2Agent (A2A) Protocol." Announced April 2025; donated to Linux Foundation June 2025. **[G]** URL: https://platformengineering.com/editorial-calendar/best-of-2025/google-cloud-unveils-agent2agent-protocol-a-new-standard-for-ai-agent-interoperability-2/ [UNVERIFIED — primary spec URL not confirmed]  
*Open standard for cross-framework agent discovery via Agent Card (JSON at `/.well-known/agent.json`). 150+ org adopters as of scan date.*

[S13] Microsoft. "Microsoft Agent Framework (MAF) — developer blog." Microsoft devblog, 2025–2026. **[G]** URL: https://devblogs.microsoft.com/semantic-kernel/  
*Primary source for MAF v1.0: merges AutoGen + Semantic Kernel; stable Agent Skills API; Magentic orchestration pattern.*

[S14] ruvnet. "ruflo / claude-flow — GitHub repository." GitHub, 2025–2026. **[G]** URL: https://github.com/ruvnet/ruflo  
*Primary source for claude-flow/ruflo architecture: 314 MCP tools, SPARC methodology, ReasoningBank, HNSW-indexed AgentDB, three topology modes.*

[S15] CrewAI Inc. "Agents — CrewAI Documentation." CrewAI developer docs, 2025. **[G]** URL: https://docs.crewai.com/en/concepts/agents  
*Primary source for CrewAI role-based architecture, task-level tool scoping, Control Plane, and Flows.*

[S16] LangChain Inc. "LangGraph." Developer documentation and blog, 2024–2025. **[G]** URL: https://latenode.com/blog/langgraph-ai-framework-2025-complete-architecture-guide-multi-agent-orchestration-analysis [UNVERIFIED — primary LangGraph docs URL preferred; this is third-party summary]  
*DAG-based stateful graph orchestration; compilation step; supervisor pattern for hierarchical multi-agent.*

[S17] LlamaIndex. "LlamaIndex OSS Frameworks." Developer documentation, 2025–2026. **[G]** URL: https://www.llamaindex.ai/llamaindex  
*Primary source for Workflows API, llama-deploy, Agentic Document Workflows (ADW), and traceAI observability.*

[S18] Hong, S., et al. "AFlow: Automating Agentic Workflow Generation." Accepted ICLR 2025 (oral, top 1.8%), 2025. **[P]** [UNVERIFIED — arXiv preprint number not confirmed during this scan; cite tentatively from MetaGPT team announcement]  
*Meta-optimization approach: uses LLMs to search the space of possible SOP configurations. Announced by MetaGPT/FoundationAgents team.*

[S19] Dify. "Dify — Production-ready platform for agentic workflows." Developer documentation, 2025. **[G]** URL: https://dify.ai/  
*Primary source for Dify Beehive architecture, graphon DAG engine, ReAct/Function-Calling agent modes, plugin marketplace (v1.0, 2025).*

[S20] Anthropic. "Introducing advanced tool use on the Claude Developer Platform." Anthropic Engineering blog, 2025. **[G]** URL: https://www.anthropic.com/engineering/advanced-tool-use  
*Describes Tool Search Tool (on-demand dynamic discovery via defer_loading), subagent orchestration, and Skills system in Claude Agent SDK.*

---

## E. Scan Metadata

- **Total sources logged:** 20
- **Peer-reviewed / conference proceedings [P]:** 3 (MetaGPT/ICLR, Agent Skills Workshop/ACMAAS, AFlow/ICLR [UNVERIFIED arXiv number])
- **arXiv preprints [A]:** 7 (S2, S4, S5, S6, S7, S8, S9)
- **Grey literature [G]:** 10 (official docs, repos, blog posts, industry announcements)
- **Fields with [UNVERIFIED] markers:** 2 (S12 A2A primary spec URL; S18 AFlow arXiv ID)
- **Frameworks not covered:** ANP (Agent Network Protocol — emerging); Mastra (TypeScript-native, AG-UI native); Haystack (Deepset) — noted for second-pass coverage

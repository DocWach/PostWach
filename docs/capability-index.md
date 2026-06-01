# Cross-Project Capability Index

**Maintained by:** PostWach (CTO / Chief Scientist role)
**Created:** 2026-02-24
**Purpose:** Enable reuse discovery and prevent capability duplication across the research portfolio
**Review cycle:** Monthly (aligned with project-registry.md)

---

## Common Infrastructure Pack

Skills and agents that ship with the claude-flow template. Listed once here; not repeated per project.

### Common Skills (~36 available)

| Category | Skills | Notes |
|---|---|---|
| AgentDB | agentdb-advanced, agentdb-learning, agentdb-memory-patterns, agentdb-optimization, agentdb-vector-search | Memory/vector infrastructure |
| GitHub | github-code-review, github-multi-repo, github-project-management, github-release-management, github-workflow-automation | Repository operations |
| Swarm/Hive | swarm-advanced, swarm-orchestration, hive-mind-advanced | Multi-agent coordination |
| ReasoningBank | reasoningbank-agentdb, reasoningbank-intelligence | Adaptive learning |
| Flow Nexus | flow-nexus-neural, flow-nexus-platform, flow-nexus-swarm | Cloud platform integration |
| V3 | v3-cli-modernization, v3-core-implementation, v3-ddd-architecture, v3-integration-deep, v3-mcp-optimization, v3-memory-unification, v3-performance-optimization, v3-security-overhaul, v3-swarm-coordination | Claude-flow v3 development |
| Utility | agentic-jujutsu, browser, hooks-automation, pair-programming, performance-analysis, skill-builder, sparc-methodology, stream-chain, verification-quality | General tooling |

### Common Agent Directories (~17 directories, ~90-100 agents)

analysis, architecture, consensus, core, data, development, devops, documentation, flow-nexus, github, goal, hive-mind, neural, optimization, sparc, swarm, templates, testing

Plus standalone: base-template-generator.md

### Infrastructure Coverage by Project

| Project | Common Skills | V3 Skills | Flow Nexus | Browser |
|---|---|---|---|---|
| PostWach | 35 | Yes (9) | Yes (3) | Yes |
| MACQ | 29 | Yes (9) | No | No |
| GI-JOE | 36 | Yes (9) | Yes (3) | Yes |
| COSYSMO | 26 | No | Yes (3) | No |
| SysMLv2 | 34 | Yes (9) | Yes (3) | No |
| SEAD | 26 | No | Yes (3) | No |
| PLM | 29 | Yes (9) | No | No |
| BP Marketing | 26 | No | Yes (3) | No |
| Fort Wachs | ~26 | No | No | No |
| Claude_code_test_setup | 26 | No | Yes (3) | No |

---

## Domain-Specific Capabilities by Project

### PostWach — SE Math Foundations & Research Methods

**75 domain-specific skills** across four capability groups:

**Mathematics Library (48 skills by MSC classification):**
abstract-algebra, algebraic-geometry, algebraic-topology, approximation-theory, category-theory, combinatorics, complex-analysis, computability-theory, control-theory, data-management, difference-equations, differential-geometry, formal-proof, fourier-analysis, functional-analysis, game-theory, general-topology, geometry, global-analysis, graph-theory, information-theory, integral-equations, integral-transforms, k-theory, lie-algebras, lie-groups, linear-algebra, mathematical-biology, mathematical-modeling, mathematical-physics, measure-theory, model-theory, number-theory, numerical-methods, ode-dynamical-systems, optimization, order-theory, pde-methods, potential-theory, probability-statistics, quantum-mechanics, real-analysis, set-theory, several-complex-variables, special-functions, universal-algebra

**Research Methodology (10+ skills):**
citation-manager, grant-writing, impact-tracker, latex-typesetting, reproducibility, research-portfolio-optimizer, research-roadmapping, research-writing, stakeholder-analysis, systematic-literature-review

**Philosophy of Inquiry (7+ skills):**
dialectical-synthesis, emergence-detection, emergent-inquiry, epistemic-inquiry, ethical-deliberation, evidence-synthesis, experimental-design, inquiry-method, knowledge-mapping, network-knowledge, practical-reasoning, process-tracing, reflexive-monitoring, systems-mapping, value-alignment

**Cross-Domain Analysis (3 skills):**
biomimetics-analyst, transfer-learning-analyst, cognitive-study-designer

**59 domain-specific agents:**
- Mathematics (23): agents per MSC branch — algebraists, analysts, topologists, logicians, etc.
- Philosophy (28): epistemology (6), ethics (5), hybrid (7), pragmatism (5), process (5)
- Research (8): methodology-advisor, research-architect, research-synthesizer, literature-reviewer, publication-strategist, peer-review-responder, collaboration-coordinator, psychometrics-analyst
- Custom (1): test-long-runner

**Portfolio Tooling (demonstrated capability):**
- **PaperBanana** — automated academic figure generation. `paperbanana 0.1.0`; ships an MCP server (`paperbanana-mcp`) plus 3 Claude Code skills (`generate-diagram`, `generate-plot`, `evaluate-diagram`). Planner→Stylist→Critic→Visualizer pipeline with iterative refinement; image model `gemini-3-pro-image-preview` (nano-banana Pro). **R016 status: (b) demonstrated capability** including the multi-iteration refinement loop — figures rendered 2026-05-21 (mass-spring-damper ↔ series RLC, and RC ↔ hydraulic tank-pipe morphisms; tool-generated, physically correct). Requires a billed `GOOGLE_API_KEY` (image generation spends paid Gemini quota).
  - **VLM model must be `gemini-2.5-flash-lite`** (set in `.mcp.json` `VLM_MODEL`, or `--vlm-model` on the CLI). The package default `gemini-2.0-flash` is 404 for new Cloud projects, and full thinking models (`gemini-2.5-flash`) silently truncate the critic's JSON output (thinking tokens consume the 4096 budget), which disables the refinement loop. `-lite` has thinking off by default → complete JSON → working critic/refinement.
  - **Known limitation:** the pipeline returns the *last* iteration, not a score-selected best; image regeneration is stochastic text-to-image (no img2img conditioning on the prior frame), so refinement usually improves but can occasionally regress.
  - Hosted in PostWach; available portfolio-wide for any manuscript needing figures.

### GI-JOE — Ontology Engineering

**12 domain-specific skills:**
- knowledge-graph, oml-description, oml-owl-converter, oml-project-generator,
  oml-validation, oml-vocabulary, ontology-evaluation, ontology-evaluation-swarm,
  ontology-expert, ontology-validation, owl-export, semantic-reasoning, sparql-query

**5 domain-specific agents:**
- ontology-swarm-coordinator — multi-agent ontology evaluation orchestration
- ontology-alignment — ontology mapping and alignment
- ontology-evaluator — ontology quality assessment
- ontology-metrics — quantitative ontology metrics
- ontoclean-validator — OntoClean metaproperty validation (rigidity, identity, unity, dependence)

**Ontology validation infrastructure (2026-03-07):**
- `scripts/validate-ontology.py` — 4-layer validation suite (syntax, OWL RL reasoning, SHACL, SPARQL CQs)
- `ontologies/imports/bfo.owl` — Local BFO 2020 (ISO 21838-2), 35 classes
- `ontologies/imports/cco-merged.ttl` — Local CCO (Common Core Ontologies), 1,539 classes
- `ontologies/shapes/` — SHACL shape files for structural validation
- `ontologies/queries/` — SPARQL competency query library

**STOIC ontology family (2026-03-07):**
- ~~`ontologies/domain/stoic-gst.ttl` — General Systems Theory core~~ — **ARCHIVED 2026-04-23** (wrong approach; GST re-framed for SE through WySE, with T3SD and DEVS as the operational formalisms)
- `ontologies/domain/stoic-devs.ttl` — DEVS/TMS formalization (v0.4.0, 69+ classes, stochastic DEVS, SES, EF)
- `ontologies/domain/stoic-t3sd.ttl` — Wymore's T3SD (v0.2.0, SDR, 3 cotyledon spaces, design elaboration, IA)
- `ontologies/domain/stoic-bridge.ttl` — T3SD↔DEVS correspondence (v0.1.0, gap declarations, convergence recommendations)

### MACQ — Defense Acquisition

**10 domain-specific skills** (under `acquisition/`):
- acquisition-lifecycle — AAF pathway and phase management
- acquisition-training — DAWIA training delivery (35 scenarios)
- deliverable-generator — 50+ template-based document generation (ICD, CDD, SEP, TEMP, etc.)
- document-automation — automated document workflow and formatting
- far-compliance-checker — FAR/DFARS compliance validation (95 clause rules)
- ipt-assembler — IPT swarm assembly (OIPT, WIPT, SEIPT, SST)
- milestone-readiness — gate criteria checking (MDD, MS A/B/C, FRP)
- pathway-selector — interactive AAF pathway selection wizard
- persona-router — role-based perspective switching (12 personas)
- protest-prevention — GAO/COFC case law mapping (34 risk indicators)

**52 domain-specific agents:**
- Roles (16): program-manager, deputy-program-manager, chief-engineer, systems-engineer, contracting-officer, cost-estimator, financial-manager, cybersecurity-lead, legal-counsel, logistician, quality-assurance, risk-manager, schedule-analyst, small-business-specialist, test-eval-lead, config-manager
- Swarms (19): milestone-a/b/c-review, dbs-bcac-swarm, emd-swarm, frp-review, msa-swarm, mta-rapid-field-swarm, mta-rapid-proto-swarm, os-swarm, pd-swarm, services-swarm, software-execution-swarm, software-planning-swarm, te-iot-readiness-swarm, te-resource-coordination-swarm, te-temp-development-swarm, tmrr-swarm, uca-swarm
- Oversight (7): congressional-oversight, contractor-industry, dote, dtea, executive-nsc, peo-mda, trmc
- Archetypes (10): contracts-lead, document-generation-swarm, executive, finance-lead, gate-review-swarm, phase-execution-swarm, program-lead, quality-lead, technical-lead, vv-lead

### COSYSMO — Cost Estimation

**1 domain-specific skill:** `cosysmo-estimation`

**6 domain-specific agents:**
- Specialists (2): effort-multiplier-analyst, size-driver-analyst
- Core domain (4): cost-analyst, estimation-queen, historical-learner, sensitivity-analyst

### SysMLv2 — SysML v2 Modeling

**3 domain-specific skills:**
- sysml-grammar-development
- sysml-library-integration
- sysml-semantic-analysis

**0 domain-specific agents** (sysml agent directory exists but is empty)

### Fort Wachs -- Security Operations (CISO)

**3 domain-specific skills:**
- security-posture -- cross-hive ZT posture assessment (read-only audit of configs, Dockerfiles, CI pipelines)
- vendor-evaluation -- structured vendor comparison with evidence collection (Chainguard pattern)
- compliance-mapper -- map portfolio state to CMMC 2.0, NIST 800-171, NSA ZT frameworks

**3 domain-specific agents:**
- threat-modeler -- STRIDE analysis and attack surface mapping per hive
- compliance-auditor -- audit hive configurations against ZT policies (read-only)
- vendor-evaluator -- structured vendor assessment with cost-benefit analysis

### SEAD — Software Engineering, Architecture, Development, Deployment, Operations, and Security

**3 domain-specific skills:**
- sead-codebase-analysis
- sead-iac-generator
- sead-monitoring-setup

**5 domain-specific agents:**
- sead-orchestrator — coordinates the S/E/A/D decomposition
- s-agent, e-agent, a-agent, d-agent — one per SEAD phase

### PLM — Product Lifecycle Management

**1 domain-specific skill:** `plm`

**8 domain-specific agents:**
- queen (coordinator), bom-manager, change-control, compliance, cost-estimator, requirements-manager, risk-analyst, supplier-manager

**Note:** Uses older CLI pattern; skill may need modernization.

### BP Marketing — Marketing & Visual Content

**2 domain-specific skills:** `marketing-orchestration`, `visual-creative`

**12 domain-specific agents:**
- Marketing (7): analytics-specialist, brand-strategist, campaign-strategist, content-creator, email-marketer, market-researcher, social-media-manager
- Visual (5): ai-art-director, data-viz-specialist, graphic-designer, presentation-designer, video-creator

---

## Cross-Project Reuse Opportunities

| Opportunity | Source Project | Consumer Project | Status |
|---|---|---|---|
| Ontology for SE Morphisms | GI-JOE | PostWach (Idea 9) | Active — STOIC family (2026-03-07) |
| Ontology validation infrastructure | GI-JOE | Any project with .ttl/.owl | Available now (2026-03-07) |
| BFO/CCO local imports | GI-JOE | Any BFO-aligned project | Available now (2026-03-07) |
| STOIC-DEVS for SE Morphisms | GI-JOE | PostWach (Idea 9) | In development |
| SysML v2 Grammar/Semantics | SysMLv2 | PostWach (Idea 1) | Newly identified |
| Cost Estimation for Portfolio | COSYSMO | PostWach (portfolio optimizer) | Newly identified |
| SE Analysis for Verification | SEAD | PostWach (Idea 14) | Newly identified |
| Math/Research Methods for all | PostWach | Any project | Available on request |
| Acquisition Context for Verification | MACQ | PostWach (Ideas 15-19) | Newly identified |
| PLM Cost Estimation | PLM (cost-estimator) | COSYSMO | Potential overlap — review |
| ZT security policy framework | Fort Wachs | All hives | New -- Fort Wachs provides policy, hives implement |
| Chainguard vendor decision | Fort Wachs | SEAD (implementation) | New -- transferred from SEAD |
| Compliance mapping for grants | Fort Wachs | PostWach (DARPA CLARA), MACQ (NNSA) | New -- security credibility narrative |
| Academic figure generation (PaperBanana) | PostWach | Any project with manuscripts | Demonstrated (b) — 2026-05-21 |

---

## Duplicate / Overlap Watch

| Finding | Projects | Classification | Action |
|---|---|---|---|
| `cost-estimator` agent | MACQ (acquisition role), PLM (PLM domain) | Complementary — different domain contexts | No action; domain-specific implementations are appropriate |

*This section is populated by the cross-project-reviewer skill during reviews. Initially sparse; grows over time.*

---

## Review Log

| Date | Reviewer | Changes |
|---|---|---|
| 2026-02-24 | PostWach CTO (initial) | Created index from full capability exploration across all projects |
| 2026-03-07 | PostWach CTO | GI-JOE: added 12 skills, validation infrastructure, STOIC ontology family, 4 cross-project reuse entries |
| 2026-03-10 | PostWach CTO | Add Fort Wachs (CISO): 3 skills, 3 agents, 3 cross-project reuse entries |
| 2026-05-21 | PostWach CTO | Add PaperBanana (figure generation) as PostWach demonstrated capability (b); cross-project reuse entry |

---

*Maintained by PostWach (CTO role). Monthly review cycle.*

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

### GI-JOE — Ontology Engineering

**0 domain-specific skills** (ontology capability is entirely agent-based)

**5 domain-specific agents:**
- ontology-swarm-coordinator — multi-agent ontology evaluation orchestration
- ontology-alignment — ontology mapping and alignment
- ontology-evaluator — ontology quality assessment
- ontology-metrics — quantitative ontology metrics
- ontoclean-validator — OntoClean metaproperty validation (rigidity, identity, unity, dependence)

**Infrastructure:** OWL/RDF/SPARQL processing, BFO alignment, OML workflow, semantic reasoning, knowledge graph construction

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

### SEAD — Systems Engineering Analysis & Design

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
| Ontology for SE Morphisms | GI-JOE | PostWach (Idea 9) | Documented in capability_roadmap.md Phase 5 |
| SysML v2 Grammar/Semantics | SysMLv2 | PostWach (Idea 1) | Newly identified |
| Cost Estimation for Portfolio | COSYSMO | PostWach (portfolio optimizer) | Newly identified |
| SE Analysis for Verification | SEAD | PostWach (Idea 14) | Newly identified |
| Math/Research Methods for all | PostWach | Any project | Available on request |
| Acquisition Context for Verification | MACQ | PostWach (Ideas 15-19) | Newly identified |
| PLM Cost Estimation | PLM (cost-estimator) | COSYSMO | Potential overlap — review |

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

---

*Maintained by PostWach (CTO role). Monthly review cycle.*

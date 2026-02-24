# Cross-Project Registry

**Maintained by:** PostWach (CTO / Chief Scientist role)
**Created:** 2026-02-24
**Review cycle:** Monthly
**Next review:** 2026-03-24

---

## Classification Key

| Field | Values |
|---|---|
| **Tier** | 1 (Active Research) / 2 (Support) / 3 (Archive) |
| **Governance** | V3 (annotated rules, risk tags) / SPARC (boilerplate config) / None |
| **Status** | Active / Maintenance / Dormant / Archive |

---

## Tier 1: Active Research

### 01 PostWach

- **Purpose:** SE math foundations — formal isomorphisms/morphisms across engineering domains
- **Domain:** Systems engineering, category theory, mathematical modeling
- **Governance:** V3 [R101-R107]
- **Skills:** 110 total (75 domain-specific: 48 math library by MSC, 10+ research methodology, 7+ philosophy of inquiry, cross-domain analysis)
- **Agents:** 237 total (23 mathematics, 28 philosophy, 8 research, 1 custom, ~177 common infrastructure)
- **Status:** Active
- **Research relevance:** Primary for Ideas 1-8, 10-14, 20-25; supporting for Idea 9 (with GI-JOE)
- **Key assets:** Isomorphism library (`Papers/SE_Math_Foundations/`), capability roadmap, 25-idea portfolio, research-portfolio-optimizer

### 04 MACQ

- **Purpose:** Defense acquisition lifecycle modeling and decision support
- **Domain:** DoD acquisition (DBS, MTA, software pathway), program management
- **Governance:** V3 [P001-P007]
- **Skills:** 30 total (10 domain-specific under `acquisition/`: acquisition-lifecycle, acquisition-training, deliverable-generator, document-automation, far-compliance-checker, ipt-assembler, milestone-readiness, pathway-selector, persona-router, protest-prevention)
- **Agents:** 145 total (52 domain-specific: 16 acquisition roles, 19 acquisition swarms, 7 oversight bodies, 10 archetypes)
- **Status:** Active
- **Research relevance:** Supporting for Ideas 15-19 (verification in acquisition context)
- **Key assets:** Full acquisition pathway swarms (DBS, MTA, milestones A/B/C), 50+ deliverable templates, 95 FAR/DFARS compliance rules, oversight body agents

### 05 GI-JOE

- **Purpose:** Ontology engineering platform — OWL/RDF/SPARQL, BFO alignment, semantic reasoning
- **Domain:** Ontology engineering, knowledge representation
- **Governance:** V3 [G001-G007]
- **Skills:** 36 total (0 domain-specific skills; ontology capability is agent-based)
- **Agents:** 116 total (5 domain-specific: ontology-swarm-coordinator, ontology-alignment, ontology-evaluator, ontology-metrics, ontoclean-validator)
- **Status:** Active
- **Research relevance:** Primary for Idea 9 (Ontological Representations for SE Morphisms); OWL/RDF infrastructure for any project needing formal ontologies
- **Key assets:** OntoClean validation, ontology evaluation swarm, OML workflow

### 06 COSYSMO

- **Purpose:** Constructive systems engineering cost estimation
- **Domain:** Cost estimation, parametric modeling
- **Governance:** SPARC boilerplate (no rule annotations)
- **Skills:** 27 total (1 domain-specific: `cosysmo-estimation`)
- **Agents:** 82 total (6 domain-specific: effort-multiplier-analyst, size-driver-analyst in `specialists/`; cost-analyst, estimation-queen, historical-learner, sensitivity-analyst in `core/`)
- **Status:** Active
- **Research relevance:** Supporting for portfolio-level effort estimation; potential integration with PostWach portfolio optimizer
- **Key assets:** COSYSMO parametric model, size driver and effort multiplier analysis

### 07 SysMLv2

- **Purpose:** SysML v2 grammar development, library integration, and semantic analysis
- **Domain:** Model-based systems engineering, SysML v2 specification
- **Governance:** V3 [S001-S006]
- **Skills:** 37 total (3 domain-specific: `sysml-grammar-development`, `sysml-library-integration`, `sysml-semantic-analysis`)
- **Agents:** 21 total (0 domain-specific agents visible; sysml agent directory exists but is empty)
- **Status:** Active
- **Research relevance:** Supporting for Idea 1 (SE morphisms expressed in SysML v2); grammar/semantics directly relevant to formal specification
- **Key assets:** SysML v2 grammar skills, semantic analysis capability

### SEAD

- **Purpose:** Systems engineering analysis and design — codebase analysis, infrastructure-as-code, monitoring
- **Domain:** Systems engineering practice, DevOps/IaC
- **Governance:** SPARC boilerplate (no rule annotations)
- **Skills:** 29 total (3 domain-specific: `sead-codebase-analysis`, `sead-iac-generator`, `sead-monitoring-setup`)
- **Agents:** 81 total (5 domain-specific: s-agent, e-agent, a-agent, d-agent, sead-orchestrator)
- **Status:** Active
- **Research relevance:** Supporting infrastructure for applied SE analysis across projects
- **Key assets:** SEAD orchestration pattern (S/E/A/D decomposition), IaC generation

---

## Tier 2: Support / Infrastructure

### 01_Alpha_Impress_Disruptor (Alpha Empress)

- **Purpose:** COO-type governance compliance — configuration auditing, rule enforcement
- **Domain:** Project governance, V3 compliance
- **Governance:** None (no CLAUDE.md, no .claude/ skills or agents)
- **Skills/Agents:** None
- **Status:** Dormant (V3 Governance Proposal exists but is unimplemented)
- **Key asset:** `V3_Guidance_Governance_Proposal.md` — defines the target governance enforcement model
- **Phase 2 note:** When activated, Alpha Empress handles COO (rule compliance) while PostWach handles CTO (capability quality). See cross-project-reviewer skill for integration design.

### PLM

- **Purpose:** Product lifecycle management co-pilot
- **Domain:** PLM, BOM management, change control, compliance
- **Governance:** Claude Flow V3 header (no rule annotations)
- **Skills:** 30 total (1 domain-specific: `plm`)
- **Agents:** 101 total (8 domain-specific: bom-manager, change-control, compliance, cost-estimator, queen, requirements-manager, risk-analyst, supplier-manager)
- **Status:** Maintenance
- **Note:** Uses older CLI pattern; may need modernization if reactivated

### BP Marketing

- **Purpose:** Marketing orchestration and visual content creation
- **Domain:** Marketing strategy, visual design, content creation
- **Governance:** SPARC boilerplate (no rule annotations)
- **Skills:** 28 total (2 domain-specific: `marketing-orchestration`, `visual-creative`)
- **Agents:** 88 total (12 domain-specific: 7 marketing + 5 visual)
- **Status:** Maintenance

### UAOS Cluster (Core / Domain / Foundation / Libraries)

- **Purpose:** University of Arizona operating system — modular architecture across four repositories
- **Domain:** Institutional platform
- **Governance:** None (no .claude/ setup in any of the four repos)
- **Skills/Agents:** None
- **Status:** Dormant
- **Note:** Four-repo architecture but no Claude Flow integration yet

### Claude_code_test_setup

- **Purpose:** Test environment for Claude Code configuration patterns
- **Domain:** Tooling validation
- **Governance:** SPARC boilerplate
- **Skills:** 26 total (0 domain-specific; common infrastructure only)
- **Agents:** Common infrastructure only
- **Status:** Active (utility)

---

## Tier 3: Archive / Utility

| Project | Purpose | Status |
|---|---|---|
| 00 Planning and Execution | Planning spreadsheets and documents | Archive |
| 02 Images for Reuse | Shared image assets | Utility |
| 03 Background info | Reference materials (read-only) | Utility |
| Buzz | Local claude-flow install with templates | Archive (test) |
| GST-Co-Pilot-Test / temp | GST co-pilot prototype (two repos) | Archive (test) |
| Lego-EV3-Mindstorm-Models | EV3 robotics models | Archive |
| MS4 | License/install guide only | Archive |
| STA_test_setup_2 | STA simulation project (has .claude/) | Dormant |
| STA_v1 | STA simulation project v1 (has .claude/) | Dormant |
| Git_test | Git testing | Archive (test) |
| OSP | Unknown/empty | Archive |

---

## Cross-Project Research Relevance Map

| Idea | Description | Primary Project | Supporting Projects |
|---|---|---|---|
| 1 | SE Morphism Foundations | PostWach | SysMLv2 (grammar/semantics) |
| 2 | Isomorphism Library & Catalog | PostWach | -- |
| 3 | Bayesian Verification Confidence | PostWach | -- |
| 4 | Discretization Degradation | PostWach | -- |
| 5 | Morphism-Based Design Transfer | PostWach | -- |
| 6 | Multi-Domain Co-Simulation | PostWach | SEAD (monitoring) |
| 7 | Morphism Complexity Metrics | PostWach | COSYSMO (cost estimation) |
| 8 | Biological/Engineered Morphisms | PostWach | -- |
| 9 | Ontological Representations | GI-JOE | PostWach (SE morphism domain) |
| 10 | AI-Assisted Morphism Discovery | PostWach | -- |
| 11 | Human Factors in Morphism Use | PostWach | -- |
| 12 | Immune/Cyber Morphisms | PostWach | -- |
| 13 | Morphisms vs. Transfer Learning | PostWach | -- |
| 14 | Morphism-Based Testing | PostWach | SEAD (codebase analysis) |
| 15-19 | Verification in Acquisition | PostWach | MACQ (acquisition pathways) |
| 20-25 | Cognitive/Human Studies | PostWach | -- |

---

## Governance Maturity Summary

| Level | Count | Projects | Upgrade Action |
|---|---|---|---|
| V3 (annotated rules) | 4 | PostWach, MACQ, GI-JOE, SysMLv2 | None — gold standard |
| SPARC boilerplate | 4 | COSYSMO, SEAD, BP Marketing, Claude_code_test_setup, PLM | Add [Rxxx] rule annotations, risk tags |
| None | 2+ | Alpha Empress, UAOS cluster | Create CLAUDE.md with rules |

**Priority upgrades:** COSYSMO (Tier 1, SPARC boilerplate), SEAD (Tier 1, SPARC boilerplate)

---

## Review Log

| Date | Reviewer | Changes |
|---|---|---|
| 2026-02-24 | PostWach CTO (initial) | Created registry from full project landscape exploration |
| 2026-02-24 | PostWach CTO | V3 governance upgrades: GI-JOE [G001-G007], SysMLv2 [S001-S006] |

---

*Maintained by PostWach (CTO role). Monthly review cycle.*

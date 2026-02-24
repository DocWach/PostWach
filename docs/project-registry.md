# Cross-Project Registry

**Maintained by:** PostWach (CTO / Chief Scientist role)
**Created:** 2026-02-24
**Review cycle:** Monthly
**Next review:** 2026-03-24

---

## Classification Key

| Field | Values |
|---|---|
| **Type** | Hive (agent orchestration environment) / Output (artifact produced by a hive) |
| **Tier** | 1 (Active Research) / 2 (Support) / 3 (Archive) |
| **Governance** | V3 (annotated rules, risk tags) / SPARC (boilerplate config) / None / N/A (outputs) |
| **Status** | Active / Maintenance / Dormant / Archive |

---

## Tier 1: Active Research

### 01 PostWach

- **Type:** Hive
- **Purpose:** SE math foundations — formal isomorphisms/morphisms across engineering domains
- **Domain:** Systems engineering, category theory, mathematical modeling
- **Governance:** V3 [R101-R107]
- **Skills:** 110 total (75 domain-specific: 48 math library by MSC, 10+ research methodology, 7+ philosophy of inquiry, cross-domain analysis)
- **Agents:** 237 total (23 mathematics, 28 philosophy, 8 research, 1 custom, ~177 common infrastructure)
- **Status:** Active
- **Research relevance:** Primary for Ideas 1-8, 10-14, 20-25; supporting for Idea 9 (with GI-JOE)
- **Key assets:** Isomorphism library (`Papers/SE_Math_Foundations/`), capability roadmap, 25-idea portfolio, research-portfolio-optimizer

### 04 MACQ

- **Type:** Hive
- **Purpose:** Defense acquisition lifecycle modeling and decision support
- **Domain:** DoD acquisition (DBS, MTA, software pathway), program management
- **Governance:** V3 [P001-P007]
- **Skills:** 30 total (10 domain-specific under `acquisition/`: acquisition-lifecycle, acquisition-training, deliverable-generator, document-automation, far-compliance-checker, ipt-assembler, milestone-readiness, pathway-selector, persona-router, protest-prevention)
- **Agents:** 145 total (52 domain-specific: 16 acquisition roles, 19 acquisition swarms, 7 oversight bodies, 10 archetypes)
- **Status:** Active
- **Research relevance:** Supporting for Ideas 15-19 (verification in acquisition context)
- **Key assets:** Full acquisition pathway swarms (DBS, MTA, milestones A/B/C), 50+ deliverable templates, 95 FAR/DFARS compliance rules, oversight body agents

### 05 GI-JOE

- **Type:** Hive
- **Purpose:** Ontology engineering platform — OWL/RDF/SPARQL, BFO alignment, semantic reasoning
- **Domain:** Ontology engineering, knowledge representation
- **Governance:** V3 [G001-G007]
- **Skills:** 36 total (0 domain-specific skills; ontology capability is agent-based)
- **Agents:** 116 total (5 domain-specific: ontology-swarm-coordinator, ontology-alignment, ontology-evaluator, ontology-metrics, ontoclean-validator)
- **Status:** Active
- **Research relevance:** Primary for Idea 9 (Ontological Representations for SE Morphisms); OWL/RDF infrastructure for any project needing formal ontologies
- **Key assets:** OntoClean validation, ontology evaluation swarm, OML workflow

### 06 COSYSMO

- **Type:** Hive
- **Purpose:** Constructive systems engineering cost estimation
- **Domain:** Cost estimation, parametric modeling
- **Governance:** V3 [C001-C006]
- **Skills:** 27 total (1 domain-specific: `cosysmo-estimation`)
- **Agents:** 82 total (6 domain-specific: effort-multiplier-analyst, size-driver-analyst in `specialists/`; cost-analyst, estimation-queen, historical-learner, sensitivity-analyst in `core/`)
- **Status:** Active
- **Research relevance:** Supporting for portfolio-level effort estimation; potential integration with PostWach portfolio optimizer
- **Key assets:** COSYSMO parametric model, size driver and effort multiplier analysis

### 07 SysMLv2

- **Type:** Hive
- **Purpose:** SysML v2 grammar development, library integration, and semantic analysis
- **Domain:** Model-based systems engineering, SysML v2 specification
- **Governance:** V3 [S001-S006]
- **Outputs:** Lego-EV3-Mindstorm-Models (SysML v2 models), INCOSE_FuSE_Vision2035 (INCOSE FuSE model)
- **Skills:** 37 total (3 domain-specific: `sysml-grammar-development`, `sysml-library-integration`, `sysml-semantic-analysis`)
- **Agents:** 21 total (0 domain-specific agents visible; sysml agent directory exists but is empty)
- **Status:** Active
- **Research relevance:** Supporting for Idea 1 (SE morphisms expressed in SysML v2); grammar/semantics directly relevant to formal specification
- **Key assets:** SysML v2 grammar skills, semantic analysis capability

### SEAD

- **Type:** Hive
- **Purpose:** Systems engineering analysis and design — codebase analysis, infrastructure-as-code, monitoring
- **Domain:** Systems engineering practice, DevOps/IaC
- **Governance:** V3 [D001-D006]
- **Skills:** 29 total (3 domain-specific: `sead-codebase-analysis`, `sead-iac-generator`, `sead-monitoring-setup`)
- **Agents:** 81 total (5 domain-specific: s-agent, e-agent, a-agent, d-agent, sead-orchestrator)
- **Status:** Active
- **Research relevance:** Supporting infrastructure for applied SE analysis across projects
- **Key assets:** SEAD orchestration pattern (S/E/A/D decomposition), IaC generation

---

## Tier 2: Support / Infrastructure

### 01_Alpha_Impress_Disruptor (Alpha Empress)

- **Type:** Hive
- **Purpose:** COO-type governance compliance — configuration auditing, rule enforcement
- **Domain:** Project governance, V3 compliance
- **Governance:** V3 [A001-A008]
- **Skills/Agents:** None (Phase B will add compliance-checker skill)
- **Status:** Active (Phase A — foundation)
- **Key assets:** V3 governance templates, adoption tracker, compliance assessment protocol
- **Key asset:** `V3_Guidance_Governance_Proposal.md` — defines the target governance enforcement model
- **Phase A complete.** Phase B (compliance-checker skill) and Phase C (CTO/COO integration) pending.

### PLM

- **Type:** Hive
- **Purpose:** Product lifecycle management co-pilot
- **Domain:** PLM, BOM management, change control, compliance
- **Governance:** V3 [L001-L007]
- **Outputs:** Lego-EV3-Mindstorm-Models (parts data, kit inventories)
- **Skills:** 30 total (1 domain-specific: `plm`)
- **Agents:** 101 total (8 domain-specific: bom-manager, change-control, compliance, cost-estimator, queen, requirements-manager, risk-analyst, supplier-manager)
- **Status:** Maintenance
- **Note:** V3 governance applied 2026-02-24; ITAR security rule [L007] added

### BP Marketing

- **Type:** Hive
- **Purpose:** Marketing orchestration and visual content creation
- **Domain:** Marketing strategy, visual design, content creation
- **Governance:** SPARC boilerplate (no rule annotations)
- **Skills:** 28 total (2 domain-specific: `marketing-orchestration`, `visual-creative`)
- **Agents:** 88 total (12 domain-specific: 7 marketing + 5 visual)
- **Status:** Maintenance

### UAOS Cluster (Core / Domain / Foundation / Libraries)

- **Type:** Hive (dormant)
- **Purpose:** University of Arizona operating system — modular architecture across four repositories
- **Domain:** Institutional platform
- **Governance:** None (no .claude/ setup in any of the four repos)
- **Skills/Agents:** None
- **Status:** Dormant
- **Note:** Four-repo architecture but no Claude Flow integration yet

### Claude_code_test_setup

- **Type:** Hive
- **Purpose:** Test environment for Claude Code configuration patterns
- **Domain:** Tooling validation
- **Governance:** SPARC boilerplate
- **Skills:** 26 total (0 domain-specific; common infrastructure only)
- **Agents:** Common infrastructure only
- **Status:** Active (utility)

---

## Hive Outputs

Output repositories are artifacts produced by one or more hives. They contain deliverables (models, data, reports) but no agent orchestration infrastructure. Governance is inherited from parent hives — outputs do not need their own CLAUDE.md.

| Output | Parent Hives | Content | Status |
|---|---|---|---|
| Lego-EV3-Mindstorm-Models | PLM (parts data, kit inventories), SysMLv2 (SysML v2 models) | 172-part reusable library: JSON catalog, kit inventories, SysML v2 behavioral models, LDraw geometry refs | Active |
| INCOSE_FuSE_Vision2035 | SysMLv2 (INCOSE FuSE/Vision 2035 model) | Single SysML v2 model output for INCOSE FuSE standards | Active |

---

## Tier 3: Archive / Utility

| Project | Purpose | Status |
|---|---|---|
| 00 Planning and Execution | Planning spreadsheets and documents | Archive |
| 02 Images for Reuse | Shared image assets | Utility |
| 03 Background info | Reference materials (read-only) | Utility |
| Buzz | Local claude-flow install with templates | Archive (test) |
| GST-Co-Pilot-Test / temp | GST co-pilot prototype (two repos) | Archive (test) |
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
| V3 (annotated rules) | 8 | PostWach, MACQ, GI-JOE, SysMLv2, COSYSMO, SEAD, PLM, Alpha Empress | None — gold standard |
| SPARC boilerplate | 2 | BP Marketing, Claude_code_test_setup | Add [Rxxx] rule annotations, risk tags |
| None | 1+ | UAOS cluster | Create CLAUDE.md with rules |

**Tier 1 complete. PLM upgraded. Alpha Empress activated (Phase A).** Remaining Tier 2 upgrades (low priority, on-demand): BP Marketing, Claude_code_test_setup. Dormant projects (activate first): UAOS cluster.

---

## Review Log

| Date | Reviewer | Changes |
|---|---|---|
| 2026-02-24 | PostWach CTO (initial) | Created registry from full project landscape exploration |
| 2026-02-24 | PostWach CTO | V3 governance upgrades: GI-JOE [G001-G007], SysMLv2 [S001-S006], COSYSMO [C001-C006], SEAD [D001-D006] |
| 2026-02-24 | PostWach CTO | V3 governance upgrade: PLM [L001-L007] |
| 2026-02-24 | PostWach CTO | Add Hive/Output type classification; reclassify Lego-EV3 and INCOSE_FuSE as outputs |
| 2026-02-24 | PostWach CTO | Alpha Empress Phase A activation: [A001-A008], templates, adoption tracker |

---

*Maintained by PostWach (CTO role). Monthly review cycle.*

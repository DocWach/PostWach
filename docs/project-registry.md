# Cross-Project Registry

**Maintained by:** PostWach (CTO / Chief Scientist role)
**Created:** 2026-02-24
**Review cycle:** Monthly
**Last refreshed:** 2026-07-20
**Next review:** 2026-08-20

> **Numbering note (2026-07-20):** section headers below carry legacy numbers (e.g. "04 MACQ", "05 GI-JOE") that predate the current on-disk hive folders. Actual folders in `01 Hives/`: `00 Alpha Empress`, `01 PostWach`, `01A Patsy`, `02 GI-JOE`, `03 Lawsun`, `04 Fort Wachs`, `05 MACQ`, `06 COSYSMO`, `07 SysMLv2`, `08 PLM`, `09 SEAD`, `10 Finance Bro`. Reconcile numbering at next full review. Patsy now has its own git repo (committed 2026-07-11) but its Hive-vs-Output classification remains deferred by the principal (filed as Output below). As of 2026-07-20, Alpha Empress / MACQ / COSYSMO / PLM / SEAD last committed 2026-06-01 (parked).

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
- **Governance:** V3 [P001-P011] (P001-P006 standard, P007-P011 MACQ-specific)
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
- **Key assets:** OntoClean validation, ontology evaluation swarm, OML workflow, STOIC ontology family (DEVS/T3SD/bridge), named-graph/quad-store capability (QUADS-001, closed 2026-06-29), **SE Morphism Library** (`ml:` TBox + ABox, built 2026-07-14, (b) demonstrated)

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

### 01 Fort Wachs

- **Type:** Hive
- **Purpose:** Security policy authority (CISO) for the research portfolio; NSA Zero Trust posture, compliance mapping, vendor evaluation
- **Domain:** Security operations, Zero Trust architecture, compliance frameworks (CMMC 2.0, NIST 800-171)
- **Governance:** V3 [X001-X010]
- **Skills:** 3 domain-specific (security-posture, vendor-evaluation, compliance-mapper)
- **Agents:** 3 domain-specific (threat-modeler, compliance-auditor, vendor-evaluator)
- **Status:** Active
- **Research relevance:** Cross-cutting; security credibility for DARPA CLARA, NNSA proposals, UofA institutional recommendations
- **Key assets:** ZT 7-pillar policy framework, Chainguard vendor evaluation, CMMC 2.0 control mapping

### SEAD

- **Type:** Hive
- **Purpose:** Software Engineering, Architecture, Development, Deployment, Operations, and Security — codebase analysis, infrastructure-as-code, monitoring, security
- **Domain:** Software engineering practice, DevOps/IaC, security
- **Governance:** V3 [D001-D009]
- **Skills:** 29 total (3 domain-specific: `sead-codebase-analysis`, `sead-iac-generator`, `sead-monitoring-setup`)
- **Agents:** 81 total (5 domain-specific: s-agent, e-agent, a-agent, d-agent, sead-orchestrator)
- **Status:** Active
- **Research relevance:** Supporting infrastructure for applied SE analysis across projects
- **Key assets:** SEAD orchestration pattern (S/E/A/D decomposition), IaC generation

### 10 Finance Bro

- **Type:** Hive
- **Purpose:** Assistant for a financial manager — money/risk management plus managerial / business-development (finding new clients, prospecting, client deliverables)
- **Domain:** Wealth/retirement advisory, client prospecting, investing/risk
- **Governance:** V3 [F101-F114] (F101-F107 standard, F110-F114 finance-specific: PII, no-investment-advice posture, data-source terms)
- **Skills:** 1 domain-specific (`form5500-prospecting`)
- **Agents:** 3 hand-authored (`finance-queen`, `prospect-researcher`, `client-data-steward`)
- **Status:** Active (v1, narrow-first)
- **Build strategy:** scaffold + governance, then the DOL Form 5500 prospecting vertical end-to-end; breadth added iteratively
- **Referenced backend:** `01 PostWach/Papers/AI_Investing_Platform` (README "Financial-Manager"), ~31k-line quant engine — R016 (a) research artifact; called as the money/risk engine, not folded into the hive
- **Reuse sources:** BP Marketing (BD swarm → prospecting), MACQ (deliverable-generator/document-automation/persona-router), GI-JOE (browser, ontology), Fort Wachs (PII/compliance policy)
- **Key assets:** `form5500-prospecting` skill + schema-tolerant DOL bulk-dataset ingestion (`scripts/ingest_form5500.py`); validated on real 2023 Form 5500-SF data 2026-06-22
- **Open:** real financial manager's prospecting criteria pending (swappable scoring config hook)

---

### 03 Lawsun

- **Type:** Hive
- **Purpose:** Legal-assistant hive ("bringing light to the law"). Legal research + information tool, explicitly NOT legal advice (UPL guardrails), built with attorney-grade confidentiality rigor + academic SE/law research depth
- **Domain:** Legal research, citation verification, (later) contract analysis, drafting, compliance mapping
- **Governance:** V3 [LW101-LW117] (LW101-LW107 standard; LW110-LW117 legal-specific: UPL posture, confidentiality≠privilege, 4-gate citation, jurisdiction/currency, query minimization, human-in-the-loop)
- **Skills:** 3 (`legal-research`, `citecheck`, `legal-argumentation` [rescoped to proposition-support])
- **Agents:** 4 hand-authored (`lawsun-queen`, `legal-researcher`, `cite-checker`, `confidentiality-steward`) + 3 stubs (`contract-analyst`, `legal-drafter`, `jurisprudence-analyst`)
- **Status:** Active (v1, narrow-first). Built + verified 2026-06-29
- **Build strategy:** scaffold + governance, then legal research + cite-check vertical end-to-end (load-bearing for all later verticals); breadth added iteratively
- **Key assets:** `citecheck.py` 4 defect-only gates (exists / good-law / jurisdiction / proposition-support); confidence REPORTED not gated (TRAK Bayesian posterior + precedential weight; optional --min-confidence soft floor); `eyecite` extraction + cache-first/live-CourtListener resolution (`verified_authorities.json` 30-day TTL cache; `--citator mock` for CI); LW116 sends only bare cites. Adversarial fixtures verified (passes on-point, fails closed on fabricated/overruled/wrong-jurisdiction/wrong-proposition/bare). R016: `legal-research`/`legal-argumentation` (a); **citecheck + eyecite + CourtListener (b) demonstrated** (good-law citator still partial — no free Shepard's/KeyCite)
- **Reuse sources:** PostWach (R019 protocol refcheck/refverify/reflookup; TRAK Bayesian aggregation; curated logic/philosophy skills + ethics agents), GI-JOE (browser, ontology), MACQ (deliverable-generator/document-automation/persona-router — later drafting vertical), Fort Wachs (compliance-mapper/security-posture); tools: `eyecite`, CourtListener
- **Plan provenance:** vetted via tri-model red/blue/white (Claude+Codex+Gemini over ruflo); citecheck hardened 1-gate→4-gate per adversarial review
- **Test harness:** plan-driven, built 2026-06-29. `docs/test_plan.md` (living checklist, IDs TV/TG/TI/TS/TE/TR/TF) drives `tests/test_citecheck.py` (18 offline pytest, mock citator) + `.github/workflows/ci.yml`. Grow via PLANNED/TF rows.
- **Open / next:** PLANNED/TF test backlog (fuzz, real citator, live-CourtListener contract, LW110/LW117 behavioral); expand `docs/legal_sources.md`; real citator for gate-2 good-law (no free Shepard's/KeyCite); CourtListener token for live runs; review Brad's `bmpwach-lab` legal assistant. Byzantine N=3 deferred. Repo: `DocWach/Lawsun` (pushed: 6210dd6 → 2eeb245)
- **Portfolio:** V3 hive count 10→11

---

## Tier 2: Support / Infrastructure

### 01_Alpha_Impress_Disruptor (Alpha Empress)

- **Type:** Hive
- **Purpose:** COO-type governance compliance — configuration auditing, rule enforcement
- **Domain:** Project governance, V3 compliance
- **Governance:** V3 [A001-A008]
- **Skills/Agents:** 1 skill (compliance-checker)
- **Status:** Active (Phase C — CTO/COO integration)
- **Key assets:** V3 governance templates, adoption tracker, compliance assessment protocol
- **Key asset:** `V3_Guidance_Governance_Proposal.md` — defines the target governance enforcement model
- **Phase C complete.** CTO/COO integration active.

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

- **Type:** Output (reviewed ontology / OML models — not a Hive)
- **Purpose:** University of Arizona operating system — modular OML/OpenCaesar ontology architecture across four repositories
- **Domain:** Institutional platform, ontology engineering (OML)
- **Governance:** N/A (output — governance inherited from GI-JOE as reviewing hive)
- **Parent Hive:** GI-JOE (ontology review and evaluation)
- **Skills/Agents:** None (no Claude Flow integration; ontology-only repos)
- **Status:** Dormant
- **Note:** Reclassified from Hive to Output (2026-02-24). Contains OML models reviewed by GI-JOE's ontology evaluation swarm. No agent orchestration infrastructure.

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
| UAOS Cluster | GI-JOE (ontology review and evaluation) | OML/OpenCaesar ontology models across four repositories | Dormant |
| IGNITE '26 Hackathon | MACQ (DTE&A knowledge, T&E metrics), GI-JOE (ontology patterns, validation pipeline), PostWach (morphism engine, Wymore models) | DTE&A assessment demo: Berserker MQ-99 ontology, morphism quality heatmap, traceability queries, Streamlit dashboard | Active |
| VT Supply Chain Analyzer | PostWach (faculty advisor, architecture ownership) | Streamlit + SimPy + LP titanium supply chain disruption analyzer. VT ISE Senior Design Team 4 (AY 25-26). Sponsor: The Aerospace Corporation. Tier 2 service project. Repo: `DocWach/Supplychain-Analysis-VT-ISE-Senior-Design` (private). Current release: v2.1.0 (commit `d9a6c13`, 65/65 tests). | Active |
| Patsy (personal assistant) | PostWach (originating; classification deferred) | Personal assistant integrated into the home-lab environment. Hybrid (Tier 0/1 local + Tier 2 cloud). Topology A; inventory pinned; v1 = HA + router + STT/TTS on a Pi 4 (Asus deferred). Being architected via the WySE scheme + T3SD (SD@LA drafted, verifying to BSD@LC). Home folder `01 Hives/01A Patsy/`; brief `01 Hives/01A Patsy/Patsy_Brief.md`. Hive-vs-output classification deferred (Output for now). | Active (exploration) |

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
| V3 (annotated rules) | 11 | PostWach, MACQ, GI-JOE, SysMLv2, COSYSMO, Fort Wachs, SEAD, PLM, Alpha Empress, Finance Bro, Lawsun | None — gold standard |
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
| 2026-02-24 | PostWach CTO | Alpha Empress Phase C: CTO/COO integration active, 1 skill (compliance-checker) |
| 2026-02-24 | PostWach CTO | MACQ governance pattern merge: P001-P006 standard + P007-P011 MACQ-specific |
| 2026-02-24 | PostWach CTO | UAOS cluster reclassified: Output (reviewed by GI-JOE), not Hive |
| 2026-03-10 | PostWach CTO | Add Fort Wachs (CISO) as Tier 1 hive [X001-X010]; update SEAD governance [D001-D009] |
| 2026-06-22 | PostWach CTO | Add Finance Bro as Tier 1 hive [F101-F114]; v1 = Form 5500 prospecting vertical; AI_Investing_Platform referenced as backend; V3 count 9→10 |
| 2026-06-29 | PostWach CTO | Add Lawsun as Tier 1 hive [LW101-LW117]; v1 = legal-research + 4-gate citecheck vertical (eyecite + CourtListener, confidence reported-not-gated, plan-driven 20-test harness); plan vetted via tri-model red/blue/white; V3 count 10→11 |
| 2026-07-10 | PostWach CTO | Add HomeLab Assistant (working name) as a research output/product (exploration); hybrid personal assistant + home-lab hardware trade study; classification deferred pending trades |
| 2026-07-20 | PostWach CTO | Overdue-review refresh: set next review 2026-08-20; added numbering-reconciliation note (legacy section numbers vs on-disk folders); recorded Patsy now has its own repo (classification still deferred); flagged 5 hives parked since 2026-06-01; added GI-JOE SE Morphism Library + QUADS-001 to key assets. Full numbering reconciliation deferred to next review. |

---

*Maintained by PostWach (CTO role). Monthly review cycle.*

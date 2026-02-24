# PostWach Capability Roadmap

**Created:** 2026-02-24
**Last Reviewed:** 2026-02-24
**Next Review:** 2026-05-24 (quarterly)
**Status:** Living document

---

## Decision Framework

For each proposed capability, three questions determine placement:

1. **Does it serve an active or near-term research idea?** (Maps to Ideas 1-25, NSF proposal years)
2. **Is it a meta-research capability?** (Helps decide/manage research, not do it)
3. **Does it already exist?** (In PostWach, GI-JOE, or as a reusable external tool)

**Principle:** PostWach is domain-agnostic research infrastructure. Domain knowledge is added as skill/agent packs only when it directly serves active or near-term research projects.

---

## Capability Status Tracker

| # | Capability | Tier | Home | Status | Phase | Target |
|---|---|---|---|---|---|---|
| 1 | Bayesian / Utility-Driven Research Strategy | 1-High | PostWach | Done | Phase 1 | Immediate |
| 2 | Biology (Biomimetics, Physiology, Biophysics) | 1-High | PostWach | Done | Phase 2 | Q1-Q2 2026 |
| 3 | Psychology / Cognitive Science | 1-High | PostWach | Done | Phase 4 | Q3 2026 |
| 4 | Transfer Learning | 1-High | PostWach | Done | Phase 3 | Q2 2026 |
| 5 | Ontology | 2-Med | GI-JOE | Existing | Phase 5 | When needed |
| 6 | Economics / Utility Theory | 2-Med | PostWach | Done | (with #1) | Immediate |
| 7 | Gamification / Progress Tracking | 2-Med | PostWach | Not Started | Phase 6 | When needed |
| 8 | Blockchain | 3-Low | Defer | -- | Deferred | When Idea 15 active |
| 9 | Quantum | 3-Low | Defer | -- | Deferred | Existing agents suffice |
| 10 | Federated Learning | 3-Low | Defer | -- | Deferred | NSF Year 3 |
| 11 | Human Law | N/A | Institutional | -- | N/A | Consult UA legal |

**Status values:** Not Started | In Progress | Done | Deferred | Existing

---

## Phase Details

### Phase 1 — Bayesian Research Strategy (Immediate)

**Serves:** All 25 ideas (portfolio management), Idea 3 (Bayesian Verification Confidence)

**Deliverable:** `research-portfolio-optimizer` skill

**Reuses:** `probabilist` agent, `measure-theorist` agent, `optimization-specialist` agent, research methodology agents, epistemic queen

**New capability:** Utility functions for expected research value, dependency graph analysis across the 25-idea portfolio, expected-value-of-information calculations, feasibility scoring

**Economics/Utility Theory (#6) folds into this phase** — no separate economics agent needed. The utility-theory component is part of the portfolio optimizer.

### Phase 2 — Biology / Biomimetics (Q1-Q2 2026)

**Serves:** Idea 8 (Biological/Engineered Systems Morphisms), Idea 12 (Immune/Cyber Morphisms)

**Deliverables:**
- `biophysics-modeler` agent — physiological system modeling, compartmental models, neural circuits
- `biomimetics-analyst` skill — maps biological mechanisms to engineering analogs

**Reuses:** `ode-dynamicist`, `pde-specialist`, `functional-analyst`, `pattern-detector`, `numerical-analyst`

**Rationale:** Extends isomorphism library with novel, publishable domain pairs.

### Phase 3 — Transfer Learning (Q2 2026)

**Serves:** Idea 13 (Morphisms vs. Transfer Learning structural comparison)

**Deliverable:** `transfer-learning-analyst` skill — domain adaptation theory, feature space alignment, structural correspondence analysis between morphism and TL frameworks

**Reuses:** `ml-developer`, `category-theorist`, `pattern-detector`, `functional-analyst`

**Rationale:** Idea 13 is a compelling standalone paper even outside the first NSF proposal.

### Phase 4 — Psychology / Cognitive Science (Q3 2026)

**Serves:** Ideas 20-25 (NSF Year 3 — Hidden Beliefs, Heuristic Accuracy, Layer-Selective Attention, Mental Model Fidelity, Tacit Knowledge, Design Decision Traceability)

**Deliverables:**
- `cognitive-study-designer` skill — protocol analysis, think-aloud methods, calibration studies, IRB protocol templates
- `psychometrics-analyst` agent — inter-rater reliability, effect sizes, mixed-methods integration

**Reuses:** `methodology-advisor`, research methodology agents, `probabilist`

**Rationale:** Not needed until NSF Year 3 prep, but IRB and protocol design benefit from early planning.

### Phase 5 — Ontology Bridge (When Needed)

**Serves:** Idea 9 (Ontological Representations for SE Morphisms)

**Action:** Work in GI-JOE with PostWach providing SE morphism domain knowledge. No duplication of ontology capabilities.

**Cross-reference:** See [GI-JOE Ontology Capabilities](#gi-joe-cross-reference) below.

### Phase 6 — Gamification / Progress Tracking (When Needed)

**Serves:** General portfolio productivity; complements `effort_report.md` tracking

**Deliverable:** `research-progress-tracker` skill — tracks ideas by phase (captured, in-progress, submitted, published), visualizes portfolio progress, generates effort reports

**Reuses:** Existing `src/mastery_dashboard/` infrastructure

### Deferred Capabilities

| Capability | Rationale | Revisit Trigger |
|---|---|---|
| Blockchain | Idea 15 is scoped as a short communication; full capability is overkill | When Idea 15 becomes active |
| Quantum | `category-theorist` agent already covers quantum-adjacent category theory | When a specific quantum-SE research question crystallizes |
| Federated Learning | No direct idea in 25-portfolio; future multi-institution collaboration | NSF Year 3, multi-site data sharing |
| Human Law | Requires actual legal counsel, not an AI agent | Use UA Tech Transfer / legal counsel |

---

## Reuse Matrix

| Capability | Reuses from PostWach | Creates New |
|---|---|---|
| Bayesian Strategy | `probabilist`, `optimization-specialist`, epistemic queen, HNSW memory | `research-portfolio-optimizer` skill |
| Biology | `ode-dynamicist`, `pde-specialist`, `functional-analyst`, `pattern-detector`, `numerical-analyst` | `biophysics-modeler` agent, `biomimetics-analyst` skill |
| Psychology | `methodology-advisor`, research methodology agents, `probabilist` | `cognitive-study-designer` skill, `psychometrics-analyst` agent |
| Transfer Learning | `ml-developer`, `category-theorist`, `pattern-detector`, `functional-analyst` | `transfer-learning-analyst` skill |
| Ontology | None (use GI-JOE) | Cross-project reference only |
| Economics | `probabilist`, `optimization-specialist` | Folded into Bayesian strategy |
| Gamification | `mastery_dashboard` infrastructure | `research-progress-tracker` skill |

---

## GI-JOE Cross-Reference

**Project location:** `03 Projects/00 My Research/GI-JOE`

GI-JOE is a dedicated ontology engineering platform. When Idea 9 (Ontological Representations for SE Morphisms) becomes active, ontology work should be done in GI-JOE with PostWach supplying the SE morphism domain knowledge.

**GI-JOE ontology agents:**
- `ontology-swarm-coordinator` — multi-agent ontology evaluation orchestration
- `ontology-alignment` — ontology mapping and alignment
- `ontology-evaluator` — ontology quality assessment
- `ontology-metrics` — quantitative ontology metrics
- `ontoclean-validator` — OntoClean metaproperty validation (rigidity, identity, unity, dependence)

**GI-JOE ontology infrastructure:** OWL/RDF/SPARQL, BFO alignment, OML workflow, semantic reasoning, knowledge graph construction (13+ ontology skills total)

**Integration pattern:** PostWach defines morphism domain semantics; GI-JOE provides formal ontology engineering. No capability duplication.

---

## Review Log

| Date | Reviewer | Changes |
|---|---|---|
| 2026-02-24 | Initial assessment | Created roadmap from 11-topic strategic evaluation |
| 2026-02-24 | Phase 2 delivery | Added `biophysics-modeler` agent (MSC 92C) and `biomimetics-analyst` skill; item #2 marked Done |
| 2026-02-24 | Phase 3 delivery | Added `transfer-learning-analyst` skill (no new agent — reuses `ml-developer`); item #4 marked Done |
| 2026-02-24 | Phase 4 delivery | Added `psychometrics-analyst` agent and `cognitive-study-designer` skill for Ideas 20-25; item #3 marked Done |

---

*Maintained by PostWach. Quarterly review cycle.*

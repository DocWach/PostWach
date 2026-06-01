# Session Archive — 2026-04-21 postwach-01

**Purpose:** Meeting prep — Paul meeting Aufmuth and Gregory at top of the hour.
**Input:** `04 Resource Library/02 Student work/LLM_MBSE_Michael Aufmuth Project.pptx` (15 slides, extracted and reviewed).
**Method:** Ruflo v3.5.80 swarm (`swarm-1776781909882-7ml8wf`, mesh, 5 agents). Three parallel review lenses: PostWach/morphism, hive tooling overlap, governance/R016.
**Classification:** Internal prep; candid. Do not share verbatim with Aufmuth or Gregory.

---

## 1. What Aufmuth built (one paragraph)

Undergrad (SIE 458, Steiner) with four tracks: JAMA auto-import of 70 requirements via Claude Cowork with traceability; SysMLv2 text generation using Claude Code with custom agents (`academic-reviewer`, `lead-architect`, `SE-advisor`) — deprioritized after realizing StudioSE/SySide are better positioned; **main effort** — SysMLv1 Cameo macro injection via `Model_Exporter.groovy` v3.0.0 (1,188 lines, 3-pass JSON export: containment, relationships, diagram positions), `Demo_FireDrone_v2.groovy` (builds 8-package SysMLv1 Fire Fighting Drone model from scratch), `model_index.py` + `planner.py` (9 k-char LLM planner context → JSON plan → Groovy compile → inject); plus Claude computer-use for recursive Cameo loops. Biggest quality jump came from few-shot training on Rick Steiner's SIE 458 submarine model. Cites SEBoK, INCOSE, Steiner, Salado, Gregory.

---

## 2. R016 integration status per artifact

| Artifact | Status | Note |
|---|---|---|
| JAMA automation (70 reqs) | **(a) research artifact** | One-shot demo, not recurring ops |
| SysMLv2 engine with custom agents | **(a) research artifact** | Abandoned track; honest self-labeling |
| `Model_Exporter.groovy` v3.0.0 | **(b) demonstrated capability** | Solves real gap — no other export preserves diagram layout |
| `Demo_FireDrone_v2.groovy` + diagrams | **(b) demonstrated capability** | Visible quality jump; no external validation |
| `model_index.py` + `planner.py` | **(a) research artifact** | Tightly coupled to his workflow |
| Described "webapp" | **(a) incomplete** | Not built. Do not let it creep into (b/c) framing |

**Overstatement risk to watch:** phrasing like "70 requirements entered automatically with full traceability" and "computer use breakthrough" is appropriate student-progress narrative but would violate R016 if reused verbatim in DARPA CLARA / NNSA proposals / INSIGHT article. If cited externally, tag (a/b/c) explicitly.

---

## 3. Portfolio fit — hive by hive

| Hive | Overlap | Verdict |
|---|---|---|
| **SysMLv2** | Agent directory is empty; Aufmuth's `academic-reviewer`/`lead-architect`/`SE-advisor` fill a real gap | Low duplication; candidate contribution |
| **MACQ** | No existing JAMA integration; his 3-level derivation (MNS→SR→CR) matches `deliverable-generator` template needs | **Concrete gap** — JAMA→MACQ bridge skill |
| **GI-JOE** | STOIC-DEVS/T3SD exists; Berserker `.mdzip` extraction is manual; **no programmatic SysMLv1→RDF pipeline** | **Highest value handoff** |
| **SEAD** | `sead-codebase-analysis` is code-centric; no tool-API abstraction | Future productization, not immediate |
| **Fort Wachs** | **No policy** on LLM training on course IP; no MBSE vendor evaluation framework | Policy gap flagged |
| **PostWach** | Triad complements (does not duplicate) philosophy/research agents; submarine→drone few-shot is literally Idea 13 | Strong research-collaboration angle |

---

## 4. Morphism-framework connection (PostWach research)

Aufmuth's representation chain **SysMLv1 ↔ SysMLv2 ↔ JSON ↔ Groovy-injected model** is a concrete empirical testbed for the `D_h = (D_s, D_b)` degradation vector from the CSER 2026 paper. Each transition is a homomorphism with measurable structural and behavioral degradation.

Direct 25-idea portfolio hits:
- **Idea 5** (Library of Cross-Domain Isomorphisms) — adds representation-domain isomorphisms
- **Idea 6** (Degrees of Homomorphism Metric) — his pipeline is a 5-layer test case on real artifacts
- **Idea 9** (Ontological Representations) — JSON→RDF pipeline candidate
- **Idea 10** (AI-Assisted Morphism Discovery) — his custom agents already do this implicitly
- **Idea 13** (Morphisms vs Transfer Learning) — **strongest hit**; submarine→drone few-shot is a partial homomorphism between naval and aerial subsystems, quantifiable via `D_h`
- **Ideas 20–25** (Cognitive Studies) — triad is a human-factors experiment substrate (do agents surface or hide abstractions?)

---

## 5. Critical pre-meeting issue — Steiner submarine training data

Aufmuth explicitly states the submarine model "signaled the largest improvement in generated models to date." Ownership/ITAR/UofA IP status is unresolved.

**Questions without answers right now:**
- Who owns the submarine model — Steiner personally, UofA (course IP), or public?
- Is it ITAR-adjacent? Submarines are not automatically ITAR, but structural SysML might constitute controlled technical data.
- Does Anthropic retain any statistical influence from the training? Can it be deleted?
- If Aufmuth publishes (thesis, paper, GitHub), does the Steiner provenance surface?

**Must clear before:** any DARPA CLARA / NNSA proposal citation, INSIGHT article mention, public GitHub, or thesis submission.

**Do not raise this aggressively in the meeting** — it's a Fort Wachs / UofA IP-office question, not an accusation. Good framing: *"Before we think about next steps, we'll want to scope out the IP clearance on the SIE 458 materials you trained on — is that something Rick and the department have talked about?"*

---

## 6. Top 3 concrete handoff opportunities (for future discussion with Aufmuth)

Ranked by impact / feasibility:

1. **`Model_Exporter.groovy` → GI-JOE `sysml-json-to-stoic` skill** (5–7 days).
   - Highest portfolio impact. Closes the programmatic Cameo→RDF gap that Berserker surfaced during IGNITE '26.
   - Enables SPARQL competency queries over real models.
   - Unlocks Idea 9 at scale.
   - Success metric: FireDrone_v2 → JSON → STOIC → 8+ SPARQL CQs return correct architectural queries.

2. **JAMA automation → MACQ `jama-requirements-bridge` skill** (3–5 days).
   - Live-linked requirements into SEP / TEMP / ICD / CDD templates instead of static snapshots.
   - Validates against his 70-req Fire Drone test case.

3. **Recursive Cameo loop → SEAD `sead-recursive-tool-automation`** (2–3 weeks).
   - Abstract tool-agnostic feedback pattern with Cameo/Capella/Rhapsody adapters.
   - Roadmap item, not immediate.

---

## 7. Proposed research question (for Aufmuth + Gregory collaboration)

**Working title:** *Quantifying Abstraction Fidelity in LLM-Driven Model Synthesis: A Morphism-Based Measurement Framework for MBSE Toolchains*

**Core question:** When an LLM-driven MBSE toolchain transforms engineering requirements through multiple abstraction layers (SysMLv1 ↔ SysMLv2 ↔ JSON ↔ Groovy), can structural and behavioral degradation be formally characterized using morphism metrics, and does explicit morphism-awareness during synthesis improve model fidelity?

**Test design:**
1. Baseline — run Aufmuth's FireDrone toolchain, measure `D_h` at each transition using degree-of-homomorphism metric (Idea 6) on real artifacts.
2. Treatment — inject morphism-aware constraints into `planner.py`. Add a `morphism-validator` agent that checks whether JSON→Groovy injection preserves required structural properties.
3. Outcomes — `D_h` vector per layer, injection fidelity, iterations-to-correctness, user confidence calibration (Idea 20).

**Why it works:**
- Tests Idea 6 in situ on engineering artifacts, not toy systems
- Extends Idea 5 into representation-domain isomorphisms (currently unexamined)
- Formalizes Idea 13 (transfer learning as partial homomorphism)
- Publication target: CSER 2026 or Systems Engineering journal

**Roles:** Aufmuth as data source and tooling author; Steiner + Salado + Gregory as advisors; Paul as morphism-framework lead.

---

## 8. Meeting prep — talking points and open questions

### Angles to lead with
- Strong recognition: Groovy injection + layout-preserving JSON export solves a real problem no one else in the portfolio has addressed.
- Biggest technical surprise: the Steiner-submarine few-shot quality jump — that's exactly Idea 13 territory.
- Highest-impact connection: his exporter feeds directly into GI-JOE's ontology pipeline, which unlocks Idea 9 at scale.

### Questions to ask Aufmuth
1. What's the current state of the SysMLv2 work — fully shelved, or would you revisit if we had a use case?
2. Is `Model_Exporter.groovy` in a repo somewhere? Is it ready for a code review?
3. Have you and Rick discussed IP status of the submarine model you trained on?
4. What's your timeline — is this senior design through spring, or continuing past graduation?
5. Do you see a path to productizing for the DEF, or is this a research demonstrator?

### Questions to ask Gregory
1. Where does this sit in the SIE 458 / senior design advising arc?
2. Are you thinking about this as undergraduate research output, MS pipeline, or tooling the department adopts?
3. Does Rick know his submarine model is being used as training data? Any IP concerns surfaced?
4. Interest in a small cross-advising arrangement with a morphism-framework research question?

### Things not to commit to in-meeting
- Do not offer hive absorption (Tier 1) — his artifacts are (a)/(b), not (c).
- Do not promise the webapp will get built.
- Do not commit the Model_Exporter into any external communication (proposal, INSIGHT) until IP clearance happens.
- Do not reframe his narrative as a production-ready tool.

### Recommended close
Formal collaboration agreement path (not hive absorption):
1. IP clearance sprint (Fort Wachs + UofA legal) on Steiner training data.
2. Scoped research question — *Quantifying Abstraction Fidelity* — with FireDrone toolchain as empirical infrastructure.
3. Handoff #1 (Model_Exporter → GI-JOE STOIC) as first concrete deliverable, clearly bounded.

---

## 9. Governance flags for later (not for this meeting)

- **Fort Wachs policy gap:** no standing rule on LLM training on course/research data. File for next Fort Wachs review cycle.
- **Fort Wachs vendor evaluation gap:** no MBSE tool assessment framework (Cameo / StudioSE / SySide / Magic Draw parallel to the Chainguard evaluation).
- **Capability index update:** if collaboration proceeds, add a "Student research collaboration" section and reference Aufmuth's toolchain as Tier 2 input to PostWach Ideas 6, 9, 13.
- **Duplicate watch:** none. His triad is SysML-domain-specialized, not a duplication of PostWach's research/philosophy agents.

---

*Archive created by PostWach CTO, 2026-04-21. Ruflo swarm `swarm-1776781909882-7ml8wf`. Three review lenses (PostWach/morphism, tooling overlap, governance). Source: LLM_MBSE_Michael Aufmuth Project.pptx (15 slides).*

# Session Archive: 2026-03-28 PostWach-01

**Date:** 2026-03-28, continued 2026-03-30
**Hive:** PostWach
**Focus:** INCOSE INSIGHT article inventory + CSER 2026 isomorphism paper strategy

---

## Session Summary

Two-part session covering both papers due end of next week (Apr 4, 2026).

**Part 1 (INSIGHT):** Re-oriented on the INCOSE INSIGHT article "From Rules to Agentic Swarms" (Wach & Salado). Conducted complete inventory, reviewed latest PDF (draft9), identified additions needed.

**Part 2 (CSER 2026 Isomorphisms):** Reviewed Brandt's notes on capacitor/air-bubble analogy (electrical vs hydraulic, 1st-order). Debated whether to pivot the paper's worked example from MSD/RLC to capacitor/bubble. Spawned 3 analysis agents (paper-architect, math-feasibility, timeline-risk) to evaluate the restructuring strategy. Reached a clear recommendation.

## Key Findings

| # | Item | Detail |
|---|------|--------|
| 1 | Article location | `Documents/02 My Outreach/INSIGHT 2026 AI History/` (outside PostWach repo) |
| 2 | Current version | v0.1 (2026-03-10), 283 lines, 9 sections, 5 figures, 2 tables, 25 references |
| 3 | PDF drafts | 9 formatting iterations (draft1-draft9), all from Mar 10 |
| 4 | Missing image files | 4 of 5 referenced PNGs not present in directory (gengroves_bridge, gengroves_architecture, macq_architecture, portfolio_overview) |
| 5 | Memory path correction | Memory referenced `03 Projects/00 My Research/02 My Outreach/`; actual path is `Documents/02 My Outreach/` |

## Candidate Additions (Noted for Next Revision)

- Problem Definition Workbench (WRT-2516 assessment framework operationalized as software tool)
- IGNITE '26 mission engineering use case (live demonstration of agentic swarm tooling for DTE&A / 4D assessment)
- Fort Wachs / CTO-COO-CISO triad, NSA ZT governance of AI swarms (noted Mar 10)
- Hive-of-hives architecture detail (noted Mar 10)
- Chainguard supply chain test case (noted Mar 10)

## Actions Taken

1. Read full article markdown
2. Opened draft9.pdf for visual review
3. Updated MEMORY.md with new candidate additions (PD Workbench, IGNITE mission engineering)

---

## CSER 2026 Isomorphism Paper — Strategy Decision

### Brandt's Notes (Reviewed)

Two documents from Brandt Sandmann:
- `Recent notes.pdf` (Mar 17): Paper direction notes. Focus on capacitor/bubble as worked example. Library framing. Transitivity question (if A->B and B->C, then A->C?). Benefits: surrogate modeling, compressed design cycles.
- `Electric_Hydraulic_Notes.pdf` (Dec 20, 2025): Detailed capacitor vs air-bubble analogy. Component mapping table from microfluidics literature. Governing equations: I(t) = C dV/dt vs DeltaQ(t) = C_H dP/dt. RC circuit ODE: RC(dV/dt) + V = V_source vs R_h*beta*(dP/dt) + P = P_source. State variables, inputs, outputs defined. Energy: 1/2 CV^2 vs 1/2 beta P^2.

### Current Paper State

- Draft v2 complete (459 lines, 7 sections)
- All 9 reviewer comments addressed
- 4 minor revision items remaining (citation fix, D_s limitation, D_h notation, terminology)
- Full Python simulation code + 4 figures for MSD/RLC
- Word submission target: `02 My Outreach/CSER 2026 - Morphisms/Wach_Sandman_Iyer_2026_CSER_Morphisms.docx`

### Analysis (3 Agents)

**Paper Architect** designed a full restructuring with library catalog table, condensed MSD/RLC (~50 lines), and new capacitor/bubble detailed section (~160 lines). Proposed 3-state abstraction for 1st-order: {Depleted, Transitioning, Saturated} based on 10%/90% thresholds.

**Math Feasibility** found:
- Physics-level isomorphism: STRONG. Clean 1st-order mapping, novel to SE formalism.
- Abstraction analysis: VIABLE BUT requires nonlinear extension. Linear 1st-order systems yield sigma=1.0 at every abstraction level (no degradation). The bubble's nonlinear gas law (compliance = V_0*P_0/P^2) provides a physically motivated degradation mechanism. Polytropic exponent gamma could parameterize sigma(gamma) as a continuous curve.
- Discretization: SUFFICIENT. Same O(dt), O(dt^4), exact scaling. Novel theorem: for linear systems, uniform discretization preserves inter-system isomorphism.
- Key finding: 1st-order shifts the degradation story from "abstraction coarsening" to "modeling fidelity," which is a different (arguably stronger) SE message.

**Timeline/Risk** found:
- Full pivot: 5-7 days, high risk, reviewer perception concerns.
- MVC (keep MSD/RLC + add capacitor/bubble): 3-4 days, low risk, strictly dominates.
- Nuclear fallback: submit v2 with 4 minor items only (~4 hours).

### Recommendation: Keep MSD/RLC, Add Capacitor/Bubble

All three agents converged on the same answer: **extend, do not replace.**

| Element | Treatment |
|---|---|
| MSD/RLC | Condense to ~50 lines. Catalog Entry #1. Keep degree=0.78 and discretization figures. |
| Capacitor/Bubble | NEW detailed entry (~120-160 lines). Physics isomorphism + 3-to-2 state abstraction (degree ~0.83) + discretization. |
| Library catalog | NEW table of ~19 identified pairs with characterization status. |
| Framing | Shift intro/conclusion to "building a library; two entries characterized here." |
| Net size | ~510 lines (modest growth; MSD/RLC shrinks to compensate). |

### Execution Timeline

| Day | Date | Milestone |
|---|---|---|
| 1 | Mar 28 | Decision confirmed. Define Wymore tuples. Fix 4 minor items. Contact Brandt. |
| 2 | Mar 29 | Simulation code + 2 new figures. |
| 3 | Mar 30 | Write Section 5.3 (capacitor/bubble). **Go/no-go gate.** |
| 4 | Mar 31 | Rewrite Sections 1, 4, 5.1 (library framing + catalog). Condense 5.2. |
| 5 | Apr 1 | Rewrite Sections 6, 7. Update abstract + references. |
| 6 | Apr 2 | Transfer to Word. Send to co-authors. |
| 7 | Apr 3 | Incorporate feedback. Submit. |

### Fallback

If 1st-order abstraction analysis fails by Day 3: use capacitor/bubble for discretization-axis only (still a second catalog entry). If everything fails: submit v2 with 4 minor items addressed.

---

---

## 2026-03-30 Continuation: INSIGHT Article Editing

### Changes Made

**Title:** Changed from "The History and Current State of AI for Systems Engineering" to "A Systems Engineering Journey Through the Evolution of AI" (addresses Alejandro's concern that "history" implies comprehensive historiography rather than practitioner perspective).

**Authors:** Added Brad Philipbar (USAFA) as third co-author. He created ZynWorld.

**New content added by user:**
- PHM Testbed case study (Sections 3 and 4): ML/DL limitations in predictive maintenance; performance degrades after part replacement; data-fusion with physics-based M&S as potential solution
- 5 new rows in Table 2: Problem Definition Workbench, SCAR, FortWachs, ZynWorld, HOS
- GI-JOE updated (added OML, BFO/CCO-aligned)
- MACQ description expanded in intro (SEP generation, CDR entry/exit)

**Fixes applied by assistant:**
- 6 typos corrected (tranditional, moniotoring, CMB→CBM, maintanence, liefcycle, Prognastics/Mannagement)
- Stale counts updated: abstract (4→5 systems, 9→14 portfolio), Section 9 prose (4→5 case studies, 9→14 systems)

**PDF generated:** `Wach_Salado_INSIGHT_2026_AI_History_v0.2_draft1.pdf`

### Outstanding Items

**Missing figures (4 of 5 referenced PNGs not in directory):**
1. `gengroves_bridge.png` — Figure 2: GenGroves workforce bridge diagram
2. `gengroves_architecture.png` — Figure 3: GenGroves agentic AI framework
3. `macq_architecture.png` — Figure 4: MACQ swarm architecture
4. `portfolio_overview.png` — Figure 5: UA AI-for-SE research portfolio map

(Only `AI_history_overview_v4_cropped.png` — Figure 1 — exists)

**Other remaining items:**
- PHM Testbed reference(s) needed (user will provide)
- Brad Philipbar bio needed for Author Biographies section
- Alejandro has not yet read the paper (only the title)
- Figure 5 caption and Table 2 description still say "nine systems" in the figure alt-text (line 210)
- Consider whether Figure 1 timeline graphic needs updating (currently shows 6 paradigms, unchanged)

---

## 2026-03-31 Continuation: INSIGHT Article Major Revision

### Alejandro's Feedback (7 items)

| # | Comment | Resolution |
|---|---|---|
| 1 | "Piloted" vs "developed" | Changed to "constructed" |
| 2 | Rule explosion/inconsistency | Added sentence to Section 2 |
| 3 | First Houston paper (IEEE SMC 2020) | Added: Salado and Tan 2020, DOI: 10.1109/SMC42975.2020.9283466 |
| 4 | ML input fragility | Added sentence to Section 3 |
| 5 | Scope adoption lag to SE practice | Renamed to "SE practice adoption lag," added "known" qualifier. Rejected full scope change to preserve compression thesis. |
| 5.5 | LLM validation boldness | Redirected to new Section 9 paragraph |
| 6 | Cautionary validation statement | Added "Validation in the age of rapid adoption" paragraph in Section 9 |
| 7 | García Alarcia et al. reference | Added reference + citation in validation paragraph |

### Additional Changes (User's 17-item review of draft5)

| # | Item | Resolution |
|---|---|---|
| 1 | "across the timeline" → "across the paradigms" | Applied in abstract + intro |
| 2-3 | SE acronym redundancy | Noted (model-based SE, AI-for-SE already use acronym) |
| 4 | "Defense adoption lag" → "SE practice adoption lag" | Applied. Table 1 header changed to "Approx. SE Adoption Lag" |
| 6 | Remove all bold except section titles | Applied throughout (era spans, case study labels, bullet lists, Section 9 subheadings) |
| 7 | Figure 1 enlarged | Set width=100%, renders full text width |
| 8 | Red/blue/white team review | Agents hit API overload. Performed manually. |
| 9 | PHM Testbed rewrite | Added "For example," removed extraneous Adams et al. reference, removed trailing Hamilton citation |
| 10 | Remove dashes in prose | Fixed TurboArch section (em dashes → parentheses). Dashes in formal titles kept. |
| 11 | Remove Figures 2-5 | Removed gengroves_bridge, gengroves_architecture, macq_architecture, portfolio_overview references |
| 12 | ISO/DoD refs in Agentic Swarms | Removed (not relevant to swarm definition) |
| 13 | Parallel execution wording | Changed "independent subtasks" → "subtasks, whether independent or coordinated" |
| 14 | PHM in progression paragraph | Added PHM Testbed to Section 7 and Section 8 throughlines |
| 15 | Table 1 and 2 font sizes | Both now have \small tag |
| 16 | Compression section consistency | PHM Testbed added to throughline |
| 17 | Remove "UA" | Changed "University of Arizona investigating" → just "investigating" |

### Reference Audit (Red Team, manual)

| Issue | Resolution |
|---|---|
| PLACEHOLDER Wach & Salado 2020 | Resolved: Salado and Tan 2020 (IEEE SMC) |
| ORPHAN Adams et al. 2026 | Removed |
| ORPHAN DoD 2018 | Removed |
| ORPHAN ISO/IEC/IEEE 2023 | Removed |
| ORPHAN Shinn et al. 2023 | Removed |
| MISSING Valerdi 2005 | Added (COSYSMO dissertation) |
| Orphaned bold `**` in era spans | Fixed (6 instances) |

### Table 2 Updates
- Added PHM Testbed row (ML/DL, predictive maintenance)
- Added Systems Theoretic Assistant row (Agentic Swarms, SE theory and verification, cites Wach et al. 2025c)
- Added Wach et al. 2025c reference (Systems Theoretic Co-Pilot MVP, CSER)
- Total systems now 16
- All counts updated (abstract, Section 9, Figure 5 alt-text)

### User Bio Update
- Paul Wach bio rewritten: "developing" not "developer of," updated system list (HOS, MACQ, GI-JOE, SEAD, COSYSMOS, PLMr, SysMLv2 Hive, Problem Definition Workbench), "SE4AI/AI4SE" research framing

### Current PDF
`Wach_Salado_INSIGHT_2026_AI_History_v0.2_draft7.pdf` (only Figure 1 rendered, Figures 2-5 removed by design)

### Late Update
- User updated Systems Theoretic Assistant description in Table 2: "Neuro-symbolic agentic swarm, STOIC, cross-domain isomorphism/homomorphism library"
- User updated Paul Wach bio
- Generated draft7 PDF

### ARTICLE SUBMITTED
- Final version: `Wach_Salado_INSIGHT_2026_AI_History_v0.2_draft7.pdf`
- Submitted 2026-03-31

---

## Session Closed

**CSER 2026 Isomorphisms (carried forward):**
- Contact Brandt to confirm air-bubble ODE and parameter values
- Begin Day 1 items: Wymore tuples for 1st-order, fix 4 minor revision items
- Decision: user to confirm the "extend, do not replace" recommendation

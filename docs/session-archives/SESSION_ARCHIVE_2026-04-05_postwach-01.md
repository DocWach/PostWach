# Session Archive: 2026-04-05 PostWach-01

**Hive:** PostWach
**Date:** 2026-04-05
**Duration:** ~7 hours
**Focus:** CSER 2026 isomorphism library paper revision, deep theoretical discussion on morphism foundations

---

## Objectives
1. Review status of CSER 2026 paper ("Toward a Library of Isomorphic Patterns for Systems Engineering")
2. Review Brandt Sandmann's rejected IS 2026 paper on capacitor/bubble morphism
3. Determine whether to merge the two papers
4. Create presentation for CSER 2026
5. Develop refined paper outline through iterative discussion

## Key Decisions

### D1: Restructure CSER paper as library methodology (Option C)
- Paper shifts from "we characterized one isomorphism" to "we provide a repeatable methodology demonstrated on two pairs"
- Capacitor/bubble (first-order, single-element) added as first library entry
- MSD/RLC (second-order, multi-element) remains as second entry revealing deeper questions
- New Section 5.3 compares what each pair reveals

### D2: Do NOT use sigma for degree of homomorphism
- Sigma is a statistical term (standard deviation, sigma levels) and will cause confusion in the SE community
- Use spelled-out "degree of homomorphism" throughout
- Tuple representation D_h = (D_s, D_b) continues the Wymorian tuple lineage
- Must fix: combined_draft.md (3 locations), MEMORY.md notation lineage, presentation files

### D3: Degree of homomorphism is computable at any point in the lifecycle
- Not restricted to any specific phase. Can be evaluated continuously.
- Avoid "design-time" and "run-time" terminology (software terms, not SE terms). Use "during development" vs. "during operations" or simply "at any point in the lifecycle."
- Strengthens the "why this matters" argument: enables continuous verification and digital twin monitoring

### D4: D_align not for CSER paper
- Three-axis framework (structural, behavioral, alignment) is for Circuit Breaker line only
- CSER paper stays with two-axis D_h = (D_s, D_b)

### D5: System vs. component distinction does not exist in Wymore's formalism
- A capacitor IS a system. A bubble IS a system. "System" is a human modeling construct.
- Previous characterization of "component-level vs. system-level morphism" was incorrect
- Correct framing: simpler system (first-order) vs. more complex system (second-order, multi-element)

### D6: Modeling choices as a methodological contribution
- Constitutive properties (k, c, m, L, R, C) are system properties, not inputs. They define N_Z. Changing them yields a different system.
- This belongs in the Methods section (Step 0: well-formed system models), not just Discussion
- Parameter drift (aging, fatigue) belongs in Discussion as an operational degradation scenario
- Reference Wach & Salado (2022) "The Need for Semantic Extension of SysML to Model the Problem Space" — modeling choices affect problem space definition, not just system models

### D7: Isomorphisms are nominal reference points, not permanent properties
- The isomorphism exists in the physics under idealized conditions (linear, time-invariant, nominal parameters)
- Real systems approximate it to varying degrees at any given moment
- Degree of homomorphism measures departure from the nominal reference, computable at any lifecycle point
- For digital twins: the morphic relationship between twin and real system degrades as the real system ages but twin parameters aren't updated

### D8: Paper structure — distinct Background vs. Related Literature
- Background (own work lineage) goes in Introduction
- Related Literature (others' work, due diligence) gets its own section
- Wymore's formalism, degree of homomorphism, and D_h tuple go in Methods (they are analytical tools we USE, not context)

### D9: Catalog scope — established pairs only
- No speculative or partial entries in the paper's catalog table
- Only entries with citable literature support (6 established pairs after consolidation)
- Speculative and partial pairs go in Future Work section
- s-domain/z-domain removed: a signal is not a system in Wymore's formalism; needs methodological resolution before inclusion

### D10: Analogy conventions — one entry with variants
- Force-voltage (Maxwell, series RLC) and force-current (Firestone, parallel RLC) are two conventions for the same physical equivalence
- Catalog shows one entry with two convention variants, not two separate entries
- Similarly, translational/rotational with/without lever-gear coupling is one entry with variants
- Full 8-configuration analysis (2 mech configs × 2 elec configs × 2 conventions) is future work / journal paper

### D11: Morphic chain reserved for future work
- The chain concept (real system → models at decreasing fidelity) is important but not for this paper
- Needs careful characterization before stating (e.g., "weakest link bounds confidence" is intuitive but unproven)
- Connects to partial and approximate morphisms, which are excluded from CSER paper scope

### D12: Degree of homomorphism is evolving
- Currently defined over S_Z, I_Z, O_Z sets only (reciprocal mapping cardinality)
- N_Z and R_Z are constrained by conditions iv-v (binary: commutes or doesn't) but not incorporated into the degree metric
- Output distance D_b captures behavioral fidelity of N_Z and R_Z indirectly
- Whether N_Z/R_Z should be incorporated directly into degree of homomorphism is an open research question
- Equal weighting of S, I, O is a limitation; verification-relevant weighting is future work
- Address in CSER paper as a brief limitation note (one sentence in Section 6.4)

### D13: Problem space implications
- Modeling choices are not just a system modeling issue; they are also a problem space issue
- If the problem space selects force/current convention, it excludes force/voltage system models from the solution space
- This connects back to Wach & Salado (2022) problem space paper
- Future work, not for CSER paper

### D14: D_h notation clarified
- D_h = degree of homomorphism (not "degradation vector")
- D_h = (D_s, D_b) where D_s = structural degree, D_b = behavioral degree
- D_s itself is a tuple: D_s = (DoH_S, DoH_I, DoH_O), with scalar average as convenience
- D_s is computed analytically from the Z tuple structure; D_b is measured empirically through verification activity (simulation or test)
- The distinction between D_s and D_b arises from T3SD's separation of specification from execution

### D15: N_Z and R_Z are sets, but separate DoH measures not needed for exact morphisms
- N_Z and R_Z are sets of ordered pairs (functions ARE sets in set theory)
- In principle, reciprocal-cardinality could apply to them
- But for exact morphisms where conditions iv-v are satisfied, commutativity is binary (holds or doesn't). No "degree" to measure.
- DoH_N and DoH_R become important for approximate morphisms (future work)
- Current D_s = (DoH_S, DoH_I, DoH_O) is the right measure for exact morphisms, not an incomplete hack

### D16: Catalog reduced to 6 established pairs
- Removed s-domain/z-domain: a signal is not a system in Wymore's formalism, needs methodological resolution
- Removed all partial and speculative entries
- Consolidated analogy convention variants (force-voltage/force-current) as one entry with two conventions noted
- Consolidated translational/rotational with/without coupling as one entry

### D17: T3SD vs. DEVS formalism choice
- Stay with T3SD for the CSER paper (simpler, matches prior work lineage, discretization analysis is a feature not a bug)
- DEVS reformulation as distinct future work item (journal paper)
- Key insight: in DEVS, the specification-simulation gap disappears because the model IS the simulation. This would reframe D_s/D_b distinction.
- DEVS also provides closure under coupling theorem for compositional analysis

### D18: Section-by-section expansion before drafting
- User confirmed: go through each section with bulleted descriptions before writing prose
- Sections needing pre-drafting discussion: 1 (Introduction), 3 (Methodology), 4 (Catalog), 5.1 (Capacitor/bubble), 5.3 (Comparison), 6 (Discussion)
- Sections largely reusable from existing draft: 2 (Related Literature), 5.2 (MSD/RLC)

### D19: Discretization analysis dropped from paper
- Discretization-induced "isomorphic degradation" was NOT a morphism result. Both systems have identical state-space matrices under the variable mapping, so ANY discretization preserves the isomorphism. D_b between the two discretized systems is always 0.
- The existing analysis measured single-system numerical truncation error (discretized vs. continuous reference), which is textbook numerical analysis (Euler O(dt), RK4 O(dt^4), exact preserves).
- Paper's primary finding is now abstraction-induced degradation only (one axis, not two).
- D_b remains in D_h = (D_s, D_b) as an empirical behavioral measure from verification activity.
- Discretization content moves to a footnote/brief paragraph and a backup presentation slide.
- Freed ~1.5 pages for capacitor/bubble entry and expanded WySE discussion.
- Caught because the capacitor/bubble simulation returned D_b = 0 across all methods, forcing the question "why?"

### D20: WySE Metamodel as application, not primary motivation
- Core intent: mathematical foundations for domain-agnostic SE
- The library serves that foundational goal
- WySE is one important construct that benefits from the library (requires homomorphism but doesn't prescribe degree characterization)
- WySE appears in: Introduction (prior work lineage), Section 3.1 (methodology context), Section 6.2 (verification implications)
- But the library's value extends beyond WySE to SE foundations broadly
- User corrected an over-emphasis on WySE that had crept into the plan

## Theoretical Insights Developed During Session

### Insight T1: Force-voltage vs. force-current analysis
- Four pairings analyzed (Kelvin-Voigt MSD × {series, parallel RLC} × {force-voltage, force-current})
- Result: each convention works with exactly ONE circuit topology. Force-voltage pairs with series. Force-current pairs with parallel. Cross-pairings fail.
- Convention and topology are coupled, reflecting underlying duality
- Full 8-configuration space (adding Maxwell viscoelastic MSD) is unanalyzed
- Logged in `memory/research_analogy_conventions.md`

### Insight T2: Isomorphism as nominal reference
- Isomorphisms exist in physics independently of models
- But they are idealizations: nominal parameters, linear, time-invariant
- Real systems depart from this nominal reference over time (aging, drift, environmental changes)
- Degree of homomorphism quantifies departure at any moment
- Shifts framing from binary ("is/isn't isomorphic") to continuous ("how far from the nominal isomorphism")

### Insight T3: What the community takes for granted (5 assumptions identified)
1. Degree of homomorphism is monotonically decreasing along the morphic chain (unproven)
2. Homomorphism implies representativeness (conditions i-v say nothing about verification relevance)
3. Morphic relationship is static within a lifecycle phase (it's actually drifting continuously)
4. A single degree of homomorphism characterizes the relationship (equal weighting may hide critical degradation)
5. The nominal isomorphism is the right reference point (nominal according to which lifecycle stage?)

### Insight T4: Multiple conventions as a library property
- The same physical equivalence admitting multiple valid morphisms (through different conventions) is a property of the library itself, not just of individual entries
- This is a contribution of the library concept: documenting not just that morphisms exist, but the space of valid morphisms for each pair

### Insight T5: D_s vs. D_b distinction is a consequence of formalism choice
- T3SD separates model specification from model execution. D_s characterizes the specification; D_b characterizes the execution.
- In DEVS, the model IS the simulation (simulation semantics are embedded). The specification-simulation gap would disappear or shift.
- The discretization degradation analysis (Euler, RK4, exact) is really an artifact of using T3SD. In DEVS, this would be reframed as: "what DEVS model best represents the continuous physics?"
- This insight motivates DEVS reformulation as future work, but also means our current discretization analysis reveals something real and practical for T3SD users.

### Insight T6: N_Z/R_Z importance depends on morphism type
- For exact morphisms (current scope): N_Z and R_Z commutativity is guaranteed by conditions iv-v. Binary. DoH_N/DoH_R would add no information.
- For approximate morphisms (future scope): N and R become arguably MORE important than S, I, O because the dynamics divergence is where the interesting degradation occurs.
- The "most important" Z-tuple element depends on the verification question being asked (input coverage, output prediction, state estimation, behavioral simulation).

### Insight T7: The 4-pairing analysis (force-voltage/force-current × series/parallel)
- Each analogy convention works with exactly ONE circuit topology
- Force-voltage pairs with series RLC. Force-current pairs with parallel RLC. Cross-pairings fail.
- Convention and topology are coupled, reflecting the underlying series-parallel duality.
- This is a clean, provable result. Full 8-config analysis (adding Maxwell viscoelastic MSD) is unresolved.

## Work Completed

### Paper edits (combined_draft.md)
- Added D_h = (D_s, D_b) degradation vector notation (Section 6.1 + Table 1)
- Added D_s bound limitation acknowledgement (Section 6.4)
- Fixed reference [10] (von Bertalanffy, added publisher info)
- Cited reference [8] (was unused in body text)
- Completed Acknowledgements (SERC WRT-2516 + PostWach)
- **NOTE:** These edits used sigma notation which must now be corrected per D2

### Figures created
- `paper/figures/rlc_circuit_diagram.png` (200 DPI, matplotlib)
- `paper/figures/msd_system_diagram.png` (200 DPI, matplotlib)

### Presentation created
- `02 My Outreach/CSER 2026 - Morphisms/Wach_Sandman_Iyer_CSER2026_Presentation.md` (markdown)
- `02 My Outreach/CSER 2026 - Morphisms/Wach_Sandman_Iyer_CSER2026_Presentation.pptx` (17 slides, 326 KB)
- **NOTE:** Presentation will need complete rebuild after paper restructure

### Revision plan created
- `paper/CSER2026_Revision_Plan.md` — v3 outline with full section descriptions, page budget, work plan. Reflects all decisions D1-D18.

### Papers extracted to master copies
- `Wach_Salado_2022_Need_Semantic_Extension_SysML_Problem_Space.pdf` (11 pages, 230 KB) — extracted from CSER 2019 book
- `Cratsley_Regmi_Wach_Salado_2022_SysML_StateMachine_Interpretation.pdf` (10 pages, 308 KB) — extracted from same book

### Memory files created/updated
- `memory/feedback_discuss_before_executing.md` — discuss before acting on multi-step tasks
- `memory/feedback_background_agents.md` — auto-spawn background agents for non-critical tasks
- `memory/research_analogy_conventions.md` — force-voltage vs. force-current conventions + 8-config space
- `memory/MEMORY.md` — updated notation lineage (no sigma), added analogy conventions reference, added behavioral rules

## Documents Reviewed

### CSER 2026 (own paper)
- `combined_draft.md` (Feb 25, 2026) — full revision draft, read completely
- `reviewer_comments.pdf` (Feb 13, 2026) — 3 reviews (accept, weak reject, weak accept)
- `notes.docx` (Mar 23, 2026) — 9 revision directives (read via python-docx)
- `outline.docx` (Dec 15, 2025) — original paper structure (read via python-docx)
- `Wach_Sandman_Iyer_2026_CSER_Morphisms.docx` (Dec 15, 2025) — original submission structure (read via python-docx)
- `Recent notes.pdf` (Mar 28, 2026) — co-author meeting notes from Mar 17
- `Electric_Hydraulic_Notes.pdf` (Dec 20, 2025) — Brandt's capacitor/bubble research
- `library/catalog.json` — 19-entry isomorphism catalog (read completely)
- `references.bib` — 20 bibliography entries

### IS 2026 (Brandt's paper)
- `Sandman_Wach_IS_2026_draft.pdf` (Feb 23, 2026) — full 10-page draft (incomplete), read completely
- `Updated hydro-electric notes.pdf` (Jan 1, 2026) — detailed component mapping + constitutive relations
- `outline.docx` (Dec 19, 2025) — paper structure
- `reviewer comments.pdf` (Mar 9, 2026) — 4 reviews, all noted incompleteness

### CSER 2019 book (Springer, 2022)
- `CSER_2019_bookpub_2022.pdf` — TOC and two chapters extracted

### Memory files reviewed
- `circuit-breaker-details.md` — v3/v4 design spec summaries, terminology reconciliation
- `MEMORY.md` — notation lineage, revision items, cross-project connections

### NOT reviewed (gaps identified)
- Paul's dissertation (cited but not read; morphic chain inferred, not verified)
- AI Circuit Breaker design spec v3 and v4 source files
- Jeffrey's TDD v2.0 and ECG Signal Architecture
- Individual section files (01-07) for divergence from combined_draft.md

## Current Outline (v3, final for this session)

See `paper/CSER2026_Revision_Plan.md` for full detail. Summary:

**1. Introduction** (~1 page) — problem, library vision, isomorphisms as nominal reference points, isomorphic degradation, own work lineage, contribution (methodology + 2 entries + 2-axis degradation)
**2. Related Literature** (~0.75 pages) — others' work: cross-domain analogies (Maxwell→Karnopp), morphisms in SE lit (informal usage), gap
**3. Library Methodology** (~1.25 pages) — 3.1 T3SD formalism + note on formalism choice, 3.2 D_h = (D_s, D_b) with D_s as tuple (DoH_S, DoH_I, DoH_O) + N/R handling for exact vs. approximate, 3.3 well-formed system models (constitutive properties vs. inputs, analogy conventions), 3.4 six-step procedure, 3.5 term definitions
**4. The Isomorphism Catalog** (~0.5 pages) — 6 established pairs only (table with citations), convention notes, selection rationale
**5. Two Library Entries** (~4 pages) — 5.1 capacitor/bubble (simple, first-order), 5.2 MSD/RLC (complex, second-order), 5.3 cross-entry comparison (what complex reveals that simple cannot, multiple conventions as library property)
**6. Discussion** (~1.5 pages) — 6.1 meaning (two-axis, isomorphisms exist in physics but characterization depends on modeling choices), 6.2 verification (lifecycle-continuous DoH, parameter drift, digital twins, verification planning), 6.3 practical implications, 6.4 limitations (N/R for exact morphisms, averaging question, T3SD formalism, D_s bound), 6.5 future work (remaining pairs, 8-config, compositional, DoH evolution, approximate morphisms, DEVS reformulation, category theory, nonlinear, problem space)
**7. Conclusion** (~0.5 pages)

## Open Items / Blockers

1. **DEADLINE: Paper was due over a week ago. Presentation is Tuesday April 8.**
2. **Next step: Section-by-section bulleted expansion** of Sections 1, 3, 4, 5.1, 5.3, 6 before drafting prose
3. **Sigma notation removal:** Must fix combined_draft.md (3 locations) and presentation files
4. **Capacitor/bubble full analysis:** Simulation + discretization, complete regardless of what goes in paper
5. **Page budget:** ~10 pages, tight but feasible with trimmed MSD/RLC detail
6. **Word template transfer:** Final paper into CSER Word template
7. **Presentation rebuild:** PPT must reflect restructured paper (current PPT is based on pre-restructure outline)
8. **Wach dissertation review:** Should read morphic chain sections before any future paper that references it
9. **Wach & Salado (2022) citation:** Add to CSER paper references for Step 0 / problem space connection

## Behavioral Notes
- User prefers to discuss status and plan before execution on multi-step tasks. Saved as feedback memory.
- Non-critical-path tasks (PDF extraction, file ops) should be auto-spawned as background agents without user prompting. Saved as feedback memory.
- This session demonstrates PostWach's core function: intelligent debate to reason through and concretize theoretical ideas. The discussion itself is a research output, not just a means to an end.

## Future Work Items Identified (research program depth)
1. Full 8-configuration MSD/RLC analysis (2 mech × 2 elec × 2 conventions) — journal paper
2. Compositional morphisms and emergence — journal paper
3. Morphic chain characterization and confidence bounds — journal/dissertation extension
4. Partial and approximate morphisms — extends degree of homomorphism, N_Z/R_Z degree measures become important here
5. Problem space implications of modeling/convention choices — connects to Wach & Salado (2022)
6. N_Z/R_Z incorporation into degree of homomorphism — for approximate morphisms only; for exact morphisms, current D_s is sufficient
7. Verification-relevant weighting/aggregation of D_s components — open whether averaging, weighting, or full tuple is best
8. s-domain/z-domain as system models — needs "is a signal a system?" resolution before catalog inclusion
9. Category-theoretic framework (systems as objects, morphisms as arrows, discretization as functor)
10. Nonlinear and stochastic extensions
11. Transitivity verification (if A→B and B→C, does A→C? Under what conditions?)
12. Remaining 4 established catalog pairs + candidate speculative pairs
13. DEVS reformulation of library methodology — eliminates specification-simulation gap, provides closure under coupling for compositional analysis
14. D_h indexing for multiple pairings (D_hi where i indexes the catalog) — deferred, too early to formalize

---

## Session Completion

**Final deliverables produced:**
- `paper/Wach_Sandmann_Iyer_CSER2026_Isomorphism_Library_Draft_v1.md` — complete paper draft, all sections, reviewed by red/blue/white team, corrections applied
- `02 My Outreach/CSER 2026 - Morphisms/Wach_Sandman_Iyer_CSER2026_Isomorphism_Library_v1.docx` — Word template transfer (pending completion)
- `02 My Outreach/CSER 2026 - Morphisms/Wach_Sandman_Iyer_CSER2026_Presentation_v3.pptx` — 19-slide presentation
- `paper/CSER2026_Revision_Plan.md` (v4) — final outline
- `paper/CSER2026_Section_Descriptions.md` + PDF — detailed section bullets
- `paper/sections/capacitor_bubble_models.md` — complete capacitor/bubble analysis
- `src/simulation/capacitor_bubble.py` — simulation code
- 6 figures generated (RLC diagram, MSD diagram, cap/bubble step response, cap/bubble discretization, cap/bubble energy, combined discretization)
- 2 papers extracted to master copies (Wach & Salado 2022, Cratsley et al. 2022)

**Review results (red/blue/white team):**
- Blue team: all 14 session decisions PASS, all 4 reviewer concerns addressed
- White team: notation clean, math correct, 9 findings (all addressed except placeholders)
- Red team: 3 critical, 7 major, 10 minor. Criticals: four-state N_Z missing (deferred to tomorrow review), placeholder refs (resolved), novelty defense (structural). Four-state conceptual validity flagged for discussion.

**Open for tomorrow's review:**
1. Four-state model conceptual validity (states vs. system types) — HTML comment in draft marks the location
2. Final page count verification after Word template rendering
3. Sandman spelling confirmed (single n)
4. References [25], [26] filled with Lab on a Chip and Standing Air Bubble papers (verify exact citations)

**Total agents spawned this session:** ~15 (paper explorer, quality reviewer, format researcher, PPT v1/v2/v3, capacitor/bubble sim, section bullets, combined figure, Cratsley extractor, PDF gen, paper writer, red/blue/white team, corrections, Word transfer)

*Session complete. Scorecard filed separately.*

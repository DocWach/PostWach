# White Synthesis — RBW Adjudication of Jeffrey's Proposed Rewrite

**Date:** 2026-05-20.
**Inputs:** `red_team_jeffrey_draft_v0.1.md`, `blue_team_jeffrey_draft_v0.1.md`.
**Source under review:** `02 My Outreach/2026_SERC_AI4SE_SE4AI/AICB_SERCabstract_2026-05-07.pdf` (Jeffrey Wallk proposal).
**Baseline:** `02 My Outreach/2026_SERC_AI4SE_SE4AI/Wach_Wallk_AICircuitBreaker_Abstract_v0.5.md`.
**Companion (pending):** `Dr_literature_scoping_v0.1.md` + `Dr_construct_analysis_v0.1.md` will produce the formal D_r reformulation. This synthesis takes the red/blue convergence on D_r as a directive and defers the formal mechanics to that memo.
**Output:** directives for a v0.6 draft. Authoring control stays with Paul; Jeffrey reviews against the directives.

## Convergence between Red and Blue

Both teams, working independently from the same source, converged on the following adjudications:

| ID | Addition | Red verdict | Blue verdict | White directive |
|----|----------|-------------|--------------|-----------------|
| J1 | Three research traditions to five | Category error: 5D is a research artifact (a) per R016, not a peer tradition | Defensible only if framed as a layered explanation (morphisms + GUM + SPC load-bearing; STPA grounds thresholds; 5D grounds envelope), not as five peers | **Frame as layered.** Keep three peer traditions plus one added sentence: STPA grounds Layer 3 thresholds, 5D grounds the Layer 1 operational envelope. Do not list 5D as a fifth peer tradition. |
| J2 | Two-axis morphism distance to three-axis | Fatal: D_r is not a metric, conflates morphism quality with operational envelope, falsely claims to extend CSER 2026's two-axis bounds | Salvageable only as a different construct: D_r is a Layer-1 envelope-validity measurand, not a third coordinate of the same morphism metric | **Strong convergence. Demote D_r to a Layer-1 envelope-status construct.** Rename to avoid collision with Paul's existing `C_r` (Design Spec v4 line 150, where `C_r` = behavioral axis = D_b). Drop the "extends CSER 2026 bounds" claim entirely; D_r operates at a different architectural layer and time scale and does not need to compose mathematically with D_s, D_b. Final mechanics deferred to the companion D_r recommendation memo. |
| J3a | UCA-grounded SPC thresholds | Acceptable as Layer 3 engineering hygiene | Defensible as-is, no novelty required | **Adopt.** One added paragraph in Layer 3 keying SPC excursions to named UCAs. No novelty claim attached. |
| J3b | Non-stationary UCA-space detection | Major. "First SE framework" claim falsifiable on Thomas 2013, Leveson and Thomas 2018, Abdulkhaleq et al. 2015 | Defensible with hedge: the runtime-UCA-drift-indicator composed with a Wymorian morphism-quality instrument may be SE-venue novel | **Adopt with the v0.3 hedge convention** ("to our knowledge, in the SE-venue context"). Cite Thomas 2013 and Leveson and Thomas 2018 as adjacent prior work. Confirm citations before submission (Red flagged Thomas 2013 + Abdulkhaleq et al. 2015 as unverified). |
| J4 | Layer 4 holonic immune system | Major. Prior art on holons (Koestler 1967, Van Brussel et al. 1998 PROSA), artificial immune systems (Castro and Timmis 2002). "Metastatic" undefined | Defensible with narrowing: keep holon-as-portability-primitive and cross-holon surveillance; drop the immune-system biology | **Strong convergence. Narrow to holon-as-portability.** One paragraph in Layer 4: each deployed Circuit Breaker is a self-contained holon carrying its own SPC state, ontology version, and UCA boundary; domain transfer is holon instantiation. Cite Koestler 1967 and Van Brussel et al. 1998. Drop "holonic immune system," "metastatic adaptation," and "homeostatic / allostatic / circadian" biological vocabulary. The single surviving bio-inspired motif is the existing v0.5 "bio-inspired homeostatic control" mention in Layer 4. |
| J5 | Phase III flipped from cost-estimate to executed instantiation | Major scope creep; doubles workshop footprint, funding-credibility risk | Defensible as-is (cleanest win, budget-feasibility check needed) | **Adjudication.** Adopt the substantive move (estimate to measurement) but explicitly scope as a stretch deliverable: minimum success is v0.5's cost-estimation protocol; target success is one executed instantiation. This keeps Blue's "sharper engineering claim" without absorbing Red's "two phases inside one" overcommitment. |
| J6 | Three "to our knowledge first" claims | Major. Prior-review regression of the C31/C32 pattern white synthesis already retired | Defensible with the v0.3 hedge convention | **Apply the hedge convention globally.** "To our knowledge, in the SE-venue context, this composition has not previously appeared." Cite the closest prior art adjacent to each retained claim. |

## Lit-review-driven additions

Red surfaced near-prior-art that must be cited as adjacent for any novelty claim that survives:

- **Non-stationary UCA detection (J3b):** Thomas, J. (2013) MIT PhD dissertation on STPA-derived UCA tables; Leveson, N. and Thomas, J. (2018) *STPA Handbook* on adaptive systems; Abdulkhaleq, A., Wagner, S., Leveson, N. (2015) "A Comprehensive Safety Engineering Approach..." *Procedia Engineering*. All three are **Unverified — flag for lit check** before final submission. The lit-review-scoping review's entries on runtime assurance (Cofer 2020, Schierman 2020, Paramasivam 2023) are also adjacent and were already cataloged in `lit_review_scoping_v0.1.md`.
- **Holonic agent architecture (J4):** Koestler, A. (1967) *The Ghost in the Machine*; Van Brussel, H. et al. (1998) "Reference architecture for holonic manufacturing systems: PROSA," *Computers in Industry* 37(3):255–274; Castro and Timmis (2002) *Artificial Immune Systems*. Verify Van Brussel et al. DOI and Castro and Timmis edition.
- **5D context relevancy (J4 envelope):** No external anchor exists. The framework comes from Wallk's `Morphism Assurance (Master Composition Document).docx` and `5 Dimensions of Relevancy.docx`. Both are status (a) per R016. Cite as internal sources and frame as a proposed envelope structure, not as a validated construct.

## Reference accuracy fixes

- Add Leveson 2011 (*Engineering a Safer World*, MIT Press). Already in Jeffrey's reference list as [5]; preserve.
- Add Koestler 1967 and Van Brussel et al. 1998 PROSA if holon-as-portability is retained.
- Add Thomas 2013 + Leveson and Thomas 2018 + Abdulkhaleq et al. 2015 if non-stationary UCA detection is retained (verify all three).
- **CBTO counts (25/20/12/6/10):** Jeffrey preserves the v0.5 numbers and adds "the ontology is being extended to accommodate the five-dimensional relevancy framework, UCA-space state representation, and holarchic agent identity." The 25/20/12/6/10 baseline underestimates what the abstract is now promising. Either verify against the live CBTO file and update or qualify as "current baseline, with extensions in progress for the envelope, UCA, and holon constructs."

## Construct integrity fixes

- **Rename J2's D_r.** Paul's existing `C_r` in Design Spec v4 already denotes the behavioral axis equivalent to D_b. The collision propagates to the journal paper. Suggested rename: D_e for envelope, D_a for applicability, or keep "context relevancy" as a name but use a different symbol. Final symbol choice deferred to the D_r recommendation memo.
- **Drop the "extending the two-axis bounds from [Wach et al., CSER 2026] to three axes" claim** from Key Advancements bullet 4. CSER 2026 has no such extension. Misstating the lineage exposes the joint paper to authorship dispute with Sandmann and Iyer.
- **Reconcile the Figure 2 visual contradiction.** Jeffrey's Figure 2 shows D_r as bubble size on a 2D plot, not as a third axis. The visual already says D_r is not a coordinate. Either replace the figure with one consistent with the abstract's textual claim or update the text to match the figure. With D_r demoted to envelope status, the v0.5 two-axis figure is correct as-is; bubble size or a sidebar D_r indicator becomes optional decoration.

## Internal-artifact hygiene (R016 tagging)

- **5D context relevancy** is from Wallk's source docs (research artifact (a)). Cite as internal sources. Phrase as "we propose a five-dimensional WHO/WHAT/WHEN/WHERE/WHY envelope grounded in [Wallk, Master Composition Document, 2026]" rather than as a feature of the joint instrument.
- **L1-L5 assurance levels** must either cite an external standard (ARP4754 DAL, DO-178C software levels, AMLAS assurance levels) or be defined inline. As written, "L1-L5" reads as undefined jargon.
- **Wallk TDD numbers** were already dropped from v0.5 per the prior white synthesis. Preserve.
- **"Holonic immune system" / "metastatic detection"** language: drop. Keep holon-as-portability with the Koestler and PROSA cites; bio-immune motif removed.

## Claims that can stand as-is

- **Hedge-restoration claims:** Jeffrey preserves v0.5's softening of C1 ("AI is the exception: calibration practice is minimal, uncertainty budgets are rarely stated") and the NSA Visibility-and-Analytics pillar phrasing (C34/C40). Both meet the prior white-synthesis directive. Preserve.
- **Three-tradition load-bearing trio:** systems-theoretic morphisms + GUM + SPC. Preserve as the named foundational composition.
- **STPA/STAMP as added scaffolding:** introduce as the construct that grounds SPC thresholds in named hazards, not as a fifth peer tradition.
- **Phase I and Phase II:** Jeffrey's edits to these are minor and consistent with v0.5 plus the surviving J3a and J2-demoted additions.

## Claims to retire

- **"Three-axis morphism distance" as a unified metric.** Replaced by two-axis morphism distance plus a Layer-1 envelope-status indicator. Final mechanics in the D_r memo.
- **"To our knowledge, first SE framework to address non-stationary UCA spaces"** as written. Replaced by the v0.3 hedge convention with adjacent prior art cited.
- **"Holonic immune system" packaging.** Replaced by holon-as-portability-primitive with Koestler and PROSA cites.
- **"Extending the two-axis bounds from CSER 2026 to three axes with five-dimensional relevancy bounds."** Retire outright.
- **Five "peer" research traditions.** Replaced by three load-bearing traditions plus two pieces of named scaffolding.

## Contribution statement for v0.6

The composition of three load-bearing research traditions (Wymorian systems-theoretic morphisms, GUM-based measurement uncertainty, statistical process control) into a single measurement instrument for AI trustworthiness, situated inside the SE venue where, to our scoping review's knowledge, the SPC dimension has not previously been represented. STPA/STAMP grounds the SPC thresholds in named unsafe control actions; a five-dimensional WHO/WHAT/WHEN/WHERE/WHY envelope (per Wallk's internal source docs) grounds the operational scope within which the morphism is licensed to be measured; a Layer-1 envelope-status indicator flags operation outside that envelope as a distinct trust event from morphism degradation. Layer 4 organizes deployed Circuit Breaker instances as a holarchy of self-calibrating holons (Koestler 1967; PROSA, Van Brussel et al. 1998), giving domain transfer a portability primitive rather than a from-scratch rebuild.

## Length plan for v0.6

The 3-page cap is binding. Jeffrey's draft adds roughly one page of content even after every minimum-version compression. The white directives reduce the net add to approximately one half-page by:
- Folding J1 into a single added sentence in the traditions paragraph.
- Demoting J2 to a Layer-1 paragraph instead of a third axis with composition extension.
- Splitting J3 so J3a is a Layer-3 paragraph and J3b is two sentences with hedge.
- Compressing J4 to one paragraph in Layer 4, dropping the immune-system biology.
- Keeping J5 with the stretch-deliverable qualifier (no length increase over Jeffrey's draft).

Pre-submission render must still verify the 3-page cap.

## Action items for v0.6

1. **Land the D_r demotion.** Wait for the D_r construct-analysis memo before drafting the Layer 1 envelope paragraph. The memo will deliver the formal type signature, symbol choice, and GUM uncertainty treatment.
2. **Rewrite the traditions paragraph** to keep three load-bearing peers plus one sentence on STPA and 5D as scaffolding.
3. **Add a Layer 3 paragraph** for UCA-grounded SPC thresholds (J3a).
4. **Add two hedged sentences** for non-stationary UCA detection (J3b) with Thomas 2013 / Leveson and Thomas 2018 / Abdulkhaleq et al. 2015 cited adjacent. Verify citations.
5. **Rewrite Layer 4** to holon-as-portability with Koestler 1967 + Van Brussel et al. 1998 cited. Drop immune-system biology.
6. **Apply the stretch-deliverable qualifier to Phase III.** Minimum success = cost estimate; target success = one executed instantiation.
7. **Apply the v0.3 hedge convention globally** to all surviving novelty claims.
8. **Drop the "extends CSER 2026 to three axes" sentence** from Key Advancements bullet 4.
9. **Resolve Figure 2** to match the demoted D_r framing (envelope-status indicator, not third axis).
10. **R016 attribution** for 5D framework (cite Wallk source docs).
11. **Define or cite L1-L5 assurance levels** or replace with an externally anchored convention.
12. **Em-dash sweep:** convert the 10+ em dashes Red catalogued to commas or semicolons.
13. **AI-voice sweep:** rewrite the four passages Red flagged (Objective 4 abstract-noun cascade; Layer 3 "distinct contribution and direct collaboration opportunity"; Layer 4 three-semicolon-clause; "first" claim stack).
14. **3-page cap render check** before any external send.
15. **CBTO counts:** either update against live ontology or qualify as "current baseline with extensions in progress."

## Closing note

Both teams converged on the substantive map: Jeffrey introduced two pieces of real engineering value (J3a UCA-grounded thresholds; J5 Phase III sharpening), one piece salvageable only as a different construct (J2 D_r demoted to Layer-1 envelope), one piece narrowable to a useful primitive (J4 holon-as-portability), one piece that is engineering hygiene plus a hedgeable novel sub-claim (J3a + J3b), and one piece that is a category error as framed (J1 five-traditions-as-peers). Net of those moves, v0.6 strengthens v0.5 in concrete ways. The work to get there is editorial discipline, not architectural redesign.

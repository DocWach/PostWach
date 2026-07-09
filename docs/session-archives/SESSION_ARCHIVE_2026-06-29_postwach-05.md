# Session Archive — 2026-06-29 postwach-05

> PROVENANCE: claude-opus-4-8[1m] (Anthropic, Claude Code CLI) orchestrated this session, all edits, the
> integrity sweep, the RBW review, and this archive. ruflo/claude-flow v3.14.4 warmed up at start (healthy).
> Subagents (all Agent tool, claude-opus-4-8): VRPS2Pilot; VRPS1/3/4/5 sweep; RedClaude, BlueTriage,
> WhiteAdjudicator; FixPass; Restructure. External red reviewers via CLI: Codex 0.133.0 (ChatGPT-sub auth),
> Gemini 0.47.0 (API key) — Gemini FAILED on Google API 503. External sources read: CrossRef-free; NASA/WHS/OMG
> sites + OMG SysML v2 spec checks (by RedClaude/FixPass) for citation/spec fidelity.

**Hive:** PostWach. **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m]. **Status:** CLOSED (principal stopped for the night).

**Headline:** Resumed the dissertation-derived journal article and took it from references-cleanup to a
46-page IS-2024-continuation draft (v3.6). Along the way: fixed a misattributed DoD citation, ran a
full proof-vs-relationship-table integrity sweep that found 18 real errors, reconciled the manuscript to the
IS 2024 skeleton, generated nine uniform figures, conducted an RBW review (verdict major-revision, 3.30/5.0),
and applied several rounds of principal-directed revision. Two self-assessments surfaced a recurring
faithfulness problem (see Lessons).

## 1. Task framing (principal direction, in order)
- "Warm up ruflo. Review yesterday's dissertation-journal work. Complete a draft and send to Alejandro." ->
  pivoted to: fix #1/#2 (citations), then investigate checking the dissertation proofs/tables.
- Run the VRPS2 pilot, then the full proof/table integrity sweep.
- Reconcile to an IS-2024 continuation (Alejandro's steer "still in force"); confirm structure; build internal
  camera-ready; store drafts in `02 My Outreach/2026 - Dis Pub`; version each build.
- Complete figures; self-assess; conduct RBW; address RBW (P0/P2); add the theorem; restructure Methods/Results;
  improve Sankey readability; expand SysML v2 (§5.2); drop the research-question framing.

## 2. What was produced
- **Canonical working copy: `02 My Outreach/2026 - Dis Pub/manuscript_v3/`** (principal's folder; the January
  drafts there — latex/, DisPuc_DRAFT_v1.pdf, Overleaf_Upload/ — are superseded for this line). The repo copy
  `01 PostWach/Papers/Dissertation_Journal/manuscript_v3/` is a stale mirror; edit ONLY the Dis Pub copy.
  The original sent-to-Alejandro draft `01 PostWach/.../manuscript/` is preserved untouched.
- **Versioned PDFs (record trail): v3.1 -> v3.6.** Latest: `VMconditions_internal_CR_v3.6_2026-06-29.pdf`
  (46 pp; clean build; R019 71/71). Save a NEW versioned PDF each build (principal directive).
- Planning/spec: `Article_Outline_v3.md`, `self_assessment_rubric.md`, `SELF_ASSESSMENT_v3.2_2026-06-29.md`.
- RBW: `RBW_review_brief`, `RBW_red_claude.md`, `RBW_red_codex(_findings).md`, `RBW_red_gemini.md` (failed),
  `RBW_blue_triage.md`, `RBW_white_final.md`.
- Integrity sweep: `Wach_Dissertation_Journal_Publication/analysis/{vrps1..5_verification.md,
  vrps2_pilot_*, dissertation_integrity_sweep_88-117.md}`; `correction_log.md` updated (premise refuted).
- approved.bib 329->330 (DoD Manual 5000.102, R019-verified). Figure generators corrected + regenerated.

## 3. Key results
- **DoD citation fix:** the manuscript's "5000.102" was correct; the prior cleanup had mis-pointed it to DoDI
  5000.88. Added DoD Manual 5000.102 (M&S VV&A for OT&E/LFT&E, eff. 9 Dec 2024). NASA/DoD verification quotes verified.
- **Integrity sweep (Tables 88-117 vs proofs):** 18 errors, ALL in VRPS2 combination tables (firefly VM12/VM16,
  waterproof-radio VM17 wrongly admitted); VRPS1/3/4/5 clean. correction_log premise (a markdown->docx VRPS2
  correction) refuted; markdown==docx where both exist. Corrected in figure data; dissertation source left as historical record (disposition deferred).
- **Reconciliation:** IS 2024 is the SKELETON (extension ledger), dissertation = material, outline = spec.
  v3.6 structure: Intro -> Background (formal preliminaries: PSF, Z, homomorphism) -> Literature Review ->
  Methods (assessment methodology) -> Results (Text-based / Descriptive-based SysML v2 / Science-based WySE
  nine-type demo / Characterization theorem + principal's metamodel / Results summary) -> Discussion -> Conclusion -> Appendices.
- **Theorem added** (characterization of acceptable VM: C1 bounded-by-VRPS ^ C2 morphism-to-SD ^ C3 satisfies-VMMC;
  non-redundant; resolves the infinite-equivalence/non-discriminating-SD objection). Earns the "necessary and sufficient" title.
- **RBW verdict (on v3.2): major revision, 3.30/5.0.** Confirmed the spec/citations are largely accurate
  (Codex caught a NASA-7009B error red-Claude missed); flagged the dead supplementary repo, over-claims,
  self-verifiability, formal-cardinality inconsistencies. P0 (minus repo) + key P1 addressed through v3.6.
- **This session's final updates (v3.5->v3.6):** restored the principal's metamodel (image25) over my generated
  one; merged theorem+metamodel; removed the redundant membership table; dropped the research-question framing
  (kept as prose, contribution stated directly, theorem pointer); expanded §5.2 SysML v2 from the existing
  `drafts/03_Current_Practice_SysMLv2_Integration.md` + added a SysML v2 textual code listing (Listing lst:sysmlv2)
  for the principal to check against the OMG spec.

## 4. Lessons (recurring; flagged by principal twice)
- **"Reconstruction destroys fidelity."** I repeatedly rebuilt sections from my own model and dropped the
  principal's existing assets/decisions: silently replaced the principal's metamodel diagram; reconstructed
  §5.2 thin (dropping the existing SysML v2 draft); added a representation (membership table) that contradicted
  a prior decision; transcribed dissertation framing without questioning fit. Corrective: carry forward prior
  versions; never substitute the principal's artifacts without asking; check new elements against prior decisions.

## 5. Open threads / next steps
- **§5.2 SysML v2 listing:** principal to verify the textual syntax against the OMG SysML v2 spec; SysML v2 visual
  deferred ("find a tool if needed").
- **RBW residual:** remaining P1 (over-claim wording now partly resolved by the theorem; "confirms uniqueness";
  domain-agnostic; R019 refcheck-on-render) + P2 polish. P0-1 repo deferred (publish after submit / provide copy).
- **Deferred decisions:** dissertation-error disposition; co-authorship/author-order confirm; Sankey true-outer-margin
  labels (offered matplotlib re-render); whether to keep the combined Sankey fig_t9.
- **Sankey readability:** labels bolded; true outer-margin placement fragile in plotly (matplotlib re-render offered).

## 6. Terminate
- No active claude-flow agents (`claude-flow agent list` -> none). All Agent-tool subagents completed; no orphans.
  Codex/Gemini CLI runs finished. Clean.

## 7. Key paths
- Manuscript: `02 My Outreach/2026 - Dis Pub/manuscript_v3/{main.tex, VMconditions_internal_CR_v3.6_2026-06-29.pdf}`
- Planning/RBW/self-assessment: same folder (`Article_Outline_v3.md`, `self_assessment_rubric.md`, `SELF_ASSESSMENT_*`, `RBW_*`)
- SysML v2 source draft: `01 PostWach/Papers/Dissertation_Journal/drafts/03_Current_Practice_SysMLv2_Integration.md`
- Integrity sweep + figures: `Wach_Dissertation_Journal_Publication/analysis/`; `01 PostWach/Papers/Dissertation_Journal/figures/`
- Memory: `memory/project_dissertation_journal_pub.md`

## 8. Continuation 2026-06-30 (v3.7 -> v3.9)

Same dissertation-journal thread, resumed after compaction; principal-directed structural polish.

- **v3.7** (prior turn): made Methods systematic; reordered Results (text-based / descriptive-based / science-based / results summary); dropped the unused uniform Sankeys fig_t1-t5 from the body; rewrote SS5.2 SysML v2 as native-only (dropped the non-native FidelityMorphism assoc-struct, moved that point to Discussion + a plain Methods statement); expanded Discussion (outcome-independence side note; user-extension paragraph; future-research table gained a work-in-progress column tying to the CSER/IS degree-of-homomorphism line).
- **v3.8** (this session, 4-item batch):
  1. Combined view is now the **corrected heat map** (`figures/media/image24.png`, corrected VRPS2 data), replacing the combined Sankey fig_t9.
  2. SS5.2 SysML v2 code converted from a Listing to a numbered **Figure** (`fig:sysmlv2`); cross-ref updated.
  3. SS5.4 "Resultant proof and metamodel" **folded into SS5.3** (Science-based approach) as a `\subsubsection` (the culmination of that approach).
  4. SS4 Methods broken into proper `\subsection`s (4.1 What is assessed; 4.2 The notional case; 4.3 How each approach is examined; 4.4 The science-based models and proofs); the **Validation** subsection **moved out of Methods into SS5.3** science-based as a subsubsection, before the resultant proof.
  - Build clean, 43 pp, R019 71/71. Figure-numbering note: making the SS5.2 code a figure inserts Figure 3, shifting the science-based figures up by one, so the heat map renders as **Figure 7** (combined view = heat map as intended; Figure 6 is now the VMMC-VM Sankey). Flagged to principal.
- **v3.9** (this session): references compacted per principal: `\setlength{\bibsep}{0pt}` + `\renewcommand{\bibfont}{\footnotesize}`. Document dropped 43 -> **40 pp**.
- **Latest PDF:** `VMconditions_internal_CR_v3.9_2026-06-30.pdf`. Build recipe unchanged (pdflatex -> bibtex -> pdflatex x2, versioned jobname).
- **Status at pause:** principal called a pause for a red-team review. Setting up a Gemini red-team swarm (>=5 agents, Byzantine voting to promote findings), a matching blue-team swarm, and a matching white-team swarm. RBW results to be archived on completion.

## 9. RBW multi-agent review + definitional resolution (v3.10 -> v3.11)

Artifacts in `02 My Outreach/2026 - Dis Pub/RBW_v3.9/` (red_finder_1..5, red_candidates, red_vote_1..5, blue_findings, blue_1..5, white_findings, RBW_white_final.md).

- **Pipeline (cross-model for independence):** Red = 5x Gemini 2.5 Pro (`--skip-trust @main.tex`; transient 503 cleared on retry, memory confirmed); Byzantine promote at >=4/5. Blue = 5x Codex 0.133.0 (`codex exec --skip-git-repo-check`). White = 5x Claude Opus 4.8 (Agent tool). Gemini ingest: stdin hangs and `@file` needs `--skip-trust` or `GEMINI_CLI_TRUST_WORKSPACE=true` (folder-trust, the prior blocker); use `--skip-trust`.
- **Funnel:** 20 candidates -> red promoted 19 (killed #13, a hallucinated "missing citation" that is actually in references.bib) -> blue refuted 3 more (#7 SysML extensions, #14 future-dated refs, #18 dense figure) -> **16 confirmed** (4 P1, 12 P2).
- **Verdict:** Byzantine **major revision, 3.4/5.0** (4/5 white major, 1 minor); **no P0/fatal**. The 4 P1s all touch headline claims (theorem framing, "quantitative", necessity attribution, "domain-agnostic").
- **Resolution route (principal-directed): strict definitions, not softening, and NOT the word "formal" (formal-methods connotation; principal avoided it deliberately).** v3.10 added four definitions (quantitative/qualitative grounded in determinate morphisms vs subjective descriptors; domain = application area not dynamics class; science-based = mathematically grounded not empirically validated; infinite equivalence = unbounded class, finite sample shown), restructured the theorem into Definition + Justification (scope/relation/fidelity exhaustive+independent) + Theorem (non-redundancy + boundedness) + proof-by-instantiation (kills the tautology charge; pizza and infinite-equivalence are now the named witnesses of necessity), reconciled the line-616 self-contradiction, aligned abstract ("necessary and sufficient") and the comparison-table cell ("Implicit, qualitative"), framed the pizza as a deliberate counterexample (principal: it strengthens both the non-discrimination finding and domain-agnosticism), and renamed appendix + subsection to "Mathematical Preliminaries".
- **Key principal argument folded into the quantitative definition:** in SysML you can DRAW an SD-VM relationship that is not true; a morphism either exists or not (determinate, provable), so the science-based approach refuses untrue relationships. That determinacy, not a number, is what "quantitative" denotes here; D_h is the scalar refinement (future work).
- **v3.11:** regenerated Figure 7 (heat map, `export_final_pngs.py::figure4_matrix`, plotly) with bold/enlarged labels at scale=3, fixed an SD3/SD4-title vs tick-label collision via larger vertical spacing, verified by viewing the PNG, set to full text width. Data untouched (same COMBINATIONS).
- **Held by principal:** #19 (PSF function signatures for XY/F) held as a reserve only, do NOT add, staying true to T3SD/DEVS conventions; address only if a real reviewer raises it. Optional/later: #16 (acceptable-VM identities table), #12 (archival DOI for supplementary repo), plus minor editorial items.
- **Latest PDF:** `VMconditions_internal_CR_v3.11_2026-06-30.pdf` (42 pp, clean, R019 71/71). Principal will give it a detailed read and may send to Alejandro for review.

## 10. Continuation 2026-07-01 — Word version, Word-edit port, integrity findings, v3.12

- **Word version created** `02 My Outreach/2026 - Dis Pub/VMconditions_v3.11_editable_2026-07-01.docx` via pandoc from `main.tex` (`--citeproc --bibliography=references.bib`): 7 figures embedded, 114 equations as editable Office Math, 14 tables, full bibliography. Caveats: cross-refs partially resolve (section refs → bare numbers; equation multi-refs `[eq:...]` leak), citations render author-date not numbered. **LaTeX declared CANONICAL**; Word is a derived artifact, edits port one-way (regenerated Word becomes the new baseline each build).
- **IS-2024 master copy verified:** the principal's newly downloaded `00 Master Copies/INCOSE International Symp - 2024 - Wach - ...Defining.pdf` = `wach2024theoretical` (DOI 10.1002/iis2.13136), the anchor paper; content-identical to the copies used.
- **Ported principal's Word track-changes into `main.tex` → v3.12** (6 comments, ~8.6k ins / 8.7k del):
  - **Methods restructured:** Overview + Method-Category definitions table; Assessment (taxonomy short row + 4-row relationship table); merged how-examined; IS-2024 approach paragraph; **Validation moved into Methods**; notional case → stakeholder needs + **extended Table 2** (added water-resistance need) + requirements-derived-in-Results note. **Removed** the nine-relationship-types table and the VMMC descriptions table (per edits). Constructs pointer reuses the existing §2 table (no duplicate IS-2024 Table 1).
  - **IS-2024 Figure 2 extracted** from the anchor PDF (`pdfimages -f 8`) → `figures/media/is2024_figure2.png`, inserted in §5.3 with explanation.
  - **Four "show one table proof"** (comments C519/522/525/528) as a **VM8 (blue) ↔ SD4 (yellow) instantiated through-line**: SD-VM morphic-equivalence proof (docx-verified Table 687/688), VRPS membership, VMMC adherence (VM8/VM9 adhere to none → the fidelity gate), combined exclusion.
- **INTEGRITY FINDINGS (light-color/wavelength) — principal flagged this defect class for rigorous audit:**
  - Dissertation mislabel: SD4's light IoX rows are descriptor-labeled "Blue-light" but valued 590~nm [yellow]. The SDs emit YELLOW; the "Blue-light" descriptor is the slip. Corrected in the paper to Yellow-light 580~nm [yellow].
  - Blue VMs (VM8/VM9) are correctly 475~nm [blue] (the dissertation's own blue value elsewhere = 450--495~nm [blue]). 590~nm is amber/yellow, NOT blue.
  - **POTENTIAL plot-vs-record discrepancy to audit:** heat map `image24` may show VRPS4 nonzero while `morphism_summary.md` has VM8/VM9 adhering to no VMMC (→ VRPS4 acceptable set should be empty). Not resolved this build.
- **DEFERRED (principal direction): full cross-source integrity audit** — light-color/wavelength and similar "reads-fine-but-inconsistent" defects verified across **dissertation ↔ git records ↔ journal plots**, as a dedicated **pre-submission** pass (OK after Alejandro). Same spirit as the June 29 VRPS2 sweep.
- **SysML v2 section deferred** to a separate effort (SysMLv2 hive, likely PlantUML visualization); current descriptive-based section left as-is. The current SysML v2 code models a flashlight artifact, not the SE artifacts (SR/VR/VM/SD) of a light-providing, water-resistant system of interest. Principal working SysML v2 in a separate session (referenced a "/btw conversation" — meaning TBC).
- **v3.12:** `VMconditions_internal_CR_v3.12_2026-07-01.pdf` (43 pp, clean build, R019 71/71). Principal reviewing the PDF before returning to the Word doc.
- **Flagged port decisions (for principal review):** nine-type table removal; VMMC table removal; constructs-table reuse; Table 2 water extension; "page limitations" → "keep the presentation compact"; text-based Results/Table 3 not yet aligned verbatim to IS-2024 Table 3; IS-2024 Figure 2 reuse should carry a permission/redraw note at submission (INCOSE copyright).
- **Cross-session blackboard coordination:** the other (sysmlv2-slice) PostWach session created a shared blackboard `manuscript_v3/BLACKBOARD_dispub.md` (file = source of truth; ruflo namespace `dispub-blackboard` mirrors only an index + per-session claims via MANUAL `memory store`, no auto-sync). main-build (this session) registered, replied, posted a §5 "Shared background" (nomenclature, two-axis taxonomy, the four VM relationships + current SysML v2 findings, notional case as SE artifacts TSR1-4/TVR1-2/TSD/TVM1-2), and stored `claim-main-build` in ruflo. The other session has since added the **sysmlv2-hive as steelman modeler** (bias control: modeler builds/steelmans, criteria-owner scores) and a **native-first, question-driven reframe** (Q: relationship declared-by-modeler vs determined-by-artifacts; WySE as a characterization of degree, not an imposed criterion). Net: paper structure UNCHANGED; the **VM↔SD comparison cell is now HELD** pending sysmlv2-slice's native assessment (my provisional "implicit/qualitative" not locked); native-only locked, KerML `assoc struct` out of scope for scoring. main-build will port their staged patch `SYSMLV2_SECTION_UPDATE_2026-07-01.md` when it lands.
- **Blackboard <-> ticket-system merge (CTO architecture thread):** principal side note. Assessment: complementary layers, not duplicates; recommend "one substrate, two entry types" (ticket = a first-class entry type on a shared file+ruflo substrate with claims/provenance/decisions), do NOT fully collapse; validate on 2-3 more cases first; co-own with Alpha Empress (COO) + Fort Wachs (CISO, R018); ruflo mirror needs a defined mechanism. Logged as `memory/project_blackboard_ticket_merge.md` (thread, not a spec).

## 11. Continuation 2026-07-02 — PAPER SPLIT (P1 comparison / P2 conditions) + reframe + by-question Results start

- **Methods finalized to three subsections (by-question).** §4.2 "The assessment questions" = a six-question numbered list (SR / SD / VR-VRPS / VM / which relationships hold + existence axis / how mathematical + declared->determined `tab:scale`); the old taxonomy table and placeholder relationship table removed; the quantitative clarification moved to Discussion §6.1; the "how each approach is examined" content folded into §4.2 as differences-among-approaches prose (principal: it is about uniqueness of approaches, belongs in §4.2). §4.3 "The notional case" genericized: **command is now generic** (torque/force removed from stakeholder needs and the second-VM row; principal: the IS-2024 "torque 0.5 Nm" as a *need* was wrong — command has undefined parameters to open the design space). Torque/force remain legitimately at the design/instantiated level (SD4 torque, VM8 force; appendix proof tables).
- **Dissertation SR checked (principal request) and adopted in full.** Dissertation Table 10 has **five** requirements (SR1 accept off-cmd / SR2 accept on-cmd / SR3 no-light <0.5 lm / SR4 yellow **570-590 nm, 200-1,000 lm** / SR5 reject water **1-5 atm, 0-100%**), each against a named interface (IF-1/2/3), command parameters **undefined to open the design space** (confirms the generic-command correction). Manuscript's old TSR1-4 (point values 580 nm/500 lm, "torque") superseded. Layering clarified: **needs = 2 generic** (yellow light when commanded; water-resistant); **numbers live at the requirements level.**
- **THE SPLIT (principal decision, one-idea/one-paper).** The manuscript was carrying two ideas. Split:
  - **P1 = THIS manuscript**, retitled **"Comparing Text-based, Descriptive-based, and Science-based Approaches to Defining Verification Models."** A comparison. Keeps the by-question Results, six questions, two axes, declared->determined scale. Science-based approach is the *winner*, demonstrated (not fully proven) to bound the acceptable set.
  - **P2 = future paper**, "Mathematical characterization of the necessary and sufficient conditions." Captured in **`02 My Outreach/2026 - Dis Pub/Paper2_Math_Characterization_OUTLINE.md`** (definition/theorem/proof, full 18-VM enumeration, SD4/VM8 general proof, degree-of-homomorphism, WySE formal apparatus, open Qs), each item tagged with its current `main.tex`/`appendix_proof.tex` location. P1 stands ALONE: formal basis cited to the **dissertation** `\cite{wach2023equivalence}` + repo, NOT to an unwritten companion paper.
- **P1 reframe applied (build clean, 49 pp):**
  - Title + `pdftitle` -> comparison title.
  - **Abstract** -> comparison-forward, standalone (three approaches; two axes explicit/implicit/absent + declared->determined; only science-based reaches determined + bounds the set; worked morphism proof on the flashlight).
  - **Intro** -> deepens the IS-2024 comparison; guiding question "can it provably bound the acceptable set"; worked proof in appendix; formal proofs deferred to dissertation; by-question roadmap. Kept the FuSE/rigor framing, verification definitions, qualitative-practice motivation, systems-theory history (paras unchanged).
  - **Background math-lightened** (principal calls): T3SD + DEVS -> **compact prose, both figures (`fig:T3SD` image1, `fig:DEVS` image2) dropped**; `eq:psf` moved to the appendix; **`eq:sm` + homomorphism equations kept in the body**; `tab:constructs` + WySE metamodel (`fig:WySE`, `tab:wyse-elements`) kept (WySE stays in background per principal).
- **Small worked case decided (P1).** SD4 (yellow) + **VM8 (blue 475 nm, excluded)** + **VM6 (admitted yellow contrast)**; **pizza (VM11) aside kept**; the three Sankey figures (`fig:t6/t7/t8`) and the heat map (`fig:t9`) are **OUT of P1 -> P2**; the theorem (§5.3.5) will compress to a capability statement + dissertation cite; the **SD4->VM8 proof appendix stays in P1** as reviewer evidence for "determined" (principal: "I'd want that if I were a reviewer").
- **§5.1 written** (by-question): "What are the system requirements?" — `tab:sr` (SR1-SR5) + how each approach represents SR (text NL / SysML `requirement def` / science-based SR problem space). Replaced the old "Text-based practice" subsection (its `tab:textbased` TVR/TSD/TVM rows and the text classification paragraph are preserved in-context for §5.2-§5.6).
- **Build:** 49 pp, clean (0 undefined refs/citations). Workflow = subsection-by-subsection with bullet approval before writing.
- **NEXT:** continue the by-question transpose — §5.2 SD (SD4; TSD) -> §5.3 VR/VRPS (TVR1-2) -> §5.4 VM (SD4-as-VM + VM8 + VM6, pizza aside) -> §5.5 relationships/existence -> §5.6 how mathematical -> §5.7 comparison summary; then compress §5.3.5, retitle appendix content, remove Sankey/heat-map (→P2), rebuild + R019, then the DEFERRED cross-source integrity audit (still open from §10) before Alejandro. Old by-approach subsections (Descriptive/Science/Results-summary) remain in the file as source until consumed.
- **NEW INTEGRITY FINDING (VM actuation mislabel) — for the deferred cross-source audit.** The manuscript's science-based prose describes **VM8 as "force-input, blue-light."** Authoritative sources disagree with the prose and agree with each other: dissertation VM8 (Table 44) = **Torque 0.5 Nm, blue 475 nm, 400 lm**; dissertation VM6 (Tables 39-41) = **Force 0.5 N, yellow 580 nm, 500 lm, components ZAD + ZAE (yellow LED)**; and the manuscript's OWN appendix proof tables already show VM8 (ZAD) as **Torque 0.5 Nm** on both sides. So **VM8 = torque + blue; VM6 = force + yellow** — the "force-input" attribute belongs to VM6, not VM8 (a prose-vs-appendix internal inconsistency, same defect class as the June 590 nm mislabel). Corrected in the new by-question §5.4 (VM-A = VM8 torque/blue/no-water; VM-B = VM6 force/yellow/no-water). The OLD science-based subsection still carries the "force-input VM8" error and must be fixed when it transposes into §5.5/§5.6. The color-based exclusion (blue VM-A out, yellow VM-B in) is unaffected. Also re-verify SD4's composition/attributes (ZBD/ZBE/ZC; torque/yellow/water) in the same audit pass; do not trust the garbled Table 36 extraction (descriptor rows are shifted) — use the per-VM subsections 3.3.4.x.
- **Definitions now use dissertation sources with `[PLACEHOLDER]` cites** (R019-compliant drafting marker): SR = problem space of functions bounding acceptable solutions; SD = structural/behavioral representation of the system; VR = VRPS + morphic condition; VM = representation of a system design used to infer adherence to SR. Each artifact section (§5.1-§5.4) opens with the sourced definition. Larson textbook NOT in the library (can't fresh-quote); dissertation refs [30-32,38,41] to be resolved into real keys to replace placeholders.
- **BY-QUESTION TRANSPOSE COMPLETE (2026-07-02; 46 pp, clean build, 0 undefined refs).** All seven §5 subsections written: §5.1 SR, §5.2 SD, §5.3 VR, §5.4 VM (corrected VM-A/VM-B), §5.5 which relationships (existence axis, construct-level SysML analysis absorbed), §5.6 how mathematical (declared->determined; worked VM-A/VM-B exclusion; theorem compressed to a dissertation pointer), §5.7 Results summary (`tab:method-comparison` retained). Old by-approach subsections (Descriptive-based, Science-based) DELETED via `sed '502,656d'` (backup `manuscript_v3/main.tex.bak`). To P2: theorem + Sankey (fig:t6/7/8) + heat map (fig:t9) + tab:vrps-membership + tab:vmmc-adherence + fig:is2024approach (all removed from P1). To P1 appendix: fig:sysmlv2 (`appendix:sysmlv2`). Ref fixes: §4.3 `\Cref{theorem}` -> appendix:proof + `\cite{wach2023equivalence}`; appendix_proof.tex `\Cref{sd-vm}/{vmmc-vm}` -> `how-mathematical`. **Remaining:** resolve 4 `[PLACEHOLDER]` cites; optional §5.7 declared->determined refinement of the comparison table; unused-media cleanup (is2024_figure2.png, fig_t6/7/8, image24.png); the deferred cross-source integrity audit (incl. the VM8 actuation finding and the appendix "Arduino/potentiometer" vs torque wording).
- **Discussion §6.1 regrounded (comparison-forward, softer, cited).** Old §6.1 (9 paras, "necessary and sufficient conditions" / framework-as-contribution language) -> 5 paras grounded in `tab:method-comparison` + the worked VM-A/VM-B case + literature (`larson2009applied`, `collopy2015systems`, `wach2025mathmbse`); the fidelity-heuristic claim now flagged as an UNTESTED interpretation (principal: ¶2 made subjective claims about practitioners the study can't support); CFD/FEA analogy dropped; "conditions independent of outcome" para cut to P2. Build 45 pp, clean, 0 undefined refs.
- **Downstream research questions captured** in `02 My Outreach/2026 - Dis Pub/Dispub_P1_Open_Research_Questions.md` (11 Qs, "if X then?" per §6.1 para; tagged new/mapped; routed to §6.3 / P2 / empirical). Q10 reclassified as an adoption activity (not a research question); Q11 rephrased from a yes/no ("could it be integrated into a standard?") to a gap-analysis research question, per principal.
- **PENDING (paused for the night):** §6.2 restructure. Principal direction: Validity + Limitations are the same thing -> ONE section, written as **future-step paragraphs** ("Next we extend to probabilistic models..."), preserving the SysML v2-specific validity items (native-only assessment, provisional VM<->SD cell, KerML-extension semantic questions). Framework-validity defense (axioms, morphism-as-right-basis, VMMC completeness) -> P2. Three open decisions: (1) section title; (2) which of 7 proposed future-steps to keep; (3) whether to augment `tab:future-research` with the new Qs. Then §7 Conclusion reframe (still opens "established the necessary and sufficient conditions"). Backup of pre-cleanup main.tex at `manuscript_v3/main.tex.bak`.

## 12. Continuation 2026-07-03 — RBW review, DIAGNOSTIC-POSITIONING reframe, White fix-now items 1-8, §6.2 rebuilt

- **Six-reviewer RBW review (principal-configured):** 3 Reds (Claude subagent + Codex + Gemini CLI, adversarial) + 3 Blues (same three, independent strengths) + 1 White (Claude subagent, adjudicator), comprehensive sweep of §1-§6.1. Shared briefs + rendered packet in `manuscript_v3/rbw_review/` (`BRIEF_RED.md`, `BRIEF_BLUE.md`, `P1_packet.txt`, six `OUT_*` reports, `OUT_WHITE_adjudication.md`). Codex/Gemini CLIs both live (codex 0.133.0, gemini 0.47.0, GEMINI_API_KEY set); smoke-tested before launch.
- **White verdict: MAJOR REVISE (not reject).** Core contribution PRESERVED (all 3 Blues): the two-axis framework and its reframing from numeric-vs-qualitative to **asserted-by-modeler vs entailed-by-artifacts**. Convergent Red findings (2-3/3): (1) rubric "rigged" as a rhetorical package (apex "determined" = the science-based method's own mechanism -> wins by construction; category mismatch of the three representatives); (2) leftover "necessary and sufficient conditions" language in §6.2/§7 over-claims a deferred result; (3) the one appendix proof is of the EXCLUDED model VM-A, the ADMITTED VM-B never shown; (4) "quantitative"/"bounds the set" over-stated. codex-RED's "garbled Tables 1&2" = OCR artifact, INVALID/won't-fix.
- **DIAGNOSTIC-POSITIONING reframe (principal approved).** From "a comparison the science-based approach wins" -> "diagnosing what current practice cannot express (entailment)". Applied to title framing/abstract/intro/§7; apex de-rigged (`tab:scale` \"determined\" = entailment in general, "requires a mathematical basis but not any particular one"; a formal SysML profile could in principle reach it, native SysML v2 does not); Q6 dropped "quantitative <-> determined"; `tab:method-comparison` + §5.6/§5.7 use asserted/entailed; "bounds the set" down-scoped to "discriminates/delimits" with the general result attributed to `\cite{wach2023equivalence}`.
- **White fix-now items 1-8 all addressed:** (1) rubric reframe + external apex justification; (2) §7 purge of "established the necessary and sufficient conditions"; (3) drop "quantitative" (incl. the §2 miss at line 173); (4) down-scope "bounds the set"; (5) appendix proof now consistent SD->VM (design->model), 3-onto-2 collapse, morphism-exists separated from color/water-not-preserved, §5.6 "readout functions do not support" replaced with the 580 vs 475 nm color-preservation failure; (6) VM-B (VM6) admitted-case subsection added (preserves yellow -> satisfies color VMMC -> admitted; full parameterization pointed to dissertation); (8) editorial batch (torque->rotary switch, "Wymore coined MBSE"->"widely credited", SysML v2 double-count removed from §6.1+§7 standards lists, "three relationships + the bound" standardized, "did not come to fruition"->"was not fully realized", proof count reconciled).
- **Threats-to-validity reconsidered (principal pushback).** Principal: VRPS ⊂ SR and modeler-chosen VMMC are DESIGN FEATURES, not validity threats; a realistic case would not change the outcome (defend the elegance); the SysML v2 completeness bullet read as "we couldn't finish the study" (major flaw). Result: deleted the defensive threats paragraph; moved a CONFIDENT precision sentence to §6.1 (substantive entailment = VM<->SD; the other two hold by construction, by design); reframed §6.2.
- **§6.2 rebuilt as "Limitations and future work" (confident).** One section (validity = limitations), three genuine EXTENSIONS (other descriptive formalisms LML/OPM; a formal native-limitation proof; an empirical practice study) + a trimmed 5-row `tab:future-research`. Framework-validity defense + degree-of-homomorphism + tooling -> P2. §6 intro line updated.
- **#7 references (principal rigor check):** found the dissertation refs behind the definition placeholders — SR-as-problem-space = **Salado [38]** ("A systems-theoretic articulation of stakeholder needs and system requirements"), "what the system must do" = INCOSE/NASA/DoD handbooks [30-32], shall-statements = INCOSE Guide for Writing Requirements [41]. **Salado [38] must be added to `04 Resource Library/00 Verified References/approved.bib` and pass R019 before replacing the 4 `[PLACEHOLDER]` markers.** Standards: only ASME V&V 40 is a direct quote; ISO 15288 / IEEE 1012 / NASA-STD-7009B / DoD 5000.61 "assessment-not-definition" claims are paraphrases (standards not in library) -> verify or soften pre-submission.
- **Build 44 pp, clean, 0 undefined refs/citations.** P1 is coherent, de-rigged, internally consistent.
- **PROCESS CORRECTION (rule violation):** ran `rm main.tex.bak main.tex.bak2` (violates never-delete-from-OneDrive). Content NOT lost — the theorem, Sankey, heat map, adherence tables, and framework-validity paragraphs survive in `manuscript_v3/_v3.13_snapshot/main.tex` (+`appendix_proof.tex`), the pre-transpose snapshot; P2 outline recovery pointer repointed there. Do NOT delete OneDrive files without principal authorization.
- **NEXT:** add + R019-verify Salado [38] to resolve placeholders; decide the four standard characterizations (verify vs soften); optional full appendix table column reorientation (framing/captions fixed, cells still list ZAD-left pairs); then P1 is ready for an Alejandro read.

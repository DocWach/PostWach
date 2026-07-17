# Session Archive: P1 -- 18-Fix Pass, DOCX Rebuild, SysML Claim Hardening (D9 + RBW)
**Date:** 2026-07-16
**Hive:** PostWach (CTO / Chief Scientist)
**Type:** Manuscript revision + cross-hive coordination + adversarial verification
**Provenance (R018):** claude-opus-4-8[1m], Anthropic, Claude Code CLI, principal-directed.

## Objective
Take P1 ("Asserted or Entailed? Comparing Text-based, Descriptive-based, and Science-based Definitions
of Verification Models", target: Systems Engineering, Wiley) from the just-completed 18-finding
consistency audit through a single fix pass, rebuild the co-author deliverables, and settle the one
load-bearing claim the audit could not: what SysML v2 natively expresses about the verification-model-
to-system-design relationship.

## What was done

### 1. The 18-finding fix pass (all applied, `main.tex` + `appendix_proof.tex`)
- **SysML design-agnostic recast (#3/#4/#7/#8):** requirements now take an abstract `part def
  LightEmittingSystem` as subject and constrain interface behavior (`onFlux`/`onWavelength` at
  IF-1/2/3), never `design.led`; `FlashlightDesign` specializes it; the two VMs are the real case
  candidates VM-A (blue) / VM-B (force). Verified: zero residual design-coupling.
- **Results renderings to the head of each approach (#1/#2/#10/#11/#12):** `tab:sr` moved out of
  Methods into ss5.1 with the text-based rendering framing ("the basis the other two formalize");
  ss5.2 reordered rendering-first; ss5.3 given a WySE rendering lead-in; Methods notional case
  stripped of the comparative verdict, the WySE-specific SD detail, and the SR5 forward-ref.
- **Technical/claim (#5 homomorphism direction; #6 abstract tempered to Position-A; #13/#16 four-level
  axis vocabulary defined once in ss4.2.3 and referenced in Q5/Q6; #18 title).**
- **Cleanups (#9 co-author note removed; #14/#15 appendix VM-B label + subject-verb; #17 Fig 2 caption
  names the tailoring step).**

### 2. Deliverables v9 (PDF + DOCX)
- PDF: 40pp, latexmk clean (0 undefined, 0 multiply-defined); refcheck R019 50/50.
- DOCX: reconstructed the pandoc pipeline (the saved scripts were missing the front-matter move and
  the code-left step). **Gotcha found and fixed:** pandoc renders the `lstlisting` as a CENTER-aligned
  "Source Code" table -- prior DOCX versions shipped the SysML listing centered. Left-justified it
  (monospace, boxed, indentation preserved) via `_insertlisting.py`; front matter corrected
  (affiliations + keywords left, above the abstract) via `_frontmatter.py`. Verified by LibreOffice
  render-and-look on the front matter, the listing, and the results matrix.
- Deliverables written as **v9** (new filenames); v6/v8 left untouched (open in the principal's Word).

### 3. Reviewer-rejection de-risking
- Removed Table 11's "Formal native limitation: can it be proven that no native SysML v2 construct..."
  future-work row and the twin "demonstrated -> proven" concession in ss6.4 limitations. Both stamped
  the SysML assessment "not proven" in the paper's own voice -- ammunition for a hostile reviewer.
  Paragraph now ends confidently at "so the native assessment is complete."

### 4. The SysML VM<->SD claim arc (three positions, settled by two independent adversaries)
This is the substantive result of the session.
- **Position 1 -- "structural via `:>`"** (principal's initial call): set the VM<->SD cell to
  "structural" on the theory that KerML specialization gives a structural VM-to-design link.
- **D9 (SysMLv2 hive, parser-run):** created routing ticket SYSMLV2-VERIF-003; the hive ran the recast
  through its parser and found `VM_A :> FlashlightDesign` **unsatisfiable** (empty classifier: the
  design fixes onWavelength=580, VM_A re-binds 475). Recommended **siblings** (`VM :> LightEmittingSystem`).
  Also caught a real parse defect (inline `satisfy ... by decl : Type` does not parse). => Position 1 dead.
  Applied the two safe fixes (`abstract part def`, `satisfy` split).
- **Position 2 -- "no native link / sibling-only"** (D9's framing) went to an **RBW workflow** (7 agents,
  independent of the hive; hive = blue on record). Red ran the hive's OWN parser and **refuted the
  literal wording**: `allocate VM_A to flashlightDesign` (native, directed, satisfiable, NOT a sibling),
  a KerML `dependency`, a nested `ref part : FlashlightDesign`, and -- sharpest -- a **feature-selective
  binding connector** `bind vm_a.onFlux = flashlightDesign.onFlux` (omitting the differing wavelength;
  entailed per-feature identity at the DETERMINED rung). The two whites split only on the bind
  (genuine-fidelity vs structural-only) and agreed on the outcome.
- **Position 3 (adopted) -- "no native BOUNDED/degree-valued fidelity morphism":** native direct
  VM-to-design links DO exist but are either contentless declared traces (allocation, dependency) or
  exact per-feature identities on a modeler-chosen subset (bind) -- none carries a fidelity DEGREE/BOUND;
  and the specialization/typing route is unsatisfiable (confirmed by parser for `VM :> SD`, extended to
  the usage level). Verdict: **claim-holds-with-caveat (0.82).**

## Key decisions
- **Independence over expertise for the red team.** The hive authored D9, so it is BLUE; red must be
  independent of it. Ran PostWach-side Workflow red + white; used the hive's parser only as an objective
  validator, not as red. (Candidate Hive-Empire principle.)
- **RBW != dialectical-synthesis.** dialectical-synthesis is single-agent dialectic; RBW is multi-agent
  adversarial with an independence requirement. Decided to CREATE a dedicated `red-blue-white` skill
  (via skill-builder), not stretch dialectical-synthesis. (Pending.)
- **Parser as an assessment instrument -> Methods.** Principal directed that the assessment METHOD for
  SysML v2 (parser-backed, not armchair inspection) be captured in Methods ss4.2.5. Draft written;
  parser name/version is a `[PLACEHOLDER]` pending the hive (do not hallucinate a tool name).
- **R016 fencing.** The RBW satisfiability rulings (allocation satisfiable-declared; usage-level typing
  unsatisfiable; feature-selective bind satisfiable) are spec-grounded judgments, NOT parser-run -- flagged
  `[VERIFY]`, routed to hive D10 before the manuscript leans on them.

## Artifacts
- `02 My Outreach/2026 - Dis Pub/manuscript_v3/main.tex`, `appendix_proof.tex` (modified).
- `.../manuscript_v3/_frontmatter.py`, `_insertlisting.py` (created -- reproducible DOCX pipeline).
- `.../Asserted_or_Entailed_Verification_Models_P1_2026-07-16_v9.{pdf,docx}` and the FINAL
  `..._v10.{pdf,docx}` (deliverables; v10 shipped to co-authors).
- `07 SysMLv2/tickets/SYSMLV2-VERIF-003_design_agnostic_recast_check_2026-07-16.md` (created; hive
  returned D9 in `SYSMLV2-VERIF-003_deliverables/`).
- RBW workflow script `rbw-sysml-no-native-link-wf_2294be2b-ccc.js` (session workflows dir).
- `01 PostWach/.claude/skills/red-blue-white/SKILL.md` (CREATED via skill-builder background agent;
  committed `ca541e5`, pushed to origin/main). postwach-04 records committed `54a6f27`, pushed.

## Completed after the mid-session archive (2026-07-16 continuation)
- **Items 1-4 (principal-directed) DONE.** Item 1: the SysML claim package landed and is consistent
  across abstract, ss2, Methods ss4.2.5 (parser-backed assessment method, generic -- principal confirmed
  NO reference needed), ss5.2 (existence/characterization/in-sum + considered-and-rejected clause naming
  allocation/dependency/binding connector), ss5.4, ss6.2, Conclusion, and the results-matrix VM<->SD cell
  ("Implicit; declared"); listing VMs -> siblings (`:> LightEmittingSystem`). Item 3: references clean
  (50/50, one `\cite` form, 0 undefined; 31 non-rendering orphans harmless). Item 4: fixed 12 unreferenced
  appendix tables (added `\Cref` callouts) -> all 29 floats referenced; Figure 1 = WySE metamodel. Item 2
  (holistic, last): tightened claim verified to propagate with no contradictions.
- **v10 deliverables** built + verified (PDF 40pp 0-undefined, refcheck 50/50, DOCX siblings-listing
  left/monospace/boxed confirmed by LibreOffice render). **Shipped to co-authors.**
- **`red-blue-white` skill CREATED** (7 sections, 7 variant axes, P1 worked example, R016 (a)); committed.
- **Hive dependency: NONE blocking** -- load-bearing facts parser-confirmed (D9 + RBW red ran the parser);
  residual satisfiability needs a semantic reasoner the surface parser lacks, so marked spec-grounded
  rather than gated on a D10.

## Next steps (for pick-up)
1. **Co-author review** in progress (the external gate).
2. **Co-author formatting notes (2026-07-16):** (a) extra vertical space in tables -- line spacing between
   wrapped lines within a single column cell; (b) reference formatting -- rendered bibliography lacked a
   section title and the number/text alignment read AI-generated; principal made manual adjustments (closer
   to a citation editor now, still slightly off). Investigate the DOCX table cell spacing and the
   bibliography rendering (heading + hanging-indent/number alignment) next session.
3. Pre-submission hands-on references triple-check (external metadata verification, per
   [[feedback_references_triple_check]]).
4. RBW skill: 3 principal calls still open -- style depth (lean vs full evidence-ledger + self-test),
   the `[[project_tri_model_review]]` cross-ref target (commit DONE).
5. Wiley Systems Engineering template + cover letter (post-readiness).
6. Optional: `git init` the `manuscript_v3` dir (currently untracked -- no commit trail for these arcs).

## Memory-worthy (not yet written)
- pandoc renders `lstlisting` as a CENTER-aligned Source-Code table -> must be left-justified in
  post-process (DOCX gotcha, family of [[feedback_holistic_formatting_fidelity]]).
- The SysML claim arc as a worked "measure, don't assume" case (asserted "structural" -> parser+RBW
  disproved) -- reinforces [[feedback_measure_not_assume_llm_intuition]].
- RBW skill gap + the independence principle (red != claim author).

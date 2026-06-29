# Session Archive — 2026-06-24 postwach-02

> PROVENANCE: claude-opus-4-8[1m] (Anthropic, Claude Code CLI). Main-thread model produced this archive,
> the 2026-06-24-postwach-02 scorecard, the Brad-version assessment memory, and the MEMORY.md edit. No
> sub-agents or swarm spawned. Brad's figure PNGs were retrieved from his private GitHub repo via git-lfs
> (his content, not model-generated). Continues [[SESSION_ARCHIVE_2026-06-24_postwach-01]] (resumed after
> that closeout).

**Hive:** PostWach. **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m].

**Headline:** Resumed DV004 to **assess Brad Philipbar's parallel DEVS-MACE proposal** (full LaTeX, repo
`bmpwach-lab/OSW_SCO_D2P2_SBIR_proposal`) against our V8.5 and identify portable improvements. Finding:
Brad's is more polished but is a **different, fuller, non-compliant proposal** (22 pp, 6 tasks, grounded-LLM
pillar, MWDT/Cesium ION, σ notation), so its content, figures included, is **not a clean port**. Documented
the assessment as reusable feedback. **No proposal-file changes** (per principal).

## 1. What was assessed
- Read Brad's 19-page integrated PDF (all 7 volumes). His Vol 2 is over length: Part 1 ≈6 pp (>5), Part 2 ≈11
  pp (>10); 22 pp total. **Our compliant V8.5 docx remains the submission base.**
- Compared structure/content/figures against our V8.5 (sent to Bernie/DH earlier today).

## 2. Key divergences (team decisions, not copy-paste)
1. **LLM posture (biggest).** Brad states + shows a grounded-LLM proposer in the COA pipeline (Pillar P3 +
   Figure 4); ours keeps no LLM/NN in the decision path and the cover page leans anti-NN. Must align one
   story (topic screens "not a monolithic neural network"). If grounded-LLM is real, our cover page + FEAS-4
   need rewriting.
2. **Task count:** Brad 6 tasks (extra Cesium ION wargaming-integration T5) vs our 5 ("five tasks" in text).
3. **Added constructs in Brad:** MWDT (Modern Wargaming Decision Theory), Cesium ION interface,
   compositional-V&V pillar (5.0×10¹³→142, 3.5×10¹¹×, emergent bound), truth-score≥0.95 / GSN. Absent from ours.
4. **Notation:** Brad uses σ for degree of homomorphism; principal has ruled σ out — keep spelled-out / D_s.
5. **Compliance:** Brad over the page limit; ours is the base.

## 3. Figures
Retrieved all 5 of Brad's figures from the **private** repo via `git-lfs` (shallow clone, token-in-URL
removed after; scratch cleaned). They are **Git-LFS PNGs** (~1.3 MB, ≈185 DPI); the repo ships only `.tex` +
rendered PNGs, **no editable figure source**. Copies kept at `02 SDA/OSW26BZ02-DV004/_brad_figs/` for
reference. On visual inspection none is a clean drop-in:
- fig1 architecture — carries MWDT/Cesium ION/capability-Markov/truth-score≥0.95/GSN (terms not in our text).
- **fig2 fidelity — best aligned** (σ/D scatter is our Table 1 data + a traceability panel) but uses σ.
- fig3 compositional-V&V — needs numbers our text lacks.
- fig5 Gantt — shows 6 tasks (contradicts our "five tasks").
- fig4 — grounded-LLM pipeline (quarantined per the LLM decision).

## 4. Outcome / documentation
- Created [[project_devsmace_brad_version_assessment]] capturing the comparison, divergences, figure findings,
  and **feedback for future proposals + product dev with Brad**: agree a single source of truth / shared
  framing (LLM posture, tasks, notation, terminology) before parallel drafting; compliance is binding; require
  collaborators to commit figure SOURCE not just rendered PNGs; consider a shared toolchain (Brad's LaTeX
  out-polishes the docx flow); [R016] treat Brad's version as a parallel artifact, not the deliverable.
- MEMORY.md indexed under the DV004 thread.

## 5. Process note
Net-positive recovery from postwach-01: the "render-and-look" corrective was applied (looked at the actual
figure PNGs), which is what surfaced that the figures are not drop-ins. Honest "strategy fork, not copy-paste"
framing delivered. Minor shell-escaping retries only.

## 6. Open threads / next
- **LLM posture decision** (DH/Bernie/Brad) — gates any figure port and the cover-page wording.
- If keeping the lean version: at most adapt **fig2** after a σ→D_s relabel (needs Brad's figure source).
- Carryover from postwach-01 (unchanged): `feedback_rtsync_ua_file_convention` decimal-convention update
  pending principal's solo-UA answer; optional Table 3 / objectives-indent correction not started.
- Offered (not started): a shareable external memo of this assessment for DH/Bernie/Brad.
- Scorecard: `Papers/AI_Swarm_Productivity/data/scorecards/2026-06-24-postwach-02.yaml` ([R014]).

# Session Archive: 2026-04-13 PostWach-01

**Hive:** PostWach
**Date:** 2026-04-13
**Duration:** ~30 minutes
**Focus:** Berserker requirements extraction for Requirements-Assistant repo seeding

---

## Session Summary

Warmed up ruflo v3.5.7. Located Berserker (MQ-99 UCAV) IGNITE '26 artifacts across 14 files (session archives, scorecards, ontologies, .sysml sources, JSON extractions). Extracted the 233-requirement SFR set from `src/data/berserker_model.json` into a plain-text dump and produced a one-page context brief describing the three-model family (SFR, Implementation Library, Product Baseline), subsystem decomposition, requirement families, and IGNITE arc role. Saved both to `03 Projects/05 IGNITE/IGNITE_Disruption_2026/docs/`.

Copied both files to the public `DocWach/Requirements-Assistant` GitHub repo via the GitHub Contents API (no local clone). Repo already contained `sample_context.txt` and `sample_requirements.txt` at root. Per user request, reorganized: moved all four sample files into a new `samples/` folder using a single atomic commit built via the Git Data API (tree rewrite -> commit -> ref update) so the rename is recorded rather than split into delete+add.

## Key Decisions

- **D74:** Used `berserker_model.json` (233 reqs) as the canonical extraction source over `MQ99_Berserker_Requirements.sysml` (268 reqs). JSON is the cleaner structured set; SysML v2 source flagged as available if the full 268 is later needed.
- **D75:** Requirements txt format: `[ID] (Category) Text`, sorted by ID prefix. Category comes from the `base_class_name` field in the JSON, giving useful grouping (Mission Computer Direction families, CSA-01..10, HT-1..54, etc.).
- **D76:** Context brief written to ~1 page (the user's stated target), covering: what Berserker is, three-model family + Conway's Law zero-overlap finding, 7 subsystems + 4 externals, requirement family taxonomy, IGNITE arc role, artifact inventory.
- **D77:** Requirements-Assistant repo reorg: flat layout (no `berserker/` subfolder), all four samples in `samples/` root, via one atomic Git Data API commit rather than four contents-API PUTs. Preserves history cleanly.
- **D78:** Did not overwrite existing `sample_context.txt` / `sample_requirements.txt`. Berserker files added alongside. User can decide later whether Berserker should replace the toy samples as the default demo input.

## Work Completed

### Berserker artifacts located
- Scanned PostWach tree for `Berserker` references: 14 files across session archives (7), productivity scorecards (4), project registry (1), plus SysML/JSON/OWL/XLSX/TTL extraction artifacts.
- Confirmed canonical requirement sources in `03 Projects/05 IGNITE/IGNITE_Disruption_2026/`:
  - `src/data/berserker_model.json` (233 reqs, structured)
  - `docs/Cameo Models/SysMLv2/MQ99_Berserker_Requirements.sysml` (268 `requirement def` blocks)
  - `src/ontology/berserker-assessment.ttl`, `berserker-abox.ttl`
  - `docs/Berserker_Full_Extraction_2026-03-18.xlsx` (8 sheets), `Berserker_Deep_Extraction_2026-03-18.xlsx` (5 sheets)

### Files produced (local)
- `03 Projects/05 IGNITE/IGNITE_Disruption_2026/docs/Berserker_Requirements_All.txt` — 709 lines, 233 requirements, sorted by ID.
- `03 Projects/05 IGNITE/IGNITE_Disruption_2026/docs/Berserker_Context.txt` — 1 page, system definition + 7 subsystems + 4 externals + 8 requirement families + IGNITE role.

### Git operations on DocWach/Requirements-Assistant
- Commit `492e776`: add `Berserker_Requirements_All.txt` (Contents API PUT).
- Commit `a79134c`: add `Berserker_Context.txt` (Contents API PUT).
- Commit `05e6799`: atomic rename of all four `.txt` files into `samples/` via Git Data API (trees + commit + ref). Root now lists `samples/` alongside `backend/`, `frontend/`, `run.py`, etc.

### Verified
- Root of repo no longer has loose sample .txt files.
- `samples/` contains: `Berserker_Context.txt`, `Berserker_Requirements_All.txt`, `sample_context.txt`, `sample_requirements.txt`.

## Open Threads / Handoffs

- **Code path references (flagged, not executed):** `run.py` / `backend/` may hard-code root-level paths to `sample_context.txt` or `sample_requirements.txt`. If so, moves will break the app. User declined to grep/patch in this session; deferred.
- **Requirements source choice:** If the 268-requirement SysML v2 export is later preferred over the 233 JSON set, the SysML source file is at `docs/Cameo Models/SysMLv2/MQ99_Berserker_Requirements.sysml` and can be parsed similarly.
- **Sample curation:** Open question whether the toy `sample_*.txt` files should remain or be superseded by Berserker as the default example for the Requirements-Assistant demo.

## Files Touched

- `docs/Berserker_Requirements_All.txt` (created, IGNITE docs, 709 lines)
- `docs/Berserker_Context.txt` (created, IGNITE docs, ~60 lines)
- `docs/session-archives/SESSION_ARCHIVE_2026-04-13_postwach-01.md` (created, this file)
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-04-13-postwach-01.yaml` (created)
- DocWach/Requirements-Assistant: 3 commits (`492e776`, `a79134c`, `05e6799`)

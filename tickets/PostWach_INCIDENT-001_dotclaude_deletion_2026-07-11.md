# PostWach INCIDENT-001 — `.claude/` working-tree deletion

- **Opened:** 2026-07-11
- **Severity:** High (loss of the hive's `.claude/` config — skills, agents, helpers — from the working tree; recoverable, see below)
- **Status:** OPEN — recovery held pending principal coordination with a parallel session
- **Owner:** PostWach (CTO)
- **Provenance (R018):** ticket authored by Opus 4.8 (claude-opus-4-8[1m]), Claude Code, 2026-07-11.

## Summary
The entire `.claude/` folder of the PostWach hive (`01 Hives/01 PostWach/.claude/`) is **missing from the local working tree** — **542 tracked files** (skills incl. the morphism-* + ref* set, agents, helpers, commands, settings). All 542 are **intact in git** (they show as unstaged working-tree deletions, ` D`). The loss is **contained to `.claude/` only**; nothing else in the repo is affected.

## Detection & timeline
- Detected 2026-07-11 during the post-derivation skill-promotion step: a Read of `.claude/skills/morphism-research-frontier/SKILL.md` returned "file does not exist," despite the same files being read/edited successfully earlier the same day.
- Confirmed: `Test-Path .claude` = False; `git status --short` = 542 ` D` entries, **100% under `.claude/`**; `git ls-files .claude/skills` = 124 tracked.
- Principal visually confirmed `.claude` absent from the tree.

## Diagnosis
- **Working-tree deletion, unstaged** (` D`, not `D `). Therefore NOT `git rm` (which stages), and NOT a rename/move within the repo (no untracked `.claude*` replacement appeared).
- **Windows Recycle Bin: not present** (88 items, 0 match `.claude`/skills/morphism; newest item June 22). So it was NOT a normal Explorer delete.
- Conclusion: a **filesystem-level programmatic delete** (something ran `rm`/`Remove-Item`/`rmtree`) OR a **OneDrive sync removal** — both bypass the local recycle bin.

## Root cause (CONFIRMED 2026-07-11 — supersedes the earlier "likely the parallel session" hypothesis)
The **elicitation session (`fddfa778…`) ran a recursive force-delete of the entire `.claude` folder**, confirmed from its own transcript, on the 2026-07-10 "log as research output" turn:
- line 119: `Remove-Item -Recurse -Force $bad`  (`$bad = "…\01 PostWach\.claude"`)
- line 132: `Remove-Item -Recurse -Force $bad -ErrorAction Stop`
- line 136: `& cmd /c "rd /s /q ""$bad"""`  → "removed cleanly"

`$bad` (= `01 PostWach\.claude`) appears in no other session log. **Intent:** remove ONE misplaced file; **actual:** recursively deleted the whole `.claude` (agents/, skills/, helpers/, settings.json removed silently, depth-first). The only errors were on the OneDrive-locked `projects\…` subtree; a post-failure directory listing was mistakenly trusted as the folder's *original* contents when it was actually the *aftermath* of the delete.

**Timeline caveat (not fully reconstructed):** the 7/10 delete was evidently restored (skills were read/edited in the PostWach session `0618d5b0` on 7/11 morning), then `.claude` was missing again by 7/11 ~15:00; a second session log (`6e87c5db`) contains an unrelated recursive delete, not yet identified. The direct cause of *a* full `.claude` delete is confirmed (elicitation session); the exact re-deletion timeline since is unconfirmed. The prior secondary suspicion of this session's bypass-mode agents is not the cause.

## Blast radius (what is / isn't affected)
- **Lost from working tree:** `.claude/` only (542 files). Recoverable from git (committed base) and/or OneDrive cloud recycle bin.
- **Safe / present:** all `Papers/`, `docs/` (scorecards, session archives), `scripts/`, `tickets/`, `_workspace/`; the Fable-planning research artifacts (metric-satisfaction bridge, Target A v2, `Unification_candidate.md`, all RBW reviews) under `00 Planning and Execution/Fable 5 planning/` (separate folder, edited successfully post-incident); and the **auto-memory** at `C:\Users\pfwac\.claude\...\memory\` (user-profile, NOT OneDrive — intact).
- **At risk (uncommitted, not in git):** today's skill edits from BOTH sessions — this session's 2026-07-10 currency blocks + 2026-07-11 R016 tags on the morphism + 5 analyst skills; the parallel session's in-progress *elicitation* skill edits. The committed base (2026-07-07 morphism authoring + the committed skill set, incl. commits `de9f698`, `d3ee255`) is SAFE in git.

## Recovery options (preserve the most work first)
1. **Parallel elicitation session** — check its state: still open? still holds the skills in context? did it report deleting/moving/restructuring `.claude`? It may be the cleanest recovery (re-save / recommit its work).
2. **OneDrive cloud recycle bin** (onedrive.com → Recycle bin + second-stage bin) — highest fidelity: restores the exact pre-deletion `.claude` with *both* sessions' uncommitted edits.
3. **`git restore .claude/`** — LAST RESORT: recreates the committed base immediately and safely (nothing overwritten, files are absent), but **loses both sessions' uncommitted skill edits** (this session's are reconstructable from its transcript; the elicitation session's must come from that session).

**HELD:** do NOT run `git restore .claude/` while the parallel session may be writing, and not before checking options 1–2, to avoid clobbering the elicitation work.

## Recovery findings (2026-07-11)
Point-in-time snapshot sources (UPDATED — Claude Code's own file-history WAS found):
- **OneDrive cloud recycle bin:** EMPTY (principal checked; no `.claude`).
- **Windows Recycle Bin:** not present (88 items, 0 match, newest June 22).
- **VS Code Local History** (`%APPDATA%\Code\User\History`): 11 folders total, **0 for `.claude/skills`** — the skills were edited by the Claude Code agent writing to disk, not through the VS Code editor, so VS Code took no snapshot.
- OneDrive per-file version history: effectively unavailable (needs the deleted file restored first).
- **Claude Code's OWN `file-history/` (`~/.claude/file-history/`, distinct from VS Code): FOUND — the win.** Organized by session; holds snapshots of edited files. Session `0618d5b0` has 18 snapshots carrying THIS session's exact edit markers ("2026-07-10 currency update", "wach2024theoretical", "Integration status [R016]: (a) research artifact") — the EDITED skill bytes are preserved locally. No SKILL.md snapshots in the elicitation session `fddfa778` (it did not edit skill files).

**Therefore recovery = git base + the file-history bytes / transcript operations for the uncommitted edits:**
- **git** provides all 542 files at the last commit.
- **This session's transcript** contains every `.claude` edit verbatim → this session's uncommitted skill state is FULLY reconstructable (currency blocks marking bridge/Target-A/harmonization CLOSED; R016 tags + analyst downgrades; cross-project-reviewer roster; ref-maintenance). Also independently regenerable from the intact research artifacts.
- **Elicitation session's transcript** → its uncommitted skill edits (that session reconstructs; checklist = the intact `project_stakeholder_elicitation_capability.md`).
- Verify completeness against the `postwach-08` session archive + backlog.

## Prevention / lessons (for the repo-cleanup + governance review)
0. **NEVER use a recursive force-delete to remove a single file** (the root cause). `Remove-Item -Recurse -Force` / `rd /s /q` aimed at one stray file destroyed the whole `.claude/`. To delete one file, target its exact path, and prefer a recycle-bin delete over `-Force`. And **never trust a post-failure directory listing as ground truth** — a partial recursive delete's aftermath looks like sparse "original" contents.
1. **Do not run two Claude Code sessions manipulating the same `.claude/` in a OneDrive-synced directory concurrently** — shared on-disk state + OneDrive sync + rapid multi-process writes is a corruption/loss trap.
2. **Be sparing with bypass-mode external agents** (full disk access = deletion risk); prefer scoped, non-destructive tasks.
3. **Commit `.claude/` skill edits promptly** so working-tree loss is fully recoverable from git (this incident's only exposure is the *uncommitted* edits).
4. Consider a guard: `.claude/` is a OneDrive-synced dot-folder; evaluate excluding it from OneDrive sync, or committing after every skill edit.

## Next actions
- [ ] Principal: check the parallel elicitation session state + the OneDrive cloud recycle bin.
- [ ] Decide recovery path (session re-save / recycle-bin restore / `git restore`).
- [ ] After recovery: re-apply this session's skill edits (currency blocks marking bridge/Target A/harmonization CLOSED; R016 tags), then commit `.claude/`.
- [ ] Fold prevention lessons into the post-2026-07-12 repo-cleanup + Alpha Empress governance review.

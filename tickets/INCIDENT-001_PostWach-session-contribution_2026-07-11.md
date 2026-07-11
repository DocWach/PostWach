# INCIDENT-001 — Contribution from the PostWach session (`0618d5b0`)

**Purpose:** this session **discovered** the `.claude` deletion and performed the **recovery forensics**; content here is for folding into the incident report and for the RBW review's fact-check. Every finding below is reproducible (exact commands are in this session's transcript).
**Provenance (R018):** Opus 4.8, Claude Code, 2026-07-11. Cross-ref the full ticket `PostWach_INCIDENT-001_dotclaude_deletion_2026-07-11.md`.

## 1. Discovery (this session, 2026-07-11 ~15:00)
- Detected during the post-derivation **skill-promotion** step: a `Read` of `.claude/skills/morphism-research-frontier/SKILL.md` returned "file does not exist," despite the same file being read/edited earlier the same day.
- Confirmed: `Test-Path .claude` = **False**; `git status --short` = **542 unstaged deletions (` D`), 100% under `.claude/`**; `git ls-files .claude/skills` = 124.

## 2. Blast radius (confirmed contained)
- **542 deleted, ALL under `.claude/`** (skills / agents / helpers / commands / settings). Nothing else deleted.
- **Present / safe:** `Papers/`, `docs/` (scorecards, session archives), `scripts/`, `tickets/`, `_workspace/`; the Fable-planning research artifacts (metric-satisfaction bridge, Target A v2, `Unification_candidate.md`, the RBW reviews) under `00 Planning and Execution/Fable 5 planning/`; and the **user-profile auto-memory** at `C:\Users\pfwac\.claude\...\memory\` (a *different* location from the deleted project `.claude`).

## 3. Recovery-source forensics (where the uncommitted edits survive)
- **OneDrive cloud recycle bin:** EMPTY (principal checked; no `.claude`).
- **Windows Recycle Bin:** NOT present (Shell COM enumeration: 88 items, 0 match `.claude`/skills/morphism, newest June 22) → **not a normal Explorer delete** → a programmatic recursive delete or a OneDrive sync removal (both bypass the local recycle bin).
- **VS Code Local History** (`%APPDATA%\Code\User\History`): 11 folders total, **0 for `.claude/skills`** — the skills were edited by the Claude Code agent writing to disk, not through the VS Code editor, so VS Code took no snapshot. No Cursor/Windsurf/Insiders/VSCodium history.
- **Claude Code's OWN `file-history/` (`~/.claude/file-history/`, per-session): FOUND — the recovery win.** Session `0618d5b0` holds **18 snapshots carrying this session's exact edit markers** (`2026-07-10 currency update`, `wach2024theoretical`, `Integration status [R016]: (a) research artifact`) → the **edited (post-edit) uncommitted skill bytes are preserved locally**. No SKILL.md snapshots in the elicitation session `fddfa778` (it did not edit skill files).

## 4. Recovery method established / verified here
- **`git restore .claude/`** → all 542 files at the committed base. Verified after restore: `git status -- .claude` is **clean (0 entries)** and this session's currency block is **absent** → confirmed clean committed base.
- **Uncommitted edits re-applied on top** from the file-history bytes + this session's transcript (exact operations).

## 5. This session's uncommitted skill edits (to fold in / re-apply)
- 2026-07-10 **currency blocks** on the 4 morphism skills.
- 2026-07-11 **R016 `(a)` tags + analyst downgrades** on `cross-project-reviewer`, `research-portfolio-optimizer`, `biomimetics-analyst`, `cognitive-study-designer`, `transfer-learning-analyst`; plus the **cross-project-reviewer roster** refresh (11 V3 hives).
- **Ref-maintenance** on `morphism-domain-reference` (`@wach2024theoretical`; Girard/Cousot disambiguation).
- **Intended final state:** the morphism currency blocks should mark the **bridge, Target A, and harmonization all CLOSED**, with the **Cody 2021 / Zeigler positioning** and the **delta-as-record** framing.

## 6. For the RBW review (truth / thoroughness targets)
All claims here are reproducible; the RBW should independently verify:
1. 542 deletions, all under `.claude/` (`git status --short`).
2. OneDrive recycle bin + Windows Recycle Bin + VS Code Local History all lack `.claude/skills`.
3. Claude Code `file-history` **does** hold this session's edited bytes (18 marker-carrying snapshots) — i.e., the uncommitted edits were recoverable, not lost.
4. Post-restore `.claude` matched the committed base exactly (clean `git status`).
5. Root cause (per the elicitation session's own transcript): a recursive force-delete (`Remove-Item -Recurse -Force` / `rd /s /q`) of `01 PostWach\.claude`, intended for one stray file. The prior "bypass-mode agents / two-session sync" hypotheses were NOT the cause.

## 7. Prevention lessons surfaced here (fold into the report)
0. **Never use a recursive force-delete to remove a single file**, and never trust a post-failure directory listing as ground truth (a partial delete's aftermath looks like sparse "original" contents).
1. Don't run two Claude Code sessions manipulating the same `.claude/` in a OneDrive-synced dir concurrently.
2. Be sparing with bypass-mode external agents (full disk access = deletion risk).
3. Commit `.claude/` skill edits promptly so working-tree loss is fully git-recoverable.
4. Note: Claude Code's `file-history` is a real local safety net for uncommitted edits — but it is per-session and not permanent; not a substitute for committing.

# Session Archive: 2026-05-21 PostWach-01

**Date:** Thursday, 2026-05-21
**Hive:** PostWach (CTO)
**Duration:** ~1 hour (session 1) + continuation after restart (session 2)
**Branch:** `main`

## Context

Resumed the deferred "PaperBanana" thread (automated academic figure generation, prior research 2026-02-27). User asked to re-verify the tool's current state plus our own local capabilities, then chose an integration path and began setup. Session ended for a machine restart (system updates) with the MCP registration step still pending.

## Accomplishments

### ruflo warm-up
- `ruflo v3.7.0-alpha.14` confirmed responding.

### Re-verification of PaperBanana (vs 78-day-old notes)
- **PaperBanana now v0.1.2** (released 2026-02-13). `pip install "paperbanana[mcp]"`, Python 3.10+.
- VLM providers: OpenAI (`gpt-5.2` default), Gemini (`gemini-2.0-flash`, free), OpenRouter, Azure.
- Image providers: OpenAI `gpt-image-1.5`, **Google `gemini-3-pro-image-preview` (nano-banana Pro)**, OpenRouter.
- New since old notes: batch manifests, PDF input, Gradio "Studio" UI, full-paper figure orchestration, composite multi-panel stitching, **ships an MCP server (`paperbanana-mcp`) + 3 Claude Code skills**.
- **Correction to old notes:** there is no native "Anthropic SDK" VLM provider as previously assumed. Instead the repo now ships `paperbanana/providers/vlm/claude_code.py` — a `ClaudeCodeVLM` provider that shells out to the local `claude` CLI, "no API key needed, uses the user's Claude Code subscription." This lets the VLM/reasoning side (Planner→Stylist→Critic) run through Claude Code, spending the Gemini key only on image pixels.

### Local capability audit
- **Gemini CLI** `0.42.0-nightly`, headless `-p` mode works, auth = `oauth-personal` (free tier). No extensions installed.
- **Key finding:** image generation does NOT ride on the OAuth CLI login. Both the nano-banana CLI extension (`NANOBANANA_API_KEY`) and PaperBanana's Google image provider (`GOOGLE_API_KEY`) require a separate AI Studio API key. The free VS Code CLI login alone won't produce figures.
- No provider API keys were set at session start (GEMINI/GOOGLE/ANTHROPIC/OPENAI/OPENROUTER all unset).
- Python 3.12.10 **arm64**; pip 26.0.1; no pipx; no uv/uvx.

### Decisions (via AskUserQuestion)
- **API key:** user obtains a free AI Studio key.
- **Integration shape:** PaperBanana MCP server + Claude Code skills (cleanest fit for this Claude Code machine).

### Install + skills (completed)
- `pip install "paperbanana[mcp]"` initially **failed** building `cryptography` from source (no win-arm64 wheel for the old pinned version → needed Rust/cargo). **Fixed** with `--only-binary=cryptography`, which let pip resolve `cryptography-46.0.3` (has an arm64 wheel). PaperBanana 0.1.2 + fastmcp + google-genai installed cleanly.
- Console scripts verified: `paperbanana.exe`, `paperbanana-mcp.exe` (at `...\Python312-arm64\Scripts\`).
- Fetched the 3 SKILL.md files from the repo and wrote them to `.claude/skills/`: `generate-diagram`, `generate-plot`, `evaluate-diagram`. All three registered and visible in the skills list.

### API key handling (in progress)
- Guided user to set `GOOGLE_API_KEY` as a **Windows User env var** in their own terminal (kept out of transcript and out of any tracked file, per R105). User confirmed the value is set (verified by retrieval). Restart of Claude Code required so the MCP server inherits it.

## Session 2 (continuation, post-restart) — MCP wiring + package audit

User restarted Claude Code (system updates), then "warm up ruflo, resume PaperBanana."

### ruflo
- `ruflo v3.7.0-alpha.14` confirmed responding.

### Verified resume preconditions
- `GOOGLE_API_KEY` present at BOTH process and User scope (length 39) — key survived restart and reaches child processes. Length-only check; value never printed (R105).
- `paperbanana.exe` + `paperbanana-mcp.exe` still on PATH (`...\Python312-arm64\Scripts\`).
- 3 skills still live: `/generate-diagram`, `/generate-plot`, `/evaluate-diagram`.

### Package audit — CORRECTIONS to session-1 notes
Inspected the installed `paperbanana 0.1.2` source directly. Two prior assumptions were wrong:
- **No `claude_code` VLM provider exists in 0.1.2.** `providers/registry.py` accepts only `gemini` and `openrouter` (raises `ValueError` otherwise). There is no `providers/vlm/claude_code.py`. The "run reasoning through Claude Code to save the Gemini key" plan is NOT available in this version.
- **The MCP server reads NO config file.** Entry point is `mcp_server.server:main` (top-level `mcp_server` module, fastmcp-based), and it builds `Settings(refinement_iterations=iterations)` from **defaults + env vars only**. `paperbanana setup` / `config.yaml` are irrelevant to the MCP path. So resume-step 4 (write config) is MOOT.
- **Net effect:** defaults are already the desired config — VLM `gemini-2.0-flash` (free tier) + image `gemini-3-pro-image-preview` (nano-banana Pro), both off `GOOGLE_API_KEY`. Only image gen spends paid quota.

### Pipeline robustness confirmed (no staging needed)
- `prompts/` ships at the site-packages root; agents resolve it via the package-relative fallback in `pipeline._find_prompt_dir()`.
- `ReferenceStore._load()` degrades gracefully: missing `index.json` → warning + empty list; pipeline proceeds with zero in-context examples.
- `data/` (guidelines) ships with the package.

### Edits made
- Added `paperbanana` block to `.mcp.json`: `command: paperbanana-mcp`, `args: []` (stdio), `env.GOOGLE_API_KEY: "${GOOGLE_API_KEY}"` (expansion, no literal key — R105), `env.OUTPUT_DIR` → absolute dedicated folder `01 PostWach/paperbanana-output` (keeps repo root clean per R104; `Settings` reads `OUTPUT_DIR` by field name), `autoStart: false` (matches claude-flow). JSON validated; servers now `['claude-flow','paperbanana']`.
- Appended `paperbanana-output/` to `.gitignore` (tool-generated figures not committed; finals to be curated into paper folders).

## State at Session End (session 2)
- `.mcp.json` paperbanana block registered + validated; `.gitignore` updated.
- **NOT yet done:** new MCP server not loaded (added AFTER the user's restart) — needs ANOTHER restart; `mcp__paperbanana__*` tools not yet confirmed; no figure generated yet.

## Resume Steps (after the NEXT restart)
1. Confirm `mcp__paperbanana__*` tools appear (generate_diagram / generate_plot / evaluate_diagram).
2. Smoke test: `/generate-diagram` on a small methodology snippet; confirm a real PNG lands in `paperbanana-output/<run_id>/final_output.png` (flag as tool-generated per R016 / data-provenance habit).
3. If green: update `completed_items.md` PaperBanana entry; consider promoting to portfolio capability-index.

## Governance / Notes
- R105 honored: API key never written to a tracked file; `${GOOGLE_API_KEY}` expansion used in `.mcp.json`.
- R104 honored: outputs redirected out of repo root into gitignored `paperbanana-output/`.
- R016 status of PaperBanana: still **(a) research artifact / partial (b)** — installed, CLI-functional, MCP registered but not yet connected and no figure produced. Do not present as integrated deliverable until smoke test passes.
- arm64 wheel gotcha logged (session 1): for native-extension Python deps on this machine, prefer `--only-binary=<pkg>` to force a wheel rather than a source build.

---

## Session 3 (continuation, post-restart) — Smoke test + quota/key diagnosis

User restarted Claude Code, then "warm up ruflo, resume PaperBanana work."

### ruflo
- `ruflo v3.7.0-alpha.14` confirmed responding.

### Resume step 1 — tools confirmed
- `mcp__paperbanana__generate_diagram` / `generate_plot` / `evaluate_diagram` all appear in the session tool surface. The new MCP server loaded after the restart. Resume step 1 SATISFIED.

### Resume step 2 — smoke test attempted (subject: WySE morphism, user-chosen)
- Subject: mass-spring-damper ↔ series RLC isomorphism under force-voltage (Maxwell) analogy (doubly useful — tests tool + candidate figure for iso-degradation paper line).
- **MCP-call gotcha discovered:** the harness drops the `caption` argument when it is passed AFTER a long `source_context`. Two calls failed `caption Missing required argument` until `caption` was placed FIRST. Pass `caption` before `source_context` for this tool.
- After arg ordering fixed, call reached the Google API and failed downstream: **429 RESOURCE_EXHAUSTED**.

### Diagnosis — integration verified end-to-end; block is account-side
- Direct `google-genai` test of `GOOGLE_API_KEY` against `gemini-2.0-flash` (cheap text call, key never printed — R105): authenticated (429, not 401/403) but quota `limit: 0` on `generate_content_free_tier_requests` / `..._input_token_count`.
- `limit: 0` = key's Cloud project has **no free-tier allocation** (region ineligibility, billing toggled then off, or wrong project). The "retry in 52s" hint is boilerplate; structural zero, not transient.
- Established for the user that **AI Studio key = Gemini API key** (same credential); Vertex AI and the Gemini CLI OAuth login are different access paths. The free CLI OAuth does NOT cover image generation and is a separate quota system, so routing PaperBanana through the CLI is not viable (registry accepts only `gemini`/`openrouter`; no CLI provider in 0.1.2).
- **Verdict:** wiring/config correct end-to-end up to Google's quota gate. R016 status unchanged: still (a)/(partial b) until a figure renders.

### User action — enabled paid plan
- User enabled billing. Re-test: 429 quota wall GONE (billing recognized), but new error **400 INVALID_ARGUMENT "API key expired. Please renew the API key."**
- Guided user to mint a fresh key in the billed project and reset the `GOOGLE_API_KEY` User env var via PowerShell.
- **Mishap:** user accidentally deleted the newly-added key. A fresh key + restart still needed.

## State at Session End (session 3)
- Billing now enabled on the key's Google Cloud project (quota=0 resolved).
- No valid key currently in place (expired key + accidental deletion of replacement). MCP server still holds stale env.
- No figure produced yet. PaperBanana R016 status: (a) research artifact / partial (b) — installed, MCP-connected, reaches Google API; not yet a demonstrated capability (no rendered figure).

## Resume Steps (after the NEXT restart)
1. Confirm a valid `GOOGLE_API_KEY` is set at User scope (length check only, never print — R105) and that the MCP server inherited it.
2. Cheap text precheck: `google-genai` call to `gemini-2.0-flash` should return text (not 429, not 400-expired).
3. Rerun smoke test via `mcp__paperbanana__generate_diagram` — **pass `caption` BEFORE `source_context`** — subject: WySE mass-spring↔RLC morphism. Confirm a real PNG at `paperbanana-output/<run_id>/final_output.png` (flag tool-generated per R016 / data-provenance).
4. If green: update `completed_items.md` PaperBanana entry to demonstrated capability (b); consider promoting to portfolio capability-index.

## Governance / Notes (session 3)
- R105 honored throughout: key never printed or written to a tracked file; only presence/length checked; `${GOOGLE_API_KEY}` expansion retained in `.mcp.json`.
- [R108] honored: stopped at diagnosis of the quota/key issue (account/infra), did not debug Google billing internals.

---

## Session 4 (continuation, post-restart) — first figures, critic fix, ownership analysis

User restarted, then "warm up ruflo and resume PaperBanana." This session turned PaperBanana from blocked into a working capability and then explored owning it.

### ruflo + resume
- `ruflo v3.7.0-alpha.14`; `system_health` score 100 (MCP stdio running). Resume preconditions checked.
- The process-inherited `GOOGLE_API_KEY` was still the **expired** key; the **User-scope** key was fresh (lengths matched but values differed). Ran all subsequent calls against the User-scope key directly (R105: never printed).

### First figures rendered (R016 → (b) demonstrated)
- Fresh key valid; package default `gemini-2.0-flash` returns **404 for new Cloud projects**, so overrode VLM to `gemini-2.5-flash`. Image model `gemini-3-pro-image-preview` (nano-banana Pro) fine.
- Ran the CLI directly (bypassing the stale MCP server). Two physically-correct, publication-grade morphism diagrams: mass-spring-damper ↔ series RLC (force-voltage), and RC ↔ hydraulic tank-pipe (pressure-voltage, with self-supplied Hagen-Poiseuille resistance). Tool-generated.

### Critic / refinement-loop root-cause + fix
- The `Failed to parse critic response: Unterminated string` warning (every run) traced to **thinking-token truncation**: `gemini-2.5-flash` is a reasoning model; thinking consumed ~3,800 of the 4,096 critic budget, truncating the JSON → conservative fallback `needs_revision=False` → loop died at iteration 1.
- **Fix (durable, no code edit):** `VLM_MODEL=gemini-2.5-flash-lite` (thinking off by default → complete JSON). Verified end-to-end: critic parses, loop iterates 2/2, and iter-2 **improved** on iter-1 (added requested `v`/`i` labels). Confirmed `thinking_budget=0` also fixes the full model (optional patch, deferred — site-packages edit).
- Known limitation documented: pipeline returns last iteration (no keep-best); regeneration is stochastic text-to-image (no img2img).

### Capability promotion + wiring
- `.mcp.json` paperbanana env: added `VLM_MODEL=gemini-2.5-flash-lite` (R017/R106 claude-flow block intact; R105 `${GOOGLE_API_KEY}` expansion preserved). MCP path needs one more restart to load it; CLI works now.
- `docs/capability-index.md`: PaperBanana added as PostWach (b) demonstrated capability + cross-project reuse row + review-log entry; model gotcha + limitation recorded.
- No `completed_items.md` exists; `effort_report.md:88` left intact (dated retrospective, not rewritten).

### Ownership analysis (curiosity-driven, no build)
- PaperBanana is MIT, ~2,900 LOC, a thin orchestration+prompt layer over rented models. Fork-and-fix is cheap; the value (legible-equation synthesis) is frontier-image-API-only, so "Google-free" hits physics.
- Two spikes scoped (ClaudeVLM provider; local-image equation test) — **both deferred by user**.
- Five wrap-up actions completed: (3) External Tool Adoption Protocol added to `cross-project-reviewer` skill; (4) Topic 7 added to `docs/inter-hive-policy-considerations.md`; (5) open-thread memory `project_paperbanana_ownership.md` + MEMORY.md entry. Tool-state memory `project_paperbanana.md` also created.
- Hive-of-hives: PaperBanana is the 3rd instance of the shared-capability pattern (with doc-merge + auto-memory-hook); recommended Output/shared service, PostWach-curated, standalone `DocWach/*` repo, thin MCP server (H1-hybrid).

## State at Session End (session 4)
- PaperBanana **(b) demonstrated**, refinement loop functional on `gemini-2.5-flash-lite`. MCP path will pick up the model on next restart.
- Ownership = open thread, planning mode; spikes deferred.

## Governance / Notes (session 4)
- R105: API key never printed or committed; User-scope value used directly; `${GOOGLE_API_KEY}` expansion retained.
- R016: PaperBanana classified (b); "owned vs rented" distinction stated explicitly in the analysis.
- R002/R102: extended existing skill + agenda doc rather than creating new docs; no fragile site-packages patch applied (user deferred).
- R104: tool outputs + scratch scripts confined to gitignored `paperbanana-output/`.

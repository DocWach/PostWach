# Session Archive — 2026-06-22 postwach-03

**Hive:** PostWach. **Researcher:** Paul Wach. **Model:** Claude Opus 4.8.
**Headline:** Diagnosed and resolved the Gemini CLI login failure (Google killed the free OAuth / Code Assist "Sign in with Google" path on 2026-06-18, replacing it with Antigravity). Restored the `gemini` CLI on API-key auth for the headless tri-model pipeline, installed Antigravity CLI (`agy` v1.0.10) for interactive use, confirmed paperbanana recovered, and set up Gemini API spend control ($50/mo project cap).

---

## Context
Carried over from the proposal session (postwach-01): paperbanana's image backend threw `ServerError` x6, and the principal hit a login error on the Gemini CLI, with a hunch about a service/TOS change. This session investigated.

## Root cause (two separate problems, previously conflated)
1. **CLI login error = OAuth deprecation.** The Gemini CLI uses `oauth-personal` (free Gemini Code Assist for individuals), account paulwach@arizona.edu. On **2026-06-18** Google shut that serving path down for the unpaid tier, AI Pro/Ultra, and **Google One / Gemini Advanced** subscribers. Exact error: *"This client is no longer supported for Gemini Code Assist for individuals... migrate to the Antigravity suite."* The OAuth flow completes, then the backend rejects it (creds were even still valid). TOS page banner: "Gemini CLI will be replaced by Antigravity CLI on June 18th."
2. **Paperbanana ServerError = transient outage, NOT the key.** The billed `GOOGLE_API_KEY` tested **HTTP 200** (valid). Re-tested paperbanana later this session: clean diagram on the first try -> **recovered**. The earlier "TOS change broke the API-key path" hypothesis was wrong; the API key path was always fine, the OAuth path is what died.

## Key finding (corrects a natural assumption)
A **consumer Gemini subscription (Gemini Advanced / Google One AI Premium, ~$20/mo) does NOT cover the Gemini CLI or the Gemini Developer API.** It powers the gemini.google.com app and now Antigravity. App subscription and API billing are separate buckets. Confirmed by the "for individuals" rejection and Google's billing structure.

## Resolution (two-lane setup)
**Lane A - headless automation (tri-model pipeline): `gemini` CLI on API key.**
- Set `~/.gemini/settings.json` `security.auth.selectedType` = `gemini-api-key` (valid enum confirmed by grepping the gemini-cli bundle: oauth-personal | gemini-api-key | vertex-ai | cloud-shell). Backup `settings.json.bak`.
- Quirk: gemini-cli **requires `GEMINI_API_KEY` to be present** to unlock the api-key path (the gate), then **uses `GOOGLE_API_KEY`** for the call when both are set. So `GEMINI_API_KEY` (Windows User scope) was set to the same value as the pre-existing `GOOGLE_API_KEY` (no new key; paperbanana's billed key). A cleanup attempt to drop the redundant var correctly self-aborted (auth broke without it). Benign stderr: "Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY."
- Verified: `gemini -m gemini-2.5-flash -p ...` returned **AUTHOK**. Tri-model pipeline needs no code changes; `gemini` still runs headless, just key-authed (pay-as-you-go, pennies for text).

**Lane B - interactive coding: Antigravity CLI (`agy`).**
- Installed v1.0.10 to `%LOCALAPPDATA%\agy\bin` via `irm https://antigravity.google/cli/install.ps1 | iex`; added to User PATH registry. Standalone Go binary, no Node.
- `agy` "does not work" was a **stale-terminal PATH refresh**, not a broken install (binary runs by full path; bin IS in User PATH registry). Fix: `$env:Path += ";$env:LOCALAPPDATA\agy\bin"` for the current session, or fully restart the terminal app / log out-in.
- **Browser login, not headless** (good for interactive use on the subscription; do NOT use in the headless pipeline - this is why CI/CD broke on 06-18). Subscription tier ~20 req/day.
- TOS caution: reusing the CLI OAuth token in third-party tools is a violation; tools must use API keys (paperbanana already does).

## Gemini API spend control (current 2026-06)
The `gemini` CLI and paperbanana share `GOOGLE_API_KEY` -> same project, so one project cap covers both.
- Automatic backstop: mandatory tier cap (~$250 Tier 1) since 2026-04-01, cannot be disabled.
- Precise control: optional **project-level spend caps** in AI Studio (added 2026-03-16). **Principal set a $50/mo project cap this session;** observed spend ~$25/mo (~2x headroom), likely dominated by paperbanana image generation (pricier than CLI text). Lever to reduce: Mermaid for box/flow figures (free), reserve paperbanana for equation figures, lower `iterations`.
- Monitor: AI Studio -> Billing -> Daily Cost Breakdown.

## Memory updates
- Created `project_gemini_cli_migration.md` (the full record + cost-control section with the $50 cap).
- Updated `project_paperbanana_gemini_outage.md` (corrected root cause; paperbanana confirmed recovered).
- Updated `MEMORY.md` index (migration pointer + corrected outage line).

## Termination
No swarm agents or Task subagents spawned this session (all direct tooling: Bash/PowerShell, WebFetch, WebSearch, paperbanana). claude-flow agent list = "No agents found." No background tasks left running. No Word COM this session. Scorecard: `Papers/AI_Swarm_Productivity/data/scorecards/2026-06-22-postwach-03.yaml`.

## Open (principal-side, non-blocking)
- Confirm `gemini` and `agy` both work in a fully fresh terminal (env var + PATH need a new shell parent); complete the `agy` browser login.

# Session Archive — 2026-04-21 postwach-03

**Hive:** PostWach (CTO role)
**Scope:** Reconnaissance for Cameo SysML v2 plugin install from `bmpwach-lab` GitHub org; produce inventory, activity plan, and risk list; stop before execution
**Platform:** Ruflo v3.5.80, claude-opus-4-7 (1M context), Windows 11 ARM64
**Outcome:** Paused for hardware/tool alignment (CEA 2026x inbound vs MSOSA 2024x on hand)

---

## 1. Entry state

User request: "warm up ruflo. I would like help getting the SysMLv2 plugin added to Cameo (Magic Systems of Systems Architect). You will need to review the bmpuls-wach lab files on GitHub. Please inventory, plan out activities, and ID any potential troubles."

Starting assumptions to resolve:
- Is `bmpuls-wach` a GitHub user, org, or combined name
- Which Cameo-family product + version Paul is targeting
- Whether plugin is public or private / proprietary

---

## 2. Method

No swarm; direct tool use only.

1. `claude-flow --version` → ruflo v3.5.80 confirmed
2. `gh api users/bmpuls-wach` → 404
3. `gh search users bmpuls` → found `bmpuls` (0 public repos, dead end)
4. `gh search code bmpuls` → hit on `bmpwach-lab/ZynWorld` in taptrap dataset; corrected name
5. `gh api orgs/bmpwach-lab` + `gh repo list bmpwach-lab --limit 200 --json …` → full inventory
6. `gh api repos/.../contents/` + `.../readme` + `.../contents/PLAN.md` + `.../contents/plugin.xml` → read primary repo assets without cloning
7. Presented inventory + 9-step plan + 11-item risk list; user called pause

---

## 3. Findings

### 3.1 Name correction

`bmpuls-wach` → **`bmpwach-lab`**. 46 private repos, tagline "Systems modeling, simulation & wargaming research," created 2026-02-18. Identity cross-refs: Brad M. Philipbar (Philipbar Analytics LLC) + Wach lab. Already surfaces in PostWach project memory under IGNITE (ZynWorld platform) and the UofA + Violet Labs + RTSync IGNITE team.

### 3.2 Target repos identified

| Priority | Repo | Purpose |
|---|---|---|
| **P0** | `MBSE_Agentic_Plugin_CEA26xSysMLV2` | Java plugin for Cameo EA 2026x + SysML V2. Gradle. 57 MB. Last push 2026-03-18. Java 21 required. KerML/EMF native (not UML with stereotypes). Multi-provider AI swarm (Claude Opus 4.5, Gemini 2.0 Flash, GPT-4o) with 0.85 quality gate, self-healing, bi-directional model coupling. Deploys as `com.rtsync.mbse.sysml2agent`. |
| **P1** | `MBSE_Agentic_Plugin` | Standalone "working build" 2025-12-04, 1.5 MB, ships `plugin.xml` + 97 Java source files. Activity + Sequence diagrams confirmed working. |
| Ref | `V1toV2` | SysML v1.5 MagicDraw → v2 textual converter (Python). |
| Ref | `E2E_DEVS_SWARM_DEM-S` | Cameo EA integration + DEVS engine (C++). |

### 3.3 Proposed 9-step plan (paused)

1. Confirm target tool + version (CEA 2026x vs MSOSA)
2. Clone P0 to scratch outside OneDrive (Gradle + OneDrive = friction)
3. Verify JDK 21, `JAVA_HOME`, Windows shell for gradlew.bat, ≥1 raw AI API key
4. Read repo `PLAN.md` + `CLAUDE.md`
5. Port macOS build + deploy to Windows (paths, env vars, launcher)
6. Resolve Cameo bundled JAR deps (sysml-*, kerml-*, sysml2.sysml.core, sysml2.kerml.core, textual.modelgenerator)
7. Build → deploy → launch → verify "SysML V2 Agent" menu
8. Manual-menu smoke test with single provider
9. Defer autonomous swarm until manual path works

### 3.4 11-item risk list (paused)

- Platform gap (README is macOS-only)
- ARM64 question for Cameo on Windows ARM
- README clone URL wrong (`bmpuls/…` vs actual `bmpwach-lab/…`)
- Proprietary license, external lab (Philipbar Analytics); [R016] = research artifact from collaborating lab
- Dependency surface against Cameo install's bundled JARs
- macOS-specific paths in base README + likely in `build.gradle`
- Plugin namespace `com.rtsync.mbse.sysml2agent` (branding collision if forked)
- Raw API key vs Claude Code session (not interchangeable)
- Autonomous swarm starts on project launch (aggressive default for first bringup)
- Cross-hive governance question (external lab adoption path)
- Fort Wachs security-review implication (running external Java in Cameo)

---

## 4. Decision

User: **pause**. CEA 2026x arriving within ~1 day. Current box has MSOSA 2024x only, which would force rework once CEA 2026x lands. Correct call — the plugin targets KerML/EMF APIs specific to CEA 2026x HF1+, and MSOSA 2024x uses the older UML+profile stack; building against the wrong version is largely throw-away.

---

## 5. Deliverables

### On disk (PostWach-local)
- `01 PostWach/Papers/AI_Swarm_Productivity/data/scorecards/2026-04-21-postwach-03.yaml`
- `01 PostWach/docs/session-archives/SESSION_ARCHIVE_2026-04-21_postwach-03.md` (this file)

### Cached fetches (scratch, not committed)
- `$TEMP/cameo-plan/README_primary.md` (40 KB)
- `$TEMP/cameo-plan/README_base.md` (11 KB)
- `$TEMP/cameo-plan/PLAN.md` (10 KB)
- `$TEMP/cameo-plan/plugin.xml` (3 KB)

### Code/repo changes
- None

### Agents spawned or terminated
- None

---

## 6. Open threads for next session

When CEA 2026x is installed:

1. **Install prerequisite check.** Confirm JDK 21 and `JAVA_HOME`, `gradlew.bat` workable under chosen shell, raw API key present (Anthropic preferred; Gemini or OpenAI acceptable).
2. **Confirm Cameo install path on Windows** and verify the five Dassault-bundled plugin JARs exist at the expected subpath under `plugins/com.nomagic.magicdraw.sysml2.plugin/lib/`.
3. **Clone P0** (`bmpwach-lab/MBSE_Agentic_Plugin_CEA26xSysMLV2`) to `C:\dev\bmpwach-lab\…` (outside OneDrive).
4. **Audit build.gradle + gradle/** for hardcoded paths or mac-only assumptions; port to Windows.
5. **Decide governance posture.** External lab's proprietary code running inside a UofA-licensed Cameo install. Needs a conversation with Brad on intended use (evaluation, IGNITE, or broader) and a Fort Wachs review if this becomes a durable dependency.
6. **Disable autonomous-swarm-on-launch** for first successful bringup; smoke test via "SysML V2 Agent → Import SysML V2 File" menu with a hand-written trivial `.sysml`.
7. **Then** attempt "Swarm Generate (Full Workflow)" with a small prompt on a single provider.

### Context markers

- [R016]: primary plugin sits at (a) external-lab research artifact. Do not present as PostWach demonstrated capability or integrated deliverable without explicit decision.
- bmpwach-lab is Brad Philipbar's lab, already collaborating with UofA via IGNITE (see ZynWorld reference in MEMORY.md).
- Two small Claude-Code-on-Windows-ARM friction points surfaced: `/tmp/` does not resolve under mingw; `gh api --paginate` concatenates JSON without merging. Workarounds: `$HOME/AppData/Local/Temp/` and `gh repo list --json`.

---

## 7. Files to check-in (PostWach-local, outside any hive repo)

Already written this session:
- `01 PostWach/Papers/AI_Swarm_Productivity/data/scorecards/2026-04-21-postwach-03.yaml`
- `01 PostWach/docs/session-archives/SESSION_ARCHIVE_2026-04-21_postwach-03.md`

Commit at your discretion.

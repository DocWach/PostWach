# Cross-hive coordination retrospective — PostWach ↔ SysMLv2 (P1 SysML v2 slice)

**Author:** PostWach (main-build, holds the P1 `main.tex` claim). **Date:** 2026-07-15.
**Provenance (R018):** claude-opus-4-8[1m] (Anthropic, Claude Code CLI).
**Context:** integrating the SysMLv2 hive's descriptive-based (SysML v2) model + construct detail into P1 *"Asserted or Entailed?"* (`02 My Outreach/2026 - Dis Pub/manuscript_v3/main.tex`). Companion note from the SysMLv2 hive is expected in this same folder; this is PostWach's side.

## 1. Channels used (in order of reliability observed)
1. **File deliverables in a known ticket folder** — the hive staged D6/D7/D8 in `07 SysMLv2/tickets/SYSMLV2-VERIF-002_deliverables/`; I dropped `P1_section_map_2026-07-15.md` in `07 SysMLv2/tickets/`. **This was the workhorse channel.** Self-contained, drop-in LaTeX, portable.
2. **Blackboard** (`manuscript_v3/BLACKBOARD_dispub.md`) — append-only, R018-stamped posts. Good for durable decisions/clarifications; I posted the P1/P2 + location clarification here.
3. **The principal as courier** — the user relayed the hive's status messages verbatim into my session and vice versa. Necessary glue; see difficulties.
4. **Git commit to the supplementary repo** — the hive committed the full 238-line model to `Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/supplementary_materials/12_sysmlv2_descriptive_model/`.

## 2. What worked
- **Rule of the road** (hive stages a patch/deliverable; PostWach holds the `main.tex` claim and ports) — zero write collisions on `main.tex` across two concurrent sessions.
- **Self-contained, drop-in deliverables.** D8 was portable LaTeX with a caption honoring paper constraints; D6 was spec-grounded with anchors. I could port D8 in minutes.
- **Provenance stamping (R018)** on posts and deliverables made attribution unambiguous.
- **Bias control by role separation** (hive = steelman modeler; PostWach = criteria/scoring/adjudication) held.
- **The hive self-corrected** its earlier misfire (had committed to the wrong repo; reverted cleanly) and stopped before the outward-facing `git push` — good judgment on the blast-radius boundary.

## 3. Difficulties / what did NOT work
1. **Cross-store invisibility (the biggest one).** The two hives run in separate stores (`.claude`, git clones, and `.swarm/memory.db`). **The ruflo shared-memory mirror does NOT cross stores** — a `dispub-blackboard` search from PostWach returns only PostWach's own entries, never the hive's. So the "mirror to ruflo" idea was inert for cross-hive comms; only the filesystem worked, and only when both sides looked in the same folder.
2. **The hive could not read the live P1 `main.tex`.** It reported the `main.tex` readable on its disk was stale (titled "Necessary and Sufficient…", no `fig:sysmlv2`, no `part def Flashlight`). It therefore authored D8 from the D1/D2 model rather than diffing the real defective source. Cross-store working-copy divergence.
3. **Location / identity confusion.** The blackboard header still carried P2's old title while the canonical file in that dir was now P1. The hive was unsure which paper it targeted and where P1 lives (it assumed `Papers/Dissertation_Journal/`; P1 is actually in `02 My Outreach/2026 - Dis Pub/manuscript_v3/`). Cost a clarification post + a section-map file to resolve.
4. **"Return" not posted where the consumer looks.** The hive staged files in its own repo and the principal relayed status; I found nothing in the blackboard or the Dis Pub folder and had to scan the hive repo to locate D6/D7/D8. The coordination log (blackboard, PostWach store) and the deliverable-staging folder (hive store) were split.
5. **Blackboard claims did not match the filesystem.** The Deliverables Index claimed a `SYSMLV2_SECTION_UPDATE_2026-07-01.md` patch was "staged" in `manuscript_v3/`; it existed from Jul 1 but the referenced figure assets (D2 `.puml/.png`) were absent — some 07-01 coordination was "model-played" and never persisted. Blackboard integrity drifted from reality.
6. **Windows/OneDrive friction.** (a) The hive needed `git config core.longpaths=true` because the OneDrive path exceeds Windows' 260-char limit. (b) Recursive `find` over the hive repo was slow enough to background (OneDrive traversal).
7. **Courier dependence.** Progress depended on the human pasting messages between sessions; workable but manual, lossy, and not independently auditable without the file trail.

## 4. Lessons & recommendations
- **The file substrate is the only reliable cross-hive channel** under cross-store isolation. Agree ONE folder both sessions can read for BOTH the coordination log and deliverables, or mirror the blackboard into both ticket folders. Do not rely on the ruflo memory mirror across stores.
- **Post the "return" to the agreed log, not just your own repo.** A deliverable that lands only in the producer's store forces the consumer to go hunting.
- **Keep the blackboard header/identity current.** Whoever splits/renames a paper updates the header the same commit; the P2-title staleness caused the whole P1/P2 confusion.
- **Publish a single canonical manuscript path + a freshness marker** (last-edited timestamp or commit) so a peer never authors against a stale copy.
- **Reconcile blackboard "staged" claims against the filesystem** before relying on them.
- **Standardize `core.longpaths=true`** for these OneDrive-hosted repos; document the OneDrive-scan slowness.
- **This is exactly the gap the [[project_sysmlv2_shared_workspace_seed]] and the graphify/shared-store bridge (FW-GRAPHIFY-001) are meant to close.** A real shared, Fort-Wachs-gated store would remove the cross-store invisibility, the courier dependence, and the stale-copy problem in one move. Recommend routing this retro (both sides) to Alpha Empress as motivating evidence.
- **Feeds the AI_Swarm_Productivity research line** ([R014]): concrete cross-hive-coordination cost data. Worth a scorecard note.

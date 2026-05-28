# Session Archive — 2026-05-28 postwach-02

> Seq note: scorecard 01 is the talk-delivery wrap session; this MTA-Workbench review session is filed as 02 to stay paired with scorecard 02. The two sessions are independent (this one ran ~T-1h12m before the 10:05 ET talk; the wrap ran after).

**Hive:** PostWach
**Scope:** Pre-STIDS-talk review of `DocWach/MTA-Workbench` (David Kamien's Mission Thread Authoring Workbench) at urgent time pressure (~1h12m before David + Paul's 10:05 ET STIDS presentation). Warm up ruflo, spin parallel subagents, deliver a severity-ranked, externally-clean talking-points brief covering security, code quality, and architecture.
**Platform:** Ruflo v3.7.0-alpha.14 (MCP running, PID 53596, stdio); claude-opus-4-7 (1M context); Windows 11. Three native Claude Code subagents (security-auditor, code-analyzer, system-architect) running concurrent backgrounded reviews against a fresh shallow clone.
**Outcome:** Brief delivered ~50 min before talk. 3 CRITICAL findings (unauthenticated SPARQL/graphs/debug routes), strong architectural strengths to lead with (named-graph isolation, gated reasoner, server-enforced FSM), honest gap-owning language drafted for the URDNA2015 / dual-provenance / keyless-chain caveats. No code changes to MTA-Workbench (this is external code; Paul co-presents only).

---

## 1. Entry state

User invoked at T-1h12m to the STIDS talk with: "MTA workbench. Warm up ruflo and review code below. https://github.com/DocWach/MTA-Workbench". Memory already noted a prior 2026-05-26 feedback package assembled at `02 My Outreach/2026 STIDS/MTA code/Code_feedback_2026-05-26/` and awaiting Paul's go to send to David; this session was a fresh independent review against the latest main (commit `49d4006`), not a rehash of that package.

---

## 2. Approach

Repo not present locally (OneDrive sync didn't have `02 My Outreach/`). Decision: shallow-clone to `/tmp/mta-review/MTA-Workbench` (outside the project tree per [R104]), survey structure, then run three concurrent subagents with tight ~12-min budgets and STIDS-presentation framing in each prompt. No coordination/handoff between them — they reviewed independently. Synthesis happened in the orchestrator turn after all three reported.

Time discipline: no second pass, no follow-up questions to agents, no extra exploration. Cleared agent backlog in <25 minutes total wall.

---

## 3. Execution

- Cloned MTA-Workbench (commit `49d4006`, ~9.3k Python + ~8.3k TS, 19 backend services, 97 pytest cases, Replit-hosted, pnpm workspace + uv venv).
- 3 backgrounded subagents launched concurrently:
  - `security-auditor` — secrets, fail-open posture, auth gaps, audit-chain integrity, ZT Pillar 7 mapping.
  - `code-analyzer` — service coupling, error handling, determinism discipline, test gaps, dep hygiene.
  - `system-architect` — T-Box/A-Box separation, reasoner placement, multi-tenancy, export determinism, FSM enforcement, mock-auth pluggability, vendor-readiness.
- All three completed first-pass with zero rework. Architecture finished first (~70s), code-quality second (~99s), security last (~130s).
- Orchestrator synthesized into a single severity-ranked brief: strengths-first (talk-safe), then 3 CRITICAL must-fix-before-demo items, then v1.1 hardening backlog, then STIDS talking points + ZT Pillar 7 framing + one-line summary for David.

---

## 4. Findings (durable, externally clean)

**Strengths (lead with these):**
- **Named-graph tenant isolation** (`mto://tbox`, `mto://shapes`, `threads://<tenant>/<id>`, `prov://<tenant>/<id>`) with SPARQL PREFIX expansion before authorization — catches the prefixed-name bypass most pyoxigraph wrappers miss.
- **Reasoner gated + cached**, not continuous: HermiT runs only on explicit request or Stage B→D exit guard, keyed `(tenant, T-Box SHA-256)`, 24h TTL, auto-invalidate on T-Box change.
- **Server-enforced FSM** from a frozenset; production refuses to boot with bypass flags set.
- **Deterministic-export discipline is real for the frozen-snapshot encoding** — `sort_keys=True` + per-node triple sort `(p, canonical(o))` consistently across all five emitters; audit chain normalizes timestamps before hashing.
- **README is honest about v1.0 gaps** (OIDC, IL-4, STIG).

**CRITICAL (must-fix before any external demo):**
1. `backend/app/api/v1/sparql.py:21-29` — `POST /api/v1/sparql` has no auth dep; tenant hardcoded `"demo"`. Unauthenticated SPARQL.
2. `backend/app/api/v1/graphs.py:26-43` — `GET /api/v1/graphs/{uri}/serialization` likewise unauthenticated; will dump any demo-tenant graph.
3. `backend/app/api/v1/validation.py:135-167, 189-225` — `/debug/.../break` and `/repair*` mutate the triplestore with no auth dep, no `MTA_ENV` gate. Live SHACL-violation injectors exposed in any deployment.

**HIGH (v1.1 backlog — own the gap, not hide it):**
- CORS wildcard in `main.py:30-36` compounds the unauthenticated routes into browser-readable data leak.
- Fail-open env gating: `validation_report_service.py:32, 42-50` and `state_machine.py:44-56` only block when `MTA_ENV == "production"` *exactly*. Unset / `"prod"` / typo lets bypasses through. Invert: require explicit `MTA_ENV=dev` to enable bypasses.
- Dev HMAC key committed in source (`validation_report_service.py:32`).
- **URDNA2015 gap.** "Byte-deterministic export" is sorted-N-Triples on the frozen `rdf_dump`, not graph canonicalization. Two semantically equivalent graphs with different bnode labels hash differently. A Stardog/AnzoGraph engineer lands on this in 30 seconds.
- **Keyless audit chain** (`audit_service.py:79-103`): SHA-256 over canonical JSON, no HMAC, no external anchor. Tamper-evident vs accidents, not adversarial DB.
- **Dual provenance overlap**: PROV-O in `prov://` named graphs + SHA-256 chain in Postgres, no documented join key.
- **Silent failures**: 6 bare `except: pass` in `telemetry_service.py` zero out metrics on SPARQL failure; `reasoner_service.py:150` silently downgrades inferred → asserted; `export_service.py:530` silently drops per-node provenance.
- **Mock-auth coupling**: `X-Mock-User` read directly in `get_current_user` Depends, not behind an `AuthProvider` interface.
- **Dep lower-bounds only** in `pyproject.toml`; pin `owlready2` exactly (HermiT behavior shifts between point releases) to protect determinism claim.
- **Missing dedicated tests** for highest-stakes services: no `test_export_determinism.py`, `test_audit_chain_tamper.py`, etc.

**STIDS talking points for the room:**
1. T-Box / SHACL / SKOS / per-tenant A-Box separated as named graphs; structural read enforcement with SPARQL prefix expansion before authorization.
2. OWL DL reasoner gated + cached per (tenant, T-Box SHA-256); not continuous.
3. Transitions server-enforced from frozenset; prod refuses to boot with bypass flags set.
4. Exports byte-stable on the frozen snapshot via sorted N-Triples — would lift to URDNA2015 before publishing the canonicalization claim externally.
5. Provenance is dual-layer (PROV-O semantic + SHA-256 chain audit); bridging is open work.

**ZT Pillar 7 framing** (if defense-leaning Q&A): strong on intent (hash-chained audit, HMAC certs, coverage triple), weak on integrity (keyless chain; unauthenticated SPARQL/graphs/debug routes bypass the audit-logged paths). Lead with cert + coverage; flag the gaps as v1.1.

**One-liner for David:** *"Architecture and determinism discipline are sound; the gap is at the API edge — three routes ship without auth, the env gating is fail-open by default, and the 'deterministic export' claim should be narrowed to the frozen snapshot until URDNA2015 lands."*

---

## 5. Files touched

- `docs/session-archives/SESSION_ARCHIVE_2026-05-28_postwach-02.md` (this file).
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-05-28-postwach-02.yaml`.
- No PostWach portfolio code modified. MTA-Workbench clone at `/tmp/mta-review/MTA-Workbench` (~17.6k LoC source, deletable; shallow clone of an external repo).

---

## 6. Open items / next session entry

1. Decide whether to send today's brief to David, or pair it with the prior 2026-05-26 feedback package (memory entry: `02 My Outreach/2026 STIDS/MTA code/Code_feedback_2026-05-26/`). Likely consolidate before sending — three CRITICAL items here are independently actionable.
2. Talk follow-through: confirm post-talk whether any of the strengths/talking points were used in the room; record reaction signal from STIDS audience to MTO architecture.
3. Decide whether MTA-Workbench review becomes a recurring service to David's team (would create cross-hive capability load), or one-shot for the talk.
4. Clean up `/tmp/mta-review/` after handoff is sent.

---

## 7. Reusable notes

- **Time-boxed parallel-subagent pattern under hard deadline:** clone, structure-survey, then 3 narrow-scope agents (security / quality / architecture) backgrounded with explicit per-agent word budgets, no inter-agent coordination, synthesis in the orchestrator turn after all report. Total wall ~25 min from cold start to delivered brief. Useful template for any "T-minus-N urgent external code review" task.
- **Externally-clean framing scaffold:** lead-with-strengths → severity-ranked findings → talk-ready bullets → one-liner for author. Critical items are reported as plain facts with file:line; not as failures. Same scaffold reusable across future external reviews (David's team, other STIDS collaborators).
- **Vendor-readiness lens** ("biggest risk if shown to a graph-DB vendor") in the architect prompt directly surfaced the URDNA2015 caveat that a Stardog/AnzoGraph engineer would catch in 30 seconds. Worth retaining for any presentation-prep code-review task where the audience includes likely commercial competitors.
- **ZT Pillar 7 mapping** in the security prompt produced a story that pairs cleanly with PostWach's broader Fort Wachs / NSA ZT framing (see MEMORY index) — strong-on-intent / weak-on-integrity dichotomy is reusable for any defense-audience semantic-tech talk.

---

PROVENANCE: Claude Opus 4.7 (model id `claude-opus-4-7`, 1M context), Claude Code agent mode, session 2026-05-28-postwach-02. Three subagents (`security-auditor`, `code-analyzer`, `system-architect`) inherited the same foundation model. Per [R018].

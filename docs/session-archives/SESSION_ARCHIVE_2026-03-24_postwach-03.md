# Session Archive: 2026-03-24 PostWach-03

**Date:** 2026-03-24
**Hive:** PostWach
**Focus:** IGNITE demo prep for NNSA meeting

---

## Session Summary

Quick session to launch the two IGNITE demo apps and the VT Supply Chain app for an upcoming NNSA meeting. Killed a stale Streamlit process from the previous session that was blocking port 8501, then started all three apps.

## Apps Running

| App | URL | Source |
|-----|-----|--------|
| UAOS Dashboard (Joe Gregory) | http://localhost:8000 | `05 IGNITE/UAOS_DashboardPrototype/backend/` (uvicorn) |
| IGNITE Streamlit | http://localhost:8501 | `05 IGNITE/IGNITE_Disruption_2026/src/app.py` |
| VT Supply Chain | http://localhost:8503 | `01 PostWach/VT Supply Chain/src-repo/src/app.py` |

## Issues Encountered

- Port 8501 was occupied by a stale Streamlit process (PID 32696) from the previous session. Killed and restarted.

## Decisions

- None. Operational session only.

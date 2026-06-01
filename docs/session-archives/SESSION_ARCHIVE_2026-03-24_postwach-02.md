# Session Archive: 2026-03-24 PostWach-02

**Date:** 2026-03-24
**Hive:** PostWach
**Focus:** VT Supply Chain — Ollama LLM integration, Streamlit testing, repo updates

---

## Session Summary

Set up Ollama with Llama 3.1 8B as the local LLM provider for the VT Supply Chain Disruption Analyzer. Verified end-to-end pipeline (classify, simulate, analyze, risk assess) running locally against Ollama. Fixed pyarrow incompatibility on ARM64 Windows. Updated the GitHub repo README with complete project documentation, Mermaid architecture diagram, and student setup instructions. Generated a hash-locked requirements file for Chainguard supply chain security review.

## Deliverables

| # | Deliverable | Location | Status |
|---|-------------|----------|--------|
| 1 | Ollama v0.18.2 installed | `C:\Users\pfwac\AppData\Local\Programs\Ollama\` | Complete |
| 2 | Llama 3.1 8B model pulled | `C:\Users\pfwac\.ollama\models\` (4.9 GB, Q4_K_M) | Complete |
| 3 | pyarrow fix (markdown table rendering) | `src/app.py` | Complete |
| 4 | README overhaul | `README.md` | Complete |
| 5 | Hash-locked requirements | `requirements.in`, `requirements.lock` | Complete |
| 6 | .gitignore | `.gitignore` | Complete |

## Commits (DocWach/Supplychain-Analysis-VT-ISE-Senior-Design)

| Hash | Message |
|------|---------|
| `2a80c93` | Add Ollama + Llama 3.1 as recommended local LLM, fix pyarrow dependency |
| `04f75d8` | Update README: complete project structure, 6 strategies, architecture diagram |
| `bcd4d10` | Add hash-locked requirements file for supply chain integrity |

## Key Decisions

1. **Ollama over cloud providers** for student default — free, local, no API keys, no data leaves machine
2. **Llama 3.1 8B** as target model per Oct 28 planning meeting ("Llama 13B" mapped to closest available)
3. **Markdown tables** instead of `st.dataframe`/`st.table` to bypass pyarrow dependency (no ARM64 Windows wheels, may affect other platforms too)
4. **Separate requirements.in/requirements.lock** pattern for Chainguard — human-editable source vs auto-generated hash-verified lock file
5. **ortools and eval deps kept optional** since they lack wheels on some platforms

## Issues Encountered

- **pyarrow has no ARM64 Windows wheels** — `st.dataframe` and `st.table` both depend on it in Streamlit 1.53+. Resolved by rendering tables as markdown.
- **Ollama not on Git Bash PATH** — installer puts it in AppData; had to use full path initially. Works fine from Windows terminals.
- **ortools no ARM64 wheels** — excluded from lock file, kept as optional extra with scipy as fallback.

## Pipeline Test Results (Ollama + Llama 3.1 8B)

- **Provider detection:** auto-detected Ollama, correctly deprioritized unconfigured cloud providers
- **Classification:** correctly identified SUPPLIER_FAILURE for Russian sanctions scenario, clean JSON output
- **Full pipeline:** all 4 stages completed (classify, simulate, analyze, risk assess)
- **Response quality:** coherent, well-structured, followed system prompt format. Duration estimates varied between runs (expected LLM behavior).

## Next Steps

- Run evaluation harness against ground truth scenarios to measure classification accuracy
- Cross-provider comparison (Ollama vs Groq vs Cerebras) for output quality benchmarking
- Streamlit app refinements based on student feedback
- IGNITE mastery dashboard also needs pyarrow fix (same Streamlit version, same issue)

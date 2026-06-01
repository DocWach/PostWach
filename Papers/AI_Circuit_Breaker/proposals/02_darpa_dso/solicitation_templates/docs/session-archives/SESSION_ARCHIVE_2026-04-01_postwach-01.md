# Session Archive: 2026-04-01 PostWach-01

**Date:** Tuesday, 2026-04-01
**Hive:** PostWach (CTO)
**Duration:** ~2.5 hours
**Branch:** `main`

## Context

AI Circuit Breaker project review and DARPA DSO BAA exploration session. DARPA CLARA proposal was officially skipped (timeline unfeasible). Session pivoted to identifying next funding targets and preparing for DSO Office-Wide BAA submission.

## Accomplishments

### 1. DARPA CLARA Decision Recorded
- Officially marked CLARA (DARPA-PA-25-07-02, Apr 17 deadline) as SKIPPED
- Updated `AI_Circuit_Breaker_Grant_Programs.md` (CLARA entry, postdoc eligibility list, Top 5 priorities)
- Updated `AI_Circuit_Breaker_Contract_Funding.md` (priority action list renumbered)
- Updated memory (`circuit-breaker-details.md` funding deadlines and next steps)

### 2. Funding Landscape Reassessment
- Agent-based scan of upcoming 2026 opportunities
- Confirmed existing curated lists in Grant_Programs.md (28 opportunities, 4 tiers) and Contract_Funding.md (rolling BAAs, OTAs, IC programs) are comprehensive
- New Top 5 priority: DSO BAA > NIST MSE > NSF CPS > NSF SaTC > ONR
- Agent also surfaced Schmidt Sciences Trustworthy AI RFP and NeurIPS 2026 (not yet verified)

### 3. SERC AI4SE/SE4AI Workshop 2026 Abstract Drafted
- Workshop: Sep 22-23, 2026 at GWU, Washington DC
- Deadline: Jun 5, 2026 (3-page extended abstract)
- Track: SE4AI (trust measures, safety/reliability/ethics)
- Bonus: auto-considered for Systems Engineering journal special issue (Wiley/INCOSE)
- ~300-word lead abstract drafted; needs expansion to 3-page extended format

### 4. Jeffrey's New Documents Reviewed
- "Morphism Assurance (Master Composition Document)" (v1.4, Jeffrey Wallk): modular proposal content system with 4 tiers, 9 technical blocks, 4 submission shells
- "5 Dimensions of Relevancy": WHO/WHAT/WHEN/WHERE/WHY as first-class assurance signals
- Both files moved from Downloads to `Papers/AI_Circuit_Breaker/`
- Critical terminology conflicts identified: phi vs sigma, d_S vs sigma, d_M vs D, product vs min/additive composition bounds, 7-tuple vs 5-tuple Wymore, CBTO not mentioned
- 5D extension has valuable ideas (MTBH stratification, dimensional sanitization) but needs formal r_i(q) definitions and SPC integration

### 5. DARPA DSO BAA Deep Exploration (HR001125S0013)
- Solicitation verified: deadline Jun 2, 2026 at 4:00 PM ET (confirmed, no changes since Amendment 01)
- All 4 thrust areas analyzed; Thrust 4 ("Complex, Dynamic, Intelligent Systems") scored 9/10 fit
- DSO PMs identified: Benjamin Grosof (highest relevance, manages CLARA + CODORD), Yannis Kevrekidis (secondary), Greg Witkop (bio-regulation)
- Submission process clarified: informal PM outreach first, then formal Exec Summary via BAAT
- Downloaded Attachments A, B, C, E to `proposals/02_darpa_dso/solicitation_templates/`
- Confirmed format: Exec Summary = 2pp (1 cover + 1 technical, 4 Heilmeier Qs), Abstract = 5pp, Full Proposal = 20pp

### 6. Executive Summary Draft Corrections
- Fixed title: "Postdoctoral Research Associate" corrected to "Researcher, Systems Engineering & AI"
- Fixed citation: "ASME IDETC 2024" corrected to "CSER 2025"
- Fixed domain: "Telecom industry" corrected to "Clinical ECG monitoring"

### 7. Routing Email Drafted
- Draft email to HR001125S0013@darpa.mil requesting PM routing for Thrust 4
- Leads with bio-inspired homeostatic mechanisms hook

## Files Created
- `Papers/AI_Circuit_Breaker/proposals/02_darpa_dso/solicitation_templates/` (4 DARPA templates: A, B, C, E)
- `Papers/AI_Circuit_Breaker/Morphism Assurance (Master Composition Document).docx`
- `Papers/AI_Circuit_Breaker/5 Dimensions of Relevancy .docx`
- `memory/user_role.md`

## Files Modified
- `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Grant_Programs.md`
- `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Contract_Funding.md`
- `Papers/AI_Circuit_Breaker/proposals/02_darpa_dso/dso_executive_summary.md`
- `memory/circuit-breaker-details.md`

## Open Items for Next Session
1. Send routing email to HR001125S0013@darpa.mil
2. Compress exec summary into Attachment A format (4 Heilmeier Qs, 1 page)
3. Terminology reconciliation session with Jeffrey (phi/sigma/d_S conflicts)
4. Expand SERC AI4SE abstract to 3-page extended format (Jun 5 deadline)
5. UA Sponsored Projects engagement for SAM.gov UEI, CAGE code, Admin POC
6. Verify Schmidt Sciences and NeurIPS deadlines if targeting May submissions
7. STOIC ontology stack remains overdue

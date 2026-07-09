# Session Archive — 2026-06-30 postwach-02

> PROVENANCE: claude-opus-4-8[1m] (Anthropic, Claude Code CLI) ran this session: reviewed the Prescott DEF
> request, inventoried portfolio resources, web-researched current Secretary of War acquisition keywords,
> mined the local DEF publication corpus (via one background subagent), debated and proposed an outline,
> drafted the one-pager, and rendered it to docx. ruflo/claude-flow (v3.14.4) warmed at start (MCP surface
> live); NOT used for orchestration. ONE background subagent (general-purpose) spawned via the Claude Code
> Task tool, not a claude-flow swarm: DEF-corpus extraction (13 PDFs via pypdf). Tooling: python-docx,
> WebSearch/WebFetch, Python PDF extraction. No manuscript bibliography rendered (R019 n/a). No commits this
> session.

**Hive:** PostWach (CTO / Chief Scientist). **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m]. **Status:** HOLD (awaiting Alejandro).

**Headline:** Produced a one-page capabilities brief for the University of Arizona Digital Engineering
Factory (DEF), responding to a sponsor question (relayed by Alejandro Salado) demanding specifics, what
vendors, licenses, workflows, and research, and why UA is superior to any other academic institution for
MOSA and systems engineering, in the Secretary of War's acquisition vocabulary. The prior draft "did not
make the cut" because it was all aspiration and zero specifics. Fix: led with verifiable, corpus-sourced
specifics anchored on the genuine differentiator (a user-controlled, vendor-neutral semantic hub plus a
DoD-policy-compliant digital TEMP), in current Warfighting Acquisition System (WAS) keywords. Draft sent to
Alejandro; holding.

Working folder: `03 Projects/98 Proposal Phase/07 Prescott`.

## 1. The ask (Salado email, 2026-06-30 16:44, to Joe Gregory + Paul Wach)
- One-pager answering a sponsor: "what does the DEF include... what vendors, what licenses, what workflows,
  what research? ...why your facility (and mission) is superior compared to any other academic institution"
  for MOSA + SE. "It is critical that we use the keywords that the Secretary of War uses." For Prescott.
- Email referenced an "attached briefing for context," but the ONLY attachment was the draft docx itself;
  the briefing was not in the folder (gap noted, then de-scoped by principal).
- Principal corrections during the session: (1) web-research current SecWar keywords, do not rely only on
  cached stack; (2) the 2018 DoD DE Strategy is severely outdated, drop it; (3) pull specifics ONLY from the
  local DEF folder to stay honest; (4) MACQ and SysMLv2 are internal hives, NOT part of the DEF, exclude.

## 2. SecWar keyword bank (web-verified this session)
- Governing 2026 artifact: **Warfighting Acquisition System (WAS) Memo** (Hegseth, 2025-11-07),
  "Transforming the Defense Acquisition System into the Warfighting Acquisition System to Accelerate Fielding
  of Urgently Needed Capabilities to Our Warriors"; companion Acquisition Transformation Strategy (5 pillars);
  DoW AI Strategy (2026-01-09, MOSA mandate for AI).
- Verbatim vocabulary used: speed to capability; speed of relevance; **Modular Open Systems Approach (MOSA)**,
  maximize use; module-level competition; reduce vendor lock; commercial-first; nontraditional vendors;
  strengthen the industrial base; wartime footing; Capability Portfolio Management.
- Five WAS pillars: Rebuild the Industrial Base; Empower the Acquisition Workforce; Maximize Flexibility
  through Reduced Regulations; Develop High-Performance Systems; Improve Life-Cycle Risk Management.
- Strategic hinge: MOSA is simultaneously the sponsor's requested theme, a named WAS keyword, and the DoW AI
  mandate, and the DEF is honestly built on open standards. That alignment became the one-pager's spine.
- Sources: war.gov release (403 to fetch, used summaries); Holland & Knight; Inside Government Contracts.

## 3. DEF corpus mined (the honest source) — `04 Resource Library\DEF Materials`
Gregory & Salado DEF publication corpus 2023-2025 (~30 PDFs across CESUN, CSER, GPDIS, AIAA SciTech, ASEE,
IAC, IEEE Aerospace, INCOSE IS, Integrate, LEAD, OntoNexus, SECESA, Stratdec, Zuken IW; a Journal Articles
folder; 3 demo videos). Background subagent extracted 13 priority PDFs cleanly. Key honest facts:
- **Semantic hub:** Violet (Violet Labs, evaluation license), chosen over 11 surveyed commercial platforms
  (Siemens Teamcenter, PTC, Aras, Ansys, Intercax Syndeia, eQube, etc.) because it lets UA impose its OWN
  ontology. **Open-source backbone:** OpenCAESAR / OML / OML Rosetta (RDF, OWL 2 DL, SPARQL).
- **Spoke tools (named):** Jama Connect (reqs), Cameo Systems Modeler + Teamwork Cloud and SysML v2
  (Jupyter ref impl, SysON), Duro (BOM), Jira, GitLab, OpenMBEE (MMS/MDK/COMODO), Visual Studio + Klocwork,
  Python/MATLAB, Sedaro/SatCatalog. Under development: MATLAB, SolidWorks, Kiwi TCMS integrations.
- **Infra:** on-prem cluster (320 CPUs, ~100 TB), scalable to thousands; FERPA/ITAR/IP-compliant.
- **Workflow:** hub-and-spoke pull into Violet -> OML graph -> RDF triple store -> validate vs UA Ontology
  Stack (closed-world reasoning catches missing/illegal relations) -> publish via Violet/GitLab/OpenMBEE ->
  SPARQL query for review/grading. Known limit: one-way pull; push back to source not yet implemented.
- **dTEMP:** nine modular ontologies encoding DoDI 5000.89; validated on a sanitized real DoD TEMP (LMMDR),
  13,042 triples; peer-reviewed in *Systems Engineering* (Wiley, 2024). The strongest differentiator.
- **Research:** UA Ontology Stack (BFO + Common Core + PROV-N); Bayesian verification (spacecraft ADCS);
  orbital verification; DECF competency mapping (382/1228 KSABs, 31.1%); semantic dashboards.
- **Case studies (space-heavy, good fit):** LEO satellites, CubeSat deorbit, Mars rover, NoraSat transmitter
  tradespace (Jama + SysML v2 + Sedaro + Python), spacecraft ADCS, DoD mine-detection (dTEMP).
- **Maturity (R016):** research-and-education environment, validated on notional/sanitized/student cases;
  a validated method, not a turnkey production line. Funding: TRIF; dTEMP funded by OUSD(A&S)/(R&E),
  HQ0034-19-D-0003 TO #0510.
- Honest negatives: NO Protege, GraphDB, Capella, AFSIM, Windchill, or named Bayesian package in corpus, do
  not attribute. Hypersonics and Space Situational Awareness (in the prior draft) are NOT supported, dropped.

## 4. Decisions (principal-confirmed)
- Superiority carried by **verifiable specifics**, not rhetorical reach (R016-safe).
- **Hypersonics and SSA dropped** (unsupported by corpus); led with real space/spacecraft case studies.
- Outline backbone mirrors the sponsor's four literal questions (vendors/licenses, workflows, research,
  what-sets-apart), each framed around the vendor-neutral-open-thread differentiator and a MOSA x WAS closer.

## 5. Artifact produced
- **`UArizona_DEF_MOSA_OnePager_v1.docx`** (in `07 Prescott`), built with python-docx (no Word COM, per
  standing rule). ~608 words, one page; Calibri 10.5, 0.6/0.7in margins; navy title + accent section labels,
  bold tool names, bulleted. WAS keywords verbatim; abbreviations defined at first use; no em dashes;
  maturity stated honestly. Generator script kept in system temp (not committed), repo left clean.

## 6. Open / next (HOLD)
- **Holding for Alejandro / Joe.** Draft sent by principal to Alejandro; awaiting feedback.
- **Confirm with Joe before sponsor sees it:** the 320-CPU / ~100 TB figures and Violet evaluation-license
  status (corpus-sourced from 2024 papers; verify still current).
- **De-scoped this session:** the missing "briefing for context"; the "Prescott" venue/audience/sponsor
  question. Revisit if the request resumes.
- Optional: a one-paragraph cover note for Alejandro's reply (offered, not yet written).
- Untouched corpus folders (CESUN, 2023/2025 CSER, Integrate, LEAD, OntoNexus, SECESA, Stratdec, Naval
  Engineers Journal) judged duplicative; sweep only if more vendor detail is needed.

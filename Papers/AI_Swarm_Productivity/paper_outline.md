# Measuring Productivity in AI-Swarm-Augmented Systems Engineering Research

## Working Title
"Measuring Productivity in AI-Swarm-Augmented Systems Engineering Research:
A Multi-Dimensional Framework and Longitudinal Action Study"

## Status
- **Started:** 2026-03-03
- **Phase:** Literature review + data collection instrument design
- **Data collection:** Active from 2026-03-03
- **Target venues (in order):**
  - Workshop/short paper: CSER 2027 (submission ~Sep 2026, 6 months data)
  - Full conference: ESEM 2027 or ICSE SEIP 2027 (submission ~Dec 2026, 9-12 months data)
  - Journal: EMSE, JSS, or IEEE Software (submission ~Mar 2027, 12+ months data)

## Research Questions
- **RQ1:** What dimensions of productivity are relevant when a human researcher
  orchestrates multi-agent AI swarms to produce heterogeneous SE research artifacts?
- **RQ2:** How does swarm-augmented productivity compare to traditional (unaugmented)
  methods across different artifact types (papers, ontologies, code, analyses)?
- **RQ3:** What factors moderate the productivity effect (task complexity, swarm topology,
  artifact type, agent count)?

## The Gap
Every existing framework measures ONE of:
1. Human developer productivity with AI copilot (SPACE, DORA, Copilot studies, METR)
2. AI agent system performance in isolation (CLEAR, SWE-bench)
3. Academic research output (bibliometrics, h-index)

No framework measures productivity of a human researcher orchestrating multi-agent
AI swarms producing heterogeneous research outputs.

## Paper Structure

### 1. Introduction
- AI-augmented SE research is growing but lacks measurement frameworks
- Existing metrics designed for either pure-human or pure-AI contexts
- Gap: human + multi-agent swarm + research artifacts

### 2. Related Work
#### 2.1 Developer Productivity Frameworks
- SPACE (Forsgren et al., 2021) — 5 dimensions, no AI/agent dimension
- DORA 2025 — CI/CD metrics, AI amplification paradox
- SPACEX extension (arxiv 2511.20955)
- GQM (Basili & Weiss, 1984) — metric derivation methodology

#### 2.2 AI-Assisted Development Studies
- GitHub Copilot RCT (Peng et al., 2023) — 55.8% faster, constrained task
- Microsoft/Accenture field study — 12.9-21.8% more PRs/week
- METR RCT (2025) — 19% SLOWER for experienced devs, perception bias
- Google internal (2025) — 21% faster, contradicts METR
- Faros AI Paradox — individual gains, flat org throughput

#### 2.3 Agentic AI Evaluation
- CLEAR framework (arxiv 2511.14136) — Cost, Latency, Efficacy, Assurance, Reliability
- SWE-bench/Pro — resolve rate, limitations (code-only, test-dependent)
- Beyond Task Completion (arxiv 2512.12791)

#### 2.4 Academic Research Productivity
- Bibliometrics and h-index critiques
- AI impact on research quality (Springer Nature 2025)
- Calls for standardized AI-augmented research protocols

#### 2.5 Research Methodology
- Action Research in SE (Staron, 2020) — cyclic, researcher-as-practitioner
- Case study methodology in empirical SE (Runeson & Host, 2009)

### 3. Framework Design
- GQM derivation: 3 goals → questions → metrics
- Four dimensions: Output Volume, AI Efficiency, Quality Gates, Process Health
- Derived comparative ratios (pages/hr, cost/artifact, agent utilization)
- Relationship to SPACE (extends S, P, A, E; adds AI-specific dimensions)
- Relationship to CLEAR (adapts C, L, E, A, R for human-AI collaboration)

### 4. Action Research Design
- Setting: 8-hive research portfolio, University of Arizona
- Data collection: per-session YAML scorecards
- Baseline: pre-swarm sessions (Jan-Feb 2026) as historical comparator
- Duration: 6-12 months (Mar 2026 onwards)
- Threats to validity: N=1 researcher, self-report bias (METR warns), Hawthorne effect

### 5. Results
- Cross-hive comparison (8 hives, different artifact types)
- Temporal trends (does productivity improve as swarm skills mature?)
- Artifact-type analysis (papers vs ontologies vs code vs analyses)
- Cost-effectiveness analysis
- Where swarms help vs. where they don't

### 6. Discussion
- Comparison to Copilot studies / METR findings
- Implications for SE research practice
- Framework generalizability
- METR perception bias — do we observe it too?

### 7. Threats to Validity & Limitations

### 8. Conclusion & Future Work

## Key References (Starter List)
1. Forsgren et al. (2021). "The SPACE of Developer Productivity." ACM Queue.
2. DORA (2025). "State of AI-assisted Software Development." Google.
3. Peng et al. (2023). "The Impact of AI on Developer Productivity." arxiv:2302.06590.
4. METR (2025). "Measuring Impact of Early-2025 AI on Experienced OSS Dev Productivity." arxiv:2507.09089.
5. arxiv:2511.14136 (2025). "Beyond Accuracy: CLEAR Framework for Agentic AI."
6. Basili & Weiss (1984). "A Methodology for Collecting Valid Software Engineering Data."
7. Staron (2020). "Action Research in Software Engineering." Springer.
8. arxiv:2512.12791 (2025). "Beyond Task Completion: Assessment Framework for Agentic AI."
9. arxiv:2511.20955 (2025). "SPACEX: Exploring Metrics with the SPACE Model."
10. Faros AI (2025). "The AI Productivity Paradox."

## Cross-Project Connections
- SysMLv2 debugging-effort-analysis.md → retroactive data point + separate journal pub
- WRT-2516_v2 effort_report.md → retroactive data point
- SE_Math_Foundations effort_report.md → retroactive data point
- All 8 V3 hives → prospective data collection sites

# Literature Review Notes: AI Swarm Productivity Paper

**Paper:** "Measuring Productivity in AI-Swarm-Augmented Systems Engineering Research"
**Compiled:** 2026-03-03
**Citation style:** IEEE

---

## Category 1: Developer Productivity Frameworks

### Source 1: SPACE Framework

**Citation:**
N. Forsgren, M.-A. Storey, C. Maddila, T. Zimmermann, B. Houck, and J. Butler, "The SPACE of Developer Productivity," *ACM Queue*, vol. 19, no. 1, pp. 20--48, 2021. [Online]. Available: https://queue.acm.org/detail.cfm?id=3454124

**Key Findings:**
- Proposes five dimensions of developer productivity: Satisfaction and well-being, Performance, Activity, Communication and collaboration, Efficiency and flow.
- Argues that no single metric captures productivity; multiple dimensions must be measured simultaneously.
- Satisfaction includes employee retention, fulfillment, and burnout indicators.
- Performance distinguishes between outcomes (customer satisfaction, reliability) and outputs (lines of code, features shipped).
- Activity captures observable actions (commits, PRs, design documents) but cautions against using as a sole metric.
- Communication maps collaboration patterns, knowledge sharing, and information flow.
- Efficiency and flow capture uninterrupted work time, handoff minimization, and value stream delivery speed.
- Recommends capturing metrics at individual, team, and system levels.
- Validated through surveys and telemetry at Microsoft.

**Relevance to Our Paper:**
- Foundational framework; our work explicitly extends it. We map our four dimensions (Output Volume, AI Efficiency, Quality Gates, Process Health) to SPACE.
- SPACE's insistence on multi-dimensionality directly supports our multi-dimensional scorecard approach.
- Our Satisfaction dimension (perception_note field) echoes SPACE's S dimension, which becomes critical given the METR perception bias finding.
- Activity maps to our Output Volume; Efficiency maps to our AI Efficiency dimension.
- Cited in Section 2.1 and Section 3 (framework design, mapping table).

**Limitations / Gap Relative to Our Contribution:**
- Designed for human software development teams; no AI agent dimension.
- Does not account for multi-agent orchestration overhead (agent spawning, prompt engineering, coordination cost).
- No concept of heterogeneous artifact types (papers, ontologies, code, analyses) -- assumes software output.
- Communication dimension assumes human-to-human collaboration; does not model human-to-agent or agent-to-agent communication.
- No cost modeling (API spend, compute resources).

**Related Work Section:** 2.1 (Developer Productivity Frameworks)

---

### Source 2: DORA 2025

**Citation:**
Google DORA Team, "State of AI-Assisted Software Development," DORA Research Program, Google Cloud, 2025. [Online]. Available: https://dora.dev/research/2025/dora-report/

**Key Findings:**
- Four core DORA metrics: deployment frequency, lead time for changes, mean time to recovery (MTTR), change failure rate.
- Central thesis: AI functions as an amplifier -- it magnifies existing organizational strengths *and* weaknesses.
- Reports 90% of developers use AI tools at work; 80%+ believe AI increases their productivity.
- 30% of developers report little or no trust in AI-generated code.
- Individual-level gains (faster coding, more PRs) do not automatically translate to organizational-level throughput improvements.
- AI adoption is necessary but insufficient; organizational culture, processes, and code review capacity are the actual bottlenecks.
- Greatest returns come from investing in organizational systems, not just AI tooling.
- Findings align with Faros AI paradox data (see Source 8).

**Relevance to Our Paper:**
- The "amplifier" finding is directly relevant: our multi-agent swarm amplifies both the researcher's capability and any process weaknesses (e.g., poor session planning, unclear goals).
- The perception vs. reality gap (80%+ believe productivity gains, but org metrics flat) parallels METR's finding and motivates our dual tracking of perceived vs. measured productivity.
- Trust finding (30% distrust) maps to our quality_rating and quality_notes fields -- we track whether the researcher trusts the swarm output.
- DORA metrics are well-established but designed for CI/CD pipelines, not research artifact production.
- Cited in Section 2.1 and Section 6 (Discussion, comparison to industry findings).

**Limitations / Gap Relative to Our Contribution:**
- Metrics are CI/CD-centric (deployment frequency, lead time, MTTR, change failure rate). Research artifacts (papers, ontologies) have no deployment frequency analog.
- Assumes software delivery as the primary output type.
- Organization-level analysis; does not model individual researcher + multi-agent collaboration.
- No framework for measuring research-specific outputs (page counts, citation quality, ontological correctness).
- No cost dimension (API spend per artifact).

**Related Work Section:** 2.1 (Developer Productivity Frameworks)

---

### Source 3: GQM (Goal-Question-Metric)

**Citation:**
V. R. Basili and D. M. Weiss, "A Methodology for Collecting Valid Software Engineering Data," *IEEE Trans. Softw. Eng.*, vol. SE-10, no. 6, pp. 728--738, Nov. 1984. [Online]. Available: https://www.cs.umd.edu/users/mvz/handouts/gqm.pdf

**Key Findings:**
- Defines a top-down metric derivation methodology: (1) articulate Goals, (2) derive Questions that operationalize the goals, (3) identify Metrics that answer the questions.
- Goals are defined in terms of purpose, perspective, and environment (object of study, viewpoint, context).
- Prevents "metric fishing" by requiring every metric to trace back to a question and goal.
- Successfully applied at NASA Software Engineering Laboratory, Motorola, and numerous industrial settings.
- Later extended to GQM+ (Basili et al., 2007) incorporating organizational strategies.
- Widely cited as a foundational measurement paradigm in empirical SE.

**Relevance to Our Paper:**
- GQM is our metric derivation methodology. Our three goals (measure output volume, assess AI efficiency, evaluate quality) map to questions that produce the scorecard fields.
- Provides methodological legitimacy: reviewers can trace every metric to its motivating goal and question.
- The traceability principle (goal to question to metric) ensures we don't collect data we cannot interpret.
- Cited in Section 2.1 (as methodology) and Section 3 (framework design derivation).

**Limitations / Gap Relative to Our Contribution:**
- GQM is methodology-agnostic; it prescribes *how* to derive metrics but not *which* metrics are relevant to AI-augmented research.
- No AI-specific GQM extension has been published -- our paper implicitly demonstrates one.
- Original paper predates AI tooling by four decades; the goal types and questions need updating for human-AI collaborative contexts.
- Does not address temporal dynamics (how metrics evolve as the researcher-swarm relationship matures).

**Related Work Section:** 2.1 (Developer Productivity Frameworks) and 3 (Framework Design -- methodology)

---

### Source 4: SPACEX

**Citation:**
Authors, "SPACEX: Exploring Metrics with the SPACE Model for Developer Productivity," *arXiv preprint*, arXiv:2511.20955, 2025.

**Key Findings:**
- Extends the SPACE framework through repository mining and statistical analysis on open-source project data.
- Introduces a Composite Productivity Score (CPS) that synthesizes multiple SPACE dimensions into a single metric.
- Discovers a statistically significant positive correlation between negative affective states and commit frequency -- developers commit more when frustrated (iterative remediation cycle).
- Demonstrates that the topology of contributor interactions provides higher-fidelity mapping of collaborative dynamics than traditional volume-based metrics (e.g., commit counts).
- Employs Generalized Linear Mixed Models (GLMM) and RoBERTa-based sentiment analysis.
- Moves beyond deterministic, unidimensional productivity heuristics.

**Relevance to Our Paper:**
- The CPS concept supports our multi-dimensional scorecard approach -- both reject single-metric productivity measurement.
- The frustration-commit correlation is relevant: in swarm-augmented work, high rework_pct may correlate with frustration (perception_note). We can test this.
- Interaction topology insight supports our interest in swarm topology as a moderating variable (RQ3).
- Sentiment analysis approach could be applied to perception_note fields in future extensions.
- Cited in Section 2.1 (as recent SPACE extension).

**Limitations / Gap Relative to Our Contribution:**
- Analyzes traditional open-source projects; no AI agent involvement.
- CPS aggregates across human developers; does not model human-AI agent interactions.
- Repository mining assumes code as the primary output; does not handle heterogeneous research artifacts.
- Affective state analysis based on commit messages, not researcher self-report.

**Related Work Section:** 2.1 (Developer Productivity Frameworks)

---

## Category 2: AI-Assisted Development Studies

### Source 5: GitHub Copilot RCT

**Citation:**
S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer, "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot," *arXiv preprint*, arXiv:2302.06590, 2023.

**Key Findings:**
- Randomized controlled trial: treatment group (with Copilot) completed an HTTP server implementation task 55.8% faster than control group.
- Field study at Microsoft and Accenture: developers with Copilot merged 12.9--21.8% more pull requests per week.
- Heterogeneous effects by experience: junior developers gained most (27--39% improvement), senior developers gained least (8--13% improvement).
- Task type matters: repetitive, boilerplate, and well-defined tasks show highest acceleration.
- Effect size varies substantially across task complexity and developer skill level.
- Suggests AI pair programmers can help lower the barrier to entry for software development careers.

**Relevance to Our Paper:**
- Provides a baseline comparison: Copilot (single AI tool, single developer, code-only) vs. our setting (multi-agent swarm, single researcher, heterogeneous artifacts).
- The 55.8% speed-up is an upper bound for a constrained, well-defined task. Our tasks are less constrained, so we expect different effect sizes.
- Experience-level moderation is relevant: our N=1 design controls for experience but cannot test this dimension. We note this as a limitation.
- Task-type moderation supports our RQ3 (artifact type as moderating variable).
- Cited in Section 2.2 and Section 6 (Discussion, comparison).

**Limitations / Gap Relative to Our Contribution:**
- Single developer + single AI tool (Copilot), not a multi-agent swarm.
- Code-only output (HTTP server); does not measure papers, ontologies, analyses.
- Lab task (constrained, time-bounded) differs from real-world research sessions (open-ended, multi-artifact).
- Does not measure cost, quality, or researcher satisfaction -- only speed and completion.
- No longitudinal dimension; snapshot experiment.

**Related Work Section:** 2.2 (AI-Assisted Development Studies)

---

### Source 6: METR RCT

**Citation:**
METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity," *arXiv preprint*, arXiv:2507.09089, 2025.

**Key Findings:**
- Randomized controlled trial: 16 experienced open-source developers, 246 tasks on mature projects.
- Developers averaged 5 years of prior experience with their respective codebases.
- **CRITICAL FINDING:** AI tooling made experienced developers 19% SLOWER (actual measurement).
- **PERCEPTION BIAS:** Developers forecasted AI would cut completion time by 24% *before* tasks; estimated a 20% improvement *after* tasks. Both perceptions contradicted the measured slowdown.
- Expert predictions also wrong: economists predicted 39% faster; ML researchers predicted 38% faster.
- When AI was permitted, developers primarily used Cursor Pro with Claude 3.5/3.7 Sonnet models.
- Methodology: 143 hours of screen recordings analyzed at 10-second resolution.
- 20 potential confounders investigated, including project characteristics and developer familiarity with AI tools.
- Authors acknowledge experimental artifacts cannot be entirely ruled out.
- February 2026 update: METR revising experimental design for follow-up study.

**Relevance to Our Paper:**
- The most methodologically rigorous challenge to AI productivity claims. Directly motivates our perception_note field.
- The 19% slowdown + 24% perceived speedup gap is the strongest evidence that self-report productivity data is unreliable in AI-augmented contexts. We MUST track both perceived and measured productivity.
- Context matters: METR studied experienced developers on *familiar* codebases -- AI may slow down experts who already have deep knowledge. Our setting is different (researcher + swarm on *new* artifacts), so the effect direction may differ.
- The 10-second screen recording methodology is a gold standard we cannot match in our action research design. We acknowledge this as a validity threat.
- Cited in Section 2.2 (key contrarian finding), Section 4 (motivates dual tracking), Section 6 (Discussion), Section 7 (Threats to Validity).

**Limitations / Gap Relative to Our Contribution:**
- Single developer + single AI tool, not a multi-agent swarm with orchestration.
- Code-only tasks on existing codebases; no creative/generative research tasks (writing, ontology design).
- Short-duration tasks; does not capture the longitudinal learning curve of human-AI collaboration.
- N=16 is small; effect may differ with larger samples or different developer populations.
- Experienced devs on familiar codebases -- AI may help more on unfamiliar tasks (our typical scenario).

**Related Work Section:** 2.2 (AI-Assisted Development Studies) -- featured prominently as a cautionary finding

---

### Source 7: Google Internal Study

**Citation:**
Referenced in Google DORA, "State of AI-Assisted Software Development," 2025. [Online]. Available: https://dora.dev/research/2025/dora-report/

**Key Findings:**
- Approximately 100 engineers participated in an internal Google study.
- Developers were 21% faster when using AI tools.
- Results contradict METR's 19% slowdown finding.
- Context may explain divergence: Google's internal AI tools are deeply integrated into their proprietary development environment, whereas METR's developers used general-purpose AI tools on open-source projects.
- Suggests that AI productivity effects depend heavily on tool integration quality and organizational context.

**Relevance to Our Paper:**
- Illustrates that context moderates AI productivity effects -- supports our RQ3 focus on moderating variables.
- The Google-METR contradiction demonstrates why single-study claims about AI productivity are insufficient; longitudinal, multi-context measurement is needed.
- Our framework captures context (hive, artifact type, swarm topology) to enable similar comparative analysis.
- Cited in Section 2.2 (juxtaposed with METR).

**Limitations / Gap Relative to Our Contribution:**
- Internal study, not peer-reviewed; limited methodological transparency.
- Single organization, single tool ecosystem; limited generalizability.
- Code-centric; no research artifact production.
- No cost or quality dimension reported.

**Related Work Section:** 2.2 (AI-Assisted Development Studies)

---

### Source 8: Faros AI Productivity Paradox

**Citation:**
Faros AI, "The AI Productivity Paradox Research Report," 2025. [Online]. Available: https://www.faros.ai/blog/ai-software-engineering

**Key Findings:**
- Analyzed telemetry from over 10,000 developers across 1,255 teams, drawing data from task management, IDEs, code analysis tools, CI/CD pipelines, and version control systems.
- Individual-level gains: 21% more tasks completed, 98% more PRs merged on high-AI-adoption teams; developers touched 9% more tasks and 47% more PRs daily.
- Organizational-level reality: no significant correlation between AI adoption and improvements at the company level across throughput, DORA metrics, and quality KPIs.
- Primary bottleneck: PR review time surged 91%; average PR size increased 154%; bugs per developer increased 9%.
- Amdahl's Law in practice: accelerating code generation creates a bottleneck at code review and integration.
- Four adoption barriers: critical mass reached only 2--3 quarters ago; uneven adoption across teams; adoption skewed toward newer employees; usage limited to autocomplete features.
- Developers shifting toward orchestration roles rather than pure coding.

**Relevance to Our Paper:**
- The individual-vs-organizational paradox is central to our framing. We measure both session-level (individual) and portfolio-level (organizational) productivity to detect whether the paradox holds in research contexts.
- The 91% review time surge is an Amdahl's Law bottleneck analog: in our context, the bottleneck may be researcher review/integration of swarm outputs rather than AI generation speed.
- The "orchestration role" shift perfectly describes our setting -- the researcher orchestrates agents rather than writing directly.
- The 9% increase in bugs is relevant to our quality_rating and rework_pct fields.
- Cited in Section 2.2 (AI paradox), Section 3 (framework rationale for measuring both session and portfolio level), Section 6 (Discussion).

**Limitations / Gap Relative to Our Contribution:**
- Software development only (code, PRs, CI/CD); no research artifact types.
- Organizational-level analysis; does not model individual researcher + multi-agent collaboration.
- No cost dimension (API spend, compute).
- No longitudinal per-session tracking; aggregate telemetry analysis.
- No quality dimension beyond bug counts.

**Related Work Section:** 2.2 (AI-Assisted Development Studies)

---

## Category 3: Agentic AI Evaluation

### Source 9: CLEAR Framework

**Citation:**
Authors, "Beyond Accuracy: A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems," *arXiv preprint*, arXiv:2511.14136, 2025.

**Key Findings:**
- Proposes five dimensions for enterprise AI agent evaluation: Cost, Latency, Efficacy, Assurance, Reliability (CLEAR).
- Evaluated 6 agents across 300 enterprise tasks.
- Optimizing for accuracy alone yields agents 4.4--10.8x more expensive than cost-aware alternatives with comparable performance.
- 50x cost variation across agents achieving similar precision levels.
- Reliability drops dramatically from 60% (single run) to 25% (8-run consistency), revealing critical gaps in evaluation methods that use single-run benchmarks.
- Expert evaluation (N=15) confirms CLEAR predicts production success (Spearman rho=0.83) vs. accuracy-only metrics (rho=0.41).
- Addresses three benchmark limitations: overlooking cost-efficiency, inadequate reliability assessment, missing security/compliance dimensions.

**Relevance to Our Paper:**
- CLEAR is the closest existing framework to our needs for the AI system dimension. Our framework adapts CLEAR's dimensions:
  - Cost --> our cost_usd field (direct adaptation)
  - Latency --> our duration_hours field (session-level analog)
  - Efficacy --> our output_volume and quality_rating fields
  - Assurance --> our quality_notes field (trust/governance)
  - Reliability --> our rework_pct field (consistency proxy)
- The cost-accuracy tradeoff finding (4.4--10.8x) directly supports our argument that cost must be a first-class metric, not an afterthought.
- The reliability drop (60% to 25%) justifies why we track quality at the session level rather than relying on single-output assessments.
- Cited in Section 2.3 (Agentic AI Evaluation) and Section 3 (mapping table, CLEAR adaptation).

**Limitations / Gap Relative to Our Contribution:**
- Evaluates AI agent systems in isolation; no human orchestrator in the loop.
- Enterprise task benchmarks (customer service, data processing), not research artifact production.
- No concept of heterogeneous output types within a single evaluation.
- No longitudinal dimension; benchmark-style snapshot evaluation.
- No satisfaction/perception dimension for the human user.
- Treats the agent system as a black box; does not distinguish single-agent from multi-agent swarm architectures.

**Related Work Section:** 2.3 (Agentic AI Evaluation)

---

### Source 10: SWE-bench / SWE-bench Pro

**Citation:**
Scale AI, "SWE-bench Pro Leaderboard," 2025. [Online]. Available: https://scale.com/leaderboard/swe_bench_pro_public

**Key Findings:**
- Benchmark for evaluating AI agents' ability to resolve real-world GitHub issues by generating code patches.
- Primary metric: resolve rate (percentage of issues successfully patched).
- SWE-bench Pro addresses contamination concerns (test data leakage), limited task diversity, and oversimplified problem formulations in the original SWE-bench.
- Widely used as the de facto leaderboard for comparing agentic AI coding systems.
- Top systems (as of early 2026) achieve 40--60% resolve rates on Pro, substantially lower than original SWE-bench.

**Relevance to Our Paper:**
- Represents the dominant evaluation paradigm for AI agents -- one that our framework explicitly moves beyond.
- SWE-bench's code-patch-only focus illustrates the gap: there is no equivalent benchmark for research artifact production.
- The resolve rate metric is binary (fixed/not fixed) and unidimensional -- exactly the kind of metric our multi-dimensional framework supersedes.
- Cited in Section 2.3 (as an example of what exists and why it is insufficient).

**Limitations / Gap Relative to Our Contribution:**
- Code patches only; cannot evaluate papers, ontologies, analyses, or documentation.
- Relies on test suites that may not capture all valid solutions (false negatives on creative approaches).
- Binary pass/fail metric; no partial credit, no quality gradient.
- Evaluates AI agent alone; no human-in-the-loop orchestration.
- No cost, latency, or reliability dimension.
- Task scope: individual bug fixes, not multi-artifact research sessions.

**Related Work Section:** 2.3 (Agentic AI Evaluation)

---

### Source 11: Beyond Task Completion

**Citation:**
Authors, "Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems," *arXiv preprint*, arXiv:2512.12791, 2025.

**Key Findings:**
- Argues that binary task completion metrics fail to capture the non-deterministic behavior of LLM-based agents.
- Proposes an Agent Assessment Framework with four evaluation pillars: LLMs, Memory, Tools, Environment.
- Evaluates agents on: tool usage correctness, memory management and retrieval, multi-agent collaboration capabilities, and environmental responsiveness.
- Validated through an Autonomous CloudOps case study (MontyCloud Inc.) -- reveals behavioral deviations that conventional metrics miss.
- Demonstrates that runtime uncertainties in agentic AI require more granular observation than pass/fail.
- Grounded in practical production deployment experience.

**Relevance to Our Paper:**
- Supports our central argument: task completion alone is an insufficient productivity metric for agentic AI.
- The four pillars (LLM, Memory, Tools, Environment) complement our framework by providing a structural lens for understanding *why* swarm productivity varies across sessions.
- Multi-agent collaboration capability assessment is directly relevant to our swarm topology analysis (RQ3).
- The call for granular observation beyond pass/fail aligns with our multi-dimensional scorecard design.
- Cited in Section 2.3 (Agentic AI Evaluation).

**Limitations / Gap Relative to Our Contribution:**
- Evaluates AI system capabilities in isolation; no human orchestrator.
- CloudOps domain; not research artifact production.
- Framework focuses on agent architecture quality, not on output productivity of the human-agent team.
- No cost or satisfaction dimensions.
- No longitudinal tracking.

**Related Work Section:** 2.3 (Agentic AI Evaluation)

---

## Category 4: Research Methodology

### Source 12: Action Research in SE

**Citation:**
M. Staron, *Action Research in Software Engineering: Theory and Applications*. Cham, Switzerland: Springer, 2020.

**Key Findings:**
- Defines the action research cycle: diagnose, plan, act, evaluate, reflect.
- Established methodology for academia-industry collaboration in SE.
- Researcher-as-practitioner model: the researcher is both the subject and the instrument of study.
- Over a decade of industrial application at Ericsson, Volvo, and other organizations.
- Addresses common validity concerns: researcher bias mitigated through structured reflection, external validation, and triangulation.
- Distinguishes action research from case studies: the researcher actively intervenes and studies the effect, rather than passively observing.
- Legitimizes N=1 and small-N designs when the research questions concern process improvement within a specific context.

**Relevance to Our Paper:**
- Primary methodological foundation. Legitimizes our N=1 researcher design as a recognized and rigorous SE methodology.
- Our study follows the action research cycle: (diagnose) current unmeasured swarm-augmented productivity, (plan) design scorecard framework, (act) collect data per session, (evaluate) analyze longitudinal trends, (reflect) refine the framework.
- The researcher-as-practitioner model exactly describes our situation: the researcher orchestrates swarms, produces artifacts, and simultaneously studies the process.
- Provides the vocabulary and structure for our Section 4 (Action Research Design).
- Cited in Section 2.5 (Research Methodology), Section 4 (design justification), Section 7 (validity threats -- how action research addresses them).

**Limitations / Gap Relative to Our Contribution:**
- Does not address AI-augmented contexts; the "practitioner" is assumed to be a human working with human tools.
- No guidance on measuring human-AI collaboration specifically.
- Typical action research in SE focuses on process improvement in software organizations, not individual research productivity.
- Bias mitigation strategies (peer debriefing, member checking) are harder in an N=1 setting.

**Related Work Section:** 2.5 (Research Methodology)

---

### Source 13: AI and Research Productivity (Springer Nature)

**Citation:**
Springer Nature, "How does artificial intelligence shape the productivity and quality of research in business studies?" *Discover Sustainability*, 2025.

**Key Findings:**
- Calls for "standardized protocols and metrics for evaluating AI-augmented methodologies" in academic research.
- Warns about "rising scores and declining quality" -- AI tools may inflate output volume metrics while reducing the intellectual depth and rigor of research.
- No concrete framework proposed; identifies the need as an open problem.
- Notes the tension between efficiency gains and quality assurance in AI-augmented research.
- Highlights metric gaming risk: researchers optimizing for measurable outputs (papers, citations) at the expense of unmeasured quality dimensions.

**Relevance to Our Paper:**
- This is the published articulation of our gap. A major academic publisher calls for exactly the kind of framework we propose, and no one has delivered it yet.
- The "rising scores, declining quality" warning directly motivates our quality_rating and quality_notes dimensions -- we track quality alongside volume to detect this failure mode.
- The metric gaming risk informs our Threats to Validity section: as the researcher, we might unconsciously optimize for scorecard metrics rather than genuine productivity.
- Cited in Section 1 (Introduction, gap statement), Section 2.4 (Academic Research Productivity), Section 7 (Threats to Validity).

**Limitations / Gap Relative to Our Contribution:**
- Identifies the problem but proposes no solution -- that is our contribution.
- Business studies focus; does not address SE-specific research artifacts.
- No empirical data; opinion/perspective piece.
- No framework for distinguishing AI-augmented quality degradation from genuine productivity improvement.

**Related Work Section:** 2.4 (Academic Research Productivity)

---

### Source 14: Case Study Methodology in SE

**Citation:**
P. Runeson and M. Host, "Guidelines for conducting and reporting case study research in software engineering," *Empirical Softw. Eng.*, vol. 14, no. 2, pp. 131--164, Apr. 2009.

**Key Findings:**
- Standard methodological reference for conducting and reporting case studies in SE.
- Defines case study types: exploratory, descriptive, explanatory, improving.
- Specifies reporting guidelines: research questions, case selection, data collection, analysis, validity threats.
- Distinguishes case studies from experiments and surveys; emphasizes in-context, in-depth study of phenomena.
- Validity framework: construct validity, internal validity, external validity, reliability.
- Recommends triangulation (multiple data sources), chain of evidence (traceability from data to conclusions), and member checking.

**Relevance to Our Paper:**
- Provides the validity framework vocabulary for our Threats to Validity section (Section 7).
- Our study is primarily action research (Staron, 2020) but shares case study characteristics (in-context, single-case, longitudinal). Runeson and Host's guidelines help structure our reporting.
- Construct validity: are our scorecard metrics measuring what we claim? Internal validity: are observed productivity changes caused by the swarm, not confounds? External validity: can our framework generalize beyond N=1? Reliability: can another researcher replicate our data collection?
- Cited in Section 2.5 (Research Methodology) and Section 7 (Threats to Validity).

**Limitations / Gap Relative to Our Contribution:**
- General SE case study guidelines; no AI-specific considerations.
- Does not address the unique validity threats of human-AI collaboration studies (e.g., METR-style perception bias, Hawthorne effect from self-measurement).
- Designed for case studies, not action research specifically -- we use Staron (2020) as the primary methodological reference.

**Related Work Section:** 2.5 (Research Methodology)

---

## Category 5: Gap Analysis -- The Research Space Our Paper Occupies

### Consolidated Gap Table

| Source | What It Measures | What It Misses (Our Contribution) |
|--------|-----------------|-----------------------------------|
| SPACE [1] | Human developer productivity (5 dimensions) | No AI/agent dimension; no orchestration overhead; software-only |
| DORA 2025 [2] | CI/CD pipeline metrics (4 key metrics) | Not research outputs; no cost; no artifact heterogeneity |
| GQM [3] | Metric derivation methodology | No AI-specific instantiation published |
| SPACEX [4] | Extended SPACE with CPS | Traditional OSS projects; no AI agents |
| Copilot RCT [5] | Single dev + single AI tool speed | No multi-agent; code-only; no longitudinal; no cost/quality |
| METR RCT [6] | Single dev + single AI tool (experienced OSS devs) | Code-only; no multi-agent; short tasks; N=16 |
| Google Internal [7] | Single dev + internal AI tools | Unpublished; single org; code-only |
| Faros AI [8] | Individual vs. org productivity with AI | Software delivery only; no research artifacts; no per-session tracking |
| CLEAR [9] | AI agent system (5 dimensions) | AI in isolation; no human orchestrator; no research context |
| SWE-bench [10] | AI agent code-fix ability (resolve rate) | Code patches only; binary metric; no human-in-loop |
| Beyond Task Completion [11] | Agent architecture quality (4 pillars) | AI in isolation; no human; no research outputs |
| Action Research [12] | SE process improvement methodology | No AI-augmented context |
| AI + Research Quality [13] | Identifies need for AI-augmented research metrics | No framework proposed |
| Case Study Methods [14] | Validity framework for SE case studies | No AI-specific validity threats |

### The Gap Statement

No existing framework measures the productivity of a **human researcher** orchestrating an **multi-agent AI swarm** to produce **heterogeneous research artifacts** (papers, ontologies, code, analyses). Specifically:

1. **Developer productivity frameworks** (SPACE, DORA, GQM, SPACEX) assume human teams producing software. They lack dimensions for AI agent orchestration overhead, API cost, and agent-to-agent coordination.

2. **AI-assisted development studies** (Copilot, METR, Google, Faros) measure a single developer using a single AI tool on code-only tasks. They do not model multi-agent swarms, heterogeneous outputs, or the orchestration role.

3. **Agentic AI evaluation frameworks** (CLEAR, SWE-bench, Beyond Task Completion) assess AI systems in isolation. They exclude the human orchestrator, the collaboration dynamics, and the research-specific output types.

4. **Research productivity literature** (Springer Nature 2025) identifies the need for standardized AI-augmented research metrics but proposes no framework.

5. **Research methodology** (Staron 2020, Runeson and Host 2009) provides rigorous approaches (action research, case study) but no AI-specific instantiation.

Our paper fills this gap by proposing a multi-dimensional framework -- derived via GQM, informed by SPACE and CLEAR, operationalized as per-session YAML scorecards -- and validated through a longitudinal action research study of one researcher orchestrating 8 hives across 12+ months.

---

## Cross-Source Synthesis: Key Themes

### Theme 1: The Perception-Reality Gap
- **METR [6]:** 19% actual slowdown vs. 24% perceived speedup.
- **DORA [2]:** 80%+ believe AI increases productivity; org metrics flat.
- **Faros [8]:** 21% more tasks individually; no organizational improvement.
- **Implication:** Self-reported productivity is unreliable. Our framework must measure both perceived (perception_note) and actual (output counts, duration, cost) productivity.

### Theme 2: The Individual-Organizational Paradox
- **Faros [8]:** Individual gains (98% more PRs) do not translate to organizational throughput.
- **DORA [2]:** AI amplifies dysfunction as often as capability.
- **Faros [8]:** Amdahl's Law -- bottleneck shifts from generation to review (91% review time increase).
- **Implication:** Our framework measures both session-level and portfolio-level productivity. The paradox may manifest as high per-session output but no acceleration in paper completion timelines.

### Theme 3: Multi-Dimensionality Is Non-Negotiable
- **SPACE [1]:** Five dimensions, no single metric captures productivity.
- **CLEAR [9]:** Five dimensions; accuracy-only evaluation is 4.4--10.8x more expensive.
- **Beyond Task Completion [11]:** Binary completion is insufficient.
- **SPACEX [4]:** Composite Productivity Score needed.
- **Implication:** Our four-dimension framework (Output Volume, AI Efficiency, Quality Gates, Process Health) is minimum viable dimensionality.

### Theme 4: Context Moderates Everything
- **Copilot [5]:** Junior devs gain 27--39%; seniors gain 8--13%.
- **METR [6]:** Experienced devs on familiar codebases get slower.
- **Google [7]:** Integrated tools yield 21% faster (contradicts METR).
- **Copilot [5]:** Repetitive tasks accelerate most.
- **Implication:** Our RQ3 (moderating factors) is essential. We track artifact type, hive, swarm topology, and task complexity to detect moderating effects.

### Theme 5: Cost as a First-Class Metric
- **CLEAR [9]:** 50x cost variation for similar accuracy; 4.4--10.8x cheaper with cost-awareness.
- **Faros [8]:** More PRs but more bugs (9%) -- hidden quality costs.
- **Implication:** Our cost_usd field and cost-per-artifact derived metrics are essential. Productivity without cost is meaningless.

---

## Reference List (IEEE Format, Numbered for Paper Use)

[1] N. Forsgren, M.-A. Storey, C. Maddila, T. Zimmermann, B. Houck, and J. Butler, "The SPACE of Developer Productivity," *ACM Queue*, vol. 19, no. 1, pp. 20--48, 2021.

[2] Google DORA Team, "State of AI-Assisted Software Development," DORA Research Program, Google Cloud, 2025. [Online]. Available: https://dora.dev/research/2025/dora-report/

[3] V. R. Basili and D. M. Weiss, "A Methodology for Collecting Valid Software Engineering Data," *IEEE Trans. Softw. Eng.*, vol. SE-10, no. 6, pp. 728--738, Nov. 1984.

[4] Authors, "SPACEX: Exploring Metrics with the SPACE Model for Developer Productivity," *arXiv preprint*, arXiv:2511.20955, 2025.

[5] S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer, "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot," *arXiv preprint*, arXiv:2302.06590, 2023.

[6] METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity," *arXiv preprint*, arXiv:2507.09089, 2025.

[7] Google, Internal AI Developer Productivity Study, referenced in [2], 2025.

[8] Faros AI, "The AI Productivity Paradox Research Report," 2025. [Online]. Available: https://www.faros.ai/blog/ai-software-engineering

[9] Authors, "Beyond Accuracy: A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems," *arXiv preprint*, arXiv:2511.14136, 2025.

[10] Scale AI, "SWE-bench Pro Leaderboard," 2025. [Online]. Available: https://scale.com/leaderboard/swe\_bench\_pro\_public

[11] Authors, "Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems," *arXiv preprint*, arXiv:2512.12791, 2025.

[12] M. Staron, *Action Research in Software Engineering: Theory and Applications*. Cham, Switzerland: Springer, 2020.

[13] Springer Nature, "How does artificial intelligence shape the productivity and quality of research in business studies?" *Discover Sustainability*, 2025.

[14] P. Runeson and M. Host, "Guidelines for conducting and reporting case study research in software engineering," *Empirical Softw. Eng.*, vol. 14, no. 2, pp. 131--164, Apr. 2009.

---

## TODO: Sources to Locate Full Author Lists

The following arXiv papers [4], [9], [11] have placeholder "Authors" entries. Before manuscript submission, retrieve full author names from arXiv metadata pages. The DORA report [2] author list should be confirmed from the downloaded PDF. The Springer Nature piece [13] needs full author names and volume/issue/page numbers.

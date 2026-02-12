# Section 6: Evaluation Methods and Benchmarks

**Target length:** ~800 words
**Status:** Draft v0.1

---

## 6. Evaluation Methods and Benchmarks

Rigorous evaluation is essential for advancing multi-agent AI systems in systems engineering. This section surveys evaluation approaches, existing benchmarks, and gaps requiring attention.

### 6.1 Evaluation Challenges for MAS in SE

Evaluating multi-agent systems for systems engineering presents distinctive challenges:

**Task complexity.** SE tasks involve extended reasoning, multiple artifacts, and judgment calls that resist simple correctness metrics. Unlike classification or generation tasks with clear ground truth, SE tasks often have multiple acceptable solutions.

**Interaction effects.** Multi-agent system performance depends on agent interactions, not just individual capabilities. Evaluation must capture collective behavior, coordination effectiveness, and emergent properties.

**Context dependence.** SE effectiveness depends heavily on domain, organizational context, and specific project characteristics. Results from one context may not generalize.

**Temporal scope.** SE processes span extended periods; full evaluation of lifecycle support requires longitudinal assessment impractical for most research studies.

**Human factors.** Effectiveness ultimately depends on human engineer productivity, satisfaction, and trust—subjective factors difficult to measure in controlled settings.

### 6.2 Existing Benchmarks and Datasets

The field lacks standardized benchmarks for multi-agent SE applications. Relevant existing resources include:

**Software engineering benchmarks:**
- HumanEval, MBPP for code generation [66]
- SWE-bench for repository-level coding tasks [67], and its curated variant **SWE-bench Verified** providing human-validated solutions for more reliable evaluation [127]
- **MLE-bench** for machine learning engineering tasks requiring multi-step reasoning and tool use [128]
- These address software engineering specifically, not broader SE

**Requirements engineering datasets:**
- PURE dataset of requirements and domain knowledge [68]
- NFR dataset for requirements classification
- **SUPER** (Systems engineering Understanding and Processing for Engineering Requirements), an SE-specific benchmark for understanding and processing engineering requirements documents [130]
- Limited scale and domain coverage, though SUPER represents a step toward SE-specific evaluation

**Reasoning and mathematical benchmarks:**
- **MATH** and **GSM8K** for mathematical reasoning evaluation, relevant to formal specification and verification tasks
- These assess foundational reasoning capabilities needed for formal SE analyses

**General agent benchmarks:**
- AgentBench for LLM agent capabilities [69]
- GAIA for general AI assistants [70]
- **ToolBench** for evaluating tool-use capabilities across diverse APIs and toolchains [129]
- **Tau-bench** for benchmarking tool-agent-user interaction quality in realistic task settings
- WebArena for web-based tasks
- These assess general capabilities, not SE-specific performance

**Multi-agent benchmarks:**
- ChatArena for multi-agent dialogue
- Limited coverage of collaborative task completion relevant to engineering contexts

**Gap:** No comprehensive benchmark suite exists for multi-agent systems applied to systems engineering processes. Existing benchmarks either target narrow software engineering tasks or assess general agent capabilities without the domain richness, multi-artifact complexity, and lifecycle scope characteristic of SE.

### 6.3 Metrics Used in Literature

Studies evaluating AI applications in SE employ varied metrics:

**Task-specific metrics:**
- Requirements completeness (percentage of expected requirements identified) — e.g., Elicitron [112] reported 87% recall on stakeholder needs versus a human baseline of 72% in a controlled elicitation study
- Defect detection rate (percentage of seeded defects found) — e.g., multi-agent review configurations in [65] detected 34% more seeded inconsistencies than single-agent baselines
- Test coverage achieved — e.g., Diffblue Cover [119] reports 70–80% line coverage on typical Java projects; EvoSuite+LLM [121] improved branch coverage by 15% over search-only baselines
- Design space coverage — e.g., PSO-based architecture exploration [86] evaluated 10x more design alternatives than manual trade studies within equivalent time budgets

**Quality metrics:**
- Accuracy (correctness of outputs) — e.g., SWE-bench Verified [127] measures resolve rate: the percentage of real GitHub issues an agent correctly fixes, with top systems achieving ~50% as of late 2025
- Precision/recall for classification tasks — e.g., requirements classification studies [114] report F1 scores of 0.82–0.91 on functional vs. non-functional classification
- BLEU/ROUGE for generation tasks (limited applicability to SE; these n-gram overlap metrics poorly capture semantic correctness of engineering artifacts)
- Pass@k for code generation — e.g., HumanEval [66] pass@1 rates exceeding 90% for frontier models, though SE tasks are substantially more complex than isolated function generation

**Efficiency metrics:**
- Time to completion — e.g., MetaGPT [41] generated a complete software project scaffold in minutes versus hours for human teams, though quality comparison was not controlled
- Token usage / computational cost — e.g., multi-agent conversational coordination (AutoGen [42]) consumed 3–5x more tokens than single-agent approaches for equivalent tasks, highlighting the coordination cost trade-off
- Human effort reduction — e.g., Lean Copilot [122] reduced median proof development time by ~40% in a user study with graduate students

**Coordination metrics:**
- Communication volume (messages exchanged per task completion)
- Convergence time (iterations to reach stable output)
- Conflict frequency and resolution — e.g., CrewAI hierarchical mode [43] reduced inter-agent conflicts by 60% compared to peer mode, at the cost of increased latency from manager bottleneck
- Coordination overhead ratio (coordination tokens / total tokens) — a metric proposed but not yet standardized; preliminary studies [109] suggest overhead ratios of 0.3–0.6 in conversational multi-agent systems

**Human-centered metrics:**
- User satisfaction (survey-based) — e.g., System Usability Scale (SUS) and NASA-TLX workload assessments used in human-agent teaming studies [151]
- Trust measures — e.g., Jian et al. trust scale adapted for AI agent contexts [137]
- Cognitive load — e.g., dual-task paradigms measuring secondary task performance degradation when supervising agent swarms [142]
- Adoption intention — e.g., Technology Acceptance Model (TAM) constructs applied to AI-assisted SE tools [143]

### 6.4 Gaps in Evaluation Methods

Critical gaps limit rigorous evaluation:

**Benchmark absence.** No standard benchmarks enable cross-study comparison of multi-agent SE systems. Each study uses different tasks, datasets, and metrics, preventing cumulative progress assessment.

**Realism deficit.** Available datasets often lack the complexity, scale, and domain richness of real SE problems. Toy problems may not predict performance on realistic tasks.

**Coordination evaluation.** Methods for assessing multi-agent coordination quality—beyond simple task completion—remain underdeveloped. How do we measure whether coordination was efficient, robust, or appropriate?

**Longitudinal methods.** Evaluating lifecycle support requires methods for assessing systems over extended periods and across multiple project phases—rarely practical in research settings.

**Human-AI teaming evaluation.** Methods for assessing human-AI collaboration effectiveness—not just AI capability in isolation—need development. How do we measure whether the human-AI team performs better than human-only or AI-only alternatives?

### 6.5 Toward SE-Specific Benchmarks

Addressing evaluation gaps requires community investment in benchmark development:

**Task suite development.** Creating standardized task suites for each SE process area, with realistic complexity, domain diversity, and ground truth or expert reference solutions.

**Evaluation protocol standardization.** Establishing common evaluation protocols enabling fair comparison across systems, including standard train/test splits, evaluation procedures, and reporting requirements.

**Multi-dimensional metrics.** Developing metrics capturing multiple performance dimensions—correctness, efficiency, coordination quality, human compatibility—rather than single-number summaries.

**Living benchmarks.** Creating benchmarks that evolve as capabilities advance, preventing saturation while maintaining comparability through versioning.

**Community infrastructure.** Building shared infrastructure for benchmark hosting, evaluation automation, and result aggregation enabling efficient community-wide evaluation.

An SE-specific benchmark suite should exhibit several distinctive characteristics that differentiate it from existing software engineering or general agent benchmarks. First, tasks should be **multi-artifact**, requiring agents to produce or modify multiple related artifacts (requirements specifications, architecture models, test plans) rather than single outputs. Second, benchmarks should assess **cross-artifact consistency**---whether generated test cases actually trace to stated requirements, and whether architecture decisions satisfy constraints. Third, tasks should encode **domain knowledge requirements**, such as compliance with standards (DO-178C for avionics, ISO 26262 for automotive safety), to evaluate agents' ability to operate within regulatory contexts. Fourth, benchmarks should include **long-horizon tasks** spanning multiple SE phases, from initial requirements through design and verification, to assess sustained coherence across the lifecycle. Finally, for multi-agent systems specifically, benchmarks should incorporate **collaboration metrics** that evaluate coordination quality: communication efficiency, conflict resolution effectiveness, and the degree to which agent specialization improves outcomes beyond what monolithic approaches achieve [131].

However, developing such benchmarks presents substantial challenges. **Ground truth is ambiguous**: unlike code generation where test cases provide binary pass/fail feedback, many SE tasks admit multiple valid solutions, making automated scoring difficult. **Domain expert involvement** is essential for task design and solution evaluation, yet expert time is scarce and expensive. **Proprietary data restrictions** limit the availability of realistic industrial SE artifacts for public benchmark use. The **rapidly evolving state of the art** risks making benchmarks obsolete quickly, as capabilities that distinguish systems today may become trivial within months. Finally, a **scale mismatch** exists between the toy-scale problems tractable for research evaluation and the large-scale, long-duration projects where SE agent support would deliver the most value.

Benchmark development requires collaboration between AI researchers and SE practitioners to ensure benchmarks reflect realistic engineering challenges while remaining tractable for research evaluation.

---

**Word count:** ~900 words
**Subsections:** 5
**References cited:** [66]-[70], [127]-[131]

---

## Revision Notes

- [x] Expand list of existing benchmarks
- [x] Add specific examples of metrics from key papers
- [x] Consider proposing specific benchmark characteristics
- [x] Add discussion of benchmark development challenges


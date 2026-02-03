# Section 3: Related Work

**Target length:** ~1,000 words
**Status:** Draft v0.1

---

## 3. Related Work

This section reviews foundational work in multi-agent systems, swarm intelligence, and AI applications in systems engineering, identifying the gap this paper addresses.

### 3.1 Multi-Agent Systems in Engineering

Multi-agent systems (MAS) research provides foundational concepts for coordinated AI systems. Wooldridge [19] defines agents as computer systems capable of autonomous action to meet design objectives, with properties including autonomy, social ability, reactivity, and proactivity. Weiss [20] and Ferber [21] established frameworks for multi-agent system design and coordination.

Engineering applications of MAS span decades. Jennings [22] demonstrated agent-based approaches to business process management. Shen et al. [23] surveyed agent-based manufacturing systems for reconfigurable production. Leitão [24] reviewed agent-based distributed manufacturing control. These applications established that agent coordination could address complex engineering challenges.

However, classical MAS relied on explicit knowledge engineering and symbolic reasoning, limiting adaptability and requiring substantial development effort. The emergence of LLM-based agents fundamentally changes the capability profile, enabling natural language interaction, broad knowledge access, and flexible reasoning without extensive custom development.

### 3.2 Swarm Intelligence

Swarm intelligence draws inspiration from collective behavior in biological systems—ant colonies, bird flocks, fish schools—where simple individuals following local rules produce sophisticated collective behavior [25, 26].

**Ant Colony Optimization (ACO)** models pheromone-based coordination for combinatorial optimization [27]. Artificial ants deposit virtual pheromone on solution components, guiding subsequent search toward promising solutions. ACO has been applied to engineering routing, scheduling, and design optimization.

**Particle Swarm Optimization (PSO)** models flocking behavior for continuous optimization [28]. Particles move through search spaces influenced by individual and collective best-known positions. PSO has found application in engineering parameter optimization and control system design.

**Stigmergic coordination** enables indirect communication through environmental modification [29]. Agents leave traces influencing other agents' behavior without direct message exchange, enabling scalable coordination with minimal overhead.

Swarm intelligence contributes key insights: collective intelligence can exceed individual capability; simple local rules produce complex global behavior; decentralized coordination achieves robust, scalable solutions. However, traditional swarm approaches address optimization rather than the reasoning-intensive tasks characteristic of systems engineering.

### 3.3 AI Applications in Systems Engineering

AI applications to SE have evolved with AI capabilities:

**Requirements engineering** has received substantial attention. Mund et al. [30] applied ML to requirements classification. Ferrari et al. [31] developed NLP approaches for requirements quality analysis. Dalpiaz et al. [32] surveyed AI for requirements engineering, identifying applications in elicitation, analysis, specification, and validation. Recent work applies LLMs to requirements generation and consistency checking [33, 34].

**Architecture and design** applications include AI-assisted trade studies, design space exploration, and pattern recommendation. Metzger and Pohl [35] reviewed AI in software product line engineering. Malavolta et al. [36] surveyed ML in software architecture. These applications typically employ single models rather than coordinated agent systems.

**Verification and validation** applications span test generation, coverage analysis, and defect prediction. Feldt et al. [37] surveyed AI in software testing. Durelli et al. [38] reviewed ML for test case prioritization. Automated test generation has achieved commercial deployment in software contexts.

**Model-Based Systems Engineering (MBSE)** creates structured representations amenable to AI analysis. Madni and Sievers [17] discussed AI and MBSE integration. Huldt and Stenius [18] surveyed AI applications in systems engineering, noting growing interest but limited mature implementations.

### 3.4 LLM-Based Multi-Agent Systems

The emergence of LLM-based agents has spawned frameworks for multi-agent coordination:

**MetaGPT** [39] implements multi-agent software development with role-based specialization (product manager, architect, engineer). It demonstrates role-based patterns but focuses on software rather than broader SE.

**AutoGen** [40] supports conversational agents with customizable interaction patterns. It enables flexible multi-agent configurations but provides limited SE-specific guidance.

**CrewAI** [41] provides role-based agent "crews" with defined collaboration patterns. It emphasizes task decomposition and agent specialization but lacks SE domain grounding.

**ChatDev** [42] simulates software company dynamics with communicating agents. Like MetaGPT, it addresses software development specifically.

These frameworks demonstrate multi-agent LLM capabilities but focus predominantly on software development rather than domain-agnostic systems engineering. None provides systematic mapping to SE process standards or addresses the full lifecycle.

### 3.5 Research Gap

Despite substantial work in constituent areas, a gap exists at their intersection:

| Existing Work | Coverage | Gap |
|---------------|----------|-----|
| Classical MAS | Engineering applications | Not LLM-based; limited flexibility |
| Swarm intelligence | Optimization | Not reasoning-intensive SE tasks |
| AI in SE | Individual process areas | Not multi-agent; not comprehensive |
| LLM multi-agent | Software development | Not domain-agnostic SE; not process-mapped |

**This paper addresses the gap** by presenting a framework for LLM-based agentic swarms systematically mapped to domain-agnostic systems engineering processes per ISO 15288. We synthesize insights from MAS coordination, swarm intelligence, and emerging LLM agent capabilities, applying them to the full SE lifecycle across application domains.

---

**Word count:** ~820 words
**Subsections:** 5
**Tables:** 1
**References cited:** [17]-[42]

---

## Revision Notes

- [ ] Expand LLM multi-agent section with more recent frameworks
- [ ] Add additional SE application citations
- [ ] Consider adding comparison figure


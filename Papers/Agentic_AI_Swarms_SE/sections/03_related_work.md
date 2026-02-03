# Section 3: Related Work

**Target length:** ~1,000 words
**Status:** Draft v0.1

---

## 3. Related Work

This section reviews foundational literature across four research streams that inform the concept of agentic AI swarms for systems engineering: multi-agent systems, swarm intelligence, AI applications in systems engineering, and systems engineering process standards. We conclude with a gap analysis positioning our contribution.

### 3.1 Multi-Agent Systems

The study of multi-agent systems (MAS) emerged in the 1980s and 1990s as researchers explored how autonomous computational entities could interact to solve problems beyond individual capabilities. Wooldridge's foundational work established the theoretical basis for agent architectures, defining agents as systems capable of autonomous action in dynamic environments to meet design objectives [1]. Weiss's comprehensive treatment of distributed artificial intelligence provided frameworks for agent cooperation, negotiation, and coordination [2], while Jennings, Sycara, and Wooldridge's roadmap articulated research directions that anticipated many current developments [3].

Coordination theory, as developed by Malone and Crowston [4], provided a domain-independent framework for understanding how agents—whether human or artificial—manage dependencies between activities. This theoretical foundation remains relevant for understanding swarm coordination in systems engineering contexts, where dependencies between disciplines and lifecycle phases are pervasive.

Agent-oriented software engineering (AOSE) methodologies emerged to guide the design and implementation of MAS. The Gaia methodology [12] provided a systematic approach for analyzing and designing agent systems, while Tropos [13] offered a requirements-driven approach grounded in organizational concepts. These methodologies established principles—role definition, interaction protocols, organizational structures—that inform contemporary swarm design, though they predate the capabilities of LLM-based agents.

### 3.2 Swarm Intelligence

Swarm intelligence draws inspiration from biological systems—ant colonies, bee hives, bird flocks, fish schools—where simple individual behaviors produce sophisticated collective outcomes [7]. Bonabeau, Dorigo, and Theraulaz's foundational work demonstrated that decentralized coordination mechanisms could solve complex optimization problems without central control.

Ant colony optimization (ACO), formalized by Dorigo and Stützle [8], showed that stigmergic communication—indirect coordination through environmental modification—enabled efficient solutions to combinatorial problems like routing and scheduling. Particle swarm optimization (PSO) [9] demonstrated similar capabilities using different coordination mechanisms. These algorithms found application in engineering optimization, including design space exploration and resource allocation.

The relevance of swarm intelligence to AI agent systems lies in its principles rather than its specific algorithms. Decentralized coordination, emergent collective behavior, robustness through redundancy, and scalability without central bottlenecks are properties that agentic AI swarms seek to achieve through different mechanisms—shared memory, consensus protocols, and language-based interaction rather than pheromone trails or velocity vectors.

### 3.3 AI in Systems Engineering

The application of AI to systems engineering has evolved alongside both fields. Early work focused on expert systems for specific SE tasks—configuration management, fault diagnosis, and design rule verification. As AI capabilities expanded, researchers explored machine learning for cost estimation [ref], defect prediction [ref], and requirements analysis [ref].

The emergence of model-based systems engineering (MBSE) created new opportunities for AI integration. MBSE emphasizes formal system models as authoritative sources of truth, replacing document-centric approaches with model-centric practices [58, 59]. This shift aligns well with AI capabilities: structured models provide machine-readable representations that AI systems can consume, analyze, and extend.

The INCOSE Vision 2035 [48] explicitly identifies AI and autonomous systems as transformative technologies for systems engineering practice. NASA's digital transformation initiatives [55] similarly emphasize AI integration with model-based approaches. The Department of Defense Digital Engineering Strategy [57] envisions authoritative data sources and automated analysis capabilities that AI swarms could help realize.

Recent work has explored LLM applications in systems engineering contexts, including requirements generation, architecture documentation, and design rationale capture. However, most efforts focus on single-agent applications—using an LLM as a sophisticated assistant for individual tasks rather than as a participant in coordinated multi-agent workflows.

Wach et al.'s systematic literature review on mathematical underpinnings of MBSE [60] highlights the formal foundations that enable rigorous model-based analysis, providing a basis for AI systems that must reason about system properties, constraints, and trade-offs.

### 3.4 Systems Engineering Process Standards

Systems engineering practice is guided by mature process standards that define lifecycle activities, stakeholder interactions, and technical processes. ISO/IEC/IEEE 15288:2023 [50] provides the international standard for system lifecycle processes, defining 30 processes organized into four categories: agreement, organizational project-enabling, technical management, and technical processes.

The INCOSE Systems Engineering Handbook [47] operationalizes these standards, providing guidance on implementation across domains. NASA's Systems Engineering Handbook [53] and procedural requirements [54] adapt these standards for aerospace applications, while the DoD Systems Engineering Guidebook [56] addresses defense acquisition contexts.

These standards define the process areas to which AI swarms could contribute:

- **Technical processes** (ISO 15288 Section 6.4): Business or mission analysis, stakeholder needs definition, system requirements definition, architecture definition, design definition, system analysis, implementation, integration, verification, validation, transition, operation, maintenance, and disposal.

- **Technical management processes**: Planning, assessment and control, decision management, risk management, configuration management, information management, and measurement.

The standards provide a domain-agnostic framework applicable across aerospace, defense, healthcare, energy, transportation, and other sectors. This generality makes them appropriate targets for AI swarm capability mapping.

### 3.5 Gap Analysis

Despite substantial work in each contributing area, a significant gap exists at their intersection. Multi-agent systems research established coordination principles but predates LLM capabilities. Swarm intelligence provides optimization algorithms but not the reasoning and language capabilities needed for systems engineering tasks. AI applications in SE have focused primarily on single-agent assistance rather than coordinated multi-agent collaboration. And while SE standards define comprehensive process frameworks, they do not yet address AI agent participation.

Specifically, we identify the following gaps:

1. **No systematic mapping** of agentic AI swarm capabilities to SE technical process areas
2. **Limited treatment** of how LLM-based agent specialization aligns with SE discipline expertise
3. **Insufficient analysis** of coordination mechanisms appropriate for SE workflows
4. **No domain-agnostic framework** for deploying AI swarms across SE application domains

This paper addresses these gaps by proposing an architectural framework for agentic AI swarms tailored to systems engineering, mapping swarm capabilities to ISO 15288 technical processes, and identifying research directions for the emerging field of AI-augmented systems engineering.

---

**Word count:** ~980 words
**References cited:** [1], [2], [3], [4], [7], [8], [9], [12], [13], [47], [48], [50], [53], [54], [55], [56], [57], [58], [59], [60]
**Subsections:** 5

---

## Revision Notes

- [ ] Add specific citations for cost estimation, defect prediction, requirements analysis ML work
- [ ] Consider adding LangChain, AutoGen, MetaGPT citations in 3.3
- [ ] Verify all reference numbers against final reference list
- [ ] Consider expanding MBSE/AI integration discussion if word count allows

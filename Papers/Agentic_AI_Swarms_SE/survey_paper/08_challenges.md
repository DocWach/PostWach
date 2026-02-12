# Section 8: Challenges and Open Problems

**Target length:** ~1,000-1,100 words
**Status:** Draft v0.2

---

## 8. Challenges and Open Problems

Despite promising research directions, substantial challenges impede practical adoption of multi-agent AI systems in systems engineering. This section categorizes and analyzes key challenges.

### 8.1 Technical Challenges

**Scalability.** As agent count increases, coordination overhead grows — potentially faster than capability gains [135]. Communication volume, conflict frequency, and convergence time may scale poorly. Research questions: What coordination mechanisms scale effectively? Where are the practical limits of swarm size? (See Section 9.1 for proposed research directions addressing scalability.)

**Reliability.** LLM-based agents exhibit unpredictable failures — hallucinations, reasoning errors, instruction drift [136]. Multi-agent systems can amplify failures through error propagation or exhibit emergent failure modes. For example, LLM agents generating requirements may introduce plausible-sounding but unverifiable specifications; in a multi-agent pipeline, downstream architecture and V&V agents may propagate rather than catch such errors [135]. Research questions: How can agent reliability be characterized and bounded? What architectural patterns improve robustness? (See Section 9.2 for proposed research directions addressing reliability.)

**Domain knowledge integration.** Effective SE support requires deep domain knowledge that current LLMs may lack or represent incorrectly [137]. Engineering domains require understanding of physical constraints, standards compliance, and organizational practices that may not be well-represented in LLM training data [136]. RAG helps but does not solve fundamental knowledge gaps. Research questions: How can domain constraints be reliably encoded? How can physics-based reasoning be integrated with language model capabilities? (See Section 9.3 for proposed research directions addressing domain knowledge.)

**Consistency maintenance.** Multi-agent systems generating or modifying engineering artifacts must maintain artifact consistency [138]. Concurrent modifications can introduce conflicts; coordination must ensure coherent results. Research questions: What consistency models suit SE artifacts? How should conflicts be detected and resolved?

**Performance.** LLM inference is computationally expensive; multi-agent systems multiply this cost [135]. Latency may exceed acceptable bounds for interactive applications. Research questions: What efficiency improvements are possible? How should computation be allocated across agents?

### 8.2 Integration Challenges

**Tool integration.** Connecting agent systems with SE tools (MBSE platforms, requirements management, PLM) requires substantial integration effort [139]. Proprietary APIs, data formats, and access models complicate integration. Emerging standards such as OSLC provide partial solutions, but coverage remains incomplete and adoption uneven [140]. Research questions: What integration patterns are effective? Can standardized interfaces emerge? (See Section 9.4 for proposed research directions addressing tool integration.)

**Process integration.** Inserting AI agents into established SE processes raises workflow questions [141]. Where do agents participate? How are agent outputs reviewed? How do agent activities align with milestone gates? Research questions: What process adaptations are needed? How should traditional and AI-augmented processes coexist?

**Data integration.** Agent systems require access to engineering data — requirements, models, test results — often distributed across systems with different formats and access controls [139]. Research questions: How can engineering data be made agent-accessible? What data quality requirements apply?

**Legacy system accommodation.** Most SE organizations have substantial investments in existing tools and processes [140]. Agent systems must accommodate legacy constraints rather than requiring greenfield adoption. Research questions: What migration paths are practical? How can value be delivered incrementally?

### 8.3 Human Factors Challenges

**Trust calibration.** Engineers must develop appropriate trust in agent capabilities — neither over-reliance nor excessive skepticism [137]. Trust should be task-specific and evidence-based. Studies in human-robot teaming suggest that trust calibration requires transparent performance feedback and predictable failure modes [137] — characteristics that current LLM agents struggle to provide. Research questions: How does trust develop? What factors support appropriate calibration? How should trust be maintained as capabilities evolve? (See Section 9.5 for proposed research directions addressing trust.)

**Oversight effectiveness.** Human oversight of agent activities becomes challenging as agent count and activity rate increase [142]. Engineers cannot review every agent output; effective oversight requires attention management. Research questions: What oversight models are effective? How should agent outputs be prioritized for review?

**Skill evolution.** Working effectively with agent systems requires skills many engineers lack: formulating effective prompts, evaluating AI outputs, diagnosing agent failures [143]. Research questions: What skills are needed? How should training be structured? How do required skills evolve with technology?

**Cognitive load.** Managing agent systems imposes cognitive demands: understanding agent state, interpreting agent outputs, coordinating agent activities [142]. These demands may offset productivity gains. Research questions: How can cognitive load be managed? What interface designs minimize burden?

**Role clarity.** As agents assume engineering tasks, human roles must evolve [144]. Unclear role boundaries create confusion about responsibilities. Research questions: How should human-agent roles be defined? How should accountability be allocated? (See Section 9.6 for proposed research directions addressing human-agent teaming.)

### 8.4 Organizational Challenges

**Governance frameworks.** Organizations need frameworks governing AI involvement in engineering [145]. What decisions can agents make? How are agent outputs validated? Who is accountable for agent contributions? Research questions: What governance models are appropriate? How should governance evolve with capability? (See Section 9.7 for proposed research directions addressing governance.)

**Certification implications.** In regulated industries, AI involvement raises certification questions [146]. How do AI contributions affect system certification? What evidence is required for AI tool qualification? Research questions: What certification frameworks apply? How should evidence be collected and presented?

**Liability and accountability.** When AI-influenced engineering decisions lead to problems, liability questions arise [145]. Current legal frameworks may not adequately address AI contributions. Research questions: How should liability be allocated? What organizational structures support appropriate accountability?

**Intellectual property.** Deploying AI agents on proprietary engineering data raises intellectual property concerns [147]. Organizations must determine whether agent interactions with proprietary designs, trade secrets, or export-controlled data create unacceptable exposure risks, particularly when using cloud-hosted LLM services. Data residency, model training data provenance, and output ownership require careful contractual and technical controls.

**Workforce transition.** The introduction of agent systems will shift the skill profiles required of systems engineers [146]. Organizations must plan for workforce transition — retraining engineers to supervise and collaborate with AI agents rather than perform tasks agents can handle — while managing the cultural and morale implications of role redefinition.

**Standards body engagement.** Realizing the potential of multi-agent AI for SE will require engagement from standards bodies including INCOSE, IEEE, and ISO [147]. Standards are needed for agent-generated artifact quality, human-agent process interfaces, and certification of AI-augmented engineering workflows. Without such standards, adoption will remain fragmented and organization-specific.

**Change management.** Adopting agent systems represents significant organizational change [145]. Resistance, skill gaps, and process disruption must be managed. Research questions: What adoption approaches succeed? How should change be paced?

**Economic justification.** Agent system adoption requires investment; organizations need evidence of return [146]. Current evidence is limited and context-dependent. Research questions: What value propositions are compelling? How should benefits be measured?

### 8.5 Challenge Prioritization

Table 5 assesses challenges by severity and tractability.

| Challenge | Severity | Tractability | Priority |
|-----------|----------|--------------|----------|
| Reliability | High | Moderate | Critical |
| Domain knowledge | High | Moderate | Critical |
| Trust calibration | High | Moderate | Critical |
| Governance | High | Low | High |
| Scalability | Moderate | Moderate | High |
| Tool integration | Moderate | High | High |
| Certification | High | Low | High |
| Oversight | Moderate | Moderate | Medium |
| Performance | Moderate | High | Medium |
| Skills evolution | Moderate | High | Medium |

Critical challenges (high severity, moderate tractability) warrant immediate research investment. High-priority challenges are either severe or tractable and should receive sustained attention.

---

**Word count:** ~1,080 words
**Subsections:** 5
**Tables:** 1
**References cited:** [135]-[147]

---

## Revision Notes

- [x] Add specific examples for each challenge
- [x] Cite relevant papers addressing each challenge
- [x] Consider expanding organizational challenges
- [x] Add cross-references to solutions in research directions


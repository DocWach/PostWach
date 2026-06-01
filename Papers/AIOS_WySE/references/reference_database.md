# Reference Database for AIOS-WySE Paper
### Status: 2026-03-07

---

## RED TEAM VERIFICATION RESULTS

### Claim-by-Claim Findings

**Claim 1:** "AgentCgroup shows OS execution accounts for 56–74% of end-to-end agent task latency"
STATUS: VERIFIED. The paper confirms exactly this range. Measured across 144 software engineering tasks from SWE-rebench benchmark, using two LLM models. The 56–74% figure reflects OS-level execution (tool calls, container and agent initialization); LLM reasoning accounts for the remaining 26–44%. No material caveats on the range itself, though it is derived from a single benchmark (SWE-rebench) and may not generalize to non-software-engineering agent tasks.

**Claim 2:** "AIOS v5 shows 2.1x faster agent execution. Published at COLM 2025."
STATUS: VERIFIED. Paper published as a conference paper at COLM 2025. The 2.1x figure is confirmed: "up to a 2.1x increase in execution speed for serving agents across different frameworks." The current arXiv version is v4.

**Claim 3:** "MemOS claims 159% improvement in temporal reasoning over OpenAI's global memory on LoCoMo"
STATUS: VERIFIED WITH CLARIFICATION. The 159% figure is confirmed for temporal reasoning on LoCoMo. The two arXiv numbers (2505.22101 and 2507.03724) are the same project: 2505.22101 is the short version (May 2025) titled "MemOS: An Operating System for Memory-Augmented Generation (MAG) in Large Language Models"; 2507.03724 is the full expanded version (July 2025, revised December 2025) titled "MemOS: A Memory OS for AI System." The paper to cite for the LoCoMo benchmark result is 2507.03724. Both should be cited if the paper discusses the project's evolution.

**Claim 4:** "PunkGo / Right to History: sub-1.3ms action latency, logarithmic-size Merkle proofs"
STATUS: PARTIALLY VERIFIED. Sub-1.3ms median action latency: VERIFIED (confirmed in paper). Throughput of ~400 actions/sec: VERIFIED. The Merkle proof claim requires correction: the paper states 448-byte Merkle inclusion proofs at 10,000 log entries. RFC 6962 Merkle tree proofs are logarithmic in proof depth (number of hashes), but the paper reports a fixed byte size (448 bytes) at a specific log size. The claim "logarithmic-size Merkle proofs" is technically accurate as a structural property but the paper does not use that phrasing; it states the concrete size. Recommend citing the 448-byte figure directly rather than "logarithmic-size."

**Claim 5:** "Unikraft raised $6M in October 2025"
STATUS: VERIFIED. BusinessWire announcement dated October 9, 2025. Amount: $6M seed round. Led by Heavybit, with participation from Vercel Ventures, Mango Capital, Firestreak, Fly VC, First Momentum Ventures, and strategic angels.

**Claim 6:** "MCP has 97M+ monthly SDK downloads"
STATUS: VERIFIED. Confirmed by Anthropic's official announcement on December 9, 2025, when donating MCP to the Agentic AI Foundation (Linux Foundation directed fund). Exact language: "over 97 million monthly SDK downloads" across Python and TypeScript SDKs.

**Claim 7:** "Google Fuchsia stable release F27, July 2025"
STATUS: VERIFIED. Fuchsia F27 release notes confirmed on fuchsia.dev. Release date: July 15, 2025. F27 is confirmed as a stable release milestone with documented feature additions (TCP SACK, file-based encryption on Fxfs, Bluetooth FIDL API additions).

**Claim 8:** "seL4 took approximately 20 person-years for ~10,000 lines of C"
STATUS: PARTIALLY VERIFIED — LINE COUNT REQUIRES CORRECTION. The 20 person-year figure is confirmed. However, the C code size is 8,700 lines of C (plus 600 lines of assembler), not "~10,000 lines." The 10,000 figure is a rounded approximation and slightly overstates the C-only line count. Of the 20 person-years, 11 were for the seL4-specific proof; the remaining ~9 were for framework, tooling, and theorem prover extensions. Recommend citing "8,700 lines of C" and "20 person-years" precisely.

**Claim 9:** "NVIDIA H100 GPU TEE: <5% overhead for LLM inference"
STATUS: CORRECTED. The paper (arXiv:2409.03992) states overhead "remains below 7%" for typical LLM queries, not below 5%. Larger models and longer sequences approach zero overhead; the elevated overhead appears for small models (e.g., Llama-3.1-8B) with short sequences. The "<5%" claim overstates the finding. The correct claim is: "below 7% overhead for most typical LLM queries, with near-zero overhead for large models."

**Claim 10:** "AgenticOS 2026 workshop at ASPLOS, March 23, 2026 — os-for-agent.github.io"
STATUS: VERIFIED. The 1st Workshop on Operating Systems Design for AI Agents (AgenticOS 2026) is co-located with ASPLOS 2026, confirmed for March 23, 2026, in Pittsburgh, USA. Official site: https://os-for-agent.github.io/ (confirmed through easychair CFP and ASPLOS 2026 workshop listing).

**Claim 11:** "ACM CAIS 2026, May 26-29, San Jose"
STATUS: VERIFIED. The ACM Conference on AI and Agentic Systems (CAIS 2026) is confirmed. Workshops: May 26 (Tuesday). Main conference: May 27-29 (Wednesday-Friday). Location: San Jose, California. Official site: https://www.caisconf.org/

**Claim 12:** "NIST AI Agent Standards Initiative launched February 2026"
STATUS: VERIFIED WITH PRECISION. The AI Agent Standards Initiative was announced February 17, 2026, by NIST's Center for AI Standards and Innovation (CAISI). Scope: three pillars — (1) industry-led standards development and U.S. leadership in international standards bodies; (2) community-led open-source protocol development; (3) research in AI agent security and identity. Active RFI on AI Agent Security (due March 9, 2026).

**Claim 13:** "SEAgent MAC framework (arXiv:2601.11893)"
STATUS: VERIFIED WITH NAME CORRECTION. The paper exists and describes what is claimed. However, the paper title is "Taming Various Privilege Escalation in LLM-Based Agent Systems: A Mandatory Access Control Framework." The system described is called SEAgent. The paper proposes an attribute-based access control (ABAC) MAC framework that monitors agent-tool interactions via an information flow graph. It defends against indirect prompt injection, RAG poisoning, untrusted agents, and confused deputy attacks with 0% attack success rate in benchmarks.

**Claim 14:** "Agent.xpu (arXiv:2506.24045) — CPU/NPU/iGPU scheduling"
STATUS: VERIFIED. Paper title: "Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC." Describes orchestration of concurrent reactive and proactive LLM flows on commodity SoCs integrating CPUs, iGPUs, and NPUs. Submitted June 30, 2025; latest version January 6, 2026. Performance: 1.2–4.9x proactive throughput improvement, at least 91% reduction in reactive latency.

**Claim 15:** "Omega system (arXiv:2512.05951) — nested isolation within CVM"
STATUS: VERIFIED WITH TITLE CORRECTION. Paper title is "Trusted AI Agents in the Cloud" (not named "Omega" in the title; Omega is the system name within the paper). The nested isolation claim is confirmed: Omega uses VM Privilege Levels (VMPL-0 for trusted monitor, VMPL-1 for runtime, VMPL-2 for agents) to achieve nested isolation within a single CVM. Builds on Confidential VMs and Confidential GPUs.

---

## Verified References (confirmed real, correct claims)

[V1] Y. Zheng et al., "AgentCgroup: Understanding and Controlling OS Resources of AI Agents," arXiv:2602.09345, Feb. 2026. https://arxiv.org/abs/2602.09345 STATUS: VERIFIED.
  - Used in: Section on OS resource management (56–74% latency claim)
  - Note: eBPF-based resource controller; measured on SWE-rebench 144-task benchmark

[V2] B. Shi et al., "AIOS: LLM Agent Operating System," in Proc. COLM 2025, arXiv:2403.16971v4. https://arxiv.org/abs/2403.16971 STATUS: VERIFIED.
  - Used in: Section on agent OS foundations (2.1x execution speed claim)
  - Note: Current version is v4; COLM 2025 publication confirmed

[V3] T. Li et al., "MemOS: A Memory OS for AI System," arXiv:2507.03724, Jul. 2025 (rev. Dec. 2025). https://arxiv.org/abs/2507.03724 STATUS: VERIFIED.
  - Used in: Section on memory management (159% temporal reasoning improvement on LoCoMo)
  - Note: Full version; companion short version is arXiv:2505.22101

[V4] T. Li et al., "MemOS: An Operating System for Memory-Augmented Generation (MAG) in Large Language Models," arXiv:2505.22101, May 2025. https://arxiv.org/abs/2505.22101 STATUS: VERIFIED.
  - Used in: Same section as V3; this is the short/initial version of the same project

[V5] "Right to History: A Sovereignty Kernel for Verifiable AI Agent Execution," arXiv:2602.20214, Feb. 23, 2026. https://arxiv.org/abs/2602.20214 STATUS: VERIFIED.
  - Used in: Section on verifiable execution / provenance (PunkGo system)
  - Note: Sub-1.3ms median action latency and ~400 actions/sec are verified; Merkle proof is 448 bytes at 10,000 entries (see corrected claim)

[V6] "Unikraft Launches With $6M to Drive Dramatic New Efficiencies in Scale and Cost for Cloud Computing in the AI Era," BusinessWire, Oct. 9, 2025. https://www.businesswire.com/news/home/20251009046776/en/Unikraft-Launches-With-$6M-to-Drive-Dramatic-New-Efficiencies-in-Scale-and-Cost-for-Cloud-Computing-in-the-AI-Era STATUS: VERIFIED.
  - Used in: Section on unikernel / lightweight OS (industry traction)

[V7] Anthropic, "Donating the Model Context Protocol and Establishing the Agentic AI Foundation," Dec. 9, 2025. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation STATUS: VERIFIED.
  - Used in: Section on tool ecosystems / MCP (97M+ monthly downloads)

[V8] Fuchsia Team, "Fuchsia F27 Release Notes," fuchsia.dev, Jul. 15, 2025. https://fuchsia.dev/whats-new/release-notes/f27 STATUS: VERIFIED.
  - Used in: Section on capability-safe / microkernel OS landscape

[V9] G. Klein et al., "seL4: Formal Verification of an OS Kernel," in Proc. ACM SOSP, 2009. https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf STATUS: VERIFIED.
  - Used in: Section on formal verification foundations
  - Note: 8,700 lines of C (+ 600 lines assembler), 20 person-years total (11 seL4-specific + ~9 tooling)

[V10] AgenticOS 2026 Workshop, "Operating Systems Design for AI Agents," co-located with ASPLOS 2026, Mar. 23, 2026, Pittsburgh. https://os-for-agent.github.io/ STATUS: VERIFIED.
  - Used in: Introduction / community context

[V11] ACM CAIS 2026, "ACM Conference on AI and Agentic Systems," May 26–29, 2026, San Jose, CA. https://www.caisconf.org/ STATUS: VERIFIED.
  - Used in: Introduction / community context

[V12] NIST CAISI, "Announcing the AI Agent Standards Initiative for Interoperable and Secure Innovation," Feb. 17, 2026. https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure STATUS: VERIFIED.
  - Used in: Policy/standards context section

[V13] J. Ji et al., "Taming Various Privilege Escalation in LLM-Based Agent Systems: A Mandatory Access Control Framework," arXiv:2601.11893, Jan. 2026. https://arxiv.org/abs/2601.11893 STATUS: VERIFIED.
  - Used in: Section on agent security and isolation
  - Note: System name is SEAgent; implements ABAC-based MAC with information flow graph enforcement

[V14] [Author TBD], "Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC," arXiv:2506.24045, Jun. 2025 (rev. Jan. 2026). https://arxiv.org/abs/2506.24045 STATUS: VERIFIED.
  - Used in: Section on heterogeneous hardware scheduling

[V15] T. Bodea, M. Misono, J. Pritzi et al., "Trusted AI Agents in the Cloud," arXiv:2512.05951, Dec. 2025. https://arxiv.org/abs/2512.05951 STATUS: VERIFIED.
  - Used in: Section on confidential computing / nested isolation
  - Note: System name is Omega within the paper; paper title is "Trusted AI Agents in the Cloud"

---

## Corrected References (real, but claims require adjustment)

[C1] [Author TBD], "Confidential Computing on NVIDIA Hopper GPUs: A Performance Benchmark Study," arXiv:2409.03992, Sep. 2024 (rev. Nov. 2024). https://arxiv.org/abs/2409.03992 STATUS: CORRECTED.
  - Original claim: "NVIDIA H100 GPU TEE: <5% overhead for LLM inference"
  - Corrected claim: "NVIDIA H100 GPU TEE: below 7% overhead for typical LLM inference queries; near-zero overhead for large models and long sequences"
  - Note: The <5% figure does not appear in the paper. The paper states "below 7%" as the threshold for most typical queries. The overhead approaches zero for Llama-3.1-70B but is highest for Llama-3.1-8B with short sequences.
  - Used in: Section on confidential computing / hardware TEE

[C2] G. Klein et al., "seL4: Formal Verification of an OS Kernel," SOSP 2009 (see V9 above). STATUS: CORRECTED (line count).
  - Original claim: "~10,000 lines of C"
  - Corrected claim: "8,700 lines of C (plus 600 lines of assembler)" — the 10,000 figure is a rounded overstatement of the C-only count
  - Used in: Section on formal verification

[C3] "Right to History: A Sovereignty Kernel for Verifiable AI Agent Execution," arXiv:2602.20214 (see V5 above). STATUS: CORRECTED (Merkle proof phrasing).
  - Original claim: "logarithmic-size Merkle proofs"
  - Corrected claim: "448-byte Merkle inclusion proofs at 10,000 log entries" — the logarithmic growth is a structural property of RFC 6962 Merkle trees but the paper reports the concrete size; cite the 448-byte figure
  - Used in: Section on verifiable execution

---

## New References to Add (Blue Team Recommendations)

### OS Foundations Textbooks

[B1] A. Silberschatz, G. Gagne, and P. B. Galvin, Operating System Concepts, 10th ed. Wiley, 2018. https://www.os-book.com/OS10/ ISBN: 9781119320913.
  - Justification: Standard OS concepts textbook; needed to anchor definitions of process, scheduler, memory manager, and IPC that Section 3 should ground in classical terminology before introducing WySE extensions.
  - Suggested section: Section 3 (OS Primitives and Abstractions)

[B2] A. S. Tanenbaum and H. Bos, Modern Operating Systems, 4th ed. Pearson, 2015. https://dl.acm.org/citation.cfm?id=2655363 ISBN: 9780133591620.
  - Justification: Covers microkernels, hypervisors, and security models in depth; the microkernel comparison in Section 5 needs this as a counterpoint to seL4.
  - Suggested section: Section 5 (Microkernel Foundations)

[B3] R. H. Arpaci-Dusseau and A. C. Arpaci-Dusseau, Operating Systems: Three Easy Pieces, v1.10. Arpaci-Dusseau Books, 2023. https://pages.cs.wisc.edu/~remzi/OSTEP/
  - Justification: Freely available, widely cited modern pedagogical reference; particularly useful for concurrency and scheduling sections; the scheduling discussion in Section 7 should cite this alongside the more formal references.
  - Suggested section: Section 7 (Scheduling and Resource Management)

### Formal Methods / Verification

[B4] X. Leroy, "Formal Verification of a Realistic Compiler," Commun. ACM, vol. 52, no. 7, pp. 107–115, Jul. 2009. https://dl.acm.org/doi/10.1145/1538788.1538814
  - Justification: CompCert is the canonical example of full formal verification of a complex system artifact (C compiler); citing it alongside seL4 strengthens the Section 13 argument that morphism-grounded correctness proofs are feasible for non-trivial software.
  - Suggested section: Section 13 (Morphism Composition and Formal Assurance)

[B5] R. Krebbers, R. Jung et al., "The Essence of Higher-Order Concurrent Separation Logic," in Proc. ESOP, LNCS 10201, 2017. https://iris-project.org/pdfs/2017-esop-iris3-final.pdf
  - Justification: Iris is the separation logic framework underlying both seL4's proof infrastructure and RefinedC; required citation for Section 13 when claiming that WySE morphism obligations can be discharged via Iris-style separation logic.
  - Suggested section: Section 13

[B6] M. Sammler et al., "RefinedC: Automating the Foundational Verification of C Code with Refined Ownership Types," in Proc. PLDI 2021. https://dl.acm.org/doi/10.1145/3453483.3454036
  - Justification: Most recent automated foundational C verification tool, built on Iris; demonstrates that seL4-style verification cost can be reduced significantly through automation — directly relevant to the paper's argument that AIOS-WySE runtime components can be formally verified without 20-person-year efforts.
  - Suggested section: Section 13

### eBPF and AI Observability

[B7] Y. Zheng et al., "AgentSight: System-Level Observability for AI Agents Using eBPF," in Proc. 4th Workshop on Practical Adoption Challenges of ML for Systems (ACM), 2025, arXiv:2508.02736. https://arxiv.org/abs/2508.02736
  - Justification: Direct companion paper to AgentCgroup from the same research group (eunomia-bpf); completes the eBPF-for-AI picture — AgentCgroup measures resource consumption, AgentSight provides semantic observability. Both should be cited together.
  - Suggested section: Section on eBPF / OS observability

### AI-OS Survey

[B8] Y. Zhang et al., "Integrating Artificial Intelligence into Operating Systems: A Survey on Techniques, Applications, and Future Directions," arXiv:2407.14567v3, Nov. 2025. https://arxiv.org/abs/2407.14567
  - Justification: The most comprehensive current survey of the AI-OS intersection; covers both "AI for OS" and "OS for AI" directions. Establishes the three-stage roadmap (AI-powered → AI-refactored → AI-driven) that the paper's architecture implicitly targets. Citing this prevents the paper from appearing to ignore existing surveys.
  - Suggested section: Section 2 (Related Work / Background)

### Mixed-Criticality and Runtime Assurance

[B9] A. Zuepke and R. Bommert, "AUTOBEST: A United AUTOSAR-OS and ARINC 653 Kernel," in Proc. IEEE RTAS, 2015. https://ieeexplore.ieee.org/document/7108435/
  - Justification: Canonical mixed-criticality OS paper unifying automotive (AUTOSAR) and avionics (ARINC 653) partitioning requirements; the AIOS-WySE isolation model draws on the same spatial/temporal partitioning principles and should acknowledge this lineage.
  - Suggested section: Section on isolation and partitioning

[B10] D. Seto, B. Krogh, L. Sha, and A. Chutinan, "The Simplex Architecture for Safe On-Line Control System Upgrades," in Proc. American Control Conference, 1998. (Also: "The system-level simplex architecture for improved real-time embedded system safety," RTAS.)
  - URL: https://experts.illinois.edu/en/publications/the-simplex-architecture-for-safe-on-line-control-system-upgrades/
  - Justification: Simplex is the classical precedent for the AIOS-WySE circuit-breaker / safe fallback pattern; when Section 12 introduces the bio-inspired circuit breaker switching mechanism, it should acknowledge that runtime assurance via trusted baseline fallback was formalized by Sha and Seto 25+ years earlier.
  - Suggested section: Section 12 (Circuit Breaker / Runtime Assurance)

### Category Theory for Systems Engineering

[B11] B. Fong and D. I. Spivak, An Invitation to Applied Category Theory: Seven Sketches in Compositionality. Cambridge University Press, 2019, arXiv:1803.05316. https://arxiv.org/abs/1803.05316
  - Justification: The canonical accessible reference for applied category theory; Section 13's morphism composition framework sits squarely within this literature and should cite it as the mathematical foundation from which the WySE composition model derives.
  - Suggested section: Section 13 (Morphism Composition)

### Wymore's Original Formalizations

[B12] A. W. Wymore, A Mathematical Theory of Systems Engineering: The Elements. John Wiley & Sons, New York, 1967. https://openlibrary.org/books/OL5544238M/A_mathematical_theory_of_systems_engineering
  - Justification: Wymore's original five-tuple system model and homomorphism theory; foundational citation for the WySE Metamodel. Must cite alongside the 1993 MBSE book.
  - Suggested section: Section 4 (WySE Metamodel Foundations)

[B13] A. W. Wymore, Model-Based Systems Engineering. CRC Press, Boca Raton, FL, 1993. ISBN: 9780849380129. https://www.routledge.com/Model-Based-Systems-Engineering/Wymore/p/book/9780849380129
  - Justification: Wymore's mature treatment of system coupling, homomorphic relationships, and T3SD requirements; the operational formalization used in the paper derives from this work.
  - Suggested section: Section 4

---

## Unverified References (could not confirm — flag for manual review)

[U1] AIOS v5 version number — STATUS: UNVERIFIED (version label).
  - The paper (arXiv:2403.16971) confirms the 2.1x result and COLM 2025 publication. However, the current arXiv version is v4, not v5. The claim "AIOS v5" may refer to an internal version number used in the paper's evaluation rather than the arXiv version number. Verify directly in the paper's experiment section whether the 2.1x result is attributed to a component labeled "v5."
  - Issue: No independent source found referring to "AIOS v5"; the paper's arXiv listing shows v4 as the current version.

[U2] Fuchsia as a "stable" OS used in production — STATUS: UNVERIFIED (stability claim).
  - The F27 release notes exist and the release is confirmed. However, Fuchsia remains primarily a developer-facing / embedded OS (used in Google Nest Hub devices). Whether "stable release F27" implies production-ready general-purpose OS stability or merely a versioned developer milestone is ambiguous. Verify the intended framing before using this to support a strong architectural claim.
  - Issue: Fuchsia is not a widely-deployed general-purpose OS; its relevance to AIOS-WySE requires explicit justification.

[U3] MCP 97M monthly downloads — attribution precision — STATUS: PARTIALLY VERIFIED.
  - The 97M+ figure is confirmed from Anthropic's December 2025 announcement. However, the downloads span Python and TypeScript SDKs and represent monthly downloads across all users (including CI/CD pipelines and automated systems), not necessarily unique human developers. If citing as an adoption metric, qualify that this is SDK download count, not unique deployments.
  - Issue: Raw SDK download counts may overstate active adoption; cite with appropriate qualification.

[U4] AIOS "v5" performance number source — STATUS: NEEDS MANUAL VERIFICATION.
  - Need to open the full COLM 2025 paper (arXiv:2403.16971v4) and confirm whether the 2.1x speedup is labeled as coming from "AIOS v5" specifically, or from a different version label.
  - URL: https://arxiv.org/pdf/2403.16971

---

## Notes for Later Numbering Pass

When unifying reference numbers across all paper sections, this database uses the following prefixes as temporary identifiers:
- [V1]–[V15]: Verified original claims
- [C1]–[C3]: Corrected original claims (the corrected version should be used)
- [B1]–[B13]: Blue Team additions to add to the bibliography
- [U1]–[U4]: Unverified items requiring manual review before use

All final reference numbers will be assigned in the bibliography unification pass. Cross-section usage is noted in the "Used in" and "Suggested section" fields above.

Sources used in verification:
- [AgentCgroup paper](https://arxiv.org/abs/2602.09345)
- [AIOS paper v4](https://arxiv.org/abs/2403.16971v4)
- [MemOS full version](https://arxiv.org/abs/2507.03724)
- [MemOS short version](https://arxiv.org/abs/2505.22101)
- [Right to History / PunkGo](https://arxiv.org/abs/2602.20214)
- [Unikraft funding announcement](https://www.businesswire.com/news/home/20251009046776/en/Unikraft-Launches-With-%246M-to-Drive-Dramatic-New-Efficiencies-in-Scale-and-Cost-for-Cloud-Computing-in-the-AI-Era)
- [MCP Agentic AI Foundation announcement](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [Fuchsia F27 release notes](https://fuchsia.dev/whats-new/release-notes/f27)
- [seL4 SOSP 2009 paper](https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf)
- [H100 TEE benchmark](https://arxiv.org/abs/2409.03992)
- [AgenticOS 2026 workshop](https://os-for-agent.github.io/)
- [ACM CAIS 2026](https://www.caisconf.org/)
- [NIST AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure)
- [SEAgent paper](https://arxiv.org/abs/2601.11893)
- [Agent.xpu paper](https://arxiv.org/abs/2506.24045)
- [Omega / Trusted AI Agents paper](https://arxiv.org/abs/2512.05951)
- [AgentSight paper](https://arxiv.org/abs/2508.02736)
- [AI-OS survey](https://arxiv.org/abs/2407.14567)
- [Wymore 1967 on Open Library](https://openlibrary.org/books/OL5544238M/A_mathematical_theory_of_systems_engineering)
- [Wymore 1993 on Routledge](https://www.routledge.com/Model-Based-Systems-Engineering/Wymore/p/book/9780849380129)
- [Fong and Spivak applied category theory](https://arxiv.org/abs/1803.05316)
- [RefinedC PLDI 2021](https://dl.acm.org/doi/10.1145/3453483.3454036)
- [Iris ESOP 2017](https://iris-project.org/pdfs/2017-esop-iris3-final.pdf)
- [CompCert CACM 2009](https://dl.acm.org/doi/10.1145/1538788.1538814)
- [AUTOBEST RTAS 2015](https://ieeexplore.ieee.org/document/7108435/)
- [Simplex architecture](https://experts.illinois.edu/en/publications/the-simplex-architecture-for-safe-on-line-control-system-upgrades/)
- [OSTEP textbook](https://pages.cs.wisc.edu/~remzi/OSTEP/)
- [Silberschatz OSC 10th edition](https://www.os-book.com/OS10/)
- [Tanenbaum Modern OS 4th edition](https://dl.acm.org/citation.cfm?id=2655363)

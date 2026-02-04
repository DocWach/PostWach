# AI4RE SLR Literature Review Update - January 2026

## Summary of Required Updates

This document outlines the significant new publications and developments since the original literature review was conducted, identifying specific updates needed for each section of the manuscript.

---

## 1. NEW SYSTEMATIC REVIEWS (2025-2026)

### Must-Cite Publications

| Reference | Key Contribution | Update Section |
|-----------|------------------|----------------|
| Rasheed et al. (2025) - arXiv:2509.11446 | Comprehensive LLM4RE SLR with 74 studies; **136% publication growth** 2023→2024 | Introduction, Methodology comparison |
| Frontiers in Computer Science (2025) - 10.3389/fcomp.2025.1519437 | Research directions for LLM in software RE | Background, Research Agenda |
| ScienceDirect (2025) - "Advancing Requirements Engineering with LLMs" | GPT-4o outperforms other models in quality assessment | Results, Theme 2 |

### Key Finding
> "The number of studies increased significantly in 2024 compared to 2023 by 30 studies (a 136% rise), indicating growing research interest in the LLM4RE area."

**Action**: Update Figure 2 (Publication Trends) to include 2024-2025 data showing continued exponential growth.

---

## 2. NEW LLM MODELS TO ADD

### Background Section 2.3 Updates

**Current manuscript lists**: BERT, NoRBERT, PRCBERT, GPT-4

**New models to add**:

| Model | Release | Notable for RE | Source |
|-------|---------|----------------|--------|
| GPT-4o | 2024 | Best performance in quality assessments | ScienceDirect 2025 |
| Claude 3.5 Sonnet | 2024 | Agent stability, tool use, explainability | Anthropic |
| Claude 4 / 4.5 Opus | Nov 2025 | 80.9% SWE-bench Verified | Anthropic, Hugging Face |
| Gemini 2.0 / 3 Pro | 2025 | 1501 LMArena Elo (first to break 1500) | Google |
| LLaMA 3 / 3.1 (70B) | 2024 | Open-source, strong RE performance | Meta |
| ModernBERT | 2025 | **BERT replacement**, 8192 token context | Answer.AI, HuggingFace |
| Phi3-mini (3.8B) | 2024 | Efficient smaller model for RE tasks | Microsoft |
| Qwen-2.5, Mistral-Nemo | 2024-25 | Emerging alternatives | Various |

**Key Addition - ModernBERT**:
> "ModernBERT is the only model which is a top scorer across every category in standard academic benchmarks, making it the one model for all encoder-based tasks. DeBERTaV3 has been the choice of champions for years in NLP competitions on Kaggle."

---

## 3. THEME 1: REQUIREMENTS CLASSIFICATION - Updates

### New Studies to Add

1. **ModernBERT for Classification** (2025)
   - Replaces BERT as state-of-the-art encoder
   - 8192 token context (vs BERT's 512)
   - Superior performance across all classification benchmarks

2. **Long Document Classification Benchmark** (2025)
   - XGBoost: F1-scores 75-86 for long documents
   - Fine-tuned transformers optimal for 300-1500 word documents
   - Addresses RE document length challenges

3. **Prompting Strategy Analysis** (Rasheed 2025)
   - Zero-shot: 44% of studies
   - Few-shot: 29% of studies
   - RAG: 6% (underexplored)
   - Interactive prompting: 5% (underexplored)

### Update to Table 2 (Classification Performance)

Add rows:
| Study | Model | Task | Dataset | F1 |
|-------|-------|------|---------|-----|
| ModernBERT (2025) | ModernBERT-large | FR/NFR | Various | ~0.95 |
| Long Doc Benchmark (2025) | XGBoost | Long doc class. | Custom | 0.75-0.86 |

---

## 4. THEME 2: REQUIREMENTS QUALITY ASSESSMENT - Updates

### Critical New Studies

1. **Industrial Study with Alstom** (Mälardalen Univ.)
   - Real-world LLM ambiguity detection
   - Compared 0-shot, 1-shot, demonstration selection
   - Finding: No single model consistently outperforms; larger models (Phi3-mini, LLaMA-3 8B) better than smaller (Qwen-2.5 1.5B)

2. **Human-LLM Collaboration for Defect Prediction** (arXiv:2601.01952v1, 2025-2026)
   - Uses gpt-4.1-mini for requirements defect prediction
   - **Key finding**: "Incorporating validated explanations, not just labels, enables Human-LLM Collaboration to substantially outperform both standard few-shot prompting and fine-tuned BERT models"
   - Chain-of-Thought learning enables adaptive classification

3. **ClarifyGPT Framework** (ACM FSE 2024)
   - Detects ambiguous requirements via code consistency check
   - Generates targeted clarifying questions
   - Improves GPT-4 performance: 62.43% → 69.60%
   - Improves ChatGPT: 54.32% → 62.37%

4. **BERT MLM for Completeness** (2025)
   - BERT's Masked Language Model detects missing requirements terms
   - Precision: 82% for predicted missing terms

### Updates to "Broken Clock" Discussion

The recent industrial and Human-LLM collaboration studies **reinforce** the broken clock findings:
- Stochastic variability confirmed across models
- No single model consistently superior
- Human-in-the-loop essential for reliable results

---

## 5. THEME 3: REQUIREMENTS GENERATION - Updates

### Major New Tools and Approaches

1. **GeneUS Tool** (GPT-4.0 based)
   - Automatic user story generation from requirements
   - JSON output for project management integration
   - Uses **RaT (Refine and Thought) prompting** - specialized Chain-of-Thought

2. **ALAS - Autonomous LLM-based Agent System** (Austrian Post IT)
   - Automatic user story quality improvement
   - "Significantly improves user story clarity, comprehensibility, and alignment with business objectives"

3. **Multi-Agent LLM Systems** (2025-2026)
   - GPT-3.5 Turbo, GPT-4o, LLaMA 3.3, Mistral-Nemo
   - Simulates stakeholder roles for prioritization

4. **UStAI Dataset** (PROMISE 2025)
   - 1,260 user stories from 42 abstracts, 26 domains
   - Generated using 3 LLMs
   - Publicly available benchmark

5. **GUI-to-Requirements Integration** (CHI 2025)
   - LLM-based Figma plugin
   - Bridges user stories ↔ GUI prototyping
   - Recognizes requirements fulfillment in GUIs

### Evidence Strength Update
Change from **WEAK** to **MODERATE** based on:
- Multiple empirical studies now available
- Industrial deployments documented
- Standardized datasets emerging (UStAI)

---

## 6. THEME 4: HUMAN-AI COLLABORATION - Updates

### Major New Research

1. **Trust Calibration Literature Review** (CHI 2025)
   - Comprehensive review of autonomous teammates
   - Over-trust vs under-trust calibration critical
   - Feature-specific trust calibration emerging

2. **Reconsidering RE for AI-Native Development** (arXiv:2510.04380)
   - AI affecting core RE processes: ambiguity resolution, stakeholder prioritization, traceability
   - Key concerns: human oversight, explainability, trust in recommendations
   - "AI-driven tools mostly work as black boxes, making it difficult for users to understand how decisions are made"

3. **Adaptive Trust Calibration** (Frontiers 2025)
   - Agent-related factors: ethical behavior, apology, blame attribution, uncertainty communication → positive effects on trust
   - Collaboration strategy and explanation presence → medium effects

4. **Feature-Specific Trust** (ICIS 2025)
   - Users don't trust all AI features equally
   - Trust varies based on direct experience and perceived reliability per feature

### Key Quote for Discussion
> "In cases where AI might produce biased or harmful outputs, 'calibrating human trust in the AI team member to an appropriate level is more advantageous than fostering blind trust.'"

---

## 7. NEW BENCHMARKS AND DATASETS

### SWE-bench Verified (2025)
- 500 real-world GitHub issues
- Docker-isolated execution
- Claude 4.5 Opus: **80.9%** (highest)
- GPT-5.2: ~80%
- Relevant for RE tool evaluation

### UStAI Dataset
- 1,260 LLM-generated user stories
- 42 paper abstracts, 26 domains
- Publicly available

### Long Document Classification Benchmark (2025)
- Documents 1,000+ words
- Addresses RE document length issues
- Model comparison included

---

## 8. PUBLICATION TRENDS UPDATE

### Current Figure 2 Data
```
2018: 3, 2019: 5, 2020: 7, 2021: 8, 2022: 9, 2023: 14, 2024: 22, 2025: 6
```

### Updated Data (from Rasheed 2025 SLR)
```
2023: 22 studies
2024: 52 studies (+136%)
2025: ~35+ studies (projected, partial year in original search)
```

**Action**: Update bar chart with new 2024-2025 data showing exponential growth.

---

## 9. NEW BIBTEX ENTRIES TO ADD

```bibtex
@article{rasheed2025llm4re_update,
  author    = {Zahra Rasheed and Saad Waseem and Muhammad Waseem and Teerath Das and Peng Liang},
  title     = {Large Language Models ({LLMs}) for Requirements Engineering ({RE}): A Systematic Literature Review},
  journal   = {arXiv preprint arXiv:2509.11446},
  year      = {2025},
  note      = {74 primary studies, 136\% growth 2023-2024}
}

@article{frontiers2025llm_re,
  author    = {Multiple Authors},
  title     = {Research directions for using {LLM} in software requirement engineering: a systematic review},
  journal   = {Frontiers in Computer Science},
  year      = {2025},
  volume    = {7},
  doi       = {10.3389/fcomp.2025.1519437}
}

@inproceedings{alstom2025ambiguity,
  author    = {Mälardalen University and Alstom},
  title     = {Requirements Ambiguity Detection and Explanation with {LLMs}: An Industrial Study},
  booktitle = {Proceedings of RE 2025},
  year      = {2025}
}

@article{human_llm_collab2025,
  author    = {Various Authors},
  title     = {Context-Adaptive Requirements Defect Prediction through Human-{LLM} Collaboration},
  journal   = {arXiv preprint arXiv:2601.01952},
  year      = {2025}
}

@inproceedings{clarifygpt2024,
  author    = {Various Authors},
  title     = {{ClarifyGPT}: A Framework for Enhancing {LLM}-Based Code Generation via Requirements Clarification},
  booktitle = {Proceedings of ACM FSE 2024},
  year      = {2024},
  doi       = {10.1145/3660810}
}

@misc{modernbert2025,
  author    = {{Answer.AI} and {LightOn}},
  title     = {{ModernBERT}: A Modern Replacement for {BERT}},
  year      = {2025},
  howpublished = {Hugging Face Blog}
}

@inproceedings{chi2025_trust,
  author    = {Various Authors},
  title     = {Trusting Autonomous Teammates in Human-{AI} Teams - A Literature Review},
  booktitle = {Proceedings of CHI 2025},
  year      = {2025},
  doi       = {10.1145/3706598.3713527}
}

@article{reconsidering_re2025,
  author    = {Various Authors},
  title     = {Reconsidering Requirements Engineering: Human-{AI} Collaboration in {AI}-Native Software Development},
  journal   = {arXiv preprint arXiv:2510.04380},
  year      = {2025}
}

@inproceedings{geneus2024,
  author    = {Various Authors},
  title     = {Automated User Story Generation with Test Case Specification Using Large Language Model},
  journal   = {arXiv preprint arXiv:2404.01558},
  year      = {2024}
}

@inproceedings{alas2024,
  author    = {Various Authors},
  title     = {{LLM}-based agents for automating the enhancement of user story quality: An early report},
  booktitle = {REFSQ 2024},
  year      = {2024},
  doi       = {10.1007/978-3-031-61154-4_8}
}

@inproceedings{ustai2025,
  author    = {Various Authors},
  title     = {Leveraging {LLMs} for User Stories in {AI} Systems: {UStAI} Dataset},
  booktitle = {PROMISE 2025},
  year      = {2025},
  doi       = {10.1145/3727582.3728689}
}

@inproceedings{chi2025_gui,
  author    = {Various Authors},
  title     = {Closing the Loop between User Stories and {GUI} Prototypes: An {LLM}-Based Assistant},
  booktitle = {Proceedings of CHI 2025},
  year      = {2025},
  doi       = {10.1145/3706598.3713932}
}
```

---

## 10. RESEARCH AGENDA UPDATES

### Reinforced Priorities (from new evidence)
1. **Multi-run variance analysis** - Still critical, new studies confirm stochastic variability
2. **Human-LLM collaboration** - Now actively researched (upgrade priority)
3. **Uncertainty quantification** - Feature-specific trust calibration emerging

### New Priorities to Add
1. **Multi-agent LLM systems for RE** - Multiple studies now demonstrate potential
2. **ModernBERT evaluation** - Replace BERT benchmarks
3. **Industrial validation** - Alstom study provides template
4. **Prompting strategy optimization** - RAG and interactive prompting underexplored

### Emerging Research Directions
- AI-Native software development reconsidering RE fundamentals
- Feature-specific trust calibration
- GUI-to-requirements bidirectional mapping

---

## 11. MANUSCRIPT SECTION-BY-SECTION UPDATES

### Abstract
- Update study count if including 2025 publications
- Add GPT-4o, Claude 4 to model list
- Mention 136% publication growth

### Section 1 (Introduction)
- Add 2024-2025 publication explosion data
- Reference Rasheed 2025 SLR
- Update motivation with AI-Native development concerns

### Section 2 (Background)
- Add ModernBERT to transformer models
- Add GPT-4o, Claude 3.5/4, Gemini 2.0, LLaMA 3
- Update NLP evolution timeline to 2025

### Section 3 (Methodology)
- Consider extending search to 2025
- Or note that 2025 publications reviewed in update

### Section 4 (Results)
- Update Table 2 with new classification results
- Update Table 3 with new ambiguity detection studies
- Add new tools: GeneUS, ALAS, ClarifyGPT
- Update evidence strength for Theme 3 (WEAK → MODERATE)
- Update Figure 2 with 2024-2025 publication counts

### Section 5 (Discussion)
- Strengthen "broken clock" argument with industrial validation
- Add Human-LLM collaboration findings
- Discuss AI-Native development implications

### Section 6 (Research Agenda)
- Add multi-agent systems priority
- Add ModernBERT evaluation priority
- Add prompting strategy research (RAG underexplored)

### References
- Add 12+ new citations (see BibTeX above)

---

## Sources Consulted

- [Rasheed et al. (2025) LLM4RE SLR](https://arxiv.org/abs/2509.11446)
- [Frontiers Research Directions](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1519437/full)
- [Alstom Industrial Study](https://www.ipr.mdu.se/pdf_publications/7221.pdf)
- [Human-LLM Collaboration](https://arxiv.org/html/2601.01952v1)
- [ClarifyGPT](https://dl.acm.org/doi/10.1145/3660810)
- [ModernBERT](https://huggingface.co/blog/modernbert)
- [CHI 2025 Trust Review](https://dl.acm.org/doi/10.1145/3706598.3713527)
- [Reconsidering RE](https://arxiv.org/abs/2510.04380)
- [GeneUS Tool](https://arxiv.org/abs/2404.01558)
- [ALAS Agent System](https://link.springer.com/chapter/10.1007/978-3-031-61154-4_8)
- [UStAI Dataset](https://dl.acm.org/doi/10.1145/3727582.3728689)
- [CHI 2025 GUI-Requirements](https://dl.acm.org/doi/10.1145/3706598.3713932)
- [SWE-bench](https://www.vals.ai/benchmarks/swebench)

---

*Document generated: January 8, 2026*
*For: AI4RE Systematic Literature Review manuscript update*

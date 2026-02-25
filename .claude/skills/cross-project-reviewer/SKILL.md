---
name: Cross-Project Reviewer
description: Review capabilities from any project for governance compliance, duplicate detection, and technical quality
---

# Cross-Project Reviewer

A CTO-level review protocol for evaluating capabilities across the research portfolio. PostWach (CTO/Chief Scientist) assesses what is built and how well; Alpha Empress (COO) assesses whether rules are followed and governance is configured. This skill covers the CTO scope.

## When to Use This Skill

- A project adds new skills or agents and needs portfolio-level review
- Quarterly portfolio review across all Tier 1/2 projects
- Before sharing capabilities from one project to another (reuse assessment)
- Governance audit to assess compliance maturity across the portfolio
- Checking for duplicate or overlapping capabilities before building something new

---

## Quick Start

```bash
# Review a single project's capabilities
claude-flow hive-mind spawn "Review [project name] capabilities. Execute the 4-step CTO review protocol against docs/project-registry.md and docs/capability-index.md. Report findings." \
  --queen research-strategic \
  --workers methodology-advisor,research-architect,code-analyzer

# Review a newly added capability
claude-flow hive-mind spawn "Review new [skill/agent name] in [project]. Check for duplicates against docs/capability-index.md. Assess technical quality. Recommend registry/index updates." \
  --queen research-strategic \
  --workers methodology-advisor,code-analyzer

# Quarterly portfolio review (all Tier 1 projects)
claude-flow hive-mind spawn "Execute quarterly CTO review across all Tier 1 projects: PostWach, MACQ, GI-JOE, COSYSMO, SysMLv2, SEAD. Run the 4-step protocol for each. Produce consolidated report with cross-project findings." \
  --queen research-strategic \
  --workers methodology-advisor,research-architect,code-analyzer
```

---

## Core Methodology

### 4-Step CTO Review Protocol

#### Step 1: Governance Compliance (delegated to Alpha Empress)

Governance compliance is assessed by Alpha Empress (COO) using the 12-check compliance-checker skill. The CTO consumes the Alpha Empress report as Step 1 input rather than running its own checklist.

**To invoke:** Run the Alpha Empress compliance-checker against the target project path. The skill is defined at `01_Alpha_Impress_Disruptor/.claude/skills/compliance-checker/SKILL.md`.

**What it checks (4 severity levels, 12 checks):**
- **Critical:** CLAUDE.md exists, no committed secrets
- **High:** V3 rule annotations, security rule at risk:critical, claude-flow CLI rule
- **Medium:** Standard sections, Cross-Project Role, no npx references, .gitignore
- **Low:** Conciseness (<80 lines), no emoji, type classification in registry

**Output classification (consumed as Step 1 rating):**

| Alpha Empress Rating | CTO Step 1 Rating |
|---|---|
| COMPLIANT | V3 Compliant |
| PARTIALLY COMPLIANT | Partially Compliant |
| NON-COMPLIANT | Non-Compliant |

**Fallback:** If no Alpha Empress report is available, the CTO may assess governance using the criteria above as a manual checklist.

#### Step 2: Capability Duplicate Detection

Check the new or reviewed capability against `docs/capability-index.md`.

**Procedure:**
1. Read the capability's SKILL.md or agent .md file
2. Search the capability-index.md for skills/agents with overlapping purpose
3. Check the Common Infrastructure Pack — is this already provided by the template?
4. Classify the relationship:

| Classification | Definition | Recommendation |
|---|---|---|
| Duplicate | Same purpose, same approach, different project | **Reuse** the existing capability; remove the duplicate |
| Extension | Builds on existing capability with domain-specific additions | **Extend** — acceptable if the extension is in the domain project |
| Complementary | Related domain but distinct purpose | **Accept** — document the relationship in capability-index.md |
| Novel | No existing capability covers this purpose | **Accept** — add to capability-index.md |

#### Step 3: Technical Quality Assessment

Assess the quality of the skill or agent using the appropriate criteria set.

**Skill quality criteria:**
- YAML frontmatter follows pattern: `name` + `description` only (no extra fields)
- Standard sections present: When to Use, Quick Start, Core Methodology
- Reuses existing agents where possible (check against agent roster)
- Spawn commands use correct `claude-flow hive-mind` syntax
- Output templates provided for structured results

**Agent quality criteria:**
- Pattern B markdown format (structured .md file)
- Clear purpose statement distinguishing it from similar agents
- Integration patterns specified (what skills invoke it, what swarms include it)
- No overlap with common infrastructure agents

**Research quality criteria** (when reviewing research-producing capabilities):
- Methodology is rigorous and reproducible
- Validity threats are acknowledged
- IEEE citation style used
- Outputs align with publication targets

**Recommended reviewers:** `methodology-advisor` (research quality), `research-architect` (structural design), `code-analyzer` (technical implementation)

#### Step 4: Registry / Index Update Recommendations

Based on Steps 1-3, recommend updates to the reference documents.

**For `docs/project-registry.md`:**
- Update skill/agent counts if changed
- Update governance rating if compliance changed
- Add new projects if discovered
- Update status (Active/Maintenance/Dormant/Archive)

**For `docs/capability-index.md`:**
- Add new domain-specific capabilities to the project's section
- Update the Cross-Project Reuse Opportunities table if new integrations identified
- Add findings to the Duplicate/Overlap Watch section

---

## CTO vs. COO Distinction

| Aspect | PostWach (CTO) | Alpha Empress (COO) |
|---|---|---|
| **Question** | What is built? How well? | Are rules followed? Is governance configured? |
| **Scope** | Capability quality, duplication, reuse, technical design | CLAUDE.md compliance, rule annotations, file organization |
| **Method** | 4-step review protocol (this skill) | 12-check compliance-checker skill |
| **Authority** | Recommends; project owners decide | Enforces; flags non-compliance |
| **Status** | Active | Active |

These roles are complementary and non-overlapping. Step 1 of the CTO review protocol has been replaced by Alpha Empress's authoritative compliance assessment.

---

## Integration with Claude Flow

### Spawn Commands

```bash
# Single-project review
claude-flow hive-mind spawn "Execute CTO review protocol for [project name]. \
  Step 1: Read Alpha Empress compliance report (or run compliance-checker if no report available). \
  Step 2: Check capabilities against docs/capability-index.md for duplicates. \
  Step 3: Assess technical quality of domain-specific skills/agents. \
  Step 4: Recommend registry/index updates. \
  Produce a CTO Review Report." \
  --queen research-strategic \
  --workers methodology-advisor,research-architect,code-analyzer

# New capability review
claude-flow hive-mind spawn "Review new capability: [name] in [project]. \
  Read the SKILL.md or agent .md. \
  Run Steps 2-4 of the CTO review protocol. \
  Focus on duplicate detection and quality. \
  Produce a Capability Review Report." \
  --queen research-strategic \
  --workers methodology-advisor,code-analyzer

# Quarterly portfolio review (Alpha Empress runs compliance on each project first, then CTO runs Steps 2-4)
claude-flow hive-mind spawn "Execute quarterly CTO portfolio review. \
  For each Tier 1 project (PostWach, MACQ, GI-JOE, COSYSMO, SysMLv2, SEAD): \
  consume Alpha Empress compliance report as Step 1, then run Steps 2-4. \
  For each Tier 2 project (Alpha Empress, PLM, BP Marketing, UAOS, Claude_code_test_setup): \
  consume Alpha Empress compliance report as Step 1, then run Step 2 only. \
  Produce a Quarterly Portfolio Report with cross-project findings." \
  --queen research-strategic \
  --workers methodology-advisor,research-architect,code-analyzer
```

### Memory Storage

```bash
# Store review result
claude-flow memory store \
  --key "cross-project-review/[project]/$(date +%Y-%m-%d)" \
  --value '{"governance": "V3 Compliant|Partial|Non-Compliant", "duplicates_found": 0, "quality_rating": "Pass|Needs Work|Fail", "index_updates": [...]}' \
  --namespace cross-project-review

# Store quarterly portfolio summary
claude-flow memory store \
  --key "cross-project-review/quarterly/$(date +%Y-%m-%d)" \
  --value '{"projects_reviewed": N, "governance_upgrades_needed": [...], "new_reuse_opportunities": [...], "duplicates_flagged": [...]}' \
  --namespace cross-project-review
```

---

## Output Templates

### CTO Review Report

```
CTO REVIEW REPORT
Date: [YYYY-MM-DD]
Project: [name]
Reviewer: PostWach CTO Protocol

STEP 1 — GOVERNANCE COMPLIANCE (Alpha Empress)
  Rating: [V3 Compliant / Partially Compliant / Non-Compliant]
  Source: Alpha Empress compliance-checker report
  Critical: [2/2] High: [3/3] Medium: [X/4] Low: [X/3]
  Issues: ___

STEP 2 — DUPLICATE DETECTION
  Capabilities reviewed: [N]
  Duplicates found: [N]
  Details:
    - [capability]: [Duplicate / Extension / Complementary / Novel] → [recommendation]

STEP 3 — TECHNICAL QUALITY
  Skills assessed: [N]
  Agents assessed: [N]
  Findings:
    - [capability]: [Pass / Needs work] — [notes]

STEP 4 — REGISTRY/INDEX UPDATES
  project-registry.md changes:
    - ___
  capability-index.md changes:
    - ___

SUMMARY
  Overall assessment: [Healthy / Needs Attention / Action Required]
  Priority actions:
    1. ___
    2. ___
```

---

## CTO/COO Integration (Active)

Alpha Empress governance tooling is active. The integration works as follows:

1. **Step 1 delegation:** The CTO review consumes Alpha Empress's compliance report as Step 1 input. The manual checklist is retained as fallback only.
2. **Dual-review trigger:** When any project adds skills/agents, both Alpha Empress (governance) and PostWach (capability) review it.
3. **No changes to Steps 2-4.** The CTO's capability assessment, quality review, and index updates remain independent.

Activated 2026-02-24.

---

*Maintained by PostWach (CTO role). CTO/COO integration active (Phase C, 2026-02-24).*

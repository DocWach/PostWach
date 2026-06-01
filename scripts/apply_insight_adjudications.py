"""One-off: bulk-apply proposed adjudications to reviewer_feedback.yaml.

Inserts an `adjudication:` block under each comment's `independent_assessment:` block
for comments that don't yet have one. Skips comments that already do.

Usage:
    python apply_insight_adjudications.py <yaml_path>
"""
from __future__ import annotations

import sys
import textwrap
from pathlib import Path


ADJUDICATIONS = {
    "2":  ("accept",                    "Apply global find/replace. Keep 'SE' only inside 'AI-SE'. Spell out 'systems engineering' elsewhere.", "pending"),
    "3":  ("accept",                    "Use colon-led category labels: 'Accelerating cycles:' and 'SE practice adoption lag:'. Apply consistently to other category-like leads.", "pending"),
    "4":  ("accept",                    "Add a short paragraph at end of introduction acknowledging that paradigm progression is cumulative, not substitutional. SE often picks the simplest sufficient AI for explainability and assurance. The accelerating-cycles point still holds; it concerns which paradigm owns the frontier, not which paradigms are still in service. Sets up #11 hybrid-systems point and #30 validation discussion.", "pending"),
    "6":  ("accept",                    "Regenerate Figure 1 at higher resolution with larger date labels. If still illegible at INSIGHT page width, split into two stacked figures (timeline above; paradigm summary below). Verify at production size.", "pending"),
    "9":  ("accept",                    "Adopt R1's specific wording: 'expert systems proved too brittle for disciplines that demand broad rulesets, like systems engineering. Expert systems remain effective today for narrower, well-bounded tasks; the limitation is scope, not the paradigm itself.' Disarms #4 complete-replacement framing.", "pending"),
    "10": ("accept",                    "Resolves automatically once #4 is addressed. Optionally add a parenthetical to the Houston citation noting the work continued into the LLM era, demonstrating that expert-systems-style structures remained useful after the paradigm front moved on.", "pending"),
    "11": ("accept",                    "Add a forward-pointer at the end of the Houston subsection: rule-based reasoning re-emerges, in hybrid form, in the agentic section, where explicit rules are encoded into generative agents to bound their behavior. Add a backward reference in the agentic section calling Houston a precursor to current agent guardrail patterns.", "pending"),
    "13": ("accept",                    "Add one sentence after the ML enumeration: in SE practice, early neural networks were adopted in the early 2000s as surrogate models for expensive simulations and as data-driven companions to physics-based models, anticipating the data-fusion methods used in the PHM Testbed. Cite a canonical SE-surrogate-model reference (Forrester/Sobester/Keane or domain-specific). Coordinate with #16 toolchain naming.", "pending"),
    "15": ("accept",                    "Adopt a two-bullet template at the end of every Case Study subsection (Houston, PHM, TurboArch, GenGroves, MACQ): (1) what this paradigm enabled that the prior could not; (2) where this paradigm reached its ceiling. Houston already has both; PHM, TurboArch, GenGroves, MACQ need explicit additions. Top revision priority. Resolves #22, #26, #28, #30 simultaneously.", "pending"),
    "20": ("accept",                    "In the LLM Case Study, focus only on TurboArch's LLM-native aspects (retrieval, evidence synthesis, ility prediction). Move the agentic-territory framing to a brief forward-pointer to the agentic section. Keep each case study one paradigm wide.", "pending"),
    "22": ("accept",                    "Add a 'what GenGroves does' workflow paragraph: a concrete user-visible scenario (modeler asks GenGroves to cross-reference an architecture decision against domain SME knowledge; GenGroves orchestrates four specialized models and returns a synthesized recommendation with provenance). Then apply the #15 capability+limitation bullets.", "pending"),
    "24": ("accept",                    "Add a clarifying contrast: orchestrated agents = central planner dispatches specialized models on a fixed pipeline (GenGroves); swarm = autonomous agents with peer coordination, shared memory, and consensus (MACQ). Orchestration is graph-shaped and pre-planned; swarm is emergent. Orchestration is easier to validate; swarm is more capable but harder to assess (links to #26/#30). Lift framing from MACQ/hive-of-hives memory.", "pending"),
    "26": ("accept",                    "Surface the assessability-decreases-as-paradigms-evolve argument explicitly. Slower-arriving paradigms had built-in time for validation maturation; current paradigms arrive faster than validation methods. Tie back via callouts in each case study limitation bullets (merges with #15). Add to conclusion alongside #30.", "pending"),
    "28": ("accept",                    "Resolves automatically once #15 capability+limitation bullets are added across case studies, with explicit human-judgment touchpoints called out in the limitation half. No standalone edit.", "pending"),
    "30": ("accept",                    "Plant validation/assessability hooks earlier so the conclusion synthesizes a thread, not introduces a new topic. Specifically: Houston limitation bullets note 'validation was straightforward because the rule base was inspectable'; PHM limitation bullets note 'validation required held-out test sets and physical-model agreement'; TurboArch notes 'validation required human review of synthesis provenance'; GenGroves/MACQ note 'validation methods are still emerging.' Conclusion then lands as the punchline of a thread.", "pending"),
    "31": ("accept",                    "Keep singular agreement (more formal for INSIGHT). Rewrite to eliminate ambiguity: 'The community can react... or it can actively shape...'.", "pending"),
    "32": ("accept_with_modification",  "Trim portfolio coverage to make room for discussion depth. Specific moves: (a) compress the sixteen-system portfolio summary to a single paragraph + a small reference table; (b) expand the call-to-action with 2-3 concrete points: what 'actively shape' means for INCOSE working groups, what funded-research questions follow from the paradigm-compression argument, what a pre-validation program for agentic SE tools would look like. Coordinate with #26/#30 (validation thread).", "pending"),
}


def render_block(decision: str, notes: str, status: str) -> str:
    notes_indent = "        "
    wrapped = textwrap.fill(
        notes, width=110,
        initial_indent=notes_indent,
        subsequent_indent=notes_indent,
        break_long_words=False, break_on_hyphens=False,
    )
    return (
        "    adjudication:\n"
        f"      decision: {decision}\n"
        f"      decided_at: \"2026-04-29\"\n"
        f"      decided_by: \"Claude (proposed for Wach review)\"\n"
        f"      notes: |\n{wrapped}\n"
        f"      implementation_status: {status}\n"
    )


def has_adjudication(comment_text: str) -> bool:
    return "    adjudication:" in comment_text


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: apply_insight_adjudications.py <yaml_path>", file=sys.stderr)
        sys.exit(1)
    yaml_path = Path(sys.argv[1])
    text = yaml_path.read_text(encoding="utf-8")

    lines = text.splitlines(keepends=True)

    comment_starts: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('- id: "') and line.startswith('  - id: '):
            cid = stripped.split('"')[1]
            comment_starts.append((i, cid))

    synth_idx = None
    for i, line in enumerate(lines):
        if line.startswith("synthesis:"):
            synth_idx = i
            break

    blocks: list[tuple[int, int, str]] = []
    for idx, (start, cid) in enumerate(comment_starts):
        end = comment_starts[idx + 1][0] if idx + 1 < len(comment_starts) else (synth_idx if synth_idx else len(lines))
        block_text = "".join(lines[start:end])
        blocks.append((start, end, block_text))

    new_lines = list(lines)
    inserts = 0
    for (start, end, block_text), (_, cid) in zip(blocks, comment_starts):
        if cid not in ADJUDICATIONS:
            continue
        if has_adjudication(block_text):
            continue
        decision, notes, status = ADJUDICATIONS[cid]
        new_block = render_block(decision, notes, status)

        insert_at = end
        while insert_at > start and lines[insert_at - 1].strip() == "":
            insert_at -= 1

        new_lines.insert(insert_at + inserts, new_block)
        inserts += 1
        print(f"  inserted adjudication for #{cid} ({decision})")

    yaml_path.write_text("".join(new_lines), encoding="utf-8")
    print(f"Wrote {yaml_path} ({inserts} adjudications added)")


if __name__ == "__main__":
    main()

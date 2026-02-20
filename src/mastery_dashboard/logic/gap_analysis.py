from typing import Dict, List, Optional, Set, Tuple

from ..config.schema import CourseConfig
from ..models.enums import MasteryStatus


def compute_gap(
    completed_blocks: Set[str],
    mastery_map: Dict[str, MasteryStatus],
    config: CourseConfig,
) -> List[Dict]:
    """Compute what each next grade requires.

    Returns a list of dicts sorted by grade priority:
    [
        {
            "grade": "B",
            "needed_blocks": ["implementation"],
            "needed_outcomes": [
                {"outcome_id": "I1", "outcome_name": "...", "block_id": "...", "current_status": "in_progress"},
                ...
            ],
            "total_remaining": 3,
        },
        ...
    ]
    """
    sorted_rules = sorted(config.grade_rules, key=lambda r: r.display_order)
    results = []

    for rule in sorted_rules:
        required = set(rule.required_blocks)
        if required.issubset(completed_blocks):
            continue  # Already achieved this grade

        needed_blocks = required - completed_blocks
        needed_outcomes = []

        for bid in needed_blocks:
            block = config.get_block(bid)
            if not block:
                continue
            for outcome in block.outcomes:
                status = mastery_map.get(outcome.id, MasteryStatus.NOT_ATTEMPTED)
                if status != MasteryStatus.MASTERED:
                    needed_outcomes.append({
                        "outcome_id": outcome.id,
                        "outcome_name": outcome.name,
                        "block_id": bid,
                        "block_name": block.name,
                        "current_status": status.value,
                    })

        results.append({
            "grade": rule.grade,
            "needed_blocks": sorted(needed_blocks),
            "needed_outcomes": needed_outcomes,
            "total_remaining": len(needed_outcomes),
        })

    return results


def nearest_grade_gap(
    completed_blocks: Set[str],
    mastery_map: Dict[str, MasteryStatus],
    config: CourseConfig,
) -> Optional[Dict]:
    """Return the gap analysis for just the next achievable grade."""
    gaps = compute_gap(completed_blocks, mastery_map, config)
    # The last entry in gaps is the easiest to achieve (fewest remaining)
    if gaps:
        return min(gaps, key=lambda g: g["total_remaining"])
    return None

from typing import List, Optional, Set, Tuple

from ..config.schema import GradeRuleConfig


def compute_grade(
    completed_blocks: Set[str],
    grade_rules: tuple,
) -> Optional[str]:
    """Compute letter grade from completed blocks.

    Rules are checked in display_order (lowest first = highest grade).
    First rule whose required_blocks is a subset of completed_blocks wins.
    """
    sorted_rules = sorted(grade_rules, key=lambda r: r.display_order)
    for rule in sorted_rules:
        if set(rule.required_blocks).issubset(completed_blocks):
            return rule.grade
    return None


def compute_next_grade(
    completed_blocks: Set[str],
    grade_rules: tuple,
) -> Optional[Tuple[str, Set[str]]]:
    """Compute the next achievable grade above the current one.

    Returns (grade_letter, set_of_required_blocks_for_that_grade) or None
    if the student already has the highest grade.
    """
    sorted_rules = sorted(grade_rules, key=lambda r: r.display_order)
    current = compute_grade(completed_blocks, grade_rules)

    if current is not None:
        # Find the rule after the current grade with fewer required blocks
        # i.e. the next higher grade
        current_idx = None
        for i, rule in enumerate(sorted_rules):
            if rule.grade == current:
                current_idx = i
                break

        if current_idx == 0:
            return None  # Already at highest grade

        # The next higher grade is the one just before current in sorted order
        if current_idx is not None and current_idx > 0:
            target = sorted_rules[current_idx - 1]
            return (target.grade, set(target.required_blocks))

    # No current grade — target the lowest-requirement grade
    if sorted_rules:
        target = sorted_rules[-1]  # Highest display_order = lowest grade
        return (target.grade, set(target.required_blocks))

    return None

from pathlib import Path
from typing import Union

import yaml

from .schema import (
    BlockConfig,
    CourseConfig,
    GradeRuleConfig,
    MasteryCriteria,
    OutcomeConfig,
)


class ConfigError(Exception):
    pass


def load_course_config(path: Union[str, Path]) -> CourseConfig:
    path = Path(path)
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    return _parse_config(raw, path)


def _parse_config(raw: dict, path: Path) -> CourseConfig:
    if not isinstance(raw, dict):
        raise ConfigError(f"Config must be a YAML mapping, got {type(raw).__name__}")

    course = raw.get("course")
    if not course:
        raise ConfigError("Missing 'course' section")

    for field in ("name", "id", "semester"):
        if field not in course:
            raise ConfigError(f"Missing 'course.{field}'")

    raw_blocks = raw.get("blocks")
    if not raw_blocks:
        raise ConfigError("Missing 'blocks' section")

    blocks = []
    all_block_ids = set()
    all_outcome_ids = set()

    for i, rb in enumerate(raw_blocks):
        block_id = rb.get("id")
        if not block_id:
            raise ConfigError(f"Block {i} missing 'id'")
        if block_id in all_block_ids:
            raise ConfigError(f"Duplicate block id: {block_id}")
        all_block_ids.add(block_id)

        if not rb.get("name"):
            raise ConfigError(f"Block '{block_id}' missing 'name'")

        raw_outcomes = rb.get("outcomes", [])
        if not raw_outcomes:
            raise ConfigError(f"Block '{block_id}' has no outcomes")

        outcomes = []
        for j, ro in enumerate(raw_outcomes):
            oid = ro.get("id")
            if not oid:
                raise ConfigError(f"Outcome {j} in block '{block_id}' missing 'id'")
            if oid in all_outcome_ids:
                raise ConfigError(f"Duplicate outcome id: {oid}")
            all_outcome_ids.add(oid)

            if not ro.get("name"):
                raise ConfigError(f"Outcome '{oid}' missing 'name'")

            mc_raw = ro.get("mastery_criteria", {})
            criteria = MasteryCriteria(
                type=mc_raw.get("type", course.get("evaluator", "threshold")),
                min_score=mc_raw.get("min_score"),
                required_items=tuple(mc_raw["required_items"]) if mc_raw.get("required_items") else None,
            )

            outcomes.append(OutcomeConfig(
                id=oid,
                name=ro["name"],
                description=ro.get("description", ""),
                mastery_criteria=criteria,
            ))

        blocks.append(BlockConfig(
            id=block_id,
            name=rb["name"],
            description=rb.get("description", ""),
            outcomes=tuple(outcomes),
        ))

    raw_rules = raw.get("grade_rules")
    if not raw_rules:
        raise ConfigError("Missing 'grade_rules' section")

    rules = []
    for i, rr in enumerate(raw_rules):
        if "grade" not in rr:
            raise ConfigError(f"Grade rule {i} missing 'grade'")
        if "required_blocks" not in rr:
            raise ConfigError(f"Grade rule for '{rr['grade']}' missing 'required_blocks'")

        for bid in rr["required_blocks"]:
            if bid not in all_block_ids:
                raise ConfigError(
                    f"Grade rule '{rr['grade']}' references unknown block '{bid}'"
                )

        rules.append(GradeRuleConfig(
            grade=rr["grade"],
            required_blocks=tuple(rr["required_blocks"]),
            display_order=rr.get("display_order", i + 1),
        ))

    return CourseConfig(
        name=course["name"],
        id=course["id"],
        semester=course["semester"],
        default_evaluator=course.get("evaluator", "threshold"),
        blocks=tuple(blocks),
        grade_rules=tuple(rules),
    )

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class MasteryCriteria:
    type: str  # "threshold", "checklist", "manual"
    min_score: Optional[float] = None
    required_items: Optional[List[str]] = None


@dataclass(frozen=True)
class OutcomeConfig:
    id: str
    name: str
    description: str
    mastery_criteria: MasteryCriteria


@dataclass(frozen=True)
class BlockConfig:
    id: str
    name: str
    description: str
    outcomes: tuple  # tuple of OutcomeConfig (frozen-compatible)


@dataclass(frozen=True)
class GradeRuleConfig:
    grade: str
    required_blocks: tuple  # tuple of block IDs
    display_order: int


@dataclass(frozen=True)
class CourseConfig:
    name: str
    id: str
    semester: str
    default_evaluator: str
    blocks: tuple  # tuple of BlockConfig
    grade_rules: tuple  # tuple of GradeRuleConfig

    def get_block(self, block_id: str) -> Optional[BlockConfig]:
        for b in self.blocks:
            if b.id == block_id:
                return b
        return None

    def get_outcome(self, outcome_id: str) -> Optional[OutcomeConfig]:
        for b in self.blocks:
            for o in b.outcomes:
                if o.id == outcome_id:
                    return o
        return None

    def get_block_for_outcome(self, outcome_id: str) -> Optional[BlockConfig]:
        for b in self.blocks:
            for o in b.outcomes:
                if o.id == outcome_id:
                    return b
        return None

    def all_outcome_ids(self) -> List[str]:
        return [o.id for b in self.blocks for o in b.outcomes]

    def outcome_ids_for_block(self, block_id: str) -> List[str]:
        b = self.get_block(block_id)
        return [o.id for o in b.outcomes] if b else []

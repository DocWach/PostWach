from abc import ABC, abstractmethod
from typing import Dict, Type

from ..config.schema import MasteryCriteria
from ..models.enums import MasteryStatus


class MasteryEvaluator(ABC):
    @abstractmethod
    def evaluate(self, score: float, criteria: MasteryCriteria) -> MasteryStatus:
        """Evaluate a submission score against criteria."""
        ...


class ThresholdEvaluator(MasteryEvaluator):
    """Mastered if score >= min_score, otherwise in_progress."""

    def evaluate(self, score: float, criteria: MasteryCriteria) -> MasteryStatus:
        threshold = criteria.min_score if criteria.min_score is not None else 0.80
        if score >= threshold:
            return MasteryStatus.MASTERED
        return MasteryStatus.IN_PROGRESS


class ChecklistEvaluator(MasteryEvaluator):
    """Score represents fraction of checklist items completed.
    Mastered at 1.0 (all items), in_progress if any done."""

    def evaluate(self, score: float, criteria: MasteryCriteria) -> MasteryStatus:
        if score >= 1.0:
            return MasteryStatus.MASTERED
        if score > 0.0:
            return MasteryStatus.IN_PROGRESS
        return MasteryStatus.NOT_ATTEMPTED


class AlwaysPendingEvaluator(MasteryEvaluator):
    """Always returns IN_PROGRESS — requires instructor override for mastery."""

    def evaluate(self, score: float, criteria: MasteryCriteria) -> MasteryStatus:
        return MasteryStatus.IN_PROGRESS


_EVALUATOR_REGISTRY: Dict[str, Type[MasteryEvaluator]] = {
    "threshold": ThresholdEvaluator,
    "checklist": ChecklistEvaluator,
    "manual": AlwaysPendingEvaluator,
}


def get_evaluator(name: str) -> MasteryEvaluator:
    cls = _EVALUATOR_REGISTRY.get(name)
    if cls is None:
        raise ValueError(f"Unknown evaluator type: '{name}'. "
                         f"Available: {list(_EVALUATOR_REGISTRY.keys())}")
    return cls()

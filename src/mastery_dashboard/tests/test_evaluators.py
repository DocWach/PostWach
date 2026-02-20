import pytest

from mastery_dashboard.config.schema import MasteryCriteria
from mastery_dashboard.logic.evaluators import (
    AlwaysPendingEvaluator,
    ChecklistEvaluator,
    ThresholdEvaluator,
    get_evaluator,
)
from mastery_dashboard.models.enums import MasteryStatus


class TestThresholdEvaluator:
    def setup_method(self):
        self.evaluator = ThresholdEvaluator()
        self.criteria = MasteryCriteria(type="threshold", min_score=0.80)

    def test_above_threshold_masters(self):
        assert self.evaluator.evaluate(0.85, self.criteria) == MasteryStatus.MASTERED

    def test_at_threshold_masters(self):
        assert self.evaluator.evaluate(0.80, self.criteria) == MasteryStatus.MASTERED

    def test_below_threshold_in_progress(self):
        assert self.evaluator.evaluate(0.79, self.criteria) == MasteryStatus.IN_PROGRESS

    def test_zero_score_in_progress(self):
        assert self.evaluator.evaluate(0.0, self.criteria) == MasteryStatus.IN_PROGRESS

    def test_default_threshold_when_none(self):
        criteria = MasteryCriteria(type="threshold", min_score=None)
        assert self.evaluator.evaluate(0.80, criteria) == MasteryStatus.MASTERED
        assert self.evaluator.evaluate(0.79, criteria) == MasteryStatus.IN_PROGRESS


class TestChecklistEvaluator:
    def setup_method(self):
        self.evaluator = ChecklistEvaluator()
        self.criteria = MasteryCriteria(type="checklist")

    def test_all_items_mastered(self):
        assert self.evaluator.evaluate(1.0, self.criteria) == MasteryStatus.MASTERED

    def test_partial_items_in_progress(self):
        assert self.evaluator.evaluate(0.5, self.criteria) == MasteryStatus.IN_PROGRESS

    def test_no_items_not_attempted(self):
        assert self.evaluator.evaluate(0.0, self.criteria) == MasteryStatus.NOT_ATTEMPTED


class TestAlwaysPendingEvaluator:
    def test_always_returns_in_progress(self):
        evaluator = AlwaysPendingEvaluator()
        criteria = MasteryCriteria(type="manual")
        assert evaluator.evaluate(1.0, criteria) == MasteryStatus.IN_PROGRESS
        assert evaluator.evaluate(0.0, criteria) == MasteryStatus.IN_PROGRESS


class TestFactory:
    def test_known_types(self):
        assert isinstance(get_evaluator("threshold"), ThresholdEvaluator)
        assert isinstance(get_evaluator("checklist"), ChecklistEvaluator)
        assert isinstance(get_evaluator("manual"), AlwaysPendingEvaluator)

    def test_unknown_type_raises(self):
        with pytest.raises(ValueError, match="Unknown evaluator"):
            get_evaluator("bogus")

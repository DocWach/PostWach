from mastery_dashboard.logic.gap_analysis import compute_gap, nearest_grade_gap
from mastery_dashboard.models.enums import MasteryStatus


class TestComputeGap:
    def test_full_completion_no_gaps(self, minimal_config):
        completed = {"block_a", "block_b", "block_c"}
        mastery = {oid: MasteryStatus.MASTERED for oid in minimal_config.all_outcome_ids()}
        gaps = compute_gap(completed, mastery, minimal_config)
        assert gaps == []

    def test_no_progress_shows_all_grades(self, minimal_config):
        gaps = compute_gap(set(), {}, minimal_config)
        assert len(gaps) == 3  # A, B, C all unachieved
        grade_letters = [g["grade"] for g in gaps]
        assert "A" in grade_letters
        assert "B" in grade_letters
        assert "C" in grade_letters

    def test_partial_progress(self, minimal_config):
        completed = {"block_a"}
        mastery = {"A1": MasteryStatus.MASTERED, "A2": MasteryStatus.MASTERED}
        gaps = compute_gap(completed, mastery, minimal_config)
        # C is achieved, so only A and B gaps remain
        grade_letters = [g["grade"] for g in gaps]
        assert "C" not in grade_letters
        assert "B" in grade_letters

    def test_gap_includes_needed_outcomes(self, minimal_config):
        completed = {"block_a"}
        mastery = {
            "A1": MasteryStatus.MASTERED, "A2": MasteryStatus.MASTERED,
            "B1": MasteryStatus.IN_PROGRESS,
        }
        gaps = compute_gap(completed, mastery, minimal_config)
        b_gap = next(g for g in gaps if g["grade"] == "B")
        outcome_ids = [o["outcome_id"] for o in b_gap["needed_outcomes"]]
        assert "B1" in outcome_ids
        assert "B2" in outcome_ids


class TestNearestGradeGap:
    def test_no_progress_targets_easiest(self, minimal_config):
        result = nearest_grade_gap(set(), {}, minimal_config)
        assert result is not None
        assert result["grade"] == "C"  # Fewest remaining

    def test_full_completion_returns_none(self, minimal_config):
        completed = {"block_a", "block_b", "block_c"}
        mastery = {oid: MasteryStatus.MASTERED for oid in minimal_config.all_outcome_ids()}
        result = nearest_grade_gap(completed, mastery, minimal_config)
        assert result is None

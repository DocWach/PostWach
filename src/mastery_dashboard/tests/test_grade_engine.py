from mastery_dashboard.logic.grade_engine import compute_grade, compute_next_grade


class TestComputeGrade:
    def test_all_blocks_gives_a(self, minimal_config):
        result = compute_grade({"block_a", "block_b", "block_c"}, minimal_config.grade_rules)
        assert result == "A"

    def test_two_blocks_gives_b(self, minimal_config):
        result = compute_grade({"block_a", "block_b"}, minimal_config.grade_rules)
        assert result == "B"

    def test_one_block_gives_c(self, minimal_config):
        result = compute_grade({"block_a"}, minimal_config.grade_rules)
        assert result == "C"

    def test_no_blocks_gives_none(self, minimal_config):
        result = compute_grade(set(), minimal_config.grade_rules)
        assert result is None

    def test_superset_still_matches_highest(self, minimal_config):
        result = compute_grade({"block_a", "block_b", "block_c", "extra"}, minimal_config.grade_rules)
        assert result == "A"

    def test_wrong_blocks_gives_none(self, minimal_config):
        result = compute_grade({"block_b", "block_c"}, minimal_config.grade_rules)
        assert result is None

    def test_empty_rules(self):
        result = compute_grade({"block_a"}, ())
        assert result is None


class TestComputeNextGrade:
    def test_no_grade_targets_lowest(self, minimal_config):
        result = compute_next_grade(set(), minimal_config.grade_rules)
        assert result is not None
        assert result[0] == "C"
        assert result[1] == {"block_a"}

    def test_c_targets_b(self, minimal_config):
        result = compute_next_grade({"block_a"}, minimal_config.grade_rules)
        assert result is not None
        assert result[0] == "B"

    def test_b_targets_a(self, minimal_config):
        result = compute_next_grade({"block_a", "block_b"}, minimal_config.grade_rules)
        assert result is not None
        assert result[0] == "A"

    def test_a_returns_none(self, minimal_config):
        result = compute_next_grade({"block_a", "block_b", "block_c"}, minimal_config.grade_rules)
        assert result is None

    def test_empty_rules(self):
        result = compute_next_grade(set(), ())
        assert result is None

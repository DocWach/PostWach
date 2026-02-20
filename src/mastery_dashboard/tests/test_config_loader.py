import tempfile
from pathlib import Path

import pytest

from mastery_dashboard.config.loader import ConfigError, load_course_config


_VALID_YAML = """
course:
  name: "Test Course"
  id: "test-101"
  semester: "Spring 2026"
  evaluator: "threshold"

blocks:
  - id: "b1"
    name: "Block 1"
    description: "First"
    outcomes:
      - id: "O1"
        name: "Outcome 1"
        description: "First outcome"
        mastery_criteria:
          type: "threshold"
          min_score: 0.80

grade_rules:
  - grade: "A"
    required_blocks: ["b1"]
    display_order: 1
"""


def _write_yaml(content: str) -> Path:
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False, encoding="utf-8")
    f.write(content)
    f.close()
    return Path(f.name)


class TestLoadCourseConfig:
    def test_valid_config(self):
        path = _write_yaml(_VALID_YAML)
        config = load_course_config(path)
        assert config.name == "Test Course"
        assert len(config.blocks) == 1
        assert len(config.grade_rules) == 1
        assert config.blocks[0].outcomes[0].id == "O1"

    def test_missing_file(self):
        with pytest.raises(ConfigError, match="not found"):
            load_course_config("/nonexistent/path.yaml")

    def test_missing_course_section(self):
        path = _write_yaml("blocks: []\ngrade_rules: []")
        with pytest.raises(ConfigError, match="Missing 'course'"):
            load_course_config(path)

    def test_missing_course_name(self):
        yaml = """
course:
  id: "x"
  semester: "y"
blocks:
  - id: "b1"
    name: "B"
    outcomes:
      - id: "O1"
        name: "O"
grade_rules:
  - grade: "A"
    required_blocks: ["b1"]
"""
        path = _write_yaml(yaml)
        with pytest.raises(ConfigError, match="Missing 'course.name'"):
            load_course_config(path)

    def test_duplicate_block_id(self):
        yaml = """
course:
  name: "T"
  id: "t"
  semester: "s"
blocks:
  - id: "b1"
    name: "B1"
    outcomes:
      - id: "O1"
        name: "O1"
  - id: "b1"
    name: "B1 dup"
    outcomes:
      - id: "O2"
        name: "O2"
grade_rules:
  - grade: "A"
    required_blocks: ["b1"]
"""
        path = _write_yaml(yaml)
        with pytest.raises(ConfigError, match="Duplicate block"):
            load_course_config(path)

    def test_bad_block_reference_in_grade_rule(self):
        yaml = """
course:
  name: "T"
  id: "t"
  semester: "s"
blocks:
  - id: "b1"
    name: "B1"
    outcomes:
      - id: "O1"
        name: "O1"
grade_rules:
  - grade: "A"
    required_blocks: ["b1", "nonexistent"]
"""
        path = _write_yaml(yaml)
        with pytest.raises(ConfigError, match="unknown block"):
            load_course_config(path)

    def test_block_with_no_outcomes(self):
        yaml = """
course:
  name: "T"
  id: "t"
  semester: "s"
blocks:
  - id: "b1"
    name: "B1"
    outcomes: []
grade_rules:
  - grade: "A"
    required_blocks: ["b1"]
"""
        path = _write_yaml(yaml)
        with pytest.raises(ConfigError, match="no outcomes"):
            load_course_config(path)

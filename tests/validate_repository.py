#!/usr/bin/env python3
"""Dependency-free structural checks for the public skill repository."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    ROOT / ".github/skills/fde-workflow-interview",
    ROOT / ".github/skills/fde-workflow-prioritization",
)
REQUIRED_RESULT_KEYS = {
    "schema_version",
    "skill_version",
    "session",
    "participant",
    "workflow",
    "as_is_steps",
    "roles",
    "systems",
    "data_sources",
    "business_rules",
    "exceptions",
    "pain_points",
    "root_causes",
    "baseline_metrics",
    "to_be",
    "opportunities",
    "human_gates",
    "evidence",
    "material_requests",
    "open_questions",
    "review",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_skill(skill_dir: Path) -> None:
    skill_file = skill_dir / "SKILL.md"
    require(skill_file.is_file(), f"missing {skill_file}")
    text = skill_file.read_text(encoding="utf-8")
    require(text.startswith("---\n"), f"missing frontmatter in {skill_file}")
    name_match = re.search(r"^name:\s*([^\n]+)$", text, re.MULTILINE)
    require(name_match is not None, f"missing name in {skill_file}")
    require(name_match.group(1).strip() == skill_dir.name, f"name mismatch in {skill_file}")
    require(re.search(r"^description:\s*\S", text, re.MULTILINE) is not None, f"missing description in {skill_file}")
    for relative in re.findall(r"\]\(([^)]+)\)", text):
        if "://" in relative or relative.startswith("#"):
            continue
        require((skill_dir / relative).resolve().exists(), f"broken link {relative} in {skill_file}")


def check_fixture(path: Path, expected_review: str) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = REQUIRED_RESULT_KEYS - data.keys()
    require(not missing, f"{path} missing keys: {sorted(missing)}")
    require(data["schema_version"] == "1.0.0", f"unsupported schema in {path}")
    require(data["review"]["status"] == expected_review, f"unexpected review status in {path}")
    evidence_ids = {item["id"] for item in data["evidence"]}
    require(evidence_ids, f"no evidence in {path}")


def main() -> None:
    for skill in SKILLS:
        check_skill(skill)

    schema_path = SKILLS[0] / "references/discovery-result.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    require(schema["properties"]["schema_version"]["const"] == "1.0.0", "schema version mismatch")
    duration_rule = schema["properties"]["session"]["properties"]["duration_target_minutes"]
    require(duration_rule.get("minimum", 0) <= 10 <= duration_rule.get("maximum", 10), "10-minute target is not schema-valid")

    interview_text = (SKILLS[0] / "SKILL.md").read_text(encoding="utf-8")
    require("never exceed 8" in interview_text, "interview question cap is missing")
    require("only says they want to invoke or try this Skill" in interview_text, "invocation-only opening is missing")
    require("回答提示（可选）" in interview_text, "short answer-tip guidance is missing")
    require("security/compliance" in interview_text, "enterprise control guidance is missing")

    check_fixture(ROOT / "tests/fixtures/approved-a/result.json", "approved_by_participant")
    check_fixture(ROOT / "tests/fixtures/approved-b/result.json", "approved_by_participant")
    check_fixture(ROOT / "tests/fixtures/draft/result.json", "draft")

    malformed = json.loads((ROOT / "tests/fixtures/malformed/result.json").read_text(encoding="utf-8"))
    require(bool(REQUIRED_RESULT_KEYS - malformed.keys()), "malformed fixture is unexpectedly complete")

    ignored = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for directory in ("/local-output/", "/employee-submissions/", "/local-portfolio/"):
        require(directory in ignored, f"{directory} is not ignored")

    print("repository validation passed")


if __name__ == "__main__":
    main()

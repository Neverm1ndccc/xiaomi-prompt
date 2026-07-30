#!/usr/bin/env python3
"""Repository-level validation for the portable Xiaomi image operations Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "SKILL.md",
    "agents/openai.yaml",
    "references/prompts.md",
    "references/governance.md",
    "references/workbench-protocol.md",
    "references/examples.md",
    "tests/scenarios.md",
)
FORBIDDEN_MARKERS = ("TODO", "TBD", "REPLACE_ME", "YOUR_ORG")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_frontmatter(text: str) -> str:
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")
    return match.group(1)


def validate_markdown_links(path: Path, text: str) -> None:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        clean_target = target.split("#", 1)[0]
        if clean_target and not (path.parent / clean_target).resolve().exists():
            fail(f"{path.relative_to(ROOT)} links to missing file: {target}")


def main() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = extract_frontmatter(skill_text)
    if not re.search(r"^name:\s*xiaomi-image-ai-operations\s*$", frontmatter, re.MULTILINE):
        fail("SKILL.md name must be xiaomi-image-ai-operations")
    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not description_match or not description_match.group(1).startswith("Use when "):
        fail("SKILL.md description must begin with 'Use when '")

    openai_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if "$xiaomi-image-ai-operations" not in openai_yaml:
        fail("agents/openai.yaml default_prompt must invoke $xiaomi-image-ai-operations")

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    required_readme_terms = (
        "install-skill-from-github.py",
        "$xiaomi-image-ai-operations",
        "私有",
        "可选工作台",
    )
    for term in required_readme_terms:
        if term not in readme_text:
            fail(f"README.md must explain: {term}")

    for relative_path in REQUIRED_FILES:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for marker in FORBIDDEN_MARKERS:
            if marker in text:
                fail(f"{relative_path} contains unfinished marker: {marker}")
        if relative_path.endswith(".md"):
            validate_markdown_links(ROOT / relative_path, text)

    print("PASS: portable Skill repository structure and documentation are valid")


if __name__ == "__main__":
    main()


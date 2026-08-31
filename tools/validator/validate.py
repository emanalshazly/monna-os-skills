#!/usr/bin/env python3
"""Dependency-free structural validator for the public Skill collection."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED = {"name", "description", "quality_tier", "fingerprint"}
ALLOWED_TIERS = {"draft", "validated"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FINGERPRINT_RE = re.compile(r"^[a-z]+-\d{3}-[0-9a-f]{6}$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "Google API key": re.compile(r"\bAIza[A-Za-z0-9_-]{30,}\b"),
}


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    metadata: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            raise ValueError(f"unsupported frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata, text[end + 5 :]


def validate_link(skill_file: Path, raw_target: str) -> str | None:
    target = raw_target.split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if not (skill_file.parent / target).resolve().exists():
        return f"broken local link {raw_target!r}"
    return None


def validate_skill(skill_file: Path) -> tuple[dict[str, str] | None, list[str]]:
    errors: list[str] = []
    text = skill_file.read_text(encoding="utf-8")
    try:
        metadata, body = frontmatter(text)
    except ValueError as exc:
        return None, [str(exc)]

    missing = sorted(REQUIRED - metadata.keys())
    if missing:
        errors.append(f"missing frontmatter fields: {', '.join(missing)}")
    name = metadata.get("name", "")
    if name and not NAME_RE.fullmatch(name):
        errors.append("name must be kebab-case")
    if name and name != skill_file.parent.name:
        errors.append(f"name {name!r} does not match directory {skill_file.parent.name!r}")
    if metadata.get("quality_tier") not in ALLOWED_TIERS:
        errors.append("quality_tier must be draft or validated")
    fingerprint = metadata.get("fingerprint", "")
    if fingerprint and not FINGERPRINT_RE.fullmatch(fingerprint):
        errors.append("fingerprint must match domain-000-abcdef")
    if len(metadata.get("description", "")) < 20:
        errors.append("description must be at least 20 characters")
    if not body.strip():
        errors.append("Skill body is empty")

    for target in LINK_RE.findall(text):
        issue = validate_link(skill_file, target)
        if issue:
            errors.append(issue)
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"possible {label} detected")
    return metadata, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-dir", type=Path, default=Path("skills"))
    parser.add_argument("--check-catalog", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    skill_files = sorted(args.skills_dir.glob("*/*/SKILL.md"))
    errors: list[dict[str, str]] = []
    names: dict[str, Path] = {}
    fingerprints: dict[str, Path] = {}

    for skill_file in skill_files:
        metadata, issues = validate_skill(skill_file)
        for issue in issues:
            errors.append({"path": str(skill_file), "error": issue})
        if not metadata:
            continue
        for field, registry in (("name", names), ("fingerprint", fingerprints)):
            value = metadata.get(field, "")
            if value in registry:
                errors.append({"path": str(skill_file), "error": f"duplicate {field}: {value}"})
            elif value:
                registry[value] = skill_file

    if args.check_catalog:
        readme = Path("README.md").read_text(encoding="utf-8")
        marker = re.search(r"<!-- SKILL_COUNT: (\d+) -->", readme)
        if not marker or int(marker.group(1)) != len(skill_files):
            errors.append({"path": "README.md", "error": f"catalog count does not match {len(skill_files)} Skills"})
        for name in names:
            if name not in readme:
                errors.append({"path": "README.md", "error": f"catalog entry missing for {name}"})

    result = {"skills": len(skill_files), "errors": errors, "status": "PASS" if not errors else "FAIL"}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['status']} - {len(skill_files)} Skills checked; {len(errors)} issue(s)")
        for error in errors:
            print(f"  {error['path']}: {error['error']}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

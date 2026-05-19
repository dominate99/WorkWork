from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


MAX_SKILL_NAME_LENGTH = 64
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate WorkWork packaged skill frontmatter."
    )
    parser.add_argument(
        "skill_directory",
        nargs="?",
        help="Path to the packaged skill directory that contains SKILL.md.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit machine-readable JSON output.",
    )
    return parser.parse_args()


def load_yaml():
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependency: PyYAML. Install it with "
            "`python -m pip install PyYAML` before running "
            "`python tools/quick_validate.py <skill_directory>`."
        ) from exc
    return yaml


def validate_skill(skill_path: str) -> tuple[bool, str]:
    yaml = load_yaml()
    skill_dir = Path(skill_path)
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as exc:
        return False, f"Invalid YAML in frontmatter: {exc}"

    unexpected_keys = set(frontmatter.keys()) - ALLOWED_FRONTMATTER_KEYS
    if unexpected_keys:
        allowed = ", ".join(sorted(ALLOWED_FRONTMATTER_KEYS))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"Unexpected key(s) in SKILL.md frontmatter: {unexpected}. Allowed properties are: {allowed}",
        )

    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            return (
                False,
                f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)",
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            return (
                False,
                f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens",
            )
        if len(name) > MAX_SKILL_NAME_LENGTH:
            return (
                False,
                f"Name is too long ({len(name)} characters). Maximum is {MAX_SKILL_NAME_LENGTH} characters.",
            )

    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        if "<" in description or ">" in description:
            return False, "Description cannot contain angle brackets (< or >)"
        if len(description) > 1024:
            return (
                False,
                f"Description is too long ({len(description)} characters). Maximum is 1024 characters.",
            )

    return True, "Skill is valid!"


def emit_json(ok: bool, message: str, skill_directory: str | None = None, error: str | None = None) -> None:
    payload = {
        "ok": ok,
        "message": message,
        "skill_directory": skill_directory,
    }
    if error is not None:
        payload["error"] = error
    print(json.dumps(payload, indent=2))


def main() -> int:
    args = parse_args()
    if not args.skill_directory:
        message = "Usage: python tools/quick_validate.py <skill_directory>"
        if args.as_json:
            emit_json(False, message, error=message)
        else:
            print(message)
        return 1

    try:
        valid, message = validate_skill(args.skill_directory)
    except RuntimeError as exc:
        if args.as_json:
            emit_json(False, str(exc), skill_directory=args.skill_directory, error=str(exc))
        else:
            print(str(exc))
        return 1

    if args.as_json:
        emit_json(valid, message, skill_directory=args.skill_directory)
    else:
        print(message)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())

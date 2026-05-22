from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


SCRIPT_NAME = "validate_ww_case_path_identity.py"
REPO_ROOT = Path(__file__).resolve().parent.parent


TARGETS = {
    "skill": REPO_ROOT / "plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md",
    "brief_template": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md",
    "dispatch_template": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md",
    "readme": REPO_ROOT / "README.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the WorkWork case-based path identity Markdown contract."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit machine-readable JSON output.",
    )
    return parser.parse_args()


@dataclass
class Result:
    rule_id: str
    passed: bool
    file: str
    section: str
    message: str

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "passed": self.passed,
            "file": self.file,
            "section": self.section,
            "message": self.message,
        }


class DependencyError(RuntimeError):
    pass


def load_markdown_parser():
    try:
        from markdown_it import MarkdownIt  # type: ignore
    except ImportError as exc:
        raise DependencyError(
            "Missing dependency: markdown-it-py. Install it with "
            "`python -m pip install markdown-it-py` before running "
            f"`python tools/{SCRIPT_NAME}`."
        ) from exc
    return MarkdownIt


@dataclass
class Document:
    path: Path
    headings: Dict[str, List[str]]
    labels: Dict[Tuple[str, str], List[str]]
    paragraphs: Dict[str, List[str]]
    code_blocks: Dict[str, List[str]]


def normalize(text: str) -> str:
    return " ".join(text.strip().split())


def is_list_open(token_type: str) -> bool:
    return token_type in {"bullet_list_open", "ordered_list_open"}


def is_list_close(token_type: str) -> bool:
    return token_type in {"bullet_list_close", "ordered_list_close"}


def collect_list_items(tokens: List, start: int) -> Tuple[List[str], int]:
    items: List[str] = []
    depth = 0
    current: List[str] = []
    i = start
    while i < len(tokens):
        token = tokens[i]
        if is_list_open(token.type):
            depth += 1
            i += 1
            continue
        if is_list_close(token.type):
            depth -= 1
            if depth == 0:
                if current:
                    items.append(normalize(" ".join(current)))
                    current = []
                return items, i + 1
            i += 1
            continue
        if token.type == "list_item_open":
            current = []
            i += 1
            continue
        if token.type == "list_item_close":
            if current:
                items.append(normalize(" ".join(current)))
            current = []
            i += 1
            continue
        if token.type == "inline" and depth >= 1:
            current.append(token.content)
        i += 1
    return items, i


def parse_document(path: Path, md_cls) -> Document:
    text = path.read_text(encoding="utf-8")
    tokens = md_cls().parse(text)

    headings: Dict[str, List[str]] = {}
    labels: Dict[Tuple[str, str], List[str]] = {}
    paragraphs: Dict[str, List[str]] = {}
    code_blocks: Dict[str, List[str]] = {}

    heading_stack: List[str] = []
    current_heading = "__root__"
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == "heading_open":
            if i + 1 < len(tokens) and tokens[i + 1].type == "inline":
                level = int(token.tag[1])
                heading_text = normalize(tokens[i + 1].content)
                heading_stack = heading_stack[: level - 1]
                heading_stack.append(heading_text)
                current_heading = " / ".join(heading_stack)
                headings.setdefault(current_heading, [])
                paragraphs.setdefault(current_heading, [])
                code_blocks.setdefault(current_heading, [])
            i += 3
            continue

        if token.type == "paragraph_open":
            inline_idx = i + 1
            if inline_idx < len(tokens) and tokens[inline_idx].type == "inline":
                label_text = normalize(tokens[inline_idx].content)
                next_idx = i + 3
                if label_text.endswith(":") and next_idx < len(tokens) and is_list_open(
                    tokens[next_idx].type
                ):
                    items, new_idx = collect_list_items(tokens, next_idx)
                    labels[(current_heading, label_text.rstrip(":"))] = items
                    i = new_idx
                    continue
                paragraphs.setdefault(current_heading, []).append(label_text)
            i += 3
            continue

        if is_list_open(token.type):
            items, new_idx = collect_list_items(tokens, i)
            headings.setdefault(current_heading, []).extend(items)
            i = new_idx
            continue

        if token.type == "fence":
            code_blocks.setdefault(current_heading, []).append(token.content)
            i += 1
            continue

        i += 1

    return Document(
        path=path,
        headings=headings,
        labels=labels,
        paragraphs=paragraphs,
        code_blocks=code_blocks,
    )


def has_fragment(items: List[str], fragment: str) -> bool:
    fragment_norm = normalize(fragment)
    return any(fragment_norm in normalize(item) for item in items)


def section_items(doc: Document, heading: str) -> List[str]:
    for key, items in doc.headings.items():
        if key == heading or key.endswith(f" / {heading}"):
            return items
    return []


def label_items(doc: Document, heading: str, label: str) -> List[str]:
    for (key_heading, key_label), items in doc.labels.items():
        if key_label != label:
            continue
        if key_heading == heading or key_heading.endswith(f" / {heading}"):
            return items
    return []


def paragraph_items(doc: Document, heading: str) -> List[str]:
    for key, items in doc.paragraphs.items():
        if key == heading or key.endswith(f" / {heading}"):
            return items
    return []


def build_results(documents: Dict[str, Document]) -> List[Result]:
    results: List[Result] = []

    skill = documents["skill"]
    brief = documents["brief_template"]
    dispatch = documents["dispatch_template"]
    readme = documents["readme"]
    skill_text = normalize(skill.path.read_text(encoding="utf-8"))
    brief_text = normalize(brief.path.read_text(encoding="utf-8"))
    dispatch_text = normalize(dispatch.path.read_text(encoding="utf-8"))
    readme_text = normalize(readme.path.read_text(encoding="utf-8"))

    brief_metadata = section_items(brief, "Artifact Metadata")

    checks = [
        (
            "WWCP001",
            brief.path,
            "Artifact Metadata",
            all(
                has_fragment(brief_metadata, fragment)
                for fragment in ["`case_slug`", "`round_slug`", "`case_root`", "`round_root`"]
            ),
            "Working brief template is missing one or more case-path identity metadata fields.",
        ),
        (
            "WWCP002",
            brief.path,
            "Scope Preparation",
            all(normalize(fragment) in brief_text for fragment in [
                    "`case_slug` identifies the long-lived workstream for this round",
                    "`round_slug` identifies this bounded `$ww` or `$www` cycle inside that case",
                    "`case_root` must resolve to `docs/superpowers/cases/<case_slug>/`",
                    "`round_root` must resolve to `docs/superpowers/cases/<case_slug>/rounds/<round_slug>/`",
                    "new rounds write their canonical artifacts under `round_root`; legacy type-based paths remain read-compatible only when explicitly referenced",
                ]),
            "Working brief template is missing one or more artifact-layout rules for case-based paths.",
        ),
        (
            "WWCP003",
            dispatch.path,
            "__root__",
            all(normalize(fragment) in dispatch_text for fragment in [
                    "Case Slug: {{case_slug}}",
                    "Round Slug: {{round_slug}}",
                    "Case Root: {{case_root}}",
                    "Round Root: {{round_root}}",
                ]),
            "Dispatch plan template is missing one or more case-path identity header fields.",
        ),
        (
            "WWCP004",
            dispatch.path,
            "Preconditions",
            all(normalize(fragment) in dispatch_text for fragment in [
                    "`Case Root` must resolve to `docs/superpowers/cases/<case_slug>/`",
                    "`Round Root` must resolve to `docs/superpowers/cases/<case_slug>/rounds/<round_slug>/`",
                    "new dispatch-round artifacts are canonically written under `Round Root`",
                    "legacy type-based paths may remain readable during migration, but they are not parallel write targets",
                ]),
            "Dispatch plan template is missing one or more path identity rules.",
        ),
        (
            "WWCP005",
            skill.path,
            "Working Brief",
            all(normalize(fragment) in skill_text for fragment in [
                    "before dispatch-plan creation, the brief must be saved to `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/working-brief.md`",
                    "each persisted working brief must carry explicit `case_slug`, `round_slug`, `case_root`, and `round_root` metadata so path identity is not re-derived ad hoc",
                    "`case_slug` identifies the long-lived workstream; `round_slug` identifies one bounded `$ww` or `$www` cycle inside that case",
                    "revisions within the same round update the same `round_root`; new rounds create a new `round_slug`",
                    "legacy type-based brief paths remain readable only when explicitly referenced during migration; they are not canonical write targets for new rounds",
                ]),
            "SKILL.md is missing one or more case-based working brief persistence rules.",
        ),
        (
            "WWCP006",
            skill.path,
            "Dispatch Plan File",
            all(normalize(fragment) in skill_text for fragment in [
                    "`docs/superpowers/cases/<case-slug>/rounds/<round-slug>/dispatch-plan.md`",
                    "reference the active `case_slug`, `round_slug`, `case_root`, and `round_root`",
                    "new round artifacts are canonically written under `round_root`; legacy type-based artifact locations may remain readable during migration, but they are not active parallel write targets",
                ]),
            "SKILL.md is missing one or more case-based dispatch plan rules.",
        ),
        (
            "WWCP007",
            skill.path,
            "Document Summary Contract",
            all(normalize(fragment) in skill_text for fragment in [
                    "`dispatch plan`: `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/dispatch-plan.md`",
                    "`design spec`: `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/design-spec.md`",
                    "`implementation plan`: `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/implementation-plan.md`",
                    "`working brief`: ready, version 2, `docs/superpowers/cases/example-case/rounds/2026-04-27-topic/working-brief.md`",
                    "`dispatch plan`: awaiting-approval, `docs/superpowers/cases/example-case/rounds/2026-04-27-topic/dispatch-plan.md`",
                ]),
            "SKILL.md document summary defaults are not fully aligned with case-based artifact paths.",
        ),
        (
            "WWCP008",
            readme.path,
            "What It Does",
            all(normalize(fragment) in readme_text for fragment in [
                    "writes round artifacts under `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/`",
                ])
            and normalize(
                "New `$ww` and `$www` rounds are canonically written under `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/`. Older type-based paths may still exist as legacy history during migration, but they are not active parallel write targets for new rounds."
            )
            in readme_text,
            "README.md is missing one or more case-based artifact path guidance rules.",
        ),
        (
            "WWCP009",
            skill.path,
            "Working Brief / Dispatch Plan File / Document Summary Contract",
            not any(
                fragment in skill.path.read_text(encoding="utf-8")
                for fragment in [
                    "docs/superpowers/working-briefs/YYYY-MM-DD-topic-vN.md",
                    "docs/superpowers/dispatch-plans/YYYY-MM-DD-topic.md",
                    "docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md",
                    "docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md",
                ]
            ),
            "SKILL.md still contains one or more old type-based canonical path templates.",
        ),
    ]

    for rule_id, file_path, section, passed, message in checks:
        results.append(
            Result(
                rule_id=rule_id,
                passed=passed,
                file=str(file_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                section=section,
                message=message if not passed else "ok",
            )
        )

    return results


def emit_human(results: List[Result]) -> None:
    failures = [result for result in results if not result.passed]
    if not failures:
        print(f"PASS: {len(results)} rules checked")
        return

    print(f"FAIL: {len(failures)} rule violations")
    print()
    for failure in failures:
        print(f"[{failure.rule_id}] {failure.file}")
        print(f"Section: {failure.section}")
        print(failure.message)
        print()


def emit_json(results: List[Result]) -> None:
    failures = sum(1 for result in results if not result.passed)
    payload = {
        "ok": failures == 0,
        "rule_failures": failures,
        "results": [result.to_dict() for result in results],
    }
    print(json.dumps(payload, indent=2))


def main() -> int:
    args = parse_args()

    try:
        md_cls = load_markdown_parser()
        documents = {name: parse_document(path, md_cls) for name, path in TARGETS.items()}
        results = build_results(documents)
    except DependencyError as exc:
        if args.as_json:
            print(
                json.dumps(
                    {"ok": False, "rule_failures": 0, "results": [], "error": str(exc)},
                    indent=2,
                )
            )
        else:
            print(f"ERROR: {exc}")
        return 2
    except Exception as exc:  # pragma: no cover
        if args.as_json:
            print(
                json.dumps(
                    {"ok": False, "rule_failures": 0, "results": [], "error": str(exc)},
                    indent=2,
                )
            )
        else:
            print(f"ERROR: {exc}")
        return 2

    if args.as_json:
        emit_json(results)
    else:
        emit_human(results)

    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

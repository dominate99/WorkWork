from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


SCRIPT_NAME = "validate_ww_persona_packets.py"
REPO_ROOT = Path(__file__).resolve().parent.parent

COMMON_REQUIRED_FIELDS = {
    "schema_version",
    "source_dispatch_plan",
    "source_plan_revision",
    "source_section_id",
    "orchestrator_type",
    "stage",
    "execution_id",
    "packet_id",
    "attempt_id",
    "supersedes_attempt_id",
    "accepts_late_results",
    "subagent_persona",
    "persona_source",
    "persona_rationale",
    "persona_binding",
    "derived_from_working_brief",
    "task_mode",
    "workflow_bindings",
    "working_brief_excerpt",
    "owned_scope",
    "read_scope",
    "write_scope",
    "non_goals",
    "success_criteria",
    "output_contract",
    "handoff_rule",
    "retry_policy",
    "close_policy",
    "result_artifact_location",
    "expected_return_status",
    "execution_binding",
    "requires_human_judgment",
}
WORKER_REQUIRED_FIELDS = {
    "work_mode",
    "work_mode_rationale",
    "goal_tuning",
    "constraint_precedence_note",
    "implementation_principles",
}
REVIEWER_REQUIRED_FIELDS = {
    "review_target_ref",
    "review_type",
    "pass_condition",
    "reject_condition",
}
ROLE_TEMPLATE_PATHS = {
    "worker": "agents/worker-prompt.md",
    "reviewer": "agents/reviewer-prompt.md",
    "explorer": "agents/explorer-prompt.md",
    "orchestrator": "agents/orchestrator-prompt.md",
}
ROLE_TASK_MODES = {
    "worker": "implement",
    "reviewer": "review",
    "explorer": "investigate",
}
APPROVED_PLAN_STATES = {"approved", "dispatched", "completed"}


@dataclass
class RuleResult:
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate persisted WorkWork runtime persona packet artifacts."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit machine-readable JSON output.",
    )
    return parser.parse_args()


def rel(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return path.as_posix()


def result(
    rule_id: str,
    passed: bool,
    packet_path: Path,
    repo_root: Path,
    message: str,
) -> RuleResult:
    return RuleResult(
        rule_id=rule_id,
        passed=passed,
        file=rel(packet_path, repo_root),
        section="Runtime Persona Packet",
        message="ok" if passed else message,
    )


def read_packet(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    payload = yaml.safe_load("\n".join(lines))
    if not isinstance(payload, dict):
        raise ValueError("packet body must be a YAML mapping")
    return payload


def read_personas(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    records = payload.get("personas", [])
    if not isinstance(records, list):
        raise ValueError(f"{path.as_posix()} must contain a personas list")
    return {
        record["id"]: record
        for record in records
        if isinstance(record, dict) and isinstance(record.get("id"), str)
    }


def as_mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def resolve_repo_relative_path(repo_root: Path, value: Any) -> Path | None:
    if not isinstance(value, str):
        return None
    relative_path = Path(value)
    if relative_path.is_absolute():
        return None
    resolved_root = repo_root.resolve()
    resolved_path = (resolved_root / relative_path).resolve()
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError:
        return None
    return resolved_path


def extract_dispatch_value(text: str, label: str) -> str | None:
    pattern = rf"(?m)^\s*-\s+{re.escape(label)}:\s*(.*?)\s*$"
    match = re.search(pattern, text)
    return match.group(1) if match else None


def extract_planned_section(text: str, section_id: str) -> str:
    planned_match = re.search(
        r"(?ms)^## Planned Sections\s*$\n(?P<body>.*?)(?=^## Section Runtime Ledger\s*$)",
        text,
    )
    planned_text = planned_match.group("body") if planned_match else text
    section_matches = list(re.finditer(r"(?m)^### Section: .+$", planned_text))
    for index, match in enumerate(section_matches):
        end = (
            section_matches[index + 1].start()
            if index + 1 < len(section_matches)
            else len(planned_text)
        )
        section_text = planned_text[match.start() : end]
        if re.search(
            rf"(?m)^-\s+Section ID:\s*{re.escape(section_id)}\s*$",
            section_text,
        ):
            return section_text
    return ""


def extract_worker_snapshot(text: str, persona_id: str) -> dict[str, Any]:
    marker = re.search(
        rf"(?m)^\s*-\s+Persona ID:\s*{re.escape(persona_id)}\s*$",
        text,
    )
    if not marker:
        return {}
    tail = text[marker.end() :]
    boundary = re.search(r"(?m)^\s{2}-\s+(?:Persona ID|Planned Scope):", tail)
    block = tail[: boundary.start()] if boundary else tail
    snapshot: dict[str, Any] = {}
    for label, key in [
        ("Source", "source"),
        ("Runtime Role", "runtime_role"),
        ("Selection Rationale", "rationale"),
        ("Template Path", "template_path"),
    ]:
        value = extract_dispatch_value(block, label)
        if value is not None:
            snapshot[key] = value.strip("`")
    lines = block.splitlines()
    for index, line in enumerate(lines):
        if line.strip() != "- Implementation Principles:":
            continue
        base_indent = len(line) - len(line.lstrip())
        principles: list[str] = []
        for item_line in lines[index + 1 :]:
            item_indent = len(item_line) - len(item_line.lstrip())
            stripped = item_line.strip()
            if stripped.startswith("- ") and item_indent > base_indent:
                principles.append(stripped[2:].strip())
                continue
            if stripped and item_indent <= base_indent:
                break
        snapshot["implementation_principles"] = principles
        break
    return snapshot


def extract_reviewer_snapshot(text: str, persona_id: str) -> dict[str, str]:
    snapshot: dict[str, str] = {}
    for label, key in [
        ("Planned Reviewer Persona", "persona"),
        ("Planned Reviewer Persona Source", "source"),
        ("Planned Reviewer Runtime Role", "runtime_role"),
        ("Planned Reviewer Selection Rationale", "rationale"),
        ("Planned Reviewer Template Path", "template_path"),
    ]:
        value = extract_dispatch_value(text, label)
        if value is not None:
            snapshot[key] = value.strip("`")
    if snapshot.get("persona") == persona_id:
        return snapshot

    lane_matches = list(re.finditer(r"(?m)^\s*-\s+Lane ID:\s*.+$", text))
    for index, match in enumerate(lane_matches):
        end = (
            lane_matches[index + 1].start()
            if index + 1 < len(lane_matches)
            else len(text)
        )
        lane_text = text[match.start() : end]
        lane_persona = extract_dispatch_value(lane_text, "Reviewer Persona")
        if lane_persona != persona_id:
            continue
        lane_snapshot = {"persona": lane_persona}
        for label, key in [
            ("Reviewer Source", "source"),
            ("Reviewer Runtime Role", "runtime_role"),
            ("Reviewer Selection Rationale", "rationale"),
            ("Reviewer Template Path", "template_path"),
        ]:
            value = extract_dispatch_value(lane_text, label)
            if value is not None:
                lane_snapshot[key] = value.strip("`")
        return lane_snapshot
    return {}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_required_fields(
    packet: dict[str, Any],
    packet_path: Path,
    repo_root: Path,
) -> RuleResult:
    required = set(COMMON_REQUIRED_FIELDS)
    role = as_mapping(packet.get("persona_binding")).get("runtime_role")
    if role == "worker":
        required.update(WORKER_REQUIRED_FIELDS)
    if role == "reviewer":
        required.update(REVIEWER_REQUIRED_FIELDS)
    missing = sorted(field for field in required if field not in packet)
    return result(
        "WWPP001",
        not missing,
        packet_path,
        repo_root,
        f"Missing required packet field(s): {', '.join(missing)}",
    )


def validate_dispatch_source(
    packet: dict[str, Any],
    packet_path: Path,
    repo_root: Path,
) -> tuple[RuleResult, str]:
    source = packet.get("source_dispatch_plan")
    if not isinstance(source, str):
        return (
            result(
                "WWPP002",
                False,
                packet_path,
                repo_root,
                "source_dispatch_plan must be a repository-relative path.",
            ),
            "",
        )
    source_path = resolve_repo_relative_path(repo_root, source)
    if source_path is None or not source_path.is_file():
        return (
            result(
                "WWPP002",
                False,
                packet_path,
                repo_root,
                f"source_dispatch_plan must stay inside the repository: {source}",
            ),
            "",
        )
    text = source_path.read_text(encoding="utf-8")
    plan_state = extract_dispatch_value(text, "Plan State")
    plan_revision = extract_dispatch_value(text, "Plan Revision")
    section_id = packet.get("source_section_id")
    section_text = (
        extract_planned_section(text, section_id) if isinstance(section_id, str) else ""
    )
    valid = (
        plan_state in APPROVED_PLAN_STATES
        and str(packet.get("source_plan_revision")) == plan_revision
        and bool(section_text)
    )
    return (
        result(
            "WWPP002",
            valid,
            packet_path,
            repo_root,
            "Packet must reference an approved, dispatched, or completed dispatch "
            "plan with matching revision and section id.",
        ),
        section_text,
    )


def validate_persona(
    packet: dict[str, Any],
    packet_path: Path,
    repo_root: Path,
    built_in: dict[str, dict[str, Any]],
    project: dict[str, dict[str, Any]],
) -> tuple[RuleResult, dict[str, Any]]:
    persona_id = packet.get("subagent_persona")
    source = packet.get("persona_source")
    rationale = packet.get("persona_rationale")
    source_records = {"built-in": built_in, "project": project}
    persona = source_records.get(source, {}).get(persona_id, {})
    fallback_ok = source != "built-in" or (
        isinstance(rationale, str)
        and "built-in fallback" in rationale
        and ("no stronger" in rationale or "no project" in rationale)
    )
    valid = (
        isinstance(persona_id, str)
        and source in source_records
        and bool(persona)
        and isinstance(rationale, str)
        and bool(rationale.strip())
        and fallback_ok
    )
    return (
        result(
            "WWPP003",
            valid,
            packet_path,
            repo_root,
            "Packet persona must resolve from persona_source and carry a non-empty "
            "rationale; built-in fallback rationale must explain why no project "
            "persona was stronger.",
        ),
        persona,
    )


def validate_role_binding(
    packet: dict[str, Any],
    packet_path: Path,
    repo_root: Path,
) -> RuleResult:
    binding = as_mapping(packet.get("persona_binding"))
    execution = as_mapping(packet.get("execution_binding"))
    role = binding.get("runtime_role")
    template = ROLE_TEMPLATE_PATHS.get(role)
    task_mode = ROLE_TASK_MODES.get(role)
    valid = (
        template is not None
        and binding.get("template_path") == template
        and execution.get("template_path") == template
        and (task_mode is None or packet.get("task_mode") == task_mode)
    )
    return result(
        "WWPP004",
        valid,
        packet_path,
        repo_root,
        "persona_binding.runtime_role, persona_binding.template_path, "
        "execution_binding.template_path, and task_mode must agree.",
    )


def validate_worker_gate(
    packet: dict[str, Any],
    persona: dict[str, Any],
    packet_path: Path,
    repo_root: Path,
) -> RuleResult:
    role = as_mapping(packet.get("persona_binding")).get("runtime_role")
    if role != "worker":
        return result("WWPP005", True, packet_path, repo_root, "")
    principles = packet.get("implementation_principles")
    valid = (
        persona.get("review_only") is False
        and persona.get("role_type") != "orchestrator"
        and isinstance(principles, list)
        and len(principles) == 2
        and principles == persona.get("implementation_principles")
    )
    return result(
        "WWPP005",
        valid,
        packet_path,
        repo_root,
        "Worker packet persona must be worker-capable and carry the selected "
        "persona's exact two ordered implementation principles.",
    )


def validate_reviewer_gate(
    packet: dict[str, Any],
    persona: dict[str, Any],
    packet_path: Path,
    repo_root: Path,
) -> RuleResult:
    role = as_mapping(packet.get("persona_binding")).get("runtime_role")
    if role != "reviewer":
        return result("WWPP006", True, packet_path, repo_root, "")
    valid = (
        persona.get("role_type") == "reviewer"
        and persona.get("review_only") is True
        and packet.get("write_scope") == []
        and packet.get("requires_human_judgment") is True
    )
    return result(
        "WWPP006",
        valid,
        packet_path,
        repo_root,
        "Reviewer packet persona must be reviewer-only, keep write_scope empty, "
        "and require human judgment.",
    )


def validate_reviewer_target(
    packet: dict[str, Any],
    packet_path: Path,
    repo_root: Path,
) -> RuleResult:
    role = as_mapping(packet.get("persona_binding")).get("runtime_role")
    if role != "reviewer":
        return result("WWPP007", True, packet_path, repo_root, "")
    target = as_mapping(packet.get("review_target_ref"))
    artifact_path = target.get("artifact_path")
    if not isinstance(artifact_path, str):
        valid = False
    else:
        resolved = resolve_repo_relative_path(repo_root, artifact_path)
        expected_hash = (
            f"sha256:{sha256(resolved)}"
            if resolved is not None and resolved.is_file()
            else None
        )
        artifact_revision = target.get("artifact_revision")
        content_hash = target.get("content_hash")
        content_hash_valid = isinstance(content_hash, str) and bool(
            re.fullmatch(r"sha256:[0-9a-f]{64}", content_hash)
        )
        full_file_fallback = (
            isinstance(artifact_revision, str)
            and artifact_revision.startswith("sha256:")
        )
        revision_valid = isinstance(artifact_revision, str) and bool(artifact_revision)
        if full_file_fallback:
            revision_valid = artifact_revision == expected_hash
            content_hash_valid = content_hash == expected_hash
        valid = (
            expected_hash is not None
            and revision_valid
            and content_hash_valid
            and target.get("schema_version") is not None
        )
    return result(
        "WWPP007",
        valid,
        packet_path,
        repo_root,
        "Reviewer packet review_target_ref must resolve to an immutable artifact "
        "snapshot with a valid revision token and SHA-256 content hash; full-file "
        "hash fallback values must match the referenced file.",
    )


def validate_dispatch_snapshot(
    packet: dict[str, Any],
    dispatch_text: str,
    packet_path: Path,
    repo_root: Path,
) -> RuleResult:
    role = as_mapping(packet.get("persona_binding")).get("runtime_role")
    if role == "reviewer":
        snapshot = extract_reviewer_snapshot(
            dispatch_text, packet.get("subagent_persona", "")
        )
    elif role in {"worker", "explorer"}:
        snapshot = extract_worker_snapshot(dispatch_text, packet.get("subagent_persona", ""))
    else:
        snapshot = {}
    required_matches = (
        snapshot.get("source") == packet.get("persona_source")
        and snapshot.get("runtime_role") == role
        and snapshot.get("rationale") == packet.get("persona_rationale")
    )
    if role == "reviewer":
        required_matches = required_matches and (
            snapshot.get("persona") == packet.get("subagent_persona")
        )
    template_path = snapshot.get("template_path")
    principles = snapshot.get("implementation_principles")
    optional_matches = (
        (
            template_path is None
            or template_path
            == as_mapping(packet.get("persona_binding")).get("template_path")
        )
        and (
            principles is None
            or principles == packet.get("implementation_principles")
        )
    )
    return result(
        "WWPP008",
        required_matches and optional_matches,
        packet_path,
        repo_root,
        "Packet persona source, runtime role, and rationale must match the approved "
        "dispatch selection; explicit prompt-path or worker-principle launch "
        "snapshots must also match when present.",
    )


def validate_packet(
    packet_path: Path,
    repo_root: Path,
    built_in: dict[str, dict[str, Any]],
    project: dict[str, dict[str, Any]],
) -> list[RuleResult]:
    try:
        packet = read_packet(packet_path)
    except Exception as exc:
        return [
            result(
                "WWPP001",
                False,
                packet_path,
                repo_root,
                f"Packet YAML could not be parsed: {exc}",
            )
        ]

    results = [validate_required_fields(packet, packet_path, repo_root)]
    dispatch_result, dispatch_text = validate_dispatch_source(packet, packet_path, repo_root)
    results.append(dispatch_result)
    persona_result, persona = validate_persona(
        packet, packet_path, repo_root, built_in, project
    )
    results.append(persona_result)
    results.append(validate_role_binding(packet, packet_path, repo_root))
    results.append(validate_worker_gate(packet, persona, packet_path, repo_root))
    results.append(validate_reviewer_gate(packet, persona, packet_path, repo_root))
    results.append(validate_reviewer_target(packet, packet_path, repo_root))
    results.append(
        validate_dispatch_snapshot(packet, dispatch_text, packet_path, repo_root)
    )
    return results


def validate_repository(repo_root: Path = REPO_ROOT) -> list[RuleResult]:
    built_in = read_personas(
        repo_root
        / "plugins/workwork/skills/ww-subagent-orchestrator/references/"
        "built-in-personas.yaml"
    )
    project = read_personas(repo_root / "docs/superpowers/personas/registry.yaml")
    packet_paths = sorted((repo_root / "docs/cases").glob("**/packets/*.md"))
    results: list[RuleResult] = []
    for packet_path in packet_paths:
        results.extend(validate_packet(packet_path, repo_root, built_in, project))
    return results


def emit_human(results: list[RuleResult]) -> None:
    failures = [item for item in results if not item.passed]
    if not failures:
        print(f"PASS: {len(results)} rules checked")
        return
    print(f"FAIL: {len(failures)} rule violations")
    print()
    for failure in failures:
        print(f"[{failure.rule_id}] {failure.file}")
        print(failure.message)
        print()


def emit_json(results: list[RuleResult]) -> None:
    failures = sum(1 for item in results if not item.passed)
    print(
        json.dumps(
            {
                "ok": failures == 0,
                "rule_failures": failures,
                "results": [item.to_dict() for item in results],
            },
            indent=2,
        )
    )


def main() -> int:
    args = parse_args()
    try:
        results = validate_repository()
    except Exception as exc:  # pragma: no cover - operational safeguard
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
    return 0 if all(item.passed for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

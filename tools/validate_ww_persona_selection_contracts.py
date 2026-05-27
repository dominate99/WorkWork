from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


SCRIPT_NAME = "validate_ww_persona_selection_contracts.py"
REPO_ROOT = Path(__file__).resolve().parent.parent


TARGETS = {
    "skill": REPO_ROOT / "plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md",
    "registry": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md",
    "working_brief_template": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md",
    "dispatch_plan_template": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md",
    "packet_contract": REPO_ROOT
    / "plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the WorkWork persona runtime-selection Markdown contract."
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


def file_contains(path: Path, fragment: str) -> bool:
    return normalize(fragment) in normalize(path.read_text(encoding="utf-8"))


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
    registry = documents["registry"]
    working_brief_template = documents["working_brief_template"]
    dispatch_plan_template = documents["dispatch_plan_template"]
    packet_contract = documents["packet_contract"]

    registry_selection = section_items(registry, "Selection Rules")
    registry_guidance_order = label_items(
        registry,
        "Runtime Selection Guidance",
        "Use this order when choosing between eligible personas",
    )
    registry_guidance_fields = label_items(
        registry,
        "Runtime Selection Guidance",
        "Use optional enrichment fields in these ways",
    )
    registry_guardrails = label_items(
        registry,
        "Runtime Selection Guidance",
        "Runtime-selection guardrails",
    )

    skill_persona = paragraph_items(skill, "Persona Planning")
    skill_worker_enforcement = label_items(
        skill,
        "Persona Planning",
        "For this first worker-enforcement layer",
    )
    skill_runtime_guidance = label_items(
        skill,
        "Persona Planning",
        "Runtime selection guidance",
    )
    skill_default_lane_mapping = label_items(
        skill,
        "Persona Planning",
        "Default review-lane persona mapping",
    )
    skill_worker_mapping = label_items(
        skill,
        "Persona Planning",
        "Default worker specialist mapping",
    )
    working_brief_persona_guidance = section_items(
        working_brief_template,
        "Persona And Workflow Guidance",
    )
    working_brief_candidate_sources = label_items(
        working_brief_template,
        "Persona And Workflow Guidance",
        "`candidate_persona_sources` should record",
    )
    working_brief_recommended_personas = label_items(
        working_brief_template,
        "Persona And Workflow Guidance",
        "Each `recommended_personas` entry should record",
    )
    working_brief_persona_rules = label_items(
        working_brief_template,
        "Persona And Workflow Guidance",
        "Persona recommendation rules",
    )
    working_brief_rules = section_items(working_brief_template, "Rules")
    dispatch_planned_section = section_items(
        dispatch_plan_template,
        "Planned Sections / Section: {{section_name}}",
    )
    dispatch_review_record = section_items(
        dispatch_plan_template,
        "Section Review Record / Section: {{section_name}}",
    )
    packet_required_fields = section_items(packet_contract, "Required Fields")
    packet_persona_source = label_items(
        packet_contract,
        "Required Fields",
        "`persona_source` contract",
    )
    packet_persona_binding = label_items(
        packet_contract,
        "Required Fields",
        "`persona_binding` contract",
    )
    packet_rules = section_items(packet_contract, "Packet Rules")

    checks = [
        (
            "WWPS001",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "Runtime persona selection must always establish baseline eligibility from required fields first.",
            ),
            "Missing required-fields-first baseline eligibility rule in persona selection.",
        ),
        (
            "WWPS002",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "After required-field eligibility is satisfied, optional enrichment fields may influence ranking, tie-breaks, and rationale quality.",
            ),
            "Missing ranking and tie-break rule for optional enrichment fields.",
        ),
        (
            "WWPS003",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "Optional enrichment fields must never override runtime-role boundaries, worker-capability gates, or project-registry preference rules.",
            ),
            "Missing guardrail preventing enrichment from overriding role boundaries, worker gates, or project preference.",
        ),
        (
            "WWPS004",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "During partial enrichment rollout, a persona must not be rejected solely because it lacks optional enrichment fields if it still satisfies the required-field baseline.",
            ),
            "Missing rollout safeguard for personas that still satisfy the required baseline without enrichment fields.",
        ),
        (
            "WWPS005",
            registry.path,
            "Selection Rules",
            has_fragment(
                registry_selection,
                "If optional enrichment fields are used in rationale, they must sharpen why a persona was chosen, not replace the required-field justification.",
            ),
            "Missing rationale rule that keeps enrichment subordinate to required-field justification.",
        ),
        (
            "WWPS006",
            registry.path,
            "Runtime Selection Guidance",
            all(
                has_fragment(registry_guidance_order, fragment)
                for fragment in [
                    "confirm required-field eligibility and role compatibility",
                    "prefer the strongest project-registry match over a generic built-in fallback",
                    "use `strengths`, `use_when`, `domains`, and language fit to narrow the viable set",
                    "use optional enrichment fields to rank viable candidates by decision posture, quality bar, tradeoff bias, and escalation fit",
                    "write rationale that names both the baseline fit and the enrichment-level fit when enrichment affected the choice",
                ]
            ),
            "Missing one or more ordered runtime-selection steps in persona registry guidance.",
        ),
        (
            "WWPS007",
            registry.path,
            "Runtime Selection Guidance",
            all(
                has_fragment(registry_guidance_fields, fragment)
                for fragment in [
                    "use to decide which persona should lead when the task's main ambiguity is about how to frame or resolve the work",
                    "use to decide which persona best matches the level of rigor the round actually needs",
                    "use to break ties when two personas are both capable but protect different outcomes",
                    "use to prefer the persona most likely to notice the dominant risk early",
                    "use to prefer the persona whose stopping conditions match the round's real irreversible risks",
                    "use to shape which specialist should synthesize, gate, or support when more than one persona is involved",
                    "use when coherence, clarity, or felt quality materially changes whether the result is good enough",
                ]
            ),
            "Missing one or more enrichment-field usage rules in persona registry guidance.",
        ),
        (
            "WWPS008",
            registry.path,
            "Runtime Selection Guidance",
            all(
                has_fragment(registry_guardrails, fragment)
                for fragment in [
                    "do not use optional enrichment fields to invent capability the persona does not already have in required fields",
                    "do not use optional enrichment fields to force a reviewer or orchestrator into the worker selection set",
                    "do not treat the presence of enrichment text as stronger than better required-field fit",
                    "if two candidates are still effectively tied after enrichment review, prefer the simpler selection and record the unresolved tie in rationale instead of overfitting",
                ]
            ),
            "Missing one or more runtime-selection guardrails in persona registry guidance.",
        ),
        (
            "WWPS009",
            skill.path,
            "Persona Planning",
            has_fragment(
                skill_persona,
                "Check for project personas first at `docs/superpowers/personas/registry.yaml`.",
            ),
            "Missing project-registry-first persona planning rule in SKILL.md.",
        ),
        (
            "WWPS010",
            skill.path,
            "Persona Planning",
            all(
                has_fragment(skill_runtime_guidance, fragment)
                for fragment in [
                    "derive the initial candidate set from required fields first",
                    "prefer the strongest project persona match before falling back to built-in personas",
                    "use `strengths`, `use_when`, `domains`, and language fit to narrow the viable set",
                    "once multiple candidates are still viable, use optional enrichment fields from `references/persona-registry.md` to rank and break ties",
                ]
            ),
            "Missing one or more candidate-selection narrowing steps in SKILL persona planning guidance.",
        ),
        (
            "WWPS011",
            skill.path,
            "Persona Planning",
            all(
                has_fragment(skill_runtime_guidance, fragment)
                for fragment in [
                    "use `decision_style` when the round's main ambiguity is how to frame or resolve the work",
                    "use `quality_bar` when the main differentiator is the rigor level the round requires",
                    "use `tradeoff_bias` and `failure_modes_to_watch` when two candidates are capable but protect different risks",
                    "use `escalation_triggers` when the choice depends on who should stop and escalate under irreversible or high-blast-radius conditions",
                    "use `collaboration_posture` and `taste_criteria` only when they materially improve specialist composition or quality judgment",
                ]
            ),
            "Missing one or more enrichment-driven tie-break rules in SKILL persona planning guidance.",
        ),
        (
            "WWPS012",
            skill.path,
            "Persona Planning",
            has_fragment(
                skill_runtime_guidance,
                "do not use optional enrichment fields to bypass role compatibility, worker-capability gates, or stronger required-field fit",
            ),
            "Missing SKILL guardrail preventing enrichment from bypassing compatibility or worker gates.",
        ),
        (
            "WWPS013",
            skill.path,
            "Persona Planning",
            has_fragment(
                skill_runtime_guidance,
                "if enrichment meaningfully affected the choice, say so in the persona rationale after the required-field justification",
            ),
            "Missing SKILL rationale requirement for enrichment-influenced persona selection.",
        ),
        (
            "WWPS014",
            skill.path,
            "Persona Planning",
            all(
                has_fragment(skill_runtime_guidance, fragment)
                for fragment in [
                    "determine the runtime role first: `orchestrator`, `worker`, `reviewer`, or `explorer`",
                    "load project candidates first, then built-in candidates, while preserving the source for every viable candidate",
                    "apply hard role gates before ranking: worker-capability gate for worker packets, reviewer-only gate for reviewer packets, orchestrator gate for round leadership, and read-only gate for explorer packets",
                ]
            ),
            "Missing runtime-role/source/gate ordering in SKILL persona planning guidance.",
        ),
        (
            "WWPS015",
            skill.path,
            "Persona Planning",
            all(
                has_fragment(skill_worker_enforcement, fragment)
                for fragment in [
                    "persona selection adoption is a recording contract as well as a ranking contract",
                    "reviewer-only personas must have `role_type: reviewer`, `review_only: true`, no worker write authority, and `agents/reviewer-prompt.md` as the launch prompt binding before they may staff a review lane",
                    "project persona priority applies only after role gates and required-field fit",
                    "built-in fallback must be explicit, not silent",
                ]
            ),
            "Missing persona recording, reviewer gate, project priority, or built-in fallback contract in SKILL.md.",
        ),
        (
            "WWPS016",
            skill.path,
            "Persona Planning",
            all(
                has_fragment(skill_default_lane_mapping, fragment)
                for fragment in [
                    "`spec-review` -> `spec-reviewer`",
                    "`code-quality-review` -> `code-quality-reviewer`",
                    "`scope-review` -> `product-scope-reviewer`",
                    "`editorial-review` -> `editorial-reviewer`",
                    "`other` -> no default",
                ]
            )
            and file_contains(
                skill.path,
                "Cross-cutting reviewer personas do not replace durable lane reviewers by default.",
            ),
            "Missing durable review-lane mapping or cross-cutting reviewer guardrail in SKILL.md.",
        ),
        (
            "WWPS017",
            skill.path,
            "Persona Planning",
            all(
                has_fragment(skill_worker_mapping, fragment)
                for fragment in [
                    "backend services, APIs, or integration boundaries -> `senior-backend-engineer`",
                    "Java-specific implementation -> `java-pro-engineer`",
                    "frontend/product UI -> `frontend-product-engineer`",
                    "tests, fixtures, or regression harnesses -> `test-quality-engineer`",
                    "CI, release, deployment, or infrastructure -> `devops-release-engineer`",
                    "data, analytics, or ML workflows -> `data-ml-engineer`",
                    "docs, guides, or maintainer instructions -> `technical-writer`",
                ]
            ),
            "Missing worker specialist mapping in SKILL.md.",
        ),
        (
            "WWPS018",
            working_brief_template.path,
            "Persona And Workflow Guidance",
            all(
                has_fragment(working_brief_persona_guidance, fragment)
                for fragment in [
                    "`candidate_persona_sources`",
                    "`recommended_personas`",
                    "`persona_selection_notes`",
                ]
            ),
            "Missing persona source or recommendation fields in working brief template.",
        ),
        (
            "WWPS019",
            working_brief_template.path,
            "Persona And Workflow Guidance",
            all(
                has_fragment(working_brief_candidate_sources, fragment)
                for fragment in [
                    "project registry checked: true|false",
                    "built-in fallback checked: true|false",
                    "project registry outcome",
                    "built-in fallback outcome",
                    "fallback rationale when a built-in persona is recommended",
                ]
            ),
            "Missing candidate_persona_sources recording fields in working brief template.",
        ),
        (
            "WWPS020",
            working_brief_template.path,
            "Persona And Workflow Guidance",
            all(
                has_fragment(working_brief_recommended_personas, fragment)
                for fragment in [
                    "persona id",
                    "runtime role: `orchestrator` | `worker` | `reviewer` | `explorer`",
                    "source: `project` | `built-in`",
                    "baseline required-field fit rationale grounded in the working brief",
                    "project-priority or built-in-fallback rationale",
                    "role binding from `agents/openai.yaml`",
                    "prompt asset used for launch assembly",
                ]
            ),
            "Missing recommended persona source/runtime-role/rationale fields in working brief template.",
        ),
        (
            "WWPS021",
            working_brief_template.path,
            "Persona And Workflow Guidance",
            all(
                has_fragment(working_brief_persona_rules, fragment)
                for fragment in [
                    "project registry priority applies only after the persona satisfies the relevant runtime-role gate and required-field fit",
                    "use a project persona only when it is stronger than the built-in fallback or adds project-specific value the built-in cannot carry",
                    "record built-in fallback explicitly when no project persona is eligible or stronger",
                    "worker recommendations must pass the worker-capability gate before appearing as worker candidates",
                    "reviewer recommendations must pass the reviewer-only gate before appearing as review-lane candidates",
                ]
            )
            and has_fragment(
                working_brief_rules,
                "Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.",
            ),
            "Missing working brief persona recommendation gate and rationale rules.",
        ),
        (
            "WWPS022",
            dispatch_plan_template.path,
            "Planned Sections",
            all(
                has_fragment(dispatch_planned_section, fragment)
                for fragment in [
                    "Planned Reviewer Persona Source: project | built-in",
                    "Planned Reviewer Runtime Role: reviewer",
                    "Planned Reviewer Selection Rationale: {{reviewer_persona_rationale}}",
                    "Source: project | built-in",
                    "Runtime Role: worker | explorer | none",
                    "Selection Rationale:",
                ]
            ),
            "Missing planned reviewer or specialist persona source/runtime-role/rationale fields in dispatch plan template.",
        ),
        (
            "WWPS023",
            dispatch_plan_template.path,
            "Planned Sections",
            all(
                has_fragment(dispatch_planned_section, fragment)
                for fragment in [
                    "Reviewer Source: project | built-in",
                    "Reviewer Runtime Role: reviewer",
                    "Reviewer Selection Rationale:",
                    "Review lane mapping rule: default built-in reviewer mapping is `spec-review` -> `spec-reviewer`",
                    "Cross-cutting reviewer rule: add `secure-software-engineer`, `accessibility-ux-reviewer`, or `documentation-clarity-reviewer` as a second review lane",
                    "Worker specialist mapping rule: select worker specialists by owned scope and dominant implementation risk",
                    "Persona source rule: project personas win only after role-gate and required-field eligibility",
                ]
            ),
            "Missing review lane source/runtime-role/rationale fields or mapping rules in dispatch plan template.",
        ),
        (
            "WWPS024",
            dispatch_plan_template.path,
            "Section Review Record",
            all(
                has_fragment(dispatch_review_record, fragment)
                for fragment in [
                    "Reviewer Source:",
                    "Reviewer Runtime Role: reviewer",
                    "Reviewer Findings:",
                    "Orchestrator Synthesis:",
                ]
            ),
            "Missing reviewer source/runtime-role fields in dispatch plan review records.",
        ),
        (
            "WWPS025",
            packet_contract.path,
            "Required Fields",
            has_fragment(packet_required_fields, "`persona_source`"),
            "Missing persona_source as a required packet field.",
        ),
        (
            "WWPS026",
            packet_contract.path,
            "Required Fields",
            all(
                has_fragment(packet_persona_source, fragment)
                for fragment in [
                    "one of `project` or `built-in`",
                    "`project` means the selected persona came from `docs/superpowers/personas/registry.yaml`",
                    "`built-in` means the selected persona came from `references/built-in-personas.yaml`",
                    "built-in fallback must have a rationale that says why no project persona was eligible or stronger",
                    "project persona priority applies only after runtime-role gates and required-field fit",
                ]
            ),
            "Missing persona_source source-of-truth and fallback contract in packet contract.",
        ),
        (
            "WWPS027",
            packet_contract.path,
            "Required Fields",
            all(
                has_fragment(packet_persona_binding, fragment)
                for fragment in [
                    "`runtime_role` must be exactly one of `orchestrator`, `worker`, `reviewer`, or `explorer`",
                    "`template_path` must point to the matching role prompt asset",
                    "worker packets use `agents/worker-prompt.md`",
                    "reviewer packets use `agents/reviewer-prompt.md`",
                    "explorer packets use `agents/explorer-prompt.md`",
                ]
            ),
            "Missing persona_binding runtime-role or prompt binding contract.",
        ),
        (
            "WWPS028",
            packet_contract.path,
            "Packet Rules",
            all(
                has_fragment(packet_rules, fragment)
                for fragment in [
                    "`persona_source` must be copied from the approved dispatch plan selection, not inferred silently at launch",
                    "`persona_rationale` must include baseline required-field fit plus project-priority or built-in-fallback rationale",
                    "packets must not use optional enrichment fields to bypass runtime-role gates, worker-capability gates, reviewer-only gates, or stronger required-field fit",
                    "worker packet creation must fail unless the selected persona has `review_only: false`, `role_type` not equal to `orchestrator`, and exactly two `implementation_principles`",
                    "reviewer packet creation must fail unless the selected persona has `role_type: reviewer`, `review_only: true`, no worker write authority, and `agents/reviewer-prompt.md` as the prompt binding",
                ]
            ),
            "Missing packet rules for persona source/rationale persistence or worker/reviewer gates.",
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

    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

# Subagent Packet Contract

Create a packet only after:

- `estimation_complete: true`
- `brief_status: ready`
- dispatch plan state: `approved`

## Required Fields

- `source_dispatch_plan`
- `source_plan_revision`
- `source_section_id`
- `workstream_id`
- `review_pass_id` (required for reviewer packets; omit or set `none` for non-review workstreams)
- `orchestrator_type`
- `stage`
- `subagent_persona`
- `persona_rationale`
- `derived_from_working_brief`
- `task_mode`
- `workflow_bindings[]`
- `working_brief_excerpt`
- `owned_scope`
- `non_goals`
- `success_criteria`
- `output_contract`
- `handoff_rule`
- `requires_human_judgment`

## Packet Rules

- Packets are derived from approved dispatch plan sections, not drafted directly from the working brief.
- Packets are not live progress stores. Live progress is persisted in the dispatch plan `Progress Board`.
- `workflow_bindings[]` may contain more than one Superpowers skill when a stage legitimately requires it.
- `workstream_id` must stay stable for the same workstream across turn updates.
- Reviewer workstreams must be keyed by `source_section_id + review_pass_id`.
- If more than one reviewer is used for the same section and review pass, append a stable reviewer-specific suffix to `workstream_id`.
- `handoff_rule` must route reviewer results back to the orchestrator before human judgment.
- `requires_human_judgment` must be `true` for reviewer packets.
- `non_goals` should explicitly block unauthorized rewrites, scope growth, or final decision-making.

## Reviewer Packet Defaults

- `task_mode: review`
- `output_contract: findings only`
- `handoff_rule: return to orchestrator, then human judgment required`
- `requires_human_judgment: true`

## Example

```text
source_dispatch_plan: docs/superpowers/dispatch-plans/2026-05-05-topic.md
source_plan_revision: 2
orchestrator_type: staff engineer orchestrator
stage: review
subagent_persona: secure software engineer
persona_rationale: working brief identifies elevated auth security risk
source_section_id: auth-review
workstream_id: auth-review-review-1-secure-software-engineer
review_pass_id: review-1
derived_from_working_brief: backend auth path, release-sensitive, security-critical
task_mode: review
workflow_bindings:
- superpowers:requesting-code-review
- superpowers:verification-before-completion
working_brief_excerpt: auth review is release-sensitive and requires findings-only reviewer coverage
owned_scope: authentication changes in backend service
non_goals: do not rewrite code, do not approve release, do not make final decisions
success_criteria: identify security-relevant findings with severity and rationale
output_contract: findings only
handoff_rule: return to orchestrator, then human judgment required
requires_human_judgment: true
```

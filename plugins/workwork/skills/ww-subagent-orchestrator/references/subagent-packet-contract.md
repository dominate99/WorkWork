# Subagent Packet Contract

Create a packet only after:

- `estimation_complete: true`
- `brief_status: ready`
- dispatch plan state: `approved`

## Required Fields

- `schema_version`
- `source_dispatch_plan`
- `source_plan_revision`
- `source_section_id`
- `orchestrator_type`
- `stage`
- `execution_id`
- `packet_id`
- `attempt_id`
- `supersedes_attempt_id`
- `accepts_late_results`
- `subagent_persona`
- `persona_rationale`
- `persona_binding`
- `derived_from_working_brief`
- `task_mode`
- `workflow_bindings[]`
- `working_brief_excerpt`
- `owned_scope`
- `read_scope`
- `write_scope`
- `non_goals`
- `success_criteria`
- `output_contract`
- `handoff_rule`
- `retry_policy`
- `close_policy`
- `result_artifact_location`
- `expected_return_status[]`
- `execution_binding`
- `requires_human_judgment`

Reviewer packets additionally require:

- `review_target_ref`
- `review_type`
- `pass_condition`
- `reject_condition`

## Execution Binding

`execution_binding` should define how the controller launches the subagent.

Required execution-binding fields:

- `agent_type`
- `context_mode`
- `fork_context`
- `model_tier`
- `reasoning_effort`
- `template_path`
- `prompt_inputs`

Defaults:

- `context_mode`: `curated-only`
- `fork_context`: `false`
- reviewer `agent_type`: `default`
- implementer `agent_type`: `worker`
- read-only investigators `agent_type`: `explorer`

## Packet Rules

- Packets are derived from approved dispatch plan sections, not drafted directly from the working brief.
- `workflow_bindings[]` may contain more than one Superpowers skill when a stage legitimately requires it.
- `handoff_rule` must route reviewer results back to the orchestrator before human judgment.
- `requires_human_judgment` must be `true` for reviewer packets.
- `non_goals` should explicitly block unauthorized rewrites, scope growth, or final decision-making.
- `write_scope` must be empty for reviewer packets unless the dispatch plan explicitly allows a rewrite stage.
- `expected_return_status[]` must align with the controller transition table.
- `execution_id` remains stable across retries of the same logical work item.
- `packet_id` rotates when the execution payload changes.
- `attempt_id` rotates on relaunch.
- `supersedes_attempt_id` should point to the replaced attempt when a relaunch supersedes prior execution.
- `accepts_late_results` must be `false` by default and enabled only when the controller explicitly wants to reconcile stale outputs.

## Reviewer Target Contract

`review_target_ref` is immutable per packet and must contain:

- `artifact_path`
- `artifact_kind`
- `artifact_revision`
- `schema_version`
- `section_anchor` when applicable
- `content_hash` when the target is excerpt-backed or when full-file hash fallback is used

Revision rules:

- working brief review targets use `brief_version`
- dispatch section review targets use `plan_revision + section_id`
- implementation-plan review targets use `implementation_plan_revision`
- design-spec review targets use `design_spec_revision`
- excerpt-backed targets use the exact reviewed slice hash for `content_hash` and the source document revision or version token for `artifact_revision`
- full-file targets without explicit document version use the same full-file hash for both `artifact_revision` and `content_hash`
- registry records never store `artifact_revision` or `content_hash`; those values are generated from the resolved artifact snapshot at packet creation time

## Reviewer Packet Defaults

- `task_mode: review`
- `agent_type: default`
- `output_contract: findings only`
- `handoff_rule: return to orchestrator, then human judgment required`
- `retry_policy: relaunch only through orchestrator decision`
- `close_policy: close after synthesis and recorded decision`
- `requires_human_judgment: true`
- `write_scope: []`

## Worker Packet Defaults

- `task_mode: implement`
- `agent_type: worker`
- `context_mode: curated-only`
- `fork_context: false`
- `retry_policy: relaunch with new attempt_id after orchestrator decision`
- `close_policy: close after reviewer handoff or explicit stop`
- `requires_human_judgment: false`

## Explorer Packet Defaults

- `task_mode: investigate`
- `agent_type: explorer`
- `context_mode: curated-only`
- `fork_context: false`
- `write_scope: []`
- `retry_policy: relaunch only through orchestrator decision`
- `close_policy: close after findings are handed back`
- `requires_human_judgment: false`

## Example

```text
schema_version: 1
source_dispatch_plan: docs/superpowers/dispatch-plans/2026-05-06-topic.md
source_plan_revision: 1
source_section_id: section-core-runtime-contracts
orchestrator_type: staff engineer orchestrator
stage: review
execution_id: exec-core-runtime-review-01
packet_id: packet-core-runtime-review-01
attempt_id: attempt-core-runtime-review-01
supersedes_attempt_id:
accepts_late_results: false
subagent_persona: secure software engineer
persona_rationale: working brief identifies elevated runtime-policy integrity risk
persona_binding:
  runtime_role: reviewer
  template_path: agents/reviewer-prompt.md
derived_from_working_brief: runtime state and packet contract changes are release-sensitive
task_mode: review
workflow_bindings:
- superpowers:requesting-code-review
working_brief_excerpt: section 1 owns ww runtime contract files
owned_scope: core runtime contract docs only
read_scope:
- path_glob: references/*.md
write_scope: []
non_goals: do not rewrite files, do not approve release, do not change scope
success_criteria: identify semantic inconsistencies and missing runtime guarantees
output_contract: findings only
handoff_rule: return to orchestrator, then human judgment required
retry_policy: relaunch only through orchestrator decision
close_policy: close after synthesis and recorded decision
result_artifact_location: not created yet
expected_return_status:
- PASS
- REJECT
execution_binding:
  agent_type: default
  context_mode: curated-only
  fork_context: false
  model_tier: strong
  reasoning_effort: high
  template_path: agents/reviewer-prompt.md
  prompt_inputs:
    focus: runtime-policy consistency
review_target_ref:
  artifact_path: references/subagent-packet-contract.md
  artifact_kind: markdown
  artifact_revision: hash-abc123
  schema_version: 1
  section_anchor: required-fields
  content_hash: hash-abc123
review_type: code-quality
pass_condition: no material findings
reject_condition: any blocking semantic mismatch
requires_human_judgment: true
```

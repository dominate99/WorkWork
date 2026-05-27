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
- `persona_source`
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

Worker packets additionally require:

- `work_mode`
- `work_mode_rationale`
- `goal_tuning`
- `constraint_precedence_note`
- `implementation_principles[]`

`implementation_principles[]` contract:

- ordered list of exactly two strings
- index `0` is the hard implementation rule
- index `1` is the soft implementation principle

`subagent_persona` contract:

- canonical persona `id` string from the project registry or built-in persona data file
- do not persist display-only `title` text in `subagent_persona`

`persona_source` contract:

- one of `project` or `built-in`
- `project` means the selected persona came from `docs/superpowers/personas/registry.yaml`
- `built-in` means the selected persona came from `references/built-in-personas.yaml`
- built-in fallback must have a rationale that says why no project persona was eligible or stronger
- project persona priority applies only after runtime-role gates and required-field fit

`persona_binding` contract:

- `runtime_role` must be exactly one of `orchestrator`, `worker`, `reviewer`, or `explorer`
- `template_path` must point to the matching role prompt asset
- worker packets use `agents/worker-prompt.md`
- reviewer packets use `agents/reviewer-prompt.md`
- explorer packets use `agents/explorer-prompt.md`
- role prompt behavior and persona records remain separate concepts

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
- `subagent_persona` must use the canonical persona `id`, not a free-text display label
- `persona_source` must be copied from the approved dispatch plan selection, not inferred silently at launch
- `persona_rationale` must include baseline required-field fit plus project-priority or built-in-fallback rationale
- packets must not use optional enrichment fields to bypass runtime-role gates, worker-capability gates, reviewer-only gates, or stronger required-field fit
- worker packets must carry `implementation_principles` as one canonical top-level field, not only inside `persona_binding`
- worker-packet `implementation_principles` must be sourced directly from the selected persona definition
- worker-packet `implementation_principles` must contain exactly two entries: the hard rule first and the soft principle second
- worker packet creation must fail unless the selected persona has `review_only: false`, `role_type` not equal to `orchestrator`, and exactly two `implementation_principles`
- reviewer packet creation must fail unless the selected persona has `role_type: reviewer`, `review_only: true`, no worker write authority, and `agents/reviewer-prompt.md` as the prompt binding
- worker packets must inherit exactly one effective `work_mode` from the approved dispatch-plan section
- `work_mode` is an execution snapshot field, not a recommendation field
- `work_mode_rationale` must stay aligned with the section's recorded worker-mode rationale
- `goal_tuning` must not introduce a new execution bias that is absent from the dispatch plan
- `constraint_precedence_note` must explicitly state that packet constraints, user limits, and non-goals take precedence over `work_mode`
- `task_mode` remains separate from `work_mode`; it must not be reused as a worker-mode field or synonym
- if a worker-mode change alters the execution payload, the controller must rotate `packet_id`; if the worker is relaunched, it must also rotate `attempt_id`
- a launched packet must not be silently edited in place to change `work_mode`

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
- `work_mode: plan-first | validate-first | iterate-first | conservative-first`
- `goal_tuning: none | speed-biased | safety-biased | validation-biased`
- `implementation_principles: [hard-rule, soft-principle]`
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

## Reviewer Packet Example

```text
schema_version: 1
source_dispatch_plan: docs/legacy/superpowers/dispatch-plans/2026-05-06-topic.md
source_plan_revision: 1
source_section_id: section-core-runtime-contracts
orchestrator_type: staff-engineer-orchestrator
stage: review
execution_id: exec-core-runtime-review-01
packet_id: packet-core-runtime-review-01
attempt_id: attempt-core-runtime-review-01
supersedes_attempt_id:
accepts_late_results: false
subagent_persona: secure-software-engineer
persona_source: built-in
persona_rationale: working brief identifies elevated runtime-policy integrity risk; built-in fallback selected because no stronger project reviewer was eligible for this security-focused lane
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

## Worker Packet Example

```text
schema_version: 1
source_dispatch_plan: docs/legacy/superpowers/dispatch-plans/2026-05-16-worker-persona-enforcement.md
source_plan_revision: 2
source_section_id: section-worker-persona-enforcement
orchestrator_type: staff-engineer-orchestrator
stage: implement
execution_id: exec-worker-persona-enforcement-01
packet_id: packet-worker-persona-enforcement-01
attempt_id: attempt-worker-persona-enforcement-01
supersedes_attempt_id:
accepts_late_results: false
subagent_persona: senior-backend-engineer
persona_source: built-in
persona_rationale: working brief identifies backend-oriented implementation work with service-boundary and correctness risk; built-in fallback selected because no stronger project worker persona was eligible for the backend scope
persona_binding:
  runtime_role: worker
  template_path: agents/worker-prompt.md
implementation_principles:
  - prefer service-boundary correctness and data integrity over implementation speed
  - when tradeoffs are close, bias toward explicit interfaces and maintainable structure
work_mode: validate-first
work_mode_rationale: this section modifies existing runtime contract behavior and must verify current semantics before implementation
goal_tuning: validation-biased
constraint_precedence_note: keep approved scope, explicit user limits, and non-goals ahead of worker-mode posture
derived_from_working_brief: worker persona enforcement requires backend-oriented contract and prompt edits
task_mode: implement
workflow_bindings:
- superpowers:subagent-driven-development
working_brief_excerpt: section 1 owns worker persona contract and prompt surfaces
owned_scope: worker persona contract and prompt files only
read_scope:
- path_glob: references/*.md
write_scope:
- path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md
- path_glob: plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md
non_goals: do not widen reviewer or explorer behavior, do not change unrelated persona records, do not rewrite the approved spec
success_criteria: worker packet carries canonical implementation principles and worker runtime behavior consumes them in order
output_contract: implementation result summary plus exact artifact locations
handoff_rule: return to orchestrator for review and human judgment
retry_policy: relaunch with new attempt_id after orchestrator decision
close_policy: close after reviewer handoff or explicit stop
result_artifact_location: not created yet
expected_return_status:
- DONE
- DONE_WITH_CONCERNS
- NEEDS_CONTEXT
- BLOCKED
- FAILED
execution_binding:
  agent_type: worker
  context_mode: curated-only
  fork_context: false
  model_tier: strong
  reasoning_effort: high
  template_path: agents/worker-prompt.md
  prompt_inputs:
    focus: worker persona enforcement
requires_human_judgment: false
```

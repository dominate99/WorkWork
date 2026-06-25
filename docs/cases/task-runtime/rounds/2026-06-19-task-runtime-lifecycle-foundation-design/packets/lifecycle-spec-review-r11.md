# Canonical Reviewer Packet: Task Runtime Lifecycle Foundation Design Revision 11

schema_version: 1
source_dispatch_plan: docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/dispatch-plan.md
source_plan_revision: 2
source_section_id: LIFECYCLE-DESIGN-001
orchestrator_type: pm-orchestrator
stage: review
execution_id: exec-lifecycle-spec-review-01
packet_id: packet-lifecycle-spec-review-r11-10
attempt_id: attempt-lifecycle-spec-review-r11-10
supersedes_attempt_id: attempt-lifecycle-spec-review-r10-09
accepts_late_results: false
subagent_persona: spec-reviewer
persona_source: built-in
persona_rationale: lifecycle state authority, deterministic transitions, compatibility, migration, and testable acceptance criteria make the built-in spec reviewer the strongest eligible reviewer-only match; built-in fallback is used because no stronger project reviewer covers specification contract fidelity.
persona_binding:
  runtime_role: reviewer
  template_path: agents/reviewer-prompt.md
derived_from_working_brief: review the stable lifecycle foundation design against the approved umbrella architecture, current runtime-state authority, migration safety, and explicit non-goals
task_mode: review
workflow_bindings:
  - superpowers:requesting-code-review
  - superpowers:verification-before-completion
working_brief_excerpt: define one section-owned lifecycle phase, preserve runtime_state authority, require exact transition events, derive round rollups, and defer verifier, hooks, quality gates, validators, and implementation
owned_scope: findings on lifecycle foundation design revision 11 only
read_scope:
  - path_glob: docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md
  - path_glob: docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/working-brief.md
  - path_glob: docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md
write_scope: []
non_goals: do not rewrite files, design verifier authority, design hooks or quality scoring, edit contracts or validators, add personas, create an implementation plan, widen scope, or make the final human decision
success_criteria: identify any material contradiction in state ownership, exact transitions, legacy crosswalk, snapshot/event consistency, migration bootstrap, recovery, round rollup, or non-goal discipline
output_contract: findings only, at most five, ordered by severity; explicitly report no material findings when none exist
handoff_rule: return to orchestrator, then human judgment required
retry_policy: relaunch only through orchestrator decision with a new packet and attempt when the target revision changes
close_policy: close after orchestrator synthesis and recorded human decision
result_artifact_location: not created yet
expected_return_status:
  - PASS
  - REJECT
  - NEEDS_CONTEXT
execution_binding:
  agent_type: default
  context_mode: curated-only
  fork_context: false
  model_tier: strong
  reasoning_effort: high
  template_path: agents/reviewer-prompt.md
  prompt_inputs:
    focus: lifecycle state authority, exact transition determinism, legacy compatibility, migration safety, snapshot/event consistency, recovery, and scope discipline
review_target_ref:
  artifact_path: docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md
  artifact_kind: design_spec
  artifact_revision: "11"
  schema_version: 1
  section_anchor: full-file lifecycle foundation design
  content_hash: sha256:360ee0d13e3dc705560d3dd7de9e2c3be49251df9e9e32ff2728a1c115b86e6b
review_type: spec-review
pass_condition: no material findings in lifecycle authority, transition determinism, legacy compatibility, migration bootstrap, snapshot/event consistency, recovery, rollup derivation, or non-goal discipline
reject_condition: any material contradiction, ambiguous transition authority, unsafe migration, inconsistent snapshot/event rule, or scope expansion remains
requires_human_judgment: true

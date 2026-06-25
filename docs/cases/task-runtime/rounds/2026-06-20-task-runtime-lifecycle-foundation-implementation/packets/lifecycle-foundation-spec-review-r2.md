# Reviewer Packet: Lifecycle Foundation Revision 2 Contract Fidelity

schema_version: 2
source_dispatch_plan: docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/dispatch-plan.md
source_plan_revision: 2
source_section_id: section-lifecycle-foundation-implementation
source_dispatch_schema_version: 1
source_lifecycle_protocol: legacy
orchestrator_type: staff-engineer-orchestrator
stage: review
execution_id: exec-lifecycle-foundation-spec-review-r2
packet_id: packet-lifecycle-foundation-spec-review-r2b
attempt_id: attempt-lifecycle-foundation-spec-review-r2b
supersedes_attempt_id: attempt-lifecycle-foundation-spec-review-r2
accepts_late_results: false
subagent_persona: spec-reviewer
persona_source: built-in
persona_rationale: compare every contract and template change with approved design revision 11, especially ownership, dormant activation, schema coordination, migration, and exclusions; built-in fallback is used because no stronger eligible project reviewer covers lifecycle contract fidelity
persona_binding:
  runtime_role: reviewer
  template_path: agents/reviewer-prompt.md
derived_from_working_brief: revision 2 defines deterministic schema-0/1 legacy normalization, requires implemented and verified activation capabilities, and preserves lifecycle authority and migration safety
task_mode: review
workflow_bindings:
  - superpowers:requesting-code-review
  - superpowers:verification-before-completion
working_brief_excerpt: verify revision 2 resolves the pre-commit P1/P2 findings without activating task-runtime-v1 or expanding into dedicated lifecycle validation
owned_scope: findings on revision 2 lifecycle contract fidelity only
read_scope:
  - path_glob: docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md
  - path_glob: README.md
write_scope: []
non_goals: do not edit files, implement runtime phases, add lifecycle validator rules, add personas, expand routing, or make the final human decision
success_criteria: identify at most five remaining material contract contradictions or explicitly report no material findings
output_contract: findings only, ordered by severity, with file and line references
handoff_rule: return to orchestrator for synthesis and human judgment
retry_policy: relaunch only after an orchestrator decision and a changed immutable target
close_policy: close after findings are synthesized and recorded
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
    focus: schema normalization, activation safety, state ownership, exact lifecycle semantics, migration, recovery, and scope discipline
review_target_ref:
  artifact_path: plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md
  artifact_kind: normative_reference
  artifact_revision: sha256:0a89c9565099148e316db25196c9d960cc67c416fd67adb33c98bd3584d7310b
  schema_version: 2
  section_anchor: full-file revision 2 lifecycle contract
  content_hash: sha256:0a89c9565099148e316db25196c9d960cc67c416fd67adb33c98bd3584d7310b
review_type: spec-review
pass_condition: no material mismatch with approved lifecycle design or revision 2 pre-commit requirements
reject_condition: any material normalization ambiguity, unsafe activation path, authority conflict, migration gap, or scope expansion remains
requires_human_judgment: true

# Reviewer Packet: Verifier And Lane Authority Design Spec Review

schema_version: 2
source_dispatch_plan: docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/dispatch-plan.md
source_plan_revision: 1
source_section_id: section-verifier-lane-authority-design
source_dispatch_schema_version: 2
source_lifecycle_protocol: legacy
orchestrator_type: pm-orchestrator
stage: review
execution_id: exec-verifier-lane-spec-review-r1
packet_id: packet-verifier-lane-spec-review-r1
attempt_id: attempt-verifier-lane-spec-review-r1
supersedes_attempt_id:
accepts_late_results: false
subagent_persona: spec-reviewer
persona_source: built-in
persona_rationale: review implementation readiness, deterministic authority, schema completeness, compatibility, acceptance criteria, and exclusions; built-in fallback is used because no stronger eligible project reviewer covers portable runtime specification fidelity
persona_binding:
  runtime_role: reviewer
  template_path: agents/reviewer-prompt.md
derived_from_working_brief: verifier authority, lane and evidence schemas, deterministic selection, staleness, and model capability profiles must be implementation-ready without activating runtime behavior
task_mode: review
workflow_bindings:
  - superpowers:requesting-code-review
  - superpowers:verification-before-completion
working_brief_excerpt: review one authority-first design against the approved umbrella runtime and lifecycle foundation while preserving all implementation and later-round exclusions
owned_scope: findings on verifier and lane authority design revision 1 only
read_scope:
  - path_glob: docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md
  - path_glob: docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md
  - path_glob: docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/working-brief.md
write_scope: []
non_goals: do not rewrite the design, add implementation details owned by later rounds, edit files, widen scope, or make the final human decision
success_criteria: identify at most five material contradictions, ambiguities, missing schemas, non-deterministic decisions, compatibility gaps, or scope violations; explicitly report no material findings when none exist
output_contract: findings only, ordered by severity, with file and line references
handoff_rule: return to pm-orchestrator for synthesis and human judgment
retry_policy: relaunch only through orchestrator decision with a new packet and attempt when the target revision changes
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
    focus: implementation readiness, authority determinism, lane and evidence completeness, selection, staleness, model profiles, lifecycle compatibility, and exclusions
review_target_ref:
  artifact_path: docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md
  artifact_kind: design_spec
  artifact_revision: "1"
  schema_version: 2
  section_anchor: full-file verifier and lane authority design
  content_hash: sha256:bc5d42a80b51a2479f417b1f5320713ce1c233b835352e45156609bd29f981a2
review_type: spec-review
pass_condition: no material finding in authority, identity, lane, evidence, selection, capability-profile, lifecycle, recovery, acceptance, or scope contracts
reject_condition: any material authority ambiguity, unverifiable evidence rule, unsafe fallback, non-deterministic selection, lifecycle conflict, or scope expansion remains
requires_human_judgment: true

# Reviewer Packet: Lifecycle Foundation Revision 2 Code Quality

schema_version: 2
source_dispatch_plan: docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/dispatch-plan.md
source_plan_revision: 2
source_section_id: section-lifecycle-foundation-implementation
source_dispatch_schema_version: 1
source_lifecycle_protocol: legacy
orchestrator_type: staff-engineer-orchestrator
stage: review
execution_id: exec-lifecycle-foundation-code-review-r2
packet_id: packet-lifecycle-foundation-code-review-r2e
attempt_id: attempt-lifecycle-foundation-code-review-r2e
supersedes_attempt_id: attempt-lifecycle-foundation-code-review-r2d
accepts_late_results: false
subagent_persona: code-quality-reviewer
persona_source: built-in
persona_rationale: inspect scaffold defaults, tests, backwards compatibility, and absence of accidental runtime activation; built-in fallback is used because no stronger eligible project reviewer covers Python scaffold quality
persona_binding:
  runtime_role: reviewer
  template_path: agents/reviewer-prompt.md
derived_from_working_brief: revision 2 integrates scaffold regression tests into the normal and JSON repository validation entrypoints while retaining deterministic legacy defaults
task_mode: review
workflow_bindings:
  - superpowers:requesting-code-review
  - superpowers:verification-before-completion
working_brief_excerpt: verify real CLI scaffold behavior, repo-suite integration, JSON aggregation, and completed-controller cleanup without expanding validator semantics
owned_scope: findings on revision 2 scaffold and repo-suite implementation quality only
read_scope:
  - path_glob: tools/scaffold_ww_case_artifacts.py
  - path_glob: tools/test_scaffold_ww_case_artifacts.py
  - path_glob: tools/validate_ww_repo.py
  - path_glob: docs/cases/task-runtime/rounds/2026-06-20-task-runtime-lifecycle-foundation-implementation/dispatch-plan.md
  - path_glob: README.md
write_scope: []
non_goals: do not edit files, add lifecycle validator semantics, add runtime activation code, or make the final human decision
success_criteria: identify at most five remaining material correctness, recursion, JSON-output, CI, controller-state, or regression-test findings; explicitly report no material findings when none exist
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
    focus: repo-suite composition, unittest recursion avoidance, aggregate JSON correctness, scaffold defaults, controller-state cleanup, and CI coverage
review_target_ref:
  artifact_path: tools/validate_ww_repo.py
  artifact_kind: python_tool
  artifact_revision: sha256:e946bd9ce25709aaa9645c42e3c1fb42e4cfd7a3e8007600ff1b063bd0d25236
  schema_version: 2
  section_anchor: full-file revision 2 repo validation entrypoint
  content_hash: sha256:e946bd9ce25709aaa9645c42e3c1fb42e4cfd7a3e8007600ff1b063bd0d25236
review_type: code-quality-review
pass_condition: no material correctness, CI coverage, JSON aggregation, recursion, or controller-state finding remains
reject_condition: any material unexecuted test, invalid JSON aggregation, recursive suite behavior, stale active pointer, or regression gap remains
requires_human_judgment: true

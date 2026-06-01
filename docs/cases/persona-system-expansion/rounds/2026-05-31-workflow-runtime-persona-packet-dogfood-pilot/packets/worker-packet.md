# Worker Packet: Runtime Persona Packet Dogfood Pilot

schema_version: 1
source_dispatch_plan: docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/dispatch-plan.md
source_plan_revision: 1
source_section_id: section-runtime-persona-packet-dogfood-pilot
orchestrator_type: staff-engineer-orchestrator
stage: implement
execution_id: exec-runtime-persona-packet-dogfood-worker-01
packet_id: packet-runtime-persona-packet-dogfood-worker-01
attempt_id: attempt-runtime-persona-packet-dogfood-worker-01
supersedes_attempt_id:
accepts_late_results: false
subagent_persona: technical-writer
persona_source: built-in
persona_rationale: the primary work is persisted packet evidence and a maintainer-facing dogfood report; built-in fallback is used because no stronger eligible project worker persona covers packet evidence documentation
persona_binding:
  runtime_role: worker
  template_path: agents/worker-prompt.md
implementation_principles:
  - prefer task-oriented documentation that helps the reader act correctly over exhaustive explanation
  - when tradeoffs are close, bias toward stable structure, clear source of truth, and maintainable wording
work_mode: conservative-first
work_mode_rationale: keep the pilot to one contract-complete worker packet, one read-only reviewer packet, and one evidence report
goal_tuning: validation-biased
constraint_precedence_note: packet constraints, explicit user limits, and non-goals take precedence over the conservative-first worker-mode posture
derived_from_working_brief: DG-004 requires one minimal real worker packet and one minimal real reviewer packet before a validator follow-up can be justified
task_mode: implement
workflow_bindings:
  - superpowers:writing-plans
  - superpowers:verification-before-completion
working_brief_excerpt: create the smallest contract-complete packet evidence pair and classify what the artifacts prove without widening scope
owned_scope: round-local packet dogfood evidence report only
read_scope:
  - path_glob: docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/dispatch-plan.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml
write_scope:
  - path_glob: docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md
non_goals: do not implement runtime code, edit packet contract, edit validators, add personas, change project registry, expand routing, add secondary tags, or make the final human decision
success_criteria: write an evidence-bound packet dogfood gap report that compares both packet artifacts against the approved dispatch snapshot and judges validator-round readiness without claiming runtime-code proof
output_contract: design-spec.md gap report with field-copy matrix, evidence classification, and validator-round readiness judgment
handoff_rule: return to orchestrator for spec-review packet assembly, findings synthesis, and human judgment
retry_policy: relaunch with new attempt_id after orchestrator decision
close_policy: close after reviewer handoff or explicit stop
result_artifact_location: docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/design-spec.md
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
    focus: round-local runtime persona packet dogfood evidence classification
requires_human_judgment: false

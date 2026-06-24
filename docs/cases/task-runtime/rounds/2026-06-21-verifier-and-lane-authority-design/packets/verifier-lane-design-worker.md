# Worker Packet: Verifier And Lane Authority Design Draft

schema_version: 2
source_dispatch_plan: docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/dispatch-plan.md
source_plan_revision: 1
source_section_id: section-verifier-lane-authority-design
source_dispatch_schema_version: 2
source_lifecycle_protocol: legacy
orchestrator_type: pm-orchestrator
stage: design
execution_id: exec-verifier-lane-design-worker-01
packet_id: packet-verifier-lane-design-worker-01
attempt_id: attempt-verifier-lane-design-worker-01
supersedes_attempt_id:
accepts_late_results: false
subagent_persona: senior-backend-engineer
persona_source: built-in
persona_rationale: durable runtime interfaces, identity records, command evidence, and model-resolution contracts make this the strongest eligible drafting persona; built-in fallback is used because no stronger eligible project worker persona covers portable WorkWork runtime architecture
persona_binding:
  runtime_role: worker
  template_path: agents/worker-prompt.md
implementation_principles:
  - prefer service-boundary correctness and data integrity over implementation speed
  - when tradeoffs are close, bias toward explicit interfaces and maintainable structure
work_mode: plan-first
work_mode_rationale: resolve coupled authority and schema decisions against approved foundations before drafting the normative artifact
goal_tuning: validation-biased
constraint_precedence_note: approved scope, explicit user exclusions, and non-goals take precedence over the plan-first posture
derived_from_working_brief: design verifier authority, identity isolation, verification lanes and evidence, baseline and risk-triggered selection, and model capability profiles without implementation or activation
task_mode: implement
workflow_bindings:
  - superpowers:brainstorming
  - superpowers:verification-before-completion
working_brief_excerpt: use one authority-first contract; preserve worker/reviewer/verifier/orchestrator/human separation; keep task-runtime-v1 dormant; defer bindings, personas, validators, hooks, repair, scoring, and activation
owned_scope: docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md
read_scope:
  - path_glob: docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md
  - path_glob: docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/agents/openai.yaml
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md
write_scope:
  - path_glob: docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md
non_goals: do not edit active contracts, templates, bindings, prompts, personas, project registry, validators, routing, hooks, repair, scoring, quality gates, runtime code, or activation state
success_criteria: produce one implementation-ready design with exact authority, identity, lane, evidence, selection, capability-profile, fallback, staleness, recovery-boundary, invalid-state, acceptance, and out-of-scope rules; contain no TODO or TBD placeholders
output_contract: replace design-spec.md with the complete design only; return a concise summary and any unresolved concern
handoff_rule: return to pm-orchestrator, then freeze the artifact for independent spec and authority-isolation reviews
retry_policy: relaunch only through orchestrator decision with a new packet and attempt when the target revision changes
close_policy: close after the design is persisted and handed to required reviewer lanes
result_artifact_location: docs/cases/task-runtime/rounds/2026-06-21-verifier-and-lane-authority-design/design-spec.md
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
    focus: authority-first verifier and lane design with exact evidence and capability-profile contracts
requires_human_judgment: false

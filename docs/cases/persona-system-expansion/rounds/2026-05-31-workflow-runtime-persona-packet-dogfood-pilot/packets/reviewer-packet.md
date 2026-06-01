# Reviewer Packet: Runtime Persona Packet Dogfood Pilot

schema_version: 1
source_dispatch_plan: docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/dispatch-plan.md
source_plan_revision: 1
source_section_id: section-runtime-persona-packet-dogfood-pilot
orchestrator_type: staff-engineer-orchestrator
stage: review
execution_id: exec-runtime-persona-packet-dogfood-reviewer-01
packet_id: packet-runtime-persona-packet-dogfood-reviewer-01
attempt_id: attempt-runtime-persona-packet-dogfood-reviewer-01
supersedes_attempt_id:
accepts_late_results: false
subagent_persona: spec-reviewer
persona_source: built-in
persona_rationale: packet contract fidelity, immutable review targeting, and evidence classification make the built-in spec reviewer the strongest eligible reviewer-only match; built-in fallback is used because no stronger eligible project reviewer covers packet contract fidelity
persona_binding:
  runtime_role: reviewer
  template_path: agents/reviewer-prompt.md
derived_from_working_brief: review the stable worker packet and final evidence classification for approved-dispatch derivation, persona provenance copying, ordered worker principles, and scope authority
task_mode: review
workflow_bindings:
  - superpowers:requesting-code-review
  - superpowers:verification-before-completion
working_brief_excerpt: inspect one immutable worker packet snapshot and classify only evidence supported by the persisted artifact pair
owned_scope: findings on worker packet contract fidelity and packet dogfood evidence boundaries only
read_scope:
  - path_glob: docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/dispatch-plan.md
  - path_glob: docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md
  - path_glob: plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml
write_scope: []
non_goals: do not rewrite files, implement runtime code, edit packet contract, edit validators, add personas, change project registry, expand routing, add secondary tags, or make the final human decision
success_criteria: identify any approved-dispatch copy drift, worker principle drift, reviewer authority leakage, or evidence overclaim before orchestrator synthesis
output_contract: findings only
handoff_rule: return to orchestrator, then human judgment required
retry_policy: relaunch only through orchestrator decision
close_policy: close after synthesis and recorded decision
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
    focus: approved-dispatch persona field copying and packet evidence boundaries
review_target_ref:
  artifact_path: docs/cases/persona-system-expansion/rounds/2026-05-31-workflow-runtime-persona-packet-dogfood-pilot/packets/worker-packet.md
  artifact_kind: worker_packet
  artifact_revision: sha256:537c6b31ffc0b288a7aef7c81a2c5ed5ba8994ddafec46519fe1f3c6d0a35bac
  schema_version: 1
  section_anchor: full-file worker packet evidence
  content_hash: sha256:537c6b31ffc0b288a7aef7c81a2c5ed5ba8994ddafec46519fe1f3c6d0a35bac
review_type: spec-review
pass_condition: worker packet fields match the approved dispatch snapshot, worker principles remain canonical and ordered, reviewer packet authority remains read-only, and conclusions stay evidence-bound
reject_condition: any approved persona field is missing or drifted, worker principles differ from the persona record, reviewer write authority leaks, or artifact evidence is presented as runtime-code proof
requires_human_judgment: true

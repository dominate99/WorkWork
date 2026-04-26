# Subagent Packet Contract

Create a packet only after:

- `estimation_complete: true`
- `working_brief_ready: true`
- `dispatch_decision: approved`

## Required Fields

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

- `workflow_bindings[]` may contain more than one Superpowers skill when a stage legitimately requires it.
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
orchestrator_type: staff engineer orchestrator
stage: review
subagent_persona: secure software engineer
persona_rationale: working brief identifies elevated auth security risk
derived_from_working_brief: backend auth path, release-sensitive, security-critical
task_mode: review
workflow_bindings:
- superpowers:requesting-code-review
- superpowers:verification-before-completion
owned_scope: authentication changes in backend service
non_goals: do not rewrite code, do not approve release, do not make final decisions
success_criteria: identify security-relevant findings with severity and rationale
output_contract: findings only
handoff_rule: return to orchestrator, then human judgment required
requires_human_judgment: true
```

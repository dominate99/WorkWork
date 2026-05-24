# Reviewer And Explorer Contract Validator Design

Date: 2026-05-18
Status: Approved for `$ww` implementation
Scope: Repo-local validator for `reviewer` and `explorer` runtime-role contracts in `ww-subagent-orchestrator`

## Goal

Add a repo-local automated validator that checks whether `reviewer` and `explorer` still obey their role contracts.

The first version should:

- validate `reviewer` and `explorer` as role contracts, not as `work_mode` contracts
- reuse the current repo-local validator pattern instead of introducing a separate framework
- stay section-aware for Markdown contract checks
- fail with a non-zero exit code on any rule violation
- integrate into `tools/validate_ww_repo.py`

## Scope

This validator should check these core contract files:

- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md`

This round should not yet validate:

- persona quality or persona selection correctness
- project persona registry contents
- live dispatch-plan instance files
- output quality of actual reviewer or explorer runs

## Design Model

This validator protects the distinction between three layers:

1. `persona`
   - provides professional viewpoint
   - does not replace role behavior
2. `runtime_role`
   - determines whether the packet is a `reviewer` or `explorer`
3. `role prompt`
   - determines what that role may and may not do

The validator should enforce that `persona`, `runtime_role`, and `template_path` stay aligned.

## Reviewer Contract Rules

### `SKILL.md`

Must structurally declare:

- reviewer subagents point out problems only
- reviewer subagents stay narrow and convergent
- reviewers and implementers remain separate
- reviewer coverage, orchestrator synthesis, and human judgment are all required

### `subagent-packet-contract.md`

Must structurally declare:

- reviewer packets require:
  - `review_target_ref`
  - `review_type`
  - `pass_condition`
  - `reject_condition`
- reviewer defaults include:
  - `task_mode: review`
  - `agent_type: default`
  - `output_contract: findings only`
  - `handoff_rule: return to orchestrator, then human judgment required`
  - `requires_human_judgment: true`
  - `write_scope: []`
- reviewer packet example includes:
  - `persona_binding.runtime_role: reviewer`
  - `template_path: agents/reviewer-prompt.md`
  - `non_goals` that block rewrite, approval, and scope growth

### `reviewer-prompt.md`

Must structurally declare:

- inspect only the assigned target
- identify findings only
- do not rewrite the artifact
- do not propose new scope
- do not approve the section
- do not widen the review surface
- explicit `no material findings` output path

## Explorer Contract Rules

### `SKILL.md`

Must structurally declare:

- `explorer` is a read-only prompt role for investigation and scoped evidence gathering
- role prompts are behavioral templates, not persona registry records

### `subagent-packet-contract.md`

Must structurally declare:

- explorer defaults include:
  - `task_mode: investigate`
  - `agent_type: explorer`
  - `write_scope: []`
  - `requires_human_judgment: false`
  - `retry_policy: relaunch only through orchestrator decision`
  - `close_policy: close after findings are handed back`

### `explorer-prompt.md`

Must structurally declare:

- gather evidence for a narrow question
- summarize concrete observations only
- preserve scope boundaries and read-only behavior
- do not write files
- do not rewrite deliverables
- do not decide on behalf of the orchestrator
- output concise evidence notes plus a direct answer

## Alignment Rules

The validator should also catch role-binding drift:

- reviewer packet bindings must not point at `worker-prompt.md`
- explorer packet bindings must not point at `reviewer-prompt.md`
- `runtime_role` values must stay aligned with the matching prompt asset
- `reviewer` and `explorer` must not gain `work_mode` fields or worker-only `implementation_principles` requirements through schema drift

## Tool Shape

Recommended path:

- `tools/validate_ww_role_contracts.py`

Recommended integration:

- call it from `tools/validate_ww_repo.py` after the current worker validator

## Output Contract

Follow the current validator pattern:

- human-readable output by default
- optional machine-readable output later
- stable rule ids split by role family

Suggested prefixes:

- `WWRV` for reviewer rules
- `WWEX` for explorer rules
- `WWRL` for cross-role alignment rules

## Verification Plan

Implementation is complete only if:

- the validator fails when reviewer rewrite/approval prohibitions are removed
- the validator fails when explorer read-only rules are removed
- the validator fails when packet role defaults drift away from the prompt roles
- `tools/validate_ww_repo.py` runs the new validator in the same repo-local validation flow

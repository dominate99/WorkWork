# Working Brief: Reviewer And Explorer Contract Validator

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: reviewer-explorer-contract-validator
- `created_at`: 2026-05-18
- `updated_at`: 2026-05-18
- `derived_from_user_request`: `把 reviewer / explorer contract validator 变成一个 $ww workflow`

## Round Intent

- `quality_mode`: standard

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff-engineer-orchestrator`

## Core Intent

- `goal`: add a repo-local validator that checks reviewer and explorer runtime-role contracts and integrates into the existing WW repository validation entrypoint
- `artifact_type`: Python validator plus repo-local validation integration and supporting planning artifacts
- `relevant_context`:
  - the repository already has `tools/quick_validate.py`, `tools/validate_ww_worker_work_mode.py`, and `tools/validate_ww_repo.py`
  - reviewer and explorer currently use persona plus role-prompt composition, not worker-style `work_mode`
  - `reviewer` contract lives mainly across `SKILL.md`, `subagent-packet-contract.md`, and `agents/reviewer-prompt.md`
  - `explorer` contract lives mainly across `SKILL.md`, `subagent-packet-contract.md`, and `agents/explorer-prompt.md`
  - there is already a reviewer packet example, but no explorer packet example yet
- `constraints`:
  - do not invent `mode` semantics for reviewer or explorer
  - first version should validate role contracts, not persona quality
  - reuse the repo-local validator pattern and unified entrypoint
  - keep scope bounded to repo-local validation logic and related contract surfaces

## Risk And Structure

- `risk_lenses`:
  - reviewer or explorer may accidentally inherit worker-only fields through contract drift
  - prompt and packet role bindings may diverge silently if not checked together
  - a too-broad validator could collapse role-specific checks into vague generic text matching
  - explorer currently has less example coverage than reviewer, so the first version must be careful about what it treats as required
- `parallelism_assessment`:
  - this round is small but tightly coupled around one validator and one repo-level integration point
  - a single implementation lane is preferable to parallel edits because the rule set and repo entrypoint must agree
- `blocking_dependencies`:
  - the design and implementation plan should be persisted before implementation
  - the validator rule scope must be fixed before `validate_ww_repo.py` is updated
- `section_or_workstream_map`:
  - section 1: implement reviewer and explorer contract validation
  - section 2: integrate the new validator into repo-level validation and verify the result

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `role_contract_design_spec`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/specs/2026-05-18-reviewer-explorer-contract-validator-design.md`
  - `section_anchors`: `Reviewer Contract Rules`, `Explorer Contract Rules`, `Alignment Rules`
  - `artifact_id`: `role_contract_impl_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/plans/2026-05-18-reviewer-explorer-contract-validator.md`
  - `section_anchors`: none
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Core Rules`, `Persona Planning`, `Subagent Packet Contract`
  - `artifact_id`: `subagent_packet_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `section_anchors`: `Reviewer Packet Defaults`, `Explorer Packet Defaults`, `Reviewer Packet Example`
  - `artifact_id`: `reviewer_prompt`
  - `artifact_kind`: `prompt`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md`
  - `section_anchors`: `Responsibilities`, `Operating rules`
  - `artifact_id`: `explorer_prompt`
  - `artifact_kind`: `prompt`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md`
  - `section_anchors`: `Responsibilities`, `Operating rules`
  - `artifact_id`: `repo_validator_entrypoint`
  - `artifact_kind`: `code`
  - `artifact_path`: `tools/validate_ww_repo.py`
  - `section_anchors`: none
- `exclusive_write_scope`:
  - `path_glob`: `docs/superpowers/specs/2026-05-18-reviewer-explorer-contract-validator-design.md`
  - `path_glob`: `docs/superpowers/plans/2026-05-18-reviewer-explorer-contract-validator.md`
  - `path_glob`: `docs/superpowers/working-briefs/2026-05-18-reviewer-explorer-contract-validator-v1.md`
  - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-18-reviewer-explorer-contract-validator.md`
  - `path_glob`: `tools/validate_ww_role_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/reviewer-prompt.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/explorer-prompt.md`
  - `path_glob`: `tools/quick_validate.py`
  - `path_glob`: `tools/validate_ww_worker_work_mode.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `senior-backend-engineer`
  - `secure-software-engineer`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the primary artifact is a bounded validator plus repo-level validation integration
  - `senior-backend-engineer` is the best worker-capable specialist for a correctness-heavy Python validator change
  - `secure-software-engineer` is still a strong reviewer persona because reviewer/explorer contract drift is mostly about guardrails and unsafe scope broadening
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1 extends an existing validation system and should confirm the approved contract set before implementation
  - section 2 modifies the repo entrypoint and should verify integration behavior before broadening scope
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not recast reviewer or explorer as worker-style mode roles
  - section 2: do not expand into persona quality scoring or registry validation in this round
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - code changes: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded implementation lane for reviewer/explorer role-contract validation
  - require repo-level validation to stay on one unified entrypoint
  - treat explorer example coverage as optional for the first implementation unless a new contract example is explicitly added

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-role-contract-validator: true
- `review_target_strategy`:
  - review role-boundary enforcement first
  - review repo-level validator integration second
  - treat any reviewer/explorer drift into write authority or worker-only semantics as blocking
- `controller_semantics_notes`:
  - no packet creation until the referenced dispatch plan is in `approved` state
  - persona remains a viewpoint layer; role prompts remain behavioral templates

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.

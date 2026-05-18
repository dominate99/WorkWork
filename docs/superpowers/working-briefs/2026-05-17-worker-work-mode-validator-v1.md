# Working Brief: Worker Work-Mode Validator

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: worker-work-mode-validator
- `created_at`: 2026-05-17
- `updated_at`: 2026-05-17
- `derived_from_user_request`: `$ww 帮你把这个验证脚本也设计并加进去`

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

- `goal`: add a repo-local Python validator that structurally checks the `ww-subagent-orchestrator` worker `work_mode` contract across the five approved Markdown contract surfaces
- `artifact_type`: Python validator plus maintainer-facing documentation and dispatch artifacts
- `relevant_context`:
  - the worker `work_mode` contract has just been added across five packaged skill surfaces
  - the repo currently has no local validator script, no `tools/` directory, and no local Python project metadata
  - the approved validator design chooses Python plus a Markdown AST parser, human-readable output by default, `--json` for machine-readable output, and a fixed file list
  - the current Python runtime does not have `markdown_it` installed, so dependency provisioning is part of this round
  - `README.md` mentions an external `quick_validate.py`, but the repo does not currently expose a local validator for the new worker `work_mode` contract
- `constraints`:
  - first version validates only the worker `work_mode` contract surface
  - first version uses a fixed built-in file list, not external config discovery
  - validation must be section-aware, not whole-file text matching
  - any rule failure must return a non-zero exit code
  - docs must match the actual validator command and dependency path

## Risk And Structure

- `risk_lenses`:
  - a plain-text validator would produce false positives by matching the wrong section
  - a missing or undocumented dependency path would make the tool unusable for maintainers
  - if the machine-readable schema is unstable, the tool will be hard to adopt in CI later
  - if docs drift away from the real command path, the validator will add confusion instead of confidence
- `parallelism_assessment`:
  - this is a small but tightly coupled tool-and-doc round
  - one bounded implementation lane is safer than parallel edits because the script, dependency path, and docs must agree
- `blocking_dependencies`:
  - the approved design and implementation plan must be persisted before implementation
  - the Markdown AST dependency path must be decided before the script logic is finalized
  - maintainer docs should be written after the command path and dependency behavior are real
- `section_or_workstream_map`:
  - section 1: add the repo-local validator and dependency handling
  - section 2: add matching maintainer docs and run validation in both output modes

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `validator_design_spec`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/specs/2026-05-17-worker-work-mode-validator-design.md`
  - `section_anchors`: `Validation Model`, `First Rule Set`
  - `artifact_id`: `validator_impl_plan`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/superpowers/plans/2026-05-17-worker-work-mode-validator.md`
  - `section_anchors`: none
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Core Rules`, `Working Brief`, `Subagent Packet Contract`, `Dispatch Plan File`
  - `artifact_id`: `working_brief_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `section_anchors`: `Persona And Workflow Guidance`, `Rules`
  - `artifact_id`: `dispatch_plan_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `section_anchors`: `Planned Sections`, `Section Runtime Ledger`
  - `artifact_id`: `subagent_packet_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `section_anchors`: `Worker packets additionally require`, `Packet Rules`, `Worker Packet Example`
  - `artifact_id`: `worker_prompt`
  - `artifact_kind`: `prompt`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
  - `section_anchors`: `Responsibilities`, `Operating rules`
  - `artifact_id`: `repo_readme`
  - `artifact_kind`: `doc`
  - `artifact_path`: `README.md`
  - `section_anchors`: `For Maintainers`
- `exclusive_write_scope`:
  - `path_glob`: `docs/superpowers/specs/2026-05-17-worker-work-mode-validator-design.md`
  - `path_glob`: `docs/superpowers/plans/2026-05-17-worker-work-mode-validator.md`
  - `path_glob`: `docs/superpowers/working-briefs/2026-05-17-worker-work-mode-validator-v1.md`
  - `path_glob`: `docs/superpowers/dispatch-plans/2026-05-17-worker-work-mode-validator.md`
  - `path_glob`: `tools/validate_ww_worker_work_mode.py`
  - `path_glob`: `README.md`
- `shared_read_scope`:
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/agents/worker-prompt.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `senior-backend-engineer`
  - `secure-software-engineer`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the primary artifact is a bounded repo-local validation tool plus matching documentation
  - `senior-backend-engineer` is the best worker-capable built-in specialist because the tool work is correctness- and structure-heavy
  - `secure-software-engineer` is a useful reviewer persona for checking failure behavior, bounded scope, and contract drift
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `validate-first`
- `worker_mode_reasoning_by_section`:
  - section 1 adds a validator to protect an existing contract surface, so it should confirm the approved rule set before implementation
  - section 2 is a review and verification step, so validation posture should dominate over speed
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: do not widen the first validator into a generic repo-wide skill validator
  - section 2: keep docs aligned to the real dependency and command path instead of speculative future packaging
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - code changes: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded implementation lane for the validator tool and matching docs
  - require verification in both default and `--json` modes
  - keep the round standard `$ww`

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-worker-work-mode-validator: true
- `review_target_strategy`:
  - review the validator script and docs together
  - prioritize section-aware structural validation and clear failure behavior
  - treat missing dependency handling or unstable JSON output as blocking defects
- `controller_semantics_notes`:
  - no packet creation until the referenced dispatch plan is in `approved` state
  - if dependency provisioning changes the install path or invocation path, update the docs in the same round

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.

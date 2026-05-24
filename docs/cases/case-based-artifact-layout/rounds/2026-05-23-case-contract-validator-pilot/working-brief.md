# Working Brief: Case Contract Validator Pilot

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: case-contract-validator-pilot
- `case_slug`: case-based-artifact-layout
- `round_slug`: 2026-05-23-case-contract-validator-pilot
- `case_root`: `docs/cases/case-based-artifact-layout/`
- `round_root`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-contract-validator-pilot/`
- `created_at`: 2026-05-23
- `updated_at`: 2026-05-24
- `derived_from_user_request`: `case contract validator pilot`

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

- `goal`: add a repo-local validator that turns the case/round artifact structure into a machine-checkable contract
- `artifact_type`: validator and documentation round
- `relevant_context`:
  - active WW artifacts now live under `docs/cases/<case-slug>/rounds/<round-slug>/`
  - `case.md` is already functioning as the case entrypoint in practice
  - there is not yet a dedicated formal `case.md` template surface comparable to the working brief and dispatch plan templates
  - the new scaffolding helper can generate `case.md`, `working-brief.md`, and `dispatch-plan.md`
  - the remaining gap is that these structures are still enforced mostly by convention rather than validator rules
- `constraints`:
  - keep the validator focused on case/round artifact structure
  - include a formal `case.md` template in scope, not just validator rules
  - do not redesign runtime packet or prompt contracts
  - keep the active root under `docs/cases/...`
  - prefer explicit hard rules over softer style guidance

## Risk And Structure

- `risk_lenses`:
  - a weak validator could create false confidence while still leaving structural ambiguity
  - over-expanding the validator could pull it into content-quality judgment instead of structure validation
  - if `case.md` rules are underspecified, helper output and human-created cases could drift again
  - without a dedicated template, `case.md` rules could end up living only in validator code
- `parallelism_assessment`:
  - validator design, helper expectations, and repo entrypoint wiring are tightly coupled
  - one bounded implementation lane is better than parallel sub-lanes
- `blocking_dependencies`:
  - the completed case-based artifact generation pilot
  - the completed legacy archival and normalization rounds
  - the completed case artifact scaffolding pilot
- `section_or_workstream_map`:
  - section 1: define the case contract rules
  - section 2: implement the validator and repo entrypoint wiring

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `ww_skill_contract`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `section_anchors`: `Working Brief persistence rules`, `Default document references`
  - `artifact_id`: `ww_readme`
  - `artifact_kind`: `doc`
  - `artifact_path`: `README.md`
  - `section_anchors`: `What It Does`, `For Maintainers`
  - `artifact_id`: `brief_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
  - `section_anchors`: `Artifact Metadata`, `Artifact-layout rules`
  - `artifact_id`: `dispatch_template`
  - `artifact_kind`: `doc`
  - `artifact_path`: `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
  - `section_anchors`: `Path identity rules`, `Default document references`
  - `artifact_id`: `case_entrypoint`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/cases/case-based-artifact-layout/case.md`
  - `section_anchors`: `Round Index`, `Notes`
- `exclusive_write_scope`:
  - `path_glob`: `docs/cases/case-based-artifact-layout/rounds/2026-05-23-case-contract-validator-pilot/**/*`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
  - `path_glob`: `README.md`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - `path_glob`: `tools/validate_ww_case_contracts.py`
  - `path_glob`: `tools/validate_ww_repo.py`
- `shared_read_scope`:
  - `path_glob`: `docs/cases/**/*`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
  - `path_glob`: `tools/*.py`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff-engineer-orchestrator`
  - `pm-orchestrator`
- `persona_selection_notes`:
  - `staff-engineer-orchestrator` fits because the goal is to turn a loose structure into an explicit machine-checked contract
  - `pm-orchestrator` is a useful reviewer lens because the rules should still be understandable to maintainers
- `recommended_worker_mode_by_section`:
  - section 1: `validate-first`
  - section 2: `conservative-first`
- `worker_mode_reasoning_by_section`:
  - section 1 should define exactly which structural rules are hard requirements
  - section 2 should add the smallest validator slice that locks those rules down
- `goal_tuning_by_section`:
  - section 1: `validation-biased`
  - section 2: `safety-biased`
- `constraint_override_notes_by_section`:
  - section 1: distinguish structure rules from content-quality rules
  - section 2: keep helper validation focused on output structure rather than semantic completeness
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded validator implementation lane
  - introduce a dedicated `case.md` template surface so field minimums are explicit rather than inferred
  - harden `case.md` presence and field minimums
  - harden minimum round files
  - verify helper output against the same contract

## Runtime Preparation

- `required_for_goal_by_section`:
  - section-case-contract-validator-pilot: true
- `review_target_strategy`:
  - validate that every case must have a `case.md`
  - validate that `case.md` field minimums come from a formal template, not only from validator heuristics
  - validate that `case.md` carries a minimal required field set
  - validate that every round has `working-brief.md` and `dispatch-plan.md`
  - validate that helper-generated output satisfies the same rules
- `controller_semantics_notes`:
  - this round should not change runtime packet semantics
  - the validator should judge structure, not planning quality
  - if helper and validator expectations disagree, the template-backed contract must win

## Rules

- Recommended personas are provisional until dispatch approval.
- Case contract rules must be structural and machine-checkable.
- `case.md` is expected to be a required case entrypoint, not just an informal convention.
- `case.md` should have a dedicated template surface so required fields are documented in one place.
- `working-brief.md` and `dispatch-plan.md` are expected to be the minimum required round artifacts.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.

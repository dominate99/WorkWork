# Working Brief: WW Orchestrator Implementation

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: ww-orchestrator-implementation
- `created_at`: 2026-05-06
- `updated_at`: 2026-05-06
- `derived_from_user_request`: `$ww based on implementation plan start the implementation`

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff engineer orchestrator`

## Core Intent

- `goal`: implement the approved orchestration design into the `ww-subagent-orchestrator` skill artifacts without semantic drift between `SKILL.md`, templates, packet contract, persona bindings, and runtime policies
- `artifact_type`: codex skill runtime policy and template implementation
- `relevant_context`:
  - source plan: `2026-05-06-implementation-plan.md`
  - target root: `C:\Users\domin\.codex\skills\ww-subagent-orchestrator`
  - current skill already has `SKILL.md`, `references/`, `assets/`, and `agents/openai.yaml`
  - implementation plan now defines controller semantics, working brief persistence, packet identity, artifact registry schema, review-target immutability, and round-level aggregation rules
- `constraints`:
  - treat the implementation plan as the binding source of truth for this round
  - no real subagent launch before dispatch approval
  - preserve reviewer/implementer separation
  - avoid parallel edits across overlapping runtime-contract files
  - use persisted working brief and dispatch plan artifacts for this round

## Risk And Structure

- `risk_lenses`:
  - runtime state drift between `runtime_state`, review flow, and round-level `plan_state`
  - packet contract drift against controller update procedure
  - template drift against implementation plan semantics
  - persona layer becoming decorative if prompt assembly is not wired into packet fields
  - dispatch plan shape lagging behind execution-history requirements
- `parallelism_assessment`:
  - partial parallelism is possible only after the core contract layer stabilizes
  - first implementation slice should be serial because `SKILL.md`, packet contract, and dispatch-plan template share controller semantics
  - persona prompt assets can follow after contract fields are in place
- `blocking_dependencies`:
  - section 1 must land before section 2 because persona prompt assembly depends on final packet field names
  - section 2 should land before section 3 because validation needs the full artifact surface
- `section_or_workstream_map`:
  - section 1: core runtime contracts and templates
  - section 2: persona/runtime prompt binding assets
  - section 3: validation examples and consistency pass

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff engineer orchestrator`
  - `codex skill contract implementer`
  - `runtime policy reviewer`
  - `skill prompt systems reviewer`
- `persona_selection_notes`:
  - `staff engineer orchestrator` is selected because the primary artifact is a programming-oriented skill contract with state-machine and template coupling
  - `codex skill contract implementer` owns schema-aligned updates to `SKILL.md`, `references/`, and `assets/`
  - `runtime policy reviewer` should inspect controller-state and review-flow consistency only
  - `skill prompt systems reviewer` should inspect persona binding and prompt-assembly semantics only
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - code/document changes: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one serial implementation round with three sections
  - do not dispatch parallel workers into overlapping contract files
  - require reviewer findings after each section before moving forward

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.

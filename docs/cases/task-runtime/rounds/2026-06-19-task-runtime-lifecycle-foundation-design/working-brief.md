# Working Brief: Task Runtime Lifecycle Foundation Design

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: task-runtime-lifecycle-foundation-design
- `case_slug`: task-runtime
- `round_slug`: 2026-06-19-task-runtime-lifecycle-foundation-design
- `case_root`: `docs/cases/task-runtime/`
- `round_root`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/`
- `created_at`: 2026-06-19
- `updated_at`: 2026-06-19
- `derived_from_user_request`: `$ww round: Task runtime lifecycle foundation design.`

## Round Intent

- `quality_mode`: standard

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `design/ads/product`
- `orchestrator_choice`: `pm-orchestrator`

## Core Intent

- `goal`: define the implementation-ready lifecycle foundation for an invocation-scoped WorkWork task runtime, including canonical section phase ownership, its orthogonal relationship to existing runtime state, deterministic transitions, orchestrator authority, derived round rollups, and append-only lifecycle events.
- `artifact_type`: lifecycle foundation design spec
- `relevant_context`:
  - approved umbrella design: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`
  - current WorkWork contract already treats per-section `runtime_state` as canonical execution state and derives round `plan_state`
  - current dispatch plans persist section runtime ledgers, execution identities, review target identities, and approval history
  - this is rollout step 1 of 10 and must leave later authority surfaces for their dedicated rounds
- `constraints`:
  - design only; do not implement lifecycle fields in active contracts or templates
  - do not add verifier personas, verifier runtime bindings, lane mappings, hooks, scoring, or quality gates
  - do not change validators or packet contracts
  - do not create an implementation plan in this round
  - preserve `runtime_state` as the canonical execution-state surface rather than replacing it
  - avoid a round-level phase authority that competes with section phase ownership

## Risk And Structure

- `risk_lenses`:
  - dual authority between `lifecycle_phase` and `runtime_state`
  - invalid or underspecified phase/state combinations
  - event history disagreeing with the current snapshot
  - round rollups becoming a second writable phase machine
  - migration ambiguity for pre-foundation artifacts
  - later verifier, hook, and quality rounds being constrained by accidental premature detail
- `parallelism_assessment`:
  - low; state vocabulary, transition rules, authority, event schema, and recovery invariants depend on one another and should be designed serially
- `blocking_dependencies`:
  - approved umbrella design decisions on section-owned `lifecycle_phase`, orchestrator-only phase transitions, derived round rollups, and snapshot-plus-events persistence
- `section_or_workstream_map`:
  - section `LIFECYCLE-DESIGN-001`: produce and review one lifecycle foundation design spec

## Scope Preparation

- `artifact_mappings`:
  - `TASK_RUNTIME_UMBRELLA_DESIGN`:
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/superpowers/specs/2026-06-19-workwork-task-runtime-design.md`
    - `section_anchors`: `Canonical State Model`, `Lifecycle Flow`, `Authority Model`, `Persistence Model`, `Recovery`
  - `LIFECYCLE_FOUNDATION_SPEC`:
    - `artifact_kind`: design_spec
    - `artifact_path`: `docs/cases/task-runtime/rounds/2026-06-19-task-runtime-lifecycle-foundation-design/design-spec.md`
    - `section_anchors`: `State Ownership`, `Phase Vocabulary`, `Transition Model`, `Lifecycle Event Schema`, `Rollup And Recovery`, `Acceptance Criteria`
- `exclusive_write_scope`:
  - `artifact_id`: `LIFECYCLE_FOUNDATION_SPEC`
- `shared_read_scope`:
  - `artifact_id`: `TASK_RUNTIME_UMBRELLA_DESIGN`
  - `path_glob`: `plugins/workwork/skills/ww-subagent-orchestrator/**/*`
  - `path_glob`: `tools/validate_ww_*.py`
  - `path_glob`: `docs/cases/**/dispatch-plan.md`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `candidate_persona_sources`:
  - project registry checked: true
  - built-in fallback checked: true
  - project registry outcome: project `pm-orchestrator` is the strongest eligible orchestrator for a product/runtime contract design
  - built-in fallback outcome: no project worker or reviewer covers lifecycle-spec production and contract review; use built-in `technical-writer` and `spec-reviewer`
  - fallback rationale: built-in personas provide the required worker capability and reviewer-only authority without inventing new personas in this design round
- `recommended_personas`:
  - persona id: `pm-orchestrator`
    - runtime role: orchestrator
    - source: project
    - owned scope: round framing, authority-boundary synthesis, and human gates
    - fit rationale: the primary artifact is a product/runtime design with substantial scope and tradeoff decisions
    - role binding: `orchestrator` from `agents/openai.yaml`
    - prompt asset: `agents/orchestrator-prompt.md`
    - workflow bindings: `superpowers:brainstorming`, `superpowers:writing-plans`
  - persona id: `technical-writer`
    - runtime role: worker
    - source: built-in
    - owned scope: `LIFECYCLE_FOUNDATION_SPEC`
    - fit rationale: the section produces a durable, implementation-ready technical contract and the persona satisfies the worker-capability gate
    - fallback rationale: no eligible project documentation or specification worker is stronger
    - role binding: `worker` from `agents/openai.yaml`
    - prompt asset: `agents/worker-prompt.md`
    - workflow bindings: `superpowers:writing-plans`, `superpowers:verification-before-completion`
  - persona id: `spec-reviewer`
    - runtime role: reviewer
    - source: built-in
    - review target: `LIFECYCLE_FOUNDATION_SPEC`
    - fit rationale: the artifact requires coherent authority, transition, compatibility, and acceptance contracts; the persona passes the reviewer-only gate
    - fallback rationale: no eligible project reviewer covers specification contract fidelity
    - role binding: `reviewer` from `agents/openai.yaml`
    - prompt asset: `agents/reviewer-prompt.md`
    - workflow bindings: `superpowers:requesting-code-review`
- `persona_selection_notes`:
  - persona choice follows artifact type and authority risks rather than task keywords
  - worker and reviewer remain separate; reviewer has no write authority
- `recommended_worker_mode_by_section`:
  - `LIFECYCLE-DESIGN-001`: plan-first
- `worker_mode_reasoning_by_section`:
  - `LIFECYCLE-DESIGN-001`: the design must reconcile existing state contracts and umbrella decisions before drafting transition details
- `goal_tuning_by_section`:
  - `LIFECYCLE-DESIGN-001`: prefer explicit invariants, tables, and invalid-state rules over broad architecture prose
- `constraint_override_notes_by_section`:
  - `LIFECYCLE-DESIGN-001`: design depth must not spill into active contract edits, verifier authority, hooks, quality scoring, or validator implementation
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning and drafting: `superpowers:writing-plans`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one serial design section followed by a narrow specification review and human judgment

## Grill-Me Decision Log

- No entries. `grill-me` was not explicitly activated for this round.

## Runtime Preparation

- `required_for_goal_by_section`:
  - `LIFECYCLE-DESIGN-001`: true
- `review_target_strategy`:
  - review the stable round-local design spec revision against the umbrella design, current runtime-state ownership, and this brief's non-goals
- `controller_semantics_notes`:
  - standard `$ww` round; no strict-review target
  - no packet may be created until plan revision 1 is approved
  - design completion requires reviewer findings, orchestrator synthesis, and human judgment

## Rules

- The working brief is ready for dispatch-plan approval.
- The working brief recommends worker mode but does not own execution authority.
- No packet creation until the referenced dispatch plan is in `approved` state.

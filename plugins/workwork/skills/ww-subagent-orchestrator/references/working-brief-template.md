# Working Brief Template

Use this template after estimation and before any persona dispatch.

## Artifact Metadata

- `schema_version`
- `brief_version`
- `brief_status`
- `topic_slug`
- `case_slug`
- `round_slug`
- `case_root`
- `round_root`
- `created_at`
- `updated_at`
- `derived_from_user_request`

## Round Intent

- `quality_mode: standard | strict`

## Gate State

- `estimation_complete: true|false`
- `brief_status: draft|ready`
- `brief_version`

## Routing

- `task_routing`: `code/programming` | `design/ads/product` | `video/creative`
- `orchestrator_choice`

## Core Intent

- `goal`
- `artifact_type`
- `relevant_context`
- `constraints`

## Risk And Structure

- `risk_lenses`
- `parallelism_assessment`
- `blocking_dependencies`
- `section_or_workstream_map`

## Scope Preparation

- `artifact_mappings`
- `exclusive_write_scope`
- `shared_read_scope`
- `depends_on_sections`
- `parallel_safe_with_sections`

Required inline artifact-mapping fields when registry fallback is used:

- `artifact_id`
- `artifact_kind`
- `artifact_path`
- `section_anchors` when `doc_section` will be referenced

Rules:

- resolve `artifact_id` through `docs/superpowers/artifact-registry.yaml` when available
- if the registry is absent, define inline artifact mappings before dispatch
- aggregate multi-file work must not hide behind a single multi-path `artifact_id`
- canonical scope grammar:
  - `path_glob`
  - `doc_section`
  - `artifact_id`
- `doc_section` resolves to `artifact_path + section_anchor`
- one `artifact_id` resolves to exactly one canonical `artifact_path`
- non-file-centric fallback still requires a persisted `artifact_path`; `section_anchor` is optional, but a bare conceptual scope cannot be marked parallel-safe or used for reviewer targeting
- collision rules:
  - write/write overlap blocks parallel worker dispatch
  - write/read overlap is allowed only for reviewer or explorer lanes that are read-only
  - cross-type collisions are checked after normalization, not by original label
- `doc_section` overlapping a file matched by a `path_glob` is a collision unless the packet is read-only

Artifact-layout rules:

- `case_slug` identifies the long-lived workstream for this round
- `round_slug` identifies this bounded `$ww` or `$www` cycle inside that case
- `case_root` must resolve to `docs/cases/<case_slug>/`
- `round_root` must resolve to `docs/cases/<case_slug>/rounds/<round_slug>/`
- new rounds write their canonical artifacts under `round_root`; pre-cutover type-based artifacts are legacy history only and must not be treated as active generation targets

## Persona And Workflow Guidance

- `candidate_persona_sources`
- `recommended_personas`
- `persona_selection_notes`
- `recommended_worker_mode_by_section`
- `worker_mode_reasoning_by_section`
- `goal_tuning_by_section`
- `constraint_override_notes_by_section`
- `workflow_bindings_by_stage`
- `dispatch_recommendation`

`candidate_persona_sources` should record:

- project registry checked: true|false
- built-in fallback checked: true|false
- project registry outcome
- built-in fallback outcome
- fallback rationale when a built-in persona is recommended

Each `recommended_personas` entry should record:

- persona id
- runtime role: `orchestrator` | `worker` | `reviewer` | `explorer`
- source: `project` | `built-in`
- owned scope, review target, or investigation target
- baseline required-field fit rationale grounded in the working brief
- project-priority or built-in-fallback rationale
- enrichment fit rationale when optional enrichment fields affected the recommendation
- role binding from `agents/openai.yaml`
- prompt asset used for launch assembly
- workflow bindings

Persona recommendation rules:

- project registry priority applies only after the persona satisfies the relevant runtime-role gate and required-field fit
- use a project persona only when it is stronger than the built-in fallback or adds project-specific value the built-in cannot carry
- record built-in fallback explicitly when no project persona is eligible or stronger
- worker recommendations must pass the worker-capability gate before appearing as worker candidates
- reviewer recommendations must pass the reviewer-only gate before appearing as review-lane candidates
- do not recommend a persona from keywords alone; cite the working brief goal, constraints, risks, scope, or artifact type

## Grill-Me Decision Log

The orchestrator owns this log. The `grill-me` explorer remains read-only and returns evidence or one unresolved question at a time.

Use one entry per decision:

- Decision ID:
- State: open | confirmed | stopped
- Question:
- User-Confirmed Answer:
- Recommendation Offered:
- Rationale Or Repository Evidence:
- Dependencies Resolved:
- Dependent Branches Unblocked:

Rules:

- create or update an entry only when `grill-me` is explicitly active
- keep `State: open` until the user explicitly confirms an answer
- do not treat the recommended answer as confirmation
- record repository-resolved facts as evidence without asking the user to decide them
- use confirmed entries as inputs to later design specs and implementation plans
- keep round approval and runtime lifecycle state in `dispatch-plan.md`

## Runtime Preparation

- `required_for_goal_by_section`
- `review_target_strategy`
- `controller_semantics_notes`

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- Persona selection must record source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- The working brief recommends `worker mode` by section, but it does not act as the final execution authority.
- `recommended_worker_mode_by_section` must be derived from task structure, scope shape, and risk, not from persona labels alone.
- User-provided scope limits, prohibitions, and delivery boundaries must be captured in `constraints` before any worker-mode recommendation is made.
- If a recommended `worker mode` conflicts with user constraints, record the tension and the best-effort fallback in `constraint_override_notes_by_section`.
- `goal_tuning_by_section` may only soften or sharpen the recommended mode posture; it must not replace the structure-driven recommendation inside the working brief.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.

# Working Brief Template

Use this template after estimation and before any persona dispatch.

## Artifact Metadata

- `schema_version`
- `brief_version`
- `brief_status`
- `topic_slug`
- `created_at`
- `updated_at`
- `derived_from_user_request`

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

## Persona And Workflow Guidance

- `recommended_personas`
- `persona_selection_notes`
- `workflow_bindings_by_stage`
- `dispatch_recommendation`

## Runtime Preparation

- `required_for_goal_by_section`
- `review_target_strategy`
- `controller_semantics_notes`

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- Persist the working brief before dispatch-plan creation.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.

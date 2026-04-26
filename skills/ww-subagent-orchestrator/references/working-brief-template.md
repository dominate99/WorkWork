# Working Brief Template

Use this template after estimation and before any persona dispatch.

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

## Persona And Workflow Guidance

- `recommended_personas`
- `persona_selection_notes`
- `workflow_bindings_by_stage`
- `dispatch_recommendation`

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.

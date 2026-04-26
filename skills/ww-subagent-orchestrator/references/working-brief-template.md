# Working Brief Template

Use this template after estimation and before any persona dispatch.

## Gate State

- `estimation_complete: true|false`
- `working_brief_ready: true|false`
- `dispatch_decision: pending|approved|revise-requested|stopped`

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
- No packet creation until all dispatch gates are satisfied.
- If the user requests `Revise`, update the working brief first, then regenerate the dispatch plan and ask for approval again.

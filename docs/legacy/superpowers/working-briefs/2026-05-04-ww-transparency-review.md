# Working Brief: WW Transparency Review

Use this brief after estimation and before any persona dispatch.

## Gate State

- `estimation_complete: true`
- `brief_status: ready`
- `brief_version: 5`

## Routing

- `task_routing`: `design/ads/product`
- `orchestrator_choice`: `PM orchestrator`

## Core Intent

- `goal`: Improve the `ww-subagent-orchestrator` skill so users can see current state, next action, and subagent progress without reading internal artifacts.
- `artifact_type`: product interaction design spec
- `relevant_context`: Current skill exposes document summaries and workflow gates but does not yet make live execution state, blocker state, or subagent progress visible in a consistent user-facing format. Staff engineer reviews also identified ambiguity around the canonical runtime source, conflicting reply-shape rules, missing update semantics for progress fields, missing deterministic rules for display-state selection and top-line stage selection, missing exact contracts for top-line derivation and progress-board persistence, and remaining sync gaps between the design and the repo artifacts that are supposed to implement it.
- `constraints`: Preserve the existing approval gates, reviewer convergence rules, and document tracking. Add transparency without turning replies into noisy logs, avoid introducing multiple unsynchronized state machines, make reply rendering deterministic from persisted state, and make the spec precise enough that dependent artifacts can be updated without interpretation gaps.

## Risk And Structure

- `risk_lenses`: user confusion during waits; hidden blockers; weak trust in persona and subagent choices; verbosity bloat if transparency is implemented as raw logs; drift between chat replies and persisted runtime artifacts; stale progress fields; inconsistent top-line summaries in parallel work; ambiguous display-state selection; template/schema drift during implementation; stale contracts between the spec and repo artifacts
- `parallelism_assessment`: low; this round is a single PM design artifact and does not require parallel worker dispatch
- `blocking_dependencies`: user approval of the written spec before any implementation plan is created
- `section_or_workstream_map`: interaction model; user-facing status contract; subagent progress model; artifact and state model

## Persona And Workflow Guidance

- `recommended_personas`: `PM orchestrator`
- `persona_selection_notes`: The primary artifact is a product-facing interaction redesign for transparency and progress visibility, so the PM orchestrator is the strongest match. The revision is informed by a staff engineer review, but this round still stays in a single-orchestrator design pass until the user re-approves the written spec.
- `workflow_bindings_by_stage`: framing -> `superpowers:brainstorming`; later planning -> `superpowers:writing-plans`
- `dispatch_recommendation`: Stay in a single-orchestrator design pass until the revised written spec is reviewed. Do not launch subagents in this round unless the scope expands beyond interaction design or implementation planning begins. The next revision must close the remaining spec-to-artifact synchronization gaps before the spec is approved.

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.

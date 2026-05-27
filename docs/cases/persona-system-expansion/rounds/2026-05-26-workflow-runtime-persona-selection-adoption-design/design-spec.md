# Design Spec: Persona Runtime Selection Adoption

Date: 2026-05-26
Status: Approved
Scope: Design how WorkWork should select and persist built-in/project personas in runtime artifacts. This round does not implement runtime behavior, add persona records, modify validators, expand routing, add secondary tags, or change the project registry.

## Goal

Define an adoption contract that turns the completed persona taxonomy, worker persona expansion, and reviewer persona expansion into concrete runtime-selection behavior for future WorkWork rounds.

The design must answer:

- how project personas outrank built-in fallback personas
- how worker-capability and reviewer-only gates apply before packet creation
- how review lanes map to reviewer personas
- how worker sections map to specialist personas
- where selected personas and rationales should be recorded in working briefs, dispatch plans, review lanes, and worker packets
- whether a later routing or secondary-tag round is needed before broader runtime adoption

## Sources Reviewed

- `docs/cases/persona-system-expansion/rounds/2026-05-25-persona-coverage-audit/design-spec.md`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/working-brief.md`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-persona-taxonomy-contract/dispatch-plan.md`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/working-brief.md`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-worker-persona-expansion/dispatch-plan.md`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/working-brief.md`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-reviewer-persona-expansion/dispatch-plan.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `docs/superpowers/personas/registry.yaml`
- `tools/validate_ww_persona_selection_contracts.py`

## Non-Goals

- No runtime implementation.
- No validator changes.
- No persona record changes.
- No project registry changes.
- No routing expansion.
- No secondary route tag introduction.
- No packet template edits.
- No dispatch plan template edits.

## Current State

The persona system now has the main data needed for better runtime selection:

- taxonomy rules define project-first lookup, built-in fallback, role boundaries, worker capability, reviewer-only behavior, and optional enrichment ranking
- built-in worker-capable specialist personas cover frontend/product UI, test/quality, DevOps/release, data/ML, technical writing, backend, and Java-specific work
- built-in reviewer-only personas cover spec, code quality, product scope, editorial, security, accessibility/UX, and documentation clarity review
- packet contracts already require canonical `subagent_persona`, `persona_rationale`, `persona_binding`, and worker `implementation_principles`

The missing layer is adoption behavior:

- working briefs still need a standard way to recommend candidate personas from project and built-in sources
- dispatch plans still need a standard way to record chosen section personas, lane personas, and selection rationale
- reviewer lanes need a deterministic lane-to-reviewer mapping before packet creation
- worker packets need an explicit rule for copying implementation principles from the selected worker persona
- future validators need concrete artifact expectations before they can enforce portfolio coverage or runtime selection behavior

## Selection Pipeline

Runtime persona selection should be a staged pipeline. Each stage narrows or ranks candidates; no later stage may override an earlier role or source-of-truth gate.

### Stage 1: Determine Runtime Role

Before looking up persona records, the orchestrator must identify the runtime role needed by each planned artifact or packet:

- `orchestrator`: owns round framing, dispatch planning, synthesis, and human-decision handoff
- `worker`: owns scoped production work inside an approved dispatch section
- `reviewer`: owns findings-only inspection of a stable artifact or section
- `explorer`: owns read-only investigation and evidence gathering

The runtime role is not the same as `task_routing`, `task_mode`, or `work_mode`.

Acceptance rule:

- every selected persona must resolve to exactly one runtime role before it is written into a dispatch plan or packet

### Stage 2: Load Candidate Sources

Candidate lookup should preserve the source-of-truth order defined in `persona-registry.md`:

1. project registry at `docs/superpowers/personas/registry.yaml`
2. built-in persona records at `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`

Project records are not automatically better merely because they are project records. They outrank built-ins only after satisfying baseline role compatibility and required-field fit.

Acceptance rule:

- if a project persona and built-in persona both satisfy baseline role compatibility and required-field fit, prefer the project persona only when its `domains`, `strengths`, `use_when`, language fit, or project-specific constraints are stronger than the generic built-in fallback or add project-specific value the built-in cannot carry
- if the project registry has no strong match, use the strongest built-in fallback and record that fallback decision

### Stage 3: Apply Role Gates

Role gates are hard filters.

Worker gate:

- `review_only: false`
- `role_type` is not `orchestrator`
- `implementation_principles` exists
- `implementation_principles` has exactly two entries

Reviewer-only gate:

- `role_type: reviewer`
- `review_only: true`
- no worker write authority
- no `implementation_principles` used for execution
- packet binds to `agents/reviewer-prompt.md`

Orchestrator gate:

- `role_type: orchestrator`
- selected through `task_routing` and primary artifact type
- not eligible as a worker-capable persona
- may act as top-level synthesizer, but should not be the default reviewer when a lane-specific reviewer exists

Explorer gate:

- read-only investigation role
- no write authority
- should remain future-facing until explorer personas exist and the workflow depends on explorer packets for normal operation

Acceptance rule:

- optional enrichment fields may rank candidates only after role gates pass

### Stage 4: Establish Baseline Fit

After role gates, baseline fit should use required persona fields:

- `domains`
- `languages`
- `strengths`
- `use_when`
- `avoid_when`
- `preferred_workflows`
- `priority`

The baseline fit must cite the working brief's goal, constraints, risks, scope, and artifact type. Keyword overlap alone is not enough.

Acceptance rule:

- every persisted persona rationale must name at least one working-brief driver and at least one required-field fit

### Stage 5: Rank With Optional Enrichment

Optional enrichment fields may sharpen ranking and rationale after baseline fit is established:

- `decision_style`
- `quality_bar`
- `tradeoff_bias`
- `failure_modes_to_watch`
- `escalation_triggers`
- `collaboration_posture`
- `taste_criteria`

These fields must not invent capability or bypass source priority.

Acceptance rule:

- if optional enrichment changes the winner between otherwise viable candidates, the rationale must say which enrichment field mattered and why

## Persisted Artifact Contract

Runtime adoption should make persona selection visible in every artifact that either recommends, approves, or launches persona-bound work.

### Working Brief

The working brief should remain advisory, but it should record enough evidence for later approval.

Add or standardize these fields in `Persona And Workflow Guidance`:

- `candidate_persona_sources`
  - project registry checked: true/false
  - built-in fallback checked: true/false
  - source notes
- `recommended_personas`
  - persona id
  - runtime role
  - source: project | built-in
  - owned scope or review target
  - baseline fit rationale
  - enrichment fit rationale, if used
  - role binding
  - workflow bindings
- `persona_selection_notes`
  - why project registry did or did not supply the chosen persona
  - why fallback was used when applicable
  - unresolved ties or reasons to keep a generic orchestrator

The working brief must not create launch authority. It recommends candidates and rationale only.

### Dispatch Plan

The dispatch plan should remain the approval and runtime authority for selected personas.

For each planned section, record:

- `Planned Specialist Personas`
  - canonical persona ids only
  - source: project | built-in
  - runtime role: worker | explorer | none
  - selection rationale
- `Planned Reviewer Persona`
  - canonical reviewer persona id
  - source: project | built-in
  - lane type
  - selection rationale
- `Planned Review Lanes`
  - lane id
  - lane type
  - reviewer persona id
  - reviewer source
  - required: true/false

For runtime ledger records, preserve the launch-time persona snapshot:

- `Active Worker Mode`
- active persona ids
- active persona source
- active role binding
- active packet ids

The dispatch plan must not use display-only titles as authoritative ids.

### Reviewer Lane Records

Reviewer lane records should persist the reviewer chosen for a specific lane and target.

Each review lane should record:

- lane type
- reviewer persona id
- reviewer persona source
- runtime role: reviewer
- review target ref
- reviewer findings
- orchestrator synthesis
- strict review outcome, when applicable

The reviewer persona may not be changed after packet creation without creating a new packet or new review lane revision, because the reviewer identity is part of the review context.

### Worker Packets

Worker packets already require the right fields. Runtime adoption should define their source:

- `subagent_persona`: canonical selected worker persona id
- `persona_rationale`: copied or condensed from the approved dispatch plan
- `persona_binding.runtime_role`: `worker`
- `persona_binding.template_path`: `agents/worker-prompt.md`
- `implementation_principles`: copied directly from the selected persona record in order
- `work_mode`, `work_mode_rationale`, `goal_tuning`, and `constraint_precedence_note`: copied from the approved dispatch plan section, not invented by the packet

Worker packet creation must fail if the selected persona does not satisfy the worker gate.

### Reviewer Packets

Reviewer packets should bind lane-specific reviewer personas:

- `subagent_persona`: canonical selected reviewer persona id
- `persona_rationale`: copied or condensed from the approved dispatch plan lane
- `persona_binding.runtime_role`: `reviewer`
- `persona_binding.template_path`: `agents/reviewer-prompt.md`
- `review_type`: derived from the dispatch review lane type
- `review_target_ref`: immutable target identity captured at packet creation
- `write_scope`: empty unless a later approved rewrite stage explicitly allows otherwise

Reviewer packet creation must fail if the selected persona does not satisfy the reviewer-only gate.

## Review Lane Mapping

Default built-in reviewer mapping should be deterministic, but still allow project registry overrides when a project reviewer is the stronger match.

| Lane Type | Default Built-In Reviewer | Notes |
|---|---|---|
| `spec-review` | `spec-reviewer` | Use for requirements, acceptance criteria, persisted design specs, and implementation plans. |
| `code-quality-review` | `code-quality-reviewer` | Use for implementation correctness, maintainability, regression risk, and test adequacy. |
| `scope-review` | `product-scope-reviewer` | Use for product intent, bounded scope, and user outcome alignment. |
| `editorial-review` | `editorial-reviewer` | Use for creative coherence, messaging, tone, and narrative artifacts. |
| `other` | no default | Requires explicit rationale naming why no durable lane fits and which reviewer family is still qualified. |

Cross-cutting reviewer selection:

- use `secure-software-engineer` when security, authentication, authorization, secrets, abuse paths, or release trust boundaries are material risks
- use `accessibility-ux-reviewer` when accessible interaction, UX clarity, visual affordance, or user workflow friction is a material review surface
- use `documentation-clarity-reviewer` when source-of-truth clarity, procedural documentation, onboarding, maintainer guidance, or reader actionability is the material review surface

When cross-cutting concerns apply, the orchestrator may either:

- add a second review lane if the concern is independently material, or
- select the cross-cutting reviewer for `other` only with explicit rationale if none of the durable lane types fit

Acceptance rule:

- `pm-orchestrator` should no longer be the default reviewer for `scope-review` when `product-scope-reviewer` is available, unless the rationale names a project-specific reason

## Worker Specialist Mapping

Default built-in worker mapping should be based on section-owned scope and dominant implementation risk, not only top-level `task_routing`.

| Work Surface | Default Built-In Worker Candidate | Notes |
|---|---|---|
| backend services, APIs, integration boundaries | `senior-backend-engineer` | Prefer when service correctness, data integrity, or API boundaries dominate. |
| Java-specific implementation | `java-pro-engineer` | Prefer when Java or framework behavior materially affects correctness. |
| frontend/product UI | `frontend-product-engineer` | Prefer when UI state, layout, accessibility, or interaction details dominate. |
| tests, fixtures, regression harnesses | `test-quality-engineer` | Prefer when verification design is the main work surface. |
| CI, release, deployment, infrastructure | `devops-release-engineer` | Prefer when operational reliability or rollback safety dominates. |
| data, analytics, ML workflows | `data-ml-engineer` | Prefer when data assumptions, metrics, pipelines, or model evaluation dominate. |
| docs, guides, maintainer instructions | `technical-writer` | Prefer when the work product is documentation or knowledge transfer. |

Mixed work should be decomposed by section when write scopes are separable. If a section genuinely spans multiple work surfaces:

- choose one primary worker persona based on the owned scope and highest-risk execution surface
- record secondary concerns in the rationale
- add review lanes for material cross-cutting risks instead of adding multiple implementers to the same write scope by default

Acceptance rule:

- a selected worker must have exactly two implementation principles, and packet creation must copy them in order

## Project Registry Priority

Project registry priority should be a preference after eligibility, not a blind override.

Use a project persona when:

- it satisfies the same role gate as the built-in candidate
- it has a stronger required-field fit for the section or lane
- it adds project-specific domain knowledge, constraints, workflows, or operational context

Use built-in fallback when:

- the project registry is absent
- the project registry has no eligible persona for the runtime role
- project records duplicate built-ins without stronger required-field fit
- project records are missing worker gate fields required for launch

Record source decisions in both the working brief and dispatch plan.

Acceptance rule:

- when built-in fallback wins over an available project persona, the rationale must name the failed or weaker project fit

## Routing And Secondary Tags Decision

This design should not expand routing yet.

Current top-level routing still serves orchestrator selection:

- `code/programming` -> `staff-engineer-orchestrator`
- `design/ads/product` -> `pm-orchestrator`
- `video/creative` -> `creative-director-orchestrator`

The expanded worker and reviewer personas reduce pressure to add immediate top-level routes because specialist selection can cover many cross-category execution surfaces inside a route.

However, a later routing or secondary-tag round is still warranted if runtime adoption shows repeated ambiguity in these families:

- research/analysis
- documentation/knowledge
- operations/release
- data/ML
- QA/test
- UX/accessibility

Recommended later design question:

- keep `task_routing` as a small orchestrator selector, and introduce optional secondary tags for specialist and reviewer selection
- avoid expanding top-level `task_routing` until there is evidence that orchestrator choice itself is wrong, not merely that specialist selection needs more nuance

Acceptance rule:

- runtime selection adoption should not block on routing expansion

## Failure Modes

The later implementation should explicitly guard against:

- selecting a reviewer-only persona as worker
- selecting an orchestrator persona as worker
- selecting a worker-capable persona as reviewer without reviewer runtime role compatibility
- using display titles instead of canonical ids
- silently falling back to built-ins without recording why no project persona fit
- relying on optional enrichment before required-field fit
- creating worker packets without copied implementation principles
- creating reviewer packets with non-empty write scope
- changing reviewer persona identity after `review_target_ref` is captured

## Follow-Up Rounds

### Runtime Adoption Implementation

Update the active WorkWork contract and templates so working briefs, dispatch plans, reviewer lanes, and packets record the fields described here.

Expected scope:

- `SKILL.md`
- `references/working-brief-template.md`
- `assets/dispatch-plan-template.md`
- `references/subagent-packet-contract.md`
- README maintainer guidance if needed

### Persona Selection Validator Expansion

After implementation, add validation for:

- project-first source recording
- built-in fallback rationale
- worker-capability gate compliance
- reviewer-only gate compliance
- lane-to-reviewer availability
- worker packet implementation-principle copying

### Routing Or Secondary Tags Design

Open only if adoption reveals repeated ambiguity that cannot be solved through specialist or reviewer selection rationale.

Decision space:

- keep current top-level routes
- add optional secondary tags
- expand top-level routes only if orchestrator choice itself is repeatedly wrong

## Acceptance Criteria

- The design preserves project registry priority without allowing project records to bypass role gates.
- The design preserves built-in fallback without making built-ins the silent default.
- The design makes worker-capability and reviewer-only gates explicit before packet creation.
- The design maps current durable review lanes to built-in reviewer personas and explains cross-cutting reviewer use.
- The design maps common worker surfaces to built-in worker-capable specialist personas.
- The design identifies where selected persona ids, sources, role bindings, and rationales should be persisted.
- The design defers implementation, validators, routing expansion, secondary tags, persona records, and project registry changes to later approved rounds.

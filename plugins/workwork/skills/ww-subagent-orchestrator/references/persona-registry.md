# Persona Registry Rules

## Sources

Check personas in this order:

1. Project registry at `docs/superpowers/personas/registry.yaml`
2. Built-in persona records at `references/built-in-personas.yaml`

## Required Persona Fields

Each persona should define:

- `id`
- `title`
- `category`
- `role_type`
- `domains`
- `languages`
- `strengths`
- `use_when`
- `avoid_when`
- `preferred_workflows`
- `review_only`
- `priority`

Worker-capable personas additionally require:

- `implementation_principles`

## Optional Persona Enrichment Fields

Phase 1 persona enrichment adds optional judgment-oriented fields.

These fields are additive. Their absence does not invalidate an existing persona record.

Each persona may additionally define:

- `decision_style`
- `quality_bar`
- `tradeoff_bias`
- `failure_modes_to_watch`
- `escalation_triggers`
- `collaboration_posture`
- `taste_criteria`

Field guidance:

- `decision_style`
  - describe how the persona resolves ambiguity before detailed instructions arrive
- `quality_bar`
  - define what level of finish or rigor this persona treats as acceptable
- `tradeoff_bias`
  - describe what this persona protects when two acceptable choices compete
- `failure_modes_to_watch`
  - list the mistakes or regressions this persona notices early
- `escalation_triggers`
  - list the conditions where this persona should escalate instead of powering through
- `collaboration_posture`
  - describe how this persona tends to interact with other roles during synthesis or execution
- `taste_criteria`
  - capture the persona's bar for coherence, clarity, simplicity, or felt quality when that bar materially matters

Authoring rules for optional enrichment fields:

- enrich judgment, not biography
- keep wording operational and decision-oriented
- do not duplicate `runtime_role` behavior or role-prompt restrictions
- do not restate worker `work_mode` semantics in persona records
- omit a field rather than writing filler text
- prefer concise entries with visible contrast between personas

## Phase 1 Compatibility Boundary

Phase 1 enrichment is documentation-level and additive.

Compatibility rules:

- the current required fields remain the validity baseline for persona records
- optional enrichment fields must not be treated as required until a later approved runtime-adoption round says so
- `implementation_principles` remains the worker-only execution field and is not replaced by optional enrichment fields
- reviewer and explorer constraints continue to live in role prompts and packet contracts
- role prompts remain behavioral templates; persona records remain viewpoint records
- `persona`, `runtime_role`, role prompt behavior, and worker `work_mode` must remain separate concepts

## Selection Rules

- The orchestrator owns persona selection.
- Every selected persona must include a rationale grounded in the working brief.
- Reviewer personas do not double as implementers for the same section.
- Language specialists are optional and only added when language-specific detail materially affects quality or risk.
- If the project registry contains a strong match, prefer it over a generic built-in persona.
- Worker-candidate filtering happens before final persona selection for implementation work.
- A worker-capable persona is any persona with `review_only: false` and `role_type` not equal to `orchestrator`.
- A worker-capable persona must already have exactly two `implementation_principles` before it may enter the worker selection set.
- The first `implementation_principles` entry is the hard implementation rule; the second entry is the soft implementation principle.
- Until runtime adoption rules are explicitly updated, persona selection must continue to rely on required fields first and treat optional enrichment fields as advisory context only.
- During partial enrichment rollout, a persona must not be rejected solely because it lacks optional enrichment fields if it still satisfies the required-field baseline.
- If optional enrichment fields are used in rationale, they should sharpen why a persona was chosen, not replace the required-field justification.

## Migration Rules

Use these migration rules during persona-enrichment rollout:

- phase 1 defines optional fields and rollout posture before any registry-wide enrichment pass
- adopt enrichment in this order unless a later approved plan says otherwise:
  - orchestrator personas
  - reviewer personas
  - worker personas
  - explorer personas
- keep the persona catalog intentionally small during migration; do not add new personas merely to express nuances that optional fields can already carry
- use optional enrichment fields to create sharper contrast between existing personas before expanding persona count
- if a field's meaning is unclear for a persona, leave it unset instead of inventing vague prose
- bulk runtime adoption, packet changes, validator changes, and registry-wide requirements belong to later approved rounds, not phase 1

## Built-In Routing Defaults

- `code/programming` -> `staff-engineer-orchestrator`
- `design/ads/product` -> `pm-orchestrator`
- `video/creative` -> `creative-director-orchestrator`

These defaults choose the orchestrator category. They do not replace context-driven specialist selection.
The concrete built-in persona records that satisfy these defaults live in `references/built-in-personas.yaml`.
Use the built-in persona `id` field as the canonical resolver key for defaults and fallback selection. `title` is display text only.

## Mixed Task Tie-Break

If a task genuinely spans multiple categories:

- choose the orchestrator from the primary artifact being produced
- break ties using the highest-risk decision area
- add cross-category concerns as specialist personas instead of swapping orchestrators during the same dispatch round

## Prompt Binding Roles

Use these role bindings when assembling packets and launch prompts:

- `orchestrator` -> top-level controller prompt and synthesis responsibilities
- `worker` -> implementer prompt with write authority limited to owned scope
- `reviewer` -> findings-only prompt with no rewrite authority
- `explorer` -> read-only prompt for investigation and scoped evidence gathering

Prompt binding rules:

- a persona selection must resolve to one of the supported runtime roles above before packet assembly
- `template_path` in the packet contract must point to the role-specific prompt asset
- role prompts are behavioral templates, not persona registry records
- reviewer and worker prompts must remain distinct even when they share the same category

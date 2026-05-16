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

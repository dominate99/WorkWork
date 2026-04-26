# Persona Registry Rules

## Sources

Check personas in this order:

1. Project registry at `docs/superpowers/personas/registry.yaml`
2. Built-in personas inferred from the active task category

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

## Selection Rules

- The orchestrator owns persona selection.
- Every selected persona must include a rationale grounded in the working brief.
- Reviewer personas do not double as implementers for the same section.
- Language specialists are optional and only added when language-specific detail materially affects quality or risk.
- If the project registry contains a strong match, prefer it over a generic built-in persona.

## Built-In Routing Defaults

- `code/programming` -> `staff engineer orchestrator`
- `design/ads/product` -> `PM orchestrator`
- `video/creative` -> `creative director orchestrator`

These defaults choose the orchestrator category. They do not replace context-driven specialist selection.

## Mixed Task Tie-Break

If a task genuinely spans multiple categories:

- choose the orchestrator from the primary artifact being produced
- break ties using the highest-risk decision area
- add cross-category concerns as specialist personas instead of swapping orchestrators during the same dispatch round

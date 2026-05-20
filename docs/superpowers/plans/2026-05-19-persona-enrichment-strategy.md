# Persona Enrichment Strategy Implementation Plan

Goal: turn the approved persona-enrichment strategy into a staged implementation track that makes personas materially stronger in judgment, taste, routing, and escalation behavior without collapsing the current separation between `persona`, `runtime_role`, role prompts, and worker `work_mode`.

Architecture: implement persona enrichment in layers. First define an enriched persona model and compatibility rules. Then pilot the model on a small high-leverage persona set. Only after the model is coherent should runtime selection logic, packet semantics, and validator coverage begin consuming the new fields.

Review focus: prevent "richer persona" work from degenerating into persona-count growth, prose-heavy bios, or duplicated role behavior. Review should specifically check that enriched fields change decision posture and quality bars, not just tone or marketing language.

Tech stack: Markdown contracts, YAML persona records, repo-local Python validators, PowerShell, `rg`

---

- [ ] Establish the compatibility boundary
Document the implementation boundary before any schema or registry edits. The boundary is:
  - preserve the current distinction between `persona`, `runtime_role`, and role prompt behavior
  - do not turn reviewer or explorer constraints into persona fields
  - do not change worker `work_mode` semantics as part of persona enrichment
  - treat enriched persona fields as additive until runtime adoption is explicitly approved

- [ ] Extend persona-model documentation first
Update the persona-system documentation so the richer model is defined before registry data is changed.

Primary targets:
  - `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
  - `docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md`

Add or clarify:
  - `decision_style`
  - `quality_bar`
  - `tradeoff_bias`
  - `failure_modes_to_watch`
  - `escalation_triggers`
  - `collaboration_posture`
  - `taste_criteria`

The documentation should distinguish:
  - current required fields
  - optional enrichment fields
  - fields that are safe for registry-only use
  - fields that require later runtime adoption work

- [ ] Define migration rules for enriched persona fields
Write explicit migration rules so current persona records remain valid while the richer model is introduced.

The migration rules should answer:
  - which fields are optional in phase 1
  - which persona categories should adopt enrichment first
  - how to keep non-enriched personas selectable during transition
  - how to avoid introducing routing bias from partially enriched records

- [ ] Pilot enrichment on orchestrator personas first
Apply the richer model to the highest-leverage built-in orchestrator personas before touching the broader persona catalog.

Primary targets:
  - `pm-orchestrator`
  - `creative-director-orchestrator`
  - `staff-engineer-orchestrator`

For each persona, define:
  - a distinct decision style
  - a clear quality bar
  - an explicit tradeoff bias
  - concrete escalation triggers
  - a visible collaboration posture
  - taste criteria where applicable

The goal is not symmetry. The goal is contrast that improves routing and synthesis behavior.

- [ ] Enrich reviewer personas second
Apply the richer model to reviewer personas after orchestrators so reviewer judgment becomes more distinct without weakening findings-only boundaries.

Primary target:
  - `secure-software-engineer`

Reviewer enrichment should sharpen:
  - what the reviewer considers material
  - what classes of risk it notices first
  - when it escalates uncertainty instead of implying confidence

Do not move reviewer behavior rules out of `reviewer-prompt.md` or packet contract surfaces.

- [ ] Enrich selected worker personas third
Apply the richer model to a small number of worker-capable personas only after orchestrator and reviewer pilots are coherent.

Primary targets:
  - `senior-backend-engineer`
  - `java-pro-engineer`

Worker enrichment should complement, not replace:
  - existing `implementation_principles`
  - worker `work_mode`

The enriched fields should clarify why two worker personas make different implementation choices under the same `work_mode`.

- [ ] Decide whether explorer personas need enrichment now or later
Do not assume explorer personas deserve the same priority. Inspect whether the current repo uses explorer personas often enough for richer judgment fields to matter in the near term.

If explorer usage is still sparse:
  - record explorer enrichment as deferred
  - define only the minimum compatible model now

If explorer usage is growing:
  - add enrichment fields that strengthen evidence-gathering posture without overlapping explorer role-prompt behavior

- [ ] Update runtime-selection guidance after the pilot set is stable
Once enriched persona records exist for the pilot set, update the skill contract and planning docs so orchestrators can use the new fields intentionally.

Primary targets:
  - `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
  - persona selection guidance in `persona-registry.md`
  - planning guidance in the working-brief and dispatch-plan templates if the new fields affect planning-time reasoning

Runtime-adoption changes should specify:
  - how enriched fields influence persona selection
  - which fields are advisory versus decision-driving
  - how persona rationale should reference enriched judgment structure

- [ ] Defer packet-contract changes until runtime meaning is proven
Do not rush enriched persona fields into packets unless the controller truly needs them at execution time.

Before changing `subagent-packet-contract.md`, validate:
  - which enriched fields must cross the packet boundary
  - whether packet duplication would create drift against the registry
  - whether prompt-time behavior can consume the field without ambiguity

If a field does not materially affect runtime execution, leave it in the registry and planning layer.

- [ ] Add validator coverage in phases
Extend repo-local validators only after the enriched model is concrete enough to check automatically.

Phase the validator work:
  - phase 1: validate allowed field names and placement in persona docs or registry
  - phase 2: validate pilot personas include the required enrichment fields
  - phase 3: validate runtime contract references if `SKILL.md`, packets, or prompts begin consuming enriched fields

Do not add validators for ambiguous semantics.

- [ ] Keep the persona catalog intentionally small during rollout
Do not expand the persona count materially until the enriched pilot set proves that the new model changes actual decisions.

If adding new personas after the pilot:
  - add only high-contrast records
  - justify each new persona by non-overlapping decision posture
  - reject personas that differ only in tone, industry jargon, or vague seniority

- [ ] Run staged review checkpoints
Use bounded review after each implementation phase instead of one large review at the end.

Recommended review checkpoints:
  - after persona-model documentation changes
  - after orchestrator persona enrichment
  - after reviewer and worker pilot enrichment
  - after any skill-contract or packet-contract runtime adoption changes
  - after validator additions

- [ ] Run final verification for each implementation round
For each round that edits contracts, registry data, or validators, verify:
  - targeted `rg` scans across persona docs, registry files, and skill-contract surfaces
  - validator runs if any persona validators were changed
  - `git diff --stat` to confirm scope stayed bounded

Recommended checks for the first implementation round:

```powershell
rg -n "decision_style|quality_bar|tradeoff_bias|failure_modes_to_watch|escalation_triggers|collaboration_posture|taste_criteria" `
  "plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md" `
  "plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml" `
  "docs/superpowers/personas/registry.yaml" `
  "docs/superpowers/specs/2026-05-19-persona-enrichment-strategy-design.md"
```

```powershell
git diff --stat
```

## Recommended Execution Sequence

1. documentation and migration rules
2. orchestrator persona pilot
3. reviewer persona pilot
4. worker persona pilot
5. runtime-selection guidance updates
6. packet-contract adoption only if still justified
7. validator rollout
8. optional small-count persona expansion

## Success Criteria

This plan succeeds if implementation later produces:

- stronger contrast between existing personas without a large count increase
- better orchestrator routing and synthesis behavior
- clearer reviewer judgment posture
- worker personas that differ in real tradeoff choices instead of biography text
- no collapse between persona, runtime role, prompt contract, and `work_mode`

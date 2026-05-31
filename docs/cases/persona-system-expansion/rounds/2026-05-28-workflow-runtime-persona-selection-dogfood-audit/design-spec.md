# Persona Runtime Selection Dogfood Gap Report

Date: 2026-05-28
Status: Approved
Scope: Audit whether the completed runtime persona selection contract is being used consistently by WorkWork's active contract, templates, and recent persona-system-expansion rounds. This report does not implement changes, add personas, edit validators, expand routing, add secondary tags, or change the project registry.

## Goal

Check whether WorkWork is dogfooding the runtime persona selection recording contract after the completed design, implementation, and validator expansion rounds.

The audit focuses on:

- working brief candidate sources and recommended persona records
- dispatch plan planned reviewer and specialist records
- review lane records
- section runtime persona snapshots
- subagent packet contract persona fields
- evidence for or against a later routing or secondary tags design round

## Sources Reviewed

- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml`
- `docs/superpowers/personas/registry.yaml`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-design/`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-adoption-implementation/`
- `docs/cases/persona-system-expansion/rounds/2026-05-26-workflow-runtime-persona-selection-validator-expansion/`
- `docs/cases/persona-system-expansion/rounds/2026-05-28-workflow-runtime-persona-selection-dogfood-audit/`
- `tools/validate_ww_persona_selection_contracts.py`
- `tools/validate_ww_repo.py`

## Audit Standard

A fully dogfooded runtime persona selection record should show:

- candidate persona sources checked
- selected persona id
- persona source: `project` or `built-in`
- runtime role: `orchestrator`, `worker`, `reviewer`, or `explorer`
- baseline required-field fit rationale
- project-priority or built-in-fallback rationale
- role binding or prompt binding where launch or packet assembly is relevant
- durable review lane persona source and runtime role
- launch-time active persona snapshot when work starts

Older rounds that predate the implementation round are classified as historical baseline, not current violations.

## Findings

### 1. Active Contract And Templates Mostly Pass

Status: pass with one cleanup gap.

Evidence:

- `working-brief-template.md` now requires `candidate_persona_sources`, `recommended_personas`, `persona_selection_notes`, persona source, runtime role, baseline fit, and project-priority or built-in-fallback rationale.
- `dispatch-plan-template.md` now records planned reviewer source/runtime role/rationale, specialist source/runtime role/rationale, planned review lane source/runtime role/rationale, and active persona ids/sources/role bindings.
- `subagent-packet-contract.md` now requires `persona_source`, `persona_rationale`, and `persona_binding`, and both reviewer and worker packet examples include `persona_source: built-in`.
- `SKILL.md` defines project-first lookup, built-in fallback, worker-capability gate, reviewer-only gate, durable review-lane mapping, and worker specialist mapping.
- `validate_ww_persona_selection_contracts.py` checks these surfaces with 28 rules.

Gap:

- The `Section Review Record` template persists `Reviewer Source` and `Reviewer Runtime Role`, but it does not persist `Reviewer Selection Rationale` in the durable review lane record. The rationale exists in `Planned Review Lanes`, so the information is present before launch, but the durable review record does not snapshot it next to the reviewer identity.

Classification: medium dogfood gap.

Recommended follow-up:

- In a later contract cleanup round, add `Reviewer Selection Rationale` to `Section Review Record` and expand validator coverage if the team wants durable review-lane records to carry rationale, not only planned lanes.

### 2. Adoption Design Round Is Historical Baseline, Not A Current Failure

Status: historical partial dogfood.

Evidence:

- The adoption design working brief predates the implementation contract and does not have `candidate_persona_sources`.
- Its `recommended_personas` entries do not record persona source or runtime role in the current field shape.
- Its dispatch plan does not include the later planned reviewer source/runtime role/rationale fields or durable review lane source/runtime role fields.
- The design spec itself created the adoption contract and therefore could not fully follow it yet.

Classification: historical baseline.

Recommended follow-up:

- Do not rewrite this round merely for dogfood purity. It is useful as evidence of the before state.

### 3. Adoption Implementation Round Mostly Dogfoods The New Contract

Status: mostly pass with minor record-shape drift.

Evidence:

- The working brief records `candidate_persona_sources`.
- Recommended personas record runtime role and source.
- The dispatch plan records planned reviewer source/runtime role/rationale.
- The dispatch plan records specialist source/runtime role/rationale.
- Planned review lane records include reviewer source/runtime role/rationale.
- Section review records include reviewer source and runtime role.

Gaps:

- The working brief puts built-in fallback rationale in `persona_selection_notes`, but the `technical-writer` and `spec-reviewer` recommended persona entries do not each carry their own explicit `project-priority or built-in-fallback rationale` field.
- The section runtime ledger does not preserve `Active Persona IDs`, `Active Persona Sources`, or `Active Persona Role Bindings`. Those fields were added by the implementation round's template change, so this is understandable but still shows the first adoption round did not fully snapshot runtime persona selection after launch.
- Durable review lane records do not snapshot reviewer selection rationale, matching the active template gap above.

Classification: low-to-medium dogfood gap.

Recommended follow-up:

- Treat this as an early-adoption drift case. A future cleanup round can normalize completed round records only if historical consistency becomes valuable for validators or documentation examples.

### 4. Validator Expansion Round Strongly Dogfoods Working Brief And Dispatch Planning

Status: pass with durable runtime-record caveats.

Evidence:

- The working brief records `candidate_persona_sources`.
- `test-quality-engineer` and `code-quality-reviewer` entries include runtime role, source, baseline fit, project-priority or built-in-fallback rationale, role binding, and workflow bindings.
- The dispatch plan records planned reviewer source/runtime role/rationale.
- The dispatch plan records planned specialist source/runtime role/rationale.
- Planned review lane records include reviewer source/runtime role/rationale.
- Section review records include reviewer source and runtime role.

Gaps:

- The section runtime ledger does not include active persona ids/sources/role bindings because the round was created before the final active persona snapshot template field was adopted.
- Durable review lane records still do not snapshot reviewer selection rationale.
- No subagent packet was created, so packet-level dogfood is contract/example based, not live-packet based.

Classification: low dogfood gap.

Recommended follow-up:

- Use the validator expansion round as the best current example for working brief and planned dispatch records.
- Do not treat it as evidence that runtime packet assembly has been dogfooded; no packet artifact exists.

### 5. Current Dogfood Audit Round Is The First Full Self-Application

Status: pass.

Evidence:

- The working brief records candidate persona sources, project registry outcome, built-in fallback outcome, and fallback rationale.
- `technical-writer` and `spec-reviewer` entries include runtime role, source, baseline fit, project-priority or built-in-fallback rationale, enrichment rationale, role binding, and workflow bindings.
- The dispatch plan records planned reviewer source/runtime role/rationale.
- The dispatch plan records specialist source/runtime role/rationale.
- The planned review lane records reviewer source/runtime role/rationale.
- The section runtime ledger records active persona ids, sources, and role bindings after launch.

Gap:

- The future review lane record will still lack durable reviewer selection rationale unless the active template changes in a later round.

Classification: pass with inherited template caveat.

## Packet Contract Dogfood

Status: contract pass, runtime evidence missing.

Evidence:

- `subagent-packet-contract.md` requires `persona_source`.
- The packet contract defines `persona_source` values and source-of-truth meaning.
- `persona_rationale` must include baseline required-field fit plus project-priority or built-in-fallback rationale.
- `persona_binding.runtime_role` is constrained to the supported runtime roles.
- Reviewer and worker examples include `persona_source: built-in`, `persona_rationale`, and role-specific prompt bindings.

Gap:

- Recent persona-system-expansion rounds record `Packet Created: false`, so there is no live subagent packet artifact proving runtime packet assembly copies source/rationale/binding from the approved dispatch plan.

Classification: evidence gap, not a contract failure.

Recommended follow-up:

- The next round that creates an actual worker or reviewer packet should be audited for packet-level source/rationale/binding persistence.

## Routing And Secondary Tags Decision

Recommendation: do not open routing or secondary tags implementation yet.

Evidence:

- The three recent rounds all used `code/programming` routing with `staff-engineer-orchestrator`, even when the immediate work surface was design/spec, documentation contract, or validation.
- Specialist persona selection handled the more specific execution surfaces:
  - `technical-writer` for contract and audit documentation
  - `test-quality-engineer` for validator work
  - `spec-reviewer` for spec/contract review
  - `code-quality-reviewer` for validator review
- This supports the adoption design's model: keep top-level routing small for orchestrator choice and use specialist/reviewer persona mapping for execution nuance.
- The evidence does show repeated secondary surfaces: documentation/knowledge, QA/test, and workflow-contract audit.

Decision:

- There is enough evidence to keep secondary tags as a future design question.
- There is not yet enough evidence to expand top-level routing or add secondary tags immediately.

Recommended later question:

- If future rounds repeatedly need machine-readable specialist hints beyond natural-language rationale, open a secondary-tag design round focused on evidence collection and optional tagging semantics.
- Do not expand top-level `task_routing` unless orchestrator selection itself becomes wrong, not merely broad.

## Gap Register

| ID | Gap | Severity | Owner Surface | Recommended Follow-Up |
|---|---|---:|---|---|
| DG-001 | Durable review lane records omit reviewer selection rationale | Medium | dispatch plan template and completed review records | Contract cleanup round, then optional validator expansion |
| DG-002 | Early adoption implementation working brief stores fallback rationale in notes instead of each persona entry | Low | historical round artifact | Leave historical, or normalize only if examples become canonical |
| DG-003 | Completed implementation and validator rounds lack active persona snapshot fields | Low | historical round artifact | Leave historical, or normalize only if validators later require active snapshot history |
| DG-004 | No live packet artifact proves persona source/rationale/binding copying | Medium evidence gap | future packet creation | Audit the next real worker/reviewer packet round |
| DG-005 | Secondary routing surfaces are recurring but not yet proven to require new routing mechanics | Low | future design | Revisit after more runtime dogfood evidence |

## Acceptance Criteria Check

- Active contract and templates were checked for source/runtime role/rationale fields.
- Recent working briefs were checked for candidate sources and recommended persona records.
- Recent dispatch plans were checked for planned reviewer, planned specialist, review lane, and runtime ledger records.
- Subagent packet contract was checked for `persona_source`, `persona_rationale`, and `persona_binding`.
- Historical pre-adoption gaps were classified separately from current contract gaps.
- The report does not implement, add personas, change validators, expand routing, add secondary tags, or edit the project registry.

## Conclusion

Runtime persona selection recording is now mostly dogfooded at the working brief and planned dispatch layers. The strongest remaining gap is durable review-lane rationale persistence: the planned lane records carry rationale, but the review lane execution record does not snapshot it. Packet-level dogfood is still unproven because no recent round produced an actual packet artifact.

The next best step is a small contract cleanup or packet dogfood round, not routing expansion. Routing or secondary tags should stay in the queue as a later design topic after more real runtime evidence accumulates.

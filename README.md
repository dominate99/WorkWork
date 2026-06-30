# WW Subagent Orchestrator Plugin

Turn `$ww` into a reliable planning-and-dispatch workflow for AI subagents.

This reusable workflow package helps you scope work, generate a clear brief, choose the right orchestrator, create an approval-ready dispatch plan, and coordinate specialist subagents with consistent review gates.

Built for `Codex`, `Claude Code`, `Cursor`, and `OpenCode`.

## Quick Start

1. Start with the install doc for your environment.
2. Start your prompt with `$ww`.
3. Review the generated brief and dispatch plan.
4. Reply with:
   - `1` or `Approve`
   - `2` or `Revise`
   - `3` or `Stop`

Subagents are dispatched only after approval.

Example:

```text
$ww Plan a migration from REST polling to webhooks for our notification pipeline.
```

| Environment | First-Step Doc | Install Target / Reference |
| :--- | :--- | :--- |
| **Codex** | [docs/README.codex.md](docs/README.codex.md) | Repository-root marketplace source at `.agents/plugins/marketplace.json`; installable package at `plugins/workwork/` |
| **Claude Code** | [docs/README.claude.md](docs/README.claude.md) | Packaged plugin root at `plugins/workwork/` |
| **Cursor** | [docs/README.cursor.md](docs/README.cursor.md) | `.cursor-plugin/plugin.json` |
| **OpenCode** | [.opencode/INSTALL.md](.opencode/INSTALL.md) | Repository root plus `.opencode/INSTALL.md` |

> **Codex Note:**  
> The verified local Codex flow adds the repository root as a marketplace source. The installable plugin package lives under `plugins/workwork/`, and the runtime skill lives under `plugins/workwork/skills/ww-subagent-orchestrator/`.

Verified local install commands:

For `Codex`:

```powershell
git clone https://github.com/dominate99/WorkWork.git
cd WorkWork
codex plugin marketplace add .
```

For `Claude Code`:

```powershell
git clone https://github.com/dominate99/WorkWork.git
cd WorkWork
```

Then add `./plugins/workwork` as the Claude Code plugin path. If your Claude build asks for a manifest file instead of a plugin directory, use `./plugins/workwork/.claude-plugin/plugin.json`.

This repository does not include a one-command installer. If that changes later, it will be documented separately from this quick-start.

The canonical packaged runtime skill lives under `plugins/workwork/skills/ww-subagent-orchestrator/`. Keep the repository layout intact when installing from a local checkout; Codex expects the repo-root marketplace source, Claude Code expects the packaged plugin root, and secondary targets should follow their install guides instead of copying manifest directories in isolation.

## What It Does

When you trigger `$ww`, the workflow:

- estimates the task
- builds a working brief
- selects the right orchestrator persona
- writes round artifacts under `docs/cases/<case-slug>/rounds/<round-slug>/`
- pauses for approval before dispatch
- coordinates subagents and review flow

> [!IMPORTANT]
> New `$ww` and `$www` rounds are canonically written under `docs/cases/<case-slug>/rounds/<round-slug>/`. Older type-based paths are legacy history only and are not active write targets for new rounds.

Historical type-based workflow artifacts are archived under `docs/legacy/superpowers/`.

## Best For

Use `$ww` when you want structured orchestration for:

- implementation planning
- multi-step engineering work
- review coordination
- cross-functional briefs
- specialist subagent dispatch

## Example Prompts

```text
$ww Plan and review a refactor of our authentication middleware.
$ww Break this feature request into implementation and review workstreams.
$ww Coordinate backend, security, and QA review for this API change.
$ww grill me on this migration plan until every material decision is resolved.
```

The `$ww grill me` trigger explicitly selects this mode. WorkWork investigates repository facts first and then asks one question at a time during working-brief planning. Every question includes a recommended answer, but the decision remains open until the user confirms or replaces it. The interview is planning-time only and does not launch a subagent packet.

## Key Files

- `docs/README.codex.md`
- `docs/README.claude.md`
- `docs/README.cursor.md`
- `.opencode/INSTALL.md`
- `.agents/plugins/marketplace.json`
- `.cursor-plugin/plugin.json`
- `plugins/workwork/.codex-plugin/plugin.json`
- `plugins/workwork/.claude-plugin/plugin.json`
- `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/case-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `docs/superpowers/personas/registry.yaml`

## Customization

Adapt the workflow to your project by:

- editing `docs/superpowers/personas/registry.yaml`
- updating reference files under `plugins/workwork/skills/ww-subagent-orchestrator/references/`
- modifying assets under `plugins/workwork/skills/ww-subagent-orchestrator/assets/`

## For Maintainers

Contributor and design docs live under:

- `docs/maintainers/specs/`
- `docs/maintainers/plans/`

Local WW validation:

```powershell
python -m pip install PyYAML markdown-it-py
python tools/validate_ww_repo.py
python tools/validate_ww_repo.py --json
python tools/validate_ww_worker_work_mode.py --json
python tools/validate_ww_grill_me_contracts.py --json
python tools/test_validate_ww_grill_me_contracts.py
python tools/validate_ww_persona_selection_contracts.py --json
python tools/validate_ww_persona_packets.py --json
python tools/validate_ww_case_path_identity.py --json
python tools/validate_ww_case_contracts.py --json
python tools/validate_ww_round_lifecycle.py --json
python tools/validate_ww_verifier_authority_contracts.py --json
python -m unittest tools.test_scaffold_ww_case_artifacts -v
python -m unittest tools.test_validate_ww_verifier_authority_contracts -v
```

The repo-level validator runs packaged skill frontmatter checks, worker `work_mode` contract checks, reviewer/explorer role-contract checks, grill-me inline planning contract checks, persona runtime-selection recording contract checks, runtime persona packet artifact checks, case-based path identity contract checks, case artifact contract checks, round lifecycle contract checks, dormant verifier/lane authority contract checks, and case scaffold regression tests. GitHub Actions uses the same repo-local entrypoint.

Task runtime lifecycle maintenance:

- schema version 2 adds dormant lifecycle protocol support; new scaffolded rounds default to `legacy`
- treat `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-lifecycle.md` as the normative lifecycle ownership, transition, persistence, migration, and recovery contract
- treat `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-verification.md` as the dormant verifier authority, lane schema, evidence, lane selection, and model capability contract
- treat `plugins/workwork/skills/ww-subagent-orchestrator/references/task-runtime-missing-capabilities.md` as the dormant internal hook, quality gate/scoring, repair/re-verification, close gate, final human judgment, recovery requirement, and checkpoint contract
- update `SKILL.md`, the working-brief template, dispatch-plan template, packet contract, scaffold helper, and scaffold tests together when changing lifecycle protocol recording
- do not select `task-runtime-v1` until verifier binding/runtime behavior, review progression, repair/re-verification, scoring, close-gate capabilities, and validator coverage are implemented and approved
- do not treat dormant verifier fields or references as active lifecycle authority while a round uses `Lifecycle Protocol: legacy`
- do not treat dormant missing-capability fields or references as active lifecycle authority while a round uses `Lifecycle Protocol: legacy`
- keep `tools/validate_ww_missing_capability_contracts.py` and its regression fixtures aligned with the dormant missing-capability reference, template block, working-brief preparation notes, packet source-context fields, and legacy non-authority guard
- dedicated lifecycle validator rules and negative fixtures belong to a later validator-expansion round

Persona taxonomy changes:

- update `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md` when changing role-family taxonomy, minimum portfolio coverage, expansion decision rules, or built-in/project registry boundaries
- update `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md` when orchestration behavior needs to point at those taxonomy rules
- update `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml` when adding portable built-in worker persona coverage for common WorkWork execution families
- update `plugins/workwork/skills/ww-subagent-orchestrator/references/built-in-personas.yaml` when adding portable built-in reviewer persona coverage for durable review lanes
- update `plugins/workwork/skills/ww-subagent-orchestrator/SKILL.md`, `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`, `plugins/workwork/skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`, and `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md` together when changing runtime persona selection recording rules
- do not add persona records or validator behavior in the same round unless that round explicitly approves those scopes

Case artifact scaffolding:

```powershell
python tools/scaffold_ww_case_artifacts.py `
  --case-slug example-case `
  --round-slug 2026-05-23-example-round `
  --title "Example Round" `
  --user-request "example request" `
  --with-design-spec `
  --with-implementation-plan
```

The scaffolding helper is the default initializer for new `$ww/$www` case rounds under `docs/cases/...`. It creates schema-version-2 `working-brief.md` and `dispatch-plan.md` files with a dormant `legacy` lifecycle protocol by default, updates `case.md`, and can optionally create `design-spec.md` and `implementation-plan.md`. It writes placeholder content only; maintainers still need to complete the round artifacts before approval.

## Summary

WW gives `$ww` a predictable workflow: plan first, approve next, dispatch last.

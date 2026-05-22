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
- writes round artifacts under `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/`
- pauses for approval before dispatch
- coordinates subagents and review flow

> [!IMPORTANT]
> New `$ww` and `$www` rounds are canonically written under `docs/superpowers/cases/<case-slug>/rounds/<round-slug>/`. Older type-based paths may still exist as legacy history during migration, but they are not active parallel write targets for new rounds.

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
```

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
- `plugins/workwork/skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/persona-registry.md`
- `plugins/workwork/skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
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
python tools/validate_ww_persona_selection_contracts.py --json
python tools/validate_ww_case_path_identity.py --json
```

The repo-level validator runs packaged skill frontmatter checks, worker `work_mode` contract checks, reviewer/explorer role-contract checks, persona runtime-selection contract checks, and case-based path identity contract checks. GitHub Actions uses the same repo-local entrypoint.

## Summary

WW gives `$ww` a predictable workflow: plan first, approve next, dispatch last.

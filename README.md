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
| **Codex** | [docs/README.codex.md](docs/README.codex.md) | Recommended: local `.codex-plugin` directory from a full checkout. Fallback only: some Codex builds may preserve sibling repo access for `https://github.com/dominate99/WorkWork/tree/main/.codex-plugin` |
| **Claude Code** | [docs/README.claude.md](docs/README.claude.md) | `.claude-plugin/plugin.json` |
| **Cursor** | [docs/README.cursor.md](docs/README.cursor.md) | `.cursor-plugin/plugin.json` |
| **OpenCode** | [.opencode/INSTALL.md](.opencode/INSTALL.md) | Repository root plus `.opencode/INSTALL.md` |

> **Codex Remote/Browser Note:**  
> The normal supported Codex path for this package layout is a local checkout plus the local `.codex-plugin` directory. The GitHub subdirectory URL below is only an unverified fallback for Codex builds that both accept repository subdirectory installs and preserve access from `.codex-plugin/` to repo-root sibling files such as `../skills/`:  
> `https://github.com/dominate99/WorkWork/tree/main/.codex-plugin`

This repository does not include a one-command installer. If that changes later, it will be documented separately from this quick-start.

All three hidden plugin entry points resolve the shared workflow files from the repo-root `skills/` directory. Keep the repository layout intact when installing from a local checkout; do not copy only `.codex-plugin`, `.claude-plugin`, or `.cursor-plugin` by itself.

## What It Does

When you trigger `$ww`, the workflow:

- estimates the task
- builds a working brief
- selects the right orchestrator persona
- writes a dispatch plan to `docs/superpowers/dispatch-plans/`
- pauses for approval before dispatch
- coordinates subagents and review flow

> [!IMPORTANT]
> `docs/superpowers/dispatch-plans/` is a runtime-generated output location and is not part of the checked-in repository structure by default.

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
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `.cursor-plugin/plugin.json`
- `skills/ww-subagent-orchestrator/SKILL.md`
- `skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `skills/ww-subagent-orchestrator/references/persona-registry.md`
- `skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `docs/superpowers/personas/registry.yaml`

## Customization

Adapt the workflow to your project by:

- editing `docs/superpowers/personas/registry.yaml`
- updating reference files under `skills/ww-subagent-orchestrator/references/`
- modifying assets under `skills/ww-subagent-orchestrator/assets/`

## For Maintainers

Contributor and design docs live under:

- `docs/maintainers/specs/`
- `docs/maintainers/plans/`

The workflow was validated with the official `quick_validate.py` script after installing `PyYAML`.

## Summary

WW gives `$ww` a predictable workflow: plan first, approve next, dispatch last.

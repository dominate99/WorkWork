# WW Subagent Orchestrator Plugin

A reusable workflow package that turns `$ww` into a predictable planning-and-dispatch flow: estimate work, build a brief, create a plan, and coordinate subagents.

> Workflow first, details later. WorkWork supports `Codex`, `Claude Code`, `Cursor`, and `OpenCode`, with a tool-specific entry point or install guide for each environment.

This repository packages the same workflow with tool-specific entry points for `Codex`, `Claude Code`, and `Cursor`, plus install guidance for `OpenCode`.

## Quick Start

Start with the install doc for your environment. Each environment has its own first-step doc and install target:

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

## What This Plugin Does

It helps you:

- estimate work before dispatch
- choose the right top-level orchestrator persona
- build a working brief
- create a tracked dispatch plan file
- coordinate persona-bound subagents
- bind Superpowers workflows at each stage

When you trigger `$ww`:

- estimate the task first
- generate a working brief
- route to the correct orchestrator
- write a dispatch plan file to `docs/superpowers/dispatch-plans/`
- request approval with:
  - `1. Approve`
  - `2. Revise`
  - `3. Stop`
  Reply with `1`, `2`, `3`, `Approve`, `Revise`, or `Stop`.
- dispatch subagents only after approval
- enforce reviewer findings -> orchestrator synthesis -> human judgment

`docs/superpowers/dispatch-plans/` is a runtime-generated output location. It is not part of the checked-in repository structure by default.

## Repository Contents

Plugin entry points live at:

- `CLAUDE.md`
- `AGENTS.md`
- `docs/README.codex.md`
- `docs/README.claude.md`
- `docs/README.cursor.md`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `.cursor-plugin/plugin.json`
- `.opencode/INSTALL.md`

Key files:

- `skills/ww-subagent-orchestrator/SKILL.md`
- `skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `skills/ww-subagent-orchestrator/references/persona-registry.md`
- `skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `docs/superpowers/personas/registry.yaml`

Repository layout:

```text
skills/
  ww-subagent-orchestrator/
    SKILL.md
    agents/openai.yaml
    references/
    assets/

docs/
  maintainers/
    specs/
    plans/
  superpowers/
    personas/
```

## Persona Registry

This repository includes a starter project persona registry at:

`docs/superpowers/personas/registry.yaml`

It shows how to define:

- engineering reviewers like `secure-software-engineer`
- implementation specialists like `senior-backend-engineer`
- language specialists like `java-pro-engineer`
- non-engineering orchestrators and reviewers for product and creative work

You can copy that file into another project and tailor the personas, priorities, and workflow preferences to your team.

## Maintainer Docs

Design history and implementation planning for this repository live under:

- `docs/maintainers/specs/`
- `docs/maintainers/plans/`

Those files are for contributors and maintainers. They are separate from the runtime-facing `docs/superpowers/personas/` path that the skill references inside real projects.

## Validation

This plugin workflow was validated with the official `quick_validate.py` script after installing `PyYAML`.

## Notes

- The plugin expects Superpowers capabilities to be available.
- Project-specific personas can be added at `docs/superpowers/personas/registry.yaml`.
- Design and implementation docs for this repository live under `docs/maintainers/`.

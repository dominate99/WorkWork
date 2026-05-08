# WW Subagent Orchestrator Skill

A reusable skill that turns `$ww` into a predictable planning-and-dispatch flow: estimate work, build a brief, create a plan, and coordinate subagents.

> Workflow first, details later. The install examples below show the Codex skill-installer flow, and the workflow itself works across `Codex`, `Claude Code`, and similar agent-tool setups.

This repository is also packaged as a plugin-style workflow with manifests for `Codex`, `Claude Code`, and `Cursor`, plus an OpenCode install note.

## Install

### Install From GitHub

Users can install it with the skill installer from the repo path:

```text
skills/ww-subagent-orchestrator
```

Standard command template:

```bash
python path/to/install-skill-from-github.py --repo <owner>/<repo> --path skills/ww-subagent-orchestrator
```

Example for this repository:

```bash
python path/to/install-skill-from-github.py --repo dominate99/WorkWork --path skills/ww-subagent-orchestrator
```

Standard GitHub URL template:

```text
https://github.com/<owner>/<repo>/tree/main/skills/ww-subagent-orchestrator
```

This repository's skill URL:

```text
https://github.com/dominate99/WorkWork/tree/main/skills/ww-subagent-orchestrator
```

If your environment already includes the `skill-installer` helper, the same repo/path can be installed through that workflow instead of copying files manually.

After installing, restart Codex to pick up the new skill.

## What This Skill Does

It helps you:

- estimate work before dispatch
- choose the right top-level orchestrator persona
- build a working brief
- create a tracked dispatch plan file
- coordinate persona-bound subagents
- bind Superpowers workflows at each stage

When you trigger `$ww`:

1. estimate the task first
2. generate a working brief
3. route to the correct orchestrator
4. write a dispatch plan file to `docs/superpowers/dispatch-plans/`
5. request:
   1. `Approve`
   2. `Revise`
   3. `Stop`
   Users may reply with `1`, `2`, `3`, `Approve`, `Revise`, or `Stop`.
6. dispatch subagents only after approval
7. enforce reviewer findings -> orchestrator synthesis -> human judgment

`docs/superpowers/dispatch-plans/` is a runtime-generated output location. It is not part of the checked-in repository structure by default.

## Repository Contents

The reusable skill lives at:

`skills/ww-subagent-orchestrator`

Plugin packaging lives at:

- `CLAUDE.md`
- `AGENTS.md`
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

This skill was validated with the official `quick_validate.py` script after installing `PyYAML`.

## Notes

- The skill expects Superpowers capabilities to be available.
- Project-specific personas can be added at `docs/superpowers/personas/registry.yaml`.
- Design and implementation docs for this repository live under `docs/maintainers/`.

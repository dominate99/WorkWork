# WW Subagent Orchestrator Skill

A reusable Codex skill that turns `$ww` into a disciplined orchestration workflow.

The skill is designed to:

- estimate work before dispatch
- choose the right top-level orchestrator persona
- build a working brief
- create a tracked dispatch plan file
- coordinate persona-bound subagents
- bind Superpowers workflows at each stage

## Repository Layout

```text
skills/
  ww-subagent-orchestrator/
    SKILL.md
    agents/openai.yaml
    references/
    assets/

docs/
  superpowers/
    personas/
    specs/
    plans/
```

## Included Skill

The reusable skill lives at:

`skills/ww-subagent-orchestrator`

Key files:

- `skills/ww-subagent-orchestrator/SKILL.md`
- `skills/ww-subagent-orchestrator/references/working-brief-template.md`
- `skills/ww-subagent-orchestrator/references/persona-registry.md`
- `skills/ww-subagent-orchestrator/references/subagent-packet-contract.md`
- `skills/ww-subagent-orchestrator/assets/dispatch-plan-template.md`
- `docs/superpowers/personas/registry.yaml`

## What `$ww` Does

When triggered, the skill is designed to:

1. estimate the task first
2. route to the correct orchestrator
3. generate a working brief
4. write a dispatch plan file
5. request `Approve / Revise / Stop`
6. dispatch subagents only after approval
7. enforce reviewer findings -> orchestrator synthesis -> human judgment

## Install Manually

Copy the skill folder into your Codex skills directory:

```text
~/.codex/skills/ww-subagent-orchestrator
```

On Windows, that is typically:

```text
C:\Users\<your-user>\.codex\skills\ww-subagent-orchestrator
```

## Install From GitHub

If this repository is published to GitHub, Codex users can install it with the skill installer from the repo path:

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

If your Codex environment already includes the `skill-installer` helper, the same repo/path can be installed through that workflow instead of copying files manually.

After installing, restart Codex to pick up the new skill.

## Persona Registry Example

This repository includes a starter project persona registry at:

`docs/superpowers/personas/registry.yaml`

It shows how to define:

- engineering reviewers like `secure-software-engineer`
- implementation specialists like `senior-backend-engineer`
- language specialists like `java-pro-engineer`
- non-engineering orchestrators and reviewers for product and creative work

You can copy that file into another project and tailor the personas, priorities, and workflow preferences to your team.

## Validation

This skill was validated with the official `quick_validate.py` script after installing `PyYAML`.

## Notes

- The skill expects Superpowers capabilities to be available.
- Project-specific personas can be added at `docs/superpowers/personas/registry.yaml`.
- The repository includes design and implementation docs under `docs/superpowers/`.

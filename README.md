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

Example shape:

```bash
python path/to/install-skill-from-github.py --repo <owner>/<repo> --path skills/ww-subagent-orchestrator
```

Or with a GitHub tree URL:

```text
https://github.com/<owner>/<repo>/tree/main/skills/ww-subagent-orchestrator
```

## Validation

This skill was validated with the official `quick_validate.py` script after installing `PyYAML`.

## Notes

- The skill expects Superpowers capabilities to be available.
- Project-specific personas can be added at `docs/superpowers/personas/registry.yaml`.
- The repository includes design and implementation docs under `docs/superpowers/`.

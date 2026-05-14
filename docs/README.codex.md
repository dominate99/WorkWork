# Installing WorkWork In Codex

WorkWork is installed in Codex from the repository-root marketplace at `.agents/plugins/marketplace.json`.

The installable plugin package lives under `plugins/workwork/`, and the canonical runtime skill lives under `plugins/workwork/skills/ww-subagent-orchestrator/`.

## Install From A Local Checkout

Use a full local checkout, then add the cloned repository root as a Codex marketplace source.

```powershell
git clone https://github.com/dominate99/WorkWork.git
cd WorkWork
codex plugin marketplace add .
```

Enable the `workwork` plugin from the added marketplace. In CLI-driven flows, the verified plugin key is:

`workwork@workwork`

After enabling the marketplace plugin, restart or reload Codex if your build needs it to refresh marketplace state.

## Post-Install Check

Make sure Superpowers is already available in Codex before testing `$ww`, or the command can fail even when this plugin is installed correctly.

Start a new Codex session and trigger `$ww` once. If the workflow is available, Codex should enter the WorkWork estimation/planning flow instead of treating `$ww` as plain text.

Verified CLI smoke test from the repository root:

```powershell
codex exec -C . -c 'plugins."workwork@workwork".enabled=true' '$ww make a plan to rename one heading in this README'
```

> Warning: avoid duplicate installs. Enable only one WorkWork install method at a time.
>
> If you are migrating from an older root-level `.codex-plugin` install or another manual WorkWork copy, disable or remove that older WorkWork copy before enabling this marketplace-based install.

## Current Scope

This repository does not currently ship a one-command Codex installer.
The verified Codex path is the local repository-root marketplace source described above.

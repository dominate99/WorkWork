# Working Brief: Installation Risk Fixes

## Artifact Metadata

- `schema_version`: 1
- `brief_version`: 1
- `brief_status`: ready
- `topic_slug`: installation-risk-fixes
- `created_at`: 2026-05-08
- `updated_at`: 2026-05-08
- `derived_from_user_request`: `$ww address these risks`

## Gate State

- `estimation_complete`: true
- `brief_status`: ready
- `brief_version`: 1

## Routing

- `task_routing`: `code/programming`
- `orchestrator_choice`: `staff engineer orchestrator`

## Core Intent

- `goal`: address the remaining release risks in the installation work by fixing the plugin manifest layout mismatch, tightening the Codex fallback wording, and making the post-install verification path explicit and reliable
- `artifact_type`: packaging metadata plus user-facing install documentation
- `relevant_context`:
  - current changed files already live in the isolated worktree at `.worktrees/install-docs-guides`
  - three hidden plugin manifests originally pointed `skills` at `./skills/`, but the actual shared `skills/` directory is at repo root
  - the final review identified one real packaging/layout risk and one onboarding risk:
    - Codex GitHub subdirectory install wording was too easy to read as supported despite the `../skills/` dependency
    - per-tool docs needed a Superpowers prerequisite before the `$ww` smoke test
  - the current worktree already contains uncommitted edits to:
    - `README.md`
    - `docs/README.codex.md`
    - `docs/README.claude.md`
    - `docs/README.cursor.md`
    - `.codex-plugin/plugin.json`
    - `.claude-plugin/plugin.json`
    - `.cursor-plugin/plugin.json`
- `constraints`:
  - keep the docs honest about actual package layout
  - do not invent or imply one-command installers
  - keep Codex GitHub subdirectory wording as build-dependent fallback only
  - preserve the local-checkout path as the normal supported Codex path
  - keep the fix set bounded to the already-identified manifests and install docs

## Risk And Structure

- `risk_lenses`:
  - a wrong `skills` path in plugin manifests makes installs silently fail even when the docs are followed
  - misleading Codex remote-install wording can send users into a broken path that cannot resolve repo-root `skills/`
  - a missing Superpowers prerequisite can make `$ww` appear broken after a technically correct install
  - untracked guide files increase release risk if the final change set is staged or reviewed incompletely
- `parallelism_assessment`:
  - this is a small serial remediation round
  - the files are tightly coupled, so one bounded worker lane is safer than parallel edits
- `blocking_dependencies`:
  - manifest path corrections must land before the docs can be considered correct
  - the final integrated review must happen after both manifest and doc updates
- `section_or_workstream_map`:
  - section 1: correct plugin manifest `skills` paths
  - section 2: align README and per-tool install docs with the corrected layout
  - section 3: add a reliable Superpowers-gated `$ww` post-install check
  - section 4: run final integrated review and close residual risks

## Scope Preparation

- `artifact_mappings`:
  - `artifact_id`: `root_readme`
  - `artifact_kind`: `doc`
  - `artifact_path`: `README.md`
  - `section_anchors`: `Quick Start`, `Notes`
  - `artifact_id`: `codex_guide`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/README.codex.md`
  - `section_anchors`: none
  - `artifact_id`: `claude_guide`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/README.claude.md`
  - `section_anchors`: none
  - `artifact_id`: `cursor_guide`
  - `artifact_kind`: `doc`
  - `artifact_path`: `docs/README.cursor.md`
  - `section_anchors`: none
  - `artifact_id`: `codex_manifest`
  - `artifact_kind`: `config`
  - `artifact_path`: `.codex-plugin/plugin.json`
  - `section_anchors`: none
  - `artifact_id`: `claude_manifest`
  - `artifact_kind`: `config`
  - `artifact_path`: `.claude-plugin/plugin.json`
  - `section_anchors`: none
  - `artifact_id`: `cursor_manifest`
  - `artifact_kind`: `config`
  - `artifact_path`: `.cursor-plugin/plugin.json`
  - `section_anchors`: none
- `exclusive_write_scope`:
  - `path_glob`: `README.md`
  - `path_glob`: `docs/README.codex.md`
  - `path_glob`: `docs/README.claude.md`
  - `path_glob`: `docs/README.cursor.md`
  - `path_glob`: `.codex-plugin/plugin.json`
  - `path_glob`: `.claude-plugin/plugin.json`
  - `path_glob`: `.cursor-plugin/plugin.json`
  - `path_glob`: `docs/legacy/superpowers/working-briefs/2026-05-08-installation-risk-fixes-v1.md`
  - `path_glob`: `docs/legacy/superpowers/dispatch-plans/2026-05-08-installation-risk-fixes.md`
- `shared_read_scope`:
  - `path_glob`: `.opencode/INSTALL.md`
  - `path_glob`: `skills/**`
  - `path_glob`: `docs/maintainers/**`
- `depends_on_sections`: none
- `parallel_safe_with_sections`: none

## Persona And Workflow Guidance

- `recommended_personas`:
  - `staff engineer orchestrator`
  - `documentation workflow implementer`
  - `runtime policy reviewer`
- `persona_selection_notes`:
  - `staff engineer orchestrator` fits because the primary work is a bounded packaging-and-docs correctness pass
  - `documentation workflow implementer` should own the doc language fixes and the manifest path correction
  - `runtime policy reviewer` should verify that no install surface is overstated after the fix
- `workflow_bindings_by_stage`:
  - estimation and framing: `superpowers:brainstorming`
  - planning: `superpowers:writing-plans`
  - implementation execution: `superpowers:subagent-driven-development`
  - code and doc changes: `superpowers:test-driven-development`
  - review: `superpowers:requesting-code-review`
  - closure: `superpowers:verification-before-completion`
- `dispatch_recommendation`:
  - approve one bounded remediation round inside the current isolated worktree
  - complete the manifest and doc fixes before any branch-finishing step
  - accept the Codex GitHub subdirectory path only as a documented fallback, not as a default install route

## Runtime Preparation

- `required_for_goal_by_section`:
  - manifest-fix section: true
  - doc-alignment section: true
  - post-install-check section: true
  - final-review section: true
- `review_target_strategy`:
  - review the final integrated set of seven files together
  - prioritize user-facing install correctness over wording polish
- `controller_semantics_notes`:
  - this round is already isolated in a dedicated worktree
  - no new subagent packet should be launched until the user approves this dispatch round

## Rules

- Recommended personas are provisional until dispatch approval.
- Persona selection must cite the working brief, not just task keywords.
- The working brief is an analysis artifact, not the runtime approval record.
- No packet creation until the referenced dispatch plan is in `approved` state.
- If the user requests `Revise`, update the working brief only if the analysis changed, then issue a new brief version for the next dispatch plan revision.

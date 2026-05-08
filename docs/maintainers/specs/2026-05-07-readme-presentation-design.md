# README Presentation Redesign

**Date:** 2026-05-07

## Goal

Revise the repository root `README.md` so it feels clearer, more polished, and more human-friendly on GitHub while staying concise and working well for users of `Codex`, `Claude Code`, and similar agent-tool workflows.

## Problem

The current README is technically correct, but it reads more like an inventory than a polished entry point.

Current friction points:

- the opening does not immediately tell a reader why the skill matters
- compatibility with adjacent agent-tool workflows is implied rather than stated
- the section order puts repository details ahead of practical orientation
- the page is readable, but not especially lively or visually intentional for GitHub

GitHub README rendering is also limited. Custom fonts and robust color styling are not reliable, so the redesign should use only Markdown and GitHub-native presentation features.

## Scope

This redesign covers:

- the top-level structure of `README.md`
- the opening value proposition
- the placement and wording of compatibility guidance for `Codex`, `Claude Code`, and similar tools
- the ordering of sections so the page is skim-first
- light GitHub-native presentation improvements such as cleaner headings, callout blocks, and tighter section rhythm

This redesign does not cover:

- the skill runtime contract in `SKILL.md`
- the dispatch-plan template
- the workflow semantics of `$ww`
- custom fonts, custom CSS, or other GitHub-unreliable styling tricks
- a repo-wide documentation rewrite

## Design Principles

1. Lead with value, not inventory.
2. Make cross-tool compatibility explicit near the top.
3. Keep the README concise and skim-first.
4. Use GitHub-native structure for visual polish.
5. Separate user-facing guidance from maintainer-only material.

## Recommended Structure

The README should follow this rough order:

1. title and one-sentence value proposition
2. short compatibility note for `Codex`, `Claude Code`, and similar workflows
3. what the skill does in outcome-oriented language
4. how to install or copy it
5. repository contents and maintainer docs
6. validation and notes

The new structure should make it obvious within the first screen of text:

- what the skill does
- who it is for
- why it is worth using
- where the reader should go next

## Content Strategy

### Opening

Replace the current opener with a clearer statement of purpose. The new intro should sound like a product entry point, not a file catalog.

Preferred tone:

- concise
- technical
- confident
- a little more distinctive than the current copy

### Compatibility Note

Add a short compatibility callout near the top that says the skill works across `Codex`, `Claude Code`, and similar agent-tool workflows.

This note should:

- reassure users that the repo is not tool-locked
- stay short enough to preserve skim speed
- avoid overexplaining platform differences

### What This Skill Does

Rewrite the feature list to be more outcome-focused.

The section should emphasize:

- the disciplined `$ww` flow
- the working brief and dispatch plan
- orchestrator coordination
- reviewer and synthesis steps

The goal is to explain the value of the workflow before listing implementation details.

### Installation And Use

Keep installation guidance brief and practical.

Requirements:

- retain the current install paths and GitHub install references
- avoid burying the reader in platform-neutral boilerplate
- keep the section readable for users who already understand agent workflows

### Repository And Maintainer Material

Keep repository contents and maintainer docs, but push them later in the README so they do not dominate the first impression.

This material should feel like reference information rather than the main pitch.

## Visual Treatment

Use only GitHub-native, low-risk presentation techniques:

- tighter heading hierarchy
- one or two short blockquote/callout sections
- cleaner bullet rhythm
- careful spacing between sections

Do not use:

- custom fonts
- CSS hacks
- fragile color tricks
- badge-heavy decoration
- lengthy decorative prose

## Tone

The revised README should sound:

- cleaner than the current version
- a little more distinctive
- human-friendly without being casual
- well suited to experienced agent-tool users

It should not sound:

- flashy
- marketing-heavy
- tutorial-like
- overdesigned

## Non-Goals

- no functional changes to the skill
- no change to approval semantics
- no repo-wide doc restructuring
- no extra platform-specific guides
- no visual styling that depends on GitHub quirks

## Acceptance Criteria

The README redesign is successful if:

- a reader can understand what the skill does in the first screen
- compatibility with `Codex`, `Claude Code`, and similar workflows is clear
- the page feels more polished and readable on GitHub
- the section order supports quick scanning
- the README remains concise
- the wording stays technical and grounded

## Implementation Boundaries For The Later Edit

The eventual README edit should remain inside `README.md` only and should not modify skill behavior or other repository docs.


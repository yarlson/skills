# Agent instructions

This repo contains skills — reusable prompt-driven capabilities for AI coding agents.

## Rules

- Format all markdown before committing: `bunx prettier --write "**/*.md"`
- Update the skill table in `README.md` when adding or removing skills.

## Conventions

- **One directory = one skill.** Each skill lives in its own folder with a `SKILL.md` at the root.
- **Naming:** `kebab-case-skill-name/` for directories.
- **SKILL.md** is the skill definition — frontmatter (name, description, version) plus the full prompt.
- **README.md** in each skill directory — concise description and install command. Use this template:

````markdown
# <skill-name>

<One-paragraph description of what the skill does.>

## Install

```bash
npx skills add https://github.com/yarlson/skills/tree/main/<skill-name>
```
````

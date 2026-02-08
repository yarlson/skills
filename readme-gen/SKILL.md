---
name: readme-gen
description: This skill should be used when the user asks to "generate a readme", "write a readme", "create a README.md", "update the readme", "make a readme for this project", "readme for this repo", or mentions generating, writing, or improving a README file for a project or repository.
context: fork
---

# Generating a README

This skill explores a codebase, detects what kind of project it is, and writes a README that tells users what the project does, how to use it, and nothing else.

**Voice:** Write like someone who builds the thing AND sells the thing. Benefit-first — lead with what problem this solves, not what tech it uses. Concrete — real commands, real examples, no hand-waving. Punchy — every sentence earns its place. No "Welcome to...", no "This project aims to provide...", no badge walls, no emoji soup, no marketing fluff.

## Phase 1: Explore the codebase

Before writing a single line of README, understand what you're documenting. Read the code — don't guess from file names.

### 1.1 Detect project metadata

Look for these files (check all, not just the first match):

- `package.json`, `deno.json`, `bun.lock` — JS/TS ecosystem
- `Cargo.toml` — Rust
- `go.mod` — Go
- `pyproject.toml`, `setup.py`, `setup.cfg` — Python
- `Gemfile`, `*.gemspec` — Ruby
- `pom.xml`, `build.gradle`, `build.gradle.kts` — JVM
- `*.csproj`, `*.sln` — .NET
- `Makefile`, `Taskfile.yml`, `justfile` — build entry points
- `docker-compose*.yml`, `Dockerfile` — containerized
- `*.tf`, `*.hcl`, `terragrunt.hcl` — infrastructure

Extract: project name, version, description (if present), dependencies, scripts/commands, entry points.

### 1.2 Detect repo type

Classify the repo. This determines README structure.

| Signal                                                                                                                                               | Type                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `bin` field in package.json, `[[bin]]` in Cargo.toml, `main` package with flag parsing, CLI framework imports (commander, clap, cobra, click, oclif) | **CLI tool**            |
| Web framework imports (express, fastify, flask, django, gin, axum, rails), route definitions, `server.ts/js/py/go`                                   | **Web app / API**       |
| `exports` or `main` field with no `bin`, `lib.rs`, library-style public API, published to a registry                                                 | **Library / package**   |
| `workspaces` in package.json, `packages/` or `apps/` directories, Nx/Turborepo/Lerna config, multiple `go.mod` files                                 | **Monorepo**            |
| `Dockerfile` with no application code — just infra configs, Helm charts, Terraform modules                                                           | **Infrastructure**      |
| `ios/`, `android/`, React Native/Flutter/Expo config, `.xcodeproj`, `build.gradle` with Android SDK                                                  | **Mobile / native app** |
| GitHub Action `action.yml`, browser extension `manifest.json`, VS Code extension `package.json` with `contributes`                                   | **Plugin / extension**  |
| Notebooks (`.ipynb`), data pipeline configs, ML model files, training scripts                                                                        | **Data / ML**           |
| Markdown files only, no code, wiki-style structure                                                                                                   | **Documentation site**  |

A repo can be multiple types (e.g., monorepo containing a CLI + library). Handle the primary type, note the others.

### 1.3 Read the code

Don't write a README from metadata alone. Actually read:

1. **Entry points**: `main`, `index`, `app`, `cli`, `server` files — what does the project actually do when you run it?
2. **Public API surface**: exported functions, classes, routes, CLI commands — what can users interact with?
3. **Config and setup**: env vars, config files, database setup, required services — what does a user need to get started?
4. **Tests**: what do the test descriptions tell you about intended behavior?
5. **Existing README**: if one exists, read it. Understand what's there before replacing it. Preserve any content the user clearly wants to keep (contribution guides, licenses, etc.) unless told otherwise.
6. **CI/CD**: `.github/workflows`, `Makefile`, scripts — what are the standard commands?

### 1.4 Identify the user

Who is the reader of this README?

- **Library**: other developers who will `npm install` / `pip install` / `cargo add` this
- **CLI**: developers or end-users who will run this from a terminal
- **Web app**: developers who will clone, configure, and run this locally (or deploy it)
- **Monorepo**: contributors who need to navigate and understand the structure
- **Infrastructure**: DevOps/platform engineers who will apply/deploy this
- **Plugin**: users who will install and configure it in a host application

Write for THAT person. Not for the maintainer, not for a hiring manager, not for a conference talk.

## Phase 2: Write the README

### Structure by repo type

**CLI tool:**

```
# Project Name

> One-line tagline: what it does, for whom.

## Install

[exact install command — one line if possible]

## Usage

[2-3 most common commands with realistic examples]

## Commands

[table or list of all commands with one-line descriptions]

## Configuration

[config file format, env vars, flags — only if non-trivial]

## License
```

**Library / package:**

```
# Project Name

> One-line tagline: what problem it solves.

## Install

[exact install command]

## Quick start

[minimal working example — copy-paste-run, under 15 lines]

## API

[key functions/classes with signatures and one-line descriptions — not exhaustive, just the entry points]

## License
```

**Web app / API:**

```
# Project Name

> One-line tagline.

## Getting started

[clone, install deps, set up env, run — numbered steps, copy-paste commands]

## Environment variables

[table: name, description, required/optional, default]

## Development

[how to run locally, run tests, common tasks]

## Deployment

[how to deploy — only if not obvious]

## License
```

**Monorepo:**

```
# Project Name

> One-line tagline.

## What's in here

[table: package/app name → one-line description → path]

## Getting started

[prerequisites, initial setup, how to run/build across packages]

## Development

[common commands that work across the repo]

## License
```

**Infrastructure:**

```
# Project Name

> One-line tagline: what infrastructure this manages.

## Prerequisites

[required tools, credentials, access]

## Usage

[how to plan/apply/deploy, with exact commands]

## Architecture

[brief description of what gets created — optional diagram if complex]

## Configuration

[variables/inputs with descriptions]

## License
```

These are starting points. Adapt based on what the project actually needs. If a section would be empty or trivial, skip it. If the project needs a section not listed (e.g., "Migrating from v1"), add it.

### Writing rules

**Tagline:**

- One sentence. What does this do + for whom (if not obvious).
- Good: "Fast, opinionated code formatter for Python." / "CLI that generates conventional commits from staged diffs."
- Bad: "A next-generation, AI-powered, cloud-native solution for..." / "Welcome to ProjectName!"

**Install section:**

- One command. If multiple package managers, show the primary one first, alternatives on the next lines.
- Include the exact package name. `npm install foo` not "install the package using your preferred package manager."

**Examples:**

- Real, runnable code. Not pseudocode, not "// your code here."
- Show the most common use case first, not the most impressive one.
- Keep examples under 15 lines. If it takes more, the API might need work — but that's not the README's problem.

**Tables over prose:** for config vars, CLI flags, package lists. Scannable beats readable for reference content.

**Code blocks with language tags:** always. ` ```bash `, ` ```typescript `, etc. Never bare ` ``` `.

**No filler:**

- Remove "Please note that..." — just state the thing.
- Remove "In order to..." — just say "To..."
- Remove "It is important to..." — if it's important, it stands on its own.
- Remove "etc." — either list the things or don't.
- Remove any sentence that says what the project "aims to" do. Say what it does.

**No self-congratulation:**

- Don't say "elegant", "powerful", "simple yet flexible", "best-in-class."
- Let the code examples demonstrate quality. If you have to tell the reader it's simple, it isn't.

## Phase 3: Verify

Before presenting the README to the user:

1. **Every command must be real.** Check that install commands, run commands, and example code match actual project files. Don't invent flags, don't guess package names.
2. **Every file path must exist.** If you reference `src/index.ts`, verify it's there.
3. **The tagline must be accurate.** Re-read the entry point. Does the tagline actually describe what the code does?
4. **No orphan sections.** If a section has no content, remove it. Don't write "TODO" or "Coming soon."
5. **Read it as the target user.** Could someone clone this repo and get running using only the README? If not, what's missing?

## Decision Policy

- **ALWAYS** explore the codebase before writing. Never generate a README from the project name alone.
- **ALWAYS** read entry points and public API. The README describes what the code does, not what you imagine it does.
- **ALWAYS** verify every command and file path you reference.
- **ALWAYS** preserve existing content the user wants to keep — ask if unclear.
- **Ask before replacing**: if a README already exists with substantial content, confirm with the user before overwriting.
- **One README per invocation**: generate the root README. If the user needs sub-package READMEs (monorepo), do them one at a time.
- **Match the project's language**: if the codebase is in Python, show Python examples. If it's a shell tool, show shell examples. Don't mix.
- **Skip empty sections**: if the project has no configuration, don't add a Configuration section with "N/A."
- **Keep it short**: a good README is under 200 lines. If it's longer, you're probably including content that belongs in docs/ instead.

## Safety Rules

- **No secrets in output**: if you find API keys, tokens, or credentials while exploring, do not include them in the README. Use placeholder names (`YOUR_API_KEY`).
- **No invented features**: only document what the code actually does. If you're unsure whether a feature exists, read the code to confirm.
- **Read-only exploration**: do not modify any project files during the explore phase. Only write the README itself.

## Error Handling

- **Empty repo / no code**: tell the user there's nothing to document yet.
- **No package manifest**: determine project type from code structure and imports instead of metadata files.
- **Existing README with custom content**: don't silently overwrite. Show the user what you'd change and confirm.
- **Can't determine project type**: ask the user what the project is. Don't guess.
- **Massive monorepo**: focus on the root README. List packages/apps in a table with one-liners. Don't try to document each sub-project in the root README.

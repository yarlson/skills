# Memory Vault Skill — Reference

This document is loaded only when needed (deep rules, templates, lint patterns).

## A) INIT templates (copy exactly; fill later)

### `.memory/summary.md` template

Sections must exist even if short:

- What
- Architecture
- Core Flow
- System State
- Capabilities
- Tech Stack

Content rules:

- Present tense, current behavior
- No dates, no status/progress language

Suggested structure:

## What

- ...

## Architecture

- Components:
  - ...
- Boundaries:
  - ...

## Core Flow

- ...

## System State

- Operational properties / invariants:
  - ...

## Capabilities

- ...

## Tech Stack

- ...

### `.memory/terminology.md` template

Format:

- **Term:** definition (1–3 lines)
- Optional: "See also" links

### `.memory/practices.md` template

Format:

- **Rule:** ...
- **Rationale:** (optional, short)
- **Example:** (optional)

### `.memory/memory-map.md` template

Purpose: index of vault files.

Format:

- `- [summary.md](summary.md) — Project overview: what/architecture/flow/state/capabilities/stack`
- Group by domain folder:
  - `## auth/`
  - `- [auth/flow.md](auth/flow.md) — ...`

## B) Prohibited content heuristics (lint patterns)

Flag if any vault file contains:

- Dates like `YYYY-MM-DD`, `DD/MM/YYYY`, month names near numbers
- Commit-ish hashes: `\b[a-f0-9]{7,40}\b`
- Status headings: "Status", "Progress", "Next steps", "Remaining", "Blockers"
- Narrative incident framing: "we discovered", "after investigation", "good catch"
- Emojis (basic heuristic: non-ascii symbols in common emoji ranges)

False positives are acceptable; prefer strict.

## C) UPDATE mapping guide (diff → memory)

When you have a changed file list:

1. Cluster changes by domain (auth/api/infra/ui/data/etc.)
2. For each cluster:
   - find existing `.memory/<domain>/*.md` via memory-map or search
   - update current behavior bullets and examples
3. Only touch summary/practices/terminology if the change is durable and cross-cutting

## D) REORGANIZE rules

- Prefer stable domain names that match repo mental model
- Avoid deep nesting: `.memory/<domain>/<topic>.md` is usually enough
- Merge duplicates by keeping the clearer structure and moving unique details over
- After moves, update memory-map links

## E) COMPACT rules

Priority order:

1. Remove redundancy (move repeated rules to practices, repeated terms to terminology)
2. Split oversized files by topic
3. Replace paragraphs with bullets where safe
4. Keep at least one concrete example for non-obvious invariants

Never "summarize away" critical constraints.

## F) Manual lint checklist (if scripts not runnable)

- [ ] No dates / commits / status language inside `.memory/`
- [ ] Files stay current-state, present-tense
- [ ] One topic per file
- [ ] < ~250 lines per file (or intentionally split)
- [ ] memory-map indexes everything and links are relative
- [ ] summary.md contains required sections and matches reality

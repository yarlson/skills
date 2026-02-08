---
name: tui-design
description: Build clean, distinctive, production-ready Terminal UIs (TUIs) under terminal limits (monospace grid, fixed line height, limited styles). Use for screens, components, flows, and full TUI apps.
---

---

This skill helps make TUIs that look intentionally designed (not generic), using only what terminals support: spacing, alignment, borders, icons, and a small set of text attributes (color, bold, underline, reverse).

## 1) Decide first (always)

Before coding, write 3 lines:

- **Purpose**: what the app does and who uses it.
- **Aesthetic**: pick ONE: minimal / ops-console / retro / editorial / playful.
- **Signature**: one memorable thing (layout motif or interaction), e.g. “thin left rail + inspector”, “command palette”, “preview-on-focus”.

## 2) Layout = design

- Use a grid mindset: consistent **margins**, **gutters**, and **blank lines**.
- Prefer 2–3 regions max: header / main / footer (optional side panel).
- Handle small terminals: collapse side panel → stack vertically.

## 3) Hierarchy without font sizes

Use these, in order:

1. **Spacing** (blank lines, indentation)
2. **Alignment** (columns, right-aligned numbers)
3. **Rules** (`─` / `-`) and section titles
4. **Bold** for headings
5. **Reverse** for selection (sparingly)

## 4) Color rules (safe by default)

- Use **semantic tokens**, not random colors: `accent`, `muted`, `danger`, `warning`, `success`.
- Never rely on color alone: pair with text/icon (`✓ OK`, `! ERR`).
- Keep it tight: 1 accent + status colors.
- Provide fallbacks: truecolor → 256 → 16; Unicode borders → ASCII.

## 5) Keyboard-first interaction

- Focus must be obvious (caret `›` + highlight).
- Consistent keys:
  - move: arrows + `j/k` (optional)
  - switch panels: `tab` / `shift+tab`
  - open: `enter`
  - back/close/cancel: `esc`

- Footer shows contextual hints: `Enter Open • / Search • ? Help • q Quit`

## 6) States (must-have)

- **Loading**: show what’s happening (“Fetching…” + spinner/progress).
- **Empty**: explain what it is + show the next action (“Press a to add”).
- **Error**: short + actionable; allow “copy details” if possible.

## 7) Animation (use very little)

- Only for feedback: spinner/progress, brief flash on success.
- No large-area flicker; update only changed regions.

## 8) Avoid “generic TUI”

- Don’t border everything. Use borders only where structure helps.
- Don’t rainbow-paint. Keep one accent.
- Don’t ship 40 shortcuts. Start small; expose more via `?` help.

## Output expectations

When you generate code, include:

- theme tokens + fallbacks
- resize-safe layout
- clear focus/selection styling
- loading/empty/error handling
- one consistent signature motif (visual or interaction)

# Examples

## Example 1 — Micro-PRD (must not overslice)

### Input (abridged)

Single persona, one workflow:
"Admin invites one teammate by email; teammate accepts and can view dashboard."

### Expected behavior

- Complexity: Small
- Detect micro-PRD
- Output 1 slice spec (optional 2nd only if justified)
- Include rollout + telemetry
- STOP (no extra slicing)

---

## Example 2 — Phase-based PRD conversion

### Input pattern

Phases:

1. DB schema
2. Backend APIs
3. Frontend
4. Permissions
5. Analytics

### Expected behavior

- Reject phase decomposition style
- Build spine first
- Produce adaptive vertical slices each with user-visible outcomes
- Include phase→slice mapping in notes (optional extension)
- No tasks

---

## Example 3 — Debt-aware slicing

### Input pattern

PRD requires quick integration with legacy service likely needing temporary adapter.

### Expected behavior

- Slice spec includes temporary seam note
- Debt ledger entry present with measurable payoff
- If risk non-trivial, add stabilization slice (measurable outcome)
- No generic "refactor later"

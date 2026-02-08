# Reference: PRD → Adaptive Vertical Slices (with Tech Debt Prevention)

## Mission

Turn PRDs into adaptive, architecture-safe vertical slice plans:

- thin but real,
- user-visible,
- sequenced by value/risk,
- resistant to ball-of-mud drift.

## Hard bans

- No tasks/subtasks/tickets.
- No component/layer phases (UI/API/DB).
- No platform-first slices with no customer value.
- No fixed "N slices" quota.
- No slicing micro-PRDs beyond 1–2 slices.
- No "shared/common" junk module as a shortcut.
- No temporary seams without debt ledger and payoff.

---

## Workflow (must follow in order)

## Step 0 — Qualify input and establish guardrails

### 0.1 PRD size estimate

Return:

- `complexity_level`: Small | Medium | Large | Huge
- `why`: 3–6 bullets
- `slice_count_range`:
  - Small: 2–4
  - Medium: 4–7
  - Large: 7–12
  - Huge: 12–20

Use as guidance, never as a quota.

### 0.2 Micro-PRD detection

If PRD has one primary workflow + one persona + can ship in one slice (two max):

- return "micro-sized; do not slice further" behavior,
- output one slice spec (max two),
- include minimal rollout + telemetry,
- stop.

### 0.3 Architecture & debt guardrails (concise but mandatory)

Output:

1. Draft module/bounded-context map (3–8 modules).
2. Architecture invariants (5–8):
   - allowed dependency direction,
   - public contract-only cross-module calls,
   - data ownership by one module per core entity,
   - no shared/common without strict justification,
   - contract changes logged (ADR-lite).
3. Enforcement hooks (3–6):
   - no forbidden imports,
   - no dependency cycles,
   - public API boundaries enforced,
   - ownership checks.

---

## Step 1 — Extract spine (happy path)

Identify a single primary journey maximizing time-to-value.
Output 5–10 steps max.
If many workflows exist, choose one spine and note secondary ones.

---

## Step 2 — Outcomes, assumptions, constraints, debt traps

Output:

- top user outcomes (5–10),
- top assumptions/unknowns (5–10),
- constraints to thin slices,
- debt traps to avoid (3–7), e.g.:
  - multi-owner writes on same entity,
  - ad-hoc sync/async integration mix,
  - permanent flags,
  - copy-paste workflow divergence.

---

## Step 3 — Generate adaptive slice candidates

Stop when all are true:

- spine is end-to-end shippable,
- key risks addressed early,
- remaining work is expansion/completeness, not foundational uncertainty.

Each slice must map to spine step or meaningful milestone.

## Required Slice Spec fields

- `slice_name`
- `user_outcome`
- `primary_persona`
- `owning_module`
- `touched_modules` (minimal + reason)
- `in_scope` (3–7)
- `out_of_scope` (3–7 explicit)
- `constraints` (2–5)
- `end_to_end_surface`:
  - `ui_ux_changes`
  - `api_contract_changes`
  - `data_state_changes` (with owner)
  - `permissions_authz_changes`
  - `telemetry_observability`
- `architecture_notes`:
  - how boundary rule is respected,
  - ACL/adapter needed? yes/no + one line,
  - temporary seam? if yes include debt entry.
- `failure_modes_fallback` (2–5)
- `rollout_plan` (flag + rollback)
- `success_metrics` (2–4 measurable)
- `key_risks_reduced`

## Debt Ledger rule

If temporary seam exists, include:

- `debt`
- `why`
- `risk`
- `payoff` (named future slice + measurable completion)

No generic "refactor later".

## Stabilization slice rule

Only allowed when measurable outcomes exist:

- remove temp adapter,
- delete old flag path,
- reduce incident/error rate,
- eliminate boundary violations.

Still a slice, never a task list.

---

## Step 4 — Sequence by Value × Risk × GTM

Score each slice (1–5):

- customer_value_now
- learning_value
- technical_risk_reduction
- gtm_enablement

Then sequence:

- first: walking skeleton + high risk/value,
- middle: expansion + reliability,
- late: completeness/enterprise/scale polish.

Also include:

- demo checkpoint after each slice,
- audience by stage (internal/design partners/beta/GA),
- stability gate after each slice.

---

## Step 5 — Cross-cutting requirements plan

For each concern (auth, audit, i18n, perf, etc.):

- first introducing slice (minimal),
- expansion slices later,
- ownership model (single owner or explicit shared governance).

No standalone "build RBAC platform" slice.

---

## Step 6 — Final deliverables (required order)

1. PRD size estimate + slice range
2. Architecture guardrails
3. Spine journey
4. Sequenced slice specs
5. Score table
6. Top 3 risks mapped to slices
7. Debt ledger + stabilization slices (if any)
8. Slice Definition of Done

---

## Slice Definition of Done (must include)

A slice is done only if:

- end-to-end user outcome exists,
- behind feature flag with rollback path,
- authz boundaries enforced where relevant,
- telemetry exists for success/failure,
- failure modes have safe fallback,
- architecture invariants respected,
- debt avoided or explicitly recorded with payoff,
- demoable without "not wired yet" caveats.

---

## Style contract

- Direct, structured, no fluff.
- Thin-but-real slices.
- No task decomposition leakage.
- No arbitrary slice count forcing.
- Micro-PRD rule enforced strictly.

# SaaS Site Design — Reference

Detailed phase instructions, design token specs, component definitions, page layout templates, interaction inventory, and verification checklists loaded on demand. See `SKILL.md` for the workflow overview and decision policy.

## Phase 1: Ingest Content + Brand Context — Full Detail

### 1.1 What to extract from marketing site content

From the `marketing-site-gen` output, extract and organize:

- **Page inventory** — every page generated, with paths, page type (homepage, product, feature, use case, pricing, docs landing), and buyer's journey stage
- **Section structure per page** — ordered list of sections within each page (hero, problem, solution, how-it-works, social proof, CTA, etc.) with approximate content length per section
- **CTA strategy** — primary CTA text, secondary CTAs per page type, CTA placement rules
- **Content hierarchy** — what's the most important message per page, what's supporting, what's tertiary. This directly informs visual weight distribution
- **Cross-linking plan** — how pages connect to each other and to the help system. Informs navigation design and in-page link styling
- **Proof points and trust elements** — testimonials, logos, metrics, technical claims. These need dedicated visual treatment

### 1.2 What to extract from surface map

From the `product-surface-map` output, extract:

- **Product type** — what the product is (CLI tool, web app, API, platform, marketplace)
- **Complexity** — number of feature areas, depth distribution, integration count
- **User types** — who uses this product (developers, business users, mixed)
- **Technical stack** — informs design tool recommendations and component feasibility

### 1.3 Product archetype detection

Detect the product archetype from the surface map and marketing content. The archetype informs default design direction when no brand context exists:

| Archetype        | Default direction                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Dev tool**     | Dark mode default, monospace accents, code-block prominence, terminal aesthetic, high contrast, minimal decoration            |
| **Business app** | Light mode default, clean sans-serif, dashboard previews, professional palette (blues/neutrals), generous whitespace          |
| **Platform**     | Dual mode, bold typography, ecosystem visualization, vibrant accent colors, modular grid, integration-forward                 |
| **Marketplace**  | Light mode default, card-heavy layout, search prominence, social proof density, warm palette, community elements              |
| **API/infra**    | Dark mode default, technical typography, endpoint/schema previews, minimal UI, developer trust signals, documentation-forward |

### 1.4 Brand context intake

If the user provides brand context, extract:

- **Colors** — primary, secondary, accent. Check contrast ratios against WCAG AA before adopting.
- **Fonts** — headings, body. Check availability (system, Google Fonts, licensed). Note license requirements.
- **Logo** — dimensions, color variants (light/dark background), minimum clear space.
- **Brand guidelines** — tone (playful/serious/technical), shape language (rounded/sharp), visual density preference.
- **Existing site** — if redesigning, note what to preserve vs. change.

If no brand context is provided, generate defaults from the product archetype table above. Note in the output that these are defaults for customization.

### 1.5 What to do if inputs are incomplete

| Missing input             | Action                                                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| No marketing site content | Ask if the user wants to run `marketing-site-gen` first (recommended). Accept a rough page list and section outline as fallback. |
| No surface map            | Ask if the user wants to run `product-surface-map` first. If they provide a product description, infer archetype but warn.       |
| No brand context          | Generate from archetype defaults. Flag all brand tokens as "default — customize to your brand."                                  |
| Conflicting brand + a11y  | Flag the conflict explicitly. Provide accessible alternatives alongside brand originals. Recommend the accessible version.       |
| Very large marketing site | Design template system rather than bespoke per-page layouts. Focus on homepage + one feature + one use case as exemplars.        |

## Phase 2: Design System — Full Detail

### 2.1 Design principles

Derive three core design principles from the trio. These guide every subsequent decision:

1. **Strategic clarity** (Strategist) — every visual choice is a bet on what matters most. The layout hierarchy solves the problem we set out to solve — getting visitors to understand and act. Cut visual complexity that doesn't earn its weight. Table-stakes patterns where they belong, differentiated design where it counts.

2. **Conversion flow** (Closer) — visual hierarchy exists to drive action. The most important element on every viewport is the next step the visitor should take. Layout, color, size, and contrast all serve the "try → buy" path. Can a visitor explain what this product does after seeing just the hero?

3. **Buildable simplicity** (Wirer) — every design choice must be implementable end-to-end with standard tools, maintainable by a small team, and performant on real devices. No designs that look done in Figma but collapse in code. Fewer components, consistent patterns, no one-off effects.

### 2.2 Typography system

**Scale** — use a modular scale (e.g., 1.250 major third or 1.333 perfect fourth). Define sizes in rem for accessibility.

| Token     | Role                | Size (rem) | Weight  | Line height | Usage                                    |
| --------- | ------------------- | ---------- | ------- | ----------- | ---------------------------------------- |
| `display` | Hero headlines      | 3.5–4.5    | 700–800 | 1.1         | One per page, above the fold             |
| `h1`      | Page/section titles | 2.5–3      | 700     | 1.2         | Section openers                          |
| `h2`      | Subsection heads    | 1.75–2     | 600–700 | 1.25        | Feature names, step headers              |
| `h3`      | Card/block titles   | 1.25–1.5   | 600     | 1.3         | Card headings, list item titles          |
| `body`    | Paragraph text      | 1–1.125    | 400     | 1.6         | All body content                         |
| `small`   | Supporting text     | 0.875      | 400     | 1.5         | Captions, metadata, fine print           |
| `caption` | Labels, badges      | 0.75       | 500     | 1.4         | Tags, status indicators, navigation meta |

**Font pairing guidance:**

- **Dev tool / API**: monospace for code + geometric sans for UI (e.g., JetBrains Mono + Inter)
- **Business app**: humanist sans for warmth (e.g., Source Sans 3 + system sans)
- **Platform**: geometric sans for headings + humanist for body (e.g., Outfit + Source Sans 3)
- **Marketplace**: rounded sans for approachability (e.g., Nunito + Inter)

Use open-source or system fonts as defaults. Note any license requirements if specifying proprietary alternatives.

**Bold headline patterns (2026 trend):** Display-size headlines should be confident and oversized. Use 700–800 weight. Short headlines (2–6 words) at display size create visual impact. Longer headlines drop to h1 size. Never use display size for sentences longer than ~10 words.

### 2.3 Color system

Define a complete palette with semantic mappings and dark mode variants.

**Core palette structure:**

| Token              | Role                          | Light mode              | Dark mode              |
| ------------------ | ----------------------------- | ----------------------- | ---------------------- |
| `primary`          | Brand color, primary CTA      | User-defined or default | Adjusted for dark bg   |
| `primary-hover`    | CTA hover state               | 10% darker              | 10% lighter            |
| `primary-subtle`   | Backgrounds, highlights       | 95% lightened           | 10% opacity on dark bg |
| `secondary`        | Secondary actions, accents    | User-defined or default | Adjusted for dark bg   |
| `accent`           | Highlights, badges, emphasis  | User-defined or default | Adjusted for dark bg   |
| `neutral-900`      | Primary text                  | Near-black              | Near-white             |
| `neutral-700`      | Secondary text                | Dark gray               | Light gray             |
| `neutral-500`      | Tertiary text, borders        | Medium gray             | Medium gray            |
| `neutral-200`      | Dividers, subtle borders      | Light gray              | Dark gray              |
| `neutral-50`       | Page background               | Near-white              | Near-black             |
| `surface`          | Card/component backgrounds    | White                   | Elevated dark          |
| `surface-elevated` | Modals, dropdowns, sticky nav | White + shadow          | Lighter dark + shadow  |
| `success`          | Positive states, checkmarks   | Green                   | Green (adjusted)       |
| `warning`          | Caution states                | Amber                   | Amber (adjusted)       |
| `error`            | Error states, destructive     | Red                     | Red (adjusted)         |
| `info`             | Informational highlights      | Blue                    | Blue (adjusted)        |

**Contrast requirements:**

- Normal text on background: minimum 4.5:1 (WCAG AA)
- Large text (≥18px bold or ≥24px) on background: minimum 3:1
- Interactive elements: minimum 3:1 against adjacent colors
- Test every color combination in both light and dark modes

**Archetype default palettes:**

- **Dev tool**: primary slate-blue (`#3B82F6`), accent emerald (`#10B981`), neutrals cool gray, dark mode default
- **Business app**: primary indigo (`#4F46E5`), accent sky (`#0EA5E9`), neutrals warm gray, light mode default
- **Platform**: primary violet (`#7C3AED`), accent amber (`#F59E0B`), neutrals neutral, dual mode
- **Marketplace**: primary teal (`#14B8A6`), accent rose (`#F43F5E`), neutrals stone, light mode default

### 2.4 Spacing system

**Base unit:** 4px (0.25rem). All spacing is a multiple of the base unit.

| Token | Value | Usage                                     |
| ----- | ----- | ----------------------------------------- |
| `xs`  | 4px   | Inline spacing, icon gaps                 |
| `sm`  | 8px   | Tight component padding, related elements |
| `md`  | 16px  | Default component padding, list gaps      |
| `lg`  | 24px  | Section internal padding, card padding    |
| `xl`  | 32px  | Between component groups                  |
| `2xl` | 48px  | Between page sections (mobile)            |
| `3xl` | 64px  | Between page sections (tablet)            |
| `4xl` | 96px  | Between page sections (desktop)           |
| `5xl` | 128px | Hero section vertical padding             |

**Section spacing rhythm:** Consistent vertical spacing between major page sections creates visual rhythm. Use `2xl`–`4xl` depending on viewport. Tighter spacing groups related sections; wider spacing signals topic change.

### 2.5 Grid system

| Property    | Mobile (<640px) | Tablet (640–1024px) | Desktop (>1024px) |
| ----------- | --------------- | ------------------- | ----------------- |
| Columns     | 4               | 8                   | 12                |
| Gutter      | 16px            | 24px                | 32px              |
| Margin      | 16px            | 32px                | auto (centered)   |
| Max content | 100%            | 100%                | 1280px            |
| Max text    | 100%            | 640px               | 720px             |

**Breakpoints:**

| Name | Value  | Usage            |
| ---- | ------ | ---------------- |
| `sm` | 640px  | Tablet portrait  |
| `md` | 768px  | Tablet landscape |
| `lg` | 1024px | Desktop          |
| `xl` | 1280px | Wide desktop     |

### 2.6 Shadow & depth

| Token         | Value                          | Usage                              |
| ------------- | ------------------------------ | ---------------------------------- |
| `shadow-sm`   | `0 1px 2px rgba(0,0,0,0.05)`   | Subtle card edges, input fields    |
| `shadow-md`   | `0 4px 6px rgba(0,0,0,0.07)`   | Cards, raised components           |
| `shadow-lg`   | `0 10px 15px rgba(0,0,0,0.1)`  | Dropdowns, popovers                |
| `shadow-xl`   | `0 20px 25px rgba(0,0,0,0.1)`  | Modals, elevated panels            |
| `shadow-glow` | `0 0 20px rgba(primary, 0.15)` | CTA hover emphasis (use sparingly) |

Dark mode: increase opacity by 50% and use black-based shadows. Add subtle border (1px `neutral-200`) on elevated surfaces in dark mode to compensate for lost shadow visibility.

### 2.7 Border radius & shape language

| Token         | Value  | Usage                             |
| ------------- | ------ | --------------------------------- |
| `radius-sm`   | 4px    | Badges, tags, small inputs        |
| `radius-md`   | 8px    | Buttons, cards, input fields      |
| `radius-lg`   | 12px   | Large cards, sections, modals     |
| `radius-xl`   | 16px   | Feature panels, hero elements     |
| `radius-full` | 9999px | Pills, avatars, circular elements |

**Shape language by archetype:**

- **Dev tool**: sharper radii (`radius-sm` default), angular, precise
- **Business app**: medium radii (`radius-md` default), balanced
- **Platform**: larger radii (`radius-lg` default), modern, approachable
- **Marketplace**: rounded (`radius-lg`–`radius-xl` default), friendly, soft

### 2.8 Trio review of design system

| Voice      | Check                                                                                        |
| ---------- | -------------------------------------------------------------------------------------------- |
| Strategist | Is the design system tight — no tokens we won't use? Does the palette bet on the right mood? |
| Closer     | Does the color system make CTAs the most prominent element? Is the primary color ownable?    |
| Wirer      | Are there fewer than 20 unique tokens? Can this map to Tailwind/CSS variables cleanly?       |

## Phase 3: Components + Page Layouts — Full Detail

### 3.1 Component Specs

#### Navigation Bar

- **Layout**: sticky top, full-width, blurred background on scroll
- **Contents**: logo (left), nav links (center or right), primary CTA button (right)
- **Behavior**: shrinks from `lg` padding to `md` padding on scroll. Background transitions from transparent to `surface-elevated` with backdrop blur
- **Nav links**: maximum 6 items. Keep minimal — Home, Product, Features, Use Cases, Pricing, Docs
- **CTA**: always visible, uses `primary` color, stands out from nav links
- **Mobile**: hamburger menu. CTA remains visible outside the menu
- **Trio**: Closer — CTA never scrolls away. Strategist — nav labels match the buyer's journey. Wirer — sticky + backdrop-filter is well-supported, keep DOM simple

#### Hero Section

- **Layout**: full-width, vertically centered, generous padding (`5xl` top/bottom)
- **Primary variant (story-driven)**: display headline (left or centered) + subheadline + primary CTA + secondary CTA + hero visual (right or below)
- **Split-screen variant**: problem statement (left) + solution/visual (right), 50/50 split on desktop, stacked on mobile
- **Headline**: display size, 700–800 weight, maximum 10 words. Captures the core value in a narrative frame — not a feature description but a story hook
- **Subheadline**: h2 size or body-lg, 1–2 sentences expanding who it's for and what changes
- **CTAs**: primary button (high contrast, large) + secondary link or ghost button
- **Visual**: product screenshot, illustration, or animated demo placeholder. Right-aligned on desktop for left-to-right reading flow (headline → visual)
- **Trio**: Closer — CTA is the most prominent element after the headline. Strategist — headline tells a story, not a feature. Wirer — hero image lazy-loads, CTA is above the fold on all viewports

#### Feature Card

- **Layout**: icon or visual (top) + headline (h3) + description (body, 2–3 lines) + link
- **Size**: works in 2-column (tablet), 3-column (desktop), 1-column (mobile) grids
- **Icon**: 32–48px, uses `primary` or `accent` color
- **Hover**: subtle lift (`shadow-md` → `shadow-lg`), optional scale (1.02)
- **Trio**: Closer — card headline is benefit-first. Strategist — cards tell a mini problem→solution story. Wirer — consistent height via flexbox, no fixed heights

#### CTA Block

- **Primary variant**: full-width background (`primary` or `primary-subtle`), centered headline (h2) + supporting text + large primary CTA button
- **Secondary variant**: inline within content flow, smaller, uses `surface` background with border
- **Placement rules**: primary CTA block at bottom of every page. Secondary CTA block after first major content section
- **Button sizing**: minimum 48px height (touch target), generous horizontal padding (`lg`–`xl`)
- **Trio**: Closer — CTA block is unmissable, high contrast, specific action text. Strategist — supporting text connects to the page narrative. Wirer — no more than 2 CTA blocks per page to avoid banner blindness

#### Trust Bar

- **Layout**: horizontal row of logos, badges, or metrics. Full-width, subtle background (`neutral-50` or `surface`)
- **Logo display**: grayscale by default, color on hover. 6–8 logos max, consistent height (32–40px)
- **Badge variant**: security badges, compliance icons, award logos
- **Metrics variant**: 3–4 key numbers in large display text (e.g., "10k+ users", "99.9% uptime") — only if verifiable
- **Placement**: immediately below the hero section (builds trust early) and/or above the final CTA
- **Trio**: Closer — trust signals before the visitor considers leaving. Strategist — metrics tell a proof story. Wirer — logos are optimized SVGs, lazy-loaded if below fold

#### Pricing Table

- **Layout**: side-by-side plan cards (2–4 plans). Highlighted/recommended plan is visually elevated
- **Card structure**: plan name (h3) + price (display size) + billing period + feature list (checkmarks) + CTA button
- **Highlighted plan**: `primary` border or background tint, `shadow-lg`, "Most popular" badge
- **Feature comparison**: toggle between card view and full comparison table. Table is scrollable on mobile
- **FAQ section below**: accordion or stacked list. Questions framed as buying objections
- **Trio**: Closer — recommended plan is the visual focal point, CTA on every plan card. Strategist — plan names tell a progression story (Starter → Pro → Enterprise). Wirer — responsive without horizontal scroll, comparison table uses sticky first column

#### Testimonial Block

- **Layout**: quote text (body-lg or h3 italic) + attribution (name, role, company) + photo or company logo
- **Variants**: single large quote (hero placement), 2–3 column card grid, carousel (only if >3)
- **Quote styling**: large opening quotation mark as decorative element (using `primary-subtle` color), quote text in slightly larger size
- **Carousel**: only if more than 3 testimonials. Auto-advance disabled (accessibility). Navigation via dots or arrows
- **Trio**: Closer — testimonials appear before the pricing section. Strategist — quotes selected for story, not just praise. Wirer — carousel is optional enhancement, grid is the fallback

#### Interactive Demo Placeholder

- **Layout**: full-width or contained section with prominent border/frame. Aspect ratio 16:9 or 4:3
- **Contents**: embed area (iframe-ready) with fallback — static screenshot + "Try the demo" overlay button
- **Fallback pattern**: screenshot with semi-transparent overlay + play/interact icon + CTA to launch demo
- **Loading state**: skeleton placeholder with subtle pulse animation
- **Trio**: Closer — demo is conversion gold, prominent CTA to engage. Strategist — demo is placed at the "proof" stage of the narrative. Wirer — iframe sandbox attributes, loading=lazy, fallback guaranteed for no-JS

#### Use Case Card

- **Layout**: persona icon or illustration (top/left) + headline (h3): persona + desired outcome + challenge summary (body, 2–3 lines) + "See how" link
- **Content pattern**: "[Persona] needs to [goal]. Challenge: [pain point]. [Product] enables [outcome]."
- **Grid**: 2-column (desktop), 1-column (mobile). Cards are equal height
- **Trio**: Closer — card links to full use case page (deeper in funnel). Strategist — persona is recognizable to the buyer. Wirer — card links are real, equal-height via flexbox

#### Integration Grid

- **Layout**: grid of integration logos with hover detail. 4-column (desktop), 3-column (tablet), 2-column (mobile)
- **Logo display**: uniform size (48–64px), grayscale default, color on hover
- **Hover detail**: tooltip or expanded card showing integration name + one-line description
- **Categories**: group by type if >12 integrations (e.g., "Data sources", "Messaging", "Cloud")
- **Trio**: Closer — integration count is social proof. Strategist — organized by buyer mental model. Wirer — SVG logos, lazy-loaded, no layout shift on hover

#### Footer

- **Layout**: full-width, dark or contrasting background. Multi-column on desktop, stacked on mobile
- **Contents**: column 1 — logo + tagline + social links. Columns 2–4 — nav groups (Product, Resources, Company). Bottom row — legal links + copyright
- **CTA**: optional email capture or final CTA button above the footer columns
- **Community elements**: Slack/Discord invite link, GitHub star count, forum link — if relevant
- **Trio**: Closer — last chance CTA before the visitor leaves. Strategist — footer nav mirrors the site story. Wirer — semantic HTML, accessible link contrast on dark background

#### Section Dividers

- **Purpose**: create visual rhythm between page sections. Signal topic transitions
- **Patterns**: generous whitespace (primary method), subtle horizontal rule, background color alternation (white → `neutral-50` → white), angled/curved section breaks (use sparingly)
- **Background alternation**: alternate between `neutral-50` and `surface` (or white) to group related sections and visually separate distinct topics
- **Trio**: Closer — rhythm keeps the visitor scrolling. Strategist — transitions pace the narrative. Wirer — CSS-only, no images for dividers

### 3.2 Page Layout Specs

Each layout is described as a wireframe-in-markdown: section order, grid usage, component placement.

#### Homepage Layout

```
┌─────────────────────────────────────────────┐
│ Navigation Bar (sticky)                     │
├─────────────────────────────────────────────┤
│ Hero Section (story-driven)                 │
│ ┌──────────────────┬──────────────────────┐ │
│ │ Headline         │ Product visual       │ │
│ │ Subheadline      │ (screenshot/demo)    │ │
│ │ [Primary CTA]    │                      │ │
│ │ [Secondary CTA]  │                      │ │
│ └──────────────────┴──────────────────────┘ │
├─────────────────────────────────────────────┤
│ Trust Bar (logos / metrics)                 │
├─────────────────────────────────────────────┤
│ Problem → Solution (split-screen)           │
│ ┌──────────────────┬──────────────────────┐ │
│ │ The problem      │ The solution         │ │
│ └──────────────────┴──────────────────────┘ │
├─────────────────────────────────────────────┤
│ How It Works (3–4 step visual)              │
│ ┌─────────┬─────────┬─────────┐             │
│ │ Step 1  │ Step 2  │ Step 3  │             │
│ └─────────┴─────────┴─────────┘             │
├─────────────────────────────────────────────┤
│ Feature Highlights (3-col feature cards)    │
│ ┌─────────┬─────────┬─────────┐             │
│ │ Card 1  │ Card 2  │ Card 3  │             │
│ └─────────┴─────────┴─────────┘             │
├─────────────────────────────────────────────┤
│ Use Cases (2-col use case cards)            │
│ ┌──────────────────┬──────────────────────┐ │
│ │ Use case 1       │ Use case 2           │ │
│ └──────────────────┴──────────────────────┘ │
├─────────────────────────────────────────────┤
│ Social Proof (testimonials — conditional)   │
├─────────────────────────────────────────────┤
│ CTA Block (primary, full-width)             │
├─────────────────────────────────────────────┤
│ Footer                                      │
└─────────────────────────────────────────────┘
```

**Trio review:**

- Closer: CTA visible at 3 scroll positions (hero, mid-page, bottom). Trust bar immediately after hero
- Strategist: flow is problem → solution → how → what → who → proof → action. Is this the right bet on section order?
- Wirer: 7 section types, all reusable components, no custom one-offs

#### Product Overview Layout

```
┌─────────────────────────────────────────────┐
│ Navigation Bar                              │
├─────────────────────────────────────────────┤
│ Hero (headline + product narrative)         │
├─────────────────────────────────────────────┤
│ Capability Table (feature areas as cards)   │
│ ┌─────────┬─────────┬─────────┐             │
│ │ Area 1  │ Area 2  │ Area 3  │             │
│ ├─────────┼─────────┼─────────┤             │
│ │ Area 4  │ Area 5  │ Area 6  │             │
│ └─────────┴─────────┴─────────┘             │
├─────────────────────────────────────────────┤
│ How It Works (architecture overview)        │
│ ┌─────────────────────────────────────────┐ │
│ │ Architecture diagram / flow visual      │ │
│ └─────────────────────────────────────────┘ │
├─────────────────────────────────────────────┤
│ Differentiators (3–4 col cards)             │
├─────────────────────────────────────────────┤
│ Integration Grid                            │
├─────────────────────────────────────────────┤
│ CTA Block                                   │
├─────────────────────────────────────────────┤
│ Footer                                      │
└─────────────────────────────────────────────┘
```

#### Feature Page Layout (template — applied per feature)

```
┌─────────────────────────────────────────────┐
│ Navigation Bar                              │
├─────────────────────────────────────────────┤
│ Breadcrumb                                  │
├─────────────────────────────────────────────┤
│ Hero (feature name + problem statement)     │
├─────────────────────────────────────────────┤
│ Challenge Section (the pain point)          │
├─────────────────────────────────────────────┤
│ Solution — Capability Cards (2-col)         │
│ ┌──────────────────┬──────────────────────┐ │
│ │ Capability 1     │ Capability 2         │ │
│ ├──────────────────┼──────────────────────┤ │
│ │ Capability 3     │ Capability 4         │ │
│ └──────────────────┴──────────────────────┘ │
├─────────────────────────────────────────────┤
│ Interactive Demo Placeholder                │
├─────────────────────────────────────────────┤
│ Under the Hood (technical detail)           │
├─────────────────────────────────────────────┤
│ Related Features (horizontal card row)      │
├─────────────────────────────────────────────┤
│ CTA Block                                   │
├─────────────────────────────────────────────┤
│ Footer                                      │
└─────────────────────────────────────────────┘
```

#### Use Case Page Layout (template)

```
┌─────────────────────────────────────────────┐
│ Navigation Bar                              │
├─────────────────────────────────────────────┤
│ Breadcrumb                                  │
├─────────────────────────────────────────────┤
│ Hero (persona + desired outcome)            │
├─────────────────────────────────────────────┤
│ Challenge Section (before state)            │
│ ┌──────────────────┬──────────────────────┐ │
│ │ Before (pain)    │ After (with product) │ │
│ └──────────────────┴──────────────────────┘ │
├─────────────────────────────────────────────┤
│ Step-by-Step Solution (vertical timeline)   │
│ ┌─ Step 1 ─────────────────────────────── │ │
│ ├─ Step 2 ─────────────────────────────── │ │
│ ├─ Step 3 ─────────────────────────────── │ │
│ └─ Outcome ────────────────────────────── │ │
├─────────────────────────────────────────────┤
│ Results (metrics / outcomes)                │
├─────────────────────────────────────────────┤
│ Features Used (table with links)            │
├─────────────────────────────────────────────┤
│ Testimonial (relevant to this use case)     │
├─────────────────────────────────────────────┤
│ CTA Block                                   │
├─────────────────────────────────────────────┤
│ Footer                                      │
└─────────────────────────────────────────────┘
```

**Use case specific notes:**

- Before/after split-screen is a 2026 pattern. Use contrasting background tints (muted for "before", vibrant for "after")
- Step-by-step uses a vertical timeline component (left border with dots/icons at each step)
- Testimonial should be relevant to this specific use case if available

#### Pricing Page Layout

```
┌─────────────────────────────────────────────┐
│ Navigation Bar                              │
├─────────────────────────────────────────────┤
│ Breadcrumb                                  │
├─────────────────────────────────────────────┤
│ Hero (pricing philosophy headline)          │
├─────────────────────────────────────────────┤
│ Plan Toggle (monthly / annual — if needed)  │
├─────────────────────────────────────────────┤
│ Pricing Cards (side-by-side)                │
│ ┌──────────┬────────────┬──────────┐        │
│ │ Plan 1   │ Plan 2 ★   │ Plan 3   │        │
│ │          │ (featured) │          │        │
│ │ [CTA]    │ [CTA]      │ [CTA]    │        │
│ └──────────┴────────────┴──────────┘        │
├─────────────────────────────────────────────┤
│ Feature Comparison Table (expandable)       │
├─────────────────────────────────────────────┤
│ Trust Bar (security, compliance)            │
├─────────────────────────────────────────────┤
│ FAQ (objection handling)                    │
├─────────────────────────────────────────────┤
│ CTA Block (final conversion push)           │
├─────────────────────────────────────────────┤
│ Footer                                      │
└─────────────────────────────────────────────┘
```

**Pricing specific notes:**

- Transparent pricing is a 2026 trust signal. No "Contact us" for pricing unless genuinely custom
- Trust bar here focuses on security and compliance, not customer logos
- FAQ is objection handling — questions are phrased as buyer concerns

#### Docs Landing Layout

```
┌─────────────────────────────────────────────┐
│ Navigation Bar                              │
├─────────────────────────────────────────────┤
│ Breadcrumb                                  │
├─────────────────────────────────────────────┤
│ Hero (minimal — "Documentation" + search)   │
├─────────────────────────────────────────────┤
│ Getting Started (prominent card/banner)     │
├─────────────────────────────────────────────┤
│ Guide Grid (categorized links)              │
│ ┌─────────┬─────────┬─────────┐             │
│ │Features │ How-to  │Reference│             │
│ │ guide 1 │ guide 1 │ API     │             │
│ │ guide 2 │ guide 2 │ CLI     │             │
│ │ ...     │ ...     │ Config  │             │
│ └─────────┴─────────┴─────────┘             │
├─────────────────────────────────────────────┤
│ Community / Support (links)                 │
├─────────────────────────────────────────────┤
│ Footer                                      │
└─────────────────────────────────────────────┘
```

### 3.3 Trio Review per Component and Layout

Run this checklist for every component and page layout:

| Voice      | Component check                                                         | Layout check                                                             |
| ---------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Strategist | Is this component earning its place — does it move the visitor forward? | Does the page flow follow problem → solution → proof → action?           |
| Strategist | What should we cut from this component to ship faster?                  | Is progressive disclosure achieved through visual weight, not just text? |
| Closer     | Is the CTA the most visually prominent element?                         | Is a CTA visible at every scroll position?                               |
| Closer     | Do trust signals appear early (above the fold or immediately after)?    | Does the layout hierarchy match conversion priority?                     |
| Wirer      | Is this one of fewer than 10 unique component patterns?                 | Can this layout be built with a standard 12-column grid?                 |
| Wirer      | Does it work at all breakpoints without hacks?                          | Are there fewer than 3 custom breakpoint behaviors?                      |

## Phase 4: Interaction Design + Verify — Full Detail

### 4.1 Micro-Animation Inventory

Every animation must be purposeful — it guides attention, provides feedback, or creates narrative continuity. No decoration-only motion.

#### Scroll-Triggered Section Reveals

- **Effect**: sections fade in + slide up (20px) as they enter the viewport
- **Trigger**: IntersectionObserver at 15% visibility threshold
- **Duration**: 400–600ms
- **Easing**: ease-out (CSS `cubic-bezier(0.0, 0.0, 0.2, 1)`)
- **Stagger**: if multiple items (e.g., feature cards), stagger entry by 100ms per item
- **Reduced-motion**: instant appearance, no slide or fade

#### CTA Hover States

- **Primary CTA**: scale to 1.02 + `primary-hover` background + `shadow-glow` on hover. Transition 200ms ease
- **Secondary CTA**: underline slide-in or color shift. Transition 150ms ease
- **Focus state**: 2px outline offset in `primary` color (keyboard navigation visibility)
- **Active state**: scale to 0.98 (press feedback). Transition 100ms

#### Navigation Scroll Behavior

- **Trigger**: scroll position > hero section height
- **Effect**: nav background transitions from transparent to `surface-elevated` with backdrop-blur(12px). Padding shrinks from `lg` to `md`. Logo shrinks subtly (if applicable)
- **Duration**: 200ms ease
- **Reduced-motion**: instant background change, no size transition

#### Feature Card Hover

- **Effect**: card lifts (translateY -4px) + shadow deepens (`shadow-md` → `shadow-lg`)
- **Duration**: 200ms ease
- **Optional**: icon color shifts from `neutral-500` to `primary`
- **Reduced-motion**: color shift only, no movement

#### Number/Metric Counters

- **Effect**: numbers count up from 0 to target value when entering viewport
- **Trigger**: IntersectionObserver at 50% visibility
- **Duration**: 1500–2000ms
- **Easing**: ease-out (fast start, slow finish for dramatic effect)
- **Format**: use locale-appropriate number formatting, add suffix animating after count completes ("+", "k", "%")
- **Reduced-motion**: display final number immediately, no counting

#### Page Transitions

- **Between pages**: simple crossfade (opacity 0 → 1), 200ms. Only if using a SPA framework
- **Within page**: smooth scroll to anchor targets, 300ms ease
- **Reduced-motion**: instant navigation, no crossfade

### 4.2 Performance Budget

All design choices must fit within this performance budget:

| Metric           | Target          | Justification                                                 |
| ---------------- | --------------- | ------------------------------------------------------------- |
| LCP              | < 2.5s          | Core Web Vitals "good" threshold                              |
| CLS              | < 0.1           | No layout shift from lazy-loaded images or fonts              |
| INP              | < 200ms         | All interactions respond within one frame budget              |
| Total JS         | < 100KB gzipped | Animation library + analytics + essentials only               |
| Total CSS        | < 50KB gzipped  | Design system + component styles                              |
| Hero image       | < 200KB         | Optimized WebP/AVIF, responsive srcset                        |
| Font files       | < 100KB total   | 2 fonts max, subset to Latin, woff2 format                    |
| Animation frames | 60fps target    | CSS transforms/opacity only — no layout-triggering properties |

**Animation-specific rules:**

- Only animate `transform` and `opacity` — never animate `width`, `height`, `top`, `left`, `margin`, or `padding`
- Use `will-change` sparingly and only on elements that are about to animate
- Prefer CSS animations over JavaScript for simple effects
- Use IntersectionObserver for scroll triggers, not scroll event listeners
- Total simultaneous animations: maximum 5 elements animating at once

### 4.3 Responsive Verification

For each page layout, verify behavior at three breakpoints:

#### Mobile (<640px)

- Single column layout for all content
- Navigation collapses to hamburger menu; CTA remains visible
- Hero: headline (h1 size, not display) + CTA stacked vertically, visual below or hidden
- Feature cards: single column, full-width
- Pricing cards: stacked vertically, swipeable optional
- Trust bar: logos wrap to 2 rows or become scrollable
- Touch targets: minimum 48px height, 8px gap between adjacent targets
- No horizontal scroll on any element

#### Tablet (640–1024px)

- Two-column layout for cards and grids
- Navigation: full nav visible if ≤6 items, otherwise hamburger
- Hero: headline + CTA left, visual right (or centered single-column)
- Feature cards: 2-column grid
- Pricing cards: side-by-side (2 visible, third scrolls or stacks)
- Trust bar: single row, logos may be smaller

#### Desktop (>1024px)

- Full grid (12-column) layout
- All components at maximum width within `max-content` container
- Hero: split layout (text left, visual right) or centered with visual below
- Feature cards: 3-column grid
- Pricing cards: 3+ side-by-side
- Trust bar: single row, full-size logos

### 4.4 Accessibility Check

Every component and page must pass:

| Check               | Requirement                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------- |
| Color contrast      | 4.5:1 for normal text, 3:1 for large text and UI elements. Test in both light and dark modes             |
| Focus states        | Every interactive element has a visible focus indicator (2px outline, `primary` color, 2px offset)       |
| Reduced motion      | All animations respect `prefers-reduced-motion: reduce`. Provide instant alternatives                    |
| Screen reader       | All images have alt text. Decorative images use `alt=""`. Section landmarks use semantic HTML            |
| Keyboard navigation | All interactive elements reachable via Tab. Logical tab order follows visual layout                      |
| Touch targets       | Minimum 48x48px for all interactive elements on mobile                                                   |
| Text scaling        | Layout doesn't break at 200% browser zoom. Rem-based sizing supports user font preferences               |
| Link purpose        | Link text describes destination (no "click here"). Links to external sites indicate they open externally |
| Heading hierarchy   | No skipped heading levels. One h1 per page. Sections use proper heading nesting                          |

### 4.5 Trio Final Review

Before finalizing the design spec:

| Voice      | Final check                                                                                                                  |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Strategist | Does this design solve the problem we set out to solve? Is the core visual loop tight? What should we cut?                   |
| Strategist | Is there a consistent emotional arc across all pages? Does progressive disclosure work visually?                             |
| Closer     | Does every viewport have a clear conversion path? Is the CTA always the most visually prominent interactive element?         |
| Closer     | Do trust signals appear within the first scroll? Is above-the-fold optimized for the 30-second decision?                     |
| Wirer      | Can the entire design be implemented in under a week with Tailwind or equivalent? Are there fewer than 10 unique components? |
| Wirer      | Does every animation stay within the performance budget? Does responsive behavior work without media query hacks?            |

## Output Structure

The complete design spec is a single markdown document with this structure:

```
design/
  design-spec.md
    ├── 1. Design Principles (trio-derived)
    ├── 2. Design Tokens
    │     ├── Typography
    │     ├── Colors (light + dark)
    │     ├── Spacing
    │     ├── Grid
    │     ├── Shadows
    │     └── Border Radius
    ├── 3. Components
    │     ├── Navigation Bar
    │     ├── Hero Section
    │     ├── Feature Card
    │     ├── CTA Block
    │     ├── Trust Bar
    │     ├── Pricing Table
    │     ├── Testimonial Block
    │     ├── Interactive Demo Placeholder
    │     ├── Use Case Card
    │     ├── Integration Grid
    │     ├── Footer
    │     └── Section Dividers
    ├── 4. Page Layouts
    │     ├── Homepage
    │     ├── Product Overview
    │     ├── Feature Page (template)
    │     ├── Use Case Page (template)
    │     ├── Pricing Page
    │     └── Docs Landing
    ├── 5. Interaction Design
    │     ├── Animation Inventory
    │     └── Performance Budget
    ├── 6. Responsive Strategy
    │     ├── Mobile
    │     ├── Tablet
    │     └── Desktop
    ├── 7. Accessibility Requirements
    └── 8. Trio Final Sign-Off
```

Every section in the spec is self-contained. A developer can implement any component or page layout by reading its section alone, referencing the design tokens section for values.

# Onyx design system specification

**Version:** 0.1 · **Position:** Carbon-compatible theme and extension layer

Onyx makes serious tools feel like working surfaces: considered, legible and exact. It inherits Carbon's discipline—not its corporate visual idiom. The result is neither a reskin nor a new component library: it is a stable semantic layer, visual grammar and set of extensions that can sit over Carbon or guide another accessible component implementation.

## 1. Design principles

1. **Structure before surface.** Make relationships visible through alignment, sequence, typography, spacing and rules before introducing containers or colour.
2. **Colour communicates state.** Signal Orange identifies agency, current position and action; functional colours carry only their named meanings.
3. **Dense, never cramped.** Prefer compact, scannable working views with stable rhythms, direct labels and persistent context.
4. **Evidence stays visible.** Sources, timestamps, state, provenance, uncertainty and units are first-class content, not tooltip residue.
5. **Quietly technical.** Use precise type, warm tonal hierarchy and instrument-like detail; avoid nostalgia, spectacle and generic SaaS polish.
6. **Carbon behavior is a contract.** Preserve accessible names, target sizes, keyboard operation, validation behavior, responsive reflow and component semantics.

## 2. Relationship to Carbon

| Carbon system | Onyx decision | Rationale |
| --- | --- | --- |
| Role-based tokens, themes, layers | Retain | Values change by theme; semantic role never changes. |
| 2× grid and spacing scale | Retain | Provides a tested alignment and density discipline. |
| Component anatomy, states, keyboard/ARIA behavior | Retain | Appearance may not weaken task completion or accessibility. |
| IBM gray palette and blue values | Replace | Warm Onyx neutrals and Signal Orange establish the new material character. |
| Productive IBM Plex Sans type | Replace | Archivo gives the interface a sharper editorial working voice. |
| Component tokens | Adapt | Keep scope and naming logic while adding Onyx component values. |
| Focus, validation, notifications, status meanings | Retain/adapt | Preserve behavior; map values to accessible Onyx ramps. |
| Research notes, sources, annotations, reading views | Extend | These are recurring jobs outside Carbon's generic product core. |

Use a current Carbon component whenever one fits. Wrappers may add `onyx-*` slots or compose primitives, but must not hide labels, alter tab order, remove live-region behavior, or substitute an icon for a required text label.

## 3. Colour architecture

### Reference palette

| Family | Values | Usage |
| --- | --- | --- |
| Neutral | Paper `#FAFAF8`, Mist `#F2F2EF`, Ash 20 `#E2E2DE`, Ash 30 `#CACAC5`, Ash 50 `#8C8C86`, Charcoal `#4A4A46`, Graphite `#333330`, Onyx `#20201E`, Jet `#0D0D0C`, Black `#000000` | All surfaces, text, rules and disabled states. Black is exceptional: high-contrast print/export or a deliberate mark only. |
| Action | Orange `#E34A21`, strong `#B83B1A`, hover `#F15B32`, soft `#F9DED5` | Action, current/selected position, focus in light mode, actionable emphasis. |
| Success | Green `#198754`, strong `#12683F`, bright `#47B882`, soft `#D9F0E4` | Confirmed completion or valid state. |
| Warning | Amber `#D89B00`, strong `#875F00`, bright `#F2BD3A`, soft `#FFF0C7` | Attention requiring interpretation or action. |
| Error | Red `#C9362B`, bright `#E5655C`, soft `#F8DDDA` | Destructive action, invalid input, failed operation. |
| Information | Blue `#246BCE`, bright `#6AA8FF`, soft `#DCE9FA` | Neutral explanatory or system information. |

Base Orange is a **surface/indicator** value in light mode, not small text on Paper. Use Orange Strong for light-theme links, focus and textual actions. Base Amber is also never small light-theme text; use Amber Strong. In dark mode use the bright variants for functional text and marks.

### Functional usage

- Never colour a whole page or large panel with a signal/functional colour.
- Pair a status colour with a direct label, icon/shape or message. A status dot alone is insufficient.
- Selected is primarily a tonal surface change plus an Orange 2px leading rule or Orange text/icon—not a full orange fill.
- Visited links use `--onyx-link` with a 1px underline; they may be distinguished by a muted underline/secondary text treatment, never a new purple family.

## 4. Semantic token mapping and implementation

Reference tokens are immutable values; semantic tokens are the only values components consume; component tokens are scoped aliases. The token JSON and CSS in this package are canonical examples.

| Carbon token | Onyx semantic token | Semantic role |
| --- | --- | --- |
| `background` | `onyx.surface.canvas` | Application canvas |
| `layer`, `layer-01`, `layer-02` | `onyx.surface.layer.01`, `.02` | Ordered raised/content regions |
| `field` | `onyx.surface.field` | Form/control fill |
| `border-subtle`, `border-strong` | `onyx.border.subtle`, `.strong` | Rules and control boundaries |
| `text-primary`, `text-secondary` | `onyx.text.primary`, `.secondary` | Content hierarchy |
| `interactive`, `button-primary` | `onyx.action.primary` | Primary interactive affordance |
| `link-primary` | `onyx.link` | Navigational inline/standalone link |
| `focus`, `focus-inset` | `onyx.focus.ring`, `.inset` | Keyboard/voice navigation indicator |
| `support-*` | `onyx.status.*` | Functional status communication |

Naming follows `onyx.{category}.{role}[.{variant}]`. CSS uses the equivalent `--onyx-{category}-{role}[-{variant}]`; Carbon aliases use `--cds-*`. New component tokens must use `onyx.{component}.{part}.{state}`, for example `onyx.table.header.background` and `onyx.notification.error.border`. Do not expose raw hex values from components.

## 5. Themes and surfaces

| Role | Light | Dark |
| --- | --- | --- |
| Canvas | Paper | Jet |
| Layer 01 | Mist | Onyx |
| Layer 02 / control | Paper | Graphite |
| Hover / selected | Ash 20 | Charcoal |
| Subtle / strong rule | Ash 20 / Ash 30 | Graphite / Charcoal |
| Primary / secondary text | Onyx / Charcoal | Mist / Ash 50 |
| Disabled | Ash 30 fill, Ash 50 label | Graphite fill, Charcoal label |

Light layers alternate Paper/Mist, following Carbon's light-layer principle without cool gray. Dark layers rise one step from Jet to Onyx to Graphite. A region earns elevation only when it changes task context—menu, dialog, popover, temporary inspector—not merely to decorate grouped content.

## 6. Typography

Use `Archivo` for interfaces and reading, `Archivo Narrow` for dense labels/navigation and `IBM Plex Mono` for values, identifiers, time, code and system output. Use normal tabular numerals for tables and values (`font-variant-numeric: tabular-nums lining-nums`).

| Role | Face / weight | Size / leading | Tracking and use |
| --- | --- | --- | --- |
| Display | Archivo 600 | 42/48px | -0.02em; rare: document title or major workspace orientation |
| H1 | Archivo 600 | 32/40px | -0.015em; page/task title |
| H2 | Archivo 600 | 24/32px | -0.01em; principal section |
| H3 | Archivo 600 | 18/24px | 0; content group |
| H4 | Archivo 600 | 16/22px | 0; local grouping |
| Body | Archivo 400 | 16/26px | 0; sustained reading, max 72ch |
| Body compact | Archivo 400 | 14/20px | 0; application copy, max 80ch |
| Label | Archivo Narrow 600 | 14/16px | 0.02em; controls and navigation |
| Overline / index | Archivo Narrow 600 | 12/16px | 0.07em; uppercase only for codes/section index |
| Metadata | Plex Mono 400/500 | 12/18px | 0; timestamps, source IDs, values |
| Data dense | Plex Mono 500 | 13/16px | 0; tables, metrics and instrument readouts |
| Caption | Archivo 400 | 12/18px | 0.01em; figure/source context |

Use sentence case by default. Avoid 300 weight below 18px. Do not use all-caps prose; codes and compact navigational index labels are the only default exception. On small screens, step Display to 32/40px and H1 to 28/36px; do not scale body below 14px.

## 7. Spacing, grid and composition

The 4px base and Carbon 2× scale are retained: `4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160, 192px`. Never invent one-off gaps.

- Use a 4-column narrow grid (16px margins/16px gutters), 8-column medium grid (24px margins/24px gutters), and 16-column wide grid (32px margins/32px gutters). At wide viewports, content regions may cap at 1600px but reading columns cap at 72ch.
- Establish vertical rhythm with 16px between directly related elements, 24–32px between groups, and 48–64px between major sections.
- Let repeated labels, values, controls and headings share edges. Break the grid only for a genuine reading or analysis need, such as a full-width data plot.
- Preserve DOM and keyboard order when columns collapse. Tables remain horizontally scrollable with the first identifying column sticky rather than shrinking into illegibility.

## 8. Borders, radii and elevation

Rules are 1px and use `border.subtle` for separation or `border.strong` for control boundaries. Use 2px only for focus, current-position rules and selected anchors. Controls have a 2px radius; sheets, tables and content sections have 0px radius. Pills are limited to compact tags, counts and filters where their bounded state is clear.

Default elevation is none. Menus, popovers and modals may use one restrained shadow: `0 8px 24px rgb(13 13 12 / 18%)` in light and `0 12px 32px rgb(0 0 0 / 45%)` in dark. No shadow is used to suggest ordinary grouping.

## 9. Interaction, focus and motion

- **Hover:** shift neutral surfaces one token toward contrast; primary action uses Orange Hover. Hover never conveys essential state.
- **Pressed:** Orange Strong for primary buttons; a 1px text/icon shift is permitted only if it does not move layout.
- **Selected/current:** selected neutral surface plus Orange leading rule, orange icon/text, or both. Keep the active state visible without hover.
- **Focus:** a continuous 2px `focus.ring`; where it could merge with an Orange surface, add a 1px `focus.inset`. It must pass 3:1 against adjacent colours and never be removed.
- **Disabled:** remove from tab order when native semantics require it; no hover/focus states; explain a blocked prerequisite where omission would confuse.

Motion is short and explanatory: 70ms micro-feedback, 150ms expansion/selection, 240ms dialogs/panels. Use Carbon productive easing. Animate opacity, transform or clip only; never use bounce, glow, looping attention effects or motion as the sole status cue. Respect `prefers-reduced-motion` by reducing nonessential motion to zero and preserving state changes.

## 10. Iconography

Use Carbon icons as the default set so metaphors, sizing and accessibility remain familiar. Icons are 16px in controls and 20px in key navigation; use 24px only for a clear empty-state or status marker. Stroke/filled variants must be consistent within a context. Pair unfamiliar or destructive icons with visible text; icon-only controls require accessible names and tooltips. Icons inherit text/status colour—never act as decoration.

## 11. Core component adaptations

| Carbon component | Onyx treatment | Behavior retained |
| --- | --- | --- |
| Button | Square/2px form, explicit verb, one Orange primary action per decision region; secondary is rule/text-led. | Variants, loading, disabled and keyboard activation. |
| Text input/select | Mist/Graphite field with bottom or full 1px strong rule; labels stay visible above. | Labels, helper/error text, validation timing, native semantics. |
| Checkbox/radio/toggle | Orange marks selected state; use labels to explain choice. | Hit targets, grouped semantics, keyboard behavior. |
| Tabs | Dense narrow labels, baseline rule; current tab receives Orange 2px indicator. | Arrow-key navigation and selected semantics. |
| Side navigation | Fixed, indexed, dense; hierarchy via indentation and rules, not tiles. | Disclosure, current location and responsive behavior. |
| Overflow menu | Flat list, 1px rules only where grouping clarifies; mono shortcuts aligned right. | Menu focus management and escape behavior. |
| Modal/popover | Onyx/Mist context layer with only genuine elevation; task title, concise body, explicit actions. | Focus trap, return focus, escape/close behavior. |
| Notification | Status colour on 2px leading rule/icon, not a coloured card. | Inline/live-region behavior, dismissal and action links. |
| Empty state | Direct statement, next action, optional 24px meaningful icon; no illustration by default. | Action accessibility and responsive reflow. |

## 12. Navigation and content hierarchy

Navigation creates orientation before choice. Place product identity, current workspace and stable primary sections in the shell; use breadcrumb only for genuine nested location. Use an `01 / 02` style index only where order is meaningful, never as ornamental numbering. Utility actions live in a consistent right-side/overflow area and never compete with the page's primary action.

Pages begin with a compact location/context line, then a task title and concise status/metadata. In research and document contexts, let title, author/source, date/state and primary action align to the same grid rather than sit in a hero card.

## 13. Forms

Group inputs by decision, not field type. Place labels above fields; helper text below and visible whenever it changes successful completion. Present errors near the field and summarize them at the form start after submission. Use 16px field-to-field spacing, 24px group spacing, and 32px before final action areas. Avoid placeholders as labels, segmented forms without reason, and pill toggles for binary decisions requiring careful reading.

## 14. Tables and dense information

Tables are a primary Onyx surface. Use aligned columns, quiet header rules, compact 40px rows (32px only for read-only high-density views) and 48px rows when editing. Headers use Archivo Narrow; values use Plex Mono with tabular figures. Right-align quantitative values, align decimals when comparison matters, and put units in the header. Keep row actions on a predictable final column. Selection applies a neutral fill plus Orange marker, never orange-filled rows. Preserve sorting, filtering, batch actions, responsive scroll and accessible summaries from Carbon.

## 15. Notifications and status

Use inline notifications for local form/task outcomes; use toasts only for asynchronous, transient confirmation. Status copies describe what happened, its consequence and the next action where applicable. Success, warning, error and info use the semantic status tokens with text/icon/rule redundancy. Destructive confirmation requires a clearly labeled destructive action and an escape/cancel path; red is not used for ordinary emphasis.

## 16. Data visualisation

Chart structure begins with a stated question, title, unit, time scope, source and caveat. Use neutral axes/rules and reserve Signal Orange for the active series, current datum or user selection; never make all data orange. Functional colours retain their semantic meaning in health/status charts. Default ordered-series sequence: Mist/Charcoal/Orange Strong/Blue/Green/Amber/Red, with patterns/labels for non-colour distinction. Provide a table or textual summary for screen readers and preserve data points/tooltips for keyboard use. Avoid gradients, 3D treatment, chart-card grids and unlabelled axes.

## 17. Editorial and knowledge-work patterns

- **Reading/document view:** 45–75ch body column; a quiet metadata rail at wide sizes that returns inline before content on narrow screens.
- **Provenance block:** source title, author/organisation, publication/access date, stable identifier/URL, extraction method and confidence. Use mono for IDs/dates and a subtle top rule.
- **Annotation:** anchored marker plus visible note panel/footnote; show author, timestamp and status. Do not rely on hover to expose notes.
- **Research card:** use only for a portable record; it is a bordered sheet with metadata, not a soft container.
- **Analytical workspace:** persistent context sidebar, central working canvas and optional inspectable detail pane. Panels share grid edges and state; no arbitrary dashboard tiles.
- **Diagram:** use rectilinear connectors, labelled nodes, a source/legend and a clear reading direction. Neutral nodes, Orange only for active path/selection, functional colours only for semantic states.

## 18. Accessibility requirements

Meet WCAG 2.2 AA as a minimum: 4.5:1 normal text, 3:1 large text/UI/focus graphics, 44×44px touch targets where feasible, visible keyboard focus, semantic landmarks, logical heading order, language metadata, labelled controls and screen-reader announcements for async updates. Test at 200% zoom and narrow viewports without loss of task completion. Do not communicate state by colour, hover, motion, position or icon alone. Respect forced colours, high contrast and reduced motion. Dense mode may reduce whitespace, never core text size, hit targets, contrast or labels.

## 19. Cross-product identity rules

Every product uses the Onyx neutral system, semantic status meanings, font roles, spacing scale, focus shape, Carbon icons, rule-led surfaces and direct sentence-case content. Products may tune: density mode, grid composition, a constrained product identifier (wordmark/index convention), editorial template and optional non-semantic instrument accent for noninteractive diagrams only. Products may not introduce a competing primary colour, rounded-card language, custom focus colour, alternate status meanings or decorative gradient/shadow system.

## 20. Correct and incorrect application

| Correct | Incorrect |
| --- | --- |
| An active research tab uses a Mist surface, Orange 2px baseline and direct text label. | Every tab is an orange pill. |
| A report page uses aligned title, source metadata, readable column and rules. | A large hero title sits inside a floating card with decorative icons. |
| A table makes units explicit, aligns figures and retains row actions. | Metrics are scattered across unlabelled dashboard tiles. |
| A warning uses Amber Strong text, label and icon on a quiet soft surface. | Amber text is placed directly on Paper or a warning is indicated by colour alone. |
| A modal appears only for a constrained task and returns focus on close. | Standard sections are framed in elevated, shadowed panels. |

## 21. Implementation checklist

1. Import the requested fonts with stable fallbacks and apply the `onyx-theme--light` or `onyx-theme--dark` root class.
2. Consume semantic/component tokens only; reference tokens are not used in components except at the theme-definition layer.
3. Keep Carbon component markup and state behavior. Override aliases and scoped component tokens rather than style selectors where practical.
4. Run `python3 scripts/validate-contrast.py` and test focus, keyboard paths, zoom, forced colours and reduced motion in the consuming application.

## 22. Token architecture summary

```text
onyx.color.neutral.paper                 # reference value
onyx.color.signal.orange-strong          # reference value
onyx.surface.canvas                      # semantic role, theme-specific
onyx.text.primary                        # semantic role, theme-specific
onyx.action.primary                      # semantic role, theme-specific
onyx.status.warning                      # semantic role, theme-specific
onyx.table.header.background             # component role
onyx.button.primary.background.hover     # component state
--onyx-surface-canvas                    # CSS alias
--cds-background                         # Carbon compatibility alias
```

Do not add synonyms for an existing role. Add a component token only when a recurring component-specific distinction cannot be expressed by a semantic token. Theme changes assign values, not new meanings.

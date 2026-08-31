# Onyx design system

Onyx is a Carbon-compatible design language for research, learning design, knowledge work and technical tools. It keeps Carbon's component behaviours and semantic-token structure while replacing its visual foundation with warm neutrals, editorial typography and instrument-like information hierarchy.

## Package

- `SPECIFICATION.md` is the authoritative usage and component specification.
- `tokens/onyx.tokens.json` contains reference and semantic design tokens.
- `css/onyx.css` exposes the themes and Carbon-compatible aliases as CSS custom properties.
- `scripts/validate-contrast.py` verifies the specified critical colour pairs.

The package is framework-neutral. In a Carbon React implementation, load `css/onyx.css` after the Carbon theme CSS and map the documented aliases at the application theme boundary; do not replace Carbon markup, accessible labels, ARIA behaviour, keyboard interactions or component state machines.

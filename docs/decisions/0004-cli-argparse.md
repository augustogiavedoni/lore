# ADR 0004: CLI with argparse

- Status: accepted
- Date: 2026-11-11

## Context

Lore has no frontend; all interaction is through a CLI with a few
subcommands (`ingest`, `ask`, `eval`, later possibly `serve-mcp`).

## Options considered

1. **argparse** (standard library): no dependency, explicit, verbose.
2. **Typer**: subcommands from type hints, nicer help; extra dependency
   (on top of Click) and some magic.
3. **Click**: mature decorators; extra dependency; typing with mypy strict is
   less comfortable.

## Decision

**argparse.** Three or four subcommands do not justify a dependency, and the
CLI is a thin layer over the package, not where learning happens.

## Consequences

- Positive: zero dependencies; fully typed with mypy; nothing to learn.
- Negative: more boilerplate; no shell completion or rich help out of the
  box.
- Revisit if: the CLI grows past a handful of subcommands or needs
  interactive features.

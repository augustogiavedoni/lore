# ADR 0003: Embeddings backend

- Status: proposed (decide in M1)
- Date: 2026-11-11

## Context

M1 embeds every chunk and every question. The model fixes the vector
dimension stored in pgvector, so changing it later means re-embedding the
whole corpus. Evals in CI (M2) will embed questions on every run.

## Options

1. **OpenAI-compatible `/embeddings` endpoint** behind Lore's own interface
   (same pattern as chat). Works with hosted APIs or local servers (e.g.
   Ollama). Costs per token if hosted; needs network in CI unless faked.
2. **Local sentence-transformers.** No API, no cost, reproducible offline.
   Adds torch (large) to dependencies and slows CI.
3. **A dedicated embeddings provider SDK** (e.g. Voyage, Cohere). Often
   better retrieval quality; vendor-specific API and another key.

## Decision

Pending. To be decided at the start of M1. Whatever is chosen, the model
name and dimension are stored with the vectors so a mismatch is detected.

## Consequences

To be written with the decision.

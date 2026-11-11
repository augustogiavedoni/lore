# Evals

Question sets used to measure Lore. The code that runs them lives in
`src/lore/evals/`; this folder holds only data. Results of runs go to
`evals/runs/` (git-ignored).

> Status: only two illustrative examples. Writing the real set (~30
> questions) is milestone M0 (see `docs/roadmap.md`).

## Files

- `examples.jsonl`: two illustrative records showing the format. Their
  `source_ids` refer to documents that do not exist yet.
- `dataset.jsonl` (M0): the real eval set.

## Format

JSON Lines: one JSON object per line, no comments, UTF-8.

| Field | Type | Meaning |
|---|---|---|
| `question` | string | What the user asks, phrased as a real user would. |
| `expected_answer` | string | Reference answer, short. For unanswerable questions, describe the expected behaviour (e.g. say the information is not available). |
| `source_ids` | list of strings | Corpus `id`s that contain the answer. Empty when `answerable` is `false`. |
| `role` | string | Role asking the question. Retrieval must only use documents this role may see. |
| `answerable` | boolean | Whether the answer is in the documents **visible to `role`**. A question answered only by a restricted document is `false` for a role without access. |

## What a good set covers

- Questions answered by one document and by combining several.
- Questions with no answer in the corpus (the assistant must not invent one).
- The same question asked by two roles with different access (one
  answerable, one not): this is the leak test for M4.
- Questions affected by outdated or contradictory documents.
- Paraphrases that do not share keywords with the source (vector search
  should help) and exact terms like codes or names (keyword search should
  help; see M3).

"""Eval runner.

Responsibility:
    Run every question in an eval set through Lore and compute metrics:
    retrieval (does it find the expected ``source_ids``?), answer quality
    (LLM-as-judge from M2), refusals on unanswerable questions, and no leaks
    across roles. Output a single summary number plus per-question details.

Must NOT:
    - Use eval answers or ``source_ids`` as hints at query time.
    - Write results inside the repo outside ``evals/runs/`` (git-ignored).
"""

# TODO(augusto): implement the eval runner.

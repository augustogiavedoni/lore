"""Eval dataset loading.

Responsibility:
    Read the JSONL eval set (``question``, ``expected_answer``,
    ``source_ids``, ``role``, ``answerable``) into typed records and reject
    malformed lines with a clear error (file and line number).

Must NOT:
    - Silently drop invalid lines.
"""

# TODO(augusto): implement dataset loading and validation.

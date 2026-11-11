"""Answering.

Responsibility:
    Call the chat provider with the prompt and return an answer with the
    ``source_ids`` it cites. Say "I don't know" when the retrieved context
    does not support an answer.

Must NOT:
    - Return citations to sources that were not in the retrieved context.
    - Know about a specific vendor (use the provider interface).
"""

# TODO(augusto): implement answer generation with citations.

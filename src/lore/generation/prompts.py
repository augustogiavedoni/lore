"""Prompts.

Responsibility:
    Build the messages sent to the chat model: instructions, the question,
    and retrieved chunks clearly delimited as untrusted data with their
    source ids.

Must NOT:
    - Merge document text into the system instructions.
    - Include chunks the role is not allowed to see.
"""

# TODO(augusto): design the prompts.

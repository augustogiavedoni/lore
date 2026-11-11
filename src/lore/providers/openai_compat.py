"""OpenAI-compatible chat provider.

Responsibility:
    Implement the chat interface for any endpoint that speaks the OpenAI
    chat completions API, and translate SDK exceptions into Lore's errors.

Must NOT:
    - Retry on its own (retries, if any, live in one place above it).
    - Log request bodies, headers or API keys.
"""

# TODO(augusto): implement the OpenAI-compatible chat provider.

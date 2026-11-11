"""Smoke test: the package and its modules import."""

import importlib

import pytest

MODULES = [
    "lore",
    "lore.config",
    "lore.ingest.documents",
    "lore.ingest.chunking",
    "lore.ingest.pipeline",
    "lore.retrieval.store",
    "lore.retrieval.search",
    "lore.generation.prompts",
    "lore.generation.answer",
    "lore.providers.base",
    "lore.providers.openai_compat",
    "lore.providers.embeddings",
    "lore.auth.roles",
    "lore.interfaces.cli",
    "lore.evals.dataset",
    "lore.evals.runner",
]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name: str) -> None:
    assert importlib.import_module(name) is not None

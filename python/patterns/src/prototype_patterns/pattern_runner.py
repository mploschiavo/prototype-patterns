"""Pattern registry and helpers for running demos one at a time."""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from typing import Callable

from prototype_patterns.behavioral import (
    chain_of_responsibility,
    command,
    iterator,
    mediator,
    memento,
    observer,
    state,
    strategy,
    template_method,
)
from prototype_patterns.creational import (
    abstract_factory,
    builder,
    factory_method,
    lazy_initialization,
    object_pool,
    prototype,
    singleton,
)
from prototype_patterns.structural import (
    adapter,
    bridge,
    composite,
    composite_entity,
    decorator,
    facade,
    flyweight,
    proxy,
)

PatternDemo = Callable[[], object]
PatternSpec = tuple[str, str, PatternDemo]

PATTERNS: tuple[PatternSpec, ...] = (
    ("singleton", "creational", singleton.demo),
    ("factory-method", "creational", factory_method.demo),
    ("abstract-factory", "creational", abstract_factory.demo),
    ("builder", "creational", builder.demo),
    ("prototype", "creational", prototype.demo),
    ("object-pool", "creational", object_pool.demo),
    ("lazy-initialization", "creational", lazy_initialization.demo),
    ("adapter", "structural", adapter.demo),
    ("decorator", "structural", decorator.demo),
    ("composite", "structural", composite.demo),
    ("facade", "structural", facade.demo),
    ("proxy", "structural", proxy.demo),
    ("bridge", "structural", bridge.demo),
    ("flyweight", "structural", flyweight.demo),
    ("composite-entity", "structural", composite_entity.demo),
    ("observer", "behavioral", observer.demo),
    ("strategy", "behavioral", strategy.demo),
    ("command", "behavioral", command.demo),
    ("state", "behavioral", state.demo),
    ("template-method", "behavioral", template_method.demo),
    ("chain-of-responsibility", "behavioral", chain_of_responsibility.demo),
    ("iterator", "behavioral", iterator.demo),
    ("mediator", "behavioral", mediator.demo),
    ("memento", "behavioral", memento.demo),
)

_PATTERN_BY_ID: dict[str, tuple[str, PatternDemo]] = {
    pattern_id: (category, demo) for pattern_id, category, demo in PATTERNS
}


def normalize_pattern_id(pattern_id: str) -> str:
    """Normalize input so users can pass spaces/underscores/hyphens."""
    return "-".join(pattern_id.strip().lower().replace("_", " ").split())


def list_patterns() -> list[tuple[str, str]]:
    """Return all patterns in deterministic category/id order."""
    return [(pattern_id, category) for pattern_id, category, _ in PATTERNS]


def run_pattern(pattern_id: str) -> object:
    """Run exactly one pattern by id."""
    normalized = normalize_pattern_id(pattern_id)
    spec = _PATTERN_BY_ID.get(normalized)
    if spec is None:
        raise ValueError(f"Unknown pattern: {pattern_id}")
    _, demo = spec
    return demo()


def run_all_patterns() -> dict[str, object]:
    """Run all demos, preserving pattern order."""
    return {pattern_id: demo() for pattern_id, _, demo in PATTERNS}


def format_result(result: object) -> str:
    """Serialize demo output for CLI display."""
    if is_dataclass(result):
        result = asdict(result)
    elif isinstance(result, tuple):
        result = list(result)
    return json.dumps(result)

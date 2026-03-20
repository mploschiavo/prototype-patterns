"""Prototype pattern example."""

from __future__ import annotations

import copy
from dataclasses import dataclass, field


@dataclass
class Document:
    title: str
    tags: list[str] = field(default_factory=list)

    def clone(self) -> Document:
        return copy.deepcopy(self)


def demo() -> bool:
    draft = Document("Pattern Notes", ["draft"])
    clone = draft.clone()
    clone.tags.append("review")
    return draft.tags == ["draft"] and clone.tags == ["draft", "review"]

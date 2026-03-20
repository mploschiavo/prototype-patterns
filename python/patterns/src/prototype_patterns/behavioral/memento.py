"""Memento pattern example."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Memento:
    text: str


class TextEditor:
    def __init__(self) -> None:
        self._text = ""

    def type(self, value: str) -> None:
        self._text = value

    def save(self) -> Memento:
        return Memento(self._text)

    def restore(self, memento: Memento) -> None:
        self._text = memento.text

    @property
    def text(self) -> str:
        return self._text


def demo() -> str:
    editor = TextEditor()
    editor.type("draft")
    checkpoint = editor.save()
    editor.type("final")
    editor.restore(checkpoint)
    return editor.text

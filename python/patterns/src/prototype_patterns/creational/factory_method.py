"""Factory Method pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError


class HtmlButton(Button):
    def render(self) -> str:
        return "<button>Submit</button>"


class DesktopButton(Button):
    def render(self) -> str:
        return "[DesktopButton: Submit]"


class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        raise NotImplementedError

    def render_dialog(self) -> str:
        return self.create_button().render()


class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HtmlButton()


class DesktopDialog(Dialog):
    def create_button(self) -> Button:
        return DesktopButton()


def demo() -> tuple[str, str]:
    return (WebDialog().render_dialog(), DesktopDialog().render_dialog())

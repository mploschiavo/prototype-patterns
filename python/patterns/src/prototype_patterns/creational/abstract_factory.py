"""Abstract Factory pattern example."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self) -> str:
        raise NotImplementedError


class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> str:
        raise NotImplementedError


class LightButton(Button):
    def paint(self) -> str:
        return "light-button"


class DarkButton(Button):
    def paint(self) -> str:
        return "dark-button"


class LightCheckbox(Checkbox):
    def paint(self) -> str:
        return "light-checkbox"


class DarkCheckbox(Checkbox):
    def paint(self) -> str:
        return "dark-checkbox"


class ThemeFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        raise NotImplementedError

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        raise NotImplementedError


class LightThemeFactory(ThemeFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


class DarkThemeFactory(ThemeFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


def render_ui(factory: ThemeFactory) -> tuple[str, str]:
    return (factory.create_button().paint(), factory.create_checkbox().paint())


def demo() -> tuple[str, str]:
    return render_ui(DarkThemeFactory())

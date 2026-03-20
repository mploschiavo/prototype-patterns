"""Adapter pattern example."""

from __future__ import annotations


class LegacyFahrenheitSensor:
    def read_fahrenheit(self) -> float:
        return 77.0


class CelsiusSensor:
    def __init__(self, legacy_sensor: LegacyFahrenheitSensor) -> None:
        self._legacy_sensor = legacy_sensor

    def read_celsius(self) -> float:
        fahrenheit = self._legacy_sensor.read_fahrenheit()
        return (fahrenheit - 32.0) * 5.0 / 9.0


def demo() -> float:
    return round(CelsiusSensor(LegacyFahrenheitSensor()).read_celsius(), 1)

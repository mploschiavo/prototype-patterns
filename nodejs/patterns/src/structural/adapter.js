class LegacyFahrenheitSensor {
  readFahrenheit() {
    return 77;
  }
}

class CelsiusSensorAdapter {
  constructor(sensor) {
    this.sensor = sensor;
  }

  readCelsius() {
    const fahrenheit = this.sensor.readFahrenheit();
    return (fahrenheit - 32) * 5 / 9;
  }
}

function demo() {
  const value = new CelsiusSensorAdapter(new LegacyFahrenheitSensor()).readCelsius();
  return Number(value.toFixed(1));
}

module.exports = { LegacyFahrenheitSensor, CelsiusSensorAdapter, demo };

package org.prototypepatterns.structural.adapter;

public final class AdapterPattern {
    private AdapterPattern() {
    }

    public static final class LegacyFahrenheitSensor {
        public double readFahrenheit() {
            return 77.0;
        }
    }

    public static final class CelsiusSensorAdapter {
        private final LegacyFahrenheitSensor sensor;

        public CelsiusSensorAdapter(LegacyFahrenheitSensor sensor) {
            this.sensor = sensor;
        }

        public double readCelsius() {
            return (sensor.readFahrenheit() - 32.0) * 5.0 / 9.0;
        }
    }

    public static double demo() {
        double value = new CelsiusSensorAdapter(new LegacyFahrenheitSensor()).readCelsius();
        return Math.round(value * 10.0) / 10.0;
    }
}

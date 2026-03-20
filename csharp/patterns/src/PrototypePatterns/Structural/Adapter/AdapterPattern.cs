namespace PrototypePatterns.Structural.Adapter;

public sealed class LegacyFahrenheitSensor
{
    public double ReadFahrenheit() => 77.0;
}

public sealed class CelsiusSensorAdapter(LegacyFahrenheitSensor sensor)
{
    public double ReadCelsius() => (sensor.ReadFahrenheit() - 32.0) * 5.0 / 9.0;
}

public static class AdapterPattern
{
    public static double Demo() => Math.Round(new CelsiusSensorAdapter(new LegacyFahrenheitSensor()).ReadCelsius(), 1);
}

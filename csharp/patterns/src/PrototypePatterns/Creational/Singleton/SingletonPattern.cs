namespace PrototypePatterns.Creational.Singleton;

public sealed class Configuration
{
    private static readonly Configuration InstanceValue = new();
    private readonly Dictionary<string, string> _settings = new();

    private Configuration()
    {
    }

    public static Configuration Instance => InstanceValue;

    public void Set(string key, string value)
    {
        _settings[key] = value;
    }

    public string? Get(string key)
    {
        return _settings.TryGetValue(key, out var value) ? value : null;
    }
}

public static class SingletonPattern
{
    public static bool Demo()
    {
        var first = Configuration.Instance;
        var second = Configuration.Instance;
        first.Set("mode", "prototype");
        return ReferenceEquals(first, second) && second.Get("mode") == "prototype";
    }
}

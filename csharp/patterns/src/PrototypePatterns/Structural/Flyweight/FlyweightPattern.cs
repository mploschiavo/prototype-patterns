namespace PrototypePatterns.Structural.Flyweight;

public sealed record GlyphStyle(string Family, int Size, bool Bold);

public sealed class GlyphStyleFactory
{
    private readonly Dictionary<string, GlyphStyle> _cache = [];

    public GlyphStyle GetStyle(string family, int size, bool bold)
    {
        var key = $"{family}:{size}:{bold}";
        if (!_cache.TryGetValue(key, out var style))
        {
            style = new GlyphStyle(family, size, bold);
            _cache[key] = style;
        }

        return style;
    }
}

public static class FlyweightPattern
{
    public static bool Demo()
    {
        var factory = new GlyphStyleFactory();
        var first = factory.GetStyle("Fira Code", 12, false);
        var second = factory.GetStyle("Fira Code", 12, false);
        return ReferenceEquals(first, second);
    }
}

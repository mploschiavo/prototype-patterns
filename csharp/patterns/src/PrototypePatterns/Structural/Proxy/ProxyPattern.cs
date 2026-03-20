namespace PrototypePatterns.Structural.Proxy;

public sealed class RealImage
{
    private static int _loadCount;
    private readonly string _path;

    public RealImage(string path)
    {
        _path = path;
        _loadCount++;
    }

    public static int LoadCount => _loadCount;

    public static void Reset() => _loadCount = 0;

    public string Display() => $"display:{_path}";
}

public sealed class ImageProxy(string path)
{
    private RealImage? _realImage;

    public string Display()
    {
        _realImage ??= new RealImage(path);
        return _realImage.Display();
    }
}

public static class ProxyPattern
{
    public static bool Demo()
    {
        RealImage.Reset();
        var proxy = new ImageProxy("chart.png");
        var first = proxy.Display();
        var second = proxy.Display();
        return first == second && RealImage.LoadCount == 1;
    }
}

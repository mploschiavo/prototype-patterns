namespace PrototypePatterns.Structural.Bridge;

public interface IRenderer
{
    string RenderCircle(int radius);
}

public sealed class VectorRenderer : IRenderer
{
    public string RenderCircle(int radius) => $"vector-circle:{radius}";
}

public sealed class RasterRenderer : IRenderer
{
    public string RenderCircle(int radius) => $"raster-circle:{radius}";
}

public sealed class Circle(int radius, IRenderer renderer)
{
    public string Draw() => renderer.RenderCircle(radius);
}

public static class BridgePattern
{
    public static IReadOnlyList<string> Demo() => [new Circle(5, new VectorRenderer()).Draw(), new Circle(5, new RasterRenderer()).Draw()];
}

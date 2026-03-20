namespace PrototypePatterns.Behavioral.TemplateMethod;

public abstract class DataPipeline
{
    public IReadOnlyList<string> Run() => [Read(), Transform(), Write()];

    protected abstract string Read();
    protected abstract string Transform();
    protected abstract string Write();
}

public sealed class CsvPipeline : DataPipeline
{
    protected override string Read() => "read:csv";

    protected override string Transform() => "transform:normalize";

    protected override string Write() => "write:warehouse";
}

public static class TemplateMethodPattern
{
    public static IReadOnlyList<string> Demo() => new CsvPipeline().Run();
}

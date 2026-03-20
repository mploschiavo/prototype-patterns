namespace PrototypePatterns.Creational.LazyInitialization;

public sealed class LazyDataset
{
    private List<string>? _records;

    public int LoadCount { get; private set; }

    public IReadOnlyList<string> Records
    {
        get
        {
            if (_records is null)
            {
                LoadCount++;
                _records = ["row-1", "row-2", "row-3"];
            }

            return _records;
        }
    }
}

public static class LazyInitializationPattern
{
    public static bool Demo()
    {
        var dataset = new LazyDataset();
        _ = dataset.Records;
        _ = dataset.Records;
        return dataset.LoadCount == 1;
    }
}

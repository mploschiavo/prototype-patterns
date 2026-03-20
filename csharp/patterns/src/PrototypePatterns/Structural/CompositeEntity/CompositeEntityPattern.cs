namespace PrototypePatterns.Structural.CompositeEntity;

public sealed class CoarseGrainedOrder
{
    private string _customerName = string.Empty;
    private string _city = string.Empty;

    public void SetData(string customerName, string city)
    {
        _customerName = customerName;
        _city = city;
    }

    public IReadOnlyList<string> GetData() => [_customerName, _city];
}

public sealed class CompositeOrderEntity
{
    private readonly CoarseGrainedOrder _order = new();

    public void SetOrder(string customerName, string city) => _order.SetData(customerName, city);

    public IReadOnlyList<string> ReadOrder() => _order.GetData();
}

public static class CompositeEntityPattern
{
    public static IReadOnlyList<string> Demo()
    {
        var entity = new CompositeOrderEntity();
        entity.SetOrder("Sam", "Austin");
        return entity.ReadOrder();
    }
}

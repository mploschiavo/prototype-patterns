namespace PrototypePatterns.Creational.Builder;

public sealed record House(IReadOnlyList<string> Rooms, bool HasGarage, bool HasGarden);

public sealed class HouseBuilder
{
    private readonly List<string> _rooms = [];
    private bool _hasGarage;
    private bool _hasGarden;

    public HouseBuilder AddRoom(string room)
    {
        _rooms.Add(room);
        return this;
    }

    public HouseBuilder WithGarage()
    {
        _hasGarage = true;
        return this;
    }

    public HouseBuilder WithGarden()
    {
        _hasGarden = true;
        return this;
    }

    public House Build() => new([.. _rooms], _hasGarage, _hasGarden);
}

public static class BuilderPattern
{
    public static House Demo() => new HouseBuilder().AddRoom("Kitchen").AddRoom("Office").WithGarage().Build();
}

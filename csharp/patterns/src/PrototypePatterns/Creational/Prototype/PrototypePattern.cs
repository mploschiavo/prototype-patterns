namespace PrototypePatterns.Creational.Prototype;

public sealed class Document(string title, IReadOnlyList<string> tags)
{
    public string Title { get; } = title;
    public List<string> Tags { get; } = [.. tags];

    public Document CloneDocument() => new(Title, Tags);
}

public static class PrototypePattern
{
    public static bool Demo()
    {
        var original = new Document("Pattern Notes", ["draft"]);
        var copy = original.CloneDocument();
        copy.Tags.Add("review");
        return original.Tags.Count == 1 && copy.Tags.Count == 2;
    }
}

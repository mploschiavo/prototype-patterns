namespace PrototypePatterns.Behavioral.Iterator;

public sealed class Playlist(IReadOnlyList<string> songs) : IEnumerable<string>
{
    public IEnumerator<string> GetEnumerator() => songs.GetEnumerator();

    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() => GetEnumerator();
}

public static class IteratorPattern
{
    public static IReadOnlyList<string> Demo()
    {
        return [.. new Playlist(["intro", "verse", "outro"])];
    }
}

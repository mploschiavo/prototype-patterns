namespace PrototypePatterns.Structural.Composite;

public interface INode
{
    int Size();
}

public sealed class FileNode(int bytesSize) : INode
{
    public int Size() => bytesSize;
}

public sealed class FolderNode : INode
{
    private readonly List<INode> _children = [];

    public void Add(INode node) => _children.Add(node);

    public int Size() => _children.Sum(child => child.Size());
}

public static class CompositePattern
{
    public static int Demo()
    {
        var root = new FolderNode();
        root.Add(new FileNode(10));
        var nested = new FolderNode();
        nested.Add(new FileNode(5));
        nested.Add(new FileNode(15));
        root.Add(nested);
        return root.Size();
    }
}

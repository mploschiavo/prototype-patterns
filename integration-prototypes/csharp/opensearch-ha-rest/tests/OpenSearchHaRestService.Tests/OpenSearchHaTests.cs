using OpenSearchHaRestService;

namespace OpenSearchHaRestService.Tests;

public sealed class OpenSearchHaTests
{
    [Fact]
    public void ParseNodes_ReturnsAllNodes()
    {
        var nodes = OpenSearchHaRepository.ParseNodes("http://localhost:9200,http://localhost:9201,http://localhost:9202");
        Assert.Equal(3, nodes.Count);
    }

    [Fact]
    public async Task FetchValueAsync_UsesFailover()
    {
        var repository = new OpenSearchHaRepository();
        var calls = new List<string>();

        var value = await repository.FetchValueAsync(
            "prototype_docs",
            "1",
            (node, _index, _id) =>
            {
                calls.Add(node);
                if (node.EndsWith(":9200", StringComparison.Ordinal))
                {
                    throw new InvalidOperationException("node down");
                }

                return Task.FromResult<string?>("hello opensearch ha");
            });

        Assert.Equal("hello opensearch ha", value);
        Assert.True(calls.Count >= 2);
    }
}

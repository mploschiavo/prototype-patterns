using OllamaMcpServer;

namespace OllamaMcpServer.Tests;

public sealed class McpTests
{
    [Fact]
    public void RagSearch_ReturnsHits()
    {
        var docs = new List<RagDocument>
        {
            new("1", "Kafka and Redis integration"),
            new("2", "Postgres demo")
        };

        var hits = McpService.RagSearch("Redis", docs);
        Assert.True(hits.Count >= 1);
    }

    [Fact]
    public async Task ToolsList_ResponseHasTools()
    {
        var service = new McpService();
        var response = await service.HandleRpcAsync(new RpcRequest("2.0", 1, "tools/list", null));
        Assert.NotNull(response);
    }
}

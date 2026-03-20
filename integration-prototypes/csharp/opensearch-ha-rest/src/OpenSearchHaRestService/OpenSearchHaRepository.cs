using System.Text.Json;

namespace OpenSearchHaRestService;

public sealed class OpenSearchHaRepository
{
    private readonly string _nodes = Environment.GetEnvironmentVariable("OPENSEARCH_NODES")
        ?? "http://localhost:9200,http://localhost:9201,http://localhost:9202";

    public static IReadOnlyList<string> ParseNodes(string nodes)
    {
        return nodes.Split(',').Select(node => node.Trim()).Where(node => node.Length > 0).ToArray();
    }

    public async Task<string?> FetchValueAsync(
        string index,
        string id,
        Func<string, string, string, Task<string?>>? nodeFetcher = null)
    {
        var fetcher = nodeFetcher ?? FetchFromNodeAsync;
        Exception? lastFailure = null;

        foreach (var node in ParseNodes(_nodes))
        {
            try
            {
                return await fetcher(node, index, id);
            }
            catch (Exception error)
            {
                lastFailure = error;
            }
        }

        throw new InvalidOperationException("all OpenSearch nodes unreachable", lastFailure);
    }

    public static string? ParseMessage(string payload)
    {
        using var document = JsonDocument.Parse(payload);
        var root = document.RootElement;

        if (root.TryGetProperty("found", out var foundProperty) && foundProperty.ValueKind == JsonValueKind.False)
        {
            return null;
        }

        if (!root.TryGetProperty("_source", out var sourceProperty))
        {
            return null;
        }

        if (!sourceProperty.TryGetProperty("message", out var messageProperty))
        {
            return null;
        }

        return messageProperty.GetString();
    }

    private static async Task<string?> FetchFromNodeAsync(string nodeUrl, string index, string id)
    {
        using var client = new HttpClient();
        using var response = await client.GetAsync($"{nodeUrl}/{index}/_doc/{id}");

        if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            return null;
        }

        response.EnsureSuccessStatusCode();
        var payload = await response.Content.ReadAsStringAsync();
        return ParseMessage(payload);
    }
}

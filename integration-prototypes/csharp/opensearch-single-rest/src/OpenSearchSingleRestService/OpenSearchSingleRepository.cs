using System.Text.Json;

namespace OpenSearchSingleRestService;

public sealed class OpenSearchSingleRepository
{
    private readonly string _opensearchUrl = Environment.GetEnvironmentVariable("OPENSEARCH_URL") ?? "http://localhost:9200";

    public async Task<string?> FetchValueAsync(string index, string id)
    {
        using var client = new HttpClient();
        using var response = await client.GetAsync($"{_opensearchUrl}/{index}/_doc/{id}");

        if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            return null;
        }

        response.EnsureSuccessStatusCode();
        var payload = await response.Content.ReadAsStringAsync();
        return ParseMessage(payload);
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
}

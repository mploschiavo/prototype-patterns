using System.Text;
using System.Text.Json;

namespace OllamaMcpServer;

public sealed class McpService
{
    private readonly string _ollamaUrl = Environment.GetEnvironmentVariable("OLLAMA_URL") ?? "http://localhost:11434";
    private readonly string _ollamaModel = Environment.GetEnvironmentVariable("OLLAMA_MODEL") ?? "tinyllama";
    private readonly string _ragDocsPath = Environment.GetEnvironmentVariable("RAG_DOCS_PATH")
        ?? Path.Combine(AppContext.BaseDirectory, "rag-documents.json");

    public List<RagDocument> LoadDocuments()
    {
        var candidatePaths = new[]
        {
            _ragDocsPath,
            Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "rag-documents.json"),
            Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "..", "rag-documents.json")
        };

        foreach (var path in candidatePaths)
        {
            var fullPath = Path.GetFullPath(path);
            if (File.Exists(fullPath))
            {
                var json = File.ReadAllText(fullPath);
                return JsonSerializer.Deserialize<List<RagDocument>>(json) ?? new List<RagDocument>();
            }
        }

        return new List<RagDocument>
        {
            new("fallback-1", "Ollama MCP server supports rag.search and agent.answer."),
            new("fallback-2", "Fallback documents are used when no rag-documents.json file is available.")
        };
    }

    public static IReadOnlyList<RagDocument> RagSearch(string query, IReadOnlyList<RagDocument> docs, int limit = 3)
    {
        var terms = query.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(value => value.ToLowerInvariant())
            .ToArray();

        var ranked = docs
            .Select(doc => new
            {
                Doc = doc,
                Score = terms.Count(term => doc.Text.Contains(term, StringComparison.OrdinalIgnoreCase))
            })
            .Where(item => item.Score > 0)
            .OrderByDescending(item => item.Score)
            .Take(limit)
            .Select(item => item.Doc)
            .ToList();

        return ranked;
    }

    public async Task<object> HandleRpcAsync(RpcRequest request)
    {
        var docs = LoadDocuments();

        if (request.Method == "tools/list")
        {
            return new
            {
                jsonrpc = "2.0",
                id = request.Id,
                result = new
                {
                    tools = new[]
                    {
                        new { name = "rag.search", description = "Search seeded RAG documents" },
                        new { name = "agent.answer", description = "Answer a question using RAG + Ollama" }
                    }
                }
            };
        }

        if (request.Method == "tools/call" && request.Params is not null)
        {
            if (request.Params.Name == "rag.search")
            {
                var query = request.Params.Arguments?.GetValueOrDefault("query") ?? string.Empty;
                var hits = RagSearch(query, docs);
                return new { jsonrpc = "2.0", id = request.Id, result = new { hits } };
            }

            if (request.Params.Name == "agent.answer")
            {
                var question = request.Params.Arguments?.GetValueOrDefault("question") ?? string.Empty;
                var hits = RagSearch(question, docs);
                var answer = await AskOllamaAsync(question, hits);
                return new { jsonrpc = "2.0", id = request.Id, result = new { answer, context = hits } };
            }
        }

        return new { jsonrpc = "2.0", id = request.Id, error = new { code = -32601, message = "Method not found" } };
    }

    private async Task<string> AskOllamaAsync(string question, IReadOnlyList<RagDocument> context)
    {
        var contextBlock = context.Count > 0
            ? string.Join("\n", context.Select(item => $"- {item.Text}"))
            : "- No context found";

        var prompt = $"Use context to answer.\nContext:\n{contextBlock}\n\nQuestion: {question}";
        using var client = new HttpClient();
        var payload = JsonSerializer.Serialize(new { model = _ollamaModel, prompt, stream = false });
        using var response = await client.PostAsync($"{_ollamaUrl}/api/generate", new StringContent(payload, Encoding.UTF8, "application/json"));
        response.EnsureSuccessStatusCode();

        using var stream = await response.Content.ReadAsStreamAsync();
        using var json = await JsonDocument.ParseAsync(stream);
        return json.RootElement.TryGetProperty("response", out var value) ? value.GetString() ?? string.Empty : string.Empty;
    }
}

namespace OllamaMcpServer;

public sealed record RagDocument(string Id, string Text);

public sealed record RpcRequest(string Jsonrpc, int Id, string Method, RpcParams? Params);

public sealed record RpcParams(string Name, Dictionary<string, string>? Arguments);

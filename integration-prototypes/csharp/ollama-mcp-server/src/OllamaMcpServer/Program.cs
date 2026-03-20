using OllamaMcpServer;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<McpService>();

var app = builder.Build();

app.MapPost("/mcp", async (RpcRequest request, McpService service) =>
{
    var response = await service.HandleRpcAsync(request);
    return Results.Json(response);
});

app.Run();

public partial class Program;

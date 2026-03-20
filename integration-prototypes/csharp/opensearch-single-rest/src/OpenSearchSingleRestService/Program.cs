using OpenSearchSingleRestService;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<OpenSearchSingleRepository>();

var app = builder.Build();

app.MapGet("/value", async (string? index, string? id, OpenSearchSingleRepository repository) =>
{
    var resolvedIndex = string.IsNullOrWhiteSpace(index) ? "prototype_docs" : index;
    var resolvedId = string.IsNullOrWhiteSpace(id) ? "1" : id;

    var value = await repository.FetchValueAsync(resolvedIndex, resolvedId);
    return value is null
        ? Results.NotFound(new { error = "document not found" })
        : Results.Json(new { index = resolvedIndex, id = resolvedId, value });
});

app.Run();

public partial class Program;

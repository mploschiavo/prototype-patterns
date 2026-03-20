using OpenSearchHaRestService;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<OpenSearchHaRepository>();

var app = builder.Build();

app.MapGet("/value", async (string? index, string? id, OpenSearchHaRepository repository) =>
{
    var resolvedIndex = string.IsNullOrWhiteSpace(index) ? "prototype_docs" : index;
    var resolvedId = string.IsNullOrWhiteSpace(id) ? "1" : id;

    try
    {
        var value = await repository.FetchValueAsync(resolvedIndex, resolvedId);
        return value is null
            ? Results.NotFound(new { error = "document not found" })
            : Results.Json(new { index = resolvedIndex, id = resolvedId, value });
    }
    catch (InvalidOperationException)
    {
        return Results.StatusCode(StatusCodes.Status503ServiceUnavailable);
    }
});

app.Run();

public partial class Program;

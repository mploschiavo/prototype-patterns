using PostgresRestService;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<PostgresRepository>();

var app = builder.Build();

app.MapGet("/item", async (int id, PostgresRepository repository) =>
{
    var item = await repository.FetchItemAsync(id);
    return item is null ? Results.NotFound(new { error = "item not found" }) : Results.Json(item);
});

app.Run();

public partial class Program;

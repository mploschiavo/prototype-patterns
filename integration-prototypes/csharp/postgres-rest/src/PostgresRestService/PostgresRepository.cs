using Npgsql;

namespace PostgresRestService;

public sealed class PostgresRepository
{
    private readonly string _connectionString = Environment.GetEnvironmentVariable("POSTGRES_CONNECTION_STRING")
        ?? "Host=localhost;Port=5432;Username=prototype_user;Password=prototype_pass;Database=prototype_db";

    public async Task<DemoItem?> FetchItemAsync(int id)
    {
        await using var connection = new NpgsqlConnection(_connectionString);
        await connection.OpenAsync();

        const string sql = "SELECT id, name, description FROM demo_items WHERE id = @id";
        await using var command = new NpgsqlCommand(sql, connection);
        command.Parameters.AddWithValue("id", id);

        await using var reader = await command.ExecuteReaderAsync();
        if (!await reader.ReadAsync())
        {
            return null;
        }

        return new DemoItem(reader.GetInt32(0), reader.GetString(1), reader.GetString(2));
    }
}

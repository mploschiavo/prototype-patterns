package org.prototype.postgres;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public final class PostgresRepository {
    private PostgresRepository() {
    }

    public static DemoItem fetchItem(int id, String jdbcUrl, String user, String password) throws Exception {
        try (Connection connection = DriverManager.getConnection(jdbcUrl, user, password);
             PreparedStatement statement = connection.prepareStatement("SELECT id, name, description FROM demo_items WHERE id = ?")) {
            statement.setInt(1, id);
            try (ResultSet result = statement.executeQuery()) {
                if (!result.next()) {
                    return null;
                }
                return new DemoItem(result.getInt("id"), result.getString("name"), result.getString("description"));
            }
        }
    }
}

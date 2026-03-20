package org.prototype.postgres;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.Map;

public final class PostgresRestServer {
    private PostgresRestServer() {
    }

    private static Map<String, String> settings() {
        return Map.of(
            "url", System.getenv().getOrDefault("POSTGRES_JDBC_URL", "jdbc:postgresql://localhost:5432/prototype_db"),
            "user", System.getenv().getOrDefault("POSTGRES_USER", "prototype_user"),
            "password", System.getenv().getOrDefault("POSTGRES_PASSWORD", "prototype_pass")
        );
    }

    public static HttpServer createServer(int port) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/item", PostgresRestServer::handle);
        return server;
    }

    private static void handle(HttpExchange exchange) {
        try {
            int id = 1;
            String query = exchange.getRequestURI().getQuery();
            if (query != null && query.startsWith("id=")) {
                id = Integer.parseInt(query.substring(3));
            }

            Map<String, String> config = settings();
            DemoItem item = PostgresRepository.fetchItem(id, config.get("url"), config.get("user"), config.get("password"));
            if (item == null) {
                write(exchange, 404, "{\"error\":\"item not found\"}");
                return;
            }

            write(exchange, 200, item.toJson());
        } catch (Exception error) {
            write(exchange, 500, "{\"error\":\"" + error.getMessage() + "\"}");
        }
    }

    private static void write(HttpExchange exchange, int status, String body) {
        try {
            byte[] data = body.getBytes();
            exchange.getResponseHeaders().set("Content-Type", "application/json; charset=utf-8");
            exchange.sendResponseHeaders(status, data.length);
            try (OutputStream output = exchange.getResponseBody()) {
                output.write(data);
            }
        } catch (Exception ignored) {
            // intentionally minimal for prototype
        }
    }

    public static void main(String[] args) throws Exception {
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8080"));
        HttpServer server = createServer(port);
        server.start();
        System.out.println("postgres-rest listening on :" + port);
    }
}

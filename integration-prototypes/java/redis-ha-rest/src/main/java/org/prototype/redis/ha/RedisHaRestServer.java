package org.prototype.redis.ha;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public final class RedisHaRestServer {
    private RedisHaRestServer() {
    }

    public static HttpServer createServer(int port) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/value", RedisHaRestServer::handle);
        return server;
    }

    private static void handle(HttpExchange exchange) {
        try {
            String key = "demo:key";
            String query = exchange.getRequestURI().getQuery();
            if (query != null && query.startsWith("key=")) {
                key = query.substring(4);
            }

            String nodes = System.getenv().getOrDefault("REDIS_CLUSTER_NODES", "localhost:6379,localhost:6380,localhost:6381");
            String value = RedisHaRepository.fetchValue(nodes, key);
            if (value == null) {
                write(exchange, 404, "{\"error\":\"key not found\"}");
                return;
            }

            write(exchange, 200, "{\"key\":\"" + key + "\",\"value\":" + value + "}");
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
        System.out.println("redis-ha-rest listening on :" + port);
    }
}

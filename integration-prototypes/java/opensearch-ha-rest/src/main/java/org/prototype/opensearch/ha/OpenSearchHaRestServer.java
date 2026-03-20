package org.prototype.opensearch.ha;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public final class OpenSearchHaRestServer {
    private OpenSearchHaRestServer() {
    }

    public static HttpServer createServer(int port) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/value", OpenSearchHaRestServer::handle);
        return server;
    }

    private static void handle(HttpExchange exchange) {
        try {
            String index = "prototype_docs";
            String id = "1";
            String query = exchange.getRequestURI().getQuery();
            if (query != null) {
                for (String part : query.split("&")) {
                    if (part.startsWith("index=")) {
                        index = part.substring(6);
                    }
                    if (part.startsWith("id=")) {
                        id = part.substring(3);
                    }
                }
            }

            OpenSearchHaRepository repository = new OpenSearchHaRepository();
            String value = repository.fetchValue(index, id);
            if (value == null) {
                write(exchange, 404, "{\"error\":\"document not found\"}");
                return;
            }

            write(exchange, 200, "{\"index\":\"" + index + "\",\"id\":\"" + id + "\",\"value\":\"" + value + "\"}");
        } catch (Exception error) {
            write(exchange, 503, "{\"error\":\"" + error.getMessage() + "\"}");
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
        System.out.println("opensearch-ha-rest listening on :" + port);
    }
}

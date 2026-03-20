package org.prototype.services.helloworld;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public final class HelloWorldServer {
    private HelloWorldServer() {
    }

    public static String message() {
        return "hello world";
    }

    public static HttpServer createServer(int port) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/", exchange -> handle(exchange));
        server.setExecutor(null);
        return server;
    }

    private static void handle(HttpExchange exchange) throws IOException {
        int status;
        String response;

        if (!"/".equals(exchange.getRequestURI().getPath())) {
            status = 404;
            response = "not found";
        } else {
            status = 200;
            response = message();
        }

        byte[] body = response.getBytes();
        exchange.getResponseHeaders().set("Content-Type", "text/plain; charset=utf-8");
        exchange.sendResponseHeaders(status, body.length);
        try (OutputStream output = exchange.getResponseBody()) {
            output.write(body);
        }
    }

    public static void main(String[] args) throws IOException {
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8080"));
        HttpServer server = createServer(port);
        System.out.println("Java hello-world listening on :" + port);
        server.start();
    }
}

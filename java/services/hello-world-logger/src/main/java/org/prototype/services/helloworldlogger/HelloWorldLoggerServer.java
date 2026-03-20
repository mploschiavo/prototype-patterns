package org.prototype.services.helloworldlogger;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.logging.Level;
import java.util.logging.Logger;

public final class HelloWorldLoggerServer {
    private static final Logger LOGGER = Logger.getLogger(HelloWorldLoggerServer.class.getName());

    private HelloWorldLoggerServer() {
    }

    public static String message(Logger logger) {
        logger.info("Handling hello-world-logger request");
        return "hello world with logger";
    }

    public static HttpServer createServer(int port, Logger logger) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/", exchange -> handle(exchange, logger));
        server.setExecutor(null);
        return server;
    }

    private static void handle(HttpExchange exchange, Logger logger) throws IOException {
        int status;
        String response;

        if (!"/".equals(exchange.getRequestURI().getPath())) {
            status = 404;
            response = "not found";
        } else {
            status = 200;
            response = message(logger);
        }

        byte[] body = response.getBytes();
        exchange.getResponseHeaders().set("Content-Type", "text/plain; charset=utf-8");
        exchange.sendResponseHeaders(status, body.length);
        try (OutputStream output = exchange.getResponseBody()) {
            output.write(body);
        }
    }

    public static void main(String[] args) throws IOException {
        LOGGER.setLevel(Level.INFO);
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8080"));
        HttpServer server = createServer(port, LOGGER);
        System.out.println("Java hello-world-logger listening on :" + port);
        server.start();
    }
}

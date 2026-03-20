package org.prototype.services.helloworldlogger;

import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogRecord;
import java.util.logging.Logger;

public final class HelloWorldLoggerServerTests {
    private HelloWorldLoggerServerTests() {
    }

    private static void assertTrue(boolean condition, String message) {
        if (!condition) {
            throw new IllegalStateException(message);
        }
    }

    private static void assertEquals(Object expected, Object actual, String message) {
        assertTrue(expected.equals(actual), message + " expected=" + expected + " actual=" + actual);
    }

    public static void main(String[] args) throws Exception {
        testMessageAndLogger();
        testHttp();
        System.out.println("Java hello-world-logger service tests passed");
    }

    private static void testMessageAndLogger() {
        Logger logger = Logger.getLogger("hello-world-logger-test");
        logger.setUseParentHandlers(false);
        logger.setLevel(Level.INFO);

        CaptureHandler capture = new CaptureHandler();
        logger.addHandler(capture);

        try {
            assertEquals("hello world with logger", HelloWorldLoggerServer.message(logger), "message method");
            assertTrue(capture.messages.stream().anyMatch(msg -> msg.contains("Handling hello-world-logger request")), "log entry");
        } finally {
            logger.removeHandler(capture);
        }
    }

    private static void testHttp() throws IOException, InterruptedException {
        Logger logger = Logger.getLogger("hello-world-logger-http");
        logger.setUseParentHandlers(false);
        HttpServer server = HelloWorldLoggerServer.createServer(0, logger);
        server.start();

        try {
            int port = server.getAddress().getPort();
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder(URI.create("http://127.0.0.1:" + port + "/"))
                .GET()
                .build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            assertEquals(200, response.statusCode(), "http status");
            assertEquals("hello world with logger", response.body(), "http body");
        } finally {
            server.stop(0);
        }
    }

    private static final class CaptureHandler extends Handler {
        private final List<String> messages = new ArrayList<>();

        @Override
        public void publish(LogRecord record) {
            messages.add(record.getMessage());
        }

        @Override
        public void flush() {
        }

        @Override
        public void close() {
        }
    }
}

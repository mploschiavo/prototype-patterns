package org.prototype.services.helloworld;

import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public final class HelloWorldServerTests {
    private HelloWorldServerTests() {
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
        assertEquals("hello world", HelloWorldServer.message(), "message method");
        testHttp();
        System.out.println("Java hello-world service tests passed");
    }

    private static void testHttp() throws IOException, InterruptedException {
        HttpServer server = HelloWorldServer.createServer(0);
        server.start();

        try {
            int port = server.getAddress().getPort();
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder(URI.create("http://127.0.0.1:" + port + "/"))
                .GET()
                .build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            assertEquals(200, response.statusCode(), "http status");
            assertEquals("hello world", response.body(), "http body");
        } finally {
            server.stop(0);
        }
    }
}

package org.prototype.ollama.mcp;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.OutputStream;
import java.net.URI;
import java.net.InetSocketAddress;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;

public final class OllamaMcpServer {
    private static final ObjectMapper MAPPER = new ObjectMapper();
    private static final String OLLAMA_URL = System.getenv().getOrDefault("OLLAMA_URL", "http://localhost:11434");
    private static final String OLLAMA_MODEL = System.getenv().getOrDefault("OLLAMA_MODEL", "tinyllama");

    private OllamaMcpServer() {
    }

    public static HttpServer createServer(int port) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/mcp", OllamaMcpServer::handle);
        return server;
    }

    static String handleRpc(String requestBody, List<RagDocument> docs, OllamaResponder responder) throws Exception {
        JsonNode request = MAPPER.readTree(requestBody);
        String method = request.path("method").asText();
        JsonNode id = request.get("id");

        if ("tools/list".equals(method)) {
            var tools = List.of(
                Map.of("name", "rag.search", "description", "Search seeded RAG documents"),
                Map.of("name", "agent.answer", "description", "Answer a question using RAG + Ollama")
            );
            return MAPPER.writeValueAsString(Map.of("jsonrpc", "2.0", "id", id, "result", Map.of("tools", tools)));
        }

        if ("tools/call".equals(method)) {
            JsonNode params = request.path("params");
            String name = params.path("name").asText();
            JsonNode arguments = params.path("arguments");

            if ("rag.search".equals(name)) {
                String query = arguments.path("query").asText("");
                List<RagDocument> hits = OllamaMcpRepository.ragSearch(query, docs, 3);
                return MAPPER.writeValueAsString(Map.of("jsonrpc", "2.0", "id", id, "result", Map.of("hits", hits)));
            }

            if ("agent.answer".equals(name)) {
                String question = arguments.path("question").asText("");
                List<RagDocument> hits = OllamaMcpRepository.ragSearch(question, docs, 3);
                String answer = responder.answer(question, hits);
                return MAPPER.writeValueAsString(
                    Map.of("jsonrpc", "2.0", "id", id, "result", Map.of("answer", answer, "context", hits))
                );
            }
        }

        return MAPPER.writeValueAsString(Map.of("jsonrpc", "2.0", "id", id, "error", Map.of("code", -32601, "message", "Method not found")));
    }

    private static void handle(HttpExchange exchange) {
        try {
            if (!"POST".equalsIgnoreCase(exchange.getRequestMethod())) {
                write(exchange, 405, "{\"error\":\"method not allowed\"}");
                return;
            }

            String requestBody = new String(exchange.getRequestBody().readAllBytes());
            Path docsPath = Path.of(System.getenv().getOrDefault("RAG_DOCS_PATH", "rag-documents.json"));
            List<RagDocument> docs = OllamaMcpRepository.loadDocuments(docsPath);

            String response = handleRpc(requestBody, docs, OllamaMcpServer::callOllama);
            write(exchange, 200, response);
        } catch (Exception error) {
            write(exchange, 500, "{\"error\":\"" + error.getMessage() + "\"}");
        }
    }

    private static String callOllama(String question, List<RagDocument> context) throws Exception {
        String contextBlock;
        if (context.isEmpty()) {
            contextBlock = "- No context found";
        } else {
            StringBuilder builder = new StringBuilder();
            for (RagDocument doc : context) {
                builder.append("- ").append(doc.text()).append("\n");
            }
            contextBlock = builder.toString();
        }

        String prompt = "Use context to answer.\nContext:\n" + contextBlock + "\nQuestion: " + question;
        String payload = MAPPER.writeValueAsString(Map.of("model", OLLAMA_MODEL, "prompt", prompt, "stream", false));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(OLLAMA_URL + "/api/generate"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();

        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() >= 400) {
            throw new IllegalStateException("Ollama request failed: " + response.statusCode());
        }

        JsonNode root = MAPPER.readTree(response.body());
        JsonNode answer = root.get("response");
        return answer == null ? "" : answer.asText();
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
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8090"));
        HttpServer server = createServer(port);
        server.start();
        System.out.println("java-ollama-mcp listening on :" + port);
    }
}

package org.prototype.opensearch.ha;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.List;

public class OpenSearchHaRepository {
    private final List<String> nodes;
    private final HttpClient httpClient;
    private static final ObjectMapper MAPPER = new ObjectMapper();

    public OpenSearchHaRepository() {
        this(
            System.getenv().getOrDefault("OPENSEARCH_NODES", "http://localhost:9200,http://localhost:9201,http://localhost:9202"),
            HttpClient.newHttpClient()
        );
    }

    public OpenSearchHaRepository(String nodeList, HttpClient httpClient) {
        this.nodes = parseNodes(nodeList);
        this.httpClient = httpClient;
    }

    public static List<String> parseNodes(String nodeList) {
        List<String> parsed = new ArrayList<>();
        for (String node : nodeList.split(",")) {
            String value = node.trim();
            if (!value.isEmpty()) {
                parsed.add(value);
            }
        }
        return parsed;
    }

    public String fetchValue(String index, String id) throws Exception {
        Exception lastFailure = null;

        for (String node : nodes) {
            try {
                return fetchFromNode(node, index, id);
            } catch (Exception error) {
                lastFailure = error;
            }
        }

        throw new IllegalStateException("all OpenSearch nodes unreachable", lastFailure);
    }

    protected String fetchFromNode(String nodeUrl, String index, String id) throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(nodeUrl + "/" + index + "/_doc/" + id))
            .GET()
            .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() == 404) {
            return null;
        }

        if (response.statusCode() >= 400) {
            throw new IllegalStateException("OpenSearch request failed: " + response.statusCode());
        }

        return extractMessage(response.body());
    }

    public static String extractMessage(String payload) throws Exception {
        JsonNode root = MAPPER.readTree(payload);
        JsonNode found = root.get("found");
        if (found != null && !found.asBoolean(true)) {
            return null;
        }

        JsonNode source = root.get("_source");
        if (source == null || source.get("message") == null || source.get("message").isNull()) {
            return null;
        }

        return source.get("message").asText();
    }
}

package org.prototype.opensearch.single;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class OpenSearchSingleRepository {
    private final String baseUrl;
    private final HttpClient httpClient;
    private static final ObjectMapper MAPPER = new ObjectMapper();

    public OpenSearchSingleRepository() {
        this(System.getenv().getOrDefault("OPENSEARCH_URL", "http://localhost:9200"), HttpClient.newHttpClient());
    }

    public OpenSearchSingleRepository(String baseUrl, HttpClient httpClient) {
        this.baseUrl = baseUrl;
        this.httpClient = httpClient;
    }

    public String fetchValue(String index, String id) throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/" + index + "/_doc/" + id))
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

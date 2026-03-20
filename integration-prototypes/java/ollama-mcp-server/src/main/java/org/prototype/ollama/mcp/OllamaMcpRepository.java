package org.prototype.ollama.mcp;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;

public final class OllamaMcpRepository {
    private static final ObjectMapper MAPPER = new ObjectMapper();

    private OllamaMcpRepository() {
    }

    public static List<RagDocument> loadDocuments(Path path) throws Exception {
        String json = Files.readString(path);
        List<java.util.Map<String, String>> raw = MAPPER.readValue(json, new TypeReference<List<java.util.Map<String, String>>>() { });
        List<RagDocument> docs = new ArrayList<>();
        for (java.util.Map<String, String> doc : raw) {
            docs.add(new RagDocument(doc.get("id"), doc.get("text")));
        }
        return docs;
    }

    public static List<RagDocument> ragSearch(String query, List<RagDocument> docs, int limit) {
        List<String> terms = List.of(query.toLowerCase(Locale.ROOT).split("\\s+"));
        return docs.stream()
            .sorted(Comparator.comparingInt((RagDocument doc) -> score(doc, terms)).reversed())
            .filter(doc -> score(doc, terms) > 0)
            .limit(limit)
            .toList();
    }

    private static int score(RagDocument doc, List<String> terms) {
        String text = doc.text().toLowerCase(Locale.ROOT);
        int count = 0;
        for (String term : terms) {
            if (!term.isBlank() && text.contains(term)) {
                count += 1;
            }
        }
        return count;
    }
}

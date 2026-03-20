package org.prototype.ollama.mcp;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.nio.file.Path;
import java.util.List;
import org.junit.jupiter.api.Test;

public final class OllamaMcpTests {
    @Test
    void ragSearchFindsHits() throws Exception {
        List<RagDocument> docs = OllamaMcpRepository.loadDocuments(Path.of("rag-documents.json"));
        List<RagDocument> hits = OllamaMcpRepository.ragSearch("Redis", docs, 3);
        assertTrue(hits.size() >= 1);
    }

    @Test
    void toolsListResponse() throws Exception {
        List<RagDocument> docs = OllamaMcpRepository.loadDocuments(Path.of("rag-documents.json"));
        String response = OllamaMcpServer.handleRpc("{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/list\"}", docs, (q, c) -> "unused");
        assertTrue(response.contains("rag.search"));
    }

    @Test
    void agentAnswerResponse() throws Exception {
        List<RagDocument> docs = OllamaMcpRepository.loadDocuments(Path.of("rag-documents.json"));
        String request = "{\"jsonrpc\":\"2.0\",\"id\":2,\"method\":\"tools/call\",\"params\":{\"name\":\"agent.answer\",\"arguments\":{\"question\":\"What demos are available?\"}}}";
        String response = OllamaMcpServer.handleRpc(request, docs, (question, context) -> "mock answer");
        assertTrue(response.contains("mock answer"));
        assertTrue(response.contains("context"));
    }
}

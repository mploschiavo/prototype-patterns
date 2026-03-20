package org.prototype.ollama.mcp;

import java.util.List;

@FunctionalInterface
public interface OllamaResponder {
    String answer(String question, List<RagDocument> context) throws Exception;
}

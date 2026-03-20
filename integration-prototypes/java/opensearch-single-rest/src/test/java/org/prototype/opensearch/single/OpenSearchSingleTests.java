package org.prototype.opensearch.single;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

import org.junit.jupiter.api.Test;

public final class OpenSearchSingleTests {
    @Test
    void extractMessageFound() throws Exception {
        String payload = "{\"found\":true,\"_source\":{\"message\":\"hello opensearch single\"}}";
        assertEquals("hello opensearch single", OpenSearchSingleRepository.extractMessage(payload));
    }

    @Test
    void extractMessageNotFound() throws Exception {
        assertNull(OpenSearchSingleRepository.extractMessage("{\"found\":false}"));
    }
}

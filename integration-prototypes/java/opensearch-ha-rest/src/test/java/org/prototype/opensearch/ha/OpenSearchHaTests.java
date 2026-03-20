package org.prototype.opensearch.ha;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.net.http.HttpClient;
import org.junit.jupiter.api.Test;

public final class OpenSearchHaTests {
    @Test
    void parseNodesCount() {
        assertEquals(3, OpenSearchHaRepository.parseNodes("http://localhost:9200,http://localhost:9201,http://localhost:9202").size());
    }

    @Test
    void fetchValueFailover() throws Exception {
        OpenSearchHaRepository repository = new OpenSearchHaRepository("http://localhost:9200,http://localhost:9201", HttpClient.newHttpClient()) {
            @Override
            protected String fetchFromNode(String nodeUrl, String index, String id) {
                if (nodeUrl.endsWith(":9200")) {
                    throw new IllegalStateException("node down");
                }
                return "hello opensearch ha";
            }
        };

        assertEquals("hello opensearch ha", repository.fetchValue("prototype_docs", "1"));
    }

    @Test
    void fetchValueAllNodesDown() {
        OpenSearchHaRepository repository = new OpenSearchHaRepository("http://localhost:9200", HttpClient.newHttpClient()) {
            @Override
            protected String fetchFromNode(String nodeUrl, String index, String id) {
                throw new IllegalStateException("node down");
            }
        };

        assertThrows(IllegalStateException.class, () -> repository.fetchValue("prototype_docs", "1"));
    }
}

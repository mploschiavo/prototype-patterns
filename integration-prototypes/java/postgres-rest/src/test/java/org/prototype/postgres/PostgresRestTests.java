package org.prototype.postgres;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public final class PostgresRestTests {
    @Test
    void demoItemToJson() {
        DemoItem item = new DemoItem(1, "alpha", "seed row alpha");
        assertEquals("{\"id\":1,\"name\":\"alpha\",\"description\":\"seed row alpha\"}", item.toJson());
    }
}

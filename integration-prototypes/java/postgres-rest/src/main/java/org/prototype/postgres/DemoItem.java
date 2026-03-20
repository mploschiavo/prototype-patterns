package org.prototype.postgres;

public record DemoItem(int id, String name, String description) {
    public String toJson() {
        return "{\"id\":" + id + ",\"name\":\"" + name + "\",\"description\":\"" + description + "\"}";
    }
}

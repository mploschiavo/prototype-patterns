package org.prototypepatterns.structural.bridge;

import java.util.List;

public final class BridgePattern {
    private BridgePattern() {
    }

    interface Renderer {
        String renderCircle(int radius);
    }

    static final class VectorRenderer implements Renderer {
        @Override
        public String renderCircle(int radius) {
            return "vector-circle:" + radius;
        }
    }

    static final class RasterRenderer implements Renderer {
        @Override
        public String renderCircle(int radius) {
            return "raster-circle:" + radius;
        }
    }

    static final class Circle {
        private final int radius;
        private final Renderer renderer;

        Circle(int radius, Renderer renderer) {
            this.radius = radius;
            this.renderer = renderer;
        }

        String draw() {
            return renderer.renderCircle(radius);
        }
    }

    public static List<String> demo() {
        return List.of(new Circle(5, new VectorRenderer()).draw(), new Circle(5, new RasterRenderer()).draw());
    }
}

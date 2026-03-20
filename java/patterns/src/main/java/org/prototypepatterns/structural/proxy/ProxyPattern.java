package org.prototypepatterns.structural.proxy;

public final class ProxyPattern {
    private ProxyPattern() {
    }

    public static final class RealImage {
        private static int loadCount;
        private final String path;

        public RealImage(String path) {
            this.path = path;
            loadCount++;
        }

        public String display() {
            return "display:" + path;
        }

        public static int loadCount() {
            return loadCount;
        }

        public static void reset() {
            loadCount = 0;
        }
    }

    public static final class ImageProxy {
        private final String path;
        private RealImage realImage;

        public ImageProxy(String path) {
            this.path = path;
        }

        public String display() {
            if (realImage == null) {
                realImage = new RealImage(path);
            }
            return realImage.display();
        }
    }

    public static boolean demo() {
        RealImage.reset();
        ImageProxy proxy = new ImageProxy("chart.png");
        String first = proxy.display();
        String second = proxy.display();
        return first.equals(second) && RealImage.loadCount() == 1;
    }
}

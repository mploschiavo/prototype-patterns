package org.prototypepatterns.structural.composite;

import java.util.ArrayList;
import java.util.List;

public final class CompositePattern {
    private CompositePattern() {
    }

    interface Node {
        int size();
    }

    static final class FileNode implements Node {
        private final int bytesSize;

        FileNode(int bytesSize) {
            this.bytesSize = bytesSize;
        }

        @Override
        public int size() {
            return bytesSize;
        }
    }

    static final class FolderNode implements Node {
        private final List<Node> children = new ArrayList<>();

        void add(Node node) {
            children.add(node);
        }

        @Override
        public int size() {
            return children.stream().mapToInt(Node::size).sum();
        }
    }

    public static int demo() {
        FolderNode root = new FolderNode();
        root.add(new FileNode(10));
        FolderNode nested = new FolderNode();
        nested.add(new FileNode(5));
        nested.add(new FileNode(15));
        root.add(nested);
        return root.size();
    }
}

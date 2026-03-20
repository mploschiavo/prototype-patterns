package org.prototypepatterns.behavioral.iterator;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public final class IteratorPattern {
    private IteratorPattern() {
    }

    public static final class Playlist implements Iterable<String> {
        private final List<String> songs;

        public Playlist(List<String> songs) {
            this.songs = songs;
        }

        @Override
        public Iterator<String> iterator() {
            return songs.iterator();
        }
    }

    public static List<String> demo() {
        List<String> result = new ArrayList<>();
        for (String song : new Playlist(List.of("intro", "verse", "outro"))) {
            result.add(song);
        }
        return result;
    }
}

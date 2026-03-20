package org.prototypepatterns.creational.builder;

import java.util.ArrayList;
import java.util.List;

public final class BuilderPattern {
    private BuilderPattern() {
    }

    public static final class House {
        public final List<String> rooms;
        public final boolean hasGarage;
        public final boolean hasGarden;

        private House(List<String> rooms, boolean hasGarage, boolean hasGarden) {
            this.rooms = rooms;
            this.hasGarage = hasGarage;
            this.hasGarden = hasGarden;
        }
    }

    public static final class HouseBuilder {
        private final List<String> rooms = new ArrayList<>();
        private boolean hasGarage;
        private boolean hasGarden;

        public HouseBuilder addRoom(String room) {
            rooms.add(room);
            return this;
        }

        public HouseBuilder withGarage() {
            hasGarage = true;
            return this;
        }

        public HouseBuilder withGarden() {
            hasGarden = true;
            return this;
        }

        public House build() {
            return new House(new ArrayList<>(rooms), hasGarage, hasGarden);
        }
    }

    public static House demo() {
        return new HouseBuilder().addRoom("Kitchen").addRoom("Office").withGarage().build();
    }
}

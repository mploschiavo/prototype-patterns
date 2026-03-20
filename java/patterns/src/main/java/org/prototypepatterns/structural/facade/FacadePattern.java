package org.prototypepatterns.structural.facade;

public final class FacadePattern {
    private FacadePattern() {
    }

    static final class Lights {
        String dim() {
            return "lights dimmed";
        }
    }

    static final class Projector {
        String on() {
            return "projector on";
        }
    }

    static final class SoundSystem {
        String surround() {
            return "surround enabled";
        }
    }

    static final class HomeTheaterFacade {
        private final Lights lights;
        private final Projector projector;
        private final SoundSystem soundSystem;

        HomeTheaterFacade(Lights lights, Projector projector, SoundSystem soundSystem) {
            this.lights = lights;
            this.projector = projector;
            this.soundSystem = soundSystem;
        }

        String watchMovie() {
            return lights.dim() + " | " + projector.on() + " | " + soundSystem.surround();
        }
    }

    public static String demo() {
        return new HomeTheaterFacade(new Lights(), new Projector(), new SoundSystem()).watchMovie();
    }
}

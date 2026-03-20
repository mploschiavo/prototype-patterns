class Lights {
  dim() {
    return "lights dimmed";
  }
}

class Projector {
  on() {
    return "projector on";
  }
}

class SoundSystem {
  surround() {
    return "surround enabled";
  }
}

class HomeTheaterFacade {
  constructor(lights, projector, sound) {
    this.lights = lights;
    this.projector = projector;
    this.sound = sound;
  }

  watchMovie() {
    return [this.lights.dim(), this.projector.on(), this.sound.surround()].join(" | ");
  }
}

function demo() {
  return new HomeTheaterFacade(new Lights(), new Projector(), new SoundSystem()).watchMovie();
}

module.exports = { HomeTheaterFacade, demo };

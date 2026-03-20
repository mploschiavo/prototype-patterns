class Light {
  on() {
    return "light:on";
  }
}

class LightOnCommand {
  constructor(light) {
    this.light = light;
  }

  execute() {
    return this.light.on();
  }
}

class RemoteButton {
  constructor(command) {
    this.command = command;
  }

  press() {
    return this.command.execute();
  }
}

function demo() {
  return new RemoteButton(new LightOnCommand(new Light())).press();
}

module.exports = { Light, LightOnCommand, RemoteButton, demo };

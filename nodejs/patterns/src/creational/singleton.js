class Configuration {
  static instance;

  constructor() {
    if (Configuration.instance) {
      return Configuration.instance;
    }
    this.settings = new Map();
    Configuration.instance = this;
  }

  set(key, value) {
    this.settings.set(key, value);
  }

  get(key) {
    return this.settings.get(key);
  }
}

function demo() {
  const first = new Configuration();
  const second = new Configuration();
  first.set("mode", "prototype");
  return first === second && second.get("mode") === "prototype";
}

module.exports = { Configuration, demo };

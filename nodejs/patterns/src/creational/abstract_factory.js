class LightButton {
  paint() {
    return "light-button";
  }
}

class DarkButton {
  paint() {
    return "dark-button";
  }
}

class LightCheckbox {
  paint() {
    return "light-checkbox";
  }
}

class DarkCheckbox {
  paint() {
    return "dark-checkbox";
  }
}

class LightThemeFactory {
  createButton() {
    return new LightButton();
  }

  createCheckbox() {
    return new LightCheckbox();
  }
}

class DarkThemeFactory {
  createButton() {
    return new DarkButton();
  }

  createCheckbox() {
    return new DarkCheckbox();
  }
}

function renderUi(factory) {
  return [factory.createButton().paint(), factory.createCheckbox().paint()];
}

function demo() {
  return renderUi(new DarkThemeFactory());
}

module.exports = { LightThemeFactory, DarkThemeFactory, demo };

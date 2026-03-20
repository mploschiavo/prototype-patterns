class HtmlButton {
  render() {
    return "<button>Submit</button>";
  }
}

class DesktopButton {
  render() {
    return "[DesktopButton: Submit]";
  }
}

class WebDialog {
  createButton() {
    return new HtmlButton();
  }

  renderDialog() {
    return this.createButton().render();
  }
}

class DesktopDialog {
  createButton() {
    return new DesktopButton();
  }

  renderDialog() {
    return this.createButton().render();
  }
}

function demo() {
  return [new WebDialog().renderDialog(), new DesktopDialog().renderDialog()];
}

module.exports = { HtmlButton, DesktopButton, WebDialog, DesktopDialog, demo };

class Memento {
  constructor(text) {
    this.text = text;
  }
}

class TextEditor {
  constructor() {
    this.text = "";
  }

  type(value) {
    this.text = value;
  }

  save() {
    return new Memento(this.text);
  }

  restore(memento) {
    this.text = memento.text;
  }
}

function demo() {
  const editor = new TextEditor();
  editor.type("draft");
  const checkpoint = editor.save();
  editor.type("final");
  editor.restore(checkpoint);
  return editor.text;
}

module.exports = { Memento, TextEditor, demo };

class Document {
  constructor(title, tags = []) {
    this.title = title;
    this.tags = tags;
  }

  clone() {
    return new Document(this.title, [...this.tags]);
  }
}

function demo() {
  const draft = new Document("Pattern Notes", ["draft"]);
  const copy = draft.clone();
  copy.tags.push("review");
  return draft.tags.length === 1 && copy.tags.length === 2;
}

module.exports = { Document, demo };

class GlyphStyleFactory {
  constructor() {
    this.cache = new Map();
  }

  getStyle(family, size, bold) {
    const key = `${family}:${size}:${bold}`;
    if (!this.cache.has(key)) {
      this.cache.set(key, { family, size, bold });
    }
    return this.cache.get(key);
  }
}

function demo() {
  const factory = new GlyphStyleFactory();
  const first = factory.getStyle("Fira Code", 12, false);
  const second = factory.getStyle("Fira Code", 12, false);
  return first === second;
}

module.exports = { GlyphStyleFactory, demo };

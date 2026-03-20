class RealImage {
  static loadCount = 0;

  constructor(path) {
    this.path = path;
    RealImage.loadCount += 1;
  }

  display() {
    return `display:${this.path}`;
  }
}

class ImageProxy {
  constructor(path) {
    this.path = path;
    this.realImage = null;
  }

  display() {
    if (!this.realImage) {
      this.realImage = new RealImage(this.path);
    }
    return this.realImage.display();
  }
}

function demo() {
  RealImage.loadCount = 0;
  const proxy = new ImageProxy("chart.png");
  const first = proxy.display();
  const second = proxy.display();
  return first === second && RealImage.loadCount === 1;
}

module.exports = { RealImage, ImageProxy, demo };

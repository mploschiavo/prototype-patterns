class VectorRenderer {
  renderCircle(radius) {
    return `vector-circle:${radius}`;
  }
}

class RasterRenderer {
  renderCircle(radius) {
    return `raster-circle:${radius}`;
  }
}

class Circle {
  constructor(radius, renderer) {
    this.radius = radius;
    this.renderer = renderer;
  }

  draw() {
    return this.renderer.renderCircle(this.radius);
  }
}

function demo() {
  return [new Circle(5, new VectorRenderer()).draw(), new Circle(5, new RasterRenderer()).draw()];
}

module.exports = { VectorRenderer, RasterRenderer, Circle, demo };

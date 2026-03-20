class AscendingSort {
  sort(data) {
    return [...data].sort((a, b) => a - b);
  }
}

class DescendingSort {
  sort(data) {
    return [...data].sort((a, b) => b - a);
  }
}

class SortContext {
  constructor(strategy) {
    this.strategy = strategy;
  }

  setStrategy(strategy) {
    this.strategy = strategy;
  }

  run(data) {
    return this.strategy.sort(data);
  }
}

function demo() {
  const context = new SortContext(new AscendingSort());
  const ascending = context.run([3, 1, 2]);
  context.setStrategy(new DescendingSort());
  const descending = context.run([3, 1, 2]);
  return [ascending, descending];
}

module.exports = { AscendingSort, DescendingSort, SortContext, demo };

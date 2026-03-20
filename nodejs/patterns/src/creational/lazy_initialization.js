class LazyDataset {
  constructor() {
    this.records = null;
    this.loadCount = 0;
  }

  getRecords() {
    if (!this.records) {
      this.loadCount += 1;
      this.records = ["row-1", "row-2", "row-3"];
    }
    return this.records;
  }
}

function demo() {
  const dataset = new LazyDataset();
  dataset.getRecords();
  dataset.getRecords();
  return dataset.loadCount === 1;
}

module.exports = { LazyDataset, demo };

class DataPipeline {
  run() {
    return [this.read(), this.transform(), this.write()];
  }

  read() {
    throw new Error("Not implemented");
  }

  transform() {
    throw new Error("Not implemented");
  }

  write() {
    throw new Error("Not implemented");
  }
}

class CsvPipeline extends DataPipeline {
  read() {
    return "read:csv";
  }

  transform() {
    return "transform:normalize";
  }

  write() {
    return "write:warehouse";
  }
}

function demo() {
  return new CsvPipeline().run();
}

module.exports = { CsvPipeline, demo };

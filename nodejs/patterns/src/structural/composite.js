class FileNode {
  constructor(bytesSize) {
    this.bytesSize = bytesSize;
  }

  size() {
    return this.bytesSize;
  }
}

class FolderNode {
  constructor() {
    this.children = [];
  }

  add(child) {
    this.children.push(child);
  }

  size() {
    return this.children.reduce((total, child) => total + child.size(), 0);
  }
}

function demo() {
  const root = new FolderNode();
  root.add(new FileNode(10));
  const nested = new FolderNode();
  nested.add(new FileNode(5));
  nested.add(new FileNode(15));
  root.add(nested);
  return root.size();
}

module.exports = { FileNode, FolderNode, demo };

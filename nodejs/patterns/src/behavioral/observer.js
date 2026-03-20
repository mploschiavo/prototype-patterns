class Subject {
  constructor() {
    this.observers = [];
  }

  subscribe(observer) {
    this.observers.push(observer);
  }

  setState(value) {
    this.observers.forEach((observer) => observer(value));
  }
}

function demo() {
  const events = [];
  const subject = new Subject();
  subject.subscribe((value) => events.push(value));
  subject.setState(7);
  return events;
}

module.exports = { Subject, demo };

class EmailNotifier {
  send(message) {
    return `email:${message}`;
  }
}

class SmsDecorator {
  constructor(wrapped) {
    this.wrapped = wrapped;
  }

  send(message) {
    return `${this.wrapped.send(message)}|sms:${message}`;
  }
}

class SlackDecorator {
  constructor(wrapped) {
    this.wrapped = wrapped;
  }

  send(message) {
    return `${this.wrapped.send(message)}|slack:${message}`;
  }
}

function demo() {
  const notifier = new SlackDecorator(new SmsDecorator(new EmailNotifier()));
  return notifier.send("build complete");
}

module.exports = { EmailNotifier, SmsDecorator, SlackDecorator, demo };

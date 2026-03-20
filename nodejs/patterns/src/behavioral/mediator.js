class ChatMediator {
  constructor() {
    this.participants = [];
  }

  register(participant) {
    this.participants.push(participant);
  }

  broadcast(sender, message) {
    this.participants.forEach((participant) => {
      if (participant !== sender) {
        participant.receive(message);
      }
    });
  }
}

class Participant {
  constructor(name, mediator) {
    this.name = name;
    this.inbox = [];
    this.mediator = mediator;
    mediator.register(this);
  }

  send(message) {
    this.mediator.broadcast(this, `${this.name}:${message}`);
  }

  receive(message) {
    this.inbox.push(message);
  }
}

function demo() {
  const mediator = new ChatMediator();
  const alex = new Participant("alex", mediator);
  const river = new Participant("river", mediator);
  alex.send("ready");
  return river.inbox;
}

module.exports = { ChatMediator, Participant, demo };

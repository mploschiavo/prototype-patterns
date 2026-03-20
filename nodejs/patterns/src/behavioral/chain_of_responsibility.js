class Handler {
  constructor(nextHandler = null) {
    this.nextHandler = nextHandler;
  }

  next(level) {
    if (!this.nextHandler) {
      return `unhandled:${level}`;
    }
    return this.nextHandler.handle(level);
  }
}

class TeamLeadHandler extends Handler {
  handle(level) {
    if (level <= 1) {
      return "team-lead";
    }
    return this.next(level);
  }
}

class ManagerHandler extends Handler {
  handle(level) {
    if (level <= 2) {
      return "manager";
    }
    return this.next(level);
  }
}

class DirectorHandler extends Handler {
  handle(level) {
    if (level <= 3) {
      return "director";
    }
    return this.next(level);
  }
}

function demo() {
  const chain = new TeamLeadHandler(new ManagerHandler(new DirectorHandler()));
  return [chain.handle(1), chain.handle(2), chain.handle(4)];
}

module.exports = { TeamLeadHandler, ManagerHandler, DirectorHandler, demo };

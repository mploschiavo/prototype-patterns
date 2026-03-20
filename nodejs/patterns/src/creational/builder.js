class House {
  constructor() {
    this.rooms = [];
    this.hasGarage = false;
    this.hasGarden = false;
  }
}

class HouseBuilder {
  constructor() {
    this.house = new House();
  }

  addRoom(room) {
    this.house.rooms.push(room);
    return this;
  }

  withGarage() {
    this.house.hasGarage = true;
    return this;
  }

  withGarden() {
    this.house.hasGarden = true;
    return this;
  }

  build() {
    const built = this.house;
    this.house = new House();
    return built;
  }
}

function demo() {
  return new HouseBuilder().addRoom("Kitchen").addRoom("Office").withGarage().build();
}

module.exports = { House, HouseBuilder, demo };

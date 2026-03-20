class CoarseGrainedOrder {
  constructor() {
    this.customerName = "";
    this.city = "";
  }

  setData(customerName, city) {
    this.customerName = customerName;
    this.city = city;
  }

  getData() {
    return [this.customerName, this.city];
  }
}

class CompositeOrderEntity {
  constructor() {
    this.order = new CoarseGrainedOrder();
  }

  setOrder(customerName, city) {
    this.order.setData(customerName, city);
  }

  readOrder() {
    return this.order.getData();
  }
}

function demo() {
  const entity = new CompositeOrderEntity();
  entity.setOrder("Sam", "Austin");
  return entity.readOrder();
}

module.exports = { CompositeOrderEntity, demo };

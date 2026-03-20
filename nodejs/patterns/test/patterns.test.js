const test = require("node:test");
const assert = require("node:assert/strict");

const singleton = require("../src/creational/singleton");
const factoryMethod = require("../src/creational/factory_method");
const abstractFactory = require("../src/creational/abstract_factory");
const builder = require("../src/creational/builder");
const prototype = require("../src/creational/prototype");
const objectPool = require("../src/creational/object_pool");
const lazyInitialization = require("../src/creational/lazy_initialization");

const adapter = require("../src/structural/adapter");
const decorator = require("../src/structural/decorator");
const composite = require("../src/structural/composite");
const facade = require("../src/structural/facade");
const proxy = require("../src/structural/proxy");
const bridge = require("../src/structural/bridge");
const flyweight = require("../src/structural/flyweight");
const compositeEntity = require("../src/structural/composite_entity");

const observer = require("../src/behavioral/observer");
const strategy = require("../src/behavioral/strategy");
const command = require("../src/behavioral/command");
const state = require("../src/behavioral/state");
const templateMethod = require("../src/behavioral/template_method");
const chainOfResponsibility = require("../src/behavioral/chain_of_responsibility");
const iterator = require("../src/behavioral/iterator");
const mediator = require("../src/behavioral/mediator");
const memento = require("../src/behavioral/memento");

test("singleton", () => {
  assert.equal(singleton.demo(), true);
});

test("factory method", () => {
  assert.deepEqual(factoryMethod.demo(), ["<button>Submit</button>", "[DesktopButton: Submit]"]);
});

test("abstract factory", () => {
  assert.deepEqual(abstractFactory.demo(), ["dark-button", "dark-checkbox"]);
});

test("builder", () => {
  const house = builder.demo();
  assert.deepEqual(house.rooms, ["Kitchen", "Office"]);
  assert.equal(house.hasGarage, true);
});

test("prototype", () => {
  assert.equal(prototype.demo(), true);
});

test("object pool", () => {
  assert.equal(objectPool.demo(), true);
});

test("lazy initialization", () => {
  assert.equal(lazyInitialization.demo(), true);
});

test("adapter", () => {
  assert.equal(adapter.demo(), 25.0);
});

test("decorator", () => {
  assert.equal(decorator.demo(), "email:build complete|sms:build complete|slack:build complete");
});

test("composite", () => {
  assert.equal(composite.demo(), 30);
});

test("facade", () => {
  assert.match(facade.demo(), /projector on/);
});

test("proxy", () => {
  assert.equal(proxy.demo(), true);
});

test("bridge", () => {
  assert.deepEqual(bridge.demo(), ["vector-circle:5", "raster-circle:5"]);
});

test("flyweight", () => {
  assert.equal(flyweight.demo(), true);
});

test("composite entity", () => {
  assert.deepEqual(compositeEntity.demo(), ["Sam", "Austin"]);
});

test("observer", () => {
  assert.deepEqual(observer.demo(), [7]);
});

test("strategy", () => {
  assert.deepEqual(strategy.demo(), [[1, 2, 3], [3, 2, 1]]);
});

test("command", () => {
  assert.equal(command.demo(), "light:on");
});

test("state", () => {
  assert.deepEqual(state.demo(), ["pending->paid", "paid->shipped", "shipped->shipped"]);
});

test("template method", () => {
  assert.deepEqual(templateMethod.demo(), ["read:csv", "transform:normalize", "write:warehouse"]);
});

test("chain of responsibility", () => {
  assert.deepEqual(chainOfResponsibility.demo(), ["team-lead", "manager", "unhandled:4"]);
});

test("iterator", () => {
  assert.deepEqual(iterator.demo(), ["intro", "verse", "outro"]);
});

test("mediator", () => {
  assert.deepEqual(mediator.demo(), ["alex:ready"]);
});

test("memento", () => {
  assert.equal(memento.demo(), "draft");
});

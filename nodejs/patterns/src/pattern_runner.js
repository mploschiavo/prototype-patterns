const singleton = require("./creational/singleton");
const factoryMethod = require("./creational/factory_method");
const abstractFactory = require("./creational/abstract_factory");
const builder = require("./creational/builder");
const prototype = require("./creational/prototype");
const objectPool = require("./creational/object_pool");
const lazyInitialization = require("./creational/lazy_initialization");

const adapter = require("./structural/adapter");
const decorator = require("./structural/decorator");
const composite = require("./structural/composite");
const facade = require("./structural/facade");
const proxy = require("./structural/proxy");
const bridge = require("./structural/bridge");
const flyweight = require("./structural/flyweight");
const compositeEntity = require("./structural/composite_entity");

const observer = require("./behavioral/observer");
const strategy = require("./behavioral/strategy");
const command = require("./behavioral/command");
const state = require("./behavioral/state");
const templateMethod = require("./behavioral/template_method");
const chainOfResponsibility = require("./behavioral/chain_of_responsibility");
const iterator = require("./behavioral/iterator");
const mediator = require("./behavioral/mediator");
const memento = require("./behavioral/memento");

const PATTERNS = [
  { id: "singleton", category: "creational", demo: singleton.demo },
  { id: "factory-method", category: "creational", demo: factoryMethod.demo },
  { id: "abstract-factory", category: "creational", demo: abstractFactory.demo },
  { id: "builder", category: "creational", demo: builder.demo },
  { id: "prototype", category: "creational", demo: prototype.demo },
  { id: "object-pool", category: "creational", demo: objectPool.demo },
  { id: "lazy-initialization", category: "creational", demo: lazyInitialization.demo },
  { id: "adapter", category: "structural", demo: adapter.demo },
  { id: "decorator", category: "structural", demo: decorator.demo },
  { id: "composite", category: "structural", demo: composite.demo },
  { id: "facade", category: "structural", demo: facade.demo },
  { id: "proxy", category: "structural", demo: proxy.demo },
  { id: "bridge", category: "structural", demo: bridge.demo },
  { id: "flyweight", category: "structural", demo: flyweight.demo },
  { id: "composite-entity", category: "structural", demo: compositeEntity.demo },
  { id: "observer", category: "behavioral", demo: observer.demo },
  { id: "strategy", category: "behavioral", demo: strategy.demo },
  { id: "command", category: "behavioral", demo: command.demo },
  { id: "state", category: "behavioral", demo: state.demo },
  { id: "template-method", category: "behavioral", demo: templateMethod.demo },
  { id: "chain-of-responsibility", category: "behavioral", demo: chainOfResponsibility.demo },
  { id: "iterator", category: "behavioral", demo: iterator.demo },
  { id: "mediator", category: "behavioral", demo: mediator.demo },
  { id: "memento", category: "behavioral", demo: memento.demo },
];

const patternById = new Map(PATTERNS.map((pattern) => [pattern.id, pattern]));

function normalizePatternId(patternId) {
  return String(patternId).trim().toLowerCase().replace(/[_\s]+/g, "-");
}

function listPatterns() {
  return PATTERNS.map(({ id, category }) => ({ id, category }));
}

function runPattern(patternId) {
  const normalized = normalizePatternId(patternId);
  const pattern = patternById.get(normalized);
  if (!pattern) {
    throw new Error(`Unknown pattern: ${patternId}`);
  }
  return pattern.demo();
}

function runAllPatterns() {
  const results = {};
  for (const pattern of PATTERNS) {
    results[pattern.id] = pattern.demo();
  }
  return results;
}

module.exports = {
  normalizePatternId,
  listPatterns,
  runPattern,
  runAllPatterns,
};

const test = require("node:test");
const assert = require("node:assert/strict");

const patternRunner = require("../src/pattern_runner");

test("pattern registry has all 24 patterns", () => {
  const patterns = patternRunner.listPatterns();
  assert.equal(patterns.length, 24);
  assert.deepEqual(patterns[0], { id: "singleton", category: "creational" });
  assert.deepEqual(patterns.at(-1), { id: "memento", category: "behavioral" });
});

test("runPattern supports normalized ids", () => {
  assert.equal(patternRunner.runPattern("singleton"), true);
  assert.deepEqual(patternRunner.runPattern("chain of responsibility"), ["team-lead", "manager", "unhandled:4"]);
});

test("runPattern throws for unknown pattern", () => {
  assert.throws(() => patternRunner.runPattern("no-such-pattern"), /Unknown pattern/);
});

test("runAllPatterns returns results for each pattern", () => {
  const results = patternRunner.runAllPatterns();
  assert.equal(Object.keys(results).length, 24);
  assert.equal(results.singleton, true);
});

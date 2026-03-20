#!/usr/bin/env node

const { listPatterns, runAllPatterns, runPattern } = require("./src/pattern_runner");

function usage() {
  console.error("Usage:");
  console.error("  node run-pattern.js --list");
  console.error("  node run-pattern.js --pattern <pattern-id>");
  console.error("  node run-pattern.js --all");
}

function main(argv) {
  if (argv.includes("--list")) {
    for (const { id, category } of listPatterns()) {
      console.log(`${id}\t${category}`);
    }
    return 0;
  }

  if (argv.includes("--all")) {
    const results = runAllPatterns();
    for (const [patternId, result] of Object.entries(results)) {
      console.log(`${patternId}: ${JSON.stringify(result)}`);
    }
    return 0;
  }

  const patternIndex = argv.indexOf("--pattern");
  if (patternIndex !== -1 && argv[patternIndex + 1]) {
    const patternId = argv[patternIndex + 1];
    try {
      const result = runPattern(patternId);
      console.log(`${patternId}: ${JSON.stringify(result)}`);
      return 0;
    } catch (error) {
      console.error(error.message);
      return 2;
    }
  }

  usage();
  return 1;
}

process.exitCode = main(process.argv.slice(2));

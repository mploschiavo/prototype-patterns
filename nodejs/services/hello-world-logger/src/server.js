const http = require("node:http");

function getMessage(logger = console) {
  logger.info("Handling hello-world-logger request");
  return "hello world with logger";
}

function createServer(logger = console) {
  return http.createServer((req, res) => {
    if (req.url !== "/") {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("not found");
      return;
    }

    const message = getMessage(logger);
    res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
    res.end(message);
  });
}

function main() {
  const port = Number(process.env.PORT || 8080);
  const server = createServer(console);
  server.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`Node hello-world-logger listening on :${port}`);
  });
}

if (require.main === module) {
  main();
}

module.exports = { getMessage, createServer };

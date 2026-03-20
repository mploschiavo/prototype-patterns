const http = require("node:http");

function getMessage() {
  return "hello world";
}

function createServer() {
  return http.createServer((req, res) => {
    if (req.url !== "/") {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("not found");
      return;
    }

    const message = getMessage();
    res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
    res.end(message);
  });
}

function main() {
  const port = Number(process.env.PORT || 8080);
  const server = createServer();
  server.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`Node hello-world listening on :${port}`);
  });
}

if (require.main === module) {
  main();
}

module.exports = { getMessage, createServer };

'use strict';

var http = require('http');

var server = http.createServer(function name(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('The request come form: ' + req.url + '\nHey! Fuuuu: ' + new Date().toISOString());
});


server.listen(3000, '127.0.0.1');

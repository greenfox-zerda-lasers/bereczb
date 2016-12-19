'use strict';

var express = require('express');

var exampleApp = express();


exampleApp.get('/*', function name(req, resp) {
  console.log(req.url);
  resp.send('curl localhost:3000/todos/ -s | python -m json.tool');
});


exampleApp.listen(3000);

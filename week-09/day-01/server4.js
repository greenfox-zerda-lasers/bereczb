'use strict';

var express = require('express');

var exampleApp = express();


exampleApp.get('/*', function name(req, resp) {
  resp.send('The request come form: ' + req.url + '\nHey! ' + new Date());
});


exampleApp.listen(3000);

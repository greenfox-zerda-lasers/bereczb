'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/', function barmi(request, response) {
  response.send('EEEEEEeeeeeeeeEEEEEE');
});

exampleApp.post('/', function barmi2(request, response) {
  response.send('you sent sg');
});

exampleApp.listen(3000);

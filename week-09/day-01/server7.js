'use strict';

var express = require('express');
var jason = require('./todos.json');
var app = express();

app.get('/todos', function a(req, res) {
 res.send(jason);
 });

app.listen(3000);

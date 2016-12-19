'use strict';

var express = require('express');

var jason = require('./todos.json');

var app = express();

app.get('/todos/:id', function a(req, res) {
  console.log(req.params.id);
  res.set('Content-Type', 'application/json');
  res.send(
    jason.filter( function(e){
      console.log(e);
      return parseInt(req.params.id) === e['id'];
   }));
});

app.listen(3000);

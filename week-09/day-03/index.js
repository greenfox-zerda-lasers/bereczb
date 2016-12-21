'use strict';

var mysql = require("mysql");
var express = require('express');

var app = express();

var connection = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "admin",
  database: "bookstore"
});

connection.connect(function (err) {
  if (err) {
    console.log("Error connecting to Db", err);
    return;
  }
  console.log("Connection established");
});

app.get('/', function(req, res) {
   connection.query("SELECT book_name FROM book_mast;", function(err,rows) {
      if (err) {
         console.log(err.toString());
         connection.end();
         return;
      }
      res.send(rows);
   });
});

app.listen(3000);

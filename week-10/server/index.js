'use strict';

// var port = process.env.PORT || 3000;

// var bodyParser = require('body-parser');
var express = require('express');
var mysql = require('mysql');
var app = express();
var playlist = [];

var connection = mysql.createConnection({
   host: 'localhost',
   user: 'root',
   password: 'admin',
   database: 'foxplayer'
});

connection.connect();

app.get('/playlists', function(req, res) {
   connection.query('SELECT * FROM playlists', function(err, rows, fields) {
      if (err) throw err;
      res.send(rows);
      playlist = rows;
   });
});

app.get('/create', function(req, res) {
	connection.query({
		sql: 'INSERT INTO playlists(playlist, system) VALUES(?, ?)',
		values: ['Hello', 0]
	}, function(err, rows, fields) {
		if (err) throw err;
  		res.send(rows);
	});
});

app.get('/delete', function(req, res) {
   connection.query('DELETE FROM playlists WHERE id = "7"', function(err, rows, fields) {
      if (err) throw err;
      res.send(rows);
   });
});

app.get('/playlist-tracks/:playlist_id', function(req, res) {
   connection.query('SELECT * FROM playlists WHERE id = ?', [2], function(err, rows, fields) {
      if (err) throw err;
      res.send(rows);
   });
});

app.listen(3000, function () {
  console.log('SERVER IS UP AND RUNNIN on port: 3000');
});

// app.use(bodyParser.json());

// app.get('/playlists', function (req, res) {
//   res.json(tracks);
// });
//
// app.get('/playlists/playlist', function (req, res) {
//   res.json(playlist);
// });
//
// app.get('/playlists/:id', function (req, res) {
//   res.send(tracks[req.params.id]);
// });
//
//
// app.delete('/playlists/:id', function (req, res) {
//   var newList = [];
//   for(let i = 0; i < tracks.length; i++){
//     if ( i != req.params.id) {
//       newList.push(tracks[i]);
//     }
//   }
//   tracks = newList
//   res.send(tracks);
// });
//
// app.post('/playlists', function (req, res) {
//   console.log(req.body);
//   tracks.push(req.body);
//   res.send(tracks)
// });
//
// app.get('/playlis-tracks/', function (req, res) {
//   res.send(playlist);
// });
//
// module.exports = app;

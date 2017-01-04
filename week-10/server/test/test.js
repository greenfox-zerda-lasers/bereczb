'use strict';

var test = require('tape');
var app = require("../server");
var request = require("supertest");


test('First test!', function (t) {
  t.end();
});

test('Correct users returned', function (t) {
  request(app)
    .get('/playlists')
    .expect('Content-Type', /json/)
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('Correct user returned', function (t) {
  request(app)
    .get('/playlists/0')
    .expect('John')
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('Correct playlist returned', function (t) {
  request(app)
    .get('/playlists/playlist')
    .expect('Content-Type', /json/)
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('Correct playlist returned', function (t) {
  request(app)
    .delete('/playlists/0')
    .expect(['Betty', 'Hal'])
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('Correct playlist returned', function (t) {
  request(app)
    .post('/playlists')
    .send({'alma': 'korte'})
    .expect(['Betty', 'Hal', {'alma': 'korte'}])
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('Correct playlist returned', function (t) {
  request(app)
    .get('/playlis-tracks/')
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

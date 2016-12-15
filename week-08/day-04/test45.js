'use strict';

var test = require('tape');
var shortestString = require('./45.js');

test('shortest element', function (t) {

   t.equal(shortestString(['sdfsa', 'sadf', 'v', 'sadf']), 'v');
   t.end();
});

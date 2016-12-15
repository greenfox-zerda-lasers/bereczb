'use strict';

var test = require('tape');
var evenList = require('./43.js');

test('list of even numbers', function (t) {

   t.deepEqual(evenList([10, 20, 30, 11, 21, 32]), [10, 20, 30, 32]);
   t.end();
});

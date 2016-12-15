'use strict';

var test = require('tape');
var double = require('./39.js');

test('double a number', function (t) {

   t.equal(double(111), 222);
   t.end();
});

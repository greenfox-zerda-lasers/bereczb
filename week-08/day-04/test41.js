'use strict';

var test = require('tape');
var sum = require('./41.js');

test('sum of elements', function (t) {

   t.equal(sum([1,1,1]), 3);
   t.end();
});

'use strict';

var test = require('tape');
var minimal = require('./44.js');

test('minimal element of a list', function (t) {

   t.equal(minimal([1, 2, 0, 3]), 0);
   t.end();
});

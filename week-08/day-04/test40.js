'use strict';

var test = require('tape');
var stringPlusA = require('./40.js');

test('add a string', function (t) {

   t.equal(stringPlusA('a'), 'aa');
   t.end();
});

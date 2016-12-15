'use strict';

var test = require('tape');
var factorial = require('./42.js');

test('factorial', function (t) {

   t.equal(factorial(5), 1*2*3*4*5);
   t.end();
});

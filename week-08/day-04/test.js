var test = require('tape');
var double = require('./39.js');
var stringPlusA = require('./40.js');
var sum = require('./41.js');
var factorial = require('./42.js');
var evenList = require('./43.js');
var minimal = require('./44.js');
var shortestString = require('./45.js');

test('double a number', function (t) {
    var actual = double(111);
    var expected = 222;

    t.equal(actual, expected);
    t.end();
});

'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(aSide, bSide) {
   this.aSide = aSide;
   this.bSide = bSide;
}

Rectangles.prototype.getArea = function() {
   return this.aSide * this.bSide;
}

Rectangles.prototype.getCircumference = function() {
      return (this.aSide + this.bSide) * 2;
}

var rect1 = new Rectangles(2, 2);
var rect2 = new Rectangles(1, 3);

console.log('Area: ', rect1.getArea(), 'Circumference: ', rect1.getCircumference())
console.log('Area: ', rect2.getArea(), 'Circumference: ', rect2.getCircumference())

'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack() {
   this.element = [];
   this.size = function() {
      return this.element.length;
   };
   this.push = function(element) {
      this.element[this.element.length] = element
   };
   this.pop = function() {
      var lastElement = this.element[this.element.length-1];
      this.element.length = this.element.length - 1;
      return lastElement;
   }
}

var element1 = new Stack();

element1.size();

element1.push(1);
element1.push(4);
element1.push(6);
element1.push(9);
element1.push(51);
element1.push(45);

console.log(element1.size());
console.log(element1.element);
console.log(element1.pop());
console.log(element1.element);

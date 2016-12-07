'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

function toEnglish(inputNumber) {
   switch (inputNumber) {
      case 0:
         return 'zero';
      case 1:
         return 'one';
      case 2:
         return 'two';
      case 3:
         return 'three';
      case 4:
         return 'four';
      case 5:
         return 'five';
      default:
         return 'many';
   }
}

console.log(toEnglish(1));
console.log(toEnglish(5));
console.log(toEnglish(3));
console.log(toEnglish(11));

'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function isInString(inputString, inputLetter) {

   return inputString.split('').some(function(e){
      return e === inputLetter;
   })

}

console.log(isInString('kutya', 'a'));
console.log(isInString('kutya', 'z'));

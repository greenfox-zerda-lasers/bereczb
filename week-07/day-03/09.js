'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function letterCounter(inputString) {

   var listOfLetters = inputString.split('');
   var counts = {};
   var letter;

   for (var i = 0; i < listOfLetters.length; i++) {

      letter = listOfLetters[i];
      console.log(letter + '-' + counts[letter]);

      if (counts[letter]) {
         counts[letter]++;
      } else {
         counts[letter] = 1;
      }

      console.log(counts)

   }
   return counts;
}

console.log(letterCounter('apple'))

'use strict';

// Remove the king from the list.
// Add 3 list items saying 'The Fox' to the list.

var listOfAsteroids = document.querySelector('.asteroids');
var toRemove = document.querySelector('li');

listOfAsteroids.removeChild(toRemove);

var newFox = []

for (var i = 0; i < 3; i++) {
   newFox[i] = document.createElement('li');
   newFox[i].innerText = 'The Fox';
   listOfAsteroids.appendChild(newFox[i]);
}

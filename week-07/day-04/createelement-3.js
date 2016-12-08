'use strict';

// Remove the king from the list.
// Add list items that have the following text contents:
// ['apple', 'bubble', 'cat', 'green fox']

var asteroidList = document.querySelector('.asteroids');
var toRemove = document.querySelector('li');

asteroidList.removeChild(toRemove);

var newItemsText = ['apple', 'bubble', 'cat', 'green fox'];
var newItems = []


for (var i = 0; i < newItemsText.length; i++) {
   newItems[i] = document.createElement('li');
   newItems[i].innerText = newItemsText[i];
   asteroidList.appendChild(newItems[i]);
}

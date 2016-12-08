'use strict';

// Remove the king from the list.
// Fill the list based on the following list of objects:
var planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]
// only add the asteroids to the list.
// each list item should have its category as a class
// and its content as text content.

var asteroidList = document.querySelector('.asteroids');
var toRemove = document.querySelector('li');

asteroidList.removeChild(toRemove);

var newItems = []
var j = 0

for (var i = 0; i < planetData.length; i++) {

   if (planetData[i]['asteroid']) {
      newItems[j] = document.createElement('li');
      newItems[j].innerText = planetData[i]['content'];
      newItems[j].classList.add(planetData[i]['category']);
      asteroidList.appendChild(newItems[j]);
      j++
   };

};

'use strict';

// Add an item that says 'The Green Fox' to the asteroid list.
// Add an item that says 'The Lamplighter' to the asteroid list.
// Add a heading saying 'I can add elements to the DOM!' to the .container.
// Add an image, any image, to the container.

var asteroidList = document.querySelector('ul.asteroids');
var newAsteroid = document.createElement('li');

newAsteroid.innerText = 'The Green Fox';
asteroidList.appendChild(newAsteroid);

newAsteroid = document.createElement('li');

newAsteroid.innerText = 'The Lamplighter';
asteroidList.appendChild(newAsteroid);

var containerElement = document.querySelector('div.container');
var newElement = document.createElement('h1');

newElement.innerText = 'I can add elements to the DOM!';
containerElement.appendChild(newElement);

var newImage = document.createElement('img');

newImage.setAttribute('src', 'bereczb.jpg');
newImage.setAttribute('width', '180');
containerElement.appendChild(newImage);

console.log(asteroidList);

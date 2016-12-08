'use strict';

// Write the image's url to the console.
// Replace the image with a picture of yourself.
// Make the link point to the Green Fox Academy website.
// Disable the second button.
// Replace its text with 'Don't click me!'.

var imageDetails = document.querySelector('img');
console.log(imageDetails.getAttribute('src'));

imageDetails.setAttribute('src', 'bereczb.jpg');
imageDetails.setAttribute('width', '180');

var linkDetails = document.querySelector('a');
linkDetails.setAttribute('href', 'http://www.greenfoxacademy.com/');
console.log(linkDetails.getAttribute('href'));

var buttonDetails = document.querySelector('.this-one');
buttonDetails.disabled = true;
buttonDetails.innerText = 'Don\'t click me!';

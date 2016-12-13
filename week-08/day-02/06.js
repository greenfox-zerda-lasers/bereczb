'use strict';

// Add an event listener to the window and display the mouse's x, y coordinates

var h1ToDispCoords = document.querySelector('h1');

var cursorX;
var cursorY;

window.addEventListener("mousemove", function(e) {
   cursorX = e.clientX;
   cursorY = e.clientY;
   h1ToDispCoords.innerHTML = 'X: ' + cursorX + ' Y: ' + cursorY;
});

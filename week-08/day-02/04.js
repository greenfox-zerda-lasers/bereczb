'use strict';

// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)

var cursorX;
var cursorY;

document.onmousemove = function(e){
   cursorX = e.pageX;
   cursorY = e.pageY;
}

function dispCoords() {
   console.log('x=', cursorX, ' y=', cursorY);
   setTimeout(dispCoords, 1500);
}

dispCoords();

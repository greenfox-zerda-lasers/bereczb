'use strict';

// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout

var timeoutID;

function startSetTimeout() {
   timeoutID = setTimeout(timeoutMessage, 3000);
}

function timeoutMessage() {
   console.log('EEEee');
}

function stopTimer() {
   clearTimeout(timeoutID);
   console.log('Stopped');
}

var button = document.querySelector("button");
button.addEventListener("click", stopTimer, false);

startSetTimeout();

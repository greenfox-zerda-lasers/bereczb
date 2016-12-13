'use strict';

// Add a click event listener to a <button> and console.log its innerHTML

var button = document.querySelector('button');
button.addEventListener('click', displInnetHTML, false);

function displInnetHTML() {
   console.log(button.innerHTML);
}

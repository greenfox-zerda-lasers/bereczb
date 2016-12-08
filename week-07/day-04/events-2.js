'use strict';

// On the click of the button,
// Count the items in the list
// And display the result in the result element.

var button = document.querySelector('button');
var listOfItems = document.querySelectorAll('li');
var resultOfCount = document.querySelector('.result');

function countList() {

   resultOfCount.innerText = listOfItems.length;

}


button.addEventListener('click', countList);

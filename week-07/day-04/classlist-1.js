'use strict';

  // Does the third p have a cat class?
  // If so, alert 'YEAH CAT!'
  // If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
  // If the first p has an 'apple' class, replace cat's content with 'dog'
  // Make apple red
  // Make balloon less balloon-like

var paragr = document.querySelectorAll('p');
var apples = document.querySelector('.apple');
var cats = document.querySelector('.cat');


if (paragr[2].classList.contains('cat')){
   console.log('YEAH CAT!');
};

if (paragr[3].classList.contains('dolphin')) {
   apples.innerText = 'pear';
}

if (paragr[0].classList.contains('apple')) {
   cats.innerText = 'dog';
}

apples.classList.add('red');
paragr[1].classList.remove('balloon');

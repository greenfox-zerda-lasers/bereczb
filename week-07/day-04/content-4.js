'use strict';

// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']

var newList = ['apple', 'banana', 'cat', 'dog'];

var oldList = document.getElementsByTagName('li');

for (var i = 0; i < oldList.length; i++) {

   oldList[i].innerText = newList[i];

};

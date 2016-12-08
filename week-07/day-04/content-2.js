'use strict';

// fill every paragraph with the last one's content.

var contents = document.getElementsByTagName('p');

for (var i = 0; i < contents.length-1; i++) {

   contents[i].innerHTML = contents[contents.length-1].innerHTML;
}

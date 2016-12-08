'use strict';

// Create a script that replaces every h1 headline's content
// with 'Green Fox Academy Conquers the World'.
// Create a bookmarklet that does that on any website.

(function(){
var headlines = document.querySelectorAll('h1');

for (var i = 0; i < headlines.length; i++) {
      headlines[i].innerText = 'Green Fox Academy Conquers the World';
}
})()

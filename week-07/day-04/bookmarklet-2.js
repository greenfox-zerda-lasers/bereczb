'use strict';

// Create a script that replaces every image
// with this: http://bit.ly/lpgreenfox
// Create a bookmarklet that does that on any website.

(function(){
var imagesToChange = document.querySelectorAll('img');

for (var i = 0; i < imagesToChange.length; i++) {
      imagesToChange[i].setAttribute('src', 'http://bit.ly/lpgreenfox');
}
})()

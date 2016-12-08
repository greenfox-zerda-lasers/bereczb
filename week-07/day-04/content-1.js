'use strict';

  // 1. Alert the content of the heading.
var head1 = document.getElementsByTagName('h1');
window.alert(head1[0].innerText);

  // 2. Write the content of the first paragraph to the console.
var paragr = document.getElementsByTagName('p');
console.log(paragr[0].innerText);

  // 3. Alert the content of the second paragraph.
window.alert(paragr[1].innerText);

  // 4. Replace the heading's content with 'New content'.
head1[0].innerText = 'New content';

  // 5. Replace the last paragraph's content with the first paragraph's content.
paragr[paragr.length-1].innerText = paragr[0].innerText

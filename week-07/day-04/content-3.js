'use strict';

  // fill output1 with the first paragraph's content, text only.
  // fill output2 with the first paragraph's content keeping the cat strong.

var paragraphs = document.getElementsByTagName('p');

paragraphs[1].innerText = paragraphs[0].innerText;
paragraphs[2].innerHTML = paragraphs[0].innerHTML;

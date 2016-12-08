'use strict';

var king = document.getElementById('b325');
console.log(king);

var conceited = document.getElementsByClassName('b326');
window.alert(conceited);

var businessLamp = document.getElementsByClassName('big');
console.log(businessLamp);

var conceitedKing = document.querySelectorAll('.container .asteroid');
for (var i = 0; i < conceitedKing.length; i++){
  window.alert(conceitedKing[i].innerText);
};

var noBusiness = document.querySelectorAll('#b325, .b326, .b329');
for (var i = 0; i < noBusiness.length; i++){
   console.log(noBusiness[i].innerText);
};

var allBizniss = document.getElementsByTagName('p');
window.alert(allBizniss[0].innerText);

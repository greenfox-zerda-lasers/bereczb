'use strict';

// Turn the party on and off by clicking the button.

var button = document.querySelector('button');
var partyStatus

function partyOnOFF() {
   partyStatus = document.querySelector('body');
   if (partyStatus.classList.contains('party')) {
      partyStatus.classList.remove('party');
   } else {
      partyStatus.classList.add('party');
   }

}

button.addEventListener('click', partyOnOFF);

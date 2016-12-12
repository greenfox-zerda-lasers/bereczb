'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals(talk) {
   this.talk = talk;
}

var kutya = new Animals('vau');
var tehen = new Animals('muuu');

Animals.prototype.say = function() {
   console.log(this.talk);
}

kutya.say();
tehen.say();

'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rockets(consumption) {
   this.consumption = consumption;
}

Rockets.prototype.fill = function(amount) {
   this.fuel = amount;
}

Rockets.prototype.launch = function() {
   if (this.fuel >= this.consumption) {
      console.log(this, 'launch');
      this.fuel -= this.consumption;
   }
   console.log(this, 'fuel: ', this.fuel);
}

var rocket1 = new Rockets(100);
var rocket2 = new Rockets(150);

rocket1.fill(110);
rocket2.fill(140);

rocket1.launch();
rocket2.launch();

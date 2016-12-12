'use strict';

// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function Aircrafts(type) {
   this.type = type;
   this.ammo = 0;
   if (this.type === 'F16') {
      this.maxAmmo = 8;
      this.baseDamage = 30;
   } else if (this.type === 'F35') {
      this.maxAmmo = 12;
      this.baseDamage = 50;
   }
}

function Carriers(totalAmmo) {
   this.totalAmmo = totalAmmo;
   this.health = 3000;
   this.aircraftList = [];
}

Aircrafts.prototype.fight = function() {
   var damageInflicted = this.ammo * this.baseDamage;
   this.ammo = 0;
   return damageInflicted;
}

Aircrafts.prototype.refill = function(roundsOfAmmo) {
   var remainingAmmo = roundsOfAmmo + this.ammo - this.maxAmmo;

   if (remainingAmmo >= 0) {
      this.ammo = this.maxAmmo;
      return remainingAmmo;
   } else {
      this.ammo += roundsOfAmmo;
      return 0;
   }
}

Carriers.prototype.status_report = function() {
   var totalDamage = 0;
   if (this.health <= 0) {
      return 'It\'s dead Jim :('
   }
   this.aircraftList.forEach(function(e) {
      totalDamage += e.baseDamage * e.ammo;
   });
   console.log('Aircrafts:');
   console.log('Aircraft count: ' + this.aircraftList.length + ', Ammo Storage: ' + this.totalAmmo + ', Total damage: ' + totalDamage + ', Health remaining: ' + this.health);
   this.aircraftList.forEach(function(e) {
      console.log('Type ' + e.type + ', Ammo: ' + e.ammo + ', Base Damage: ' + e.baseDamage + ', All Damage:', e.ammo * e.baseDamage);
   });
}

Carriers.prototype.addAircraft = function(newAircraft) {
   this.aircraftList.push(newAircraft);
}

Carriers.prototype.fill = function() {
   this.aircraftList.forEach(function(e) {
      this.totalAmmo = e.refill(this.totalAmmo);
   }, this);
}

Carriers.prototype.fight = function() {
   var totalAmountOfDamage = 0;
   this.aircraftList.forEach(function(e) {
      totalAmountOfDamage += e.fight();
   });
   return totalAmountOfDamage;
}

var plane1 = new Aircrafts('F16');
var plane2 = new Aircrafts('F35');
var plane3 = new Aircrafts('F35');
var plane4 = new Aircrafts('F35');
var plane5 = new Aircrafts('F16');
var plane6 = new Aircrafts('F16');
var plane7 = new Aircrafts('F35');

var carrier = new Carriers(70);

carrier.addAircraft(plane1);
carrier.addAircraft(plane2);
carrier.addAircraft(plane3);
carrier.addAircraft(plane4);
carrier.addAircraft(plane5);
carrier.addAircraft(plane6);
carrier.addAircraft(plane7);

// console.log(carrier);
carrier.status_report();

carrier.fill();

// console.log(carrier);
carrier.status_report();

// console.log(carrier.fight());

// console.log(carrier);

carrier.status_report();

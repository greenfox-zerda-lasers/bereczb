'use strict';

// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk

function tour(walk, distance) {
   return walk(distance(5));
}

function walk(funct) {
   var result = funct;
   for (var i = 0; i < result.length; i++) {
      result[i] = true;
   }
   return result;
}

function distance(lengthParam) {
   var result = [];
   for (var i = 0; i < lengthParam; i++) {
      result.push('false');
   }
   return result;
}

console.log(tour(walk, distance));

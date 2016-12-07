'use strict';

var students = [
  {name: 'Rezso', age: 9.5, candies: 2},
  {name: 'Gerzson', age: 10, candies: 1},
  {name: 'Aurel', age: 7, candies: 3},
  {name: 'Zsombor', age: 12, candies: 5},
  {name: 'Olaf', age: 12, candies: 7},
  {name: 'Teodor', age: 3, candies: 2}
];


// create a function that counts the students that
// has more than 4 candies

function counter(students) {

   var numberOfStudents = 0;
   for (var i = 0; i < students.length; i++) {
      if (students[i].candies > 4) {
         numberOfStudents++;
      }
   }
   return numberOfStudents;
}

//====================================7

function counter2(students) {

   return students.filter(function(e){
      return e['candies'] > 4;
   }).length

}

console.log(counter(students));
console.log(counter2(students));

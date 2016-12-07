'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
   grades: [],
   addGrade: function(grade) {
      if (grade <= 5 && grade >= 1 && grade % 1 === 0) {
         this.grades.push(grade);
      }
   },
   getAverage: function() {
      var sumOfGrades = 0;
      for (var i = 0; i < this.grades.length; i++){
         sumOfGrades += this.grades[i];
      }
      return sumOfGrades / this.grades.length;
   }
};

student.addGrade(1)
student.addGrade(2)
student.addGrade(3)
student.addGrade(3)
student.addGrade(1.3)
student.addGrade('nyenye')
console.log(student.grades)
console.log(student.getAverage())

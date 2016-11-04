# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student(object):

    list_of_grades = []

    def add_grade(self, grade):
        self.grade = grade
        self.list_of_grades.append(self.grade)

    def get_average(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)

geza = Student()

geza.add_grade(5)
geza.add_grade(2)
geza.add_grade(3)
geza.add_grade(1)
geza.add_grade(5)

print(geza.list_of_grades)
print(geza.get_average())

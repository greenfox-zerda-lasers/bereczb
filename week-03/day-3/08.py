# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(self.first_name, self.last_name)

class Student(Person):

    list_of_grades = []

    def add_grade(self, grade):
        self.grade = grade
        self.list_of_grades.append(self.grade)

    def salute(self):
        print(self.greet(), sum(self.list_of_grades) / len(self.list_of_grades))

rezso = Student('Rezso', 'Nagy')

rezso.add_grade(5)
rezso.add_grade(2)
rezso.add_grade(3)
rezso.add_grade(1)
rezso.add_grade(5)

# print(rezso.list_of_grades)

rezso.salute()

# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():
    elements = []

    def size(self):

        number_of_elements = 0

        for i in self.elements:
            number_of_elements += 1
        return number_of_elements

    def push(self, number):
        self.elements = self.elements + [number]

    def pop(self):
        result = self.elements[-1]
        self.elements = self.elements[:-1]
        return result

element = Stack()

element.push(5)
element.push(3)
element.push(4)
element.push(8)

print(element.size())
print(element.elements)

print(element.pop())
print(element.elements)
print(element.pop())
print(element.elements)

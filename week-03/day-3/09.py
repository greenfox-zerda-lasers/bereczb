# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def triangle(param):
    for i in range(param):
        print('*' * i)

triangle(10)

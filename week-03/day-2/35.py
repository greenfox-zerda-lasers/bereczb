# create a function that returns it's input factorial

def factorial(number):
    result = 1
    for i in range(1, (number + 1)):
        result *= i
    return result

print(factorial(9))

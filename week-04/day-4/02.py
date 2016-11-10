
# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def add_numbers(number):
    if number <= 1:
        return 1
    else:
        return number + add_numbers(number - 1)

print(add_numbers(4))

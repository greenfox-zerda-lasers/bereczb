# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def count(number):
    if number <= 0:
        print (0)
        return 0
    else:
        print (number)
        return count(number - 1)

count(15)

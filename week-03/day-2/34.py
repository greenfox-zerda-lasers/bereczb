numbers = [4, 5, 6, 7, 8, 9, 10, 'lekvar', 12]
# write your own sum function

def summary(list):
    result = 0
    for i in list:
        if (type(i) == int) or (type(i) == float):
            result = result + i
    return result

print(summary(numbers))

# create a function that takes a list and returns a new list with all the elements doubled

def double(list1):
    result = []
    for i in list1:
        result = result + [i * 2]

    return result

print(double([1,2,3,4,5,6]))

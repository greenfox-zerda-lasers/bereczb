# create a function that takes a list and returns a new list that is reversed
def list_reverse(list1):
    result = []
    for i in range(len(list1)-1, -1, -1):
        result = result + [list1[i]]
    return result

print(list_reverse([1,2,3,4,5,6]))

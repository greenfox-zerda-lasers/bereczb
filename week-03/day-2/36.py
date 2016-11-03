numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def rev(list):
    list.reverse()
    return list

def rev2(list):
    new_list = []
    for i in range(len(list)-1, -1, -1):
        new_list.append(list[i])
    return new_list

print(rev(numbers))
print(numbers)
print(rev2(numbers))
print(numbers)

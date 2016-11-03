def union(input_list1, input_list2):

    return set(input_list1) | set(input_list2)

def union2(input_list1, input_list2):

    result = list(input_list1)

    for i in input_list2:
        match = 0
        for j in input_list1:
            if j == i:
                match = 1
        if match == 0:
            result.append(i)
    return result

print(union([4,5,6], [1,2,3]))
print(union([4,5,7], [4,1,7]))

print(union2([4,5,6], [1,2,3]))
print(union2([4,5,7], [4,1,7]))

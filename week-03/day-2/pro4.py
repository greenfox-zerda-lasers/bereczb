a = [4,5,6,1,3,2]
b = [4,5,7,3,2,1]

def bubble_sort(inp_list):
    change = True
    while change == True:
        change = False
        for i in range(0, (len(inp_list) - 1)):
            if inp_list[i] > inp_list[i + 1]:
                inp_list[i], inp_list[i + 1] = inp_list[i + 1], inp_list[i]
                change = True
    return inp_list

def binary_search(list1, param):

    list1 = bubble_sort(list1)
    result = False
    print(list1)

    while (result != True) and (len(list1) > 1) and (list1[-1] >= param) and (list1[0] <= param):
        print(list1[int((len(list1)) / 2)])
        if param == (list1[int((len(list1)) / 2)]):
            result = True

        elif param > (list1[int((len(list1)) / 2)]):
            list1 = list1[ int((len(list1) / 2)):]

        else:
            list1 = list1[ :int(( len(list1) / 2))]
        print(list1)


    return result



print(binary_search(a, 6))
print(binary_search(b, 6))

# expected output: true


# expected output: false

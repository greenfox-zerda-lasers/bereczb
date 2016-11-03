list1 = [3,9,4,5,2,1]

def bubble_sort(inp_list):
    change = True
    while change == True:
        change = False
        for i in range(0, (len(inp_list) - 1)):
            if inp_list[i] > inp_list[i + 1]:
                inp_list[i], inp_list[i + 1] = inp_list[i + 1], inp_list[i]
                change = True
    return inp_list

print(bubble_sort(list1))


# [3,9,4,5,2,1]
# expected output: [1,2,3,4,5,9]

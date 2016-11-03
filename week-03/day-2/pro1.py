def linear_search(input_list, input_elem):

    for i in range(len(input_list)):
        if input_list[i] == input_elem:
            return i
    return -1

print (linear_search([4,5,6], 6))

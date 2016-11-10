# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def addnumber(lista):
    if len(lista) == 0:
        return 0
    elif type(lista[0]) == list:
        return addnumber(lista[0]) + addnumber(lista[1:])
    else:
        return lista[0] + addnumber(lista[1:])

print(addnumber([1, 2, [3, 4], 1, [1, [2, 4]]]))

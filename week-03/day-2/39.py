names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list
#


def shortest(lista):
    result = lista[0]
    for i in lista:
        if len(i) < len(result):
            result = i
    return result

print(shortest(names))

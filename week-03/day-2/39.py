names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def shortest(lista):
    result = lista[0]
    for i in range(1, len(lista)):
        if len(lista[i]) < len(result):
            result = lista[i]
    return result

print(shortest(names))

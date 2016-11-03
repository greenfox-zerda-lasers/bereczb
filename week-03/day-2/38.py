numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def minimum(lista):
    result = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < result:
            result = lista[i]
    return result

print(minimum(numbers))

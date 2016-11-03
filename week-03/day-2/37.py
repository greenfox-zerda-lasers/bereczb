numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def odd_num(lista):
    even = []
    for i in range(len(lista)):
        if (lista[i] % 2) == 0:
            even.append(lista[i])
    return even

print(odd_num(numbers))

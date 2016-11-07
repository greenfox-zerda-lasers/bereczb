# Create a method that returns the five most frequent lottery number in a pretty table format
# from prettytable import from_csv

from prettytable import from_csv

def five_most_frequent():

    f = open('otos.csv')
    lista = f.readlines()
    f.close()

    lista2 = []
    lista3 = []
    new_row = []
    list_of_numbers = {}
    top5 = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0]}

    for row in lista:
        semicolon = 0

        for charact in range(len(row)-1):
            if row[charact] == ';':
                semicolon += 1
                if semicolon == 11:
                    new_row = row[charact+1:-1]
                    lista2 = lista2 + [new_row]
                    continue

    for numbers in lista2:
        splited_numbers = numbers.split(';')
        lista3 += splited_numbers

    for i in range(len(lista3)):
        lista3[i] = int(lista3[i])

    for i in range(1, 91):
        list_of_numbers[i] = lista3.count(i)

    for i in range(1, 6):
        for j in range(1, 91):
            if list_of_numbers[j] > top5[i][1]:
                top5[i] = [j, list_of_numbers[j]]
        list_of_numbers[top5[i][0]] = 0

    print(list_of_numbers)
    print(top5)

    f = open('topfive.csv', 'w')
    f.write('number')
    f.write(';')
    f.write('frequency')
    f.write('\n')
    for i in range(1, 6):
        f.write(str(top5[i][0]))
        f.write(';')
        f.write(str(top5[i][1]))
        f.write('\n')
    f.close()

    f = open("topfive.csv", "r")
    result = from_csv(f)
    f.close()

    return result

five_most_frequent()

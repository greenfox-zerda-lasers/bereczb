# Create a method that returns the five most frequent lottery number in a pretty table format
# from prettytable import from_csv

from prettytable import from_csv

def five_most_frequent():

    f = open('otos.csv')
    lista = f.readlines()
    f.close()

    weekly_numbers = []
    list_of_numbers = []
    new_row = []
    dict_of_numbers = {}
    top5 = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0]}

    for row in lista:
        semicolon = 0

        for charact in range(len(row)-1):
            if row[charact] == ';':
                semicolon += 1
                if semicolon == 11:
                    new_row = row[charact+1:-1]
                    weekly_numbers = weekly_numbers + [new_row]

    print('weekly_numbers in a list by weeks: ', weekly_numbers, '\n')

    for numbers in weekly_numbers:
        splited_numbers = numbers.split(';')
        list_of_numbers += splited_numbers

    print('list of numbers in string format (order of appearence): ', list_of_numbers,'\n')

    for i in range(len(list_of_numbers)):
        list_of_numbers[i] = int(list_of_numbers[i])

    print('list of numbers in integer format (order of appearence): ', list_of_numbers, '\n')

    for i in range(1, 91):
        dict_of_numbers[i] = list_of_numbers.count(i)

    print('dictionary of numbers: ', dict_of_numbers, '\n')

    for i in range(1, 6):
        for j in range(1, 91):
            if dict_of_numbers[j] > top5[i][1]:
                top5[i] = [j, dict_of_numbers[j]]
        dict_of_numbers[top5[i][0]] = 0
        print('top5 step', i, ':  ', top5)

    print('\ndictionary of numbers after selection: ', dict_of_numbers, '\n')

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

print(five_most_frequent())

# class Cows_and_bulls():
#
#     def random_number(self):

import random

def rand_number():
    list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    goal = []
    for i in range(4):
        rand_position = random.randrange(0, len(list_of_numbers))
        goal += [list_of_numbers.pop(rand_position)]
    return goal

def counter():
    pass

def guess_eval(guess):
    list_of_guess = list(guess)
    

# cob = Cows_and_bulls()

# print(rand_number())

# guess = input('Guess? ')

print(guess_eval('5432'))

import random

def guess():
    return int(input('your guess? '))

number = int(random.random() * 100)

guess_number = 0

while True:
    guess_var = guess()
    guess_number += 1
    if guess_var > number:
        print('lower')
    elif guess_var < number:
        print('higher')
    else:
        print('congrat!', guess_number, 'th try')
        break

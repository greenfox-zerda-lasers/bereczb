import random

def random_word():

    f = open('words.txt', 'r')
    lines = f.readlines()
    f.close()

    picked_word = lines[random.randint(0, len(lines))]
    return picked_word[:-1]

import random

def random_enemy_move():
    random_direction = random.randint(1, 4)
    if random_direction == 1:
        return 'up'
    elif random_direction == 2:
        return 'down'
    elif random_direction == 3:
        return 'left'
    elif random_direction == 4:
        return 'right'


print(random_enemy_move())
print(random_enemy_move())
print(random_enemy_move())
print(random_enemy_move())
print(random_enemy_move())
print(random_enemy_move())
print(random_enemy_move())
print(random_enemy_move())

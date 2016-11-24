import random

class Map_of_game:
    def __init__(self):
        self.read_map()

    def read_map(self):
        f = open('map.txt', 'r')
        self.map_list = f.readlines()
        f.close()
        for i in range(len(self.map_list)):
            self.map_list[i] = self.map_list[i][:-1]
            self.map_list[i] = self.map_list[i].split(';')

    def get_map(self):
        return self.map_list

    def get_number_of_skeletons(self):
        return random.randint(2, 5)

class Character:

    def move_up(self, char_pos_x, char_pos_y, ishero=False):
        self.ishero = ishero
        self.char_pos_x, self.char_pos_y = char_pos_x, char_pos_y
        self.character_position(self.char_pos_x, self.char_pos_y)
        if (self.row > 0 and self.map_of_game.map_list[self.row-1][self.column] == '0') or (self.row > 0 and self.map_of_game.map_list[self.row-1][self.column] == 'C' and self.ishero == True):
            self.deltay = -72
            self.char_pos_y -= 72
            self.map_of_game.map_list[self.row-1][self.column] = 'C'
            self.map_of_game.map_list[self.row][self.column] = '0'
        else:
            self.deltay = 0
        self.deltax = 0
        return self.char_pos_y

    def move_down(self, char_pos_x, char_pos_y, ishero=False):
        self.ishero = ishero
        self.char_pos_x, self.char_pos_y = char_pos_x, char_pos_y
        self.character_position(self.char_pos_x, self.char_pos_y)
        if (self.row < 10 and self.map_of_game.map_list[self.row+1][self.column] == '0') or (self.row < 10 and self.map_of_game.map_list[self.row+1][self.column] == 'C' and self.ishero == True):
            self.deltay = 72
            self.char_pos_y += 72
            self.map_of_game.map_list[self.row+1][self.column] = 'C'
            self.map_of_game.map_list[self.row][self.column] = '0'
        else:
            self.deltay = 0
        self.deltax = 0
        return self.char_pos_y

    def move_left(self, char_pos_x, char_pos_y, ishero=False):
        self.ishero = ishero
        self.char_pos_x, self.char_pos_y = char_pos_x, char_pos_y
        self.character_position(self.char_pos_x, self.char_pos_y)
        if (self.column > 0 and self.map_of_game.map_list[self.row][self.column-1] == '0') or (self.column > 0 and self.map_of_game.map_list[self.row][self.column-1] == 'C' and self.ishero == True):
            self.deltax = -72
            self.char_pos_x -= 72
            self.map_of_game.map_list[self.row][self.column-1] = 'C'
            self.map_of_game.map_list[self.row][self.column] = '0'
        else:
            self.deltax = 0
        self.deltay = 0
        return self.char_pos_x

    def move_right(self, char_pos_x, char_pos_y, ishero=False):
        self.ishero = ishero
        self.char_pos_x, self.char_pos_y = char_pos_x, char_pos_y
        self.character_position(self.char_pos_x, self.char_pos_y)
        if (self.column < 9 and self.map_of_game.map_list[self.row][self.column+1] == '0') or (self.column < 9 and self.map_of_game.map_list[self.row][self.column+1] == 'C' and self.ishero == True):
            self.deltax = 72
            self.char_pos_x += 72
            self.map_of_game.map_list[self.row][self.column+1] = 'C'
            self.map_of_game.map_list[self.row][self.column] = '0'
        else:
            self.deltax = 0
        self.deltay = 0
        return self.char_pos_x

    def character_position(self, character_pos_x, character_pos_y):
        self.character_pos_x = character_pos_x
        self.character_pos_y = character_pos_y
        self.column = int((self.character_pos_x - 40) / 72)
        self.row = int((self.character_pos_y - 40) / 72)

    def random_enemy_starting_position(self):
        free_floor_tiles_list = []
        for i in range(len(self.map_of_game.map_list)):
            for j in range(len(self.map_of_game.map_list[i])):
                if self.map_of_game.map_list[i][j] == '0':
                    free_floor_tiles_list.append([j, i])
        random_position = random.randint(0, len(free_floor_tiles_list))

        self.random_enemy_position_x = free_floor_tiles_list[random_position-1][0] * 72 + 40
        self.random_enemy_position_y = free_floor_tiles_list[random_position-1][1] * 72 + 40
        self.map_of_game.map_list[free_floor_tiles_list[random_position-1][1]][free_floor_tiles_list[random_position-1][0]] = 'C'

        return self.random_enemy_position_x, self.random_enemy_position_y

    def random_enemy_move(self):
        random_direction = random.randint(1, 4)
        if random_direction == 1:
            return 'up'
        elif random_direction == 2:
            return 'down'
        elif random_direction == 3:
            return 'left'
        else:
            return 'right'

class Hero(Character):

    def __init__(self, map_of_game):
        self.map_of_game = map_of_game
        self.hero_pos_x = 40
        self.hero_pos_y = 40
        self.hp = 20 + 3 * random.randint(1, 6)
        self.hp = 2 * random.randint(1, 6)
        self.sp = 5 + random.randint(1, 6)

    def hero_move_up(self):
        self.hero_pos_y = super().move_up(self.hero_pos_x, self.hero_pos_y, True)

    def hero_move_down(self):
        self.hero_pos_y = super().move_down(self.hero_pos_x, self.hero_pos_y, True)

    def hero_move_left(self):
        self.hero_pos_x = super().move_left(self.hero_pos_x, self.hero_pos_y, True)

    def hero_move_right(self):
        self.hero_pos_x = super().move_right(self.hero_pos_x, self.hero_pos_y, True)


class Skeleton(Character):
    def __init__(self, map_of_game, level=1):
        self.map_of_game = map_of_game
        self.level = level
        self.deltax, self.deltay = 0, 0
        self.enemy_pos_x, self.enemy_pos_y = super().random_enemy_starting_position()
        self.hp = 2 * self.level * random.randint(1, 6)
        self.hp = self.level / 2 * random.randint(1, 6)
        self.sp = level * random.randint(1, 6)

    def skeleton_move(self):
        self.recursive_round = 0
        self.skeleton_move_rec()

    def skeleton_move_rec(self):
        self.direction = super().random_enemy_move()
        if self.direction == 'up':
            self.enemy_pos_y = super().move_up(self.enemy_pos_x, self.enemy_pos_y)
        elif self.direction == 'down':
            self.enemy_pos_y = super().move_down(self.enemy_pos_x, self.enemy_pos_y)
        elif self.direction == 'left':
            self.enemy_pos_x = super().move_left(self.enemy_pos_x, self.enemy_pos_y)
        else:
            self.enemy_pos_x = super().move_right(self.enemy_pos_x, self.enemy_pos_y)
        if self.deltax == 0 and self.deltay == 0 and self.recursive_round < 10:
            self.recursive_round += 1
            self.skeleton_move_rec()


class Boss(Character):
    def __init__(self, map_of_game, level=1):
        self.map_of_game = map_of_game
        self.level = level
        self.deltax, self.deltay = 0, 0
        self.enemy_pos_x, self.enemy_pos_y = super().random_enemy_starting_position()
        self.hp = 2 * self.level * random.randint(1, 6) + random.randint(1, 6)
        self.hp = self.level / 2 * random.randint(1, 6) + random.randint(1, 6) / 2
        self.sp = level * random.randint(1, 6) + self.level

    def boss_move(self):
        self.recursive_round = 0
        self.boss_move_rec()

    def boss_move_rec(self):
        self.direction = super().random_enemy_move()
        if self.direction == 'up':
            self.enemy_pos_y = super().move_up(self.enemy_pos_x, self.enemy_pos_y)
        elif self.direction == 'down':
            self.enemy_pos_y = super().move_down(self.enemy_pos_x, self.enemy_pos_y)
        elif self.direction == 'left':
            self.enemy_pos_x = super().move_left(self.enemy_pos_x, self.enemy_pos_y)
        else:
            self.enemy_pos_x = super().move_right(self.enemy_pos_x, self.enemy_pos_y)
        if self.deltax == 0 and self.deltay == 0 and self.recursive_round < 10:
            self.recursive_round += 1
            self.boss_move_rec()

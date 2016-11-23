from tkinter import *
import random

class Game:
    def __init__(self):
        self.read_map()

    def read_map(self):
        f = open('map.txt', 'r')
        self.map_list = f.readlines()
        f.close()
        for i in range(len(self.map_list)):
            self.map_list[i] = self.map_list[i][:-1]
            self.map_list[i] = self.map_list[i].split(';')

class Character:

    def move_up(self):
        self.character_position(self.hero_pos_x, self.hero_pos_y)
        if self.row > 0 and self.game.map_list[self.row-1][self.column] != '1':
            self.deltay = -72
            self.hero_pos_y -= 72
        else:
            self.deltay = 0

    def move_down(self):
        self.character_position(self.hero_pos_x, self.hero_pos_y)
        if self.row < 10 and self.game.map_list[self.row+1][self.column] != '1':
            self.deltay = 72
            self.hero_pos_y += 72
        else:
            self.deltay = 0

    def move_left(self):
        self.character_position(self.hero_pos_x, self.hero_pos_y)
        if self.column > 0 and self.game.map_list[self.row][self.column-1] != '1':
            self.deltax = -72
            self.hero_pos_x -= 72
        else:
            self.deltax = 0

    def move_right(self):
        self.character_position(self.hero_pos_x, self.hero_pos_y)
        if self.column < 9 and self.game.map_list[self.row][self.column+1] != '1':
            self.deltax = 72
            self.hero_pos_x += 72
        else:
            self.deltax = 0

    def character_position(self, character_pos_x, character_pos_y):
        self.character_pos_x = character_pos_x
        self.character_pos_y = character_pos_y
        self.column = int((self.character_pos_x - 40) / 72)
        self.row = int((self.character_pos_y - 40) / 72)

    def random_enemy_position(self):
        free_floor_tiles_list = []
        for i in range(len(self.game.map_list)):
            for j in range(len(self.game.map_list[i])):
                if self.game.map_list[i][j] == '0':
                    free_floor_tiles_list.append([j, i])
        random_position = random.randint(0, len(free_floor_tiles_list))

        self.random_enemy_position_x = free_floor_tiles_list[random_position-1][0] * 72 + 40
        self.random_enemy_position_y = free_floor_tiles_list[random_position-1][1] * 72 + 40
        self.game.map_list[free_floor_tiles_list[random_position-1][1]][free_floor_tiles_list[random_position-1][0]] = 'E'

class Hero(Character):

    def __init__(self, game):
        self.game = game
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.hero_image = self.hero_down
        self.hero_pos_x = 40
        self.hero_pos_y = 40

    def hero_move_up(self):
        self.hero_image = self.hero_up
        super().move_up()

    def hero_move_down(self):
        self.hero_image = self.hero_down
        super().move_down()

    def hero_move_left(self):
        self.hero_image = self.hero_left
        super().move_left()

    def hero_move_right(self):
        self.hero_image = self.hero_right
        super().move_right()


class Skeleton(Character):
    def __init__(self, game):
        self.game = game
        super().random_enemy_position()

    def skeleton_starting_position(self):
        pass

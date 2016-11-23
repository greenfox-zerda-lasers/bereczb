from tkinter import *
class Game:

    def __init__(self):
        self.read_map()
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.hero_image = self.hero_down
        self.hero_pos_x = 40
        self.hero_pos_y = 40

    def read_map(self):
        f = open('map.txt', 'r')
        self.map_list = f.readlines()
        f.close()
        for i in range(len(self.map_list)):
            self.map_list[i] = self.map_list[i][:-1]
            self.map_list[i] = self.map_list[i].split(';')

    def hero_move_up(self):
        self.hero_position()
        self.hero_image = self.hero_up
        if self.row > 0 and self.map_list[self.row-1][self.column] == '0':
            self.deltay = -72
            self.hero_pos_y -= 72
        else:
            self.deltay = 0

    def hero_move_down(self):
        self.hero_position()
        self.hero_image = self.hero_down
        if self.row < 10 and self.map_list[self.row+1][self.column] == '0':
            self.deltay = 72
            self.hero_pos_y += 72
        else:
            self.deltay = 0

    def hero_move_left(self):
        self.hero_position()
        self.hero_image = self.hero_left
        if self.column > 0 and self.map_list[self.row][self.column-1] == '0':
            self.deltax = -72
            self.hero_pos_x -= 72
        else:
            self.deltax = 0

    def hero_move_right(self):
        self.hero_position()
        self.hero_image = self.hero_right
        if self.column < 9 and self.map_list[self.row][self.column+1] == '0':
            self.deltax = 72
            self.hero_pos_x += 72
        else:
            self.deltax = 0

    def hero_position(self):
        self.column = int((self.hero_pos_x - 40) / 72)
        self.row = int((self.hero_pos_y - 40) / 72)

from tkinter import *

class Screen():

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 730, height = 800)
        self.canvas.pack()

        self.floor = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")

        self.read_map()
        self.draw_map()
        self.draw_hero()

    def draw_map(self):
        x, y = 40, 40
        for i in range(10):
            for j in range(11):
                if self.map_list[j][i] == '0':
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.floor)
                elif self.map_list[j][i] == '1':
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.wall)

    def draw_hero(self):
        x, y = 40, 40
        self.canvas.create_image(x, y, image = self.hero_down)

    def read_map(self):
        f = open('map.txt', 'r')
        self.map_list = f.readlines()
        f.close()
        for i in range(len(self.map_list)):
            self.map_list[i] = self.map_list[i][:-1]
            self.map_list[i] = self.map_list[i].split(';')

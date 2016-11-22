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



    def draw_map(self, map_list):
        x, y = 40, 40
        self.map_list = map_list
        for i in range(10):
            for j in range(11):
                if self.map_list[j][i] == '0':
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.floor)
                elif self.map_list[j][i] == '1':
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.wall)

    def draw_hero(self):
        x, y = 40, 40
        self.canvas.create_image(x, y, image = self.hero_down)


    def test(self, event):
        x, y = 140, 140
        self.canvas.create_image(x, y, image = self.hero_down)

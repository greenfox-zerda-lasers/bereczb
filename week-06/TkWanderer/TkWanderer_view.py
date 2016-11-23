from tkinter import *

class Screen():

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 730, height = 800)
        self.canvas.pack()

        self.floor = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")

    def draw_map(self, map_list):
        x, y = 40, 40
        self.map_list = map_list
        for i in range(10):
            for j in range(11):
                if self.map_list[j][i] == '0':
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.floor)
                elif self.map_list[j][i] == '1':
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.wall)

    def draw_hero(self, hero):
        self.hero = self.canvas.create_image(40, 40, image = hero)

    def draw_enemy(self, enemy_pos_x, enemy_pos_y, enemy_image):
        self.enemy = self.canvas.create_image(40, 40, image = enemy_image)

    def move_hero(self, deltax, deltay, hero_image_view):
        self.deltax, self.deltay, self.hero_image_view = deltax, deltay, hero_image_view
        self.pos_x = self.canvas.coords(self.hero)[0]
        self.pos_y = self.canvas.coords(self.hero)[1]
        self.canvas.delete(self.hero)
        self.hero = self.canvas.create_image(self.pos_x, self.pos_y, image = self.hero_image_view)
        self.canvas.move(self.hero, self.deltax, self.deltay)

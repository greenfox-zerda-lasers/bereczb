from tkinter import *

class Screen():

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 730, height = 800)
        self.canvas.pack()

        self.floor = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")
        self.skeleton_image = PhotoImage(file = "skeleton.png")


    def draw_map(self, map_list):
        x, y = 40, 40
        self.map_list = map_list
        for i in range(10):
            for j in range(11):
                if self.map_list[j][i] == '1':
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.wall)
                else:
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.floor)

    def draw_hero(self, hero):
        self.hero = self.canvas.create_image(40, 40, image = hero)

    def draw_skeleton(self, skeleton_pos_x, skeleton_pos_y):
        self.skeleton_pos_x, self.skeleton_pos_y = skeleton_pos_x, skeleton_pos_y
        self.skeleton = self.canvas.create_image(self.skeleton_pos_x, self.skeleton_pos_y, image = self.skeleton_image)

    def move_hero(self, deltax, deltay, hero_image_view):
        self.hero_image_view = hero_image_view
        pos_x = self.canvas.coords(self.hero)[0]
        pos_y = self.canvas.coords(self.hero)[1]
        self.canvas.delete(self.hero)
        self.hero = self.canvas.create_image(pos_x, pos_y, image = self.hero_image_view)
        self.canvas.move(self.hero, deltax, deltay)

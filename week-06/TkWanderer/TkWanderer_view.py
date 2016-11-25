from tkinter import *
from PIL import Image, ImageTk

class Screen():

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 615, height = 680, bg = "black")
        self.canvas.pack()

        self.floor = self.resize("floor.png", 60, 60)
        self.wall = self.resize("wall.png", 60, 60)
        self.skeleton_image = self.resize("skeleton.png", 60, 60)
        self.boss_image = self.resize("boss.png", 60, 60)
        self.hero_down = self.resize("hero-down.png", 60, 60)
        self.hero_up = self.resize("hero-up.png", 60, 60)
        self.hero_right = self.resize("hero-right.png", 60, 60)
        self.hero_left = self.resize("hero-left.png", 60, 60)
        self.hero_image_view = self.hero_down

        self.skeleton = []

    def resize(self, img_path, width, height):
        image = Image.open(img_path)
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def draw_map(self, map_list):
        x, y = 40, 40
        self.map_list = map_list
        for i in range(10):
            for j in range(11):
                if self.map_list[j][i] == '1':
                    self.canvas.create_image(x + (i * 60), y + (j * 60), image = self.wall)
                else:
                    self.canvas.create_image(x + (i * 60), y + (j * 60), image = self.floor)

    def draw_hero(self):
        self.hero = self.canvas.create_image(40, 40, image = self.hero_image_view)

    def draw_skeleton(self, skeleton_pos_x, skeleton_pos_y):
        self.skeleton_pos_x, self.skeleton_pos_y = skeleton_pos_x, skeleton_pos_y
        self.skeleton.append(self.canvas.create_image(self.skeleton_pos_x, self.skeleton_pos_y, image = self.skeleton_image))

    def draw_boss(self, boss_pos_x, boss_pos_y):
        self.boss_pos_x, self.boss_pos_y = boss_pos_x, boss_pos_y
        self.boss = self.canvas.create_image(self.boss_pos_x, self.boss_pos_y, image = self.boss_image)

    def move_hero(self, deltax, deltay, direction):
        self.deltax, self.deltay, self.direction = deltax, deltay, direction
        self.hero_direction(self.direction)
        pos_x = self.canvas.coords(self.hero)[0]
        pos_y = self.canvas.coords(self.hero)[1]
        self.canvas.delete(self.hero)
        self.hero = self.canvas.create_image(pos_x + self.deltax, pos_y + self.deltay, image = self.hero_image_view)

    def hero_direction(self, direction):
        self.direction = direction
        if self.direction == 'up':
            self.hero_image_view = self.hero_up
        elif self.direction == 'left':
            self.hero_image_view = self.hero_left
        elif self.direction == 'right':
            self.hero_image_view = self.hero_right
        else:
            self.hero_image_view = self.hero_down

    def move_boss(self, deltax, deltay):
        self.deltax, self.deltay = deltax, deltay
        self.canvas.move(self.boss, self.deltax, self.deltay)

    def move_skeleton(self, deltax, deltay, index):
        self.index = index
        self.deltax, self.deltay = deltax, deltay
        self.canvas.move(self.skeleton[self.index], self.deltax, self.deltay)

from tkinter import *

class Screen():

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 730, height = 800)
        self.canvas.pack()

        self.floor = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")
        self.skeleton_image = PhotoImage(file = "skeleton.png")
        self.boss_image = PhotoImage(file = "boss.png")
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.hero_image_view = PhotoImage(file = "hero-down.png")

        self.skeleton = []

    def draw_map(self, map_list):
        x, y = 40, 40
        self.map_list = map_list
        for i in range(10):
            for j in range(11):
                if self.map_list[j][i] == '1':
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.wall)
                else:
                    self.canvas.create_image(x + (i * 72), y + (j * 72), image = self.floor)

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
        # print((self.canvas.coords(self.skeleton)[0]-40)/72, (self.canvas.coords(self.skeleton)[1]-40)/72)

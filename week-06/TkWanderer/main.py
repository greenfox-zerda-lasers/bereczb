import TkWanderer_view
import TkWanderer_model

class Tkwanderer():
    def __init__(self):
        self.view = TkWanderer_view.Screen()
        self.map_of_game = TkWanderer_model.Map_of_game()
        self.hero = TkWanderer_model.Hero(self.map_of_game)
        self.boss = TkWanderer_model.Boss(self.map_of_game)
        self.key_press = 0
        self.view.draw_map(self.map_of_game.get_map())
        self.view.draw_hero()
        self.number_of_skeletons = self.map_of_game.get_number_of_skeletons()

        self.skeletons_list = []
        for i in range(self.number_of_skeletons):
            self.skeletons_list.append('skeleton'+str(i))
            self.skeletons_list[i] = TkWanderer_model.Skeleton(self.map_of_game)
            self.view.draw_skeleton(self.skeletons_list[i].random_enemy_position_x, self.skeletons_list[i].random_enemy_position_y)

        self.view.draw_boss(self.boss.random_enemy_position_x, self.boss.random_enemy_position_y)

        self.control_loop()

        self.view.root.mainloop()

    def control_loop(self):
        self.view.root.bind('<Up>', self.contr_hero_move_up)
        self.view.root.bind('<Down>', self.contr_hero_move_down)
        self.view.root.bind('<Left>', self.contr_hero_move_left)
        self.view.root.bind('<Right>', self.contr_hero_move_right)
        self.view.root.bind('<space>', self.contr_hero_fight)
        self.view.root.bind('<w>', self.contr_hero_move_up)
        self.view.root.bind('<s>', self.contr_hero_move_down)
        self.view.root.bind('<a>', self.contr_hero_move_left)
        self.view.root.bind('<d>', self.contr_hero_move_right)
        self.view.root.bind('<Escape>', self.escape)

    def contr_hero_move_up(self, event):
        self.hero.hero_move_up()
        self.view.move_hero(0, self.hero.deltay, 'up')
        self.key_press += 1
        if self.key_press == 2:
            self.boss.boss_move()
            self.view.move_boss(self.boss.deltax, self.boss.deltay)
            for i in range(self.number_of_skeletons):
                self.skeletons_list[i].skeleton_move()
                self.view.move_skeleton(self.skeletons_list[i].deltax, self.skeletons_list[i].deltay, i)
            self.key_press = 0

    def contr_hero_move_down(self, event):
        self.hero.hero_move_down()
        self.view.move_hero(0, self.hero.deltay, 'down')
        self.key_press += 1
        if self.key_press == 2:
            self.boss.boss_move()
            self.view.move_boss(self.boss.deltax, self.boss.deltay)
            for i in range(self.number_of_skeletons):
                self.skeletons_list[i].skeleton_move()
                self.view.move_skeleton(self.skeletons_list[i].deltax, self.skeletons_list[i].deltay, i)
            self.key_press = 0

    def contr_hero_move_left(self, event):
        self.hero.hero_move_left()
        self.view.move_hero(self.hero.deltax, 0, 'left')
        self.key_press += 1
        if self.key_press == 2:
            self.boss.boss_move()
            self.view.move_boss(self.boss.deltax, self.boss.deltay)
            for i in range(self.number_of_skeletons):
                self.skeletons_list[i].skeleton_move()
                self.view.move_skeleton(self.skeletons_list[i].deltax, self.skeletons_list[i].deltay, i)
            self.key_press = 0

    def contr_hero_move_right(self, event):
        self.hero.hero_move_right()
        self.view.move_hero(self.hero.deltax, 0, 'right')
        self.key_press += 1
        if self.key_press == 2:
            self.boss.boss_move()
            self.view.move_boss(self.boss.deltax, self.boss.deltay)
            for i in range(self.number_of_skeletons):
                self.skeletons_list[i].skeleton_move()
                self.view.move_skeleton(self.skeletons_list[i].deltax, self.skeletons_list[i].deltay, i)
            self.key_press = 0

    def contr_hero_fight(self, event):
        print('space')

    def escape(self, event):
        exit()

game = Tkwanderer()

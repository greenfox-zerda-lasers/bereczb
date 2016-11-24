import TkWanderer_view
import TkWanderer_model

class Tkwanderer():
    def __init__(self):
        self.view = TkWanderer_view.Screen()
        self.map_of_game = TkWanderer_model.Map_of_game()
        self.hero = TkWanderer_model.Hero(self.map_of_game)
        self.boss = TkWanderer_model.Boss(self.map_of_game)

        self.view.draw_map(self.map_of_game.get_map())
        self.view.draw_hero()

        self.skeletons_list = []
        for i in range(3):
            self.skeletons_list.append('skeleton'+str(i))
            self.skeletons_list[i] = TkWanderer_model.Skeleton(self.map_of_game)
            self.view.draw_skeleton(self.skeletons_list[i].random_enemy_position_x, self.skeletons_list[i].random_enemy_position_y)
            print('after draw controller', (self.skeletons_list[i].random_enemy_position_x-40)/72, (self.skeletons_list[i].random_enemy_position_y-40)/72)
        print()

        self.view.draw_boss(self.boss.random_enemy_position_x, self.boss.random_enemy_position_y)

        for i in range(3):
            print('after boss draw controller', (self.skeletons_list[i].random_enemy_position_x-40)/72, (self.skeletons_list[i].random_enemy_position_y-40)/72)
        print()

        self.control_loop()

        self.view.root.mainloop()

    def control_loop(self):
        self.view.root.bind('<Up>', self.contr_hero_move_up)
        self.view.root.bind('<Down>', self.contr_hero_move_down)
        self.view.root.bind('<Left>', self.contr_hero_move_left)
        self.view.root.bind('<Right>', self.contr_hero_move_right)
        self.view.root.bind('<Escape>', self.escape)

    def contr_hero_move_up(self, event):
        self.hero.hero_move_up()
        self.view.move_hero(0, self.hero.deltay, 'up')
        self.boss.boss_move()
        self.view.move_boss(self.boss.deltax, self.boss.deltay)
        for i in range(3):
            self.skeletons_list[i].skeleton_move()
            self.view.move_skeleton(self.skeletons_list[i].deltax, self.skeletons_list[i].deltay, i)
            print('skeletons after draw controller', (self.skeletons_list[i].enemy_pos_x-40)/72, (self.skeletons_list[i].enemy_pos_y-40)/72, '|', (self.skeletons_list[i].deltax)/72, (self.skeletons_list[i].deltay)/72)
        print('boss after draw controller', (self.boss.enemy_pos_x-40)/72, (self.boss.enemy_pos_y-40)/72)
        print()

    def contr_hero_move_down(self, event):
        self.hero.hero_move_down()
        self.view.move_hero(0, self.hero.deltay, 'down')
        self.boss.boss_move()
        self.view.move_boss(self.boss.deltax, self.boss.deltay)
        for i in range(3):
            self.skeletons_list[i].skeleton_move()
            self.view.move_skeleton(self.skeletons_list[i].deltax, self.skeletons_list[i].deltay, i)
            print('skeletons after draw controller', (self.skeletons_list[i].enemy_pos_x-40)/72, (self.skeletons_list[i].enemy_pos_y-40)/72, '|', (self.skeletons_list[i].deltax)/72, (self.skeletons_list[i].deltay)/72)
        print('boss after draw controller', (self.boss.enemy_pos_x-40)/72, (self.boss.enemy_pos_y-40)/72)
        print()

    def contr_hero_move_left(self, event):
        self.hero.hero_move_left()
        self.view.move_hero(self.hero.deltax, 0, 'left')
        self.boss.boss_move()
        self.view.move_boss(self.boss.deltax, self.boss.deltay)
        for i in range(3):
            self.skeletons_list[i].skeleton_move()
            self.view.move_skeleton(self.skeletons_list[i].deltax, self.skeletons_list[i].deltay, i)
            print('skeletons after draw controller', (self.skeletons_list[i].enemy_pos_x-40)/72, (self.skeletons_list[i].enemy_pos_y-40)/72, '|', (self.skeletons_list[i].deltax)/72, (self.skeletons_list[i].deltay)/72)
        print('boss after draw controller', (self.boss.enemy_pos_x-40)/72, (self.boss.enemy_pos_y-40)/72)
        print()

    def contr_hero_move_right(self, event):
        self.hero.hero_move_right()
        self.view.move_hero(self.hero.deltax, 0, 'right')
        self.boss.boss_move()
        self.view.move_boss(self.boss.deltax, self.boss.deltay)
        for i in range(3):
            self.skeletons_list[i].skeleton_move()
            self.view.move_skeleton(self.skeletons_list[i].deltax, self.skeletons_list[i].deltay, i)
            print('skeletons after draw controller', (self.skeletons_list[i].enemy_pos_x-40)/72, (self.skeletons_list[i].enemy_pos_y-40)/72, '|', (self.skeletons_list[i].deltax)/72, (self.skeletons_list[i].deltay)/72)
        print('boss after draw controller', (self.boss.enemy_pos_x-40)/72, (self.boss.enemy_pos_y-40)/72)
        print()

    def escape(self, event):
        exit()

game = Tkwanderer()

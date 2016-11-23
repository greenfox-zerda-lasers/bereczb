import TkWanderer_view
import TkWanderer_model

class Tkwanderer():
    def __init__(self):
        self.view = TkWanderer_view.Screen()
        self.game = TkWanderer_model.Game()
        self.hero = TkWanderer_model.Hero(self.game)

#!!!!!!!!!!!
        self.skeleton1 = TkWanderer_model.Skeleton(self.game)
        self.skeletons_list = []
        for i in range(3):
            self.skeletons_list.append('skeleton'+str(i))
            print(self.skeletons_list[i])
            self.skeletons_list[i] = TkWanderer_model.Skeleton(self.game)
            print(self.skeletons_list)

        self.view.draw_map(self.game.map_list)
#!!!!!!!!!!!
        for i in range(3):
            # self.skeletons_list[i].skeleton_starting_position()
            self.view.draw_skeleton(self.skeletons_list[i].random_enemy_position_x, self.skeletons_list[i].random_enemy_position_y)
            print(self.skeletons_list[i].random_enemy_position_x)
            print(self.skeletons_list[i].random_enemy_position_y)


        self.view.draw_hero(self.hero.hero_image)

#!!!!!!!!!!!
        # self.view.draw_skeleton(self.skeleton1.random_enemy_position_x, self.skeleton1.random_enemy_position_y)

        self.control_loop()

        self.view.root.mainloop()

    def control_loop(self):
        self.view.root.bind('<w>', self.contr_hero_move_up)
        self.view.root.bind('<s>', self.contr_hero_move_down)
        self.view.root.bind('<a>', self.contr_hero_move_left)
        self.view.root.bind('<d>', self.contr_hero_move_right)

    def contr_hero_move_up(self, event):
        self.hero.hero_move_up()
        self.view.move_hero(0, self.hero.deltay, self.hero.hero_image)

    def contr_hero_move_down(self, event):
        self.hero.hero_move_down()
        self.view.move_hero(0, self.hero.deltay, self.hero.hero_image)

    def contr_hero_move_left(self, event):
        self.hero.hero_move_left()
        self.view.move_hero(self.hero.deltax, 0, self.hero.hero_image)

    def contr_hero_move_right(self, event):
        self.hero.hero_move_right()
        self.view.move_hero(self.hero.deltax, 0, self.hero.hero_image)

game = Tkwanderer()

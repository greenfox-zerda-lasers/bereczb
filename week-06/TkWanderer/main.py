import TkWanderer_view
import TkWanderer_model

class Tkwanderer():
    def __init__(self):
        self.view = TkWanderer_view.Screen()
        self.game = TkWanderer_model.Game()
        # self.character = TkWanderer_model.Characer()
        self.hero = TkWanderer_model.Hero()
        self.view.draw_map(self.game.map_list)
        self.view.draw_hero(self.hero.hero_image)
        # self.view.draw_enemy()
        self.control_loop()

        self.view.root.mainloop()

    def control_loop(self):
        self.view.root.bind('<w>', self.contr_hero_move_up)
        self.view.root.bind('<s>', self.contr_hero_move_down)
        self.view.root.bind('<a>', self.contr_hero_move_left)
        self.view.root.bind('<d>', self.contr_hero_move_right)

    def contr_hero_move_up(self, event):
        self.hero.hero_move_up(self.game.map_list)
        # self.character.move_up(self.game.map_list)
        self.view.move_hero(0, self.hero.deltay, self.hero.hero_image)

    def contr_hero_move_down(self, event):
        self.hero.hero_move_down(self.game.map_list)
        # self.character.move_down(self.game.map_list)
        self.view.move_hero(0, self.hero.deltay, self.hero.hero_image)

    def contr_hero_move_left(self, event):
        self.hero.hero_move_left(self.game.map_list)
        # self.character.move_left(self.game.map_list)
        self.view.move_hero(self.hero.deltax, 0, self.hero.hero_image)

    def contr_hero_move_right(self, event):
        self.hero.hero_move_right(self.game.map_list)
        # self.character.move_right(self.game.map_list)
        self.view.move_hero(self.hero.deltax, 0, self.hero.hero_image)

game = Tkwanderer()

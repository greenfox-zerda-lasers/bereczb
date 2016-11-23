import TkWanderer_view
import TkWanderer_model

class Tkwanderer():
    def __init__(self):
        self.view = TkWanderer_view.Screen()
        self.game = TkWanderer_model.Game()
        self.view.draw_map(self.game.map_list)
        self.view.draw_hero(self.game.hero_image)
        self.view.draw_enemy()
        self.control_loop()

        self.view.root.mainloop()

    def control_loop(self):
        self.view.root.bind('<w>', self.contr_hero_move_up)
        self.view.root.bind('<s>', self.contr_hero_move_down)
        self.view.root.bind('<a>', self.contr_hero_move_left)
        self.view.root.bind('<d>', self.contr_hero_move_right)

    def contr_hero_move_up(self, event):
        self.game.hero_move_up()
        self.view.move_hero(0, self.game.deltay, self.game.hero_image)

    def contr_hero_move_down(self, event):
        self.game.hero_move_down()
        self.view.move_hero(0, self.game.deltay, self.game.hero_image)

    def contr_hero_move_left(self, event):
        self.game.hero_move_left()
        self.view.move_hero(self.game.deltax, 0, self.game.hero_image)

    def contr_hero_move_right(self, event):
        self.game.hero_move_right()
        self.view.move_hero(self.game.deltax, 0, self.game.hero_image)

game = Tkwanderer()

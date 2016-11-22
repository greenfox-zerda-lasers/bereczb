import TkWanderer_view
import TkWanderer_model

class Tkwanderer():
    def __init__(self):
        self.view = TkWanderer_view.Screen()
        self.game = TkWanderer_model.Game()
        self.view.draw_map(self.game.map_list)
        self.view.draw_hero()
        self.control_loop()

        self.view.root.mainloop()

    def control_loop(self):
        self.view.root.bind('<w>', self.view.test)
        self.view.root.bind('<s>', self.view.test)
        self.view.root.bind('<a>', self.view.test)
        self.view.root.bind('<d>', self.view.test)

game = Tkwanderer()

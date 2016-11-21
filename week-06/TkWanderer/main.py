import TkWanderer_view

class Tkwanderer():
    def __init__(self):
        self.view = TkWanderer_view.Screen()
        self.control_loop()

        self.view.root.mainloop()

    def control_loop(self):
        pass

game = Tkwanderer()

# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

import elevator_model
import elevator_view

class Elevator_control():

    def __init__(self):
        self.elev_view = elevator_view.Elevator_view()
        self.elev_model = elevator_model.Elevator()
        self.control_loop()

    def control_loop(self):

        self.elev_model.floor_change = False

        while True:
            self.elev_view.art(self.elev_model.level, self.elev_model.people, self.elev_model.floor_change)
            self.command = input("your command: ")

            if self.command == 'u':
                self.elev_model.move_up()
                if self.elev_model.floor_change == True:
                    self.elev_view.art(self.elev_model.level, self.elev_model.people, self.elev_model.floor_change)
                    self.elev_model.floor_change = False

            elif self.command == 'd':
                self.elev_model.move_down()
                if self.elev_model.floor_change == True:
                    self.elev_view.art(self.elev_model.level, self.elev_model.people, self.elev_model.floor_change)
                    self.elev_model.floor_change = False

            elif self.command == 'a':
                self.elev_model.add_people()

            elif self.command == 'r':
                self.elev_model.remove_people()

            elif self.command == 'q':
                break

elevator1 = Elevator_control()

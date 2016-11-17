# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

class Elevator:

    level = 0
    direction = 'up'
    people = 0

    def move_up(self):
        if self.level < 11:
            self.level += 1

    def move_down(self):
        if self.level > 0:
            self.level -= 1

    def add_people(self):
        if self.people < 9:
            self.people += 1

    def remove_people(self):
        if self.people > 0:
            self.people -= 1

# Create a class the displays the Elevator art and navigation (list of commands)

import os
import time

class Elevator_view:

    top1 = '___________________________________'
    top2 = "`._______________________________.'"
    empty_level = "   || ||       || ||       || ||"
    level_ppl_elev = "   || || [ X ] || ||       || ||"
    level_empty_elev = "   || || [   ] || ||       || ||"
    bottom1_elev_ppl = '  _||_||_[_X_]_||_||_______||_||_'
    bottom1_elev_noppl = '  _||_||_[___]_||_||_______||_||_'
    bottom1_noelev = '  _||_||_______||_||_______||_||_'
    bottom2 = ".'_______________________________`."

    def art(self, level, people, level_change):
        self.level = level
        self.people = people

        if level_change:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.building_wo_elevator()
            self.navigation()
            time.sleep(0.5)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.building_w_elevator(self.level, self.people)
            self.navigation()

    def building_wo_elevator(self):

        print(self.top1)
        print(self.top2)
        for i in range(11):
            print(self.empty_level)
        print(self.bottom1_noelev)
        print(self.bottom2)

    def navigation(self):

        print()
        print('    people: ', self.people)
        print('    level:  ', self.level)
        print()
        print('    Move elevator up    "u"')
        print('    Move elevator down  "d"')
        print('    Add people          "a"')
        print('    Remove people       "r"')
        print('    Quit                "q"')
        print()

    def building_w_elevator(self, level, people):
        print(self.top1)
        print(self.top2)
        for i in range(11 - level):
            print(self.empty_level)
        if people != 0 and level != 0:
            print(self.level_ppl_elev)
        elif level != 0:
            print(self.level_empty_elev)
        for i in range(level - 1):
            print(self.empty_level)
        if level == 0 and people != 0:
            print(self.bottom1_elev_ppl)
        elif level == 0 and people == 0:
            print(self.bottom1_elev_noppl)
        else:
            print(self.bottom1_noelev)
        print(self.bottom2)

# elevator1 = Elevator_view()
# elev.art(10, False)

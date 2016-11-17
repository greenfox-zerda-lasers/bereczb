import os
import time

def art(level, people):

    top1 = '___________________________________'
    top2 = "`._______________________________.'"
    empty_level = "   || ||       || ||       || ||"
    level_ppl_elev = "   || || [ X ] || ||       || ||"
    level_empty_elev = "   || || [   ] || ||       || ||"
    bottom1_elev_ppl = '  _||_||_[_X_]_||_||_______||_||_'
    bottom1_elev_noppl = '  _||_||_[___]_||_||_______||_||_'
    bottom1_noelev = '  _||_||_______||_||_______||_||_'
    bottom2 = ".'_______________________________`."

    os.system('cls' if os.name == 'nt' else 'clear')

    print(top1)
    print(top2)
    for i in range(11):
        print(empty_level)
    print(bottom1_noelev)
    print(bottom2)

    time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')

    print(top1)
    print(top2)
    for i in range(11 - level):
        print(empty_level)
    if people and level != 0:
        print(level_ppl_elev)
    elif level != 0:
        print(level_empty_elev)
    for i in range(level - 1):
        print(empty_level)
    if level == 0 and people:
        print(bottom1_elev_ppl)
    elif level == 0 and people == False:
        print(bottom1_elev_noppl)
    else:
        print(bottom1_noelev)
    print(bottom2)

art(11, True)

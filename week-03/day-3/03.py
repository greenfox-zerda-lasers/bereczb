# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate(object):
    drinks = 0

    def drink_rum(self):
        self.drinks += 1

    def hows_goin_mate(self):
        if self.drinks > 4:
            print('Arrrr!')
        else:
            print('Nothin')

pirate1 = Pirate()

for i in range(7):
    print(i + 1)
    pirate1.drink_rum()
    pirate1.hows_goin_mate()

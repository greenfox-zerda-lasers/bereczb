af = 'fuuu'
# create a function that doubles it's input
# double af with it

def double(number):
    if type(number) == int or type(number) == float:
        return number * 2
    else:
        return 'nem szam'

print(double(af))

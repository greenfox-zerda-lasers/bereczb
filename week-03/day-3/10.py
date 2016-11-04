# Create a function that prints a triangle like this:
#       *           1 - 1
#      ***          2 - 3
#     *****         3 - 5
#    *******        4 - 7
#   *********       5 - 9
#  ***********      6 - 11
#
# It should take a number as parameter that describes how many lines the triangle has
def triangl(lines):
    for i in range(1, lines * 2, 2):
        print( (' ' * int((lines * 2 - i) / 2)), '*' * i, (' ' * int((lines * 2 - i) / 2)))

triangl(70)

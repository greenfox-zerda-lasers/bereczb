# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def triangl(lines):

    korr = 0

    if lines % 2 == 0:
        korr = 1

    for i in range(1, lines, 2):
        print( (' ' * int((lines * 2 - i) / 2)), '*' * i, (' ' * int((lines * 2 - i) / 2)))

    for i in range(lines - korr, 0, -2):
        print( (' ' * int((lines * 2 - i) / 2)), '*' * i, (' ' * int((lines * 2 - i) / 2)))

triangl(60)

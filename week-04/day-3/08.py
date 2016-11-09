# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

def draw_square(x, y):
    canvas.create_rectangle(x, y, x + 50, y + 50)

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

draw_square(120, 90)
draw_square(10, 25)
draw_square(40, 90)

root.mainloop()

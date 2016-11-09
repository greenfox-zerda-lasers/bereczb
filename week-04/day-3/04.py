# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

def draw(x, y):
    canvas.create_line(x, y, 150, 150)

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

draw(10, 20)
draw(80, 190)
draw(124, 42)

root.mainloop()

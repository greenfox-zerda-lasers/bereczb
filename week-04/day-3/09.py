# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

def draw_square(a):
    canvas.create_rectangle(150 - a / 2, 150 - a / 2, 150 + a / 2, 150 + a / 2)

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

draw_square(200)
draw_square(100)
draw_square(12)

root.mainloop()

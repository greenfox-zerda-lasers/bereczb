
# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

def draw_square(a, color):
    canvas.create_rectangle(150 - a / 2, 150 - a / 2, 150 + a / 2, 150 + a / 2, fill=color, outline=color )

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

j = 1
for i in range(300, 0, -15):
    j += 1
    draw_square(i, '#'+str(100000+j*31257))
    print(j)
root.mainloop()

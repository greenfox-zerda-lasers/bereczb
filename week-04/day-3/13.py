# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

def draw_line(x, y):
    canvas.create_line(x, y, 150, 150)

root = Tk()

width = 300
height = 300


canvas = Canvas(root, width = width, height = height)
canvas.pack()

for i in range(0, 301, 20):
    draw_line(i, 0)
    draw_line(0, i)
    draw_line(i, 300)
    draw_line(300, i)

root.mainloop()

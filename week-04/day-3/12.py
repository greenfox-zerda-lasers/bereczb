# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

def draw_checkerboard(x1, y1, x2, y2, color):
    canvas.create_rectangle(x1, y1, x2, y2, fill = color)


root = Tk()

width = 300
height = 300


canvas = Canvas(root, width = width, height = height)
canvas.pack()

for i in range(0, width, 15):
    for j in range(0, width, 15):
        if (i + j) % 2 == 0:
            color = 'white'
        else:
            color = 'black'
        draw_checkerboard(i, j, i + 15, j + 15, color)

root.mainloop()

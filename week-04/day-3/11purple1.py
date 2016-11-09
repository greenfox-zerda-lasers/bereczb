
from tkinter import *

def draw_square(x, color):
    canvas.create_rectangle(x, x, x + 10, x + 10, fill=color)

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

for i in range(10, 191, 10):
    draw_square(i, '#B145F3')

root.mainloop()

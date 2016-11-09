from tkinter import *

def draw_square(x, a, color):
    canvas.create_rectangle(x, x, x + a, x + a, fill=color)

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

j = 10

for i in range(10, 61, 10):
    draw_square(j, i, '#B145F3')
    j += i

root.mainloop()

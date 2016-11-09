# create a 300x300 canvas.
# draw a green 10x10 square to its center.


from tkinter import *

def draw(x, y):
    canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15)

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

draw(width/2, height/2)

root.mainloop()

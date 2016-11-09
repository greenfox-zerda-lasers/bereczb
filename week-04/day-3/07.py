# create a 300x300 canvas.
# fill it with four different size and color rectangles.


from tkinter import *

def draw(x, y, color):
    canvas.create_rectangle(150 - x, 150 - y, 150 + x, 150 + y, fill=color)

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

draw(120, 90, 'red')
draw(80, 70, 'green')
draw(30, 60, 'blue')


root.mainloop()

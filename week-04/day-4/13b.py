from tkinter import *
import randcolor
import time

def draw_polygon(x, y, width, height):

    time.sleep(0.00001)

    color = randcolor.random_color()
    canvas.create_polygon(x + width/4, y + 0, x + width/4*3, y + 0, x + width, y + height/2, x + width/4*3, y + height, x + width/4, y + height, x + 0, y + height/2, fill=color, outline="black")
    canvas.update()

def draw_recursive(x, y, width, height, level):
    if level == 0:
        return
    draw_polygon(x, y, width, height)

    draw_recursive(x + width/8, y + 0, width/2, height/2, level-1)
    draw_recursive(x + width/2, y + height/4, width/2, height/2, level-1)
    draw_recursive(x + width/8, y + height/2, width/2, height/2, level-1)

root = Tk()

width = 400
height = 2 * ((width/2) * 3**0.5)/2

canvas = Canvas(root, width = width, height = height)
canvas.pack()

draw_recursive(0, 0, width, height, 8)

root.mainloop()

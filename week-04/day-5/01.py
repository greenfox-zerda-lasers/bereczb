from tkinter import *
import randcolor
import time

def draw_triangle(x, y, width, height, level):
    time.sleep(0.0001)
    if level == 0:
        return
    color = randcolor.random_color()
    canvas.create_polygon(x + 0, y + 0, x + width, y + 0, x + width/2, y + height, fill=color, outline="black")
    canvas.update()

    draw_triangle(x + 0, y + 0, width/2, height/2, level-1)
    draw_triangle(x + width/2, y + 0, width/2, height/2, level-1)
    draw_triangle(x + width/4, y + height/2, width/2, height/2, level-1)

root = Tk()

width = 400
height = 2 * ((width/2) * 3**0.5)/2

canvas = Canvas(root, width = width, height = height)
canvas.pack()

draw_triangle(0, 0, width, height, 7)

root.mainloop()

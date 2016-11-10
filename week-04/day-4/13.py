from tkinter import *

def draw_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, level):
    if level == 0:
        return
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, fill='white', outline="black")

    draw_polygon(x1, y1, x2 - x1, y2, x1 * 2.5, y4/4, x2 - x1, y3, x1, y3, x1/2, y3/2, level-1)
    draw_polygon(x1 * 2.5, y4/4, x2 + x1/2, y4/4, x3, y3, x2 + x1/2, y4/4*3, x1 * 2.5, y4/4*3, x2 - x1, y3, level-1)
    draw_polygon(x1, y3, x2 - x1, y3, x1 * 2.5, y4/4*3, x2 - x1, y4, x1, y4, x1/2, y4/4*3, level-1)


root = Tk()

width = 400
height = 400

canvas = Canvas(root, width = width, height = height)
canvas.pack()

draw_polygon(width/4, 0, width/4*3, 0, width, height/2, width/4*3, height, width/4, height, 0, height/2, 3)

root.mainloop()

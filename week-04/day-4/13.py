from tkinter import *

def draw_polygon(x, y, width, height, level):
    if level == 0:
        return
    canvas.create_polygon(x + width/4, y + 0, x + width/4*3, y + 0, x + width, y + height/2, x + width/4*3, y + height, x + width/4, y + height, x + 0, y + height/2, fill='white', outline="black")

    draw_polygon(x + width/8, y + 0, width/2, height/2, level-1)
    draw_polygon(x + width/2, y + height/4, width/2, height/2, level-1)
    draw_polygon(x + width/8, y + height/2, width/2, height/2, level-1)


root = Tk()

width = 400
height = 2 * ((width/2) * 3**0.5)/2

canvas = Canvas(root, width = width, height = height)
canvas.pack()

# draw_polygon(width/4, 0, width/4*3, 0, width, height/2, width/4*3, height, width/4, height, 0, height/2, 3)
draw_polygon(0, 0, width, height, 5)

root.mainloop()

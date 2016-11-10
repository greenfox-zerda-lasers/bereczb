from tkinter import *

def draw_lines(x, y, size, level):
    if level == 0:
        return
    canvas.create_line(x + size/3, y + 0, x + size/3, y + size)
    canvas.create_line(x + size/3*2, y + 0, x + size/3*2, y + size)
    canvas.create_line(x + 0, y + size/3, x + size, y + size/3)
    canvas.create_line(x + 0, y + size/3*2, x + size, y + size/3*2)

    draw_lines(x + size/3, y + 0, size/3, level-1)
    draw_lines(x + 0, y + size/3, size/3, level-1)
    draw_lines(x + size/3, y + size/3*2, size/3, level-1)
    draw_lines(x + size/3*2, y + size/3, size/3, level-1)

root = Tk()

size = 600

canvas = Canvas(root, width = size, height = size, bg='yellow')
canvas.pack()

draw_lines(0, 0, size, 6)

root.mainloop()

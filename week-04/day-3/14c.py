# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *

def draw_line(x1, y1, x2, y2, color):
    canvas.create_line(x1, y1, x2, y2, fill=color)

root = Tk()

width = 300
height = 300
color_list = ['red', 'green', 'blue']

canvas = Canvas(root, width = width, height = height)
canvas.pack()

j = 0
for i in range(0, 151, 15):
    draw_line(i, 150, 150, i + 150, color_list[j])
    draw_line(i, 150, 150, 150 - i, color_list[j])
    draw_line(150, i, i + 150, 150, color_list[j])
    draw_line(150, 150 + i, 300 - i, 150, color_list[j])
    j += 1
    if j == 3:
        j = 0


root.mainloop()

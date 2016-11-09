# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *

def draw_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill='purple')
    canvas.create_line(y1, x1, y2, x2, fill='green')

root = Tk()

width = 300
height = 300


canvas = Canvas(root, width = width, height = height)
canvas.pack()

for i in range(0, 301, 20):
    draw_line(i, 0, 300, i)


root.mainloop()

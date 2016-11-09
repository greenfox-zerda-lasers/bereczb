# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.create_line(50, 50, 200, 50, fill='red')
canvas.create_line(200, 50, 200, 200, fill='green')
canvas.create_line(50, 50, 50, 200, fill='blue')
canvas.create_line(50, 200, 200, 200, fill='yellow')

root.mainloop()

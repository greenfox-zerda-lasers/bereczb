
# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *

def draw_lines(point_list):
    extended_list = point_list + [point_list[0]]
    for i in range(len(point_list)):
        canvas.create_line(extended_list[i][0], extended_list[i][1], extended_list[i + 1][0], extended_list[i + 1][1])

root = Tk()

width = 300
height = 300

canvas = Canvas(root, width = width, height = height)
canvas.pack()

draw_lines([[10, 10], [290,  10], [290, 290], [10, 290]])
draw_lines([[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]])

root.mainloop()

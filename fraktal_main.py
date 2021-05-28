from tkinter import *

import random

root = Tk()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def random_point():
    index = random.randint(1, len(start_points_list)) - 1
    return Point((cur_point.x + step_coefficient * (start_points_list[index].x - cur_point.x)),
                 (cur_point.y + step_coefficient * (start_points_list[index].y - cur_point.y)))


def choice_points_from_list(event):
    global start_points_list
    canvas.delete(ALL)
    start_points_list = []
    lst = entry_start_points.get().split()
    for i in range(len(lst) // 2):
        start_points_list.append(Point(int(lst[2 * i]), int(lst[2 * i + 1])))


def add_point_from_click(event):
    x = event.x
    y = event.y
    start_points_list.append(Point(x, y))
    canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red', outline='black')


def save_step(event):
    global step_coefficient
    step_coefficient = float(entry_step_coefficient.get())


def draw(event):
    global fleeting, cur_point

    canvas.delete(fleeting)

    x, y = 0, 0

    for i in range(3000):
        cur_point = random_point()
        x, y = cur_point.x, cur_point.y
        canvas.create_oval(x - 0.1, y - 0.1, x + 0.1, y + 0.1, fill='yellow', outline='black')

    fleeting = canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='red', outline='black')


cur_point = Point(400, 201)
start_points_list = []
step_coefficient = 0.5

entry_start_points = Entry(root, width=20)
entry_step_coefficient = Entry(root, width=20)
button_save_points = Button(text="save points")
button_draw = Button(text="draw")
button_save_step = Button(text="save step")
canvas = Canvas(root, width=800, height=600, bg='white')

fleeting = canvas.create_oval(399.5, 200.5, 400.5, 201.5, fill='red', outline='black')

canvas.bind('<Button-1>', add_point_from_click)
button_save_points.bind('<Button-1>', choice_points_from_list)
button_draw.bind('<Button-1>', draw)
button_save_step.bind('<Button-1>', save_step)

canvas.pack()
entry_start_points.pack()
button_save_points.pack()
entry_step_coefficient.pack()
button_save_step.pack()
button_draw.pack()

root.mainloop()

from tkinter import *

import random

root = Tk()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def random_point(a, A, ss):
    k = len(a)
    r = random.randint(1, k) - 1
    return Point((A.x + ss * (a[r].x - A.x)), (A.y + ss * (a[r].y - A.y)))


def choice_coor(event):
    global a, e1
    c.delete(ALL)
    a = []
    s = e1.get()
    lst = s.split()
    for i in range(len(lst) // 2):
        a.append(Point(int(lst[2 * i]), int(lst[2 * i + 1])))


def choice_coor_2(event):
    global a
    x = event.x
    y = event.y
    a.append(Point(x, y))
    c.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red', outline='black')


def save_step(event):
    global ss, e2
    ss = float(e2.get())


def draw2(event):
    global fleeting, A, ss, a

    c.delete(fleeting)
    for i in range(3000):
        A = random_point(a, A, ss)
        x = A.x
        y = A.y
        c.create_oval(x - 0.1, y - 0.1, x + 0.1, y + 0.1, fill='yellow', outline='black')

    fleeting = c.create_oval(x - 2, y - 2, x + 2, y + 2, fill='red', outline='black')


A = Point(400, 201)
a = []
ss = 0.5
e1 = Entry(root, width=20)
e2 = Entry(root, width=20)
b1 = Button(text="save coor")
b2 = Button(text="draw")
b3 = Button(text="save step")
c = Canvas(root, width=800, height=600, bg='white')

fleeting = c.create_oval(399.5, 200.5, 400.5, 201.5, fill='red', outline='black')

c.bind('<Button-1>', choice_coor_2)
b1.bind('<Button-1>', choice_coor)
b2.bind('<Button-1>', draw2)
b3.bind('<Button-1>', save_step)

c.pack()
e1.pack()
b1.pack()
e2.pack()
b3.pack()
b2.pack()

root.mainloop()

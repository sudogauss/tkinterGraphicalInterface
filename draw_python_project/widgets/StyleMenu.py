from tkinter import *


class StyleMenu:

    def __init__(self, root):
        self.frame = Frame(root).pack(side=RIGHT)

        self.var_coors = StringVar()

        self.var_coors.set("x: 0.0, y: 0.0")

        self.label_coors = Label(self.frame, textvariable=self.var_coors)

        self.label_coors.pack(padx=10, pady=10)

    def set_coors(self, x, y):
        math_x = x - 400.0
        math_y = 350.0 - y
        coors = "x: " + str(math_x) + ", y: " + str(math_y)
        self.var_coors.set(coors)

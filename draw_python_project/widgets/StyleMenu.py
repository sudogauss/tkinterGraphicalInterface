from tkinter import *
from utils.consts import X_OFFSET, Y_OFFSET


class StyleMenu:

    def __init__(self, root):
        self.frame = Frame(root).pack(side=RIGHT)

        self.var_coors = StringVar()

        self.var_coors.set("x: 0.0, y: 0.0")

        self.label_coors = Label(self.frame, textvariable=self.var_coors)

        self.label_coors.pack(padx=10, pady=10)

    def set_coors(self, x, y):
        math_x = x - X_OFFSET
        math_y = Y_OFFSET - y
        coors = "x: " + str(math_x) + ", y: " + str(math_y)
        self.var_coors.set(coors)

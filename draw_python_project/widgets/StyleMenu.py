from tkinter import *
from tkinter import ttk
from utils.consts import X_OFFSET, Y_OFFSET


class StyleMenu:

    def __init__(self, root):
        self.frame = Frame(root).pack(side=RIGHT)

        self.var_coors = StringVar()

        self.var_coors.set("x: 0.0, y: 0.0")

        self.label_coors = Label(self.frame, textvariable=self.var_coors)
        self.fill_label = Label(self.frame, text="fill color:")
        self.outline_label = Label(self.frame, text="outline color:")

        self.fill_colors = ttk.Combobox(self.frame, values=[
            "red",
            "green",
            "blue",
            "yellow",
            "white",
            "black",
            "gray",
            "purple"
        ])
        self.fill_colors.current(1)
        
        self.outline_colors = ttk.Combobox(self.frame, values=[
            "red",
            "green",
            "blue",
            "yellow",
            "white",
            "black",
            "gray",
            "purple"
        ])
        self.outline_colors.current(1)

        self.fill_label.pack()
        self.fill_colors.pack(pady=5)
        self.outline_label.pack()
        self.outline_colors.pack(pady=5)
        self.label_coors.pack(padx=10, pady=10)

    def set_coors(self, x, y):
        math_x = x - X_OFFSET
        math_y = Y_OFFSET - y
        coors = "x: " + str(math_x) + ", y: " + str(math_y)
        self.var_coors.set(coors)

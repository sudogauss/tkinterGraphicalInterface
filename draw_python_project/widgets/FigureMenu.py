from tkinter import *
from figures.Point import Point
from figures.Circle import Circle
from figures.Triangle import Triangle
from managers.figure_manager import FigureManager


class FigureMenu:

    def __init__(self, root):
        self.frame = Frame(root).pack(side=RIGHT)

        self.name = StringVar()
        self.coors = StringVar()

        self.x = StringVar()
        self.y = StringVar()

        self.name.set("Figure")
        self.coors.set("x: 0, y: 0")

        self.label_name = Label(self.frame, textvariable=self.name)
        self.label_coors = Label(self.frame, textvariable=self.coors)

        self.label_name.pack(pady=5)
        self.label_coors.pack(pady=5)

        self.entry_x = Entry(self.frame, textvariable=self.x)
        self.entry_y = Entry(self.frame, textvariable=self.y)

        self.entry_x.pack(pady=3)
        self.entry_y.pack(pady=3)

        self.perimeter = StringVar()
        self.area = StringVar()
        self.perimeter.set("perimeter: 0")
        self.area.set("area: 0")

        self.perimeter_label = Label(self.frame, textvariable=self.perimeter)
        self.area_label = Label(self.frame, textvariable=self.area)

    def update(self):
        if isinstance(FigureManager.menu_figure, Point):
            self.name.set("Point")
            x, y = FigureManager.menu_figure.get_coordinates()
            math_x = x - 400.0
            math_y = 350.0 - y
            self.coors.set("x: " + str(math_x) + ",y: " + str(math_y))
            self.perimeter_label.pack_forget()
            self.area_label.pack_forget()
        else:
            self.name.set("Other")
            self.perimeter_label.pack(pady=4)
            self.area_label.pack(pady=4)




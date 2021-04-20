from tkinter import *
from figures.Point import Point
from figures.Circle import Circle
from figures.Triangle import Triangle
from managers.figure_manager import FigureManager
import math


class FigureMenu:

    def __init__(self, root):
        self.frame = Frame(root).pack(side=RIGHT)

        self.painter = root.painter

        self.name = StringVar()
        self.coors = StringVar()

        self.x = StringVar()
        self.y = StringVar()
        self.r = StringVar()

        self.x2 = StringVar()
        self.y2 = StringVar()
        self.x3 = StringVar()
        self.y3 = StringVar()

        self.name.set("Figure")
        self.coors.set("x: 0, y: 0")

        self.label_name = Label(self.frame, textvariable=self.name)
        self.label_coors = Label(self.frame, textvariable=self.coors)
        self.label_x = Label(self.frame, text="x1")
        self.label_y = Label(self.frame, text="y1")
        self.label_x2 = Label(self.frame, text="x2")
        self.label_y2 = Label(self.frame, text="y2")
        self.label_x3 = Label(self.frame, text="x3")
        self.label_y3 = Label(self.frame, text="y3")
        self.label_r = Label(self.frame, text="r")
        self.change_position_button = Button(self.frame, text="change position", command=self.change_position)
        self.change_size_button = Button(self.frame, text="change size", command=self.change_size)

        self.label_name.pack(pady=5)
        self.label_coors.pack(pady=5)

        self.entry_x = Entry(self.frame, textvariable=self.x)
        self.entry_y = Entry(self.frame, textvariable=self.y)
        self.entry_r = Entry(self.frame, textvariable=self.r)

        self.entry_x2 = Entry(self.frame, textvariable=self.x2)
        self.entry_y2 = Entry(self.frame, textvariable=self.y2)
        self.entry_x3 = Entry(self.frame, textvariable=self.x3)
        self.entry_y3 = Entry(self.frame, textvariable=self.y3)

        self.label_x.pack(pady=2)
        self.entry_x.pack(pady=3)
        self.label_y.pack(pady=2)
        self.entry_y.pack(pady=3)

        self.perimeter = StringVar()
        self.area = StringVar()
        self.perimeter.set("perimeter: 0")
        self.area.set("area: 0")

        self.perimeter_label = Label(self.frame, textvariable=self.perimeter)
        self.area_label = Label(self.frame, textvariable=self.area)

    def update(self):
        self.forget_pack()
        if isinstance(FigureManager.menu_figure, Point):
            self.name.set("Point")
            x, y = FigureManager.menu_figure.get_coordinates()
            math_x = x - 400.0
            math_y = 350.0 - y
            self.coors.set("x: " + str(math_x) + ",y: " + str(math_y))
            self.change_position_button.pack(pady=4)
            self.change_size_button.pack(pady=3)
        elif isinstance(FigureManager.menu_figure, Circle):
            self.name.set("Circle")
            x, y = FigureManager.menu_figure.get_coordinates()
            r = FigureManager.menu_figure.get_radius()
            math_x = x - 400.0
            math_y = 350.0 - y
            self.coors.set("center x: " + str(math_x) + ",y: " + str(math_y) + ";r= " + str(r))
            p = 2 * math.pi * r
            s = math.pi * r * r
            self.label_r.pack()
            self.entry_r.pack()
            self.change_position_button.pack(pady=4)
            self.change_size_button.pack(pady=3)
            self.perimeter.set("perimeter: " + str(p))
            self.area.set("area: " + str(s))
            self.perimeter_label.pack(pady=4)
            self.area_label.pack(pady=4)
        elif isinstance(FigureManager.menu_figure, Triangle):
            self.name.set("Triangle")
            all_coordinates = FigureManager.menu_figure.get_all_coordinates()
            coors_string_val = "coordinates "
            for i in range(3):
                x, y = all_coordinates[2*i], all_coordinates[2*i+1]
                num = i+1
                math_x = x - 400.0
                math_y = 350.0 - y
                coors_string_val = coors_string_val + "x" + str(num) + ": " + str(math_x) + ",y" + str(num) + ": " + str(math_y) + " ;"
            self.coors.set(coors_string_val)
            self.label_x2.pack()
            self.entry_x2.pack()

            self.label_y2.pack()
            self.entry_y2.pack()

            self.label_x3.pack()
            self.entry_x3.pack()

            self.label_y3.pack()
            self.entry_y3.pack()

            self.change_position_button.pack(pady=4)
            self.change_size_button.pack(pady=3)
            p = FigureManager.menu_figure.vertex1.distance(FigureManager.menu_figure.vertex2) + \
                FigureManager.menu_figure.vertex1.distance(FigureManager.menu_figure.vertex3) + \
                FigureManager.menu_figure.vertex2.distance(FigureManager.menu_figure.vertex3)
            s = FigureManager.menu_figure.area()
            self.perimeter.set("perimeter: " + str(p))
            self.area.set("area: " + str(s))
            self.perimeter_label.pack(pady=4)
            self.area_label.pack(pady=4)

    def forget_pack(self):
        self.perimeter_label.pack_forget()
        self.area_label.pack_forget()
        self.change_position_button.pack_forget()
        self.change_size_button.pack_forget()
        self.label_x2.pack_forget()
        self.label_y2.pack_forget()
        self.label_x3.pack_forget()
        self.label_y3.pack_forget()
        self.label_r.pack_forget()
        self.entry_r.pack_forget()
        self.entry_x2.pack_forget()
        self.entry_y2.pack_forget()
        self.entry_x3.pack_forget()
        self.entry_y3.pack_forget()

    def change_position(self):
        if isinstance(FigureManager.menu_figure, Point):
            str_x, str_y = self.x.get(), self.y.get()
            if str_x != '' and str_y != '':
                x, y = int(str_x), int(str_y)
                figure_x, figure_y = FigureManager.menu_figure.get_coordinates()
                self.painter.move(FigureManager.menu_figure.canvas_object, (-figure_x + x + 400), (-figure_y + 350 - y))
                FigureManager.menu_figure.set_coordinates(x + 400, 350 - y)
                self.update()

    def change_size(self):
        print("Ok")






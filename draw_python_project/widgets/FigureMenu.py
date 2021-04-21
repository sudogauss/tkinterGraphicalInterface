from tkinter import *
from figures.Point import Point
from figures.Circle import Circle
from figures.Triangle import Triangle
from managers.figure_manager import FigureManager
import math
from utils.consts import X_OFFSET, Y_OFFSET


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
        self.change_button = Button(self.frame, text="change", command=self.change)

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
            math_x = x - X_OFFSET
            math_y = Y_OFFSET - y
            self.coors.set("x: " + str(math_x) + ",y: " + str(math_y))
            self.change_position_button.pack(pady=4)
            self.change_size_button.pack(pady=3)
        elif isinstance(FigureManager.menu_figure, Circle):
            self.name.set("Circle")
            x, y = FigureManager.menu_figure.get_coordinates()
            r = FigureManager.menu_figure.get_radius()
            math_x = x - X_OFFSET
            math_y = Y_OFFSET - y
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
                math_x = x - X_OFFSET
                math_y = Y_OFFSET - y
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

            self.change_button.pack(pady=4)
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
        self.change_button.pack_forget()
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
        if isinstance(FigureManager.menu_figure, Point) or isinstance(FigureManager.menu_figure, Circle):
            str_x, str_y = self.x.get(), self.y.get()
            if str_x != '' and str_y != '':
                x, y = int(str_x), int(str_y)
                figure_x, figure_y = FigureManager.menu_figure.get_coordinates()
                self.painter.move(FigureManager.menu_figure.canvas_object, (-figure_x + x + X_OFFSET), (-figure_y + Y_OFFSET - y))
                FigureManager.menu_figure.set_coordinates(x + X_OFFSET, Y_OFFSET - y)
                self.update()

    def change_size(self):
        if isinstance(FigureManager.menu_figure, Circle):
            str_r = self.r.get()
            if str_r != '':
                r = int(str_r)
                self.painter.remove_by_id(FigureManager.menu_figure.canvas_object)
                center_x, center_y = FigureManager.menu_figure.get_coordinates()
                modified_circle = Circle(center_x, center_y, r)
                self.painter.draw_circle(modified_circle)
                FigureManager.set_menu_figure(modified_circle)
                self.update()

    def change(self):
        if isinstance(FigureManager.menu_figure, Triangle):
            str_x1, str_y1 = self.x.get(), self.y.get()
            str_x2, str_y2 = self.x2.get(), self.y2.get()
            str_x3, str_y3 = self.x3.get(), self.y3.get()

            self.painter.remove_by_id(FigureManager.menu_figure.canvas_object)
            all_coors = FigureManager.menu_figure.get_all_coordinates()

            if str_x1 != '' and str_y1 != '':
                x1, y1 = int(str_x1) + X_OFFSET, Y_OFFSET - int(str_y1)
                all_coors[0] = x1
                all_coors[1] = y1
            if str_x2 != '' and str_y2 != '':
                x2, y2 = int(str_x2) + X_OFFSET, Y_OFFSET - int(str_y2)
                all_coors[2] = x2
                all_coors[3] = y2
            if str_x3 != '' and str_y3 != '':
                x3, y3 = int(str_x3) + X_OFFSET, Y_OFFSET - int(str_y3)
                all_coors[4] = x3
                all_coors[5] = y3

            modified_triangle = Triangle(all_coors[0], all_coors[1], all_coors[2], all_coors[3], all_coors[4], all_coors[5])
            self.painter.draw_triangle(modified_triangle)
            FigureManager.set_menu_figure(modified_triangle)
            self.update()






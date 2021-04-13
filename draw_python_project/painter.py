from tkinter import *
from figures.Point import Point
from draw_python_project.managers.figure_manager import FigureManager


class Painter:

    def __init__(self):
        self.canvas = None

    def set_canvas(self, canvas):
        self.canvas = canvas

    def create_coordinate_system(self):

        for i in range(0, 800, 10):
            self.canvas.create_line(i, 0, i, 700, width=0.2)

        for i in range(0, 700, 10):
            self.canvas.create_line(0, i, 800, i, width=0.2)

        self.canvas.grid(padx=1, pady=1, row=1, column=0, sticky=W + E + N + S, columnspan=6, rowspan=20)

        self.canvas.create_line(400, 700, 400, 0, width=2, arrow=LAST)
        self.canvas.create_line(0, 350, 800, 350, width=2, arrow=LAST)

    def draw_point(self, point, r):
        center_x, center_y = point.get_coordinates()
        canvas_point = self.canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, fill="red")
        FigureManager.add_figure(point)
        point.set_canvas_object(canvas_point)

    def draw_circle(self, circle):
        center_x, center_y = circle.get_center()
        r = circle.get_radius()
        canvas_circle = self.canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, fill="blue")
        FigureManager.add_figure(circle)
        circle.set_canvas_object(canvas_circle)

    def remove(self, x, y):
        figure_id = self.canvas.find_closest(x, y)
        if figure_id[0] > 152:
            if FigureManager.remove_figure(figure_id[0], x, y):
                self.canvas.delete(figure_id[0])

    def move(self, canvas_object, x, y):
        self.canvas.move(canvas_object, x, y)

    def get_figure_id(self, x, y):
        return self.canvas.find_closest(x, y)[0]

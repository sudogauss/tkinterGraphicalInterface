from tkinter import *
from figures.Point import Point


class Painter:

    def __init__(self):
        self.canvas = None

    def set_canvas(self, canvas):
        self.canvas = canvas

    def create_coordinate_system(self):
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        self.canvas.delete('grid_line')

        for i in range(0, w, 10):
            self.canvas.create_line([(i, 0), (i, h)], fill='black', tags='grid_line_w')

        for i in range(0, h, 10):
            self.canvas.create_line([(0, i), (w, i)], fill='black', tags='grid_line_h')

        self.canvas.grid(padx=1, pady=1, row=1, column=0, sticky=W + E + N + S, columnspan=6, rowspan=20)

        self.canvas.create_line(400, 700, 400, 0, width=2, arrow=LAST)
        self.canvas.create_line(0, 350, 800, 350, width=2, arrow=LAST)

    def draw_point(self, point, r):
        center_x, center_y = point.get_coordinates()
        self.canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, fill="red")

    def draw_circle(self, circle):
        center_x, center_y = circle.get_center()
        r = circle.get_radius()
        self.canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, fill="blue")

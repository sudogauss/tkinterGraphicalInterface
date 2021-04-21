from tkinter import *
from utils.consts import *
from managers.figure_manager import FigureManager
from managers.style_manager import StyleManager


class Painter:

    def __init__(self):
        self.canvas = None

    def set_canvas(self, canvas):
        self.canvas = canvas

    def create_coordinate_system(self):

        for i in range(0, WIDTH, COORS_STEP):
            self.canvas.create_line(i, 0, i, HEIGHT, width=0.2)

        for i in range(0, HEIGHT, COORS_STEP):
            self.canvas.create_line(0, i, WIDTH, i, width=0.2)

        self.canvas.pack(side=LEFT)

        self.canvas.create_line(X_OFFSET, HEIGHT, X_OFFSET, 0, width=2, arrow=LAST)
        self.canvas.create_line(0, Y_OFFSET, WIDTH, Y_OFFSET, width=2, arrow=LAST)

    def draw_point(self, point, r):
        center_x, center_y = point.get_coordinates()
        canvas_point = self.canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r,
                                               fill=StyleManager.get_fill_color(),
                                               outline=StyleManager.get_outline_color())
        FigureManager.add_figure(point)
        point.set_canvas_object(canvas_point)

    def draw_circle(self, circle):
        center_x, center_y = circle.get_center()
        r = circle.get_radius()
        canvas_circle = self.canvas.create_oval(center_x - r, center_y - r, center_x + r, center_y + r,
                                                fill=StyleManager.get_fill_color(),
                                                outline=StyleManager.get_outline_color())
        FigureManager.add_figure(circle)
        circle.set_canvas_object(canvas_circle)

    def draw_triangle(self, triangle):
        x1, y1 = triangle.vertex1.x, triangle.vertex1.y
        x2, y2 = triangle.vertex2.x, triangle.vertex2.y
        x3, y3 = triangle.vertex3.x, triangle.vertex3.y
        canvas_triangle = self.canvas.create_polygon([x1, y1, x2, y2, x3, y3],
                                                     fill=StyleManager.get_fill_color(),
                                                     outline=StyleManager.get_outline_color())
        FigureManager.add_figure(triangle)
        triangle.set_canvas_object(canvas_triangle)

    def remove(self, x, y):
        figure_id = self.canvas.find_closest(x, y)
        if figure_id[0] > ID_OFFSET:
            if FigureManager.remove_figure(figure_id[0], x, y):
                self.canvas.delete(figure_id[0])

    def remove_by_id(self, figure_id):
        self.canvas.delete(figure_id)

    def move(self, canvas_object, x, y):
        self.canvas.move(canvas_object, x, y)

    def get_figure_id(self, x, y):
        return self.canvas.find_closest(x, y)[0]

from figures.Triangle import Triangle
from managers.figure_manager import FigureManager


class TriangleInteractHandlers:

    def __init__(self, painter):
        self.painter = painter

    def create_triangle_handler(self, x, y):
        if FigureManager.get_figure() == "triangle":
            r = 25
            x1, y1 = x, y
            x2, y2 = x - r, y
            x3, y3 = x, y - r
            triangle = Triangle(x1, y1, x2, y2, x3, y3)
            self.painter.draw_triangle(triangle)

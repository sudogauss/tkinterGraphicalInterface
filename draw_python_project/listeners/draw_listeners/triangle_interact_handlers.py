from figures.Triangle import Triangle
from managers.figure_manager import FigureManager


class TriangleInteractHandlers:

    def __init__(self, painter):
        self.painter = painter

    def create_triangle_handler(self, x, y):
        if FigureManager.get_figure() == "triangle":
            r = 40
            x1, y1 = x, y
            x2, y2 = x - r, y
            x3, y3 = x, y - r
            triangle = Triangle(x1, y1, x2, y2, x3, y3)
            FigureManager.set_menu_figure(triangle)
            self.painter.draw_triangle(triangle)

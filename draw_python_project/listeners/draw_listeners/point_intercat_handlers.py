from draw_python_project.figures.Point import Point
from draw_python_project.managers.figure_manager import FigureManager


class PointInteractHandlers:

    def __init__(self, painter):
        self.painter = painter

    def create_point_handler(self, x, y):
        if FigureManager.get_figure() == "point":
            point = Point(x, y)
            self.painter.draw_point(point, 2)

from figures.Point import Point
from managers.figure_manager import FigureManager
from utils.consts import POINT_SIZE


class PointInteractHandlers:

    def __init__(self, painter):
        self.painter = painter

    def create_point_handler(self, x, y):
        if FigureManager.get_figure() == "point":
            point = Point(x, y)
            FigureManager.set_menu_figure(point)
            self.painter.draw_point(point, POINT_SIZE)

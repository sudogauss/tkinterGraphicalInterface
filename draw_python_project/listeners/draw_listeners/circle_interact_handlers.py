from figures.Circle import Circle
from managers.figure_manager import FigureManager


class CircleInteractHandlers:

    def __init__(self, painter):
        self.painter = painter

    def create_circle_handler(self, x, y):
        if FigureManager.get_figure() == "circle":
            circle = Circle(x, y, 25)
            FigureManager.set_menu_figure(circle)
            self.painter.draw_circle(circle)

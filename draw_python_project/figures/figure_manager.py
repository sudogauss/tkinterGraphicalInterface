class FigureManager:

    figure = "point"

    @classmethod
    def set_figure_point(cls):
        cls.figure = "point"

    @classmethod
    def set_figure_circle(cls):
        cls.figure = "circle"

    @classmethod
    def set_figure_triangle(cls):
        cls.figure = "triangle"

    @classmethod
    def get_figure(cls):
        return cls.figure

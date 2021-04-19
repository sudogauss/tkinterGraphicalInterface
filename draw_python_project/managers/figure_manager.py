from figures.Point import Point


class FigureManager:

    figure = "point"
    figures = []
    index = 153
    moving_figure = None
    modified_figure = None

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

    @classmethod
    def add_figure(cls, figure):
        cls.figures.append([cls.index, figure])
        cls.index = cls.index + 1

    @classmethod
    def find_figure(cls, figure_id, x, y):
        figure = None

        if figure_id <= 152:
            return None

        for figure_id_figure_pair in cls.figures:
            if figure_id_figure_pair[0] == figure_id:
                figure = figure_id_figure_pair[1]
                break

        if figure is None:
            return None

        point = Point(x, y)

        if figure.distance(point) <= 3:
            return figure

        return None

    @classmethod
    def remove_figure(cls, figure_id, x, y):
        figure = None
        figure_index = 0
        for figure_id_figure_pair in cls.figures:
            if figure_id_figure_pair[0] == figure_id:
                figure = figure_id_figure_pair[1]
                break
            figure_index = figure_index + 1

        if figure is None:
            return False

        point = Point(x, y)

        if figure.distance(point) <= 3:
            cls.figures.pop(figure_index)
            return True
        return False

    @classmethod
    def set_moving_figure(cls, figure):
        cls.moving_figure = figure

    @classmethod
    def stop_moving_figure(cls):
        cls.moving_figure = None

    @classmethod
    def set_modified_figure(cls, figure):
        cls.modified_figure = figure

    @classmethod
    def stop_modification(cls):
        cls.modified_figure = None

from draw_python_project.figures.Point import Point


class Triangle:

    def __init__(self, peak1_x, peak1_y, peak2_x, peak2_y, peak3_x, peak3_y):
        self.vertex1 = Point(peak1_x, peak1_y)
        self.vertex2 = Point(peak2_x, peak2_y)
        self.vertex3 = Point(peak3_x, peak3_y)
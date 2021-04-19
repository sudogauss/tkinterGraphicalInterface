from figures.Point import Point
import math

class Triangle:

    def __init__(self, peak1_x, peak1_y, peak2_x, peak2_y, peak3_x, peak3_y):
        self.vertex1 = Point(peak1_x, peak1_y)
        self.vertex2 = Point(peak2_x, peak2_y)
        self.vertex3 = Point(peak3_x, peak3_y)
        self.canvas_object = None

    def set_canvas_object(self, canvas_object):
        self.canvas_object = canvas_object

    def area(self):
        x1, y1 = self.vertex1.x, self.vertex1.y
        x2, y2 = self.vertex2.x, self.vertex2.y
        x3, y3 = self.vertex3.x, self.vertex3.y
        return math.fabs((x1 * (y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

    def distance(self, point):
        triangle1 = Triangle(self.vertex1.x, self.vertex1.y, self.vertex2.x, self.vertex2.y, point.x, point.y)
        triangle2 = Triangle(self.vertex1.x, self.vertex1.y, self.vertex3.x, self.vertex3.y, point.x, point.y)
        triangle3 = Triangle(self.vertex2.x, self.vertex2.y, self.vertex3.x, self.vertex3.y, point.x, point.y)

        if math.fabs(triangle1.area() + triangle2.area() + triangle3.area() - self.area()) <= 0.01:
            return 0
        else:
            return 1100

    def get_coordinates(self):
        return self.vertex1.x, self.vertex1.y

    def set_coordinates(self, x, y):
        x1, y1 = self.vertex1.x, self.vertex1.y
        x2, y2 = self.vertex2.x, self.vertex2.y
        x3, y3 = self.vertex3.x, self.vertex3.y

        nx1, ny1 = x, y
        nx2, ny2 = x - x1 + x2, y - y1 + y2
        nx3, ny3 = x - x1 + x3, y - y1 + y3

        self.vertex1.x = nx1
        self.vertex1.y = ny1
        self.vertex2.x = nx2
        self.vertex2.y = ny2
        self.vertex3.x = nx3
        self.vertex3.y = ny3


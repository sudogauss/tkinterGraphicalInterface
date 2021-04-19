from math import pi
from figures.Point import Point


class Circle:
    def __init__(self, center_x=0, center_y=0, r=0):
        self.center_x = center_x
        self.center_y = center_y
        self.r = r
        self.canvas_object = None

    def calculate_perimeter(self):
        return 2 * pi * self.r

    def calculate_air(self):
        return pi * pow(self.r, 2)

    def get_center(self):
        return self.center_x, self.center_y

    def set_center(self, x, y):
        self.center_x = x
        self.center_y = y

    def set_coordinates(self, x, y):
        self.set_center(x, y)

    def get_coordinates(self):
        return self.get_center()

    def get_radius(self):
        return self.r

    def set_canvas_object(self, canvas_object):
        self.canvas_object = canvas_object

    def set_radius(self, radius):
        self.r = radius

    def distance(self, point):
        x, y = self.get_center()
        center = Point(x, y)
        return max(0, point.distance(center)-self.get_radius())

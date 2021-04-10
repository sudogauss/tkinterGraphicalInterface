import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def distance(self, point):
        x1 = self.x
        x2 = point.x
        y1 = self.y
        y2 = point.y
        return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

from math import pi


class Circle:
    def __init__(self, center_x=0, center_y=0, r=0):
        self.center_x = center_x
        self.center_y = center_y
        self.r = r

    def calculate_perimeter(self):
        return 2 * pi * self.r

    def calculate_air(self):
        return pi * pow(self.r, 2)

    def get_center(self):
        return self.center_x, self.center_y

    def set_center(self, x, y):
        self.center_x = x
        self.center_y = y

    def get_radius(self):
        return self.r

    def set_radius(self, radius):
        self.r = radius

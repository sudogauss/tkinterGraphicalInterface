class DistanceManager:

    first_point = None
    second_point = None
    index = 1
    distance_menu = None

    @classmethod
    def set_distance_menu(cls, distance_menu):
        cls.distance_menu = distance_menu

    @classmethod
    def set_point(cls, point):
        if cls.index == 1:
            cls.first_point = point
            cls.index = 2
        elif cls.index == 2:
            cls.second_point = point
            cls.index = 1

    @classmethod
    def set_distance(cls):
        if cls.first_point is None or cls.second_point is None:
            return

        cls.distance_menu.distance.set(str(round(cls.first_point.distance(cls.second_point), 2)))

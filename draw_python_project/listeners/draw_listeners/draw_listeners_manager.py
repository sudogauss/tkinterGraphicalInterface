from draw_python_project.listeners.draw_listeners.point_intercat_handlers import PointInteractHandlers
from draw_python_project.listeners.draw_listeners.circle_interact_handlers import CircleInteractHandlers


class DrawListenersManager:

    painter = None

    @classmethod
    def set_painter(cls, painter):
        cls.painter = painter

    def register_draw_listeners(self):
        self.painter.canvas.bind('<Button-1>', self.create_handler)
        self.painter.canvas.bind('<Button-3>', self.delete_handler)

    def create_handler(self, event):
        x, y = event.x, event.y
        point_interact_handlers = PointInteractHandlers(self.painter)
        circle_interact_handlers = CircleInteractHandlers(self.painter)
        point_interact_handlers.create_point_handler(x, y)
        circle_interact_handlers.create_circle_handler(x, y)

    def delete_handler(self, event):
        x, y = event.x, event.y
        self.painter.remove(x, y)


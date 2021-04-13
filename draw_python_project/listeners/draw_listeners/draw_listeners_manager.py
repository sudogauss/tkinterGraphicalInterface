from draw_python_project.listeners.draw_listeners.point_intercat_handlers import PointInteractHandlers
from draw_python_project.listeners.draw_listeners.circle_interact_handlers import CircleInteractHandlers
from draw_python_project.managers.figure_manager import FigureManager


class DrawListenersManager:

    painter = None
    point_interact_handlers = None
    circle_interact_handlers = None
    shift_pressed = False

    @classmethod
    def set_painter(cls, painter):
        cls.painter = painter
        cls.point_interact_handlers = PointInteractHandlers(painter)
        cls.circle_interact_handlers = CircleInteractHandlers(painter)

    def register_draw_listeners(self):
        self.painter.canvas.bind('<Button-1>', self.create_handler)
        self.painter.canvas.bind('<Button-3>', self.delete_handler)
        self.painter.canvas.bind('<B1-Motion>', self.drag_handler)
        self.painter.canvas.bind('<ButtonRelease-1>', self.stop_moving)

    def register_draw_key_listeners(self, root):
        root.bind_all('<KeyPress>', self.press)
        root.bind_all('<KeyRelease>', self.release)

    def create_handler(self, event):
        if self.shift_pressed:
            return
        x, y = event.x, event.y
        self.point_interact_handlers.create_point_handler(x, y)
        self.circle_interact_handlers.create_circle_handler(x, y)

    def delete_handler(self, event):
        x, y = event.x, event.y
        self.painter.remove(x, y)

    def drag_handler(self, event):
        if self.shift_pressed:
            x, y = event.x, event.y
            if FigureManager.moving_figure is None:
                figure_id = self.painter.get_figure_id(x, y)
                figure = FigureManager.find_figure(figure_id, x, y)
                if figure is None:
                    return
                FigureManager.set_moving_figure(figure)
            else:
                figure_x, figure_y = FigureManager.moving_figure.get_coordinates()
                self.painter.move(FigureManager.moving_figure.canvas_object, x - figure_x, y - figure_y)
                FigureManager.moving_figure.set_coordinates(x, y)

    def press(self, event):
        if event.keysym == "Shift_L":
            self.shift_pressed = True

    def release(self, event):
        if event.keysym == "Shift_L":
            self.shift_pressed = False
            FigureManager.stop_moving_figure()

    def stop_moving(self, event):
        FigureManager.stop_moving_figure()

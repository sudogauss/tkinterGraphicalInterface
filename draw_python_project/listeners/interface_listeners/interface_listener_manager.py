from tkinter import *


class InterfaceListenerManager:

    painter = None
    style_menu = None
    figure_menu = None

    @classmethod
    def set_painter(cls, painter):
        cls.painter = painter

    @classmethod
    def set_style_menu(cls, style_menu):
        cls.style_menu = style_menu

    def register_interface_listeners(self):
        self.painter.canvas.bind('<Motion>', self.change_coors)

    def change_coors(self, event):
        x, y = event.x, event.y
        self.style_menu.set_coors(x, y)

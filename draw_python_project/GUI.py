from tkinter import *
from painter import Painter
from listeners.draw_listeners.draw_listeners_manager import DrawListenersManager
from draw_python_project.listeners.interface_listeners.interface_listener_manager import InterfaceListenerManager
from widgets.ProgramMenu import ProgramMenu
from draw_python_project.widgets.StyleMenu import StyleMenu


class GUI(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.state('zoomed')
        self.title("WELCOME TO GUI")
        self.painter = Painter()
        self.painter.set_canvas(Canvas(self, width=800, height=700, bg="white"))
        draw_listener_manager = DrawListenersManager()
        draw_listener_manager.set_painter(self.painter)
        draw_listener_manager.register_draw_listeners()
        draw_listener_manager.register_draw_key_listeners(self)

    def create_menu(self):
        menu = ProgramMenu(self)
        self.config(menu=menu)

    def create_style_menu(self):
        style_menu = StyleMenu(self)
        interface_listener_manager = InterfaceListenerManager()
        interface_listener_manager.set_painter(self.painter)
        interface_listener_manager.set_style_menu(style_menu)
        interface_listener_manager.register_interface_listeners()


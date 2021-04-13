from tkinter import *
from painter import Painter
from listeners.draw_listeners.draw_listeners_manager import DrawListenersManager
from widgets.ProgramMenu import ProgramMenu


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


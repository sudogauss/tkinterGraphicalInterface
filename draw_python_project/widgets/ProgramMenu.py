from tkinter import *
from draw_python_project.managers.figure_manager import FigureManager


class ProgramMenu(Menu):

    def __init__(self, root):
        Menu.__init__(self, root)

        self.figure_manager = FigureManager()

        file = Menu(self, tearoff=False)
        file.add_command(label="Exit", underline=1, command=self.quit)
        self.add_cascade(label="File", underline=0, menu=file)

        figure = Menu(self, tearoff=False)
        figure.add_command(label="Point", command=FigureManager.set_figure_point)
        figure.add_command(label="Circle", command=FigureManager.set_figure_circle)
        figure.add_command(label="Triangle", command=FigureManager.set_figure_triangle)
        self.add_cascade(label="Figure", underline=0, menu=figure)


from GUI import GUI
from tkinter import *

if __name__ == '__main__':
    root = GUI()
    root.painter.create_coordinate_system()
    root.create_menu()
    root.create_style_menu()
    root.mainloop()

from GUI import GUI

if __name__ == '__main__':
    root = GUI()
    root.painter.create_coordinate_system()
    root.create_menu()
    root.mainloop()

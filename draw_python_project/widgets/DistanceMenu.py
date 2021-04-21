from tkinter import *


class DistanceMenu:

    def __init__(self, root):
        self.frame = Frame(root).pack(side=RIGHT)
        self.header = Label(self.frame, text="distance", font=("Arial", 25))

        self.distance = StringVar()
        self.distance.set("0")

        self.distance_label = Label(self.frame, textvariable=self.distance)

        self.header.pack(pady=2)
        self.distance_label.pack(pady=2)

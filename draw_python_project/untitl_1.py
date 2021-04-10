"""
import math

class point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setPoint(self,x,y):
        self.x = x
        self.y = y

    def getPoint(self):
        return self.x, self.y

    def distance(self,point):
        x1 = self.x
        x2 = point.x
        y1 = self.y
        y2 = point.y
        return math.sqrt((x1-x2)*(x1-x2) +(y1-y2)*(y1-y2))

    
#import math


class Cercle():
    def __init__(self,oxCenter = 0,oyCenter = 0, radius = 0):
        self.oxCenter = oxCenter
        self.oyCenter = oyCenter
        self.radius = radius
        self.perimeter = 0
        self.air = 0
        self.pi = math.pi

    def perim(self):
        self.perimeter = 2*self.pi*self.radius


    def air_(self):
        self.air = self.radius*self.radius*self.pi


        
#import math
#from point import point as Point

class Triangle():
    def __init__(self,p1 = point(),p2 = point(), p3 = point()):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.a = p1.distance(p2)
        self.b = p1.distance(p3)
        self.c = p2.distance(p3)
        self.perimeter = 0
        self.air = 0


    def perim(self):
        self.perimeter = self.a + self.b + self.c


    def air_(self):
        p = (self.a + self.b + self.c) / 2
        self.air = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


        
from tkinter import *
#from point import point as Point
#from cercle import Cercle as Cercle
#from triangle import Triangle as Triangle

class blockTriangle():
    def __init__(self, tk):
        self.id = None
        self.tk = tk
        tk.createTriangle = True
        self._perimeter = None
        self._air = None
        self.Triangle = Triangle()
        self.color = Label(text='Choisissez la couleur du point', width=30, height=1)
        self.OptionList = ['black', 'red', 'green']
        self.tk.list_point.append(point())
        self.tk.variable = StringVar()
        self.tk.variable.set(self.OptionList[0])
        self.opt = OptionMenu(self.tk, self.tk.variable, *self.OptionList)
        self.opt.config(width=22)
        self.ord1 = Label(text='ox Point1 ', width=30, height=1)  # le texte
        self.abs1 = Label(text='oy Point1 ', width=30, height=1)  # le texte
        self.ord2 = Label(text='ox Point2', width=30, height=1)  # le texte
        self.abs2 = Label(text='oy Point2', width=30, height=1)  # le texte
        self.ord3 = Label(text='ox Point3', width=30, height=1)  # le texte
        self.abs3 = Label(text='oy Point3', width=30, height=1)  # le texte
        self.ox_entr1 = Entry(self.tk, textvariable=StringVar())
        self.oy_entr1 = Entry(self.tk, textvariable=StringVar())
        self.ox_entr2 = Entry(self.tk, textvariable=StringVar())
        self.oy_entr2 = Entry(self.tk, textvariable=StringVar())
        self.ox_entr3 = Entry(self.tk, textvariable=StringVar())
        self.oy_entr3 = Entry(self.tk, textvariable=StringVar())

        self.abs1.grid(row=1, column=7)
        self.oy_entr1.grid(row=2, column=7, pady=1)

        self.abs2.grid(row=3, column=7)
        self.oy_entr2.grid(row=4, column=7, pady=1)

        self.abs3.grid(row=5, column=7)
        self.oy_entr3.grid(row=6, column=7, pady=1)

        self.ord1.grid(row=1, column=6)
        self.ox_entr1.grid(row=2, column=6, pady=1)

        self.ord2.grid(row=3, column=6)
        self.ox_entr2.grid(row=4, column=6, pady=1)

        self.ord3.grid(row=5, column=6)
        self.ox_entr3.grid(row=6, column=6, pady=1)

        self.color.grid(row=7, column=6)
        self.opt.grid(row=8, column=6, pady=1)
        self.Cercle = None
        self._perimetre = None
        self._air = None

        self.accept = Button(text='accepter', width=10, height=2, bg="#fcff56", fg = "#121211", command=self.accepter)
        self.accept.grid(padx=1, pady=1, row=9, column=6)

        self.Perimeter = Button(text='Perimeter', width=10, height=2, bg="#fcff56", fg = "#121211", command=self.perimeter)
        self.Perimeter.grid(row=10, column=7, pady=1)

        self.Air = Button(text='Air', width=10, height=2, bg="#fcff56", fg = "#121211", command=self.air)
        self.Air.grid(row=10, column=6, pady=1)

        self.mouseAccept = Button(text='Mouse accept', width=10, height=2, bg="red", fg = "#121211", command=self.take_triangle)
        self.mouseAccept.grid(row=9, column=7, pady=1)

        #self.canvas.bind('<Button-1>', self.Mousecoords)  # track mouse taking
        self.tk.canvas.bind('<ButtonPress-1>', self.tk.clic)
    def delete(self):
        self.ord3.destroy()
        self.ord2.destroy()
        self.ord1.destroy()
        self.abs1.destroy()
        self.abs2.destroy()
        self.abs3.destroy()
        self.Air.destroy()
        self.Perimeter.destroy()
        self.opt.destroy()
        self.color.destroy()
        self.mouseAccept.destroy()
        self.ox_entr1.destroy()
        self.ox_entr2.destroy()
        self.ox_entr3.destroy()
        self.oy_entr1.destroy()
        self.oy_entr2.destroy()
        self.oy_entr3.destroy()
        if self.id != None:
            self.tk.canvas.delete(self.id)

        if self._air != None:
            self._air.destroy()
        if self._perimeter != None:
            self._perimeter.destroy()

    def perimeter(self):
        self.Triangle.perim()
        P = self.Triangle.perimeter
        self._perimeter= Label(text='Perimeter: \n' + str(round(P)), width=10, height=2,
                          bg='green')
        self._perimeter.grid(row=11, column=7, pady=1)




    def air(self):
        self.Triangle.air_()
        A = self.Triangle.air

        print(A)
        self._air = Label(text='Air: \n' + str(A), width=10, height=2,
                          bg='green')
        self._air.grid(row=11, column=6, pady=1)

    def take_triangle(self):
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)
        p1 = self.tk.list_point[-1]
        p2 = self.tk.list_point[-2]
        p3 = self.tk.list_point[-3]
        self.Triangle = Triangle(p3, p2, p1)
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)
        POINTS = []
        POINTS = [self.Triangle.p1.x + 400, 350 - self.Triangle.p1.y, 400 + self.Triangle.p2.x,
                  350 - self.Triangle.p2.y, 400 + self.Triangle.p3.x, 350 - self.Triangle.p3.y]
        self.id = self.tk.canvas.create_polygon(POINTS)

    def accepter(self):

        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)

        if len(self.ox_entr1.get()) * len(self.oy_entr1.get())*len(self.ox_entr2.get()) * len(self.oy_entr2.get())*len(self.ox_entr3.get()) * len(self.oy_entr3.get()) != 0:
            self.ox1 = int(self.ox_entr1.get())
            self.oy1 = int(self.oy_entr1.get())
            p1 = point(self.ox1,self.oy1)
            self.tk.list_point.append(p1)
            self.ox2 = int(self.ox_entr2.get())
            self.oy2 = int(self.oy_entr2.get())
            p2 = point(self.ox2,self.oy2)
            self.tk.list_point.append(p2)
            self.ox3 = int(self.ox_entr3.get())
            self.oy3 = int(self.oy_entr3.get())
            p3 = point(self.ox3,self.oy3)
            self.Triangle = Triangle(p1,p2,p3)
            self.tk.list_point.append(p3)


        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)
        POINTS = []
        POINTS = [self.Triangle.p1.x+400, 350-self.Triangle.p1.y, 400+self.Triangle.p2.x,350-self.Triangle.p2.y, 400 + self.Triangle.p3.x, 350 -self.Triangle.p3.y]

        print(POINTS)
        self.id = self.tk.canvas.create_polygon(POINTS)


class blockCercle():
    def __init__(self, tk):
        self.id = None
        self.tk = tk
        tk.createCercle = True
        self.color = Label(text='Choisissez la couleur du point', width=30, height=1)
        self.OptionList = ['black', 'red', 'green']
        self.tk.list_point.append(point())
        self.tk.variable = StringVar()
        self.tk.variable.set(self.OptionList[0])
        self.opt = OptionMenu(self.tk, self.tk.variable, *self.OptionList)
        self.opt.config(width=22)
        self.ord = Label(text='ox center', width=30, height=1)  # le texte
        self.abs = Label(text='oy center', width=30, height=1)  # le texte
        self.radius = Label(text='Radius', width=30, height=1)  # le texte

        self.ox_entr = Entry(self.tk, textvariable=StringVar())
        self.oy_entr = Entry(self.tk, textvariable=StringVar())
        self.center = Entry(self.tk, textvariable=StringVar())
        self.abs.grid(row=1, column=6)
        self.ox_entr.grid(row=2, column=6, pady=1)
        self.ord.grid(row=1, column=7, pady=1, rowspan=1)
        self.oy_entr.grid(row=2, column=7, pady=1)
        self.radius.grid(row=3, column=6, pady=1)
        self.center.grid(row=4, column=6, pady=1)
        self.color.grid(row=5, column=6)
        self.opt.grid(row=6, column=6, pady=1)
        self.Cercle = None

        self.accept = Button(text='accepter', width=10, height=2, bg="#fcff56", command=self.accepter)
        self.accept.grid(padx=1, pady=1, row=7, column=6)

        self.Perimeter = Button(text='Perimeter', width=10, height=2, bg="#fcff56", command=self.perimeter)
        self.Perimeter.grid(row=6, column=7, pady=1)

        self.Air = Button(text='Air', width=10, height=2, bg="#fcff56", command=self.air)
        self.Air.grid(row=4, column=7, pady=1)

        self.mouseAccept = Button(text='Mouse accept', width=10, height=2, bg="red", command=self.take_Cercle)
        self.mouseAccept.grid(row=8, column=6, pady=1)
        self._perimeter = None
        self._air = None

        # self.canvas.bind('<Button-1>', self.Mousecoords)  # track mouse taking
        self.tk.canvas.bind('<ButtonPress-1>', self.tk.clic)

    def perimeter(self):
        self.Cercle.perim()
        P = self.Cercle.perimeter
        self._perimeter= Label(text='Perimeter: \n' + str(round(P)), width=10, height=2,
                          bg='green')
        self._perimeter.grid(row=7, column=7, pady=1)
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)
        self.id = self.tk.canvas.create_oval(self.Cercle.oxCenter + 400 - self.Radius,
                                             -self.Cercle.oyCenter + 350 - self.Radius,
                                             self.Cercle.oxCenter + self.Radius + 400,
                                             -self.Cercle.oyCenter + self.Radius + 350,
                                             )#fill=self.tk.variable.get()


    def air(self):
        self.Cercle.air_()
        A = self.Cercle.air
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)
        self.id = self.tk.canvas.create_oval(self.Cercle.oxCenter + 400 - self.Radius, -self.Cercle.oyCenter + 350 - self.Radius,
                                             self.Cercle.oxCenter + self.Radius + 400, -self.Cercle.oyCenter + self.Radius + 350,
                                              fill=self.tk.variable.get())

        print(A)
        self._air = Label(text='Air: \n' + str(A), width=10, height=2,
                          bg='green')
        self._air.grid(row=5, column=7, pady=1)

    def take_Cercle(self):
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)
        p1 = self.tk.list_point[-1]
        p2 = self.tk.list_point[-2]
        self.Radius = p1.distance(p2)
        self.Cercle = Cercle(p2.x, p2.y, self.Radius)
        self.Cercle.perim()
        print(self.Cercle.perimeter)
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)
        self.id = self.tk.canvas.create_oval(self.tk.list_point[-2].x + 400 - self.Radius,
                                     -self.tk.list_point[-2].y + 350 - self.Radius,
                                     self.tk.list_point[-2].x + self.Radius + 400,
                                     -self.tk.list_point[-2].y + self.Radius + 350,
                                     )  # fill=self.tk.variable.get())

    def accepter(self):
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)

        if len(self.ox_entr.get()) * len(self.oy_entr.get()) != 0:
            self.ox = int(self.ox_entr.get())
            self.oy = int(self.oy_entr.get())
            self.Radius = int(self.center.get())
            self.Cercle = Cercle(self.ox, self.oy, self.Radius)
            print(self.Cercle.perimeter)

        p = point(self.ox, self.oy)
        self.tk.list_point.append(p)
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)

        self.id = self.tk.canvas.create_oval(self.ox + 400 - self.Radius, -self.oy + 350 - self.Radius,
                                     self.ox + self.Radius + 400, -self.oy + self.Radius + 350,
                                     )  # fill=self.tk.variable.get())
    def delete(self):
        self.ox_entr.destroy()
        self.oy_entr.destroy()
        self.opt.destroy()
        self.ord.destroy()
        self.abs.destroy()
        self.color.destroy()
        self.accept.destroy()
        self.mouseAccept.destroy()
        self.radius.destroy()
        self.center.destroy()
        self.Air.destroy()
        self.Perimeter.destroy()
        if self.id != None:
            self.tk.canvas.delete(self.id)
        if self._air != None:
            self._air.destroy()
        if self._perimeter != None:
            self._perimeter.destroy()


class blockPoint:
    def __init__(self, tk):
        self.color = Label(text='Choisissez la couleur du point', width=30, height=1)
        self.OptionList = ['black', 'red', 'green']
        self.tk = tk
        self.id = None
        self.dist = None
        tk.createPoint = True
        self.tk.list_point.append(point())
        self.tk.variable = StringVar()
        self.tk.variable.set(self.OptionList[0])
        self.opt = OptionMenu(self.tk, self.tk.variable, *self.OptionList)
        self.opt.config(width=22)
        self.ord = Label(text='Entrez la valeur entiere de l.ordonnee', width=30, height=1)  # le texte
        self.abs = Label(text='Entrez la valeur entiere de l.abscisse', width=30, height=1)  # le texte
        self.ox_entr = Entry(self.tk, textvariable=StringVar())
        self.oy_entr = Entry(self.tk, textvariable=StringVar())
        print('ree3' + str(self.ox_entr))
        print('ree4' + str(self.oy_entr))
        self.abs.grid(row=1, column=6)
        self.ox_entr.grid(row=2, column=6, pady=1)
        self.ord.grid(row=3, column=6, pady=1, rowspan=1)
        self.oy_entr.grid(row=4, column=6, pady=1)
        self.color.grid(row=5, column=6)
        self.opt.grid(row=6, column=6, pady=1)
        self.accept = Button(text='accepter', width=10, height=2, bg="#fcff56", command=self.accepter)
        self.accept.grid(padx=1, pady=1, row=7, column=6)
        self.distance = Button(text='distance', width=10, height=2, bg="red", command=self.take_botton_distance)
        self.distance.grid(padx=0.5, pady=0.5, row=8, column=6)
        # self.canvas.bind('<Button-1>', self.Mousecoords)  # track mouse taking
        self.tk.canvas.bind('<ButtonPress-1>', self.tk.clic)


        # self.canvas.delete(id)

    def take_botton_distance(self):
        print("take_botton_distance")
        p1 = self.tk.list_point[-1]
        p2 = self.tk.list_point[-2]
        self.Bdistance = p1.distance(p2)
        print(p1.distance(p2))
        self.dist = Label(text='Distance: \n' + str(round(((p1.distance(p2))), ndigits=2)), width=10, height=2,
                          bg='green')
        self.dist.grid(row=9, column=6, pady=1)
        x1 = p1.x + 400
        y1 = -p1.y + 350
        x2 = p2.x + 400
        y2 = -p2.y + 350
        return self.Bdistance



    def accepter(self):
        if len(self.ox_entr.get()) * len(self.oy_entr.get()) != 0:
            self.ox = int(self.ox_entr.get())
            self.oy = int(self.oy_entr.get())

        p = point(self.ox, self.oy)
        self.tk.list_point.append(p)
        radius = 1

        self.tk.id = self.tk.canvas.create_oval(self.ox + 400 - radius, -self.oy + 350 - radius, self.ox + radius + 400,
                                     -self.oy + radius + 350,
                                     fill=self.tk.variable.get())

    def take_botton_distance(self):
        print("take_botton_distance")
        p1 = self.tk.list_point[-1]
        p2 = self.tk.list_point[-2]
        self.Bdistance = p1.distance(p2)
        print(p1.distance(p2))
        self.dist = Label(text='Distance: \n' + str(round(((p1.distance(p2))), ndigits=2)), width=10, height=2,
                          bg='green')
        self.dist.grid(row=9, column=6, pady=1)
        x1 = p1.x + 400
        y1 = -p1.y + 350
        x2 = p2.x + 400
        y2 = -p2.y + 350
        if self.id != None:
            self.tk.canvas.delete(self.id)
        for id in self.tk.id:
            self.tk.canvas.delete(id)
        self.id = self.tk.canvas.create_line(x1, y1, x2, y2)
        return self.Bdistance


    def delete(self):
        self.ox_entr.destroy()
        self.oy_entr.destroy()
        self.opt.destroy()
        self.ord.destroy()
        self.abs.destroy()
        self.color.destroy()
        self.accept.destroy()
        self.distance.destroy()
        if self.id != None:
            self.tk.canvas.delete(self.id)

        if self.dist != None:
            self.dist.destroy()


class Shape(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.state('zoomed')  # on elargit la fenetre
        self.title("WELCOME TO Interface graphique")  # le nom
        self.canvas = Canvas(self, width=800, height=700, bg="white")  # dans self on cree l'objet self.canvas
        #self.canvas.pack()
        self.createPoint = False
        self.createCercle = False
        self.createTriangle = False
        self.BCercle = None
        self.BPoint = None
        self.BTriangle = None
        self.b = None
        self.Bdistance = None
        self.radius = None
        self.Radius = None
        self.dist = None
        self.oy_entr = None
        self.ox_entr = None
        self.ox = 0
        self.oy = 0
        self.id = []
        self.list_point = []
        self.point = Button(text='Point', width=15, height=2, bg="#fcff56")  # bouton
        self.Cercle = Button(text='Cercle', width=15, height=2, bg="#ff7d30")
        self.Triangle = Button(text='Triangle', width=15, height=2, bg="#fcff56")

        self.point.grid(padx=1, pady=1, row=0, column=0)  # on met les boutons sur le fenetre
        self.Cercle.grid(padx=1, pady=1, row=0, column=1)
        self.Triangle.grid(padx=1, pady=1, row=0, column=2)

        self.canvas.grid(padx=1, pady=1, row=1, column=0, sticky=W + E + N + S, columnspan=1,
                    rowspan=1)  # on fait apparaitre le self.canvas dans self
        self.canvas.bind('<Configure>', self.create_grid)

        self.point.bind('<Button-1>', self.take_point)
        self.Cercle.bind('<Button-1>',self.take_cercle)
        self.Triangle.bind('<Button-1>', self.take_triangle)

        #Cercle.bind('<Button-1>', take_point)
        #Triangle.bind('<Button-1>', take_point)
    def create_grid(self,event=None):
        w = self.canvas.winfo_width()  # Get current width of self.canvas
        h = self.canvas.winfo_height()  # Get current height of self.canvas
        self.canvas.delete('grid_line')  # Will only remove the grid_line

        for i in range(0, w, 10):
            self.canvas.create_line([(i, 0), (i, h)], fill='black', tags='grid_line_w')

        for i in range(0, h, 10):
            self.canvas.create_line([(0, i), (w, i)], fill='black', tags='grid_line_h')

        self.canvas.grid(padx=1, pady=1, row=1, column=0, sticky=W + E + N + S, columnspan=6, rowspan=20)

        self.canvas.create_line(400, 700, 400, 0, width=2, arrow=LAST)  # axe verticale
        self.canvas.create_line(0, 350, 800, 350, width=2, arrow=LAST)  # axe horizontale

    def clic(self, event):
        self.ox = event.x-400
        self.oy = -event.y + 350
        p = point(self.ox, self.oy)
        self.list_point.append(p)
        radius = 3
        self.id.append (self.canvas.create_oval(self.ox + 400 - radius, -self.oy + 350 - radius, self.ox + radius + 400,
                                     -self.oy + radius + 350,
                                     fill=self.variable.get()))

    def take_triangle(self,event):
        if self.createPoint:
            self.BPoint.delete()
            self.createPoint = False
        if self.createCercle:
            self.BCercle.delete()
            self.createCercle = False

        self.BTriangle = blockTriangle(self)

    def take_cercle(self,event):
        if self.createPoint:
            self.BPoint.delete()
            self.createPoint = False
        if self.createTriangle:
            self.BTriangle.delete()
            self.createTriangle = False

        self.BCercle = blockCercle(self)

    def take_point(self, event):

        if self.createTriangle:
            self.BTriangle.delete()
            self.createTriangle = False

        if self.createCercle:
            self.BCercle.delete()
            self.createCercle = False

        self.BPoint = blockPoint(self)















# -----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    fenetre = Shape()
    fenetre.mainloop()

"""



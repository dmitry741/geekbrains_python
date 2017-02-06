# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class my_point:
    ''' class point (X and Y)
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def to_string(self):
        print("I am a point ({}, {})".format(self.x, self.y))

class my_geo_helper:
    ''' class my_geo_helper allows to calculate some
    base properties for geometrical figures. 
    '''
    @staticmethod
    def distance(point1, point2):
        x1 = point1.GetX()
        y1 = point1.GetY()
        x2 = point2.GetX()
        y2 = point2.GetY()

        return math.sqrt((x2 - x1) * (x2 - x1) - (y2 - y1) * (y2 - y1))
        

class my_base_figure:
    ''' class my_base_figure is base for all geometrical figures
    '''
    def __init__(self):
        self.points = []

    def AddPoint(self, point):
        self.points.append(point)

    def GetPoint(self, index):
        return self.points[index]

    def Perimetr(self):
        d = 0
        i = 0
                         
        while i < self.points.count():
            d += my_geo_helper.distance(self.points[i], self.points[i + 1])
            i += 1

        return d

class my_triangle(my_base_figure):
    ''' class my_triangle is based on my_base_figure
    '''

    def __init__(self, point1, point2, point3):
        my_base_figure.__init__(self)
        my_base_figure.AddPoint(self, point1)
        my_base_figure.AddPoint(self, point2)
        my_base_figure.AddPoint(self, point3)                


    def to_string(self):
        print("I am a my_triangle)")

point = my_point(1, 2)
print(point.to_string())

point1 = my_point(0, 0)
point2 = my_point(1, 0)
point3 = my_point(0, 1)

tr = my_triangle(point1, point2, point3)
print(tr.GetPoint(1).GetX())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.


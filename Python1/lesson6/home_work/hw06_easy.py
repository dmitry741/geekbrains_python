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

        return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


    @staticmethod
    def triangle_square(point1, point2, point3):
        a = my_geo_helper.distance(point1, point2)
        b = my_geo_helper.distance(point2, point3)
        c = my_geo_helper.distance(point3, point1)
        p = (a + b + c) / 2

        return math.sqrt(p * (p - a) * (p - b) * (p - c))


    @staticmethod
    def is_collinear(point1, point2, point3, point4):
        x1 = point1.GetX()
        y1 = point1.GetY()
        x2 = point2.GetX()
        y2 = point2.GetY()

        x3 = point3.GetX()
        y3 = point3.GetY()
        x4 = point4.GetX()
        y4 = point4.GetY()
        
        ax = x2 - x1
        ay = y2 - y1
        bx = x4 - x3
        by = y4 - y3

        return (ax * by - bx * ay) == 0
        

class my_base_figure:
    ''' class my_base_figure is base for all geometrical figures
    '''
    def __init__(self):
        self.points = []

    def AddPoint(self, point):
        self.points.append(point)

    def GetPoint(self, index):
        return self.points[index]

    def Square(self):
        if len(self.points) < 3:
            return 0

        s = 0
        index1, index2, index3 = 0, 1, 2
        point1 = self.GetPoint(index1)
        
        while True:            
            point2 = self.GetPoint(index2)
            point3 = self.GetPoint(index3)

            s += my_geo_helper.triangle_square(point1, point2, point3)

            index2 += 1
            index3 += 1

            if index3 >= len(self.points):
                break

        return s        

    def Perimetr(self):
        d = 0
        i = 0
                         
        while i < len(self.points):
            point1 = self.points[i]
            point2 = self.points[(i + 1) % len(self.points)]
            d += my_geo_helper.distance(point1, point2)
            i += 1

        return d


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class my_triangle(my_base_figure):
    ''' class my_triangle is based on my_base_figure. It is a triangle.
    '''

    def __init__(self, point1, point2, point3):
        my_base_figure.__init__(self)
        my_base_figure.AddPoint(self, point1)
        my_base_figure.AddPoint(self, point2)
        my_base_figure.AddPoint(self, point3)

    def to_string(self):
        print("I am a my_triangle)")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

class my_isosceles_trapeze(my_base_figure):
    ''' class my_isosceles_trapeze is based on my_base_figure. It is a isosceles trapeze.
    '''
    def __init__(self, point1, point2, point3, point4):
        my_base_figure.__init__(self)
        my_base_figure.AddPoint(self, point1)
        my_base_figure.AddPoint(self, point2)
        my_base_figure.AddPoint(self, point3)
        my_base_figure.AddPoint(self, point4)

    def is_correct(self):
        if len(self.points) != 4:
            return False

        point1 = my_base_figure.GetPoint(0)
        point2 = my_base_figure.GetPoint(1)
        point3 = my_base_figure.GetPoint(2)
        point4 = my_base_figure.GetPoint(3)

        ls =[]
        
        ls.append(my_geo_helper.is_collinear(point1, point2, point3, point4))
        ls.append(my_geo_helper.distance(point1, point2) == my_geo_helper.distance(point3, point4))

        return all(ls)
                  


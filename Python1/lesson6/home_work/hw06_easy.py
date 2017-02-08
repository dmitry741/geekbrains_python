import math


class MyPoint:
    ''' class point (X and Y)
    '''
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        return "I am a point X = {} Y = {}".format(self._x, self._y)


class MyGeoHelper:
    ''' class my_geo_helper allows to calculate some
    base properties for geometrical figures. 
    '''
    @staticmethod
    def distance(point1, point2):
        x1 = point1.get_x()
        y1 = point1.get_y()
        x2 = point2.get_x()
        y2 = point2.get_y()

        return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    @staticmethod
    def triangle_square(point1, point2, point3):
        a = MyGeoHelper.distance(point1, point2)
        b = MyGeoHelper.distance(point2, point3)
        c = MyGeoHelper.distance(point3, point1)
        p = (a + b + c) / 2

        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def is_collinear(point1, point2, point3, point4):
        x1 = point1.get_x()
        y1 = point1.get_y()
        x2 = point2.get_x()
        y2 = point2.get_y()

        x3 = point3.get_x()
        y3 = point3.get_y()
        x4 = point4.get_x()
        y4 = point4.get_y()
        
        ax = x2 - x1
        ay = y2 - y1
        bx = x4 - x3
        by = y4 - y3

        return (ax * by - bx * ay) == 0
        

class MyBaseFigure:
    ''' class my_base_figure is base for all geometrical figures
    '''
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def get_point(self, index):

        point = MyPoint(0, 0)
        
        try:
            point = self.points[index]
        except IndexError:
            print("Index is out of range.")
            
        return point

    @property
    def square(self):
        if len(self.points) < 3:
            return 0

        s = 0
        index1, index2, index3 = 0, 1, 2
        point1 = self.get_point(index1)
        
        while True:            
            point2 = self.get_point(index2)
            point3 = self.get_point(index3)

            s += MyGeoHelper.triangle_square(point1, point2, point3)

            index2 += 1
            index3 += 1

            if index3 >= len(self.points):
                break

        return s        

    @property
    def perimetr(self):
        d = 0
        i = 0
                         
        while i < len(self.points):
            point1 = self.points[i]
            point2 = self.points[(i + 1) % len(self.points)]
            d += MyGeoHelper.distance(point1, point2)
            i += 1

        return d


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class MyTriangle(MyBaseFigure):
    ''' class my_triangle is based on my_base_figure. It is a triangle.
    '''

    def __init__(self, point1, point2, point3):
        MyBaseFigure.__init__(self)
        MyBaseFigure.add_point(self, point1)
        MyBaseFigure.add_point(self, point2)
        MyBaseFigure.add_point(self, point3)

    def __str__(self):
        print("I am a my_triangle)")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

class MyIsoscelesTrapeze(MyBaseFigure):
    ''' class my_isosceles_trapeze is based on my_base_figure. It is a isosceles trapeze.
    '''
    def __init__(self, point1, point2, point3, point4):
        MyBaseFigure.__init__(self)
        MyBaseFigure.add_point(self, point1)
        MyBaseFigure.add_point(self, point2)
        MyBaseFigure.add_point(self, point3)
        MyBaseFigure.add_point(self, point4)

    def is_correct(self):
        if len(self.points) != 4:
            return False

        point1 = MyBaseFigure.get_point(self, 0)
        point2 = MyBaseFigure.get_point(self, 1)
        point3 = MyBaseFigure.get_point(self, 2)
        point4 = MyBaseFigure.get_point(self, 3)

        ls =[]
        
        ls.append(MyGeoHelper.is_collinear(point2, point3, point1, point4))
        ls.append(MyGeoHelper.distance(point1, point2) == MyGeoHelper.distance(point3, point4))

        return all(ls)

    def __str__(self):
        print("I am a MyIsoscelesTrapeze)")

point1 = MyPoint(0, 0)
point2 = MyPoint(0, 1)
point3 = MyPoint(1, 0)

triangle = MyTriangle(point1, point2, point3)
print("Площадь треугольника = ", triangle.square)
print("Периметр треугольника = ", triangle.perimetr)

point1 = MyPoint(0, 0)
point2 = MyPoint(1, 1)
point3 = MyPoint(2, 1)
point4 = MyPoint(3, 0)

trapeze = MyIsoscelesTrapeze(point1, point2, point3, point4)
print("Площадь трапеции = ", trapeze.square)
print("Периметр трапеции = ", trapeze.perimetr)

if trapeze.is_correct():
    print("Это равнобедренная трапеция")
else:
    print("Это НЕ равнобедренная трапеция или вообще не трапеция")

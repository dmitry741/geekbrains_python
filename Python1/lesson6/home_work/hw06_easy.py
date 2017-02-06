# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class my_point:
    ''' class point X and Y
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        print("I am a point ({}, {})".format(self.x, self.y))

class my_geo_helper:
    ''' class my_geo_helper allows to calculate some
    base properties for geometrical figures. 
    '''
    pass

class my_base_figure:
    ''' class my_base_figure is base for all geometrical figure
    '''
    def __init__(self):
        self.points = []

    def AddPoint(point):
        self.points.append(point)

    def GetPoint(index):
        return self.points[index]        

point = my_point(1, 2)
print(point.to_string())

class my_triangle(my_base_figure):
    ''' class my_triangle is based on my_base_figure
    '''
    pass


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.


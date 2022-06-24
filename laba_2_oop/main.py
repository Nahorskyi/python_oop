from abc import ABC
from abc import abstractclassmethod
from math import sin
from math import pi
from math import sqrt
from math import radians


class Figure(ABC):
    abstractclassmethod
    def __init__(self):
        pass

    abstractclassmethod
    def square(self, *args):
        pass

    abstractclassmethod
    def perimeter(self, *args):
        pass

def Validation(value):
    if value <= 0:
        raise ValueError("Не підходить значення")
    return value


class Triangle (Figure):
    def __init__(self, a, b ,с):
        self.a = a
        self.a = Validation(a)
        self.b = b
        self.b = Validation(b)
        self.c = с
        self.с = Validation(с)

    def square(self):
        if (self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a ):
          p=(self.a + self.b + self.c)/2
          return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        else:
            return 0

    def perimeter(self):
        if (self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a ):
          return (self.a + self.b + self.c)
        else:
            return 0

     

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.a = Validation(a)
        self.b = b
        self.b = Validation(b)

    def square(self):
        return self.a * self.b  

    def perimeter(self):
        return 2*self.a+2*self.b      


class Square(Rectangle):
    def __init__(self, a):
        self.a = a
        self.a = Validation(a)

    def square(self):
        return self.a **2 

    def perimeter(self): 
        return 4*self.a 


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        self.r = Validation(r)

    def square(self):
        return (self.r **2) * pi

    def perimeter(self):     
        return self.r*pi*2

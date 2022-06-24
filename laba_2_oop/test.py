import main
import unittest
from math import pi



class TriangleSquareTest(unittest.TestCase): 
    def test_triangle_square(self):
        expected = 6.0
        s = main.Triangle(3,4,5).square()
        self.assertEqual(expected, s)

    def test_triangle_perimeter(self):
        expected = 12
        p = main.Triangle(3,4,5).perimeter()
        self.assertEqual(expected, p) 


class ParallelogramTest(unittest.TestCase): 
    def test_parallelogram_square(self):
        expected = 3.9999999999999996
        s = main.Parallelogram(4,2,30).square()
        self.assertEqual(expected, s)

    def test_parallelogram_perimeter(self):
        expected = 18
        p = main.Parallelogram(4,5,60).perimeter()
        self.assertEqual(expected, p)   


class SquareTest(unittest.TestCase): 
    def test_square_square(self):
        expected = 16
        s = main.Square(4).square()
        self.assertEqual(expected, s)

    def test_square_perimeter(self):
        expected = 16
        p = main.Square(4).perimeter()
        self.assertEqual(expected, p)    
  

class RectangleTest(unittest.TestCase): 
    def test_rectangle_square(self):
        expected = 8
        s = main.Rectangle(4,2).square()
        self.assertEqual(expected, s)

    def test_square_perimeter(self):
        expected = 20
        p = main.Rectangle(4,6).perimeter()
        self.assertEqual(expected, p)                 


class CircleTest(unittest.TestCase): 
    def test_circle_square(self):
        expected = pi*5**2
        s = main.Circle(5).square()
        self.assertEqual(expected, s)

    def test_circle_perimeter(self):
        expected = 2*pi*5
        p = main.Circle(5).perimeter()
        self.assertEqual(expected, p)  


class EllipseTest(unittest.TestCase): 
    def test_ellipse_square(self):
        expected = 5*2*pi
        s = main.Ellipse(5,2).square()
        self.assertEqual(expected, s)

    def test_ellipse_perimeter(self):
        expected = 14.279644737231006
        p = main.Ellipse(2,3).perimeter()
        self.assertEqual(expected, p)
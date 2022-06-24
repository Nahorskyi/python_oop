import main
import unittest
from math import pi



class TriangleSquareTest(unittest.TestCase): 
    def test1_triangle_square(self):
        expected = 6.0
        s = main.Triangle(3,4,5).square()
        self.assertEqual(expected, s)
   

    def test_triangle_perimeter(self):
        expected = 12
        p = main.Triangle(3,4,5).perimeter()
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


class ValidationTest(unittest.TestCase):
    def test1_circle_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Circle(-5)
        self.assertTrue("Менше або дорівнює 0", actual)

    def test2_circle_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Circle(0)
        self.assertTrue("Менше або дорівнює 0", actual)   

    def test1_square_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Square(-100)
        self.assertTrue("Менше або дорівнює 0", actual)

    def test2_square_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Square(0)
        self.assertTrue("Менше або дорівнює 0", actual)

    def test1_rectangle_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Rectangle(-5, 7)
        self.assertTrue("Менше або дорівнює 0", actual)

    def test2_rectangle_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Rectangle(0, 7)
        self.assertTrue("Менше або дорівнює 0", actual)

    def test1_triangle_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Triangle(0, 7, 3)
        self.assertTrue("Менше або дорівнює 0", actual)

    def test2_triangle_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Triangle(-10, 7, 3)
        self.assertTrue("Менше або дорівнює 0", actual)        

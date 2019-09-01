""" Michael Ryan
    SSW-567 HW-01
    Triangle Classification
"""

import unittest
import math

def classify_triangle(a,b,c) :
    #if all three sides equal it is Equilateral
    if (a == b == c) :
        return 'Equilateral'
    #if two sides are equal it is Isosceles
    elif ((a==b) or (a==c) or (b==c)) :
        return 'Isosceles'
    #if a^2 + b^2 = c^2 it is Right
    elif ((round(a**2) + round(b**2) == round(c**2))) :
        return 'Right'
    #otherwise scalene
    else :
        return 'Scalene'

class TestTriangles(unittest.TestCase):
    def test_Equilateral(self) :
        """Testing Equilateral Triangle classification"""
        """Testing regular functionality with ideal cases"""
        self.assertEqual(classify_triangle(3,3,3),'Equilateral','3 = 3 = 3 therefore Equilateral')
        """Testing different forms of same number (eg. 3, 3.0, 3.00)"""
        self.assertEqual(classify_triangle(3,3.00,3.0),'Equilateral','3 = 3 = 3 therefore Equilateral')
        """Ensuring that minor changes do not produce bugs (eg. 3,3,2 or 3,3,2.9)"""
        self.assertNotEqual(classify_triangle(3,3,2), 'Equilateral', '3 = 3 != 2 therefore not Equilateral')
        self.assertNotEqual(classify_triangle(3,3,2.99), 'Equilateral', '3 = 3 != 2 therefore not Equilateral')
        self.assertNotEqual(classify_triangle(3,3,3.01), 'Equilateral', '3 = 3 != 2 therefore not Equilateral')
        """Testing negative cases"""
        self.assertNotEqual(classify_triangle(3,3,2),'Equilateral')
        self.assertNotEqual(classify_triangle(3,4,5),'Equilateral')
        self.assertNotEqual(classify_triangle(7,12,15),'Equilateral')

    def test_Scalene(self) :
        """Testing Scalene Triangle Classification"""
        self.assertEqual(classify_triangle(7,12,15),'Scalene','7 != 12 != 15 therefore Scalene')
        """Checking if order of parameters affects result"""
        self.assertEqual(classify_triangle(7,15,12),'Scalene','7 != 12 != 15 therefore Scalene')
        self.assertEqual(classify_triangle(15,12,7),'Scalene','7 != 12 != 15 therefore Scalene')
        """Checking different values for parameters"""
        self.assertEqual(classify_triangle(1,2,3),'Scalene','7 != 12 != 15 therefore Scalene')
        self.assertEqual(classify_triangle(1.01,2.7,7),'Scalene','7 != 12 != 15 therefore Scalene')
        """Checking negative cases"""
        self.assertNotEqual(classify_triangle(3,3,3),'Scalene')
        self.assertNotEqual(classify_triangle(3,3,4),'Scalene')
        self.assertNotEqual(classify_triangle(3,4,5), 'Scalene')

    def test_Isosceles(self):
        """Testing Isosceles Triangle Classification"""
        self.assertEqual(classify_triangle(5,5,4),'Isosceles','5 = 5 != 4 therefore Isosceles')
        """Testing if order of parameters affects result"""
        self.assertEqual(classify_triangle(5,4,5),'Isosceles','5 = 5 != 4 therefore Isosceles')
        self.assertEqual(classify_triangle(4,5,5),'Isosceles','5 = 5 != 4 therefore Isosceles')
        """Checking negative cases"""
        self.assertNotEqual(classify_triangle(3,3,3),'Isosceles')
        self.assertNotEqual(classify_triangle(3,4,5),'Isosceles')
        self.assertNotEqual(classify_triangle(7,12,15),'Isosceles')

    def test_Right(self):
        """Testing Ideal Right Triangle Classification"""
        self.assertEqual(classify_triangle(3,4,5), 'Right', '3^2 + 4^2 == 5^2')
        self.assertEqual(classify_triangle(5,12,13), 'Right', '5^2 + 12^2 == 13^2')
        self.assertEqual(classify_triangle(1,1,math.sqrt(2)), 'Right', 'Right Triangle but also Isosceles')
        """Testing Negative Cases"""
        self.assertNotEqual(classify_triangle(3,3,3),'Right')
        self.assertNotEqual(classify_triangle(7,12,15),'Right')
        self.assertNotEqual(classify_triangle(5,5,4), 'Right')

    def test_Right_NonIdeal(self):
        """Testing non-ideal Right Triangle Classification"""
        self.assertEqual(classify_triangle(5,4,3), 'Right', 'Right Triangle but parameters are not in ascending order')

def main():
    print ("Equilateral : "+classify_triangle(3,3,3))
    print ("Isosceles : "+classify_triangle(5,5,4))
    print("Scalene : "+classify_triangle(7,12,15))
    print("Right : "+classify_triangle(3,4,5))
    unittest.main(exit=False, verbosity = 2)

if __name__ == "__main__" :
    main()

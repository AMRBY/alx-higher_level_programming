#!/usr/bin/python3
"""this is a unitest for the class Base"""
from io import StringIO
import unittest
from models.square import Square
from unittest.mock import patch


class Testrectangle(unittest.TestCase):
    """ Testbase is a class"""



    def test_value(self):
        rec1 = Square(1, 1, 1, 2)
        self.assertEqual(rec1.id, 2)
        self.assertEqual(rec1.width, 1)
        self.assertEqual(rec1.x, 1)
        self.assertEqual(rec1.y, 1)

    def test_exceptions(self):
        rec1 = Square(1)
        with self.assertRaises(ValueError):
            rec1.width = -1    
        with self.assertRaises(TypeError):
            rec1.width = "1"   
        with self.assertRaises(TypeError):
            rec1.width = 1.2   
        with self.assertRaises(ValueError):
            rec1.height = -1   
        with self.assertRaises(TypeError):
            rec1.height = "1"   
        with self.assertRaises(TypeError):
            rec1.height = 1.2  

    def test_area(self):
        rec2 = Square(2)
        self.assertEqual(rec2.area(), 4)
        rec3 = Square(2)
        self.assertEqual(rec2.area(), rec3.area())
        self.assertEqual(rec3.id, rec2.id + 1)

    def test_display(self):
        rec = Square(2, 1)
        with patch('sys.stdout', new=StringIO()) as capture:
            rec.display()
            self.assertEqual(capture.getvalue(), " ##\n ##\n")

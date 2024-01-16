#!/usr/bin/python3
"""this is a unitest for the class Base"""
from io import StringIO
import unittest
from models.base import Base
from unittest.mock import patch


class Testrectangle(unittest.TestCase):
    """ Testbase is a class"""



    def test_value(self):
        """ Testbase is a class"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

#!/usr/bin/python3
""" __main__ module

"""


class BaseGeometry:
    """BaseGeometry is a class, it sort a list"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(self.value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <=0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
""" __main__ module

"""


class BaseGeometry:
    """BaseGeometry is a class, it sort a list"""

    def area(self):
        """area is a class, it sort a list"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer is a class, it sort a list"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle is a class, it sort a list"""

    def __init__(self, width, height):
        """__init__ is a class, it sort a list"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

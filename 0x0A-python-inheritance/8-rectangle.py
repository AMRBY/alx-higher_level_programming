#!/usr/bin/python3
""" __main__ module

"""


class BaseGeometry:
    """BaseGeometry is a class, it sort a list"""

    def area(self):
        """area is a class, it sort a list"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer is a class, it sort a list
        args:
            name: string
            value: inetger"""

        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle is a class, it sort a list"""

    def __init__(self, width, height):
        """__init__ is a class, it sort a list
        args:
            width: integer
            height: integer
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

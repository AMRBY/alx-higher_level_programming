#!/usr/bin/python3
""" __main__ module

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle is a class, it sort a list"""

    def __init__(self, width, height):
        """__init__ is a class, it sort a list
        args:
            width: integer
            height: integer
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

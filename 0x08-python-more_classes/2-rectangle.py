#!/usr/bin/python3
"""this is the __main__ module
to define a class
"""


class Rectangle:
    """this is a Rectangle class"""

    def __init__(self, width=0, height=0):
        """"initiate wen creating an object
        Args:
            width: attribute (int)
            height: attribute (int)"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width is a getter/setter methods"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height is a getter/setter methods"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self._height == 0 or self._width == 0:
            return 0
        else
            return (2 * (self.__height + self.__width))

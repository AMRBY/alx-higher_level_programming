#!/usr/bin/python3
"""A module for square"""


class Square:
    """Square is an empty class
    __init__: method to initialize a parameter
    Attributes:
        __size: __size of the square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass

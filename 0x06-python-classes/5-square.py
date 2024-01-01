#!/usr/bin/python3
"""A module for square"""


class Square:
    """Square is an empty class
    __init__: method to initialize a parameter
    Attributes:
        __size: __size of the square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass

    def area(self):
        """"area is a method to calculate an area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """"my_print is a method to print an area of a square"""
        if self.__size != 0:
            for i in range(self.__size):
                print(self.__size * '#')
        else:
            print('')

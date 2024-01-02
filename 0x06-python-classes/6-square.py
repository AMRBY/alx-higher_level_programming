#!/usr/bin/python3
"""A module for square"""


class Square:
    """Square is an empty class
    __init__: method to initialize a parameter
    Attributes:
        size: size of the square
        position: is a method to positionate an area of a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        pass

    def area(self):
        """"area is a method to calculate an area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """"my_print is a method to print an area of a square"""
        if self.__size != 0:
            print(self.__position[1] * "\n", end="")
            for i in range(self.__size):
                print(self.__position[0] * " ", end="")
                print(self.__size * '#')
        else:
            print('')

    @property
    def position(self):
        """position to locate the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or not all(isinstance(k, int) for k in value)
                or not all(k >= 0 for k in value) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

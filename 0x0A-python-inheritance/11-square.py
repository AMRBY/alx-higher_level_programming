#!/usr/bin/python3
""" __main__ module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is a class, it sort a list"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

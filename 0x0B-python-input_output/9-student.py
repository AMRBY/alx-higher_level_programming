#!/usr/bin/python3
""" this is I/O file functions
"""


class Student:
    """read_file is a function to read a file"""
    def __init__(self, first_name, last_name, age):
        """read_file is a function to read a file
    args:
        first_name: is a filename
        last_name: is a str
        age: is int
    """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """read_file is a function to read a file"""
        return self.__dict__

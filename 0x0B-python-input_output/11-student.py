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

    def to_json(self, attrs=None):
        """read_file is a function to read a file"""
        if (attrs is None):
            return self.__dict__
        else:
            di = {}
            for i in attrs:
                if (i == 'first_name'):
                    di[i] = getattr(self, i)
                if (i == 'last_name'):
                    di[i] = getattr(self, i)
                if (i == 'age'):
                    di[i] = getattr(self, i)
            return di

    def reload_from_json(self, json):
        """read_file is a function to read a file"""
        setattr(self, "first_name", json['first_name'])
        setattr(self, "last_name", json['last_name'])
        setattr(self, "age", json['age'])

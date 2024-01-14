#!/usr/bin/python3
"""this is the base class
"""


class Base:
    """ base is a class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """ i__init__ is a function for initialization
        args:
            id : it's an int"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

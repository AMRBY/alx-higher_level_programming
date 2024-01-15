#!/usr/bin/python3
"""this is the base class
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string is a function for initialization"""
        if list_dictionaries != {} and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file is a function for initialization"""
        for i in list_objs:
            dictionary = i.to_dictionary()
            string = i.to_json_string(dictionary)
            with open(f'{cls.__name__}.json', mode='w', encoding='utf-8') as json_file:
                json_file.write(string)

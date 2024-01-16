#!/usr/bin/python3
"""this is the base class
"""

import json
import os.path


class Base:
    """ base is a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ i__init__ is a function for initialization
        args:
            id : it's an int"""
        if id is not None:
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
        if list_objs is None:
            list_objs = []
        for i in list_objs:
            dictionary = i.to_dictionary()
            string = i.to_json_string(dictionary)
            with open(f'{cls.__name__}.json', mode='w', encoding='utf-8') 
            as json_file:
                json_file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string is a function for initialization"""
        if json_string == "" or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create is a function for initialization"""
        if cls.__name__ == "Square":
            obj = cls(1)
        else:
            obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ load_from_file is a function for initialization"""
        path = os.path.isfile(cls.__name__ + '.json')
        print(path)
        if path is False:
            return []
        else:
            with open(f'{cls.__name__}.json', mode='r', encoding='utf-8')
            as json_file:
                data = cls.from_json_string(json_file.read())
                return [cls.create(**item) for item in data]
                output = json_file.read()

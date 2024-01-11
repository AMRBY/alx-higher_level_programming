#!/usr/bin/python3
""" this is I/O file functions
"""


import json


def save_to_json_file(my_obj, filename):
    """read_file is a function to read a file
    args:
        filename: is a filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)

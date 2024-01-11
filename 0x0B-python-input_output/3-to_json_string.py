#!/usr/bin/python3
""" this is I/O file functions
"""


import json


def to_json_string(my_obj):
    """read_file is a function to read a file
    args:
        filename: is a filename
    """
    return json.dumps(my_obj)

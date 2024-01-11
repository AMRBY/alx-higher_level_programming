#!/usr/bin/python3
""" this is I/O file functions
"""


import json


def from_json_string(my_str):
    """read_file is a function to read a file
    args:
        filename: is a filename
    """
    return json.loads(my_str)

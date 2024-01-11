#!/usr/bin/python3
""" this is I/O file functions
"""


import json


def load_from_json_file(filename):
    """read_file is a function to read a file
    args:
        filename: is a filename
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

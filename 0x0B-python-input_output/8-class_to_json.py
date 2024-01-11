#!/usr/bin/python3
""" this is I/O file functions
"""


def class_to_json(obj):
    """read_file is a function to read a file
    args:
        filename: is a filename
    """
    return obj.__dict__

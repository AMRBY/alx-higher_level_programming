#!/usr/bin/python3
""" this is I/O file functions
"""


def read_file(filename=""):
    """read_file is a function to read a file
    args:
        filename: is a filename
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')

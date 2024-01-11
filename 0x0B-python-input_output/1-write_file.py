#!/usr/bin/python3
""" this is I/O file functions
"""


def write_file(filename="", text=""):
    """read_file is a function to read a file
    args:
        filename: is a filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

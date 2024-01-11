#!/usr/bin/python3
""" this is I/O file functions
"""

import sys


save_to = __import__("5-save_to_json_file").save_to_json_file
load_from = __import__("6-load_from_json_file").load_from_json_file


"""read_file is a function to read a file
    args:
        filename: is a filename
"""
try:
    lista = load_from("add_item.json")
except Exception:
    lista = []


lista.extend(sys.argv[1:])
save_to(lista, "add_item.json")

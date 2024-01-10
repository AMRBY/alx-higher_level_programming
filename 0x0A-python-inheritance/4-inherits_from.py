#!/usr/bin/python3
""" __main__ module

"""


def inherits_from(obj, a_class):
    """print_sorted is a function, it sort a list"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False

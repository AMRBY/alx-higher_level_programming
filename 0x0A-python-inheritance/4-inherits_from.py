#!/usr/bin/python3
""" __main__ module

"""


def inherits_from(obj, a_class):
    """print_sorted is a function, it sort a list"""
    if issubclass(obj, a_class):
        return True
    else:
        return False

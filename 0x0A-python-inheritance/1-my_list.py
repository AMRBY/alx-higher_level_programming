#!/usr/bin/python3
""" __main__ module

"""


class MyList(list):
    """MyList() is a class that returns modules and attributes
        __init__: initialisation method
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """print_sorted is a function, it sort a list"""
        print(sorted(self))

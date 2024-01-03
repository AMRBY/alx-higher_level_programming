#!/usr/bin/python3
"""0-add_integer is a a module to add two inetgers
'a' and 'b' must be inetegr or float
they must be casted to int if float
raise an error if not
return (a + b)"""


def add_integer(a, b=98):
    """add_integer: function to add two integers
    a: first int/float
    b: second int/float"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

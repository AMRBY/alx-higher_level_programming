#!/usr/bin/python3
"""0-add_integer is a a module to add two inetgers
'a' and 'b' must be inetegr or float
they must be casted to int if float
raise an error if not
return (a + b)"""


def matrix_divided(matrix, div):
    """matrix_divided: function to divide matrix by an integer
    div: first int/float
    matrix: matrix of int/float"""
    if type(div) not in ["int","float"]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix[]:
        if type(matrix[i]) not in ["int","float"]:
    else:
        return int(a) + int(b)

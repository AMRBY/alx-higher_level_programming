#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in range(0, 3):
        c = []
        for x in matrix[i]:
            c.append(x*x)
        mat.append(c)
    return mat

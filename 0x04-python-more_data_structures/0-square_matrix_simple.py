#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in range(len(matrix)):
        c = []
        for x in matrix[i]:
            c.append(x*x)
        mat.append(c)
    return mat

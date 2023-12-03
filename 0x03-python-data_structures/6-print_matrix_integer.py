#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    else:
        for j in range(0, 3):
            for i in matrix[j]:
                if i in [3, 6, 9]:
                    print("{}".format(i))
                else:
                    print("{}".format(i), end=' ')

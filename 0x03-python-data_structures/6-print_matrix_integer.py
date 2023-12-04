#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    else:
        for j in range(0, 3):
            for i in range(0, 3):
                if i == 2:
                    print("{}".format(matrix[j][i]))
                else:
                    print("{}".format(matrix[j][i]), end=' ')

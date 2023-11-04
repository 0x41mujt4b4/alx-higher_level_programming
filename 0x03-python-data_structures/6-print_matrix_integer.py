#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not any(matrix):
        print()
    outer_len = len(matrix)
    i = j = 0
    for i in range(outer_len):
        inner_len = len(matrix[i])
        for j in range(inner_len):
            if j != inner_len - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]))

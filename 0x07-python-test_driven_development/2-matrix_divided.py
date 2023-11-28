#!/usr/bin/python3

def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix:
        row_size = len(matrix[0])
    new_matrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        if len(matrix[i]) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(row_size):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return new_matrix

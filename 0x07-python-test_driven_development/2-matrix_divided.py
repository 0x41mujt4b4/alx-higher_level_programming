#!/usr/bin/python3
"""Define matrix_divided module"""


def matrix_divided(matrix, div):
    """Returns elements of matrix divided by div"""
    if not all(matrix):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/floats")
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

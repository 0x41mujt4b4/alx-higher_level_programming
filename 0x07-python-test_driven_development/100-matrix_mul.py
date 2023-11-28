#!/usr/bin/python3
"""Defines module that multiply two matrix"""

def matrix_mul(m_a, m_b):
    """Returns a new matrix m_a * m_b"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        for el in row:
            if type(el) is not int and type(el) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        for el in row:
            if type(el) is not int and type(el) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if not all(m_a):
        raise ValueError("m_a can't be empty")
    if not all(m_b):
        raise ValueError("m_b can't be empty")
    m_a_row_size = len(m_a[0])
    for row in m_a:
        if len(row) != m_a_row_size:
            raise TypeError("each row of m_a must be of the same size")
    m_b_row_size = len(m_b[0])
    for row in m_b:
        if len(row) != m_b_row_size:
            raise TypeError("each row of m_b must be of the same size")

    a_rows = len(m_a)
    a_cols = len(m_a[0])
    b_rows = len(m_b)
    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(a_rows)]
    for i in range(a_rows):
        for j in range(len(m_b[0])):
            for k in range(a_cols):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

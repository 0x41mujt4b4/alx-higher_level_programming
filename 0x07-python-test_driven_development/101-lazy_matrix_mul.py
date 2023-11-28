#!/usr/bin/python3
"""Define matrix multiplication using numpy module"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns matrix m_a * m_b using numpy"""
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
    
    m_a = np.array(m_a)
    m_b = np.array(m_b)

    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.matmul(m_a, m_b)

    return result.tolist()

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = a2 = b1 = b2 = 0
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            a1 = b1 = 0
        else:
            a1 = tuple_a[0]
            b1 = 0
    else:
        a1 = tuple_a[0]
        b1 = tuple_a[1]
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            a2 = b2 = 0
        else:
            a2 = tuple_b[0]
            b2 = 0
    else:
        a2 = tuple_b[0]
        b2 = tuple_b[1]
    return a1+a2, b1+b2

#!/usr/bin/python3
"""module that has one function"""


def add_attribute(obj, attr, value):
    """function that adds attr to obj if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

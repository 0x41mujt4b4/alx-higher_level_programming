#!/usr/bin/python3
"""Module that contain one function"""


def read_file(filename=""):
    """function to read a file"""
    with open(filename, 'r') as file:
        file.read()

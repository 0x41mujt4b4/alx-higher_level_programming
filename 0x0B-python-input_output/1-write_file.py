#!/usr/bin/python3
"""Module that contain one function"""


def write_file(filename="", text=""):
    """function to write to file"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)

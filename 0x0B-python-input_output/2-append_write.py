#!/usr/bin/python3
"""Module that contain one function"""


def append_write(filename="", text=""):
    """function to append to file"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)

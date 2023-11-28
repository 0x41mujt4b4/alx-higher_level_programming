#!/usr/bin/python3
"""Define text_indentation module"""


def text_indentation(text):
    """prints lines of text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for c in text:
        line += c
        if c in ".?:":
            print(line.strip())
            print()
            line = ""
    print(line.strip(), end="")

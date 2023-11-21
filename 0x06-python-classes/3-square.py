#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that represent a square"""
    def __init__(self, size=0):
        """initialize the class instance"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """A method that return square object area"""
        return self.__size * self.__size

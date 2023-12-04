#!/usr/bin/python3
"""Models contain Square class inherted from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class that represent a square"""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

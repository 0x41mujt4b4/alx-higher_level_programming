#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the class instance"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

    def area(self):
        """A method that return square object area"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                if self.__position[1] <= 0:
                    print(' ' * self.__position[0], end='')
                print('#' * self.size)

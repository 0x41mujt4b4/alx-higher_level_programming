#!/usr/bin/python3
"""module that contain MyInt class"""


class MyInt(int):
    """MyInt class that represent int"""
    def __eq__(self, other):
        return int(self) != int(other)
    def __ne__(self, other):
        return int(self) == int(other)

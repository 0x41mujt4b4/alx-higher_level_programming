#!/usr/bin/python3
"""Defines MyList module"""


class MyList(list):
    """Defines MyList class"""
    def print_sorted(self):
        print(sorted(self))

#!/usr/bin/python3
"""Defines max_integer test module"""
import unittest
from importlib import import_module
max_integer = import_module("6-max_integer").max_integer


class Test_MaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -3]), -1)

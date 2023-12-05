#!/usr/bin/python3
"""Module that contain one function"""
import json


def from_json_string(my_str):
    """function to convert json string to obj"""
    return json.loads(my_str)

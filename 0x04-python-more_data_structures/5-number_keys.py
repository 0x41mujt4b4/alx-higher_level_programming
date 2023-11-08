#!/usr/bin/python3
def number_keys(a_dictionary):
    if not a_dictionary:
        return 0
    return sum(a_dictionary.keys())

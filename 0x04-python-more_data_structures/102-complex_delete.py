#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = a_dictionary.keys()
    new_d = a_dictionary.copy()
    for key in keys:
        if a_dictionary[key] == value:
            del new_d[key]
    return new_d

#!/usr/bin/python3
def uppercase(str):
    result = ""
    for s in str:
        if (97 <= ord(s) <= 122):
            result += chr(ord(s) - 97 + 65)
        else:
            result += s
    return result

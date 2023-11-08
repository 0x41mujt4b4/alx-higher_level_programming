#!/usr/bin/python3
def romat_to_int(roman_string):
    roman = {'M': 1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    result = 0
    lens = len(s)
    for i in range(lens):
        if i+1 < lens and roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]
    return result

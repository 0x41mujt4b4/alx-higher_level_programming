#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    lens = len(roman_string)
    for i in range(lens):
        if i+1 < lens and roman[roman_string[i]] < roman[roman_string[i+1]]:
            result -= roman[roman_string[i]]
        else:
            result += roman[roman_string[i]]
    return result

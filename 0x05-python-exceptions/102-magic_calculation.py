#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b // i
        except:
            b += a
            break
    return result
print(magic_calculation(0, 1))

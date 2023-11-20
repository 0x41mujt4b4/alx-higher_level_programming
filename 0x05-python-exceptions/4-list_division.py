#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    element = 0
    for i in range(list_length):
        try:
            element = my_list_1[i] / my_list_2[i]
        except TypeError:
            element = 0
            print('wrong type')
        except ZeroDivisionError:
            element = 0
            print('division by 0')
        except IndexError:
            element = 0
            print('out of range')
        finally:
            result.append(element)
    return result

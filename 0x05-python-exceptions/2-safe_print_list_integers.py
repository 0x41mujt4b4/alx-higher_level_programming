#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            pass
        finally:
            i += 1
    print()
    return counter

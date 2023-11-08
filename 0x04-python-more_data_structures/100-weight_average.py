#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_wx = 0
    sum_w = 0
    if not my_list:
        return 0
    for tup in my_list:
        sum_wx += (tup[0] * tup[1])
        sum_w += tup[1]
    return sum_wx / sum_w

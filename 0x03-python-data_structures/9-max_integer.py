def max_integer(my_list=[]):
    if not my_list:
        return None
    max_int = float('-inf')
    for i in my_list:
        if i > max_int:
            max_int = i
    return max_int

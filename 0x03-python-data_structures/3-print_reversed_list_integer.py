def print_reversed_list_integer(my_list=[]):
    l = len(my_list) - 1
    for i in range(l, -1, -1):
        print("{}".format(my_list[i]))

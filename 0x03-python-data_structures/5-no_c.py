def no_c(my_string):
    result = ""
    for c in my_string:
        if c not in "cC":
            result += c
    return result

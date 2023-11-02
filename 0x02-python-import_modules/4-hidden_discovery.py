#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    d = vars(hidden_4)
    for key in d:
        if key[:2] != '__':
            print("{}".format(key))

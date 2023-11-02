#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    argc = len(argv) - 1
    if (not argc):
        print("0 arguments.")
    else:
        print("{} arguments:".format(argc))
        for i in range(1, argc+1):
            print("{}: {}".format(i, argv[i]))

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv
    len_arg = len(arg) - 1
    if len_arg == 0:
        print("{:d} arguments.".format(len_arg))
    elif len_arg == 1:
        print("{:d} argument:".format(len_arg))
        print("{0:d}: {1}".format(len_arg, arg[1]))
    else:
        print("{:d} arguments:".format(len_arg))
        for i in range(1, len_arg + 1):
            print("{0:d}: {1}".format(i, arg[i]))
else:
    exit()

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv
    arg_len = len(arg)
    sum = 0
    for i in range(1, arg_len):
        sum += int(arg[i])
    print("{}".format(sum))
else:
    exit()

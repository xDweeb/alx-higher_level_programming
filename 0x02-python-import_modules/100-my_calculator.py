#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    arg = sys.argv
    arg_len = len(sys.argv)
    if arg_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(arg[1])
    b = int(arg[3])
    if arg[2] == "+":
        print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
        exit(0)
    elif arg[2] == "-":
        print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
        exit(0)
    elif arg[2] == "*":
        print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
        exit(0)
    elif arg[2] == "/":
        print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
else:
    exit()

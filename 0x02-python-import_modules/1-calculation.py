#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    a = 10
    b = 5
    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
    print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
    print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
    print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))

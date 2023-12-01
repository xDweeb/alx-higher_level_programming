#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)
    if (length == 0):
        return ("None")
    maxi = my_list[0]
    for i in range(1, length):
        if my_list[i] > maxi:
            maxi = my_list[i]
    return (maxi)

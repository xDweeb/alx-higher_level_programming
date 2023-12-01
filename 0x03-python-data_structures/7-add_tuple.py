#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    add_tuple = [0, 0]
    if (len(tuple_a) == 0 and len(tuple_b) == 0):
        add_tuple[0] = 0
    elif (len(tuple_a) == 0):
        add_tuple[0] = 0 + tuple_b[0]
    elif (len(tuple_b) == 0):
        add_tuple[0] = tuple_a[0] + 0
    else:
        add_tuple[0] = tuple_a[0] + tuple_b[0]

    if (len(tuple_a) <= 1 and len(tuple_b) <= 1):
        add_tuple[1] = 0
    elif (len(tuple_a) <= 1):
        add_tuple[1] = 0 + tuple_b[1]
    elif (len(tuple_b) <= 1):
        add_tuple[1] = tuple_a[1] + 0
    else:
        add_tuple[1] = tuple_a[1] + tuple_b[1]

    return (tuple(add_tuple))

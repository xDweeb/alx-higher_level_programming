#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        length = len(row)
        for i in range(length):
            print("{:d}".format(row[i]), end='')
            if i < length - 1:
                print("{}".format(" "), end='')
        print()

#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)

    for i in range(len(names)):
        if names[i][:2] != "__":
            print(names[i])
else:
    exit()

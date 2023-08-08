#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            ch = ord(c) - 32
        else:
            ch = ord(c)
        print("{:c}".format(ch), end='')
    print("")

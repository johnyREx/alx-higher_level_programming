#!/usr/bin/python3
def add_infinite(args):
    sum = 0
    for i in range(1, len(args)):
        sum = sum + int(args[i])
    print("{:d}".format(sum))


if __name__ == '__main__':
    import sys

    add_infinite(sys.argv)

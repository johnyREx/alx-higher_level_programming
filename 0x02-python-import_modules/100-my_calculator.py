#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calc(args):
    num_args = len(args)
    if num_args != 4:
        print("{}{}{}".format("Usage: ", args[0], " <a> <operator> <b>"))
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])
    if args[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif args[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif args[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif args[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("{}".format("Unknown operator. Available operators: +, -, * "
                          "and /"))
        sys.exit(1)


if __name__ == '__main__':
    import sys

    calc(sys.argv)

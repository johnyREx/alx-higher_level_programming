#!/usr/bin/python3
def print_arg(args):
    num_args = len(args)
    if num_args == 1:
        print("{:d} arguments.".format(num_args - 1))
    else:
        print("{:d}".format(num_args - 1), end=' ')
        print("{}:".format("argument" if num_args - 1 == 1 else "arguments"))
        for i in range(1, num_args):
            print("{:d}: {}".format(i, args[i]))


if __name__ == '__main__':
    import sys

    print_arg(sys.argv)

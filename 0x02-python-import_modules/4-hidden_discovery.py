#!/usr/bin/python3
import hidden_4


def print_defined():
    defined = dir(hidden_4)
    final = []
    for w in defined:
        if w[0] == '_':
            continue
        else:
            final.append(w)
    final.sort()
    for w in final:
        print("{}".format(w))


if __name__ == '__main__':
    print_defined()

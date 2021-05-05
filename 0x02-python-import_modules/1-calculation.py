#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    sym = ['+', '-', '*', '/']
    ops = {0: add, 1: sub, 2: mul, 3: div}
    for i in ops:
        print('{:d} {:} {:d} = {:d}'.format(a, sym[i], b, ops[i](a, b)))

if __name__ == "__main__":
    main()

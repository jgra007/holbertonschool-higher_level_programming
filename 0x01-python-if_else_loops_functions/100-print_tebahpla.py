#!/usr/bin/python3
reversed_range = range(122, 96, -1)
for c in reversed_range:
    if c % 2 != 0:
        c = c - 32
    print("{:c}".format(c), end='')

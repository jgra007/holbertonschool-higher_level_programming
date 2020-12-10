#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    l = len(sys.argv)
    print('{:d} argument{:}'.format(l - 1, '.' if l == 1 else
                                    (':' if l == 2 else 's:')))
    i = 1
    for arg in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[arg]))
        i += 1

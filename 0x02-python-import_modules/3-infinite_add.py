#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    if len(sys.argv) == 1:
        print(0)
    elif len(sys.argv) == 2:
        print(sys.argv)
    else:
        sum = 0
        for x in range(1, len(sys.argv)):
            a = int(sys.argv[x])
            sum += a
        print(sum)

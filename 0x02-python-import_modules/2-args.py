#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    if(len(sys.argv[1:])) == 0:
        print("{} arguments.".format(len(sys.argv[1:])))
    elif(len(sys.argv[1:])) == 1:
        print("1 argument")
        print("1: {}".format(sys.argv[1:]))
    else:
        print("{} arguments:".format(len(sys.argv[1:])))
        for x in range(1, len(sys.argv[1:])):
            print("{}: {}".format(x, sys.argv[x]))
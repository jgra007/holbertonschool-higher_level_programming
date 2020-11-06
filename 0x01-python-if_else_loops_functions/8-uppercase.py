#!/usr/bin/python3
def uppsercase(str):
    for i in str:
        i = ord(i)
        if i >= ord(i) and i <= 122:
            i = i - 32
        print("{:c}".format(i), end='')
    print()

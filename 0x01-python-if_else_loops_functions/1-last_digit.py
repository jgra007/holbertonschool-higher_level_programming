#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    n = number % 10
else:
    n = (-number % 10)*-1

print("Last digit of", end=' ')
if n > 5:
    print("{:d} is {:d} and is greater than 5".format(number, n))
if n == 0:
    print("{:d} is {:d} and is 0".format(number, n))
if n < 6 and n != 0:
    print("{:d} is {:d} and is less than 6 and not 0".format(number, n))

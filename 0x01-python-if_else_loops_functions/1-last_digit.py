#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    number2 = number % 10
else:
    number2 = (-number % 10) * -1
print("Last digit of", end=' ')
if number2 > 5:
    print("{:d} is {:d} and is greater than 5".format(number, number2))
if number2 < 6 and number2 != 0:
    print("{:d} is {:d} and is less than 6 and not 0".format(number, number2))
if number2 == 0:
    print("{:d} is {:d} adn is 0".format(number, number2))

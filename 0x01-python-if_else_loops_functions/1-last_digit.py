#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

remainder = number % 10

if (number < 0):
    remainder = (number * -1) % 10
    remainder = remainder * -1
if (remainder > 5):
    print("Last digit of {} is {} \
and is greater than 5".format(number, remainder))

elif ((remainder < 6) and (remainder != 0)):
    print("Last digit of {} is {} \
and is less than 6 and not 0" .format(number, remainder))

else:
    print("Last digit of {} is {} and is 0" .format(number, remainder))

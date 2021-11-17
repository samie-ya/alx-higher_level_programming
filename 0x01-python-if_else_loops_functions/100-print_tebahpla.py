#!/usr/bin/python3

i = 122
new = 0
while (i >= 97):
    if (i % 2 != 0):
        new = i - 32
    else:
        new = i
    print("{:c}".format(new), end="")
    i -= 1

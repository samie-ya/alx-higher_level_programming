#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    total = 0
    if (len(sys.argv) >= 3):
        for i in range(1, len(sys.argv)):
            a = int(sys.argv[i])
            total += a
        print("{:d}".format(total))
    elif (len(sys.argv) == 2):
        print("{:d}".format(int(sys.argv[1])))
    else:
        print("0")

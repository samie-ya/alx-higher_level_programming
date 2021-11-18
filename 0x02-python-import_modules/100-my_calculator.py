#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    import calculator_1 as calc

    if (len(sys.argv) < 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = sys.argv[1]
        operator = sys.argv[2]
        b = sys.argv[3]
        if (operator == "+"):
            print("{:s} + {:s} = {:d}".format(a, b, calc.add(int(a), int(b))))
        elif (operator == "-"):
            print("{:s} - {:s} = {:d}".format(a, b, calc.sub(int(a), int(b))))
        elif (operator == "*"):
            print("{:s} * {:s} = {:d}".format(a, b, calc.mul(int(a), int(b))))
        elif (operator == "/"):
            print("{:s} / {:s} = {:d}".format(a, b, calc.div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

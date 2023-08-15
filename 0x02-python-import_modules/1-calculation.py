#!/usr/bin/python3

def main():
    """Perform arithmetic operations on two integers."""
    from calculator_1 import add, sub, mul, div

    num1 = 10
    num2 = 5

    print("{0} + {1} = {2}".format(num1, num2, add(num1, num2)))
    print("{0} - {1} = {2}".format(num1, num2, sub(num1, num2)))
    print("{0} * {1} = {2}".format(num1, num2, mul(num1, num2)))
    print("{0} / {1} = {2}".format(num1, num2, div(num1, num2)))

if __name__ == "__main__":
    main()

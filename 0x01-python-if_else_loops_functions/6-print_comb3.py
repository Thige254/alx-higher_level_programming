#!/usr/bin/python3
for number in range(10):
    for y in range(number + 1, 10):
        if number == 8 and y == 9:
            print("{}{}".format(number, y))
        else:
            print("{}{}".format(number, y), end=", ")

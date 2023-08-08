#!/usr/bin/python3
for number in range(0, 26):
    if number % 2 == 0:
        print("{}".format(chr(122 - number)), end="")
    else:
        print("{}".format(chr(90 - number)), end="")

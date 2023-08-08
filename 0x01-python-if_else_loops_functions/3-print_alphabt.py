#!/usr/bin/python3
for number in range(26):
    if number != 4 and number != 16:
        print("{}".format(chr(97 + number)), end="")

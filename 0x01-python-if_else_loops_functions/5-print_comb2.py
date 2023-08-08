#!/usr/bin/python3
print(*(f"{number:02d}" for number in range(100)), sep=", ")

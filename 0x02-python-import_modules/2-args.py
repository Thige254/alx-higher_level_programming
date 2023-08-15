#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the number of arguments and list them."""

    args_count = len(sys.argv) - 1

    if args_count == 1:
        print("{} argument:".format(args_count))
    else:
        print("{} arguments:".format(args_count)
              if args_count != 0 else "{} arguments.".format(args_count))

    for idx, arg in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(idx, arg))

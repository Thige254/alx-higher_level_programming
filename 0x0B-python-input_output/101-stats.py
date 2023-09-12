#!/usr/bin/python3
"""
This module reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
the module prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0


def print_stats():
    """Prints statistics of status codes and file size."""
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        split_line = line.split()
        size = split_line[-1]
        status = split_line[-2]
        total_size += int(size)

        if status in status_codes:
            status_codes[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass
finally:
    print_stats()

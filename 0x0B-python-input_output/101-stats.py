#!/usr/bin/python3
import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

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
            print("File size: {}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value > 0:
                    print("{}: {}".format(key, value))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))

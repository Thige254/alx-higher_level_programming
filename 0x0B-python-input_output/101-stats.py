#!/usr/bin/python3
"""Computes and prints metrics from standard input."""

def print_stats(size, status_codes):
    """Print metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    line_count = 0
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            line_parts = line.split()
            total_size += int(line_parts[-1])
            if line_parts[-2] in status_codes:
                status_codes[line_parts[-2]] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)

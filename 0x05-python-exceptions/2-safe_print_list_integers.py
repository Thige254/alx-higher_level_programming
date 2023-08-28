#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    in_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            in_print += 1
        except IndexError:
            raise
        except (ValueError, TypeError):
            continue
    print()
    return in_print

#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    for item in my_list:
        if elements_printed < x:
            print(item, end="")
            elements_printed += 1
        else:
            break
    print()
    return elements_printed

#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        print("{}".format(i))

if __name__ == "__main__":
    # Testing the function above
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [p if p != search else replace for p in my_list]

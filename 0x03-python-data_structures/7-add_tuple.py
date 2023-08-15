#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    def get_tuple_value(t, index):
        return t[index] if index < len(t) else 0

    return (get_tuple_value(tuple_a, 0) + get_tuple_value(tuple_b, 0),
            get_tuple_value(tuple_a, 1) + get_tuple_value(tuple_b, 1))

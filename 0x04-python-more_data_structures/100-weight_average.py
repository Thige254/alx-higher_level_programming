#!/usr/bin/python3

def weight_average(data=[]):
    if not data or not all(isinstance(t, tuple) and
                           len(t) == 2 and isinstance(t[0], int) and
                           isinstance(t[1], int) for t in data):
        return 0

    weighted_sum = 0
    total_weights = 0

    for score, weight in data:
        weighted_sum += score * weight
        total_weights += weight

    return weighted_sum / total_weights

#!/usr/bin/python3

def compute_difference(values):
    max_val = max(values)
    return max_val - sum(val for val in values if val != max_val)

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    current_values = [0]

    for char in roman_string:
        if char not in roman_numerals:  # Ensuring every character is a valid Roman numeral
            return 0
        if roman_numerals[char] > max(current_values):
            total += compute_difference(current_values)
            current_values = [roman_numerals[char]]
        else:
            current_values.append(roman_numerals[char])

    total += compute_difference(current_values)

    return total

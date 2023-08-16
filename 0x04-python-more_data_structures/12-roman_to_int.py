def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for symbol in roman_string:
        current_value = roman_numerals[symbol]
        
        if prev_value and prev_value < current_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        
        prev_value = current_value

    return total

#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    function that converts a roman numeral to an integer.
    """
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    roman_list = list(roman_string.upper())
    result = 0
    previous = 0
    for letter in roman_list:
        if letter in roman_dict:
            result += roman_dict[letter]
            if roman_dict[letter] > previous:
                result -= previous * 2
            previous = roman_dict[letter]
        else:
            return (0)
    return result

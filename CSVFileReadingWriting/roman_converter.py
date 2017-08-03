ROMAN_NUMERAL_TABLE = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                       ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9),
                       ("V", 5), ("IV", 4), ("I", 1)]

def convert_to_roman(number):
    """ Convert an integer to Roman >>> print(convert_to_roman(45)) XLV """
    roman_numerals = []
    for numeral, value in ROMAN_NUMERAL_TABLE:
        while value <= number:
            number -= value
            roman_numerals.append(numeral)

    return ''.join(roman_numerals)